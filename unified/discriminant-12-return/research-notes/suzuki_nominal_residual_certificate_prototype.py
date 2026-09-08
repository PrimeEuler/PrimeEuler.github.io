#!/usr/bin/env python3
"""Nominal residual certificate prototype at the N=155 finite split.

This records the actual numerical residuals obtained from the existing finite
matrix assembly before interval inflation.  It is NOT itself a rigorous proof;
it is the midpoint prototype that the rational interval implementation must
surround.

Split:
  C={1,3,...,19}, dim 10
  B={21,23,...,153}, dim 67

Nominal results from the current 1200-node arch assembly:

  lambda_min(B)                  = 2.720147601690829e-1
  ||B-L L^T||_2                 = 8.950011006365997e-16
  ||I-Y L||_2, Y=L^{-1}         = 1.984574988649832e-16
  residual lower bound for B    = 2.720147601690794e-1
  ||C^T-BX||_2                  = 3.360147340254840e-16

The first six effective-core eigenvalues of

  F=A_CC-C B^{-1} C^T

are approximately

 -1.43553288e-11,
 -1.43538536e-11,
 -1.40089107e-11,
 -1.27803033e-11,
  4.32640082e-8,
  2.55123442e-4.

The first four signs are discarded as quadrature/assembly-floor artifacts.

For the fixed rational 10x6 matrix V from
suzuki_rational_stiff_subspace_candidate.py,

  eig(V^T F V) =
    4.32640081e-8,
    2.55123442e-4,
    8.31001270e-1,
    1.70560298,
    2.01774663,
    2.35191099.

Also ||V||_2 = 1.000000000760053.

Thus, once a rigorous operator enclosure

  ||F-F_hat|| <= eta

is instantiated with eta <= 7.1e-9, the projected perturbation obeys

  ||V^T(F-F_hat)V|| <= ||V||^2 eta < 7.10000002e-9,

leaving a design lower margin above 3.61e-8 on the first projected level.

No positivity, exact-zero, lambda_1=0, RH, or GRH claim follows from these
midpoint residuals alone.
"""

BUFFER_GAP = 0.2720147601690829
CHOLESKY_RESIDUAL = 8.950011006365997e-16
INVERSE_RESIDUAL = 1.984574988649832e-16
BUFFER_LOWER_FROM_RESIDUAL = 0.2720147601690794
SCHUR_SOLVE_RESIDUAL = 3.360147340254840e-16
V_NORM = 1.000000000760053
PROJECTED_EIGS = (
    4.32640081e-8,
    2.55123442e-4,
    8.31001270e-1,
    1.70560298,
    2.01774663,
    2.35191099,
)
DESIGN_EFFECTIVE_CORE_RADIUS = 7.1e-9

if __name__ == '__main__':
    proj_err = V_NORM*V_NORM*DESIGN_EFFECTIVE_CORE_RADIUS
    print('buffer gap', BUFFER_GAP)
    print('Cholesky residual', CHOLESKY_RESIDUAL)
    print('inverse residual', INVERSE_RESIDUAL)
    print('Schur solve residual', SCHUR_SOLVE_RESIDUAL)
    print('projected first level', PROJECTED_EIGS[0])
    print('projected perturbation budget', proj_err)
    print('design positive margin', PROJECTED_EIGS[0]-proj_err)
    print('guardrail: midpoint prototype only; rigorous interval inflation pending')
