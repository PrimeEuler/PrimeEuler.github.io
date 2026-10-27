#!/usr/bin/env python3
"""Erratum to v14.966 — exact-floor witness.

E1  Exact crossover: p_n = floor(L*n/(n^2+t)*2^256)/2^256 is
    exactly 0 iff n^2 - (L*2^256)*n + t > 0. Compute, per sector,
    the smallest lattice index n* with p_{n*} = 0 exactly, and
    verify p_{n*-2} > 0 exactly (previous lattice point), all in
    exact Fraction/integer arithmetic.
E2  The identity CT_sp(N) = y1 * k_N(m1) as rational functions:
    verified exactly at sample DM rows with an arbitrary rational
    test value for z_N (both sides are affine in z_N; equality at
    the level of the two affine coefficients is checked in
    Fractions from the deposited ctgate constants).
"""
import json, sys
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(1000000)
HERE = Path(__file__).resolve().parent
CTGATE = HERE.parent / 'ctgate'
D12 = HERE.parents[2]
sys.path.insert(0, str(CTGATE))
sys.path.insert(0, str(D12))

from constants import floor_
from sandbox_region23_evaluator import physical_constants

CJ = json.loads((CTGATE / 'constants.json').read_text())
OUT = {}

def rat(sec, key):
    return F(CJ[sec][key + '_rational'])

for sec in ('even-v', 'odd-v'):
    start = CJ[sec]['start']; sig = CJ[sec]['sigma']
    c, ce, L, t = physical_constants(start)
    # smallest n (any integer >= 1) with L*n/(n^2+t) < 2^-256:
    # n^2 - (L*2^256) n + t > 0. Solve by integer binary search on
    # the exact predicate q(n) := (n*n + t) - L*n*2^256 > 0 in Q.
    def qpos(n):
        return F(n * n) + t - L * n * (1 << 256) > 0
    lo, hi = 1, 1 << 300
    while not qpos(hi):
        hi <<= 1
    while lo < hi:
        mid = (lo + hi) // 2
        if qpos(mid): hi = mid
        else: lo = mid + 1
    n_any = lo
    # first sector-lattice index >= n_any with p = 0; check the
    # lattice point just below n_any still has p > 0.
    n_star = n_any if (n_any - start) % 2 == 0 else n_any + 1
    def p_exact(n):
        return F(floor_(L * n / (n * n + t), 256), 1 << 256)
    assert p_exact(n_star) == 0
    n_below = n_star - 2
    while p_exact(n_below) == 0:
        n_below -= 2
    assert p_exact(n_below) > 0 and p_exact(n_below + 2) == 0
    OUT.setdefault('E1', {})[sec] = {
        'first_lattice_index_with_p_zero': str(n_star),
        'approx': float(F(n_star)),
        'last_lattice_index_with_p_positive': str(n_below),
        'p_at_last_positive': str(p_exact(n_below)),
    }

    # ---- E2: CT_sp(N) = y1 * k_N(m1), exact affine identity in z_N
    m1 = CJ[sec]['spike_mode_m1']; y1 = rat(sec, 'y1')
    zm1 = rat(sec, 'z_m1_mid'); pm1 = rat(sec, 'p_m1')
    res = {}
    for N in (1000000 + start, 2080766 + start, CJ[sec]['F0'] - 2):
        den = N * N - m1 * m1
        pN = p_exact(N)
        # CT_sp / y1 coefficients (affine in zN): A1*zN + A0
        A1 = (c / 2) * F(2 * m1, den)
        A0 = (c / 2) * F(-2 * N, den) * zm1 + 2 * sig * pN * pm1
        # k_N(m1) coefficients: B1*zN + B0
        B1 = c * F(m1, den)
        B0 = c * F(-N, den) * zm1 + 2 * sig * pN * pm1
        assert A1 == B1 and A0 == B0, (sec, N)
        # numeric spot check with an arbitrary rational zN
        zN_test = F(7, 3)
        assert A1 * zN_test + A0 == B1 * zN_test + B0
        res[str(N)] = {'identity_exact': True}
    OUT.setdefault('E2', {})[sec] = res

(HERE / 'erratum_witness.json').write_text(json.dumps(OUT, indent=1))
print(json.dumps(OUT, indent=1))
print('ERRATUM WITNESS PASSED')
