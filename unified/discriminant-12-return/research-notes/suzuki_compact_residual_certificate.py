#!/usr/bin/env python3
"""Compact residual certificate architecture for the finite Suzuki reduction.

This replaces interval eigensolvers by residual checks against rational/interval
matrix data.

BUFFER CERTIFICATE
------------------
Let B be the rigorous 67x67 interval buffer matrix, and let L be a rational or
outward-rounded numerical lower-triangular factor.  Define

    E = B - L L^T.

Let Y approximate L^{-1}, and let

    rho = ||I - Y L|| < 1.

Then

    ||L^{-1}|| <= ||Y||/(1-rho),

hence

    L L^T >= ((1-rho)/||Y||)^2 I.

Therefore B>0 follows from

    ||E|| < ((1-rho)/||Y||)^2.

This is especially generous because the nominal buffer gap is ~0.27.

EFFECTIVE-CORE FOUR-DIMENSIONAL OBSTRUCTION
--------------------------------------------
Let F be the rigorous 10x10 effective-core interval matrix.  Choose ANY fixed
rational 10x6 matrix V approximating the six stiff numerical directions.  Form

    M = V^T F V.

If M is rigorously positive definite, then V must have rank six (otherwise a
nonzero x with Vx=0 would give x^T M x=0), and span(V) is a six-dimensional
positive subspace for F.  Therefore the nonpositive index of F is at most four.

Thus no certified eigenvectors, orthogonality relations, or interval lambda_5
routine are needed.  The terminal-dimension theorem can be certified by a
6x6 positive-definiteness check.

The 6x6 check can itself use the same Cholesky-residual method, or interval LDL.

Guardrail: this only certifies the finite effective core once the rigorous
Schur enclosure F is actually instantiated.  It is not yet a positivity/RH
claim for the infinite operator.
"""

BUFFER_DIM=67
CORE_DIM=10
STIFF_DIM=6
TERMINAL_DIM=4

if __name__=='__main__':
    print('certificate objects: 67D Cholesky residual + 6D projected positivity')
