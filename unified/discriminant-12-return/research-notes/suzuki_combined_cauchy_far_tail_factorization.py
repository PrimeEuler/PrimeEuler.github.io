#!/usr/bin/env python3
"""Combined pole-free Cauchy structure and low-rank far-tail factorization.

For the a=1 even-v odd-mode basis, the off-diagonal pole-free matrix is

    A0 = C_cusp + B_prime + K_arch.

The three exact off-diagonal formulas share the same Cauchy denominator:

    B_prime(m,n)=-(4/pi) (n A_m-m A_n)/(n^2-m^2),
    C_cusp(m,n)=-(2/pi) (n S_m-m S_n)/(n^2-m^2),
    K_arch(m,n)=-(4/pi) (n H_m-m H_n)/(n^2-m^2),

where

    S_j = Si(j*pi),
    H_j = int_0^2 h(t) sin(j*pi*t/2) dt.

Hence with

    Z_j = 2 A_j + S_j + 2 H_j,

one has the exact combined identity

    A0(m,n)=-(2/pi) (n Z_m-m Z_n)/(n^2-m^2),   m != n.

For a separated split m<=M<R<=n,

    1/(n^2-m^2)=sum_{k>=0} m^(2k)/n^(2k+2),

so the cross block is the convergent rank-two expansion

    A0(m,n)=-(2/pi) sum_{k>=0}
       [ m^(2k) Z_m / n^(2k+1)
         - m^(2k+1) Z_n / n^(2k+2) ].

Thus truncation after K terms has rank at most 2K.  At the targeting split
M=6001, R=16005, M/R<0.375, so the expansion converges rapidly.

Numerical midpoint targeting using the exact prime/cusp pieces and the leading
large-j arch approximation gives the far combined cross norm about

    ||A0_[21,6001],[16005,infty)||_2 ~= 0.45807.

The important point is not this decimal itself but the proof architecture:
certify a small 2K x 2K Gram matrix for the truncated low-rank factorization,
then bound the geometric remainder analytically.

Using only the safe global bounds

    |A_j| <= 2.927,
    |Si(j*pi)| <= 2,
    |H_j| <= 1/2,

one has |Z_j| <= 8.854.  With interval-certified finite Z_m values on
21<=m<=6001, a K=5 truncation is expected to leave remainder below about
3.2e-6; K=6 below about 4e-7.  These remainder figures are midpoint targeting
values until the finite Z_m intervals are instantiated.

This checkpoint also corrects the previous hope that the remote n>=16005
coupling would be only a few 1e-3.  The prime/noncompact channel makes the
remote cross norm O(10^-1), not O(10^-3).  Entrywise triangle bounds are far too
wasteful; the low-rank Cauchy factorization preserves the cancellation.

No RH/GRH, exact-zero, or full high-complement positivity conclusion follows.
"""

M=6001
R=16005
RATIO=M/R
Z_GLOBAL_BOUND=8.854
MIDPOINT_FAR_COMBINED_NORM=0.45807
K5_REMAINDER_TARGET=3.2e-6
K6_REMAINDER_TARGET=4.0e-7

if __name__=='__main__':
    print('M/R =',RATIO)
    print('far combined norm target =',MIDPOINT_FAR_COMBINED_NORM)
    print('K=5 remainder target =',K5_REMAINDER_TARGET)
    print('K=6 remainder target =',K6_REMAINDER_TARGET)
    print('guardrail: Gram matrix and finite Z_m values still need interval certification')
