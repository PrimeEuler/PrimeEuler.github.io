#!/usr/bin/env python3
"""A posteriori LDL certificate target for the shifted N=16001 high block.

Let

    B = A0_[21,16001] - 0.22 I,

and suppose a point structured LDL computation produces a unit lower-triangular
L and positive diagonal D.  Define the exact residual

    E = B - L D L^T.

Then

    L^{-1} B L^{-T} = D + L^{-1} E L^{-T}.

Therefore the sufficient condition

    ||L^{-1} E L^{-T}||_2 < d_min

proves B>0.  Using

    ||L^{-1} E L^{-T}||_2
      <= ||L^{-1}||_2^2 ||E||_2,

it is enough to verify

    ||E||_2 < d_min / ||L^{-1}||_2^2.

This checkpoint computes a deliberately crude but easy inverse-factor bound.
For a unit lower triangular L, define recursively

    y_i = 1 + sum_{j<i} |L_ij| y_j.

By forward substitution / induction,

    ||L^{-1}||_infinity <= max_i y_i.

The midpoint structured LDL from v13.354 gives

    d_min ~= 0.25429962365,
    max_i y_i ~= 21.22011808.

Without attempting a sharp 2-norm estimate, use

    ||L^{-1}||_2 <= sqrt(N) ||L^{-1}||_infinity,
    N = 7991.

This yields

    ||L^{-1}||_2 <= 1.897e3

and the conservative residual target

    ||E||_2 < 7.06e-8.

The value is intentionally crude.  It is already loose compared with the
finite-entry enclosure scale available from the rational prime/cusp/arch
construction (roughly 1e-12 to 1e-10 per scalar, and improvable arbitrarily by
adding rational-series terms).

This route avoids interval dependency explosion in the 7991-step generator
recurrence: compute a high-precision point factor, then certify the completed
factorization by a global residual bound plus an independently verified inverse
factor bound.

Guardrail: all displayed L,D and inverse-factor numbers are midpoint numerical
diagnostics until outward-rounded residual and inverse-bound calculations are
implemented.  No high-complement positivity, exact-zero, RH, or GRH theorem is
claimed here.
"""

N = 7991
D_MIN = 0.254299623648608
LINV_INF_BOUND_MIDPOINT = 21.220118080655787
LINV_2_CRUDE_BOUND = (N**0.5) * LINV_INF_BOUND_MIDPOINT
RESIDUAL_TARGET = D_MIN / (LINV_2_CRUDE_BOUND**2)

if __name__ == '__main__':
    print('N =', N)
    print('midpoint d_min =', D_MIN)
    print('midpoint ||L^-1||_inf bound =', LINV_INF_BOUND_MIDPOINT)
    print('crude ||L^-1||_2 bound =', LINV_2_CRUDE_BOUND)
    print('sufficient residual target =', RESIDUAL_TARGET)
    print('guardrail: outward-rounded residual/inverse certificate still required')
