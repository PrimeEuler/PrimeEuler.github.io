#!/usr/bin/env python3
"""Source-sensitivity budget for the odd-sector even-index finite-high block.

This file does not itself generate proof-grade scalar intervals.  It converts
uniform scalar-sequence enclosures into an operator-norm budget for

    F={22,24,...,4000}.

For off-diagonal entries

  A_mn = -(2/pi) (n Z_m - m Z_n)/(n^2-m^2),

uniform |dZ_j|<=eZ implies

  |dA_mn| <= (2/pi) eZ/|n-m|.

Because the modes have spacing 2, the maximum row sum is

  (eZ/pi) max_i (H_i + H_{N-1-i}).

This is far sharper than N*max-entry conversion.
"""
from __future__ import annotations

from math import pi, factorial

N = 1990
START = 22


def harmonic(k: int) -> float:
    return sum(1.0/j for j in range(1, k + 1))


H = [0.0]
for k in range(1, N):
    H.append(H[-1] + 1.0/k)
MAX_HPAIR = max(H[i] + H[N-1-i] for i in range(N))
Z_TO_OPERATOR = MAX_HPAIR / pi

# A deliberately loose scalar target package.  These are targets for a future
# outward generator, not assumptions about scipy.
E_H = 1.0e-8
E_PRIME_SEQUENCE = 2.0e-6
E_SI = 1.0e-8
E_Z = 2.0*E_PRIME_SEQUENCE + E_SI + 2.0*E_H

E_ARCH_DIAG_NOMINAL = 1.0e-6
E_PRIME_DIAG = 1.0e-5
E_CUSP_DIAG = 1.0e-6
ARCH_ANALYTIC_OPERATOR = 1.22e-13

OFFDIAG_OPERATOR = Z_TO_OPERATOR * E_Z
TOTAL_TARGET = (
    OFFDIAG_OPERATOR
    + E_ARCH_DIAG_NOMINAL
    + E_PRIME_DIAG
    + E_CUSP_DIAG
    + ARCH_ANALYTIC_OPERATOR
)

# Even-mode cusp simplification. At x=n*pi with even n:
#   Si(x)=pi/2-F(x),  Ci(x)=-G(x)
# where
#   F=1/x-2!/x^3+4!/x^5-6!/x^7+...
#   G=1/x^2-3!/x^4+5!/x^6-7!/x^8+...
# For x>=22*pi the displayed terms decrease strongly.  After retaining
# through 4!/x^5 and 5!/x^6 respectively, the first omitted magnitudes are:
x0 = START*pi
F_REM_FIRST = factorial(6)/x0**7
G_REM_FIRST = factorial(7)/x0**8

if __name__ == '__main__':
    print('dimension =', N)
    print('max harmonic pair =', MAX_HPAIR)
    print('uniform dZ -> operator constant =', Z_TO_OPERATOR)
    print('chosen eZ =', E_Z)
    print('off-diagonal operator budget =', OFFDIAG_OPERATOR)
    print('total illustrative source budget =', TOTAL_TARGET)
    print('cusp F first omitted term at n=22 =', F_REM_FIRST)
    print('cusp G first omitted term at n=22 =', G_REM_FIRST)
    assert Z_TO_OPERATOR < 4.762
    assert OFFDIAG_OPERATOR < 2.0e-5
    assert TOTAL_TARGET < 3.2e-5
    assert F_REM_FIRST < 1.0e-10
    assert G_REM_FIRST < 1.0e-11
