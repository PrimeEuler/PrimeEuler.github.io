#!/usr/bin/env python3
"""Certification target for the full ten-dimensional Suzuki Schur complement.

After v13.365 the even-sector high complement

    D = closure span{psi_n : n>=21, n odd}

is positive.  A rounded rigorous lower bound from the finite/high-tail Schur
estimate is

    gamma_D = 0.22 - 0.994^2/4.6732 > 8.57e-3.

Hence

    ||A_DD^{-1}|| < 1/gamma_D < 116.7.

The infinite inertia is therefore exactly the inertia of

    S10 = A_CC - A_CD A_DD^{-1} A_DC,

where C is the ten low odd modes 1,3,...,19.

For a point solve X approximating A_DD^{-1} A_DC with residual

    R = A_DC - A_DD X,

one has

    ||X_* - X|| <= ||R||/gamma_D

and therefore

    ||A_CD A_DD^{-1} A_DC - A_CD X||
        <= ||A_CD|| ||R|| / gamma_D.

If Cnorm denotes a certified bound for ||A_CD||, the final ten-dimensional
Schur error budget may be taken as

    eta_solve = Cnorm * residual / gamma_D.

Earlier finite-buffer diagnostics placed the fifth ordered Schur eigenvalue
near 4.3e-8.  Thus a practical final target is eta_total < 1e-8, preferably
3e-9, which requires solve residuals in the 1e-11--1e-10 range for Cnorm of
order one.  This is entirely compatible with high-precision structured solves.

Guardrail: the earlier 4.3e-8 value is numerical finite-section targeting data.
The full S10 has not yet been certified and no RH/GRH conclusion follows.
"""

GAMMA_D = 0.22 - 0.994**2/4.6732
INVERSE_BOUND = 1.0/GAMMA_D
TARGET_SCHUR_ERROR = 3e-9


def residual_target(Cnorm=1.0, eta=TARGET_SCHUR_ERROR):
    return eta*GAMMA_D/Cnorm


if __name__ == '__main__':
    print('gamma_D >', GAMMA_D)
    print('||A_DD^{-1}|| <', INVERSE_BOUND)
    print('solve residual target for Cnorm=1:', residual_target())
    print('guardrail: full S10 solve/certificate still pending')
