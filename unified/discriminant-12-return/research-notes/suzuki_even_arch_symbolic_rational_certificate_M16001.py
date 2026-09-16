#!/usr/bin/env python3
"""Exact-rational archimedean evaluation certificate for M=16001.

Extends the audited symbolic polynomial evaluation of
suzuki_even_arch_symbolic_rational_certificate.py to the odd Fourier modes
n=21,23,...,16001 used by the even-sector M16001 replay.

The analytic Taylor truncation is unchanged and dimension-free:
    ||h-h_32||_inf < 6.1e-14,
    ||Delta K_arch||_2 <= 1.22e-13.
This helper certifies only the rational evaluation of the degree-64
polynomials H^(32),D^(32); all endpoints are Fraction values.
"""
from fractions import Fraction
from math import comb,factorial

N=32
NMIN=21
NMAX=16001


def atan_interval(x,K):
    s=Fraction(0)
    for k in range(K+1):
        t=x**(2*k+1)/(2*k+1)
        s += t if k%2==0 else -t
    rem=x**(2*K+3)/(2*K+3)
    return (s,s+rem) if (K+1)%2==0 else (s-rem,s)


def pi_interval():
    a,b=atan_interval(Fraction(1,5),30)
    c,d=atan_interval(Fraction(1,239),10)
    return 16*a-4*d,16*b-4*c


def bernoulli_numbers(nmax):
    A=[Fraction(0) for _ in range(nmax+1)]; B=[]
    for m in range(nmax+1):
        A[m]=Fraction(1,m+1)
        for j in range(m,0,-1): A[j-1]=j*(A[j-1]-A[j])
        B.append(A[0])
    return B


def h_coefficients():
    B=bernoulli_numbers(2*N); E={0:1}
    for n in range(1,N+1):
        E[2*n]=-sum(comb(2*n,2*k)*E[2*k] for k in range(n))
    a=[Fraction(0) for _ in range(2*N+1)]
    for r in range(N+1):
        p=2*r; a[p]+=Fraction(1,4)*Fraction(E[p],factorial(p))*Fraction(1,2**p)
    for r in range(1,N+1):
        p=2*r
        c=Fraction(2*(1-2**(2*r-1)),1)*B[2*r]/factorial(2*r)
        a[p-1]+=Fraction(1,4)*c*Fraction(1,2**(p-1))
    return a


def padd(a,b):
    o=a.copy()
    for k,v in b.items(): o[k]=o.get(k,Fraction(0))+v
    return {k:v for k,v in o.items() if v}
def pscale(a,c): return {k:v*c for k,v in a.items() if v*c}
def py(a): return {k+1:v for k,v in a.items()}


def HD_polynomials(sign):
    """sign=cos(2b)=(-1)^n.  M16001 odd modes use sign=-1."""
    coeff=h_coefficients(); I=[{} for _ in range(len(coeff)+2)]; J=[{} for _ in range(len(coeff)+2)]
    for p in range(1,len(coeff)+2):
        # At b=n*pi/2, sin(2b)=0 and cos(2b)=sign.
        I[p]=pscale(py(J[p-1]),-p)
        J[p]=padd({1:Fraction(-sign*2**p)},pscale(py(I[p-1]),p))
    H={}; D={}
    for p,a in enumerate(coeff):
        H=padd(H,pscale(J[p],a))
        bracket=padd(padd(pscale(I[p],2),pscale(I[p+1],-1)),py(J[p]))
        D=padd(D,pscale(bracket,-a))
    return H,D


def width(poly,n):
    pilo,pihi=pi_interval()
    # b=n*pi/2, hence y=1/b=2/(n*pi).
    ylo=Fraction(2,n*pihi); yhi=Fraction(2,n*pilo)
    return sum(abs(c)*(yhi**k-ylo**k) for k,c in poly.items())


def report():
    H,D=HD_polynomials(-1)
    # Every monomial width decreases with n, so n=21 is the uniform maximum.
    Hw=width(H,NMIN); Dw=width(D,NMIN)
    print('M16001 odd-mode arch rational evaluation')
    print('H32 width <=',float(Hw),'at n=21')
    print('D32 width <=',float(Dw),'at n=21')
    print('analytic dimension-free arch operator tail <= 1.22e-13')
    assert Hw < Fraction(1,10**38)
    assert Dw < Fraction(1,10**39)
    print('PASS: rational evaluation is negligible relative to 1.22e-13 analytic tail')

if __name__=='__main__': report()
