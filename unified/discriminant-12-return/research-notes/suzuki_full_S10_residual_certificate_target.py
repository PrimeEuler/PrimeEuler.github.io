#!/usr/bin/env python3
"""Certification target for the corrected full ten-dimensional Suzuki Schur complement.

Post-audit status
-----------------
Audit Rounds 20-21 invalidated the legacy archimedean off-diagonal formula and
therefore made the old v13.365/v13.366 constants provisional.  The corrected
high complement has now been restored by v13.382-v13.385.

Let

    D = closure span{psi_n : n>=21, n odd},
    C = span{psi_1,psi_3,...,psi_19}.

Validated/certified inputs from the repaired chain are

    A0_[21,16001] >= 0.22 I,
    A0_[16003,infinity) >= 4.6733 I,
    ||G_corrected|| < 1.00303.

Hence the block-Schur lower bound is

    gamma_D = 0.22 - 1.00303^2/4.6733
            > 0.0047197.

Therefore

    ||A_DD^{-1}|| < 1/gamma_D < 211.9.

Since A_DD>0, exact congruence gives

    inertia(A0) = inertia(S10) + inertia(A_DD),

where

    S10 = A_CC - A_CD A_DD^{-1} A_DC.

Thus all possible nonpositive directions of the pole-free even-sector operator
are contained in the ten-dimensional S10 problem.

Residual certification
----------------------
For a point solve X approximating

    X_* = A_DD^{-1} A_DC

with residual

    R = A_DC - A_DD X,

we have

    ||X_*-X|| <= ||R||/gamma_D,

and consequently

    ||A_CD A_DD^{-1} A_DC - A_CD X||
      <= ||A_CD|| ||R||/gamma_D.

If Cnorm is a certified bound for ||A_CD||, then

    eta_solve = Cnorm * residual / gamma_D.

A practical total ten-dimensional Schur enclosure target remains

    eta_total < 3e-9.

For Cnorm=1 this requires

    residual < 1.42e-11.

This is a stricter solve target than the pre-audit v13.366 value, but remains
well within a high-precision structured solve.

Guardrails
----------
The old numerical fifth-Schur-eigenvalue diagnostic (~4.3e-8) is not promoted
here; it came from the pre-audit finite model and must be recomputed for the
corrected operator.  This file establishes only the corrected inverse and
residual targets.  No exact-zero, RH, or GRH conclusion follows.
"""

FINITE_LOWER = 0.22
TAIL_LOWER = 4.6733
CROSS_UPPER = 1.00303
GAMMA_D = FINITE_LOWER - CROSS_UPPER**2/TAIL_LOWER
INVERSE_BOUND = 1.0/GAMMA_D
TARGET_SCHUR_ERROR = 3e-9


def residual_target(Cnorm=1.0, eta=TARGET_SCHUR_ERROR):
    return eta*GAMMA_D/Cnorm


if __name__ == '__main__':
    print('corrected gamma_D >', GAMMA_D)
    print('||A_DD^{-1}|| <', INVERSE_BOUND)
    print('solve residual target for Cnorm=1:', residual_target())
    print('guardrail: corrected full S10 solve/certificate still pending')
