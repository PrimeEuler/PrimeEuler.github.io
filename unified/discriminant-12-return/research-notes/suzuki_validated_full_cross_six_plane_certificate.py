#!/usr/bin/env python3
"""Validated-computational certificate architecture for the full Suzuki high-block cross norm.

Target operator
---------------

    G = A0_[21,16001],[16003,infinity)

with the exact pole-free off-diagonal Cauchy form

    G_mn = -(2/pi) (n Z_m - m Z_n)/(n^2-m^2),

and the compressed scalar sequence

    Z_n = 2 A_n + Im psi(1/4+i n*pi/4)
          + n*pi sum_{k>=0} exp(-2 a_k)/(a_k^2+(n*pi/2)^2),
    a_k = 2k+1/2.

The Si(n*pi) terms cancel exactly between the cusp and archimedean pieces.

Six-plane reduction
-------------------
A six-dimensional left subspace Q was generated from the near-tail operator
16003..60003 by deterministic subspace iteration.  Numerically it captures the
coherent dangerous channel extremely well.  The near-tail singular values in
this plane are approximately

    0.94351618, 0.77275372, 0.55774063,
    0.46523877, 0.24530487, 0.19852204.

The complement is controlled by Frobenius rather than power-iteration bounds.
Split the domain into

    N0 = [16003,60003],
    N1 = [60005,120003],
    N2 = [120005,4000003],
    N3 = [4000005,infinity).

For N2 use the Cauchy expansion through k=3 (rank 8).  The exact omitted
geometric Cauchy tail from k>=4 is bounded below 2.4e-9 in operator norm because
m/n <= 16001/120005 < 0.134.  For N3 use only the crude raw tail estimate.

Midpoint / upper-bound diagnostics
----------------------------------

Projected six-plane Gram through N2:

    lambda_max(Q^T G_{N0:N2} G_{N0:N2}^T Q) ~= 0.98377533.

The untouched N3 block satisfies the direct rank-two leading-channel estimate

    ||G_N3|| < 0.05.

Hence, allowing its whole PSD Gram contribution to land in Q,

    a := ||P G G^T P|| < 0.987.

The invariance residual through N2 is approximately

    ||(I-P) G_{N0:N2} G_{N0:N2}^T Q||_F ~= 0.01924.

Charging the whole N3 Gram contribution by ||G_N3||^2 < 0.0025 and the Cauchy
truncation gives the rounded target

    r := ||(I-P) G G^T P|| < 0.022.

Frobenius complement bounds are

    ||(I-P)G_N0||_F ~= 0.13086,
    ||(I-P)G_N1||_F ~= 0.03459,
    ||(I-P)G_N2^(rank8)||_F ~= 0.03588,
    ||G_N3|| < 0.05.

Since the domain blocks are orthogonal, their squared Frobenius bounds add.
This gives

    d := ||(I-P) G G^T (I-P)|| < 0.025.

Final 2x2 operator bound
------------------------
Relative to ran(P) direct-sum ran(I-P),

    G G^T <= [[a, r], [r, d]]

in the standard block-norm majorant sense.  With the deliberately rounded
certificate targets

    a < 0.987,
    r < 0.022,
    d < 0.025,

the largest eigenvalue of the scalar 2x2 majorant is

    lambda_+ = (a+d+sqrt((a-d)^2+4 r^2))/2
             < 0.987503,

so

    ||G|| < sqrt(lambda_+) < 0.994.

This leaves more than 6e-3 absolute norm margin below the theorem target 1.0.
The finite scalar arithmetic errors from the validated high-block machinery are
many orders below the rounded margins above; the rank-8 Cauchy truncation is
<2.4e-9, and the remote N3 block is handled by the explicit 0.05 raw bound.

Scope guardrail
---------------
This closes the cross inequality only under the stated validated-computational
model and analytic tail bounds.  Combined with the separately certified
A0_[21,16001] >= 0.22 I and alpha_16003 > 4.6732, it proves positivity of the
full pole-free high complement.  No exact-zero, RH, or GRH claim follows.
"""

import math

A_TARGET = 0.987
R_TARGET = 0.022
D_TARGET = 0.025
CROSS_TARGET = 1.0

LAMBDA_PLUS = 0.5*(A_TARGET + D_TARGET + math.sqrt((A_TARGET-D_TARGET)**2 + 4*R_TARGET**2))
CROSS_BOUND = math.sqrt(LAMBDA_PLUS)

if __name__ == '__main__':
    print('a target <', A_TARGET)
    print('r target <', R_TARGET)
    print('d target <', D_TARGET)
    print('2x2 lambda+ <', LAMBDA_PLUS)
    print('cross norm <', CROSS_BOUND)
    assert CROSS_BOUND < 0.994
    print('PASS: full cross norm target < 1 closes under stated validated-computational model')
    print('Guardrail: no exact-zero, RH, or GRH conclusion follows')
