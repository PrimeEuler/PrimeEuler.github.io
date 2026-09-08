#!/usr/bin/env python3
"""Cusp Si/Ci certification reduction at odd integer multiples of pi.

For x=n*pi with odd n,

    Si(x)=pi/2 + F(x),
    Ci(x)=G(x),

where

    F(x)=int_0^infty exp(-x t)/(1+t^2) dt,
    G(x)=int_0^infty t exp(-x t)/(1+t^2) dt.

Finite geometric division gives rigorous asymptotic enclosures

    F=sum_{j=0}^{M-1} (-1)^j (2j)!/x^(2j+1) + R_F,
    |R_F| <= (2M)!/x^(2M+1),

    G=sum_{j=0}^{M-1} (-1)^j (2j+1)!/x^(2j+2) + R_G,
    |R_G| <= (2M+1)!/x^(2M+2).

For n>=9, near-optimal truncation is already at or below the 1e-11-ish
certificate scale required for the finite matrix.

For n=1,3,5,7 use the globally convergent entire series

    Si(x)=sum_{k>=0} (-1)^k x^(2k+1)/((2k+1)(2k+1)!),

    Ci(x)=gamma+log(x)+sum_{k>=1} (-1)^k x^(2k)/(2k(2k)!).

The Euler constant gamma itself can be enclosed with Euler-Maclaurin at N=64:

 gamma = H_N-log N-1/(2N)
         + sum_{k=1}^{m-1} B_{2k}/(2k N^(2k)) + R_m,

with the standard Bernoulli remainder bounded by the first omitted term.
Since N=64 is a power of two, log N uses only the already-certified log 2.

Finally, log(n/4) in the cusp diagonal is certified by the same atanh log
series used for the prime block.  Thus no general-purpose Si/Ci evaluator is
needed in the final finite certificate.
"""

SMALL_MODES=(1,3,5,7)
ASYMPTOTIC_START=9
EULER_MACLAURIN_N=64
TARGET_SCALAR_RADIUS=1e-11


def F_remainder_bound(n: int, M: int) -> float:
    import math
    x=n*math.pi
    return math.factorial(2*M)/x**(2*M+1)


def G_remainder_bound(n: int, M: int) -> float:
    import math
    x=n*math.pi
    return math.factorial(2*M+1)/x**(2*M+2)


def best_simple_bound(n: int):
    """Scan safe modest M values for descriptive remainder scale."""
    vals=[]
    for M in range(1,40):
        try:
            vals.append((max(F_remainder_bound(n,M),G_remainder_bound(n,M)),M))
        except OverflowError:
            break
    return min(vals)


if __name__=='__main__':
    for n in (9,11,13,19,153):
        print(n,best_simple_bound(n))
    print('small modes use convergent Si/Ci series + Euler-Maclaurin gamma')
