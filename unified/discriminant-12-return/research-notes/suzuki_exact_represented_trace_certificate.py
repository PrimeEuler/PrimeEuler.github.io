#!/usr/bin/env python3
"""Exact dyadic witness for the protected trace of represented hi/lo vectors.

The offline consumer needs only the Python standard library. No source action,
complement floor, floating Gram inverse, or midpoint defect is used.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import struct

from suzuki_trace_congruence_replay import add, inv, l1, mul


TARGET = F('1e-20')


def ratio(value):
    """Retain the scalar type's full significand; never cast LD to float."""
    n, d = value.as_integer_ratio()
    return F(n, d)


def canonical(witness):
    return (json.dumps(witness, sort_keys=True, separators=(',', ':')) + '\n').encode()


def certify(witness):
    assert witness['schema'] == 'cone.exact-represented-trace-witness.v1'
    p = [[F(x) for x in row] for row in witness['P_support_exact']]
    v = [[F(x) for x in row] for row in witness['V_support_exact']]
    assert p and len(p) == len(v)
    assert all(len(row) == 6 for row in p)
    assert all(len(row) == 7 for row in v)
    indices = witness['support_indices']
    assert len(indices) == len(p) and indices == sorted(set(indices))
    assert all(0 <= i < witness['dimension'] for i in indices)
    # The witness explicitly specifies that all other P rows are exactly zero.
    assert witness['P_outside_support_is_exactly_zero'] is True
    pt = [list(r) for r in zip(*p)]
    gram = mul(pt, p)
    pv = mul(pt, v)
    h = mul(inv(gram), pv)
    normalizer = witness['normalizer']
    t = [[F(x) for x in row] for row in normalizer['T']]
    off = [[F(x)] for x in normalizer['v']]
    assert len(t) == 6 and all(len(row) == 6 for row in t) and len(off) == 6
    target = [row + last for row, last in zip(t, mul(t, off))]
    defect = add(h, target, -1)
    relative = mul(inv(t), defect)
    rho = l1(relative)
    raw = canonical(witness)
    # Reconstruct the represented binary64 P payload independently.
    p_bytes = bytearray(2000 * 6 * 8)
    for i, row in zip(indices, p):
        assert i < 2000
        for j, x in enumerate(row):
            fx = float(x)
            assert F(*fx.as_integer_ratio()) == x
            struct.pack_into('<d', p_bytes, 8 * (6 * i + j), fx)
    p_sha = hashlib.sha256(p_bytes).hexdigest()
    assert p_sha == witness['frozen_base_P_sha256']
    return {
        'schema': 'cone.exact-represented-trace-certificate.v1',
        'arithmetic': 'exact integer ratios and Fraction matrix arithmetic',
        'certified_quantity': '||(P*P)^-1 P*V - [T,Tv]||_F and ||T^-1 D||_F for the represented hi+lo V',
        'coefficient_defect_fro_upper_rational': str(l1(defect)),
        'relative_defect_fro_upper_rational': str(rho),
        'relative_defect_target_rational': str(TARGET),
        'relative_defect_below_one_exact': rho < 1,
        'relative_defect_target_met_exact': rho <= TARGET,
        'canonical_witness_sha256': hashlib.sha256(raw).hexdigest(),
        'frozen_base_P_sha256': p_sha,
        'support_rows': len(indices),
        'dimension': witness['dimension'],
        'guardrail': 'Certifies the represented vector trace only. Source, affine assembly and exact projected residual caps remain separate; no overall certificate promotion.'}


def capture(p, vh, vl, normalizer, output):
    assert p.shape[1] == 6 and vh.shape == vl.shape == (len(p), 7)
    support = [i for i, row in enumerate(p) if any(x != 0 for x in row)]
    assert all(i < 2000 for i in support)
    p_exact = [[ratio(x) for x in p[i]] for i in support]
    v_exact = [[ratio(h) + ratio(l) for h, l in zip(vh[i], vl[i])]
               for i in support]
    p_bytes = bytearray(2000 * 6 * 8)
    for i, row in zip(support, p_exact):
        for j, x in enumerate(row):
            struct.pack_into('<d', p_bytes, 8 * (6 * i + j), float(x))
    witness = {
        'schema': 'cone.exact-represented-trace-witness.v1',
        'dimension': len(p), 'support_indices': support,
        'P_outside_support_is_exactly_zero': True,
        'P_support_exact': [[str(x) for x in row] for row in p_exact],
        'V_support_exact': [[str(x) for x in row] for row in v_exact],
        'normalizer': {'T': normalizer['T'], 'v': normalizer['v']},
        'frozen_base_P_sha256': hashlib.sha256(p_bytes).hexdigest(),
        'representation': 'Each V entry is the exact dyadic sum of stored longdouble high and low components; only rows in P support are needed.'}
    certificate = certify(witness)
    if not certificate['relative_defect_below_one_exact']:
        raise RuntimeError('represented trace cannot use the small congruence repair')
    output.parent.mkdir(parents=True, exist_ok=True)
    compressed = gzip.compress(canonical(witness), mtime=0)
    output.write_bytes(compressed)
    certificate.update({'witness_file': output.name,
                        'compressed_witness_sha256': hashlib.sha256(compressed).hexdigest()})
    return certificate


def replay(path, payload_path=None):
    compressed = path.read_bytes()
    witness = json.loads(gzip.decompress(compressed))
    result = certify(witness)
    result.update({'witness_file': path.name,
                   'compressed_witness_sha256': hashlib.sha256(compressed).hexdigest()})
    if payload_path is not None:
        payload = json.loads(payload_path.read_bytes())
        assert witness['normalizer'] == {k: payload['normalizer'][k] for k in ('T', 'v')}
        rows = [row for row in payload['rows'] if row['dimension'] == witness['dimension']]
        assert len(rows) == 1
        assert rows[0]['frozen_base_P_sha256'] == result['frozen_base_P_sha256']
        assert rows[0]['represented_trial_trace_certificate'] == result
    return result


def self_test():
    import numpy as np
    import tempfile
    checked = 0
    for exp in (-10000, -100, -1, 0, 1, 100, 10000):
        for significand in (2**63, 2**63 + 1, 2**64 - 1):
            x = np.ldexp(np.longdouble(str(significand)), exp - 64)
            assert ratio(x) == F(significand) * F(2)**(exp - 64)
            checked += 1
    x = np.longdouble('0.1')
    assert ratio(x) != F(*float(x).as_integer_ratio())
    p = np.zeros((11, 6))
    p[:6] = np.eye(6)
    h = np.zeros((11, 7), dtype=np.longdouble)
    low = np.zeros_like(h)
    for i in range(6):
        h[i, i] = np.longdouble(str(10**(3*i)))
    h[:, 6] = h[:, :6] @ np.arange(1, 7, dtype=np.longdouble)
    low[0, 0], low[0, 6] = np.ldexp(np.longdouble(1), -100), np.ldexp(np.longdouble(1), -110)
    t = [[str(int(h[i, j])) for j in range(6)] for i in range(6)]
    normalizer = {'T': t, 'v': [str(i + 1) for i in range(6)]}
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / 'synthetic.json.gz'
        certificate = capture(p, h, low, normalizer, path)
        assert certificate == replay(path)
        assert F(certificate['relative_defect_fro_upper_rational']) == F(2)**-100 + F(2)**-110
    return {'exact_longdouble_ratio_cases': checked,
            'binary64_narrowing_counterexample': True,
            'hi_plus_low_dyadic_witness_replay_identical': True,
            'known_relative_defect_exact': True}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--witness', type=Path)
    ap.add_argument('--payload', type=Path)
    ap.add_argument('--self-test', action='store_true')
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    if not args.self_test and args.witness is None:
        ap.error('--witness or --self-test required')
    out = json.dumps(self_test() if args.self_test else replay(args.witness, args.payload),
                     indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(out)
    print(out, end='')


if __name__ == '__main__':
    main()
