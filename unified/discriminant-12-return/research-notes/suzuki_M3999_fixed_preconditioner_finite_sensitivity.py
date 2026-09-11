#!/usr/bin/env python3
"""Finite-side sensitivity budget for the M=3999 six-direction Suzuki verifier.

This checkpoint quantifies the normalized fixed-preconditioner error coming from
(1) exact-vs-nominal matrix uncertainty and (2) the finite high-block solve.

Setup
-----
C = {1,3,...,19}, F = {21,23,...,3999}.  Let

    S = A_CC - A_CF A_FF^{-1} A_FC

and let B0 be the midpoint restriction of S to the six candidate-positive
finite-Schur directions.  The observed fifth midpoint level at M=3999 is

    lambda5(B0) = 3.85764945e-8.

The fixed midpoint Cholesky factor L0 satisfies

    ||L0^{-1}||^2 = 1/lambda_min(B0).

Therefore a raw Schur perturbation eps_S gives normalized distortion at most

    eta_B <= eps_S/lambda5(B0).

Analytic coupling bound
-----------------------
For the C-F coupling use only componentwise operator bounds already present in
the ledger:

    cusp  <= pi/2 + 0.706,
    prime <= 2.05,
    arch  <= 0.4598463265.

For the PSD pole term P=2 c c^T,

    c_n = 2 k_n cosh(1/2)/(k_n^2+1/4)
        <= 4 cosh(1/2)/(pi n).

Using sum_{odd n>=N} n^-2 <= N^-2 + (2N)^-1 and overbounding the core by the
full odd sum pi^2/8 gives

    ||P_CF|| <= 2 ||c_C|| ||c_F|| < 0.74.

Hence the deliberately rounded coupling target is

    ||A_CF|| < K = 5.53.

Schur perturbation from exact-vs-nominal matrix error
-----------------------------------------------------
Use the dimension-free matrix uncertainty

    eps_A = 2e-13

and the certified finite-high floor

    A_FF >= mu I,  mu = 0.22.

For an operator perturbation E with ||E||<=eps_A, the standard block-resolvent
estimate gives

    ||Delta S|| <= eps_A
      + 2 K eps_A/(mu-eps_A)
      + eps_A^2/(mu-eps_A)
      + K^2 eps_A/[mu(mu-eps_A)].

At K=5.53 this is <1.37e-10, so the normalized exact-vs-nominal distortion is
<0.00356.

Point-solve arithmetic target
-----------------------------
For a point solve Xhat of A_FF X=A_FC with residual

    R = A_FC - A_FF Xhat,

we have

    ||X-Xhat|| <= ||R||/mu

and therefore the induced Schur error is at most

    ||A_CF|| ||R||/mu <= K ||R||/mu.

Choosing

    ||R|| < 1e-12

gives solve-induced Schur error <2.52e-11.

Combining both budgets gives a total finite-side raw error below 1.63e-10,
normalized distortion below about 0.00423, and therefore a design target

    C = L0^{-1} B L0^{-T} >= 0.9957 I.

This is stronger than the v13.395 design requirement C>=0.995 I.

Guardrail
---------
The M=3999 eigenvalue and point solve are still midpoint data until replayed at
high precision with outward residual enclosure.  This file is an analytic
sensitivity/budget reduction, not a completed validated-computational proof.
No exact-zero, final inertia, RH, or GRH conclusion follows.
"""

import math

LAMBDA5_M3999 = 3.85764945e-8
EPS_A = 2.0e-13
MU = 0.22
K_COUPLING = 5.53
SOLVE_RESIDUAL_TARGET = 1.0e-12

SCHUR_MATRIX_UNCERTAINTY = (
    EPS_A
    + 2.0*K_COUPLING*EPS_A/(MU-EPS_A)
    + EPS_A**2/(MU-EPS_A)
    + K_COUPLING**2*EPS_A/(MU*(MU-EPS_A))
)
SOLVE_SCHUR_ERROR = K_COUPLING*SOLVE_RESIDUAL_TARGET/MU
TOTAL_FINITE_ERROR = SCHUR_MATRIX_UNCERTAINTY + SOLVE_SCHUR_ERROR
ETA_FINITE = TOTAL_FINITE_ERROR/LAMBDA5_M3999
C_LOWER = 1.0 - ETA_FINITE

DELTA_T = 0.18225976374175623
H_MID = 0.17910434985544155
H_ALLOWED = DELTA_T*C_LOWER
H_OUTWARD_ALLOWANCE = H_ALLOWED-H_MID

if __name__ == '__main__':
    print('lambda5 M3999 =', LAMBDA5_M3999)
    print('coupling target K =', K_COUPLING)
    print('matrix Schur uncertainty =', SCHUR_MATRIX_UNCERTAINTY)
    print('solve Schur error target =', SOLVE_SCHUR_ERROR)
    print('total finite-side error =', TOTAL_FINITE_ERROR)
    print('normalized eta finite =', ETA_FINITE)
    print('C lower target =', C_LOWER)
    print('residual-side outward allowance =', H_OUTWARD_ALLOWANCE)
    assert SCHUR_MATRIX_UNCERTAINTY < 1.37e-10
    assert SOLVE_SCHUR_ERROR < 2.52e-11
    assert ETA_FINITE < 0.0043
    assert C_LOWER > 0.9957
    assert H_OUTWARD_ALLOWANCE > 2.35e-3
    print('PASS: finite-side sensitivity fits inside v13.395 fixed-preconditioner budget')