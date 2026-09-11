#!/usr/bin/env python3
"""Verifier contract for the terminal source-faithful six-direction pencil.

Purpose
-------
v13.393 found a hybrid full-tail generalized residual bound

    delta_crit_full < 0.17910434985544155

against the separately certified source-faithful Schur-tail floor

    delta_T > 0.18225976374175623.

The normalized margin is therefore about 1.731%.

The preferred proof object is NOT an interval eigenvector calculation.  Freeze
a six-column point basis Q spanning the finite candidate-positive sector and
certify the two 6x6 symmetric matrices

    B = Q^T S_F Q,
    G = R_Q^* R_Q,

including the analytic remote-tail envelope in G.

The target inequality is

    G < delta_T B.

Because B contains the tiny fifth finite-Schur scale (~3.86e-8 at M=3999),
direct LDL of delta_T B-G would expose ~1e-10 pivots.  Instead precondition by
a verified Cholesky factor B=L L^T and certify

    T = L^{-1} G L^{-T},
    lambda_max(T) < delta_T.

Equivalently, verify positive definiteness of

    delta_T I - T.

This normalized matrix has O(1e-3) absolute margin at the midpoint rather than
O(1e-10), while the separate verified Cholesky of B handles the small fifth
finite direction at high precision.

Required verifier stages
------------------------
1. Treat the stored basis Q as exact dyadic input (or replace it by an exact
   rational/MPFR-rounded basis and re-orthogonalize with a certified QR).
2. Enclose the M=3999 finite Schur matrix S_F at high precision.
3. Enclose B=Q^T S_F Q and certify B>0 by residual-certified Cholesky/LDL.
4. Enclose the projected residual Gram through n=2,000,000.
5. Add the analytic n>2,000,000 PSD tail envelope from v13.393.
6. Verified-solve with the Cholesky factor of B to enclose T.
7. Certify delta_T I-T positive by interval LDL or a residual/Weyl bound.

Design targets
--------------
The midpoint normalized slack is

    1 - 0.17910434985544155 / 0.18225976374175623
      ~= 0.0173127.

Thus a conservative normalized outward-error target of 0.005 leaves more than
a factor-three margin in the final 6x6 test.

The finite B certification is separate: because lambda_min(B) is of order
3.9e-8, its absolute enclosure must be much tighter (a design target around
1e-10 is reasonable).  This is a finite high-precision task and no longer has
to absorb the infinite tail uniformly.

Guardrails
----------
This file is a verifier architecture, not the completed validated replay.
No exact-zero, final inertia, RH, or GRH conclusion follows.
"""

DELTA_T = 0.18225976374175623
HYBRID_DELTA_CRIT = 0.17910434985544155
NORMALIZED_SLACK = 1.0 - HYBRID_DELTA_CRIT/DELTA_T
NORMALIZED_ERROR_TARGET = 0.005
FINITE_B_ABS_ERROR_TARGET = 1.0e-10

if __name__ == '__main__':
    print('certified tail floor =', DELTA_T)
    print('hybrid full-tail generalized upper =', HYBRID_DELTA_CRIT)
    print('normalized midpoint slack =', NORMALIZED_SLACK)
    print('normalized verifier error target =', NORMALIZED_ERROR_TARGET)
    print('finite B absolute error target =', FINITE_B_ABS_ERROR_TARGET)
    assert NORMALIZED_SLACK > 0.017
    assert NORMALIZED_ERROR_TARGET < NORMALIZED_SLACK/3.0
    print('PASS: verifier design has normalized margin; validated replay remains open')
