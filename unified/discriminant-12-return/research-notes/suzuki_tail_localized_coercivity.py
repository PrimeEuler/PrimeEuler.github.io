#!/usr/bin/env python3
"""Tail-localized coercivity audit for Suzuki a=1 even-v sector.

This v13.304 control improves v13.303 in two ways:

1. The smooth pole term is recognized as rank one in the even-v sector, so its
   compression to odd Dirichlet modes n>=N has an explicit O(1/N) norm bound.
2. The cusp Hilbert-Schmidt correction is localized to the same tail using the
   analytic v13.302 estimates.

It also replaces the numerically evaluated archimedean-remainder Schur constant
from v13.299 by a fully analytic Bernoulli-polynomial majorant.

For the archimedean remainder

    r(t)=1/4 sum_{m>=2} zeta(2-m,1/4) (-2)^m t^m/m!,

use zeta(2-m,1/4)=-B_{m-1}(1/4)/(m-1) and, for k>=2,

    |B_k(x)| <= 2 k! zeta(k)/(2*pi)^k.

Writing q=2/pi gives

    int_0^2 |r''(t)| dt
      <= 1/2 + sum_{k>=2} zeta(k) q^k/k
      = 1/2 + log Gamma(1-q) - gamma q.

The symmetric Schur bound is twice this quantity.

On the tail n>=N the permanent noncompact costs retained here are

    ||H_odd|| = pi/2,
    ||B_prime|| <= 2 sum_{q in {2,3,4,5,7}} Lambda(q)/sqrt(q).

The cusp compact correction and pole term decay explicitly with N.  The final
inequality is

    <A_even c,c> >= [log(N/4)-C_tail(N)] ||c||^2.

This is a high-tail coercivity estimate only.  It does not establish a kernel,
lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import math


def odd_sum2_tail_bound(N: int) -> float:
    # For odd N and odd n>=N, spacing is 2.  First term + integral comparison.
    return 1.0/N**2 + 1.0/(2.0*N)


def odd_sum4_tail_bound(N: int) -> float:
    return 1.0/N**4 + 1.0/(6.0*N**3)


def odd_sum6_tail_bound(N: int) -> float:
    return 1.0/N**6 + 1.0/(10.0*N**5)


def cusp_tail_bound(N: int) -> float:
    # Rank-one term -2/(pi^2 mn).
    rank_one = (2.0/math.pi**2) * odd_sum2_tail_bound(N)

    # v13.302 off-diagonal error estimate.
    c = 2.0/math.pi**3 + 6.0/math.pi**4
    alpha = 2.0*c/math.pi
    offdiag = 2.0*alpha*math.sqrt(
        (math.pi**2/12.0) * odd_sum6_tail_bound(N)
    )

    # v13.302 diagonal estimate |K_nn| <= C_diag/n^2.
    C_diag = (
        2.0/math.pi**2 + 2.0/math.pi**3 +
        2.0/math.pi**4 + 6.0/math.pi**5
    )
    diagonal = C_diag*math.sqrt(odd_sum4_tail_bound(N))
    return rank_one + offdiag + diagonal


def pole_tail_bound(N: int) -> float:
    # After integration by parts the pole kernel is 2 cosh((x-y)/2).
    # In the even-v sector only 2 cosh(x/2)cosh(y/2) remains, so rank one.
    # For normalized odd Dirichlet mode psi_n,
    # |<psi_n,cosh(x/2)>| <= 4 cosh(1/2)/(pi n).
    return (
        32.0*math.cosh(0.5)**2/math.pi**2 * odd_sum2_tail_bound(N)
    )


def arch_remainder_analytic_bound() -> float:
    q = 2.0/math.pi
    l1_half = 0.5 + math.lgamma(1.0-q) - math.euler_gamma*q
    return 2.0*l1_half


def prime_operator_bound() -> float:
    # q=2,3,4,5,7.  Lambda(4)=log 2.
    weights = (
        math.log(2.0)/math.sqrt(2.0) +
        math.log(3.0)/math.sqrt(3.0) +
        math.log(2.0)/2.0 +
        math.log(5.0)/math.sqrt(5.0) +
        math.log(7.0)/math.sqrt(7.0)
    )
    return 2.0*weights


def tail_perturbation_bound(N: int) -> dict:
    hilbert = math.pi/2.0
    prime = prime_operator_bound()
    arch = arch_remainder_analytic_bound()
    cusp = cusp_tail_bound(N)
    pole = pole_tail_bound(N)
    total = hilbert + prime + arch + cusp + pole
    return {
        'N': N,
        'hilbert': hilbert,
        'prime': prime,
        'arch_remainder_analytic': arch,
        'cusp_tail': cusp,
        'pole_tail': pole,
        'total': total,
        'diag_floor': math.log(N/4.0),
        'margin': math.log(N/4.0)-total,
    }


def first_odd_coercive_cutoff(max_search: int = 2_000_000) -> dict:
    for N in range(1, max_search+1, 2):
        r = tail_perturbation_bound(N)
        if r['margin'] > 0:
            return r
    raise RuntimeError('cutoff not found in search range')


def print_report():
    print('Suzuki v13.304 tail-localized coercivity audit')
    print('prime bound=', prime_operator_bound())
    print('analytic arch remainder Schur=', arch_remainder_analytic_bound())
    r = first_odd_coercive_cutoff()
    for k,v in r.items():
        print(k, '=', v)
    print('guardrail: high-tail coercivity only; no kernel/RH/GRH conclusion')


if __name__ == '__main__':
    print_report()
