#!/usr/bin/env python3
"""Transfer the validated legacy Suzuki cross bound to the corrected operator.

After Audit Rounds 20-21 the intended archimedean off-diagonal formula differs
from the legacy formula used in the old N=16003 cross certificate.  The old
certificate is therefore NOT a certificate for the intended operator.  It is,
however, still usable as a validated bound for the legacy matrix that it
actually assembled.

Let

    G_corr   = G_cp + G_arch_corr,
    G_legacy = G_cp + G_arch_legacy,

where G_cp is the common cusp+prime cross block.  Then

    ||G_corr|| <= ||G_legacy||
                 + ||G_arch_corr|| + ||G_arch_legacy||.

The global centered-arch estimate from v13.380 is

    |Ytilde_n| = |n H_n-c_inf| < C/n^2,   C=1.27,

with

    c_inf = (2/pi) exp(-1)/(1-exp(-4)).

For odd 21<=m<=16001<n, n odd, the corrected arch entry is

    Kc_mn = pi*m*n*(Ytilde_n-Ytilde_m)/(m^2-n^2).

Since n>m,

    m n (m^-2+n^-2)/(n^2-m^2)
      = (n^2+m^2)/(m n (n^2-m^2))
      <= 1/(m(n-m)),

hence

    |Kc_mn| <= pi*C/[m(n-m)].

Write m=16003-2J, J=1,...,7991.  For fixed m,

    sum_{n>=16003, odd} 1/(n-m)^2
      = (1/4) sum_{j>=J} j^-2
      <= (1/4)(J^-2+J^-1).

The resulting finite rational sum gives the HS bound below.

For the legacy arch formula,

    Kl_mn = -(4/pi)(n H_m-m H_n)/(n^2-m^2),

substitute H_k=(c_inf+Ytilde_k)/k.  The constant part is exactly

    -(4/pi)c_inf/(mn).

The centered remainder satisfies

    |remainder_mn| <= (8*C/pi)/[m^3(n-m)].

We bound the constant part by product odd-tail sums and the remainder by the
same J-sum used above.

The legacy validated cross certificate gave

    ||G_legacy|| < 0.99918

under its stated validated-computation arithmetic model.  Combining these
bounds transfers that certificate to the corrected operator without claiming
that the legacy formula itself was correct.
"""

import math

M0 = 21
M1 = 16001
N0 = 16003
C = 1.27
LEGACY_CROSS_BOUND = 0.99918
C_INF = (2.0/math.pi)*math.exp(-1.0)/(1.0-math.exp(-4.0))


def odd_sum2_tail_bound(N: int) -> float:
    return 1.0/N**2 + 1.0/(2.0*N)


def corrected_arch_hs_bound() -> float:
    s = 0.0
    for J in range(1, 7992):
        m = N0 - 2*J
        tail_j = 1.0/J**2 + 1.0/J
        s += 0.25*tail_j/m**2
    return math.pi*C*math.sqrt(s)


def legacy_arch_hs_bound() -> float:
    # Constant c_inf/(mn) component.
    sm = odd_sum2_tail_bound(M0)
    sn = odd_sum2_tail_bound(N0)
    constant = (4.0/math.pi)*C_INF*math.sqrt(sm*sn)

    # Centered remainder <= (8 C/pi)/(m^3(n-m)).
    s = 0.0
    for J in range(1, 7992):
        m = N0 - 2*J
        tail_j = 1.0/J**2 + 1.0/J
        s += 0.25*tail_j/m**6
    remainder = (8.0*C/math.pi)*math.sqrt(s)
    return constant + remainder


def corrected_cross_bound() -> float:
    return LEGACY_CROSS_BOUND + corrected_arch_hs_bound() + legacy_arch_hs_bound()


if __name__ == '__main__':
    bc = corrected_arch_hs_bound()
    bl = legacy_arch_hs_bound()
    bg = corrected_cross_bound()
    print('corrected arch HS bound =', bc)
    print('legacy arch HS bound    =', bl)
    print('legacy cross certificate=', LEGACY_CROSS_BOUND)
    print('corrected cross bound   =', bg)
    if not bg < 1.01:
        raise SystemExit('FAIL: corrected cross transfer does not clear 1.01')
    print('PASS: corrected cross norm < 1.01 by legacy-certificate transfer')
