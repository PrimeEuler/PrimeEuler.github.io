#!/usr/bin/env python3
"""512-bit point-generator LDL backward-error contract for the N=16001 block.

This file records a deliberately over-conservative proof implementation target
for the remaining finite high-block arithmetic.

The shifted block is

    B = A0_[21,16001] - 0.22 I,

with exact-vs-nominal operator uncertainty targeted below 2e-13 (v13.357).
The midpoint structured LDL has

    min d_j ~= 0.25429962365,
    ||L^{-1}||_2 <= 284.07,

so v13.356 allows a total factor residual around 3.15e-6.

Implementation strategy
-----------------------
Run the exact displacement-generator recurrence in fixed MPFR precision,
preferably p=512 bits, using round-to-nearest point arithmetic.  Do NOT
propagate interval generators through all Schur steps.  Instead:

  1. evaluate the nominal scalar data (diagonal and Z_n) at very high precision;
  2. run the point generator LDL recurrence;
  3. record runtime maxima for every family of intermediate quantities;
  4. accumulate an outward-rounded scalar backward-error budget from the local
     floating-point model fl(a op b)=(a op b)(1+delta), |delta|<=u, together
     with absolute-error forms near cancellation;
  5. verify at the end that the resulting operator residual allowance plus the
     2e-13 matrix uncertainty is below the v13.356 threshold.

At p=512, u=2^-512 ~= 7.46e-155.  The design deliberately permits an absurd
intermediate-magnitude ceiling

    M <= 1e50.

Even a raw worst-scale estimate of the form

    (#ops) * u * M^2

with fewer than 2e9 charged scalar operations is below 2e-45.  This raw scale
is NOT by itself the rigorous backward-error theorem, because divisions and
recurrence sensitivities must be accounted for.  Its purpose is to show that
there is enormous room to use very pessimistic outward-rounded local bounds.

The verifier should impose simple runtime assertions such as

    min computed pivot > 0.25,
    max |intermediate| < 1e50,

and abort rather than weaken the proof if either fails.  The observed midpoint
minimum pivot 0.2542996 suggests the first target has ~4.3e-3 slack.

A practical final target is to certify

    arithmetic backward error < 1e-8,

which is already over 300 times smaller than the 3.15e-6 allowance and still
astronomically larger than 512-bit rounding noise.

Guardrail: this file specifies the validated-arithmetic contract; it does not
claim that the full backward-error accumulator has already been implemented or
run.  No exact-zero, RH, or GRH claim follows.
"""

BITS = 512
UNIT_ROUNDOFF = 2.0**(-BITS)
DIMENSION = 7991
INTERMEDIATE_CEILING = 1e50
CHARGED_OPS = 2_000_000_000
RAW_ROUNDING_SCALE = CHARGED_OPS * UNIT_ROUNDOFF * INTERMEDIATE_CEILING**2
PIVOT_RUNTIME_TARGET = 0.25
OBSERVED_MIN_PIVOT = 0.25429962365
MATRIX_UNCERTAINTY = 2e-13
ARITHMETIC_BACKWARD_ERROR_TARGET = 1e-8
TOTAL_RESIDUAL_ALLOWANCE = 3.15e-6

if __name__ == '__main__':
    print('unit roundoff =', UNIT_ROUNDOFF)
    print('raw 2e9*u*M^2 scale =', RAW_ROUNDING_SCALE)
    print('pivot slack over 0.25 =', OBSERVED_MIN_PIVOT-PIVOT_RUNTIME_TARGET)
    print('matrix uncertainty =', MATRIX_UNCERTAINTY)
    print('arithmetic backward-error target =', ARITHMETIC_BACKWARD_ERROR_TARGET)
    print('total residual allowance =', TOTAL_RESIDUAL_ALLOWANCE)
    print('guardrail: validated local-error accumulator still to implement')
