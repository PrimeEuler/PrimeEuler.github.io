#!/usr/bin/env python3
"""Explicit certificate contract for the N=155 effective core.

Nominal floating anatomy (not a certificate):

  full buffer lambda_min ~ 0.27201476017
  pole-free buffer lambda_min ~ 0.23848196475
  ||C||_2 ~ 0.73374574697
  effective lambda_5 ~ 4.32e-8

The certificate deliberately ignores the first four effective levels.

Sufficient proof data:

(A) prove B >= gamma I with gamma >= 0.15;
(B) prove ||C|| <= 0.8;
(C) choose a numerical solve X and prove ||R|| <= 8e-10 for
        R=C^T-BX;
(D) enclose M=A_CC-CX by a midpoint Mhat with
        ||M-Mhat|| <= 1.0e-8;
(E) certify lambda_5(Mhat) >= 3.5e-8.

Then

  ||F-Mhat|| <= 1e-8 + (0.8/0.15)*8e-10
               = 1.426666...e-8,

where F=A_CC-CB^{-1}C^T.  Weyl yields

  lambda_5(F) >= 3.5e-8 - 1.4267e-8 > 2.07e-8 > 0.

Therefore at most four eigenvalues of the finite 10x10 effective core can be
nonpositive.

This is a finite-core statement only.  It is not yet a statement about the
full infinite operator after remote-tail elimination, and it does not imply
positivity, an exact zero, lambda_1=0, RH, or GRH.
"""

GAMMA=0.15
C_NORM=0.8
RESIDUAL=8e-10
MIDPOINT_RADIUS=1e-8
LAMBDA5_MIDPOINT_LOWER=3.5e-8

SCHUR_RADIUS=MIDPOINT_RADIUS+(C_NORM/GAMMA)*RESIDUAL
LAMBDA5_TRUE_LOWER=LAMBDA5_MIDPOINT_LOWER-SCHUR_RADIUS

if __name__=='__main__':
    print('Schur operator radius <=',SCHUR_RADIUS)
    print('certified lambda5 target lower bound =',LAMBDA5_TRUE_LOWER)
    print('conclusion if A-E verified: finite effective nonpositive index <= 4')
