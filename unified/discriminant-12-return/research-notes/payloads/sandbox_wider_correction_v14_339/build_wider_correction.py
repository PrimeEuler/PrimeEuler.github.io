#!/usr/bin/env python3
"""Sandbox wider finite correction candidate (ledger v14.339 handoff).

delta_y(n) = floor_160(r_point(n) / midpoint(log_normalized(n, 128)))
on the 264192 evaluated rows per sector (256000 Middle + 8192 Far window
residual points frozen by v14.337), zero elsewhere. The patch is added to
the existing trial; on this support the refined Near trial coincides with
the original infinite seed (Near support is disjoint, below b).

Candidate construction only: no contraction or acceptance claim. Using a
point residual to choose a represented trial does not imply the point is
the exact physical residual (v14.339).

Conventions mirror Lane A's suzuki_near_trial_lift_rhs.py exactly:
  floor(q, bits) = q.numerator * (1 << bits) // q.denominator
  midpoint(log_normalized(n, 128)) = (lo + hi) / 2
  sqrt_upper(q, 192) as in suzuki_exact_integer_source_action.py
  buffer: signed little-endian, width = (max_bit_length + 8) // 8
"""
import json, hashlib, random, sys
from pathlib import Path
from fractions import Fraction as F
from math import isqrt

sys.path.insert(0, '/home/hatch/workspace/d12/laneA_modules')
from suzuki_certified_remote_diagonal import log_normalized

ROOT = Path('/home/hatch/workspace/d12/wider339')
INPUTS = ROOT / 'inputs' / 'residual_v14_337'
V300 = Path('/home/hatch/workspace/d12/refined_far/payloads/'
            'refined_near_trial_and_lift_v14_300')
OUT = ROOT / 'out'

PUBLISHED = {  # v14.337 durable witnesses
    'even-v-middle-residual.bin': '23dd9720663a508fa3524fce54def7db2f26ffcece4cedcd0e9d464ae561034a',
    'odd-v-middle-residual.bin': '6faa38f0df2f9bbaf046e0bf9c12f4933cee366a5268eaa8d7955ad58282f969',
    'even-v-far-window-residual.bin': 'd6882a889d68eae17d7753f227d91b94285a17de362c7e6dbe7de7903b9da29f',
    'odd-v-far-window-residual.bin': 'b52cb5b2595afdca74a5ee983606d30d2f2e133d29dae507af8bd44ad8037f65',
    'returned-tail-residual-even-v.json': '6678d9e273b3443c73f5ae54c1013fb237760bdcc3b9b0bcb037a81ae6e13ff0',
    'returned-tail-residual-odd-v.json': '26018181533bbdf383f001c59c547b0169e19e018cd1a0c5450576007dadfcc7',
}
CASES = {
    'even-v': dict(first=512001, far_first=1024001,
                   trial_upper='35473819604309927988660210050899722403958792260028391980463568215847636358263/226156424291633194186662080095093570025917938800079226639565593765455331328000000'),
    'odd-v': dict(first=512002, far_first=1024002,
                  trial_upper='141883060497659555101114183757359539412325992676403566513582136695460955198677/904625697166532776746648320380374280103671755200316906558262375061821325312000000'),
}


def digest(b):
    return hashlib.sha256(b).hexdigest()


def floor_bits(q, bits):
    return q.numerator * (1 << bits) // q.denominator


def sqrt_upper(q, bits=192):
    assert q >= 0
    numerator = q.numerator << (2 * bits)
    r = isqrt(numerator // q.denominator)
    if r * r * q.denominator < numerator:
        r += 1
    out = F(r, 1 << bits)
    assert out * out >= q
    return out


def read_ints(path, width, count):
    raw = path.read_bytes()
    assert len(raw) == width * count and digest(raw) == PUBLISHED[path.name]
    return [int.from_bytes(raw[i:i + width], 'little', signed=True)
            for i in range(0, len(raw), width)]


def writebuffer(root, sector, name, values, bits):
    width = max(1, (max(abs(x).bit_length() for x in values) + 8) // 8)
    raw = b''.join(x.to_bytes(width, 'little', signed=True) for x in values)
    filename = f'{sector}-{name}.bin'
    (root / filename).write_bytes(raw)
    return {'file': filename, 'bits': bits, 'width': width,
            'count': len(values), 'bytes': len(raw), 'sha256': digest(raw)}


def run(sector):
    cfg = CASES[sector]
    mints = read_ints(INPUTS / f'{sector}-middle-residual.bin', 30, 256000)
    fints = read_ints(INPUTS / f'{sector}-far-window-residual.bin', 30, 8192)
    rows = ([(cfg['first'] + 2 * i, r) for i, r in enumerate(mints)]
            + [(cfg['far_first'] + 2 * i, r) for i, r in enumerate(fints)])
    assert len(rows) == 264192
    assert rows[0][0] == cfg['first']
    assert rows[-1][0] == cfg['first'] + 2 * (264192 - 1)
    assert rows[256000][0] == rows[255999][0] + 2 == cfg['far_first']

    deltas = []
    minlog, maxlog = None, F(0)
    for idx, (n, r_int) in enumerate(rows):
        lo, hi = log_normalized(n, 128)
        logpoint = (lo + hi) / 2
        assert logpoint > 11
        minlog = logpoint if minlog is None else min(minlog, logpoint)
        maxlog = max(maxlog, logpoint)
        deltas.append(floor_bits(F(r_int, 1 << 256) / logpoint, 160))
        if (idx + 1) % 66048 == 0:
            print(sector, idx + 1, '/', len(rows), flush=True)

    # Independent verification on samples: integer-only path + quantum bound.
    rng = random.Random(20261013)
    sample_idx = sorted({0, 1, 255999, 256000, 264190, 264191}
                        | set(rng.sample(range(264192), 58)))
    for idx in sample_idx:
        n, r_int = rows[idx]
        lo, hi = log_normalized(n, 128)
        logpoint = (lo + hi) / 2
        alt = (r_int * logpoint.denominator) // (logpoint.numerator * (1 << 96))
        assert alt == deltas[idx]
        resid = F(r_int, 1 << 256) - F(deltas[idx], 1 << 160) * logpoint
        assert F(0) <= resid < logpoint * F(1, 1 << 160)

    sumsq = sum(d * d for d in deltas)
    l1int = sum(abs(d) for d in deltas)
    norm2 = F(sumsq, 1 << 320)
    nupper = sqrt_upper(norm2, 192)
    l1 = F(l1int, 1 << 160)
    trial_upper = F(cfg['trial_upper'])
    whole_upper = trial_upper + nupper

    OUT.mkdir(parents=True, exist_ok=True)
    buf = writebuffer(OUT, sector, 'wider-correction', deltas, 160)
    raw2 = (OUT / buf['file']).read_bytes()
    back = [int.from_bytes(raw2[i:i + buf['width']], 'little', signed=True)
            for i in range(0, len(raw2), buf['width'])]
    assert back == deltas and sum(d * d for d in back) == sumsq

    v300cert = (V300 / f'near-seed-refinement-{sector}.json').read_bytes()
    cert = {
        'schema': 'cone.sandbox-wider-correction-candidate.v1',
        'sector': sector,
        'task': 'v14.339 HANDOFF - Sandbox: evaluated wider finite correction candidate',
        'definition': 'delta_y(n)=floor_160(r_point(n)/midpoint(log_normalized(n,128))) '
                      'on the evaluated rows; zero elsewhere',
        'support': {
            'first_mode': cfg['first'], 'last_mode': rows[-1][0], 'step': 2,
            'count': 264192,
            'segments': [
                {'source': 'v14.337 Middle residual', 'rows': 256000,
                 'first_mode': cfg['first'], 'last_mode': rows[255999][0]},
                {'source': 'v14.337 Far-window residual', 'rows': 8192,
                 'first_mode': cfg['far_first'], 'last_mode': rows[-1][0]}]},
        'base_trial': 'patch added to the existing trial; on this support the '
                      'refined Near trial coincides with the original infinite '
                      'seed (Near support is disjoint, below b); nothing outside '
                      'the support changes',
        'inputs': {
            'residual_namespace': 'research-notes/payloads/returned_tail_residual_composition_v14_337/',
            'middle_residual_buffer_sha256': PUBLISHED[f'{sector}-middle-residual.bin'],
            'far_window_residual_buffer_sha256': PUBLISHED[f'{sector}-far-window-residual.bin'],
            'composition_certificate_sha256': PUBLISHED[f'returned-tail-residual-{sector}.json'],
            'log_normalized_module': 'suzuki_certified_remote_diagonal.py (byte-identical to repository copy)',
            'log_normalized_module_sha256': digest(Path(
                '/home/hatch/workspace/d12/laneA_modules/suzuki_certified_remote_diagonal.py').read_bytes()),
            'v14_300_trial_certificate': f'refined_near_trial_and_lift_v14_300/near-seed-refinement-{sector}.json',
            'v14_300_trial_certificate_sha256': digest(v300cert)},
        'buffer': buf,
        'rational': {
            'correction_norm_squared': str(norm2),
            'correction_norm_upper': str(nupper),
            'correction_l1': str(l1),
            'base_trial_norm_upper_v14_300': str(trial_upper),
            'whole_trial_norm_upper_triangle': str(whole_upper)},
        'display_approximate': {
            'correction_norm_upper': float(nupper),
            'correction_l1': float(l1),
            'base_trial_norm_upper_v14_300': float(trial_upper),
            'whole_trial_norm_upper_triangle': float(whole_upper)},
        'domain_justification': 'delta_y is finitely supported (264192 modes) with '
                                'dyadic-rational values; finitely supported sequences '
                                'lie in the operator domain and in every weighted l2 '
                                'space of the framework, and the domain is a vector '
                                'space containing them, so adding delta_y to the '
                                'existing domain-admissible trial (v14.300) keeps the '
                                'sum domain-admissible. (Dy)_n for a finitely supported '
                                'correction is a finite sum at every row.',
        'verification': {
            'sample_rows_checked': len(sample_idx),
            'integer_path_agrees_on_samples': True,
            'one_quantum_bound_on_samples': '0 <= r_point - delta_y*logpoint < logpoint * 2^-160',
            'buffer_round_trip_recomputed': True,
            'all_logpoints_gt_11': True,
            'logpoint_min': str(minlog), 'logpoint_max': str(maxlog)},
        'candidate_only': True,
        'contraction_claimed': False,
        'lambda_inverse_equals_schur_inverse_claimed': False,
        'new_residual_evaluated': False,
        'stationary_acceptance_met': False,
        'infinite_capacity_tail_closed': False,
    }
    (OUT / f'wider-correction-{sector}.json').write_text(
        json.dumps(cert, indent=2, sort_keys=True) + '\n')
    print(sector, 'done: norm_upper', float(nupper), 'l1', float(l1),
          'whole_trial_upper', float(whole_upper), 'width', buf['width'],
          'bytes', buf['bytes'], flush=True)
    return cert


if __name__ == '__main__':
    for s in ('even-v', 'odd-v'):
        run(s)
