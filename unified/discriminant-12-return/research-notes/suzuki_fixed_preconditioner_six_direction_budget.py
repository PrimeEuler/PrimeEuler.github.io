#!/usr/bin/env python3
"""Fixed-preconditioner budget for the terminal six-direction Suzuki verifier.

Instead of interval-Cholesky factoring an interval B, freeze a midpoint factor
L0 (stored as exact dyadic verifier input) from a high-precision point matrix B0.
For the exact six-dimensional pencil define

    C = L0^{-1} B L0^{-T},
    H = L0^{-1} G L0^{-T}.

Then

    G < delta_T B

is equivalent to

    H < delta_T C.

This formulation decouples the two validation tasks:

  * finite-Schur validation: prove C >= (1-eta_B) I;
  * residual-Gram validation: prove lambda_max(H) <= h_upper.

It suffices that

    h_upper < delta_T (1-eta_B).

Using the v13.393 midpoint generalized value

    h_mid = 0.17910434985544155

and the v13.392 certified tail floor

    delta_T = 0.18225976374175623,

the raw normalized slack is

    delta_T-h_mid = 0.003155413886314684.

Budget examples:

  eta_B=0.0025  -> residual-side outward allowance ~0.00269976
  eta_B=0.0050  -> residual-side outward allowance ~0.00224412
  eta_B=0.0075  -> residual-side outward allowance ~0.00178847

Thus eta_B=0.005 is a natural conservative design point.  It asks only that
finite-Schur validation preserve B to 0.5% in the B0 metric while still leaving
more than 2.2e-3 absolute normalized room for the entire residual-Gram replay.

Important: proving C >= 0.995 I is NOT the same as proving ||B-B0||<0.5% in raw
Euclidean norm.  The verifier should work directly with the preconditioned
matrix C, because the tiny fifth finite-Schur direction makes raw absolute
conditioning misleading.

Guardrail: architecture/budget only; no completed validated replay, exact-zero,
final inertia, RH, or GRH conclusion.
"""

DELTA_T = 0.18225976374175623
H_MID = 0.17910434985544155
ETA_B = 0.005
C_LOWER = 1.0 - ETA_B
H_ALLOWED = DELTA_T * C_LOWER
H_OUTWARD_ALLOWANCE = H_ALLOWED - H_MID
RAW_SLACK = DELTA_T - H_MID
NORMALIZED_SLACK = RAW_SLACK / DELTA_T

if __name__ == '__main__':
    print('delta_T =', DELTA_T)
    print('h_mid =', H_MID)
    print('raw normalized-coordinate slack =', RAW_SLACK)
    print('relative slack =', NORMALIZED_SLACK)
    print('C lower target =', C_LOWER)
    print('permitted H upper =', H_ALLOWED)
    print('H outward allowance after C budget =', H_OUTWARD_ALLOWANCE)
    assert C_LOWER == 0.995
    assert H_OUTWARD_ALLOWANCE > 0.0022
    print('PASS: fixed-preconditioner design retains >2.2e-3 residual-side margin')
