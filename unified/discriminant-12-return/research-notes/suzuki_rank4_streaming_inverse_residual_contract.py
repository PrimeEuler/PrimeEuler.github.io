#!/usr/bin/env python3
"""Streaming positivity certificate contract for corrected rank-four Suzuki LDL.

This checkpoint removes the need to reproduce the legacy dense/packed-L
inverse-factor calculation.  For the corrected factorization

    B = A0_[21,16001] - 0.22 I = L D L^T + E,

we only need a certified upper bound on ||L^{-1}||_2 and a certified residual
bound ||E||_2.

Streaming inverse bound
-----------------------
Let L be unit lower triangular and define recursively

    y_i = 1 + sum_{j<i} |l_ij| y_j.

By forward substitution/majorization,

    |L^{-1}| 1 <= y,

so

    ||L^{-1}||_inf <= y_max := max_i y_i.

This recurrence is streamable during ordinary left-to-right LDL elimination:
when column j is produced, y_j is already finalized, and each future row i can
accumulate

    accum_i += |l_ij| y_j.

When row i reaches its pivot, set y_i=1+accum_i.  Only O(N) storage is needed.

The elementary norm inequality then gives

    ||L^{-1}||_2 <= sqrt(N) ||L^{-1}||_inf <= sqrt(N) y_max.

Therefore a sufficient positivity condition is

    ||E_total||_2 < d_min / (N y_max^2).

Here E_total includes both arithmetic factorization residual and exact-vs-
nominal matrix uncertainty.

Rounded design target
---------------------
The corrected midpoint minimum pivot is about 0.2554790846.  A validated run
should target

    d_min > 0.25.

The legacy factor had an infinity inverse majorant about 21.22.  That number is
NOT inherited by the corrected factor; however, a deliberately loose corrected
target

    y_max < 25

would already imply

    ||L^{-1}||_2 < sqrt(7991)*25

and hence the rigorous residual allowance

    0.25/(7991*25^2) = 5.005631335...e-8.

The dimension-free exact-vs-nominal matrix uncertainty remains naturally at
about 2e-13, because the corrected archimedean formula is merely the correct
closed form of the same integral-kernel compression.  Thus a convenient replay
design is

    arithmetic residual < 1e-9,
    matrix uncertainty    < 2e-13,
    total residual        < 1.001e-9,

which leaves a factor > 49 against the y_max<25 positivity allowance.

The arithmetic residual is certified from the corrected rank-four local-defect
sum by

    E_arith <= || |L| ||_1 || |L| ||_inf sum_k delta_k,

where delta_k is the directed-rounded local Frobenius defect bound from
`suzuki_rank4_generator_ldl_local_defect_certificate.py`.

Recommended compact transcript
------------------------------
A completed run needs only report:

  1. dimension and shift;
  2. factor precision and checker precision;
  3. validated minimum pivot and mode;
  4. validated y_max;
  5. || |L| ||_1 and || |L| ||_inf;
  6. sum_k delta_k;
  7. arithmetic residual bound;
  8. matrix uncertainty bound;
  9. total residual bound;
 10. d_min/(N y_max^2);
 11. PASS/FAIL.

Guardrail: y_max<25 and arithmetic residual<1e-9 are design targets, not yet
validated outputs.  No positivity claim is promoted until the directed-rounded
7991-step replay supplies the transcript.
"""

N = 7991
SHIFT = 0.22
PIVOT_TARGET = 0.25
YMAX_TARGET = 25.0
ARITHMETIC_RESIDUAL_TARGET = 1e-9
MATRIX_UNCERTAINTY_TARGET = 2e-13
TOTAL_RESIDUAL_TARGET = ARITHMETIC_RESIDUAL_TARGET + MATRIX_UNCERTAINTY_TARGET
RESIDUAL_ALLOWANCE_IF_TARGETS_PASS = PIVOT_TARGET/(N*YMAX_TARGET**2)

if __name__ == '__main__':
    print('dimension =', N)
    print('shift =', SHIFT)
    print('pivot target >', PIVOT_TARGET)
    print('y_max target <', YMAX_TARGET)
    print('residual allowance if targets pass =', RESIDUAL_ALLOWANCE_IF_TARGETS_PASS)
    print('designed total residual target =', TOTAL_RESIDUAL_TARGET)
    print('safety factor =', RESIDUAL_ALLOWANCE_IF_TARGETS_PASS/TOTAL_RESIDUAL_TARGET)
    print('guardrail: targets are not a completed validated replay')
