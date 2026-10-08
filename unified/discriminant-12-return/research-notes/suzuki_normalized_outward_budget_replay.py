#!/usr/bin/env python3
"""Conditional finite-octave error budget, using exact rational decisions.

The error ceilings are targets to certify, not observed outward bounds.
Requires the adjacent suzuki_trace_congruence_replay.py (standard library).
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import random

from suzuki_trace_congruence_replay import (
    add, capacity, display, eye, inv, l1, mul, tr,
)


def diagonal_floor(j):
    assert j == tr(j)
    return min(j[i][i] - sum(abs(j[i][k]) for k in range(len(j)) if k != i)
               for i in range(len(j)))


def kappa(j, beta, a, b, c):
    assert j > a >= 0 and beta >= 0 and b >= 0 and c >= 0
    return c + b * (2 * beta + b) / (j - a) + a * beta**2 / (j * (j - a))


def matrix(j, b, eta):
    return [row + bj for row, bj in zip(j, b)] + [[x[0] for x in b] + [-eta]]


def synthetic(seed):
    rng = random.Random(seed)
    n = 6
    j = eye(n)
    for i in range(n):
        j[i][i] = F(2)
        for k in range(i):
            j[i][k] = j[k][i] = F(rng.randint(-2, 2), 100)
    b = [[F(rng.randint(-3, 3), 100)] for _ in range(n)]
    dj = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(i + 1):
            dj[i][k] = dj[k][i] = F(rng.randint(-2, 2), 10000)
    db = [[F(rng.randint(-3, 3), 10000)] for _ in range(n)]
    de = F(1, 100000)
    j0, b0 = diagonal_floor(j), l1(b)
    acap, bcap = max(sum(abs(x) for x in row) for row in dj), l1(db)
    bound = kappa(j0, b0, acap, bcap, de)
    base = capacity(matrix(j, b, F(1, 5)))
    for sign in (-1, 1):
        actual = capacity(matrix(add(j, dj, sign), add(b, db, sign), F(1, 5) + sign * de))
        assert abs(actual - base) <= bound
    return {"seed": seed, "both_perturbation_signs_pass_exactly": True}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--payload-root', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    rho = F('1e-20')
    nu = rho / (1 - rho)
    # Independent block assembly targets, before the trace-repair inflation.
    aj, ab, ae = F('1e-4'), F('1e-9'), F('1e-14')
    f, s = F('1e-11'), F('1e-15')
    alpha_full = aj + 2 * ab + ae
    fc, sc = f / (1 - rho), s + f * nu
    rows, values, bounds = [], {}, []
    for cutoff in (64000, 128000):
        for sector, gamma in (('even-v', F('2.95e-19')), ('odd-v', F('2.16e-17'))):
            path = args.payload_root / f'joint-{cutoff}-{sector}.json'
            raw = path.read_bytes()
            row = json.loads(raw)['rows'][0]
            m = [[F(x) for x in r] for r in row['M_trial_midpoint']]
            assert m == tr(m)
            j = diagonal_floor([r[:6] for r in m[:6]])
            beta = sum(abs(m[i][6]) for i in range(6))
            magnitude = max(sum(abs(x) for x in r) for r in m)
            trace_charge = nu * (2 + nu) * (magnitude + alpha_full)
            a = aj + trace_charge + fc**2 / gamma
            b = ab + trace_charge + fc * sc / gamma
            c = ae + trace_charge + sc**2 / gamma
            cap = kappa(j, beta, a, b, c)
            bounds.append(cap)
            values[(cutoff, sector)] = capacity(m)
            rows.append({"file": path.name, "sha256": hashlib.sha256(raw).hexdigest(),
                         "J_serialized_diagonal_dominance_floor": display(j),
                         "beta_serialized_l1_upper": display(beta),
                         "corrected_total_J_error_target": display(a),
                         "corrected_total_beta_error_target": display(b),
                         "corrected_total_eta_error_target": display(c),
                         "conditional_capacity_error_upper": display(cap),
                         "conditional_J_positive": True})
    pair = (values[(128000, 'odd-v')] - values[(64000, 'odd-v')]
            - values[(128000, 'even-v')] + values[(64000, 'even-v')])
    total = sum(bounds, F(0))
    base_bound, target = F('8.675e-10'), F('9e-10')
    assert abs(pair) <= base_bound
    assert base_bound + total < target
    assert pair + total < 0
    out = {"schema": "cone.normalized-outward-target-budget.v1",
           "arithmetic": "Fraction for all decisions; Decimal display only",
           "conditional_budget_feasible": True,
           "certificate_ready": False,
           "required_caps_not_yet_certified": {
               "relative_trace_defect_fro": str(rho),
               "original_assembly_J_operator": str(aj),
               "original_assembly_beta_l2": str(ab),
               "original_assembly_eta_abs": str(ae),
               "original_graph_residual_fro": str(f),
               "original_source_residual_l2": str(s)},
           "fullQ_floors_assumed_pending_independent_audit": {
               "even": "2.95e-19", "odd": "2.16e-17", "parent": "v14.155"},
           "synthetic_cases": [synthetic(seed) for seed in (23, 73, 197)],
           "rows": rows,
           "serialized_midpoint_pair_exact_display": display(pair),
           "conditional_pair_error_upper": display(total),
           "conditional_pair_interval": [display(pair - total), display(pair + total)],
           "rounded_original_midpoint_bound_checked_exactly": display(base_bound),
           "conditional_paired_bound_plus_error": display(base_bound + total),
           "conditional_target_upper": display(target),
           "guardrail": "Finite 64k-to-128k octave only; every proposed trace/assembly/residual cap still needs source-faithful outward certification, and the full-Q/trace bridges need independent audit. No infinite-tail conclusion."}
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
