#!/usr/bin/env python3
"""Analytic one-sided archimedean remainder bound and pole positivity audit.

For Suzuki's a=1 even-v sector, write the smooth archimedean remainder operator
with kernel

    K_r(x,y) = -r''(|x-y|),

where

    r(t)=1/4 sum_{m>=2} zeta(2-m,1/4)(-2)^m t^m/m!.

The exponential generating function for Hurwitz-zeta values gives exactly

    r''(t)=e^{-t/2}/(1-e^{-2t}) - 1/(2t)
          = e^{t/2}/(2 sinh t) - 1/(2t).

With u=t/2,

    r''(t)=1/4(csch u + sech u - 1/u).

On 0<u<=1, use

    sinh(u)/u <= 1/(1-u^2/6),

which follows coefficientwise from
1/(2k+1)! <= 1/6^k for k>=1. Also

    1/(1-u^2/6)^2 < 1+u^2/2 <= cosh u,

because

    (1+z/2)(1-z/6)^2-1 = z(z^2-10z+12)/72 > 0

for 0<z<=1. Hence sinh^2 u < u^2 cosh u and therefore

    csch(u)coth(u) > 1/u^2.

Thus d/du[4 r''(2u)] < 0, so r'' is strictly decreasing on (0,2].
Therefore r' is concave and, for x in [-1,1],

    int_{-1}^1 r''(|x-y|)dy = r'(1+x)+r'(1-x) <= 2r'(1).

Since the kernel is nonpositive, Schur yields the exact analytic norm bound

    ||K_r|| <= 2 r'(1),

and direct integration gives

    r'(t)=1/2[log(4 tanh(t/4)/t)+atan(sinh(t/2))].

Therefore

    ||K_r|| <= log(4 tanh(1/4)) + atan(sinh(1/2))
             = 0.4598463265063248...

This replaces the older analytic bound 2.0563386856...

Pole term: p(t)=-8(cosh(t/2)-1), so -p''(x-y)=2cosh((x-y)/2).
For even v,

    Q_pole(v)=2|<v,cosh(x/2)>|^2 >= 0,

because the sinh rank-one piece vanishes by parity. Hence the pole contributes
zero negative coercivity cost in this sector.

Combining the v13.310 prime bound 2.044764260347282, Hilbert cost pi/2, the
new archimedean cost, zero pole cost, and the certified cusp-tail estimate
gives first sufficient odd cutoff N=237.

No RH/GRH, kernel, or lambda_1=0 conclusion follows.
"""
from __future__ import annotations

import math

PRIME_BOUND = 2.044764260347282


def arch_bound() -> float:
    return math.log(4.0*math.tanh(0.25)) + math.atan(math.sinh(0.5))


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
    offdiag = 2.0*alpha*math.sqrt((math.pi**2/12.0)*odd_sum6_tail_bound(N))
    C_diag = 2.0/math.pi**2 + 2.0/math.pi**3 + 2.0/math.pi**4 + 6.0/math.pi**5
    diagonal = C_diag*math.sqrt(odd_sum4_tail_bound(N))
    return rank_one + offdiag + diagonal


def coercive_cutoff(max_search: int = 10000) -> dict:
    for N in range(1, max_search+1, 2):
        total = math.pi/2.0 + PRIME_BOUND + arch_bound() + cusp_tail_bound(N)
        margin = math.log(N/4.0) - total
        if margin > 0:
            return {
                'N': N,
                'prime_bound': PRIME_BOUND,
                'arch_bound': arch_bound(),
                'pole_negative_cost': 0.0,
                'cusp_tail': cusp_tail_bound(N),
                'total_tail_bound': total,
                'margin': margin,
            }
    raise RuntimeError('cutoff not found')


if __name__ == '__main__':
    print('arch bound =', arch_bound())
    print('coercive cutoff =', coercive_cutoff())
