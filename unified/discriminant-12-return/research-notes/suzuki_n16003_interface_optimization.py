#!/usr/bin/env python3
"""Midpoint targeting audit for the corrected global high-complement route.

The valid global target is positivity of

    D = closure span{psi_n : n>=21, n odd}

for the pole-free operator A0.  Once D>0 is certified, exact Schur-complement
inertia reduces the infinite problem to the ten low modes n=1,...,19.

This checkpoint compares the N=10003 and N=16003 interfaces using the unified
Cauchy sequence

    Z_n = 2 A_n + Si(n*pi) + 2 H_n,

for which

    (A0)_{mn} = -(2/pi) (n Z_m - m Z_n)/(n^2-m^2),  m!=n.

A matrix-free power iteration on the exact midpoint formula gives the following
cross-coupling diagnostics.

N=10003, finite side 21..10001:
  tail 10003..30003:  ||G||_2 ~= 0.89074
  tail 10003..60003:  ||G||_2 ~= 0.92771
  band 60005..120003: ||G||_2 ~= 0.22266

Thus N=10003 is plausible but becomes close to the Schur threshold after the
fully remote tail is added.

N=16003, finite side 21..16001:
  tail 16003..60003:  ||G||_2 ~= 0.94323

Using the robust tail-gap model based on ||B_prime||<2.05,

  alpha_16003 ~= alpha_10003 + log(16003/10003)
               ~= 4.67326749.

If the finite high block is certified with the deliberately coarse lower bound

  A0_[21,16001] >= 0.225 I,

then the admissible full cross norm is

  sqrt(0.225 * 4.67326749) ~= 1.02542.

That gives substantially more room than the N=10003 target (~0.97).  The
remaining task is to certify the remote n>=60005 cross by the low-rank Cauchy
expansion and show the full cross stays below a rounded target such as 1.00.

All values in this file are midpoint numerical targeting data, not interval
certificates.  No exact-zero, RH, or GRH conclusion follows.
"""

import math

ALPHA_10003 = 4.2033763317563
N1 = 10003
N2 = 16003
ALPHA_16003 = ALPHA_10003 + math.log(N2/N1)
FINITE_TARGET = 0.225
ALLOWABLE_CROSS = math.sqrt(FINITE_TARGET*ALPHA_16003)

CROSS_10003_30003 = 0.8907354
CROSS_10003_60003 = 0.9277058
CROSS_60005_120003 = 0.2226649
CROSS_16003_60003 = 0.9432312

if __name__ == '__main__':
    print('alpha_16003 =', ALPHA_16003)
    print('allowable full cross =', ALLOWABLE_CROSS)
    print('midpoint cross 16003..60003 =', CROSS_16003_60003)
    print('guardrail: remote tail and finite block still require certification')
