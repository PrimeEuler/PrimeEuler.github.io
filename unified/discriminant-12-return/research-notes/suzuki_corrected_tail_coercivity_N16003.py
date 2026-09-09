#!/usr/bin/env python3
"""Corrected tail coercivity at the N=16003 interface.

The tail lower bound is derived from the direct cusp decomposition, the
validated prime operator bound ||B_prime||<2.05, and the kernel-level
archimedean tail localization.  It does not use the superseded off-diagonal
arch reconstruction, so External Audit Rounds 20-21 do not invalidate it.

For odd modes n>=N,

    alpha_N = log(N/4) - pi/2 - 2.05
              - beta_cusp(N) - beta_arch(N).

The arch tail uses

    |K_arch(m,n)| <= C_r/(k_m k_n),
    C_r = 19/12 + 4*zeta(3) q^3/[4(1-q)^3], q=2/pi,

which follows directly from the convolution kernel -h(|x-y|).

At N=16003:

    beta_cusp < 6.395e-6,
    beta_arch < 1.020e-4,
    alpha_16003 > 4.67333.

We retain the rounded proof target

    alpha_16003 > 4.6733.

This is the pole-free tail block.  The pole term is positive semidefinite and
therefore can only improve the lower bound in the full even-v operator.
"""

import math

PRIME_BOUND = 2.05
N = 16003
C_R = 8.047038193418354


def odd_sum2_tail_bound(N):
    return 1.0/N**2 + 1.0/(2.0*N)


def odd_sum4_tail_bound(N):
    return 1.0/N**4 + 1.0/(6.0*N**3)


def odd_sum6_tail_bound(N):
    return 1.0/N**6 + 1.0/(10.0*N**5)


def arch_tail_bound(N):
    return C_R*(4.0/math.pi**2)*odd_sum2_tail_bound(N)


def cusp_tail_bound(N):
    rank_one=(2.0/math.pi**2)*odd_sum2_tail_bound(N)
    c=2.0/math.pi**3+6.0/math.pi**4
    alpha=2.0*c/math.pi
    offdiag=2.0*alpha*math.sqrt((math.pi**2/12.0)*odd_sum6_tail_bound(N))
    C_diag=2.0/math.pi**2+2.0/math.pi**3+2.0/math.pi**4+6.0/math.pi**5
    diagonal=C_diag*math.sqrt(odd_sum4_tail_bound(N))
    return rank_one+offdiag+diagonal


def margin(N):
    return (math.log(N/4.0)-math.pi/2.0-PRIME_BOUND
            -cusp_tail_bound(N)-arch_tail_bound(N))


if __name__ == '__main__':
    print('beta_cusp =', cusp_tail_bound(N))
    print('beta_arch =', arch_tail_bound(N))
    print('alpha_16003 =', margin(N))
    if not margin(N) > 4.6733:
        raise SystemExit('FAIL')
    print('PASS: pole-free tail >= 4.6733 I')
