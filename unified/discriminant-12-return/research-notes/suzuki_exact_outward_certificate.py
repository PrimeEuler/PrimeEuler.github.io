#!/usr/bin/env python3
"""Five outward caps from exact point assembly and exact projected residuals.

The remaining source uncertainty is charged using conservatively widened,
already-audited arch-200 scalar envelopes. Snapshots retain all vector rows.
"""
import argparse
from fractions import Fraction as F
import hashlib
import io
import json
from pathlib import Path
import struct
import sys
import zipfile

from suzuki_exact_integer_source_action import (
    ExactSource, dot, family_from_pairs, frac, norm2, sqrt_upper,
)
from suzuki_trace_congruence_replay import add, inv, l1, mul, tr, display

if hasattr(sys, 'set_int_max_str_digits'): sys.set_int_max_str_digits(0)

CAPS = {'z': F('1e-38'), 'diag': F('4.4e-37'),
        'pole': F('1e-39'), 'c': F('2e-41')}
TARGETS = {'assembly_J': F('1e-4'), 'assembly_beta': F('1e-9'),
           'assembly_eta': F('1e-14'), 'graph_residual_fro': F('1e-11'),
           'source_residual_l2': F('1e-15')}
P_HASHES = {
    'even-v': 'e1eef3afeacbe6d265237f8e643ec4340ee5fcc3b0877240015ad196172b3170',
    'odd-v': '1642a3f2617935dd5f484e4cdbd8fd5e03b3289ed437c1571894e2b5e09e8f80',
}


def decimal_floor(q, digits=100):
    n = q.numerator * 10**digits // q.denominator
    sign = '-' if n < 0 else ''; s = str(abs(n)).rjust(digits + 1, '0')
    return sign + s[:-digits] + '.' + s[-digits:]


def p_families(p):
    support = [i for i, row in enumerate(p) if any(v != 0 for v in row)]
    assert support and max(support) < 2000
    stop = max(support) + 1
    out = []
    for j in range(6):
        high = p[:stop, j]
        out.append(family_from_pairs(high, high * 0))
    return out


def support_dot(p, v):
    return frac(sum(a*b for a, b in zip(p['values'], v['values'])),
                p['bits'] + v['bits'])


def raw_source(modes, sector, frontier, bits=256):
    return {'bits': bits, 'values': [0 if n <= frontier else
             (1 << bits) // (n if sector == 'even-v' else n - 1) for n in modes]}


def subtract(a, b):
    assert len(a['values']) == len(b['values'])
    bits = max(a['bits'], b['bits'])
    return {'bits': bits,
            'values': [(x << (bits-a['bits'])) - (y << (bits-b['bits']))
                       for x, y in zip(a['values'], b['values'])]}


def p_hash(p):
    raw = bytearray(2000 * 6 * 8)
    for j, col in enumerate(p):
        for i, value in enumerate(col['values']):
            x = frac(value, col['bits']); xf = float(x)
            assert F(*xf.as_integer_ratio()) == x
            struct.pack_into('<d', raw, 8*(6*i+j), xf)
    return hashlib.sha256(raw).hexdigest()


def operator_radius(source, kernel_bits):
    n = len(source['modes'])
    assert abs(frac(source['c']['values'][0], source['c']['bits'])) < 1
    assert all(abs(frac(v, source['z']['bits'])) < 11 for v in source['z']['values'])
    # H_(n-1) <= 1+ceil(log2(n)) by dyadic grouping of positive terms.
    harmonic_cap = F(1 + (n-1).bit_length())
    ez, ed, ep, ec = (CAPS[k] for k in ('z', 'diag', 'pole', 'c'))
    scalar = ed + (ez + 11*ec)*harmonic_cap
    scalar += 8*sqrt_upper(F(n))*ep + 2*n*ep*ep
    kernel = F(22*n, 1 << kernel_bits)
    return scalar + kernel, scalar, kernel


def certificate(source, vectors, p, normalizer, sector, frontier,
                kernel_bits=256, actions=None):
    n = len(source['modes'])
    cutoff = 2*n  # even-v uses odd modes ending at R-1; odd-v ends at R.
    assert 2000 <= cutoff <= 256000
    assert len(vectors) == 7 and len(p) == 6
    assert all(len(v['values']) == n for v in vectors)
    assert all(source['component_magnitude_checks'].values())
    # Replay the component-range checks and the exact high+low reconstruction;
    # these are the hypotheses behind the 41-significant-digit audit slack.
    halves = source['represented_source_halves']
    for name, limit in (('z', 100), ('diag', 100), ('pole', 2), ('c', 1)):
        h, l, combined = halves[name+'_hi'], halves[name+'_lo'], source[name]
        assert len(h['values']) == len(l['values']) == len(combined['values'])
        for hv, lv, cv in zip(h['values'], l['values'], combined['values']):
            hh, ll = frac(hv, h['bits']), frac(lv, l['bits'])
            assert abs(hh) < limit and abs(ll) < limit
            assert hh+ll == frac(cv, combined['bits'])
    assert source['alpha'] == (2 if sector == 'even-v' else -2)
    assert source['modes'][0] == (1 if sector == 'even-v' else 2)
    assert p_hash(p) == P_HASHES[sector]
    engine = ExactSource(source, kernel_bits)
    if actions is None: actions = [engine.action(v) for v in vectors]
    assert len(actions) == 7
    g = raw_source(source['modes'], sector, frontier)
    gram = [[dot(a, b) for b in p] for a in p]
    gi = inv(gram)
    h = [[support_dot(pc, v) for v in vectors] for pc in p]
    trace = mul(gi, h)
    t = [[F(x) for x in row] for row in normalizer['T']]
    off = [[F(x)] for x in normalizer['v']]
    target = [row + last for row, last in zip(t, mul(t, off))]
    defect = add(trace, target, -1)
    rho = l1(mul(inv(t), defect))
    assert rho < 1
    m = [[dot(vectors[i], actions[j]) for j in range(7)] for i in range(7)]
    vg = [dot(v, g) for v in vectors]
    for i in range(7):
        m[i][6] -= vg[i]; m[6][i] -= vg[i]
    assert m == tr(m)
    serialized = [[decimal_floor(x) for x in row] for row in m]
    r2 = []
    for j, y in enumerate(actions):
        raw = subtract(y, g) if j == 6 else y
        q = [[support_dot(pc, raw)] for pc in p]
        squared = norm2(raw) - mul(tr(q), mul(gi, q))[0][0]
        assert squared >= 0
        r2.append(squared)
    w2 = sum((norm2(v) for v in vectors[:6]), F(0))
    u2 = norm2(vectors[6])
    wn, un = sqrt_upper(w2), sqrt_upper(u2)
    f0, s0 = sqrt_upper(sum(r2[:6], F(0))), sqrt_upper(r2[6])
    da, scalar_radius, kernel_radius = operator_radius(source, kernel_bits)
    dg = F(n, 1 << g['bits'])
    rounding = F(1, 10**100)
    bounds = {'assembly_J': da*w2 + 6*rounding,
              'assembly_beta': da*wn*un + dg*wn + 6*rounding,
              'assembly_eta': da*u2 + 2*dg*un + rounding,
              'graph_residual_fro': f0 + da*wn,
              'source_residual_l2': s0 + da*un + dg}
    checks = {k: bounds[k] <= TARGETS[k] for k in TARGETS}
    checks['relative_trace'] = rho <= F('1e-20')
    return {'schema': 'cone.exact-point-outward-certificate.v1',
            'sector': sector, 'cutoff': cutoff, 'dimension': n,
            'remote_start': frontier, 'kernel_bits': kernel_bits,
            'frozen_base_P_sha256': p_hash(p),
            'fullQ_floor_rational': str(F('2.95e-19' if sector == 'even-v' else '2.16e-17'))
                  if 8000 <= cutoff <= 256000 else None,
            'fullQ_floor_parents': ['v14.155', 'v14.158', 'v14.161'],
            'M_point_decimal': serialized,
            'bounds_rational': {k: str(v) for k, v in bounds.items()},
            'bounds_display': {k: display(v) for k, v in bounds.items()},
            'targets_rational': {k: str(v) for k, v in TARGETS.items()},
            'relative_trace_fro_upper_rational': str(rho),
            'source_scalar_caps_rational': {k: str(v) for k, v in CAPS.items()},
            'operator_radius_rational': str(da),
            'operator_scalar_radius_rational': str(scalar_radius),
            'operator_kernel_radius_rational': str(kernel_radius),
            'source_vector_radius_rational': str(dg),
            'graph_vector_norm2_rational': str(w2), 'source_trial_norm2_rational': str(u2),
            'point_projected_residual_norm2_rational': [str(x) for x in r2],
            'checks_exact': checks, 'all_six_numerical_targets_met': all(checks.values()),
            'overall_certificate_ready': False,
            'audit_status': 'new outward arithmetic bridge requires independent review',
            'guardrail': 'Exact point action/assembly/projector arithmetic; physical-source scalar and kernel uncertainty explicitly charged. Finite cutoff only; no infinite-tail result.'}


def write_snapshot(path, source, vectors, p, normalizer, sector, frontier, kernel_bits):
    arrays = {**{k: source[k] for k in ('z', 'diag', 'pole', 'c')},
              **source['represented_source_halves'],
              **{f'V{j}': v for j, v in enumerate(vectors)},
              **{f'P{j}': v for j, v in enumerate(p)}}
    manifest = {'schema': 'cone.exact-point-full-snapshot.v1',
                'sector': sector, 'remote_start': frontier, 'kernel_bits': kernel_bits,
                'modes': source['modes'], 'alpha': source['alpha'],
                'component_magnitude_checks': source['component_magnitude_checks'],
                'normalizer': normalizer, 'arrays': {}}
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for name, a in arrays.items():
            width = max(1, (max(abs(x).bit_length() for x in a['values']) + 1 + 7)//8)
            raw = b''.join(x.to_bytes(width, 'little', signed=True) for x in a['values'])
            info = zipfile.ZipInfo(name + '.bin', date_time=(1980,1,1,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, raw)
            manifest['arrays'][name] = {'bits': a['bits'], 'width': width,
                 'count': len(a['values']), 'sha256': hashlib.sha256(raw).hexdigest()}
        info = zipfile.ZipInfo('manifest.json', date_time=(1980,1,1,0,0,0))
        info.compress_type = zipfile.ZIP_DEFLATED
        z.writestr(info, json.dumps(manifest, sort_keys=True, separators=(',', ':'))+'\n')
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_snapshot(path):
    with zipfile.ZipFile(path) as z:
        manifest = json.loads(z.read('manifest.json'))
        assert manifest['schema'] == 'cone.exact-point-full-snapshot.v1'
        arrays = {}
        for name, a in manifest['arrays'].items():
            raw = z.read(name+'.bin'); width = a['width']
            assert hashlib.sha256(raw).hexdigest() == a['sha256']
            assert len(raw) == width*a['count']
            arrays[name] = {'bits': a['bits'], 'values': [int.from_bytes(raw[i:i+width], 'little', signed=True)
                                    for i in range(0, len(raw), width)]}
    source = {k: arrays[k] for k in ('z', 'diag', 'pole', 'c')}
    source['represented_source_halves'] = {k: arrays[k] for k in
                                         ('z_hi','z_lo','diag_hi','diag_lo','pole_hi','pole_lo','c_hi','c_lo')}
    source.update({k: manifest[k] for k in ('modes', 'alpha', 'component_magnitude_checks')})
    return manifest, source, [arrays[f'V{j}'] for j in range(7)], [arrays[f'P{j}'] for j in range(6)]


def replay_snapshot(path):
    meta, source, vectors, p = read_snapshot(path)
    return certificate(source, vectors, p, meta['normalizer'], meta['sector'],
                       meta['remote_start'], meta['kernel_bits'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--snapshot', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--reference', type=Path)
    ap.add_argument('--require-targets', action='store_true')
    args = ap.parse_args()
    result = replay_snapshot(args.snapshot)
    if args.require_targets: assert result['all_six_numerical_targets_met']
    encoded = json.dumps(result, indent=2, sort_keys=True)+'\n'
    if args.reference: assert encoded.encode() == args.reference.read_bytes()
    args.output.write_text(encoded)
    print(json.dumps({'all_six_numerical_targets_met': result['all_six_numerical_targets_met'],
                      'checks_exact': result['checks_exact'],
                      'bounds_display': result['bounds_display']}, indent=2))


if __name__ == '__main__': main()
