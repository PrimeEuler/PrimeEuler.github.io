#!/usr/bin/env python3
"""Sandbox finite gap-correction candidate (ledger v14.398 handoff).

delta_gap(n) = floor_160(r_gap_point(n) / midpoint(log_normalized(n, 128)))
on the evaluated gap rows (even-v 1040385..2080765, odd-v 1040386..2080766,
step 2, 520191 values per sector), zero elsewhere. r_gap_point is the exact
dyadic point residual of v14.396 (source - compact - seed on the gap rows),
reconstructed here from the frozen, hash-verified parent witnesses and
pinned to the v14.396 manifest hashes (even 52211d23..., odd 350e020a...).
The correction is ADDED to the preserved v14.345 trial (refined Near +
v14.341 Middle/window patch + original infinite seed unchanged); its
support is disjoint from the finite trial support.

Candidate construction only, mirroring the v14.339/v14.341 experiment:
no contraction, residual-acceptance, stationary or capacity claim. Using
a point residual to choose a represented correction does not imply the
point is the exact physical Schur residual (v14.398).

Conventions mirror v14.341 / Lane A's suzuki_near_trial_lift_rhs.py:
  floor(q, bits) = q.numerator * (1 << bits) // q.denominator
  midpoint(log_normalized(n, 128)) = (lo + hi) / 2
  sqrt_upper(q, 192) as in suzuki_exact_integer_source_action.py
  buffer: signed little-endian, width = (max_bit_length + 8) // 8
The log_normalized module is the pinned suzuki_certified_remote_diagonal.py,
verified byte-identical (SHA-256) to the repository copy before use.
"""
import json, hashlib, random, sys
from pathlib import Path
from fractions import Fraction as F
from math import isqrt

sys.path.insert(0, '/home/hatch/workspace/d12/laneA_modules')
from suzuki_certified_remote_diagonal import log_normalized

ROOT = Path('/home/hatch/workspace/d12/gapcorr398')
REPLAY = Path('/home/hatch/workspace/d12/replay396/inputs')
SEEDWORK = Path('/home/hatch/workspace/d12/gap351_work')
OUT = ROOT / 'out'
S = 1 << 256
NORM_CAP = F(2, 1000)  # unchanged 0.002 cap (v14.339)

MODULE_SHA256 = '08226538dffb5db42d85db5edb0f1c043a56df326ed1f51dc7391ca7cf8a2788'
PINNED_RESIDUAL_SHA256 = {
    'even-v': '52211d2328ed390dc9874b1534784c709fe9412244f552194f4dd558b9e830fe',
    'odd-v': '350e020a7bc9f30aa66dae7b1b7966e112b81c56141c7bd73ae64eaeefdcb5fd',
}
CASES = {
    'even-v': dict(first=1040385, shift=0),
    'odd-v': dict(first=1040386, shift=1),
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


def decode30(raw):
    assert len(raw) % 30 == 0
    return [int.from_bytes(raw[i:i + 30], 'little', signed=True)
            for i in range(0, len(raw), 30)]


def gap_residual_ints(sector):
    """Rebuild r_gap_point from the frozen parents; pin to v14.396 hashes."""
    cfg = CASES[sector]
    manifest = json.loads((REPLAY / 'compact-manifest.json').read_text())
    mspec = manifest['sectors'][sector]
    chunks = []
    for ch in mspec['chunks']:
        raw = (REPLAY / f"{sector}-compact.chunk{int(ch['name'][-3:]):03d}").read_bytes()
        assert digest(raw) == ch['sha256'], ch['name']
        chunks.append(raw)
    compact_raw = b''.join(chunks)
    assert digest(compact_raw) == mspec['buffer_sha256']
    seed_cert = json.loads((SEEDWORK / f'gap-action-{sector}.json').read_text())
    seed_raw = (SEEDWORK / f'{sector}-gap-action.bin').read_bytes()
    assert digest(seed_raw) == seed_cert['point_buffer']['sha256']
    compact = decode30(compact_raw)
    seed = decode30(seed_raw)
    assert len(compact) == len(seed) == 520191
    first, shift = cfg['first'], cfg['shift']
    residual = [S // (first + 2 * i - shift) - a - b
                for i, (a, b) in enumerate(zip(compact, seed))]
    width = max(1, (max(abs(v).bit_length() for v in residual) + 8) // 8)
    raw = b''.join(v.to_bytes(width, 'little', signed=True) for v in residual)
    assert width == 30 and digest(raw) == PINNED_RESIDUAL_SHA256[sector], sector
    return residual


def run(sector):
    module_bytes = Path('/home/hatch/workspace/d12/laneA_modules/'
                        'suzuki_certified_remote_diagonal.py').read_bytes()
    assert digest(module_bytes) == MODULE_SHA256
    cfg = CASES[sector]
    rints = gap_residual_ints(sector)
    first = cfg['first']
    rows = [(first + 2 * i, r) for i, r in enumerate(rints)]
    assert len(rows) == 520191 and rows[-1][0] == first + 2 * (520191 - 1)

    deltas = []
    minlog, maxlog = None, F(0)
    for idx, (n, r_int) in enumerate(rows):
        lo, hi = log_normalized(n, 128)
        logpoint = (lo + hi) / 2
        assert logpoint > 11
        minlog = logpoint if minlog is None else min(minlog, logpoint)
        maxlog = max(maxlog, logpoint)
        deltas.append(floor_bits(F(r_int, 1 << 256) / logpoint, 160))
        if (idx + 1) % 130048 == 0:
            print(sector, idx + 1, '/', len(rows), flush=True)

    # Independent verification on samples: integer-only path + quantum bound.
    rng = random.Random(20261014)
    sample_idx = sorted({0, 1, 2, 260095, 520189, 520190}
                        | set(rng.sample(range(520191), 58)))
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
    assert nupper <= NORM_CAP, 'norm cap 0.002 violated'
    l1 = F(l1int, 1 << 160)

    rhs = json.loads((ROOT / 'inputs' / f'RHS-{sector}.json').read_text())
    trial_upper = F(rhs['rational']['new_whole_trial_norm_upper'])
    whole_upper = trial_upper + nupper

    OUT.mkdir(parents=True, exist_ok=True)
    width = max(1, (max(abs(x).bit_length() for x in deltas) + 8) // 8)
    raw = b''.join(x.to_bytes(width, 'little', signed=True) for x in deltas)
    filename = f'{sector}-gap-correction.bin'
    (OUT / filename).write_bytes(raw)
    buf = {'file': filename, 'bits': 160, 'width': width,
           'count': len(deltas), 'bytes': len(raw), 'sha256': digest(raw)}
    back = [int.from_bytes(raw[i:i + width], 'little', signed=True)
            for i in range(0, len(raw), width)]
    assert back == deltas and sum(d * d for d in back) == sumsq

    cert = {
        'schema': 'cone.sandbox-gap-correction-candidate.v1',
        'sector': sector,
        'task': 'v14.398 HANDOFF - Sandbox: finite gap correction candidate from the replayed v14.396 residual',
        'definition': 'delta_gap(n)=floor_160(r_gap_point(n)/midpoint(log_normalized(n,128))) '
                      'on the evaluated gap rows; zero elsewhere',
        'support': {
            'first_mode': first, 'last_mode': rows[-1][0], 'step': 2,
            'count': 520191,
            'segments': [
                {'source': 'v14.396 gap residual (independently reconstructed in v14.397 replay)',
                 'rows': 520191, 'first_mode': first, 'last_mode': rows[-1][0]}]},
        'base_trial': 'correction added to the preserved v14.345 trial (refined Near + '
                      'v14.341 Middle/window patch + unchanged original infinite seed); '
                      'the gap support is disjoint from the finite trial support and '
                      'from the compact support; nothing outside the gap support changes',
        'inputs': {
            'residual_source': 'reconstructed from frozen parents (v14.373 compact chunks + v14.393 seed buffers) by the v14.396 convention; pinned to the v14.396 manifest',
            'residual_buffer_sha256': PINNED_RESIDUAL_SHA256[sector],
            'v14_396_manifest_sha256': '0657cccffa429feb45e297291194e8000a88529d28f327c10cd77eac8f34237a',
            'compact_buffer_sha256': json.loads((REPLAY / 'compact-manifest.json').read_text())['sectors'][sector]['buffer_sha256'],
            'seed_buffer_sha256': json.loads((SEEDWORK / f'gap-action-{sector}.json').read_text())['point_buffer']['sha256'],
            'log_normalized_module': 'suzuki_certified_remote_diagonal.py (byte-identical to repository copy)',
            'log_normalized_module_sha256': MODULE_SHA256,
            'v14_345_trial_certificate': 'research-notes/payloads/wider_correction_rhs_and_lift_v14_345/wider-correction-RHS-%s.json' % sector,
            'v14_345_trial_certificate_sha256': digest((ROOT / 'inputs' / f'RHS-{sector}.json').read_bytes())},
        'buffer': buf,
        'rational': {
            'correction_norm_squared': str(norm2),
            'correction_norm_upper': str(nupper),
            'correction_l1': str(l1),
            'base_trial_norm_upper_v14_345': str(trial_upper),
            'whole_trial_norm_upper_triangle': str(whole_upper)},
        'display_approximate': {
            'correction_norm_upper': float(nupper),
            'correction_l1': float(l1),
            'base_trial_norm_upper_v14_345': float(trial_upper),
            'whole_trial_norm_upper_triangle': float(whole_upper)},
        'norm_cap': {
            'cap': '0.002 (unchanged, v14.339)',
            'correction_norm_upper_within_cap': float(nupper) <= 0.002},
        'domain_justification': 'delta_gap is finitely supported (520191 modes) with '
                                'dyadic-rational values; finitely supported sequences '
                                'lie in the operator domain and in every weighted l2 '
                                'space of the framework, and the domain is a vector '
                                'space containing them, so adding delta_gap to the '
                                'existing domain-admissible v14.345 trial keeps the '
                                'sum domain-admissible. (D delta)_n for a finitely '
                                'supported correction is a finite sum at every row.',
        'verification': {
            'residual_reconstruction_pinned_to_v14_396_manifest': True,
            'sample_rows_checked': len(sample_idx),
            'integer_path_agrees_on_samples': True,
            'one_quantum_bound_on_samples': '0 <= r_gap_point - delta_gap*logpoint < logpoint * 2^-160',
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
    (OUT / f'gap-correction-{sector}.json').write_text(
        json.dumps(cert, indent=2, sort_keys=True) + '\n')
    print(sector, 'done: norm_upper', float(nupper), 'l1', float(l1),
          'whole_trial_upper', float(whole_upper), 'width', width,
          'bytes', len(raw), 'sha', buf['sha256'][:16], flush=True)
    return cert


if __name__ == '__main__':
    for s in ('even-v', 'odd-v'):
        run(s)
