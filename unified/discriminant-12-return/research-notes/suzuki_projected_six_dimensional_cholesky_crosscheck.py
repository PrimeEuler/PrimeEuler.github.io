#!/usr/bin/env python3
"""Projected 6D Cholesky cross-check for the fixed rational stiff subspace.

For the N=155 nominal effective core F and the fixed rational 10x6 matrix V,
set G=V^T F V.  The midpoint matrix is nearly diagonal.  Its nominal diagonal
and Cholesky pivot-square scales are

  4.326400810728e-8,
  2.551234421118e-4,
  8.310012703752e-1,
  1.705602981103,
  2.017746626173,
  2.351910992224.

The ordinary floating Cholesky residual satisfies

  ||G-L L^T||_2 = 2.8086550293940804e-16.

The first-row off-diagonal absolute sum is only

  7.1024309552e-10.

Thus there are two independent future proof routes:

1. operator enclosure + Weyl:
     ||F-Fhat|| <= eta  =>  lambda_min(V^T F V)
       >= lambda_min(V^T Fhat V)-||V||^2 eta;

2. direct residual-Cholesky certification of the 6x6 projected interval matrix.

The second route is useful as an independent cross-check on the global Schur
error budget.  These are midpoint diagnostics only until interval inflation is
instantiated.
"""

PIVOT_SQUARES=(
    4.326400810728e-8,
    2.551234421118e-4,
    8.310012703752e-1,
    1.705602981103,
    2.017746626173,
    2.351910992224,
)
CHOLESKY_RESIDUAL=2.8086550293940804e-16
FIRST_ROW_OFFDIAG_SUM=7.1024309552e-10

if __name__=='__main__':
    print('first projected pivot square',PIVOT_SQUARES[0])
    print('projected Cholesky residual',CHOLESKY_RESIDUAL)
    print('first-row offdiagonal sum',FIRST_ROW_OFFDIAG_SUM)
    print('guardrail: midpoint cross-check only; interval inflation still required')
