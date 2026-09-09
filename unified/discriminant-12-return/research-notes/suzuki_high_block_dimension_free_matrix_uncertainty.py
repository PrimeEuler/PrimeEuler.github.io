#!/usr/bin/env python3
"""Dimension-free exact-vs-nominal uncertainty budget for the N=16001 high block.

The shifted finite pole-free block is

    B = A0_[21,16001] - 0.22 I,
    A0 = C_cusp + B_prime + K_arch.

The a-posteriori LDL certificate from v13.355-v13.356 only needs a total
operator residual below roughly 3.15e-6.  This checkpoint records why the
uncertainty in the exact matrix itself can be made negligible relative to that
budget without paying a factor equal to the 7991-dimensional matrix size.

Archimedean part
----------------
The degree-64 polynomial construction from v13.339 gives a uniform kernel
approximation

    ||h-h_32||_infty < 6.1e-14   on 0 <= t <= 2.

The corresponding convolution-kernel error on [-1,1] has Schur norm

    sup_x int_{-1}^1 |delta h(|x-y|)| dy
        <= 2 * 6.1e-14
        = 1.22e-13.

Hence every orthogonal compression, in particular the 7991-mode high block,
satisfies

    ||Delta K_arch||_2 <= 1.22e-13.

This bound is dimension-free.

Prime and cusp parts
--------------------
The prime block is generated from five logarithms/base trigonometric constants
and Chebyshev recurrences.  The cusp block is generated from rational/series
certificates for Si(n*pi), Ci(n*pi).  These scalar constants can be enclosed to
arbitrarily high precision.  For a proof implementation there is no reason to
retain the earlier coarse 1e-12-scale targeting radii; choose, for example,
scalar radii <= 1e-30.

Even the deliberately crude conversion

    ||Delta A_scalar||_2 <= N * max_ij |delta A_ij|

with N=7991 then contributes < 8e-27 whenever reconstructed entry radii are
kept below 1e-30.  This is negligible next to the arch kernel truncation.

Thus a safe design target is

    ||B_exact - B_nominal||_2 < 2e-13,

with nearly all of that allowance assigned to the archimedean polynomial
truncation.  The remaining ~3.15e-6 residual budget is therefore available for
certifying the point LDL arithmetic/backward error.

This is an analytic error-budget reduction, not yet the final factor residual
certificate.  No exact-zero, RH, or GRH conclusion follows.
"""

DIMENSION = 7991
ARCH_UNIFORM_ERROR = 6.1e-14
ARCH_OPERATOR_ERROR = 2.0 * ARCH_UNIFORM_ERROR
SCALAR_RADIUS_TARGET = 1e-30
SCALAR_CRUDE_OPERATOR_ERROR = DIMENSION * SCALAR_RADIUS_TARGET
TOTAL_MATRIX_UNCERTAINTY_TARGET = 2e-13
LDL_RESIDUAL_ALLOWANCE = 3.15e-6

if __name__ == '__main__':
    print('arch operator error <=', ARCH_OPERATOR_ERROR)
    print('crude scalar-constant operator error <=', SCALAR_CRUDE_OPERATOR_ERROR)
    print('total exact-vs-nominal target =', TOTAL_MATRIX_UNCERTAINTY_TARGET)
    print('LDL residual allowance =', LDL_RESIDUAL_ALLOWANCE)
    print('separation factor =', LDL_RESIDUAL_ALLOWANCE/TOTAL_MATRIX_UNCERTAINTY_TARGET)
    print('guardrail: point-factor backward error still needs certification')
