#!/usr/bin/env python3
"""Exact finite-interval norm audit for Suzuki's prime-shift operator at a=1.

For one ramp breakpoint ell=log(q), the derivative-form reduction gives

    (S_ell f)(x) = f(x-ell) + f(x+ell),

with zero extension outside [-1,1].  Rather than using ||S_ell||<=2, decompose
[-1,1] into residue classes modulo ell.  Each fiber is a finite path graph P_r,
where r is the maximum number of points in [-1,1] separated by ell.  Therefore

    ||S_ell|| = 2 cos(pi/(r+1)),
    r = floor(2/ell)+1            when 2/ell is not an integer.

For ell=log(2), r=3 and ||S_ell||=sqrt(2).  For ell=log(q)>1,
q=3,4,5,7, r=2 and ||S_ell||=1.

This improves the rigorous triangle bound on the weighted five-shift prime
operator from 2*sum weights = 5.852468... to 3.129252....  No cancellation
between different q is assumed.

Combining this exact finite-interval prime bound with the analytic archimedean
bound and localized cusp/pole terms from v13.304 lowers the conservative
coercive cutoff in the even-v odd-mode sector to N=3441.

This is only a high-tail coercivity statement; it does not prove a kernel,
lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import math

EULER_GAMMA = 0.577215664901532860606512090082402431


def path_vertices(ell: float) -> int:
    # Maximum count of points in an interval of length 2 with spacing ell.
    return int(math.floor(2.0/ell + 1e-14)) + 1


def truncated_shift_norm(ell: float) -> float:
    r = path_vertices(ell)
    return 2.0*math.cos(math.pi/(r+1.0))


def prime_shift_data():
    data = [
        (2, math.log(2.0), math.log(2.0)/math.sqrt(2.0)),
        (3, math.log(3.0), math.log(3.0)/math.sqrt(3.0)),
        (4, math.log(4.0), math.log(2.0)/2.0),
        (5, math.log(5.0), math.log(5.0)/math.sqrt(5.0)),
        (7, math.log(7.0), math.log(7.0)/math.sqrt(7.0)),
    ]
    rows=[]
    for q,ell,w in data:
        rows.append({
            'q':q,
            'ell':ell,
            'weight':w,
            'path_vertices':path_vertices(ell),
            'shift_norm':truncated_shift_norm(ell),
            'weighted_cost':w*truncated_shift_norm(ell),
        })
    return rows


def prime_operator_bound() -> float:
    return sum(r['weighted_cost'] for r in prime_shift_data())


def old_triangle_bound() -> float:
    return 2.0*sum(r['weight'] for r in prime_shift_data())


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
    C_diag = (
        2.0/math.pi**2 + 2.0/math.pi**3 +
        2.0/math.pi**4 + 6.0/math.pi**5
    )
    diagonal = C_diag*math.sqrt(odd_sum4_tail_bound(N))
    return rank_one + offdiag + diagonal


def pole_tail_bound(N: int) -> float:
    return 32.0*math.cosh(0.5)**2/math.pi**2*odd_sum2_tail_bound(N)


def arch_remainder_analytic_bound() -> float:
    q = 2.0/math.pi
    return 2.0*(0.5 + math.lgamma(1.0-q) - EULER_GAMMA*q)


def tail_bound(N: int) -> dict:
    hilbert = math.pi/2.0
    prime = prime_operator_bound()
    arch = arch_remainder_analytic_bound()
    cusp = cusp_tail_bound(N)
    pole = pole_tail_bound(N)
    total = hilbert + prime + arch + cusp + pole
    floor = math.log(N/4.0)
    return {
        'N':N,
        'hilbert':hilbert,
        'prime':prime,
        'arch':arch,
        'cusp_tail':cusp,
        'pole_tail':pole,
        'total':total,
        'diag_floor':floor,
        'margin':floor-total,
    }


def first_odd_coercive_cutoff(max_search: int = 100000) -> dict:
    for N in range(1,max_search+1,2):
        r=tail_bound(N)
        if r['margin']>0:
            return r
    raise RuntimeError('cutoff not found')


def print_report():
    print('Suzuki v13.305 finite-interval prime-shift norm audit')
    for r in prime_shift_data():
        print(r)
    print('old prime bound=',old_triangle_bound())
    print('new prime bound=',prime_operator_bound())
    print('first coercive cutoff=',first_odd_coercive_cutoff())
    print('guardrail: high-tail coercivity only; no kernel/RH/GRH conclusion')


if __name__ == '__main__':
    print_report()
