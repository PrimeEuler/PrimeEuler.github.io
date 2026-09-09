#!/usr/bin/env python3
"""O(N)-memory contract for the final 512-bit Suzuki high-block verifier.

This file turns v13.359 into a concrete streaming verifier design.

The factorization state contains only

    n, x=n^2, diagonal d, generators u,v,

for the current trailing block.  One structured LDL column is generated at a
time.  The full dense lower factor L is never stored.

Streaming factor-growth bounds
------------------------------
For the current multiplier column ell_k, update a persistent row-sum array

    row_abs[i] += |ell_k[i]|.

The absolute column sum is

    col_abs_k = 1 + sum_i |ell_k[i]|.

At the end,

    || |L| ||_inf = max_i (1 + row_abs[i]),
    || |L| ||_1   = max_k col_abs_k.

Thus the factor-growth part of the global residual certificate costs only O(N)
storage.

Two-precision local replay
--------------------------
Recommended implementation:

  * factorization state: 512-bit point MPFR, round-to-nearest;
  * checker state: >=768 or 1024 bits with outward rounding / ball arithmetic;
  * every stored 512-bit number is treated as an exact dyadic input by the
    checker.

At each step the checker reconstructs, from the current stored point state,

    b_*, ell_*, d_*', u_*', v_*'

at checker precision, compares them with the next stored point state, and uses
the v13.359 formula to enclose the local Frobenius reconstruction defect

    delta_k >= ||Delta_k||_F.

The verifier accumulates only

    local_defect_sum += delta_k.

At the end, the arithmetic factor residual is bounded by

    arithmetic_residual
      <= absL_one * absL_inf * local_defect_sum.

Certificate conditions
----------------------
A successful run should verify all of

    min_pivot > 0.25,
    arithmetic_residual < 1e-8,
    exact_vs_nominal_matrix_uncertainty < 2e-13,

and then check

    arithmetic_residual + matrix_uncertainty < 3.15e-6.

The last number is the v13.356 sufficient a-posteriori residual threshold for
positivity of

    B=A0_[21,16001]-0.22 I.

The proof output therefore needs only a compact transcript:

    dimension,
    precision bits,
    minimum pivot and its mode,
    || |L| ||_1,
    || |L| ||_inf,
    sum local Frobenius defects,
    arithmetic residual bound,
    matrix uncertainty bound,
    total residual bound,
    pass/fail.

No dense factor or dense residual matrix is part of the proof object.

Guardrail: this is an implementation contract, not a completed validated run.
No exact-zero, RH, or GRH claim follows.
"""

DIMENSION = 7991
FACTOR_BITS = 512
CHECK_BITS = 1024
PIVOT_TARGET = 0.25
ARITHMETIC_RESIDUAL_TARGET = 1e-8
MATRIX_UNCERTAINTY_TARGET = 2e-13
TOTAL_RESIDUAL_ALLOWANCE = 3.15e-6


def final_residual_bound(absL_one, absL_inf, local_defect_sum,
                         matrix_uncertainty=MATRIX_UNCERTAINTY_TARGET):
    arithmetic = absL_one*absL_inf*local_defect_sum
    return arithmetic, arithmetic + matrix_uncertainty


if __name__ == '__main__':
    print('dimension =', DIMENSION)
    print('factor precision =', FACTOR_BITS)
    print('checker precision =', CHECK_BITS)
    print('pivot target =', PIVOT_TARGET)
    print('arithmetic residual target =', ARITHMETIC_RESIDUAL_TARGET)
    print('total residual allowance =', TOTAL_RESIDUAL_ALLOWANCE)
    print('guardrail: validated 7991-step replay not yet executed')
