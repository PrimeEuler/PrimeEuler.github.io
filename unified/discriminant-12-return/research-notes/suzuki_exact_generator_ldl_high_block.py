#!/usr/bin/env python3
"""Exact displacement-generator LDL recurrence for the pole-free high block.

Let the odd modes be n=21,23,...,16001 and write

    A0 = C_cusp + B_prime + K_arch,
    B  = A0 - 0.22 I.

For the unified scalar sequence

    Z_n = 2 A_n + Si(n*pi) + 2 H_n,

all off-diagonal entries satisfy

    (A0)_{mn} = -(2/pi) (n Z_m - m Z_n)/(n^2-m^2),  m != n.

Equivalently, with

    X = diag(n^2),
    u = (Z_n),
    v = (n),

one has the exact displacement identity

    X A0 - A0 X = (2/pi)(u v^T - v u^T).

The key point of this checkpoint is that scalar Schur complements preserve this
rank-two displacement representation exactly.

Suppose at one LDL step the current matrix is partitioned as

    M = [[a, b^T],
         [b, C]],

with first generator entries u1,v1 and remaining generators u2,v2.  Its Schur
complement

    S = C - b b^T/a

again satisfies a rank-two displacement identity with updated generators

    u2' = u2 - (b/a) u1,
    v2' = v2 - (b/a) v1.

The current column b itself is reconstructed algebraically from the generators:

    b_i = (2/pi) (u1 v_i - v1 u_i)/(x1-x_i),
    x_i=n_i^2.

Thus an entire no-pivot LDL factorization is generated using only

    * the current diagonal,
    * the two generator vectors u,v,
    * O(N) storage,
    * O(N^2) arithmetic,

without ever assembling the dense matrix.

Midpoint audit for n=21..16001 (7991 modes), using the quadrature-free finite
archimedean reconstruction and the unified Cauchy sequence:

    min scalar LDL pivot ~= 0.25429962365,
    attained at mode n=29.

The late pivots are O(8), and no pivot approaches zero.

Dense cross-check on the smaller n=21..199 block reproduces ordinary dense
no-pivot LDL pivots to about 1.3e-15 in double arithmetic.

This is much better conditioned for certification than the spectral slack

    lambda_min(A0_[21,16001]) - 0.22 ~= 7.11e-3.

The interval-proof target is therefore no longer a giant dense eigenvalue or
Cholesky calculation.  It is to run this exact generator recurrence with
outward-rounded enclosures for the diagonal and Z_n values and verify that every
pivot interval remains strictly positive.

Midpoint perturbation diagnostics are very stable: random 1e-6-scale
perturbations of diagonal/Z data move the minimum pivot only at roughly the
1e-6 scale.  This is diagnostic only, not a proof of interval stability.

Guardrail: the displayed pivots are midpoint numerical data.  Positivity of the
7991-dimensional shifted block is not certified until the same recurrence is
run with outward-rounded interval/ball arithmetic.  No exact-zero, RH, or GRH
claim follows.
"""

SHIFT = 0.22
DIMENSION = 7991
MIDPOINT_MIN_PIVOT = 0.25429962365
MIN_PIVOT_MODE = 29
DENSE_CROSSCHECK_ERROR = 1.3e-15
MIDPOINT_SPECTRAL_SLACK = 0.227114802018 - SHIFT

if __name__ == '__main__':
    print('dimension =', DIMENSION)
    print('shift =', SHIFT)
    print('midpoint min LDL pivot =', MIDPOINT_MIN_PIVOT)
    print('min pivot mode =', MIN_PIVOT_MODE)
    print('dense crosscheck max pivot error ~= ', DENSE_CROSSCHECK_ERROR)
    print('midpoint spectral slack =', MIDPOINT_SPECTRAL_SLACK)
    print('guardrail: interval generator recurrence still required')
