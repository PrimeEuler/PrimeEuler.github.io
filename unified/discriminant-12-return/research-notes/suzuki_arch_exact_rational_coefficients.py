#!/usr/bin/env python3
"""Exact rational Taylor coefficients for the certified arch polynomial h_N.

h(t)=1/4[csch(t/2)+sech(t/2)-2/t].

Even powers come from sech:

  a_{2r}= (1/4) E_{2r}/((2r)! 2^(2r)).

Odd powers come from the regular part of csch:

  a_{2r-1}= (1/4)*2(1-2^(2r-1)) B_{2r}/((2r)! 2^(2r-1)), r>=1.

Bernoulli numbers are generated exactly from

  B_m=-(1/(m+1))*sum_{k=0}^{m-1} C(m+1,k) B_k,

and Euler numbers from

  E_{2n}=-sum_{k=0}^{n-1} C(2n,2k)E_{2k}.

All coefficients are fractions.Fraction objects; no floating arithmetic enters.
"""
from fractions import Fraction
from math import comb, factorial


def bernoulli_up_to(n):
    B=[Fraction(0) for _ in range(n+1)]
    B[0]=Fraction(1)
    for m in range(1,n+1):
        B[m]=-sum(Fraction(comb(m+1,k))*B[k] for k in range(m))/Fraction(m+1)
    return B


def euler_even_up_to(n):
    # returns E_0,E_2,...,E_{2n}
    E=[0]*(n+1)
    E[0]=1
    for j in range(1,n+1):
        E[j]=-sum(comb(2*j,2*k)*E[k] for k in range(j))
    return E


def h_coefficients(N=32):
    B=bernoulli_up_to(2*N+2)
    E=euler_even_up_to(N+1)
    degree=2*N+1
    a=[Fraction(0) for _ in range(degree+1)]
    for r in range(N+1):
        a[2*r]=Fraction(E[r],4*factorial(2*r)*2**(2*r))
    for r in range(1,N+2):
        p=2*r-1
        if p>degree: break
        a[p]=Fraction(2*(1-2**(2*r-1)),4*factorial(2*r)*2**(2*r-1))*B[2*r]
    return a


if __name__=='__main__':
    a=h_coefficients(32)
    for p in range(8):
        print(p,a[p])
