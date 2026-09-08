#!/usr/bin/env python3
"""Eighth-power Schur audit for Suzuki's joint prime operator at a=1.

Let

    A = -B_prime = sum_q a_q S_{log q},
    a_q = Lambda(q)/sqrt(q), q in {2,3,4,5,7},

where S_l is the two-sided truncated translation on [-1,1]. Since A has a
nonnegative symmetric kernel,

    ||B_prime|| = ||A|| <= (sup_x (A^k 1)(x))^(1/k)

for every positive integer k. Piecewise-constant inputs remain piecewise
constant, and the breakpoint set at each iterate is generated exactly by
shifting the previous breakpoints by +/- log(q) and retaining points in
[-1,1]. Thus each power bound reduces to a finite exhaustive interval sweep.

At k=8 the floating-point evaluation gives

    sup_x(A^8 1)(x) = 408.10917852814157,
    ||B_prime|| <= 2.120054596948403.

The full k=1..8 root sequence is also reported. The finite-breakpoint reduction
is exact; the displayed decimal values are ordinary floating-point evaluations,
not interval-certified enclosures.

Combining the k=8 prime constant with the v13.304 analytic archimedean bound
and the tail-localized cusp/pole estimates gives first sufficient odd cutoff
N=1257.

No RH/GRH, kernel, or lambda_1=0 conclusion follows.
"""
from __future__ import annotations

import math
import numpy as np

SHIFTS = np.array([
    math.log(2.0), math.log(3.0), math.log(4.0),
    math.log(5.0), math.log(7.0)
])
WEIGHTS = np.array([
    math.log(2.0)/math.sqrt(2.0),
    math.log(3.0)/math.sqrt(3.0),
    math.log(2.0)/2.0,
    math.log(5.0)/math.sqrt(5.0),
    math.log(7.0)/math.sqrt(7.0),
])
EULER_GAMMA = 0.5772156649015328606


def eval_piecewise(bps, vals, x: float) -> float:
    if x < -1.0 or x > 1.0:
        return 0.0
    if x == 1.0:
        return float(vals[-1])
    j = int(np.searchsorted(bps, x, side='right') - 1)
    j = max(0, min(j, len(vals)-1))
    return float(vals[j])


def apply_A(bps, vals):
    new_bps = {-1.0, 1.0}
    for b in bps:
        for ell in SHIFTS:
            for z in (b-ell, b+ell):
                if -1.0 < z < 1.0:
                    new_bps.add(float(z))
    nb = np.array(sorted(new_bps), dtype=float)
    nv = []
    for lo, hi in zip(nb[:-1], nb[1:]):
        x = 0.5*(lo+hi)
        total = 0.0
        for ell, a in zip(SHIFTS, WEIGHTS):
            total += a*(eval_piecewise(bps, vals, x+ell) +
                        eval_piecewise(bps, vals, x-ell))
        nv.append(total)
    return nb, np.array(nv, dtype=float)


def power_schur(power: int = 8) -> dict:
    bps = np.array([-1.0, 1.0])
    vals = np.array([1.0])
    seq = []
    for k in range(1, power+1):
        bps, vals = apply_A(bps, vals)
        supv = float(np.max(vals))
        seq.append({
            'power': k,
            'intervals': len(vals),
            'sup_Ak1': supv,
            'root_bound': supv**(1.0/k),
        })
    return {'sequence': seq, 'prime_bound': seq[-1]['root_bound']}


def odd_sum2_tail_bound(N: int) -> float:
    return 1.0/N**2 + 1.0/(2.0*N)


def odd_sum4_tail_bound(N: int) -> float:
    return 1.0/N**4 + 1.0/(6.0*N**3)


def odd_sum6_tail_bound(N: int) -> float:
    return 1.0/N**6 + 1.0/(10.0*N**5)


def cusp_tail_bound(N: int) -> float:
    rank_one = (2.0/math.pi**2) * odd_sum2_tail_bound(N)
    c = 2.0/math.pi**3 + 6.0/math.pi**4
    alpha = 2.0*c/math.pi
    offdiag = 2.0*alpha*math.sqrt(
        (math.pi**2/12.0)*odd_sum6_tail_bound(N)
    )
    C_diag = (
        2.0/math.pi**2 + 2.0/math.pi**3 +
        2.0/math.pi**4 + 6.0/math.pi**5
    )
    diagonal = C_diag*math.sqrt(odd_sum4_tail_bound(N))
    return rank_one + offdiag + diagonal


def pole_tail_bound(N: int) -> float:
    return 32.0*math.cosh(0.5)**2/math.pi**2 * odd_sum2_tail_bound(N)


def arch_remainder_analytic_bound() -> float:
    q = 2.0/math.pi
    return 2.0*(0.5 + math.lgamma(1.0-q) - EULER_GAMMA*q)


def coercive_cutoff(max_search: int = 100000) -> dict:
    prime = power_schur(8)['prime_bound']
    for N in range(1, max_search+1, 2):
        total = (
            math.pi/2.0 + prime + arch_remainder_analytic_bound() +
            cusp_tail_bound(N) + pole_tail_bound(N)
        )
        margin = math.log(N/4.0) - total
        if margin > 0:
            return {
                'N': N,
                'prime_bound': prime,
                'arch_bound': arch_remainder_analytic_bound(),
                'cusp_tail': cusp_tail_bound(N),
                'pole_tail': pole_tail_bound(N),
                'total_tail_bound': total,
                'margin': margin,
            }
    raise RuntimeError('cutoff not found')


if __name__ == '__main__':
    print('power-Schur sequence')
    for row in power_schur(8)['sequence']:
        print(row)
    print('coercive cutoff', coercive_cutoff())
