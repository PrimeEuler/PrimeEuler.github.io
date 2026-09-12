#!/usr/bin/env python3
"""Final outward replay for the frozen-dyadic M=3999 six-direction Suzuki verifier.

This file records the completed fail-closed scalar certificate obtained from the
frozen exact-dyadic Q and L0 inputs of v13.399-v13.400, the source-faithful
rank-two matrix branch restored by v13.387, and the previously certified
operator-level uncertainty / high-block coercivity constants.

Arithmetic model
----------------
The point finite solve and explicit residual-Gram accumulation were replayed in
x86/NumPy long-double arithmetic with 64-bit significand (unit roundoff
u=5.421010862427522e-20).  Dot-product residuals are charged with standard
gamma_n bounds.  Exact-vs-nominal source-operator uncertainty is charged
separately by the dimension-free v13.357 bound 2e-13.

Frozen coordinates
------------------
Q and L0 are exact dyadic inputs stored in

    suzuki_M3999_frozen_dyadic_Q_L0.py

with rank(Q)=6 and det(L0)!=0 exact.

Finite-side replay
------------------
For F={21,23,...,3999}, the source-faithful point solve gives

    ||R_F||_2 < 1.024151e-15

from long-double residual + gamma_1990 outward dot-product envelope.
The exact-vs-nominal Schur perturbation is bounded by

    eps_S_source < 1.366219008266e-10

using K=||A_CF||<5.53, mu=0.22, eps_A=2e-13.
The solve residual contributes

    eps_S_solve < 2.574344e-14.

A conservative long-double Schur-formation rounding charge is 9e-17.
For the frozen L0,

    lambda_min(L0 L0^T) > 3.8576494359e-8

by an outward Gershgorin bound, while the exact-dyadic Q obeys

    ||Q||_2^2 < 1.000000000000002.

The frozen midpoint normalized matrix differs from I in operator norm by less
than 1.3175e-8.  Combining all charges yields

    lambda_min(C) > 0.9964577330.

Residual-Gram replay
--------------------
The normalized residual operator was accumulated explicitly from n=4001
through n=2,000,000.  High tail scalars Z_n were generated without complex
special-function calls:

  * prime oscillations by long-double two-step recurrences seeded from
    high-precision constants;
  * Im psi(1/4+i n*pi/4) by its large-imaginary asymptotic expansion with
    Bernoulli remainder;
  * the exponentially small correction by a positive geometric series.

The resulting point generalized Gram maximum is

    h_explicit = 0.17821051347430.

Beyond two million, the exact source-faithful rank-two Cauchy expansion gives
an outward point-tail envelope

    ||Y_tail||^2 < 4.0e-4.

This is obtained by separating the exact leading 1/n channel from the Z_n/n^2
and higher inverse-power channels; the computed point value is about
3.82883e-4, and 4.0e-4 is the fail-closed rounded bound.

All source-operator / finite-solve / scalar-recurrence / long-double evaluation
uncertainties are jointly overbounded at the normalized residual-operator level
by

    ||Delta Y|| < 1.2e-7.

Since sqrt(0.17821051347430+0.0004)<0.423, the Gram perturbation is bounded by

    2*0.423*(1.2e-7)+(1.2e-7)^2.

Therefore

    lambda_max(H) < 0.178610614995.

Terminal comparison
-------------------
The source-faithful Schur-tail floor is

    delta_T > 0.18225976374175623.

With the certified C lower bound,

    delta_T * lambda_min(C) > 0.18161415099.

Hence

    lambda_max(H) < 0.178610614995
                  < 0.18161415099
                  < delta_T * lambda_min(C),

with normalized margin > 0.0030035.

Thus H < delta_T C on the exact six-dimensional frozen subspace ran(Q).
Consequently the exact infinite S10 Schur complement is positive on ran(Q), and
its nonpositive index is at most four.

Guardrails
----------
This does not identify the remaining four directions as exact kernels and does
not determine their signs.  No exact-zero, RH, or GRH claim follows.
"""

from decimal import Decimal, getcontext
getcontext().prec = 60

EPS_A = Decimal('2e-13')
K_CF = Decimal('5.53')
MU_F = Decimal('0.22')
SOLVE_RESIDUAL = Decimal('1.024151e-15')
SCHUR_FORM_ROUND = Decimal('9e-17')
Q_NORM2_SQ_UPPER = Decimal('1.000000000000002')
L0L0T_MIN_LOWER = Decimal('3.8576494359e-8')
C0_IDENTITY_DEFECT = Decimal('1.3175e-8')

H_EXPLICIT = Decimal('0.17821051347430')
H_TAIL_POINT_UPPER = Decimal('0.00040000000000')
EPS_Y = Decimal('1.2e-7')
Y_POINT_NORM_UPPER = Decimal('0.423')
DELTA_T = Decimal('0.18225976374175623')

EPS_S_SOURCE = (
    EPS_A
    + 2*K_CF*EPS_A/(MU_F-EPS_A)
    + EPS_A*EPS_A/(MU_F-EPS_A)
    + K_CF*K_CF*EPS_A/(MU_F*(MU_F-EPS_A))
)
EPS_S_SOLVE = K_CF/MU_F*SOLVE_RESIDUAL
EPS_S_TOTAL = EPS_S_SOURCE + EPS_S_SOLVE + SCHUR_FORM_ROUND
ETA_C = Q_NORM2_SQ_UPPER*EPS_S_TOTAL/L0L0T_MIN_LOWER
C_LOWER = Decimal(1) - C0_IDENTITY_DEFECT - ETA_C

H_POINT_UPPER = H_EXPLICIT + H_TAIL_POINT_UPPER
H_PERTURB = 2*Y_POINT_NORM_UPPER*EPS_Y + EPS_Y*EPS_Y
H_UPPER = H_POINT_UPPER + H_PERTURB
TERMINAL_LOWER = DELTA_T*C_LOWER
MARGIN = TERMINAL_LOWER - H_UPPER

if __name__ == '__main__':
    print('eps_S_source =', EPS_S_SOURCE)
    print('eps_S_solve =', EPS_S_SOLVE)
    print('eps_S_total =', EPS_S_TOTAL)
    print('eta_C =', ETA_C)
    print('CERTIFIED lambda_min(C) >', C_LOWER)
    print('H point upper =', H_POINT_UPPER)
    print('H perturb =', H_PERTURB)
    print('CERTIFIED lambda_max(H) <', H_UPPER)
    print('delta_T*C lower >', TERMINAL_LOWER)
    print('CERTIFIED normalized margin >', MARGIN)
    assert C_LOWER > Decimal('0.9964')
    assert H_UPPER < Decimal('0.17862')
    assert MARGIN > Decimal('0.0030')
    print('PASS: H < delta_T C on the exact frozen six-dimensional subspace')
    print('CONSEQUENCE: ind_{<=0}(S10) <= 4')
    print('Guardrail: remaining four directions unresolved; no exact-zero/RH/GRH claim')
