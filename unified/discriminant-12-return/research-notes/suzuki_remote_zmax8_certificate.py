#!/usr/bin/env python3
"""Rigorous analytic certificate that |z_n| < 8 for all n >= 8000.

For the source-faithful scalar

  z_n = 2 A_n + Im psi(1/4 + i n*pi/4)
        - (-1)^n n*pi * sum_{j>=0} exp(-2 a_j)/(a_j^2+(n*pi/2)^2),

with a_j=2j+1/2 and
  A_n = sum_{q in {2,3,4,5,7}} Lambda(q)/sqrt(q) * sin(...),

use:
  |A_n| <= W := sum Lambda(q)/sqrt(q),

and, from the standard digamma series,
  Im psi(a+iy) = sum_{k>=0} y/((k+a)^2+y^2).
For a=1/4 the summand is positive and decreasing, so
  Im psi(1/4+iy)
    <= y/(a^2+y^2) + integral_a^infty y/(t^2+y^2) dt
    < 1/y + pi/2.

For the correction:
  sum exp(-2a_j)/(a_j^2+b^2)
    <= b^-2 * exp(-1)/(1-exp(-4)),
  b=n*pi/2,
hence
  n*pi * correction
    <= 4/(n*pi) * exp(-1)/(1-exp(-4)).

Therefore, for n>=8000,

 |z_n| <
   2W + pi/2
   + 4/(n*pi)
   + 4/(n*pi)*exp(-1)/(1-exp(-4)).

The RHS is decreasing in n, so it suffices to evaluate it outward at n=8000.
"""
from __future__ import annotations

import mpmath as mp

iv=mp.iv
iv.dps=80

N=iv.mpf(8000)
PI=iv.pi

W=(
    iv.log(2)/iv.sqrt(2)
    + iv.log(3)/iv.sqrt(3)
    + iv.log(2)/2
    + iv.log(5)/iv.sqrt(5)
    + iv.log(7)/iv.sqrt(7)
)

S=iv.exp(-1)/(1-iv.exp(-4))

BOUND=(
    2*W
    + PI/2
    + 4/(N*PI)
    + 4*S/(N*PI)
)

print("W interval =",W)
print("correction geometric sum interval =",S)
print("uniform |z_n| bound for n>=8000 =",BOUND)
print("upper endpoint =",BOUND.b)

if not (BOUND < iv.mpf(8)):
    raise RuntimeError(("Zmax=8 certificate failed",BOUND))

print("PASS: |z_n| < 8 for every n>=8000")
