#!/usr/bin/env python3
"""Residual-Gram validation budget after the v13.396 finite-side reduction.

Let L0 be the fixed six-dimensional midpoint Cholesky preconditioner and let

    Y = R_W L0^{-T}

be the normalized residual operator from the six candidate-positive finite
Schur directions into the remote tail.  Then

    H = Y^* Y.

The current hybrid source-faithful upper target from v13.393 is

    h_hybrid = 0.17910434985544155,

which already consists of explicit residual-Gram accumulation through two
million plus the analytic remainder bound beyond two million.

Finite-side allowance
---------------------
v13.396 gives, under the M=3999 solve residual target ||R_F||<1e-12,

    C_pre >= c_lower I

with c_lower > 0.9958.  Together with the certified Schur-tail floor

    delta_T > 0.18225976374175623,

the allowed residual-Gram ceiling is

    H_allowed = delta_T * c_lower > 0.18149.

Residual replay perturbation
----------------------------
If Y0 is the midpoint normalized residual operator and

    ||Y-Y0|| <= eps_Y,

then

    ||Y^*Y-Y0^*Y0||
      <= 2 ||Y0|| eps_Y + eps_Y^2.

Using ||Y0|| <= sqrt(h_hybrid), the deliberately loose target

    eps_Y <= 1e-3

costs less than 8.5e-4 in normalized Gram norm.

Analytic-tail validation reserve
--------------------------------
The current beyond-two-million analytic envelope is

    tail_bound = 8.938359453827081e-4.

Even allowing a 25% outward inflation of this already conservative envelope
costs only

    0.25 * tail_bound < 2.24e-4.

Thus the combined residual-side validation reserve is below about 1.08e-3,
well inside the >2.39e-3 allowance left after the finite-side budget.

A simple fail-closed verifier target is therefore

    lambda_max(H_exact) < 0.18025,

which is comfortably below the available ceiling ~0.18149 and leaves additional
room for small fixed-preconditioner/dyadic-input rounding terms.

Guardrail: budget/contract only.  The outward replay has not yet been executed.
No exact-zero, final inertia, RH, or GRH claim follows.
"""

import math

DELTA_T = 0.18225976374175623
LAMBDA5_M3999 = 3.85764945e-8
FINITE_RAW_ERROR = 1.366219008265705e-10 + 2.5136363636363636e-11
ETA_FINITE = FINITE_RAW_ERROR/LAMBDA5_M3999
C_LOWER = 1.0-ETA_FINITE
H_ALLOWED = DELTA_T*C_LOWER

H_HYBRID = 0.17910434985544155
TAIL_BOUND = 0.0008938359453827081
EPS_Y = 1.0e-3
GRAM_REPLAY_COST = 2.0*math.sqrt(H_HYBRID)*EPS_Y + EPS_Y**2
TAIL_INFLATION_RESERVE = 0.25*TAIL_BOUND
TOTAL_RESIDUAL_VALIDATION_RESERVE = GRAM_REPLAY_COST + TAIL_INFLATION_RESERVE
H_FAIL_CLOSED_TARGET = 0.18025

if __name__ == '__main__':
    print('C lower =', C_LOWER)
    print('H allowed =', H_ALLOWED)
    print('hybrid H =', H_HYBRID)
    print('raw residual-side allowance =', H_ALLOWED-H_HYBRID)
    print('eps_Y target =', EPS_Y)
    print('Gram replay cost =', GRAM_REPLAY_COST)
    print('25% tail inflation reserve =', TAIL_INFLATION_RESERVE)
    print('total validation reserve =', TOTAL_RESIDUAL_VALIDATION_RESERVE)
    print('fail-closed H target =', H_FAIL_CLOSED_TARGET)
    assert H_ALLOWED > 0.18149
    assert H_ALLOWED-H_HYBRID > 2.39e-3
    assert GRAM_REPLAY_COST < 8.5e-4
    assert TAIL_INFLATION_RESERVE < 2.24e-4
    assert TOTAL_RESIDUAL_VALIDATION_RESERVE < 1.08e-3
    assert H_HYBRID+TOTAL_RESIDUAL_VALIDATION_RESERVE < H_FAIL_CLOSED_TARGET
    assert H_FAIL_CLOSED_TARGET < H_ALLOWED
    print('PASS: coarse residual replay budget fits inside terminal normalized margin')