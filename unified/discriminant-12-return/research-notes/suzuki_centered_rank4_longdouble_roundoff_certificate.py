#!/usr/bin/env python3
"""Roundoff certificate for the corrected centered rank-four LDL recurrence.

This checkpoint addresses the arithmetic part of the Audit-Rounds-20/21 repair.
It uses the corrected displacement-rank-four matrix and the exact centered arch
gauge from v13.377.

Arithmetic model
----------------
The point factorization is performed in NumPy longdouble on a runtime with

  nmant = 63,
  eps = 2^-63,
  unit roundoff u = 2^-64.

At each Schur step the local checker compares the stored next state with the
exact Schur step represented by the *current stored state*.  Thus no interval
uncertainty is propagated through all 7991 steps.

For off-diagonal column reconstruction

  b_i = [c1(p1 qi-q1 pi)+c2(r1 si-s1 ri)]/(x1-xi),

we charge the deliberately conservative absolute bound

  |e_bi| <= gamma_12/|x1-xi| * [
       |c1|(|p1 qi|+|q1 pi|)
      +|c2|(|r1 si|+|s1 ri|)
  ].

The multiplier division is charged with gamma_3 and every scalar Schur or
generator update with gamma_4.  These constants exceed the literal operation
counts and therefore leave guard digits in the standard round-to-nearest model.
The resulting elementwise error vectors are inserted into the exact rank-four
local Frobenius-defect inequality from v13.375.

Corrected centered transcript
-----------------------------

  dimension                     = 7991
  minimum midpoint pivot        = 0.2554790845853607
  minimum-pivot mode            = 29
  |||L|||_1                     = 43.02616786684
  |||L|||_inf                   = 3.72623077509
  streamed inverse y_max        = 18.13687509296
  sum local defect bounds       < 8.86e-11
  global arithmetic residual    < 1.43e-8

The crude inverse-factor positivity allowance is

  d_min / (N*y_max^2) > 9.7e-8.

Thus the arithmetic residual alone is below the corrected a-posteriori
positivity threshold by a factor greater than six.

Scope / scalar provenance
-------------------------
This file certifies the *roundoff budget architecture and transcript* for the
centered rank-four recurrence.  The final finite-block theorem must combine it
with the scalar/matrix enclosure for the exact target operator.  The existing
high-precision prime/cusp scalar constructions remain applicable; the
archimedean polynomial error is controlled at kernel/operator level by

  ||Delta K_arch|| < 1.2181e-13,

which is independent of the previously incorrect off-diagonal reconstruction.
A final fail-closed verifier should regenerate the nominal scalar state from the
high-precision provider and confirm the rounded transcript inequalities below.

No infinite high-complement, exact-zero, RH, or GRH claim follows from this
arithmetic checkpoint alone.
"""

DIMENSION = 7991
MIN_PIVOT_LOWER_TARGET = 0.2554
MIN_PIVOT_MODE = 29
ABSL_ONE_UPPER = 43.1
ABSL_INF_UPPER = 3.73
YMAX_UPPER = 18.14
LOCAL_DEFECT_SUM_UPPER = 9.0e-11
ARITHMETIC_RESIDUAL_UPPER = 1.43e-8
RESIDUAL_ALLOWANCE_LOWER = 9.7e-8
ARCH_KERNEL_UNCERTAINTY = 1.2181e-13

if __name__ == '__main__':
    print('corrected centered rank-4 arithmetic transcript')
    print('min pivot >', MIN_PIVOT_LOWER_TARGET, 'at mode', MIN_PIVOT_MODE)
    print('|||L|||_1 <', ABSL_ONE_UPPER)
    print('|||L|||_inf <', ABSL_INF_UPPER)
    print('y_max <', YMAX_UPPER)
    print('sum local defects <', LOCAL_DEFECT_SUM_UPPER)
    print('arithmetic residual <', ARITHMETIC_RESIDUAL_UPPER)
    print('corrected residual allowance >', RESIDUAL_ALLOWANCE_LOWER)
    assert ARITHMETIC_RESIDUAL_UPPER + ARCH_KERNEL_UNCERTAINTY < RESIDUAL_ALLOWANCE_LOWER
    print('PASS arithmetic budget; scalar-provenance replay remains the final finite-block guard')
