#!/usr/bin/env python3
"""Compose finite endpoint caps by the audited v14.155/156/157 lemmas.

All decisions and interval endpoints are Fractions. Independent audit of the
new source-arithmetic bridge remains required; there is no infinite-tail claim.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
from suzuki_trace_congruence_replay import capacity, display, tr

if hasattr(sys, 'set_int_max_str_digits'): sys.set_int_max_str_digits(0)

P_HASHES = {'even-v': 'e1eef3afeacbe6d265237f8e643ec4340ee5fcc3b0877240015ad196172b3170',
            'odd-v': '1642a3f2617935dd5f484e4cdbd8fd5e03b3289ed437c1571894e2b5e09e8f80'}


def endpoint(path, sector, cutoff):
    raw = Path(path).read_bytes(); obj = json.loads(raw)
    normal = dict(obj['normalizer']); recorded = normal.pop('normalizer_sha256')
    assert hashlib.sha256(json.dumps(normal, sort_keys=True, separators=(',', ':')).encode()).hexdigest() == recorded
    rows = [r for r in obj['rows'] if r['sector'] == sector and r['cutoff'] == cutoff]
    assert len(rows) == 1
    row = rows[0]; cert = row['outward_numerical_certificate']
    assert row['normalizer_sha256'] == recorded
    assert cert['sector'] == sector and cert['cutoff'] == cutoff
    assert cert['frozen_base_P_sha256'] == row['frozen_base_P_sha256'] == P_HASHES[sector]
    assert cert['remote_start'] == row['remote_start']
    assert cert['all_six_numerical_targets_met'] and all(cert['checks_exact'].values())
    assert 8000 <= cutoff <= 256000
    gamma = F('2.95e-19' if sector == 'even-v' else '2.16e-17')
    assert F(cert['fullQ_floor_rational']) == gamma
    assert F(row['coercivity_contract']['gamma_certified']) == gamma
    assert row['M_trial_midpoint'] == cert['M_point_decimal']
    m = [[F(x) for x in r] for r in cert['M_point_decimal']]
    assert len(m) == 7 and all(len(r) == 7 for r in m) and m == tr(m)
    j = min(m[i][i]-sum(abs(m[i][k]) for k in range(6) if k != i) for i in range(6))
    q = sum(abs(m[i][6]) for i in range(6))
    mn = max(sum(abs(x) for x in r) for r in m)
    caps = {k: F(v) for k, v in cert['bounds_rational'].items()}
    targets = {'assembly_J': F('1e-4'), 'assembly_beta': F('1e-9'),
               'assembly_eta': F('1e-14'), 'graph_residual_fro': F('1e-11'),
               'source_residual_l2': F('1e-15')}
    assert all(0 <= caps[k] <= ceiling for k, ceiling in targets.items())
    rho = F(cert['relative_trace_fro_upper_rational']); assert 0 <= rho <= F('1e-20')
    nu = rho/(1-rho)
    alpha = caps['assembly_J']+2*caps['assembly_beta']+caps['assembly_eta']
    trace_charge = nu*(2+nu)*(mn+alpha)
    fc = caps['graph_residual_fro']/(1-rho)
    sc = caps['source_residual_l2']+caps['graph_residual_fro']*nu
    a = caps['assembly_J']+trace_charge+fc*fc/gamma
    b = caps['assembly_beta']+trace_charge+fc*sc/gamma
    c = caps['assembly_eta']+trace_charge+sc*sc/gamma
    assert j > a
    kappa = c+b*(2*q+b)/(j-a)+a*q*q/(j*(j-a))
    kval = capacity(m)
    proof = {'sector': sector, 'cutoff': cutoff, 'input_sha256': hashlib.sha256(raw).hexdigest(),
             'normalizer_sha256': recorded, 'frozen_base_P_sha256': P_HASHES[sector],
             'gamma_rational': str(gamma), 'J_lower_rational': str(j),
             'beta_norm_upper_rational': str(q), 'trace_charge_rational': str(trace_charge),
             'stationary_block_errors_rational': {'a': str(a), 'b': str(b), 'c': str(c)},
             'capacity_point_rational': str(kval), 'capacity_error_upper_rational': str(kappa),
             'capacity_error_upper_display': display(kappa), 'J_lower_exceeds_graph_error_exact': True}
    return obj, row, kval, kappa, proof


def analyze(paths, cutoffs=(64000,128000)):
    r0, r1 = cutoffs
    endpoints = [endpoint(path, sector, cutoff) for path, sector, cutoff in
                 zip(paths, ('even-v','even-v','odd-v','odd-v'), (r0,r1,r0,r1))]
    for old, new in ((endpoints[0],endpoints[1]), (endpoints[2],endpoints[3])):
        assert old[1]['normalizer_sha256'] == new[1]['normalizer_sha256']
        assert old[1]['remote_start'] == new[1]['remote_start']
    assert len({e[1]['remote_start'] for e in endpoints}) == 1
    psi = (endpoints[3][2]-endpoints[2][2])-(endpoints[1][2]-endpoints[0][2])
    error = sum(e[3] for e in endpoints)
    lower, upper = psi-error, psi+error
    bound = abs(psi)+error
    return {'schema': 'cone.exact-outward-finite-pair.v1', 'R': r0, 'R2': r1,
            'remote_start': endpoints[0][1]['remote_start'], 'endpoints': [e[4] for e in endpoints],
            'point_odd_minus_even_increment_rational': str(psi),
            'point_odd_minus_even_increment_display': display(psi),
            'endpoint_error_sum_rational': str(error), 'endpoint_error_sum_display': display(error),
            'source_interval_rational': [str(lower), str(upper)],
            'source_interval_display_approximate': [display(lower),display(upper)],
            'source_abs_bound_rational': str(bound), 'source_abs_bound_display': display(bound),
            'source_abs_bound_le_9e_minus10_exact': bound <= F('9e-10'),
            'source_interval_strictly_negative_exact': upper < 0,
            'all_four_rows_meet_all_six_numerical_targets': True,
            'overall_certificate_ready': False,
            'audit_status': 'independent review of new exact-point physical-source arithmetic bridge pending',
            'guardrail': 'Finite octave only. Exact rational composition of outward caps with audited full-Q floors and affine trace repair; no infinite-tail or final Cone theorem.'}


def main():
    p = argparse.ArgumentParser()
    for label in ('even-old','even-new','odd-old','odd-new'): p.add_argument('--'+label, required=True)
    p.add_argument('--R', type=int, default=64000); p.add_argument('--R2', type=int, default=128000)
    p.add_argument('--output', type=Path, required=True); p.add_argument('--require-budget', action='store_true')
    args = p.parse_args()
    out = analyze([args.even_old,args.even_new,args.odd_old,args.odd_new], (args.R,args.R2))
    if args.require_budget: assert out['source_abs_bound_le_9e_minus10_exact']
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k.endswith('_display') or k.endswith('_exact')}, indent=2))


if __name__ == '__main__': main()
