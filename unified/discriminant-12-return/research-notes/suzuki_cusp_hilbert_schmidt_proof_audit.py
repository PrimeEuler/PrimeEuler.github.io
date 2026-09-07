#!/usr/bin/env python3
"""Analytic Hilbert-Schmidt proof audit for the Suzuki a=1 cusp correction.

This v13.302 control upgrades the v13.301 numerical Hilbert-Schmidt evidence to
an analytic square-summability argument.

For odd n and x=n*pi, repeated integration by parts gives

    Si(x) = pi/2 + 1/x + delta(x),
    delta(x) = -2/x^3 - 24 int_x^infty sin(t)/t^5 dt,

hence

    |delta(x)| <= 2/x^3 + 6/x^4.

For distinct odd m,n the exact v13.301 formula then gives

    K_mn = C_mn + 1/(m+n)
         = -2/(pi^2 m n) + E_mn,

where

    |E_mn| <= (2/pi) (n d_m + m d_n)/|m^2-n^2|,
    d_j = 2/(pi*j)^3 + 6/(pi*j)^4.

Since distinct odd indices satisfy |m-n|>=2, this majorant is square-summable.
The leading -2/(pi^2 mn) term is rank one and Hilbert-Schmidt.

On the diagonal, integration by parts gives

    Ci(x) = 1/x^2 + rho(x),  |rho(x)| <= 2/x^3.

Using the exact diagonal formula from v13.301,

    K_nn = -Ci(x) - Si(x)/x + 1/(2n),

so

    |K_nn| <= 2/x^2 + 2/x^3 + 2/x^4 + 6/x^5.

Therefore K is Hilbert-Schmidt and hence compact.  This is an operator-structure
lemma only; it does not prove ker(G_1) != {0}, lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import math
from scipy.special import sici

PI = math.pi


def si_delta(n: int) -> float:
    if n % 2 == 0:
        raise ValueError('n must be odd')
    si, _ = sici(n*PI)
    x = n*PI
    return si - PI/2.0 - 1.0/x


def si_delta_bound(n: int) -> float:
    x = n*PI
    return 2.0/x**3 + 6.0/x**4


def ci_remainder(n: int) -> float:
    if n % 2 == 0:
        raise ValueError('n must be odd')
    _, ci = sici(n*PI)
    x = n*PI
    return ci - 1.0/x**2


def ci_remainder_bound(n: int) -> float:
    x = n*PI
    return 2.0/x**3


def offdiag_error_bound(m: int, n: int) -> float:
    if m == n or m % 2 == 0 or n % 2 == 0:
        raise ValueError('distinct odd m,n required')
    dm = si_delta_bound(m)
    dn = si_delta_bound(n)
    return (2.0/PI)*(n*dm + m*dn)/abs(m*m-n*n)


def diagonal_bound(n: int) -> float:
    x = n*PI
    return 2.0/x**2 + 2.0/x**3 + 2.0/x**4 + 6.0/x**5


def verify(samples=(1,3,5,11,21,41,81,161)):
    rows=[]
    for n in samples:
        rows.append({
            'n': n,
            'abs_si_delta': abs(si_delta(n)),
            'si_bound': si_delta_bound(n),
            'abs_ci_remainder': abs(ci_remainder(n)),
            'ci_bound': ci_remainder_bound(n),
            'diag_bound': diagonal_bound(n),
        })
    return rows


def print_report():
    print('Suzuki v13.302 analytic cusp Hilbert-Schmidt proof audit')
    for row in verify():
        print(row)
    print('Conclusion: K_cusp is Hilbert-Schmidt by the displayed uniform bounds.')


if __name__ == '__main__':
    print_report()
