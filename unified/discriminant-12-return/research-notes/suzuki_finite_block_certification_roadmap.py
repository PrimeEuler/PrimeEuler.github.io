#!/usr/bin/env python3
"""Finite-block certification roadmap after v13.328.

The v13.328 six-dimensional protected line reduces the adverse remote-tail
Schur penalty below its formal effective Rayleigh scale already at N=155.
The bottleneck is therefore finite-block certification, not remote-tail decay.

This checkpoint records the exact algebraic object that should be certified and
separates what can be enclosed analytically from what remains hybrid numerical.

Let C={1,3,...,19}, B={21,23,...,153}, T={155,157,...}.  The tail T has the
existing analytic coercive lower bound alpha_155>0.  The finite matrix on C+B
can be assembled entrywise from:

  cusp: exact Si/Ci formulas,
  prime: exact finite five-shift formulas,
  arch: one-dimensional integral of smooth h(t) times exact shift entry,
  pole: exact positive rank-one term.

The certification target is NOT the sign of a tiny floating eigenvalue.  Use
block LDL^T / Schur complements with outward-rounded entry enclosures.  This
turns positivity/inertia into pivot-interval statements and avoids subtracting
nearly equal eigenvalues after diagonalization.

Recommended hierarchy:
  1. certify the buffer block B positive by interval LDL^T;
  2. interval-solve B X = B_C and enclose Delta=A_CB B^{-1} A_BC;
  3. form an interval 10x10 effective core F=A_CC-Delta;
  4. rotate only for conditioning, never for proof; certify inertia of F by
     interval LDL^T / Sylvester sequence;
  5. attach T with the v13.328 protected-tail estimate at N=155.

A crucial numerical fact from v13.323 is that the finite buffer gap near
M=399 is ~0.267, so the buffer solve itself is well-conditioned.  The hard
uncertainty is concentrated in the tiny effective-core pivots, not in B.

No positivity, exact zero, lambda_1=0, RH, or GRH conclusion is made here.
"""

CORE = tuple(range(1,20,2))
BUFFER_153 = tuple(range(21,154,2))
TAIL_START = 155

# v13.328 non-interval scales retained only as targeting data.
PROTECTED_RAYLEIGH_SCALE = 6.517117134862395e-11
TAIL_CROSSOVER = 155


def certification_dimensions():
    return {
        'core_dim': len(CORE),
        'buffer_dim': len(BUFFER_153),
        'finite_dim': len(CORE)+len(BUFFER_153),
        'tail_start': TAIL_START,
    }


if __name__ == '__main__':
    print(certification_dimensions())
    print('proof target: interval LDL/Schur inertia, not tiny-eigenvalue sign')
