#!/usr/bin/env python3
"""Prime-block certification reduction for Suzuki a=1 finite matrix.

The prime block uses q in {2,3,4,5,7}, weights w_q=Lambda(q)/sqrt(q),
and theta_q=(pi/2) log q.  Instead of evaluating sin(n theta_q) and
cos(n theta_q) separately for every odd n<=153, certify only the base constants

    log q, sin(theta_q), cos(theta_q), sqrt(q), pi,

then generate all higher harmonics by Chebyshev/three-term recurrences:

    sin(n theta)=sin(theta) U_{n-1}(cos theta),
    cos(n theta)=T_n(cos theta).

The off-diagonal prime sequence

    A_n=sum_q w_q sin(n theta_q)

determines

    B_mn=-(4/pi)(n A_m-m A_n)/(n^2-m^2), m!=n.

Diagonal shifts use the same generated harmonics.  Thus the whole prime block
is a finite algebraic recurrence after certifying five logarithms and ten base
trigonometric constants.

For positive rational x, log x is certified by scaling x=2^k y with y in
[1,2) and using

    log y = 2 sum_{j=0}^{M-1} z^(2j+1)/(2j+1) + R,
    z=(y-1)/(y+1),
    |R| <= 2 |z|^(2M+1)/((2M+1)(1-z^2)).

Since |z|<=1/3, M=32 drives the analytic remainder far below 1e-28.
Base sine/cosine values can then be enclosed by ordinary Taylor series after
certified argument reduction.  A 1e-24 base trig enclosure is ample for odd
n<=153 even after conservative recurrence amplification.

No positivity/RH claim is made here; this is a certificate-construction step.
"""

QS=(2,3,4,5,7)
MAX_ODD_MODE=153
LOG_SERIES_TERMS=32
BASE_TRIG_TARGET=1e-24
PRIME_ENTRY_TARGET=1e-15


def log_atanh_remainder(z: float, M: int=LOG_SERIES_TERMS) -> float:
    az=abs(z)
    return 2*az**(2*M+1)/((2*M+1)*(1-az*az))


def offdiag_error_from_A(eA: float, mode_gap: int=2) -> float:
    """If all A_n radii <=eA, odd-mode spacing gives <=(4/pi)eA/gap."""
    import math
    return (4/math.pi)*eA/mode_gap


if __name__=='__main__':
    print('log series worst-case remainder=',log_atanh_remainder(1/3))
    print('prime block reduction: 5 logs + 10 base trig constants + recurrences')
