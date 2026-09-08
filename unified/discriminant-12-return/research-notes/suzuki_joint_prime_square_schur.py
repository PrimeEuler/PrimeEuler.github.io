#!/usr/bin/env python3
"""v13.307: square-Schur bound for Suzuki's joint prime-shift operator.

Let

    A = -B_prime = sum_q a_q S_{log q},
    a_q = Lambda(q)/sqrt(q), q in {2,3,4,5,7},

on L2(-1,1), with zero extension outside the interval.  A is self-adjoint and
has a nonnegative distributional kernel.  Hence A^2 also has nonnegative
kernel and

    ||B_prime||^2 = ||A||^2 = ||A^2|| <= sup_x (A^2 1)(x).

The function (A^2 1)(x) is piecewise constant.  Its breakpoints arise by
translating the first-level support breakpoints by the finite shifts ±log q.
A complete finite breakpoint sweep therefore evaluates its Schur row maximum.

The ordinary double-precision decimal is a numerical evaluation of this finite
closed computation, not an interval-arithmetic certificate.  The structural
reduction to a finite breakpoint maximum is exact.

No RH/GRH, kernel, or lambda_1=0 conclusion follows.
"""
from __future__ import annotations
import math

SHIFTS = [math.log(2.0), math.log(3.0), math.log(4.0), math.log(5.0), math.log(7.0)]
WEIGHTS = [
    math.log(2.0)/math.sqrt(2.0),
    math.log(3.0)/math.sqrt(3.0),
    math.log(2.0)/2.0,
    math.log(5.0)/math.sqrt(5.0),
    math.log(7.0)/math.sqrt(7.0),
]
EULER_GAMMA = 0.5772156649015328606


def first_row_mass(x: float) -> float:
    out = 0.0
    for ell,a in zip(SHIFTS,WEIGHTS):
        if -1.0 <= x-ell <= 1.0:
            out += a
        if -1.0 <= x+ell <= 1.0:
            out += a
    return out


def second_row_mass(x: float) -> float:
    out = 0.0
    for ell,a in zip(SHIFTS,WEIGHTS):
        y = x-ell
        if -1.0 <= y <= 1.0:
            out += a*first_row_mass(y)
        y = x+ell
        if -1.0 <= y <= 1.0:
            out += a*first_row_mass(y)
    return out


def first_breakpoints():
    bps = {-1.0,1.0}
    for ell in SHIFTS:
        for z in (ell-1.0,ell+1.0,-ell-1.0,-ell+1.0):
            if -1.0 <= z <= 1.0:
                bps.add(z)
    return sorted(bps)


def second_breakpoints():
    bps = {-1.0,1.0}
    for b in first_breakpoints():
        for ell in SHIFTS:
            for z in (b-ell,b+ell):
                if -1.0 <= z <= 1.0:
                    bps.add(z)
    return sorted(bps)


def square_schur_bound():
    bps = second_breakpoints()
    tests = list(bps)
    tests.extend((a+b)/2.0 for a,b in zip(bps[:-1],bps[1:]))
    vals = [(second_row_mass(x),x) for x in tests]
    max_row,xmax = max(vals)
    return {
        'A2_row_mass_max': max_row,
        'x_of_reported_max': xmax,
        'prime_norm_bound': math.sqrt(max_row),
        'first_level_breakpoints': len(first_breakpoints()),
        'second_level_breakpoints': len(bps),
    }


def odd_sum2_tail_bound(N: int) -> float:
    return 1.0/N**2 + 1.0/(2.0*N)


def odd_sum4_tail_bound(N: int) -> float:
    return 1.0/N**4 + 1.0/(6.0*N**3)


def odd_sum6_tail_bound(N: int) -> float:
    return 1.0/N**6 + 1.0/(10.0*N**5)


def cusp_tail_bound(N: int) -> float:
    rank_one = (2.0/math.pi**2)*odd_sum2_tail_bound(N)
    c = 2.0/math.pi**3 + 6.0/math.pi**4
    alpha = 2.0*c/math.pi
    offdiag = 2.0*alpha*math.sqrt((math.pi**2/12.0)*odd_sum6_tail_bound(N))
    Cdiag = 2.0/math.pi**2 + 2.0/math.pi**3 + 2.0/math.pi**4 + 6.0/math.pi**5
    diagonal = Cdiag*math.sqrt(odd_sum4_tail_bound(N))
    return rank_one + offdiag + diagonal


def pole_tail_bound(N: int) -> float:
    return 32.0*math.cosh(0.5)**2/math.pi**2 * odd_sum2_tail_bound(N)


def arch_remainder_analytic_bound() -> float:
    q=2.0/math.pi
    return 2.0*(0.5 + math.lgamma(1.0-q) - EULER_GAMMA*q)


def coercive_cutoff(max_search: int = 100_000):
    prime = square_schur_bound()['prime_norm_bound']
    arch = arch_remainder_analytic_bound()
    for N in range(1,max_search+1,2):
        total = math.pi/2.0 + prime + arch + cusp_tail_bound(N) + pole_tail_bound(N)
        margin = math.log(N/4.0)-total
        if margin > 0:
            return {
                'N':N,
                'prime_bound':prime,
                'arch_bound':arch,
                'cusp_tail':cusp_tail_bound(N),
                'pole_tail':pole_tail_bound(N),
                'total_tail_bound':total,
                'margin':margin,
            }
    raise RuntimeError('cutoff not found')


if __name__ == '__main__':
    print('Suzuki v13.307 joint-prime square-Schur audit')
    print(square_schur_bound())
    print(coercive_cutoff())
    print('guardrail: finite breakpoint evaluation; no kernel/RH/GRH conclusion')
