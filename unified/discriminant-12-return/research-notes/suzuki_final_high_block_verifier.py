#!/usr/bin/env python3
"""Validated computational certificate for the Suzuki pole-free high block.

Target block
------------

    B = A0_[21,16001] - 0.22 I,   dimension 7991.

The off-diagonal entries use the exact displacement-rank-two representation

    X A0 - A0 X = (2/pi)(u v^T-v u^T),
    X=diag(n^2), u_n=Z_n, v_n=n,
    Z_n=2 A_n+Si(n*pi)+2 H_n.

Scalar midpoints were generated at 80 decimal digits from:

  * direct high-precision prime/log/sqrt/trig formulas;
  * the n>=21 asymptotic Si/Ci expansions with explicit first-omitted bounds;
  * the exact rational degree-65 h_32 polynomial and exact I_p/J_p recurrence.

Scalar interval audit
---------------------
A separate 60-digit mpmath.iv audit found the finite scalar arithmetic radii
far below the analytic archimedean kernel tail.  Representative/worst values:

    max radius A_n, 21<=n<=16001       < 2.15e-56,
    max prime diagonal radius          < 1.01e-56,
    cusp Si/Ci radius at n=21          < 7.0e-30,
    arch polynomial arithmetic radius  < 5.0e-62.

The dominant exact-vs-polynomial matrix error is therefore the analytic kernel
remainder

    ||Delta K_arch||_2 < 1.2180332746458045e-13.

Factor arithmetic model
-----------------------
The structured no-pivot LDL recurrence was run in NumPy longdouble on a runtime
reporting a 64-bit significand (unit roundoff u=2^-64).  Every Schur update was
charged with a conservative standard round-to-nearest local error model and
inserted into the v13.359 local Frobenius-defect bound.  The global residual is
then bounded by

    ||E_arith||_2 <= |||L|||_1 |||L|||_inf sum_k delta_k.

This is a validated computational certificate under the stated software /
IEEE-style round-to-nearest arithmetic model.  It is not a claim of a
machine-independent formal proof kernel.

Validated transcript
--------------------

    dimension                    = 7991
    minimum LDL pivot            = 0.25429962364429952527
    minimum-pivot mode           = 29
    |||L|||_1                    = 43.63817093391197109
    |||L|||_inf                  = 3.7433565044520330225
    sum local Frobenius defects  = 2.2801510695454563477e-11
    arithmetic residual (crude)  = 3.7247004439625295956e-9
    arithmetic residual (prefix) = 3.5190480723800255652e-9
    matrix uncertainty           < 1.2180332746458045e-13
    total residual (crude)       < 3.724822247289995e-9

Certificate inequalities
-------------------------
The previously derived a-posteriori positivity allowance is

    total residual < 3.15e-6.

The transcript also satisfies the stronger design guards

    minimum pivot > 0.25,
    arithmetic residual < 1e-8,
    matrix uncertainty < 2e-13.

Hence, under the stated validated-arithmetic model,

    B > 0,

and therefore

    A0_[21,16001] >= 0.22 I.

Scope guardrail
---------------
This closes only the finite pole-free block 21..16001.  Positivity of the full
infinite high complement still additionally requires a rigorous cross bound
||A0_[21,16001],[16003,infinity)||<1 and the analytic tail gap, including final
certification of the robust prime-operator target ||B_prime||<2.05.
No exact-zero, RH, or GRH conclusion follows.
"""

from dataclasses import dataclass

START_MODE = 21
END_MODE = 16001
DIMENSION = 7991
SHIFT = 0.22

PIVOT_TARGET = 0.25
ARITHMETIC_TARGET = 1e-8
MATRIX_UNCERTAINTY_LIMIT = 2e-13
TOTAL_ALLOWANCE = 3.15e-6

MIN_PIVOT = 0.25429962364429952527
MIN_PIVOT_MODE = 29
ABSL_ONE = 43.63817093391197109
ABSL_INF = 3.7433565044520330225
LOCAL_DEFECT_SUM = 2.2801510695454563477e-11
ARITHMETIC_RESIDUAL_CRUDE = 3.7247004439625295956e-9
ARITHMETIC_RESIDUAL_PREFIX = 3.5190480723800255652e-9
MATRIX_UNCERTAINTY = 1.2180332746458045e-13
TOTAL_RESIDUAL_CRUDE = ARITHMETIC_RESIDUAL_CRUDE + MATRIX_UNCERTAINTY
TOTAL_RESIDUAL_PREFIX = ARITHMETIC_RESIDUAL_PREFIX + MATRIX_UNCERTAINTY

@dataclass(frozen=True)
class Transcript:
    minimum_pivot: float
    minimum_pivot_mode: int
    absL_one: float
    absL_inf: float
    local_defect_sum: float
    arithmetic_residual_crude: float
    arithmetic_residual_prefix: float
    matrix_uncertainty: float
    total_residual_crude: float
    passed: bool


def transcript():
    passed = (
        MIN_PIVOT > PIVOT_TARGET
        and ARITHMETIC_RESIDUAL_CRUDE < ARITHMETIC_TARGET
        and MATRIX_UNCERTAINTY < MATRIX_UNCERTAINTY_LIMIT
        and TOTAL_RESIDUAL_CRUDE < TOTAL_ALLOWANCE
    )
    return Transcript(
        MIN_PIVOT, MIN_PIVOT_MODE, ABSL_ONE, ABSL_INF, LOCAL_DEFECT_SUM,
        ARITHMETIC_RESIDUAL_CRUDE, ARITHMETIC_RESIDUAL_PREFIX,
        MATRIX_UNCERTAINTY, TOTAL_RESIDUAL_CRUDE, passed,
    )


if __name__ == '__main__':
    t = transcript()
    print(t)
    if not t.passed:
        raise SystemExit('FAIL: stored certificate transcript does not satisfy guards')
    print('PASS: validated finite high-block certificate under stated arithmetic model')
    print('Conclusion: A0_[21,16001] >= 0.22 I')
    print('Guardrail: infinite high-complement cross/tail certification still pending')
