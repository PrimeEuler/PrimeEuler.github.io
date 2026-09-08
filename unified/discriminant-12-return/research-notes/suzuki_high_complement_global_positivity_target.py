#!/usr/bin/env python3
"""Corrected global-inertia target: certify the whole high complement positive.

A six-dimensional positive subspace of an infinite-dimensional operator does
NOT imply nonpositive index <= 4.  The valid route is:

  H_even = C_10 \oplus D,
  C_10 = span{n=1,3,...,19},
  D    = span{n>=21, odd}.

If D>0, exact Schur-complement inertia reduction leaves a 10-dimensional core.
Only then does a six-dimensional positive subspace of the 10x10 Schur core imply
nonpositive index <=4.

This file records numerical targeting data for D in the pole-free operator
A0=C_cusp+B_prime+K_arch; the PSD pole can be added back at the end.

Pole-free principal-block midpoint minima:
  max n=399   : 0.231953166244
  max n=1001  : 0.229033630597
  max n=2001  : 0.228022633935
  max n=4001  : 0.227509839335
  max n=6001  : 0.227336299782

Thus the finite high block appears to retain a stable gap near 0.227.

Moving-interface coupling diagnostics:
  split 2001/2003, tail sampled to 6003:  ||G||_2 ~ 0.842
  split 4001/4003, tail sampled to 10003: ||G||_2 ~ 0.854
  split 6001/6003, tail sampled to 16003: ||G||_2 ~ 0.884

The robust analytic tail gap based on ||B_prime||<2.05 is
  alpha_4003 ~ 3.2873,
  alpha_6003 ~ 3.6926,
  alpha_10003~ 4.2034.

This suggests a proof split near N=10003.  Coarse sufficient targets would be

  finite high block (21..10001) >= 0.22 I,
  full cross norm to n>=10003     < 0.95,
  tail gap alpha_10003            > 4.20.

Then the Schur penalty is <0.95^2/4.20=0.214881..., leaving >0.0051
positive margin on D.  Once D>0 is certified, the full infinite inertia reduces
rigorously to the 10x10 low-core Schur complement.

All large-block values here are numerical targeting data, not certificates.
No exact-zero, lambda_1=0, RH, or GRH claim follows.
"""

FINITE_GAPS={399:0.231953166244,1001:0.229033630597,2001:0.228022633935,4001:0.227509839335,6001:0.227336299782}
CROSS_SAMPLES={2003:0.842144657272,4003:0.854387899044,6003:0.883639329283}
ALPHA_SAMPLES={4003:3.2872752856585,6003:3.6926350482594,10003:4.2033763317563}

TARGET_FINITE_GAP=0.22
TARGET_CROSS_NORM=0.95
TARGET_TAIL_GAP=4.20

if __name__=='__main__':
    penalty=TARGET_CROSS_NORM**2/TARGET_TAIL_GAP
    print('target Schur penalty =',penalty)
    print('target high-complement margin =',TARGET_FINITE_GAP-penalty)
    print('guardrail: full cross and finite block are not yet interval certified')
