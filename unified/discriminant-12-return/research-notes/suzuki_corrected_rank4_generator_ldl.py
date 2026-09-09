#!/usr/bin/env python3
"""Corrected displacement-rank-four LDL recurrence after Audit Rounds 20-21.

For odd modes n=21,23,... define

  U_n = Si(n*pi) + 2 A_n,
  Y_n = n H_n,

where A_n is the prime sine sequence and H_n is the archimedean sine
transform.  The corrected pole-free off-diagonal matrix is

  A0_mn = (2/pi) (n U_m - m U_n)/(m^2-n^2)
          + pi*m*n (Y_n-Y_m)/(m^2-n^2).

Equivalently, with X=diag(n^2), it is the sum of two skew displacement pairs.
The cusp+prime pair is (U,n), coefficient 2/pi.  For the arch pair there is an
exact gauge freedom because replacing n*Y_n by n*(Y_n-c) changes the skew
product by zero.  The natural asymptotic center is

  c_inf = lim_{n odd -> infinity} n H_n
        = (2/pi) * exp(-1)/(1-exp(-4)).

Thus the preferred arch generators are

  P_n = n,
  Q_n = n*(Y_n-c_inf) = n*(n H_n-c_inf),

with coefficient pi.  Two integrations by parts give Y_n-c_inf=O(n^-2), so
Q_n=O(n^-1).  This removes the large O(n) cancellation present in the raw pair
(P,nY) without changing the matrix.

Scalar Schur elimination preserves the generator form: if l=b/a is the current
LDL multiplier column, every generator column g updates by

  g_tail <- g_tail - l*g_pivot.

This file records the corrected recurrence, centered gauge, and full-scale
midpoint diagnostics.  It is not by itself the renewed directed-rounded
certificate.
"""

from math import exp, pi

SHIFT = 0.22
DIMENSION = 7991
CORRECTED_MIDPOINT_MIN_PIVOT = 0.25547908458536395
MIN_PIVOT_MODE = 29
CORRECTED_STREAMING_YMAX = 18.13687509296
CORRECTED_STREAMING_YMAX_MODE = 345
CORRECTED_ABSL_ONE = 43.02616787
CORRECTED_ABSL_INF = 3.72623078
CORRECTED_CRUDE_RESIDUAL_ALLOWANCE = 9.72e-8
LEGACY_MIN_PIVOT = 0.25429962364429953
CORRECTED_21_399_LAMBDA_MIN = 0.23450139875566745
LEGACY_21_399_LAMBDA_MIN = 0.23195316625368267
DENSE_RANK4_21_399_PIVOT_MAX_DIFF = 4.3e-10
C_INF = (2.0/pi)*(exp(-1.0)/(1.0-exp(-4.0)))


def centered_arch_q(n, Hn):
    """Preferred exact-gauge arch generator Q_n=n*(n H_n-c_inf)."""
    return n*(n*Hn-C_INF)


def column_from_generators(x1, xtail, U1, U, V1, V, P1, P, Q1, Q):
    """Reconstruct one corrected off-diagonal Schur column.

    The two generator pairs are coefficient 2/pi: (U,V), initially V=n, and
    coefficient pi: (P,Q), initially P=n and Q=n*(n H_n-c_inf).
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
    print('c_inf =', C_INF)
    print('corrected midpoint min pivot =', CORRECTED_MIDPOINT_MIN_PIVOT)
    print('minimum-pivot mode =', MIN_PIVOT_MODE)
    print('streaming y_max midpoint =', CORRECTED_STREAMING_YMAX)
    print('corrected crude residual allowance ~', CORRECTED_CRUDE_RESIDUAL_ALLOWANCE)
    print('corrected lambda_min A0_[21,399] =', CORRECTED_21_399_LAMBDA_MIN)
    print('legacy lambda_min A0_[21,399] =', LEGACY_21_399_LAMBDA_MIN)
    print('dense/rank4 21..399 pivot agreement ~', DENSE_RANK4_21_399_PIVOT_MAX_DIFF)
    print('guardrail: renewed directed-rounded residual replay still required')
