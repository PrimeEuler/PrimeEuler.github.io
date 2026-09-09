#!/usr/bin/env python3
"""Local a-posteriori defect bound for the corrected rank-four Suzuki LDL.

This is the Audit-Rounds-20/21 replacement for the rank-two local checker in
`suzuki_generator_ldl_local_defect_certificate.py`.

Corrected displacement form
---------------------------
For one trailing state, write x_i=n_i^2 and represent the off-diagonal matrix as

    M_ij = c1 (p_i q_j-q_i p_j)/(x_i-x_j)
         + c2 (r_i s_j-s_i r_j)/(x_i-x_j),     i != j,

with

    c1 = 2/pi,     (p,q) initially (U,n),
    c2 = pi,       (r,s) initially (n,n^2 H_n).

The diagonal is stored separately.  Scalar Schur elimination preserves this
form because every generator column g obeys

    g_tail' = g_tail - ell*g_pivot.

Local reconstruction
--------------------
At one step let a be the stored pivot.  From the *current stored point state*,
a higher-precision checker reconstructs the exact first column b_* represented
by that state and

    ell_* = b_*/a.

It then reconstructs the exact Schur-state data

    d_*' = d_tail - b_*^2/a,
    p_*' = p_tail - ell_* p_1,   q_*' = q_tail - ell_* q_1,
    r_*' = r_tail - ell_* r_1,   s_*' = s_tail - ell_* s_1.

The finite-precision factorization stores

    ellhat, dhat', phat', qhat', rhat', shat'.

Treat those stored values as exact dyadic inputs to the checker and define

    e_ell = ellhat-ell_*,
    e_d   = dhat'-d_*',
    e_p   = phat'-p_*',   e_q = qhat'-q_*',
    e_r   = rhat'-r_*',   e_s = shat'-s_*'.

Let Mhat' be the matrix represented by the stored next state.  The local
reconstruction defect

    Delta = M - L(ellhat) diag(a,Mhat') L(ellhat)^T

satisfies

    ||Delta||_F <= sqrt(2)|a| ||e_ell||_2
                 + ||e_d||_2
                 + delta_off
                 + |a| ||e_ell||_2 (||ell_*||_2+||ellhat||_2),

where the corrected rank-four off-diagonal mismatch obeys

    delta_off <= (2/Dmin) [
        |c1| ( ||e_p||_2 ||q_*'||_2 + ||phat'||_2 ||e_q||_2 )
      + |c2| ( ||e_r||_2 ||s_*'||_2 + ||rhat'||_2 ||e_s||_2 )
    ].

This follows pairwise from

    B(u,v)=u v^T-v u^T,
    B(uhat,vhat)-B(u*,v*) = B(e_u,v*) + B(uhat,e_v),
    ||B(y,z)||_F <= 2||y||_2||z||_2,

and 1/|x_i-x_j| <= 1/Dmin.  For consecutive odd modes in a trailing state,

    Dmin = (n+2)^2-n^2 = 4n+4.

Global composition is unchanged
-------------------------------
If Delta_k is the local defect at step k and P_k the prefix lower factor,

    E = sum_k P_k Delta_k P_k^T,

hence

    ||E||_2 <= || |L| ||_1 || |L| ||_inf sum_k ||Delta_k||_F.

Therefore the corrected validated replay still needs only O(N) persistent
storage: current diagonal/generators, row absolute sums of L, current column
absolute sum, and the accumulated local-defect sum.

The positivity test is likewise unchanged in form.  If

    B = A0_[21,16001] - 0.22 I = L D L^T + E_total,

then

    lambda_min(L^{-1} B L^{-T})
      >= d_min - ||L^{-1}||_2^2 ||E_total||_2.

A completed certificate must therefore verify a corrected lower pivot bound,
a corrected bound on ||L^{-1}||_2, and a total matrix+arithmetic residual below

    d_min / ||L^{-1}||_2^2.

The old numerical allowance 3.15e-6 is NOT automatically inherited: it came
from the legacy factor's inverse-norm bound and must be recomputed for the
corrected rank-four factor.  The corrected midpoint pivot is larger
(~0.2554790846), but that alone does not certify the new residual threshold.

Guardrail: this file derives the corrected local certificate algebra.  It does
not claim that the 7991-step directed-rounded replay has been completed, and it
makes no exact-zero, RH, or GRH claim.
"""

import math

C1 = 2.0/math.pi
C2 = math.pi
DIMENSION = 7991
SHIFT = 0.22
CORRECTED_MIDPOINT_MIN_PIVOT = 0.25547908458536395


def rank4_offdiag_defect_bound(ep2, eq2, er2, es2,
                               qstar2, phat2, sstar2, rhat2,
                               dmin, c1=C1, c2=C2):
    return (2.0/dmin) * (
        abs(c1)*(ep2*qstar2 + phat2*eq2)
        + abs(c2)*(er2*sstar2 + rhat2*es2)
    )


def local_defect_bound(a, el2, ed2,
                       ep2, eq2, er2, es2,
                       lstar2, lhat2,
                       qstar2, phat2, sstar2, rhat2,
                       dmin):
    delta_off = rank4_offdiag_defect_bound(
        ep2, eq2, er2, es2, qstar2, phat2, sstar2, rhat2, dmin)
    return (math.sqrt(2.0)*abs(a)*el2 + ed2 + delta_off
            + abs(a)*el2*(lstar2+lhat2))


if __name__ == '__main__':
    print('corrected displacement rank <= 4')
    print('dimension =', DIMENSION)
    print('shift =', SHIFT)
    print('midpoint min pivot =', CORRECTED_MIDPOINT_MIN_PIVOT)
    print('guardrail: corrected inverse-factor norm and directed-rounded replay still required')
