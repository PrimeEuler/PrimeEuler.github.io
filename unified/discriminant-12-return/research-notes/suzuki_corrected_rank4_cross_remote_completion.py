#!/usr/bin/env python3
"""Corrected rank-four cross reconstruction after Audit Rounds 20-21.

This checkpoint replaces the superseded single-Z cross model by the intended
pole-free off-diagonal formula

  G_mn = (2/pi) (n U_m-m U_n)/(m^2-n^2)
         + pi*m*n (Y_n-Y_m)/(m^2-n^2),

where

  U_n = Si(n*pi)+2 A_n,
  Y_n = n H_n.

For conditioning we use the exact gauge

  Ytilde_n = Y_n-c_inf,
  c_inf = (2/pi) exp(-1)/(1-exp(-4)),

which leaves Y_n-Y_m unchanged and satisfies Ytilde_n=O(n^-2).

For m<=16001<n, expand

  1/(m^2-n^2) = -n^-2 sum_{k>=0} (m/n)^(2k).

The corrected cross is therefore a sum of four separated channels per k:

  -(2/pi) m^(2k) U_m              * n^(-(2k+1))
  +(2/pi) m^(2k+1)                * U_n n^(-(2k+2))
  +pi      m^(2k+1) Ytilde_m      * n^(-(2k+1))
  -pi      m^(2k+1)               * Ytilde_n n^(-(2k+1)).

A K=8 (rank <=32) midpoint Gram accumulation gives the following diagnostics:

  direct near band 16003..60003       ||G|| ~= 0.94349
  remote band 60005..2,000,005        ||G|| ~= 0.39268
  coherent near+remote                 ||G|| ~= 0.99113
  after analytic completion of all pure n-power Gram tails
                                       ||G|| ~= 0.9927951

The remaining n>2,000,005 U-containing part admits the coarse Hilbert-Schmidt
bound

  ||R_U|| < 5.64e-4

using only

  |U_n| <= pi/2 + 1/(n*pi) + 2 sum_q Lambda(q)/sqrt(q) < 7.424.

At the original remote split 60005, rho=16001/60005<0.267.  The k>=8
geometric remainder of the cusp+prime channel is <3.7e-10 in Hilbert-Schmidt
norm.  The centered arch remote variable channel is lower order; a deliberately
coarse target |Ytilde_n|<=10/n^2 would make its n>2,000,005 remainder below
1.5e-9.  That decay target is to be certified separately from the exact
integration-by-parts representation.

Thus a robust final certification target is

  ||G|| < 0.995,

which allows about 1e-3 of additional interval/arithmetic padding on top of the
midpoint+analytic-tail reconstruction.

Guardrail
---------
This is a midpoint/analytic targeting checkpoint, not yet the final interval
certificate.  In particular the |Ytilde_n| decay constant and finite projected
Gram arithmetic must be outward certified before promoting ||G||<0.995 to a
theorem.  No high-complement positivity, exact-zero, RH, or GRH claim follows.
"""

NEAR_NORM_MID = 0.94349
REMOTE_TO_2M_NORM_MID = 0.39268131
COHERENT_TO_2M_NORM_MID = 0.99113
PURE_TAIL_COMPLETED_NORM_MID = 0.9927951
U_TAIL_BOUND = 5.64e-4
GEOMETRIC_K8_REMAINDER = 3.7e-10
CENTERED_ARCH_TAIL_TARGET = 1.5e-9
VALIDATION_PADDING_TARGET = 1.0e-3
FINAL_CROSS_TARGET = 0.995

if __name__ == '__main__':
    crude = (PURE_TAIL_COMPLETED_NORM_MID + U_TAIL_BOUND
             + GEOMETRIC_K8_REMAINDER + CENTERED_ARCH_TAIL_TARGET)
    print('corrected midpoint + analytic remote budget <', crude)
    print('rounded certification target =', FINAL_CROSS_TARGET)
    print('remaining nominal room =', FINAL_CROSS_TARGET-crude)
    print('guardrail: outward certification still required')
