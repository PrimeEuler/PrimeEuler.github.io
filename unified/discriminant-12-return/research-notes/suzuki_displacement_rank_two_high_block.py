#!/usr/bin/env python3
"""Exact displacement-rank-two structure of the pole-free high block.

For the pole-free operator A0 in the odd-mode basis, define

    Z_n = 2 A_n + Si(n*pi) + 2 H_n.

For m != n,

    (A0)_{mn} = -(2/pi) (n Z_m - m Z_n)/(n^2-m^2).

Let X = diag(n^2), u=(Z_n), v=(n).  Then on all off-diagonal entries,

    (X A0 - A0 X)_{mn}
      = (m^2-n^2)(A0)_{mn}
      = (2/pi)(Z_m n - m Z_n).

Therefore

    X A0 - A0 X = (2/pi)(u v^T - v u^T)

away from the diagonal, and the diagonal contributes zero to the displacement
commutator automatically.  Hence the complete finite matrix is Cauchy-like with
exact displacement rank at most two.

Consequences for certification of A0_[21,16001] >= 0.225 I:

1. No dense 7991x7991 interval Cholesky is structurally necessary.
2. Every well-separated off-diagonal block admits the geometric Cauchy expansion

       1/(n^2-m^2) = n^{-2} sum_{k>=0} (m/n)^{2k},

   with rank at most two per order and explicit geometric remainder.
3. A recursive/HODLR LDL^T certificate can use small dense leaf blocks and
   low-rank Schur updates between separated blocks.
4. The same low-rank arithmetic already used for the infinite cross coupling can
   therefore be reused inside the finite high-block positivity certificate.

This file records exact algebraic structure and a certification strategy; it is
not itself the final interval LDL certificate.
"""

import math

DISPLACEMENT_RANK = 2
FINITE_START = 21
FINITE_END = 16001
FINITE_DIM = ((FINITE_END-FINITE_START)//2)+1
TARGET_GAP = 0.225
ALPHA_16003 = 4.6732674884171095
TARGET_FULL_CROSS = 1.0
TARGET_GLOBAL_MARGIN = TARGET_GAP - TARGET_FULL_CROSS**2/ALPHA_16003

if __name__ == '__main__':
    print('finite dimension =', FINITE_DIM)
    print('exact displacement rank <=', DISPLACEMENT_RANK)
    print('target finite gap =', TARGET_GAP)
    print('target global high-complement margin =', TARGET_GLOBAL_MARGIN)
