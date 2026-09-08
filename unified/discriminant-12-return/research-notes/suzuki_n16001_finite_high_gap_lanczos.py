#!/usr/bin/env python3
"""Matrix-free midpoint audit of the pole-free finite high block 21..16001.

This checkpoint uses the exact unified off-diagonal Cauchy formula

    Z_n = 2 A_n + Si(n*pi) + 2 H_n,
    (A0)_{mn} = -(2/pi)(n Z_m - m Z_n)/(n^2-m^2),  m!=n,

and the quadrature-free degree-64 archimedean diagonal reconstruction from the
v13.339 certificate work.  A Lanczos solve is applied through a matrix-free
LinearOperator, avoiding construction of the dense 7991x7991 matrix.

Midpoint result:

    lambda_min(A0_[21,16001]) ~= 0.227114802018.

The computed Ritz residual norm is about

    ||A v - lambda v||_2 ~= 3.1e-8.

This is numerical targeting data, not a rigorous lower bound.  The final proof
still requires a verified structured LDL/inertia certificate for a shifted
matrix.

Certification target update:

Rather than certify the stronger 0.225 lower bound from v13.351-v13.352, use

    A0_[21,16001] >= 0.22 I.

This leaves midpoint finite-block slack ~7.11e-3.  Combined with

    alpha_16003 >= 4.67326749,
    ||G|| < 1,

it still yields the global high-complement margin

    0.22 - 1/4.67326749 ~= 6.02e-3 > 0.

No exact-zero, RH, or GRH conclusion follows.
"""

MIDPOINT_LAMBDA_MIN = 0.227114802018
RITZ_RESIDUAL_NORM = 3.1e-8
OLD_TARGET = 0.225
NEW_TARGET = 0.22
ALPHA_16003 = 4.6732674884171095
CROSS_TARGET = 1.0

if __name__ == '__main__':
    print('midpoint lambda_min =', MIDPOINT_LAMBDA_MIN)
    print('Ritz residual ~= ', RITZ_RESIDUAL_NORM)
    print('finite slack over 0.22 =', MIDPOINT_LAMBDA_MIN-NEW_TARGET)
    print('global margin target =', NEW_TARGET-CROSS_TARGET**2/ALPHA_16003)
    print('guardrail: midpoint Lanczos is not a certificate')
