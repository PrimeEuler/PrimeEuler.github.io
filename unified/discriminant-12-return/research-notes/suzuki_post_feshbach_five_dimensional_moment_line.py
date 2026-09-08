#!/usr/bin/env python3
"""Five-dimensional post-Feshbach moment-protected line audit.

Continues v13.326.  In the first five effective Feshbach eigendirections,
impose four linear constraints:

  prime leading channel = 0,
  cusp leading channel = 0,
  arch leading channel = 0,
  M1 := sum_m m q_m = 0.

The three channel constraints remove all 1/n remote-tail terms.  The fourth
constraint removes the leading n^-2 prime+cusp remainder, so the prime+cusp
tail begins at n^-3 and its l2 tail norm is O(N^-5/2).

Using the same hybrid M=399 effective basis as v13.324, the resulting line has
formal effective Rayleigh scale about 1.08e-11.  Conservative analytic
remainder bounds cross below that scale at about N=281, dramatically improving
the v13.326 cutoff near 2250.

All decimals are non-interval hybrid numerical values.  This is not a proof of
positivity, an exact zero mode, lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

# This file records the reduction formulas and representative output from the
# M=399, 600-node/70-digit hybrid audit.  See neighboring v13.323-v13.326
# scripts for matrix construction.

FIVE_ACTIVE_VECTOR = (-0.74375440, -0.29819239, -0.58225960, 0.13646854, 0.01614907)
COORDINATE_VECTOR = (
    0.00272511436, -0.147226497, 0.629325431, -0.706646950,
    -0.000544588571, 0.285143158, -0.0327016440, -0.0209794178,
    -0.00996619055, 0.000864226848,
)
FORMAL_EFFECTIVE_RAYLEIGH = 1.082301426577611e-11
FIRST_CROSSOVER_ODD_N = 281

# Representative signed moments on the coordinate vector:
J2_PRIME_CUSP = 0.9955201180847026
M3 = 25.7547134082699


def odd_sum_bound(N: int, p: int) -> float:
    """Elementary odd-tail majorant for sum_{odd n>=N} n^{-p}."""
    return N**(-p) + N**(-(p-1))/(2.0*(p-1))


def report():
    print('five-dimensional moment-protected line')
    print('active vector =', FIVE_ACTIVE_VECTOR)
    print('formal effective Rayleigh =', FORMAL_EFFECTIVE_RAYLEIGH)
    print('J2 prime+cusp =', J2_PRIME_CUSP)
    print('M3 =', M3)
    print('first conservative crossover odd N =', FIRST_CROSSOVER_ODD_N)
    print('guardrail: hybrid numerical anatomy only; no positivity/RH claim')


if __name__ == '__main__':
    report()
