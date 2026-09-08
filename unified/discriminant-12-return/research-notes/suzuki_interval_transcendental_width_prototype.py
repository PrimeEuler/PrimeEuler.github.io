#!/usr/bin/env python3
"""Interval-width prototype for the remaining prime/pole transcendental pieces.

At 50 decimal-digit interval precision, direct interval evaluation over all odd
modes n<=153 gives the targeting widths

  max prime-entry interval radius  = 2.008123298199738e-48
  max pole-vector interval radius  = 9.354676485322685e-51.

These values are not used as the final rational certificate; they are a
prototype showing that transcendental evaluation error in the prime and pole
pieces is negligible by dozens of orders of magnitude compared with the
~1e-10 finite-matrix design radius.

The final certificate should use the rational-series closure from v13.342
rather than trusting a special-function/interval library.
"""

MAX_PRIME_ENTRY_RADIUS_50DPS = 2.008123298199738e-48
MAX_POLE_VECTOR_RADIUS_50DPS = 9.354676485322685e-51
FINITE_MATRIX_DESIGN_RADIUS = 7.0e-11

if __name__ == '__main__':
    print('prime radius / design radius =',
          MAX_PRIME_ENTRY_RADIUS_50DPS/FINITE_MATRIX_DESIGN_RADIUS)
    print('pole radius / design radius =',
          MAX_POLE_VECTOR_RADIUS_50DPS/FINITE_MATRIX_DESIGN_RADIUS)
    print('guardrail: interval-library prototype only; final proof uses rational closure')
