#!/usr/bin/env python3
"""Exact joint-prime sequence factorization for Suzuki's a=1 even-v sector.

For odd Dirichlet modes psi_n(x)=sin(n*pi*(x+1)/2) and the truncated two-sided
translation S_ell on [-1,1], direct integration gives, for odd m != n,

    <psi_m,S_ell psi_n>
      = (4/pi) [n sin(m theta)-m sin(n theta)]/(n^2-m^2),
      theta = pi*ell/2.

For the full prime operator

    B_prime = - sum_q w_q S_{log q},
    w_q = Lambda(q)/sqrt(q), q in {2,3,4,5,7},

define the scalar oscillatory sequence

    A_j = sum_q w_q sin(j theta_q), theta_q=(pi/2)log q.

Then the entire off-diagonal prime matrix collapses exactly to

    (B_prime)_{mn} = -(4/pi) (n A_m - m A_n)/(n^2-m^2).

For a fixed odd core mode m and odd n>=N>m, with
W=sum_q w_q,

    |B_mn| <= (4/pi)/(1-(m/N)^2) [ |A_m|/n + m W/n^2 ].

Taking l2 norms in n and then Hilbert-Schmidt in the finite core gives a
rigorous infinite-tail O(N^-1/2) bound which is much sharper than v13.314's
termwise absolute-value estimate.

The reported decimals are ordinary floating evaluations of exact/analytic
formulas, not interval-certified enclosures. No RH/GRH, kernel, or lambda=0
conclusion follows.
"""
from __future__ import annotations

import math
import mpmath as mp

QS = (2, 3, 4, 5, 7)
SHIFTS = tuple(math.log(q) for q in QS)
WEIGHTS = (
    math.log(2.0)/math.sqrt(2.0),
    math.log(3.0)/math.sqrt(3.0),
    math.log(2.0)/2.0,
    math.log(5.0)/math.sqrt(5.0),
    math.log(7.0)/math.sqrt(7.0),
)
THETAS = tuple(0.5*math.pi*ell for ell in SHIFTS)
W = sum(WEIGHTS)
CORE = tuple(range(1, 20, 2))
PRIME_BOUND = 2.044764260347282


def A(j: int) -> float:
    return sum(w*math.sin(j*th) for w, th in zip(WEIGHTS, THETAS))


def shift_entry(m: int, n: int, ell: float) -> float:
    if m == n:
        raise ValueError('off-diagonal formula only')
    th = 0.5*math.pi*ell
    return (4.0/math.pi) * (n*math.sin(m*th)-m*math.sin(n*th))/(n*n-m*m)


def prime_entry(m: int, n: int) -> float:
    if m == n:
        raise ValueError('off-diagonal formula only')
    return -(4.0/math.pi) * (n*A(m)-m*A(n))/(n*n-m*m)


def odd_sum2_tail_bound(N: int) -> float:
    return 1.0/N**2 + 1.0/(2.0*N)


def odd_sum4_tail_bound(N: int) -> float:
    return 1.0/N**4 + 1.0/(6.0*N**3)


def row_tail_bound(m: int, N: int) -> float:
    if N <= m:
        raise ValueError('need N>m')
    den = 1.0 - (m/N)**2
    return (4.0/math.pi)/den * (
        abs(A(m))*math.sqrt(odd_sum2_tail_bound(N))
        + m*W*math.sqrt(odd_sum4_tail_bound(N))
    )


def core_tail_hs_bound(N: int) -> float:
    return math.sqrt(sum(row_tail_bound(m, N)**2 for m in CORE))


def r4_majorant() -> float:
    q = 2.0/math.pi
    return float(mp.zeta(3))*q**3/(4.0*(1.0-q)**3)


def arch_entry_constant() -> float:
    return 19.0/12.0 + 4.0*r4_majorant()


def arch_tail_bound(N: int) -> float:
    return arch_entry_constant()*(4.0/math.pi**2)*odd_sum2_tail_bound(N)


def odd_sum6_tail_bound(N: int) -> float:
    return 1.0/N**6 + 1.0/(10.0*N**5)


def cusp_tail_bound(N: int) -> float:
    rank_one = (2.0/math.pi**2)*odd_sum2_tail_bound(N)
    c = 2.0/math.pi**3 + 6.0/math.pi**4
    alpha = 2.0*c/math.pi
    offdiag = 2.0*alpha*math.sqrt((math.pi**2/12.0)*odd_sum6_tail_bound(N))
    C_diag = 2.0/math.pi**2 + 2.0/math.pi**3 + 2.0/math.pi**4 + 6.0/math.pi**5
    diagonal = C_diag*math.sqrt(odd_sum4_tail_bound(N))
    return rank_one + offdiag + diagonal


def tail_gap(N: int) -> float:
    adverse = math.pi/2.0 + PRIME_BOUND + cusp_tail_bound(N) + arch_tail_bound(N)
    return math.log(N/4.0) - adverse


def schur_penalty(N: int) -> float:
    beta = core_tail_hs_bound(N)
    alpha = tail_gap(N)
    return math.inf if alpha <= 0.0 else beta*beta/alpha


def report(cutoffs=(151, 201, 237, 301, 401, 501, 701, 1001)):
    print('W =', W)
    print('A_m on core')
    for m in CORE:
        print(m, A(m))
    print('cutoff, tail gap, beta_HS, beta^2/alpha')
    for N in cutoffs:
        print(N, tail_gap(N), core_tail_hs_bound(N), schur_penalty(N))


if __name__ == '__main__':
    report()
