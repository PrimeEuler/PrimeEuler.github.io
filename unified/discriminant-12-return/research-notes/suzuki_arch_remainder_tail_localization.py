#!/usr/bin/env python3
"""Tail-localized bound for Suzuki's smooth archimedean remainder.

In the a=1 even-v sector, let h(t)=r''(t) and

    K_r(x,y) = -h(|x-y|).

The previous v13.311 bound ||K_r|| <= 0.459846... is global.  This checkpoint
uses the Dirichlet half-integer cosine basis and two integrations by parts to
show the matrix entries satisfy

    |(K_r)_{mn}| <= C_r/(k_m k_n),   k_n=n*pi/2, n odd,

with an explicit analytic constant C_r < 8.048.  Hence the high-mode
compression is Hilbert-Schmidt and obeys an O(1/N) operator bound.

The only inherited non-interval ingredient in the final cutoff is the finite
power-Schur prime decimal from v13.310.  No RH/GRH or kernel conclusion follows.
"""
from __future__ import annotations

import math
import mpmath as mp

PRIME_BOUND = 2.044764260347282


def r4_majorant() -> float:
    """Analytic sup bound for |r''''(t)| on 0<=t<=2.

    With q=2/pi and k=m-1>=3, Bernoulli's Fourier bound gives

      |a_{k+1}| <= zeta(k)/(pi^k k(k+1)).

    Therefore

      sup |r''''| <= (1/8) sum_{k>=3} zeta(k)(k-1)(k-2)q^k
                   <= zeta(3) q^3/[4(1-q)^3].
    """
    q = 2.0 / math.pi
    return float(mp.zeta(3)) * q**3 / (4.0 * (1.0-q)**3)


def entry_constant() -> float:
    """Constant C_r in |K_mn| <= C_r/(k_m k_n).

    h(0)=1/4, h'(0)=-1/48, h is positive decreasing on [0,2].  After
    integrating the half-integer cosine basis once in each variable, the edge
    and corner contributions combine to at most 6 h(0)=3/2.  The mixed
    derivative measure has continuous variation at most 4 sup|h''| and a
    diagonal jump mass 4|h'(0)|=1/12.
    """
    return 19.0/12.0 + 4.0*r4_majorant()


def odd_sum2_tail_bound(N: int) -> float:
    return 1.0/N**2 + 1.0/(2.0*N)


def arch_tail_bound(N: int) -> float:
    # sum 1/k_n^2 = 4/pi^2 sum 1/n^2 over odd n>=N.
    return entry_constant() * (4.0/math.pi**2) * odd_sum2_tail_bound(N)


def odd_sum4_tail_bound(N: int) -> float:
    return 1.0/N**4 + 1.0/(6.0*N**3)


def odd_sum6_tail_bound(N: int) -> float:
    return 1.0/N**6 + 1.0/(10.0*N**5)


def cusp_tail_bound(N: int) -> float:
    rank_one = (2.0/math.pi**2) * odd_sum2_tail_bound(N)
    c = 2.0/math.pi**3 + 6.0/math.pi**4
    alpha = 2.0*c/math.pi
    offdiag = 2.0*alpha*math.sqrt((math.pi**2/12.0)*odd_sum6_tail_bound(N))
    C_diag = 2.0/math.pi**2 + 2.0/math.pi**3 + 2.0/math.pi**4 + 6.0/math.pi**5
    diagonal = C_diag*math.sqrt(odd_sum4_tail_bound(N))
    return rank_one + offdiag + diagonal


def tail_margin(N: int) -> float:
    adverse = math.pi/2.0 + PRIME_BOUND + cusp_tail_bound(N) + arch_tail_bound(N)
    return math.log(N/4.0) - adverse


def coercive_cutoff(max_search: int = 10000) -> dict:
    for N in range(1, max_search+1, 2):
        margin = tail_margin(N)
        if margin > 0:
            return {
                'N': N,
                'prime_bound': PRIME_BOUND,
                'r4_majorant': r4_majorant(),
                'entry_constant': entry_constant(),
                'arch_tail': arch_tail_bound(N),
                'cusp_tail': cusp_tail_bound(N),
                'margin': margin,
            }
    raise RuntimeError('cutoff not found')


if __name__ == '__main__':
    print('sup |r4| majorant =', r4_majorant())
    print('entry constant C_r =', entry_constant())
    print('arch tail at N=237 =', arch_tail_bound(237))
    print('cutoff =', coercive_cutoff())
    print('margin N=149 =', tail_margin(149))
    print('margin N=151 =', tail_margin(151))
