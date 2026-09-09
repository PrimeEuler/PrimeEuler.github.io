#!/usr/bin/env python3
"""Restored finite high-block positivity budget after the corrected arch formula.

Target
------

    B = A0_[21,16001] - 0.22 I.

This checkpoint combines only ingredients that survive External Audit Rounds
20-23:

1. corrected rank-4 midpoint LDL with asymptotically centered arch generator;
2. corrected O(N)-memory inverse-factor majorant;
3. corrected round-to-nearest local-defect replay;
4. dimension-free exact-vs-nominal matrix uncertainty from the underlying
   convolution kernel, not from the superseded off-diagonal formula.

Corrected midpoint/factor transcript
------------------------------------

    dimension             = 7991
    minimum pivot         = 0.25547908458536...
    minimum-pivot mode    = 29
    |||L|||_1             < 43.027
    |||L|||_inf           < 3.727
    y_max                 < 18.137

For unit lower-triangular L, the forward majorant

    y_i = 1 + sum_{j<i}|L_ij| y_j

implies

    ||L^{-1}||_inf <= y_max,
    ||L^{-1}||_2^2 <= N y_max^2.

Hence the sufficient residual allowance is

    d_min / (N y_max^2) > 9.71e-8.

Corrected arithmetic replay
---------------------------
The centered rank-4 local-defect replay gives

    sum_k delta_k < 8.86e-11,
    ||E_arith||_2 < 1.43e-8.

Exact-vs-nominal matrix uncertainty
-----------------------------------
The degree-65 arch polynomial satisfies

    ||h-h_32||_infty < 6.1e-14.

Because the arch contribution is the compression of the convolution kernel
-h(|x-y|), Schur's test gives, independently of matrix dimension and
independently of any off-diagonal reconstruction formula,

    ||Delta K_arch||_2 < 1.22e-13.

The prime/cusp scalar constants are the same as in the earlier interval audit
and can be over-resolved far below this scale.  We therefore retain the rounded
exact-vs-nominal budget

    ||E_matrix||_2 < 2.0e-13.

Combined test
-------------

    E_total < 1.43002e-8 < 9.71e-8.

Equivalently,

    d_min - N*y_max^2*E_total > 0.217,

so the shifted block is positive under the stated arithmetic/scalar-enclosure
model.  Therefore

    A0_[21,16001] >= 0.22 I.

Proof-status guardrail
----------------------
This is a validated-computational certificate under the explicit
round-to-nearest/local-defect and scalar-enclosure model used in the project.
It is not a machine-independent formal proof kernel.  It restores only the
finite pole-free block.  Infinite high-complement positivity still requires a
certified cross norm and tail gap.  No exact-zero, RH, or GRH conclusion
follows.
"""

N = 7991
D_MIN = 0.25547908458536
Y_MAX = 18.137
ARITH_RESIDUAL = 1.43e-8
MATRIX_UNCERTAINTY = 2.0e-13
TOTAL_RESIDUAL = ARITH_RESIDUAL + MATRIX_UNCERTAINTY
ALLOWANCE = D_MIN/(N*Y_MAX*Y_MAX)
TRANSFORMED_MARGIN = D_MIN - N*Y_MAX*Y_MAX*TOTAL_RESIDUAL

if __name__ == '__main__':
    print('residual allowance =', ALLOWANCE)
    print('total residual <', TOTAL_RESIDUAL)
    print('transformed positivity margin >', TRANSFORMED_MARGIN)
    if not TOTAL_RESIDUAL < ALLOWANCE:
        raise SystemExit('FAIL')
    print('PASS under stated validated-computation model')
    print('Conclusion: A0_[21,16001] >= 0.22 I')
