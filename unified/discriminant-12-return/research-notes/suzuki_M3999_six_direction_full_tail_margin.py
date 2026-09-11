#!/usr/bin/env python3
"""Hybrid source-faithful M=3999 six-direction full-tail margin.

This file records the strongest current midpoint diagnostic for the terminal
six-dimensional candidate-positive Suzuki Schur sector.

Setup
-----
C = {1,3,...,19}
F = {21,23,...,3999}
W = finite-Schur eigenvectors 5,...,10.

The matrix is the v13.387 source-faithful rank-two Suzuki matrix, with the full
PSD pole term included.  Off-diagonal high-mode entries are evaluated through

    A0_mn = -(2/pi)(n Z_m-m Z_n)/(n^2-m^2),

using the exact compressed scalar sequence

    Z_n = 2 A_n + Im psi(1/4+i n*pi/4)
          + n*pi sum_{k>=0} exp(-2 a_k)/(a_k^2+(n*pi/2)^2),
    a_k=2k+1/2.

For the diagonal archimedean term, oscillatory-weight quadrature is used rather
than ordinary adaptive quadrature; the latter becomes unreliable at sufficiently
large mode number.

Finite+remote midpoint diagnostic
---------------------------------
The generalized six-direction residual Gram was accumulated explicitly from
n=4001 through n=2,000,000.  The resulting midpoint value is

    delta_crit_mid_le_2m = 0.17821051391005885.

Analytic remainder beyond 2,000,000
-----------------------------------
For fixed finite mode m, the source-faithful off-diagonal term has leading
large-n coefficient

    A_nm = L_m/n + O(n^-2),

where

    L_m = -(2/pi) Z_m + (8 cosh(1/2)/pi) c_m

and c_m is the pole coefficient.

After the finite solve and projection into W, the leading generalized residual
channel has squared coefficient norm approximately

    ||q_norm||^2 = 1530.0464582084574.

The exact geometric denominator expansion gives a remainder bounded rowwise by

    a/n^2 + b/n^3,

and a deliberately componentwise/absolute-value evaluation at N=2,000,001
gives the total generalized-Gram tail envelope

    remaining_tail_bound = 0.0008938359453827081.

Thus the hybrid full-tail envelope is

    0.17821051391005885 + 0.0008938359453827081
      = 0.17910434985544155.

Comparison with source-faithful certified Schur-tail floor
----------------------------------------------------------
v13.392 gives

    delta_tail_cert > 0.18225976374175623.

Hence the current hybrid margin is

    margin = 0.003155413886314684.

This is NOT yet a validated-computational proof of positivity on W because the
M=3999 finite solve, finite Schur eigenbasis W, and associated projected channel
constants are still midpoint floating-point data.  The significance is that the
final finite validation now has an O(3e-3) margin rather than an O(1e-8) margin.

Guardrails
----------
* no exact-zero claim;
* no final inertia claim;
* no RH/GRH conclusion;
* the four near-zero directions remain unresolved;
* this file is a certification target, not the completed interval replay.
"""

DELTA_CRIT_TO_2M = 0.17821051391005885
TAIL_REMAINDER_BOUND = 0.0008938359453827081
FULL_HYBRID_UPPER = DELTA_CRIT_TO_2M + TAIL_REMAINDER_BOUND
CERTIFIED_TAIL_FLOOR = 0.18225976374175623
MARGIN = CERTIFIED_TAIL_FLOOR - FULL_HYBRID_UPPER
LEADING_GENERALIZED_COEFF_NORM2 = 1530.0464582084574

if __name__ == '__main__':
    print('delta_crit through 2e6 =', DELTA_CRIT_TO_2M)
    print('analytic remaining-tail bound =', TAIL_REMAINDER_BOUND)
    print('hybrid full-tail upper =', FULL_HYBRID_UPPER)
    print('certified Schur-tail floor =', CERTIFIED_TAIL_FLOOR)
    print('hybrid margin =', MARGIN)
    assert FULL_HYBRID_UPPER < CERTIFIED_TAIL_FLOOR
    assert MARGIN > 3.0e-3
    print('PASS as hybrid midpoint target only; finite M=3999 validation remains open')
