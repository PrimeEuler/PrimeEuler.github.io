#!/usr/bin/env python3
"""Local a-posteriori defect bound for the structured Suzuki generator LDL.

This checkpoint replaces interval propagation through 7991 Schur steps by a
local reconstruction check.

At one step let the current point-state matrix be M(d,u,v), with

    X = diag(x_i),
    M_ij = (2/pi)(u_i v_j-v_i u_j)/(x_i-x_j), i!=j.

Write

    a = d_1,
    b_* = exact first column reconstructed from the current point generators,
    l_* = b_*/a.

The exact Schur state has

    d_*' = d_2 - b_*^2/a,
    u_*' = u_2 - l_* u_1,
    v_*' = v_2 - l_* v_1.

Suppose the finite-precision factorization stores point values

    lhat, dhat', uhat', vhat'.

Treat those stored numbers as exact dyadic inputs to a higher-precision
checker and define

    e_l = lhat-l_*,
    e_d = dhat'-d_*',
    e_u = uhat'-u_*',
    e_v = vhat'-v_*'.

Let Mhat' be the matrix represented by (dhat',uhat',vhat').  The local
reconstruction defect is

    Delta = M - L(lhat) diag(a,Mhat') L(lhat)^T.

Its Frobenius norm admits the explicit bound

  ||Delta||_F <= sqrt(2)|a| ||e_l||_2
               + ||e_d||_2
               + delta_off
               + |a| ||e_l||_2 (||l_*||_2+||lhat||_2),

where the off-diagonal Schur-state mismatch is bounded by

  delta_off <= (2c/Dmin)
      [ ||e_u||_2 ||v_*'||_2 + ||uhat'||_2 ||e_v||_2 ],

with c=2/pi and

  Dmin = min_{i!=j}|x_i-x_j|

on the trailing state.  The bound follows from

  B(u,v)=u v^T-v u^T,
  ||B(p,q)||_F <= 2||p||_2||q||_2,

and the entrywise denominator bound 1/|x_i-x_j| <= 1/Dmin.

For odd Fourier modes n,n+2 one has

  (n+2)^2-n^2 = 4n+4,

so Dmin is explicit at every step.

Global composition
------------------
If Delta_k is the local defect at step k and P_k is the accumulated prefix
factor, the final residual satisfies exactly

    E = sum_k P_k Delta_k P_k^T.

Hence

    ||E||_2 <= || |L| ||_2^2 sum_k ||Delta_k||_2
             <= || |L| ||_1 || |L| ||_inf sum_k ||Delta_k||_F.

Thus a validated run needs only:

  * high-precision point generator LDL;
  * a higher-precision/directed-rounded replay of each local step;
  * accumulated sum of local Frobenius defect bounds;
  * row/column sums of |L|.

No interval generator state is propagated through the elimination chain.

Independent algebra check
-------------------------
A prototype deliberately performed one Schur step in float32 while evaluating
the current matrix and the defect in float64 on generic displacement-rank-two
matrices.  For dimensions 5,10,20 the measured/bounded Frobenius defects were
approximately

  n=5 : actual 2.19e-7, bound 5.09e-7,
  n=10: actual 2.87e-7, bound 8.22e-7,
  n=20: actual 3.31e-7, bound 4.30e-6.

This is an algebra/implementation cross-check, not the Suzuki certificate.
The full 7991-step validated run is still required.

Guardrail: no exact-zero, RH, or GRH claim follows.
"""

import math

C = 2.0/math.pi
DIMENSION = 7991
SHIFT = 0.22
TARGET_TOTAL_FACTOR_RESIDUAL = 3.15e-6
TARGET_ARITHMETIC_RESIDUAL = 1e-8


def local_defect_bound(a, el2, ed2, eu2, ev2,
                       lstar2, lhat2, vstar2, uhat2, dmin, c=C):
    """Scalar form of the derived Frobenius local-defect bound."""
    delta_off = (2.0*c/dmin)*(eu2*vstar2 + uhat2*ev2)
    return (math.sqrt(2.0)*abs(a)*el2 + ed2 + delta_off
            + abs(a)*el2*(lstar2+lhat2))


if __name__ == '__main__':
    print('dimension =', DIMENSION)
    print('target arithmetic residual =', TARGET_ARITHMETIC_RESIDUAL)
    print('total factor residual allowance =', TARGET_TOTAL_FACTOR_RESIDUAL)
    print('guardrail: full directed-rounded local-defect replay still required')
