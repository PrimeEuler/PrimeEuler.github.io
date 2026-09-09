#!/usr/bin/env python3
"""Corrected displacement-rank-four LDL recurrence after Audit Rounds 20-21.

For odd modes n=21,23,... define

  U_n = Si(n*pi) + 2 A_n,
  Y_n = n H_n,

where A_n is the prime sine sequence and H_n is the archimedean sine
transform.  The corrected pole-free off-diagonal matrix is

  A0_mn = (2/pi) (n U_m - m U_n)/(m^2-n^2)
          + pi*m*n (Y_n-Y_m)/(m^2-n^2).

Equivalently, with X=diag(n^2), it is the sum of two skew displacement pairs:

  (m^2-n^2) A0_mn
    = (2/pi)[U_m n - m U_n]
      + pi[m (n Y_n) - (m Y_m) n].

Thus rank(X A0-A0 X)<=4.  A scalar Schur complement preserves the generator
form: if l=b/a is the current LDL multiplier column, every generator column g
updates by

  g_tail <- g_tail - l*g_pivot.

This file records the exact recurrence and the first corrected full-scale
midpoint run.  Scalar data use the same degree-65 rational h_32 polynomial
architecture as the legacy verifier; this is midpoint numerical evidence, not
yet the renewed validated residual certificate.
"""

SHIFT = 0.22
DIMENSION = 7991
CORRECTED_MIDPOINT_MIN_PIVOT = 0.25547908458536395
MIN_PIVOT_MODE = 29
LEGACY_MIN_PIVOT = 0.25429962364429953
CORRECTED_21_399_LAMBDA_MIN = 0.23450139875566745
LEGACY_21_399_LAMBDA_MIN = 0.23195316625368267
DENSE_RANK4_21_399_PIVOT_MAX_DIFF = 4.3e-10


def column_from_generators(x1, xtail, U1, U, V1, V, P1, P, Q1, Q):
    """Reconstruct one corrected off-diagonal Schur column.

    Arrays may be numpy/mpmath/ball objects supporting ordinary arithmetic.
    The two generator pairs are

      coefficient 2/pi: (U,V), with V initially n,
      coefficient pi:   (P,Q), with P initially n and Q initially n^2 H_n.
    """
    import numpy as np
    den = x1-xtail
    return ((2.0/np.pi)*(U1*V-V1*U) + np.pi*(P1*Q-Q1*P))/den


def update_generators(l, pivot_values, tails):
    """Generic Schur update g_tail <- g_tail-l*g_pivot for four generators."""
    return tuple(g-l*g1 for g1, g in zip(pivot_values, tails))


if __name__ == '__main__':
    print('corrected displacement rank <= 4')
    print('dimension =', DIMENSION)
    print('shift =', SHIFT)
    print('corrected midpoint min pivot =', CORRECTED_MIDPOINT_MIN_PIVOT)
    print('minimum-pivot mode =', MIN_PIVOT_MODE)
    print('legacy midpoint min pivot =', LEGACY_MIN_PIVOT)
    print('corrected lambda_min A0_[21,399] =', CORRECTED_21_399_LAMBDA_MIN)
    print('legacy lambda_min A0_[21,399] =', LEGACY_21_399_LAMBDA_MIN)
    print('dense/rank4 21..399 pivot agreement ~', DENSE_RANK4_21_399_PIVOT_MAX_DIFF)
    print('guardrail: renewed validated residual replay still required')
