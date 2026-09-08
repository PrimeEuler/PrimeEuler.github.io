#!/usr/bin/env python3
"""Exact fixed-core prime-tail decay audit for Suzuki's a=1 even-v sector.

Let psi_n be the normalized odd Dirichlet modes (n odd), written in the even
cosine convention psi_n(x)=+/- cos(n*pi*x/2). For one truncated translation

    (S_l f)(x)=f(x-l)+f(x+l),

with zero extension outside [-1,1], the matrix element for odd m != n is

    <psi_m,S_l psi_n>
      = (-1)^((m-n)/2) [sin(b l)-sin(a l)]/(a-b)
        - (-1)^((m+n)/2) [sin(b l)+sin(a l)]/(a+b),

where a=m*pi/2 and b=n*pi/2. Hence, for n>m,

    |<psi_m,S_l psi_n>|
      <= (2/pi)(1+|sin(a l)|)[1/(n-m)+1/(n+m)].

For the Suzuki prime operator

    B_prime = -sum_q w_q S_{log q},
    q in {2,3,4,5,7},  w_q=Lambda(q)/sqrt(q),

set

    C_m = sum_q w_q (1+|sin((m*pi/2) log q)|).

Then for a fixed core m<=19 and odd n>=N>19,

    |(B_prime)_{mn}|
      <= (4 C_m/pi) / [n(1-(m/N)^2)].

Therefore the fixed-core-to-tail block is Hilbert-Schmidt and

    ||P_tail B_prime P_core||
      <= ||.||_HS
      <= sqrt( sum_m (4 C_m/pi)^2/(1-(m/N)^2)^2 * S_2(N) ),

where

    S_2(N)=sum_{n>=N,n odd}1/n^2
           <= 1/N^2 + 1/(2N).

This proves analytic O(N^-1/2) decoupling of every fixed finite core from the
remote prime tail. It does NOT imply the moving buffer/tail interface decays;
the prime shift operator remains noncompact there.

Displayed decimal constants are ordinary floating evaluations of exact closed
forms, not interval-certified enclosures. No RH/GRH, kernel, or lambda_1=0
conclusion follows.
"""
from __future__ import annotations

import math

SHIFTS = [math.log(2.0), math.log(3.0), math.log(4.0),
          math.log(5.0), math.log(7.0)]
WEIGHTS = [math.log(2.0)/math.sqrt(2.0),
           math.log(3.0)/math.sqrt(3.0),
           math.log(2.0)/2.0,
           math.log(5.0)/math.sqrt(5.0),
           math.log(7.0)/math.sqrt(7.0)]
CORE = list(range(1, 20, 2))


def shift_entry(m: int, n: int, ell: float) -> float:
    if m % 2 == 0 or n % 2 == 0 or m == n:
        raise ValueError('use distinct odd m,n')
    a = m*math.pi/2.0
    b = n*math.pi/2.0
    sig_d = -1.0 if (((m-n)//2) % 2) else 1.0
    sig_s = -1.0 if (((m+n)//2) % 2) else 1.0
    return (sig_d*(math.sin(b*ell)-math.sin(a*ell))/(a-b)
            - sig_s*(math.sin(b*ell)+math.sin(a*ell))/(a+b))


def prime_entry(m: int, n: int) -> float:
    return -sum(w*shift_entry(m, n, ell)
                for ell, w in zip(SHIFTS, WEIGHTS))


def C_m(m: int) -> float:
    a = m*math.pi/2.0
    return sum(w*(1.0+abs(math.sin(a*ell)))
               for ell, w in zip(SHIFTS, WEIGHTS))


def odd_sum2_tail_bound(N: int) -> float:
    return 1.0/N**2 + 1.0/(2.0*N)


def analytic_core_tail_hs_bound(N: int) -> float:
    if N <= max(CORE):
        raise ValueError('N must exceed the fixed core')
    s2 = odd_sum2_tail_bound(N)
    total = 0.0
    for m in CORE:
        fac = (4.0*C_m(m)/math.pi)/(1.0-(m/N)**2)
        total += fac*fac*s2
    return math.sqrt(total)


def numerical_partial_hs(N: int, max_n: int = 3001) -> float:
    start = N if N % 2 else N+1
    total = 0.0
    for m in CORE:
        for n in range(start, max_n+1, 2):
            total += prime_entry(m, n)**2
    return math.sqrt(total)


def report(cutoffs=(151,237,301,401,501,1001), max_n: int = 3001):
    rows = []
    for N in cutoffs:
        rows.append({
            'N': N,
            'analytic_HS_bound': analytic_core_tail_hs_bound(N),
            'numerical_partial_HS_to_%d' % max_n: numerical_partial_hs(N,max_n),
        })
    return {
        'core': CORE,
        'C_m': {m:C_m(m) for m in CORE},
        'rows': rows,
    }


if __name__ == '__main__':
    r = report()
    print('fixed core', r['core'])
    print('C_m', r['C_m'])
    for row in r['rows']:
        print(row)
