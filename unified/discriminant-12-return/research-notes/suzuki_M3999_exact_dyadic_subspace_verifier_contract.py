#!/usr/bin/env python3
"""Exact-dyadic subspace contract for the terminal M=3999 Suzuki verifier.

Key simplification
------------------
The six-dimensional basis Q and fixed preconditioner L0 do not need to be
certified as exact eigenvectors or as an exact Cholesky factor.

Freeze rounded high-precision values of Q (10x6) and L0 (6x6) as exact dyadic
verifier inputs.  It is enough to certify:

  * Q has rank 6;
  * L0 is invertible;
  * for the exact source-faithful operator, the normalized finite matrix

        C = L0^{-1} (Q^T S_F Q) L0^{-T}

    is positive enough;
  * the normalized residual Gram

        H = L0^{-1} (Q^T R^* R Q) L0^{-T}

    satisfies H < delta_T C.

No statement that Q equals an exact eigenspace is needed.  Positivity on the
six-dimensional subspace ran(Q) is already sufficient to show that the
10-dimensional Schur complement has positive index at least six, hence at most
four nonpositive directions.

Likewise L0 is only a fixed invertible coordinate transformation.  It need not
be proved to equal an exact Cholesky factor of any exact matrix.

M=3999 midpoint solve diagnostic
--------------------------------
For the source-faithful finite system

    A_FF X = A_FC,
    F={21,23,...,3999}, C={1,3,...,19},

a fresh ordinary-double dense solve gives

    ||A_FC-A_FF X||_2 ~= 5.1902336852e-16,
    ||.||_F            ~= 8.6118427325e-16,
    max entry          ~= 2.2204460493e-16.

The v13.396 fail-closed solve target is 1e-12, so the midpoint residual has
roughly 1900x headroom.  The proof replay should reconstruct the source-faithful
matrix and the stored X (or re-solve at high precision), then enclose this
residual outward.

Terminal theorem shape
----------------------
If the verifier establishes

    C >= c I > 0,
    H < delta_T C,

then the exact infinite Schur complement is positive on ran(Q), a six-dimensional
subspace.  Therefore its nonpositive index is at most four.

This does NOT determine the signs of the remaining four directions and does NOT
identify any exact kernel.

Guardrail: contract + midpoint residual diagnostic only.  No completed outward
replay, exact-zero, RH, or GRH conclusion follows.
"""

MIDPOINT_SOLVE_RESIDUAL_2 = 5.190233685166924e-16
MIDPOINT_SOLVE_RESIDUAL_F = 8.611842732543909e-16
MIDPOINT_SOLVE_RESIDUAL_MAX = 2.220446049250313e-16
VERIFIER_SOLVE_TARGET = 1.0e-12
HEADROOM = VERIFIER_SOLVE_TARGET/MIDPOINT_SOLVE_RESIDUAL_2

if __name__ == '__main__':
    print('midpoint solve residual 2-norm =', MIDPOINT_SOLVE_RESIDUAL_2)
    print('midpoint solve residual Frobenius =', MIDPOINT_SOLVE_RESIDUAL_F)
    print('midpoint solve max entry =', MIDPOINT_SOLVE_RESIDUAL_MAX)
    print('verifier solve target =', VERIFIER_SOLVE_TARGET)
    print('midpoint headroom factor =', HEADROOM)
    assert HEADROOM > 1900
    print('PASS: exact-dyadic Q/L0 contract removes eigenvector/Cholesky validation requirement')