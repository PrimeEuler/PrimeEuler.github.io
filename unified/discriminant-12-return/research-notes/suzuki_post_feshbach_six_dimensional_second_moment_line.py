#!/usr/bin/env python3
"""Six-dimensional post-Feshbach second-moment protected line audit.

Continues v13.327.  In the first six effective eigendirections impose five
linear constraints:

  prime leading 1/n channel = 0,
  cusp leading 1/n channel = 0,
  arch leading 1/n channel = 0,
  M1 = sum m q_m = 0,
  J2_total = 0,

where J2_total is the combined n^-3 coefficient of the prime+cusp+arch
expansion.  These constraints leave a one-dimensional line.

On this line the adverse remote tail begins at n^-4, hence its l2 norm is
O(N^-7/2).  With the same conservative analytic tail-gap bound used in the
v13.312+ chain, the Schur penalty is already below the line's formal effective
Rayleigh scale at odd cutoff N=155, essentially the first certified-coercive
scale N=151.

All displayed values are non-interval hybrid numerical data.  No positivity,
exact zero mode, lambda_1=0, RH, or GRH conclusion follows.
"""
from __future__ import annotations

SIX_ACTIVE_VECTOR = (
    -0.719862065, -0.292352536, -0.606196665,
     0.169563478,  0.0101080675, -0.000509773445,
)
COORDINATE_VECTOR = (
     0.00104650554, -0.128723745, 0.604523561, -0.716725495,
    -0.000579338894, 0.319119027, -0.0388828949, -0.0269833501,
    -0.0143328471, 0.00149349590,
)
FORMAL_EFFECTIVE_RAYLEIGH = 6.517117134862395e-11
FIRST_CROSSOVER_ODD_N = 155
M3 = 13.911277333350567


def report():
    print('six-dimensional five-constraint protected line')
    print('active vector =', SIX_ACTIVE_VECTOR)
    print('formal effective Rayleigh =', FORMAL_EFFECTIVE_RAYLEIGH)
    print('M3 =', M3)
    print('first conservative crossover odd N =', FIRST_CROSSOVER_ODD_N)
    print('tail order after cancellations: O(N^-7/2) in l2 norm')
    print('guardrail: hybrid numerical anatomy only; no positivity/RH claim')


if __name__ == '__main__':
    report()
