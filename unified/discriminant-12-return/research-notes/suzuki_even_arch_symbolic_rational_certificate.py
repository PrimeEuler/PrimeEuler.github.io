#!/usr/bin/env python3
"""Symbolic exact-rational even-mode archimedean certificate.

For the odd Suzuki sector the Fourier indices are even, n=2r, so b=r*pi and
sin(2b)=0, cos(2b)=+1.  With y=1/b the parity-correct recurrences are

    I_0=J_0=0,
    I_p=-p*y*J_{p-1},
    J_p=-2^p*y+p*y*I_{p-1}.

Using the exact Bernoulli/Euler Taylor coefficients of h_32, H_n^(32) and the
archimedean diagonal D_n^(32) become finite rational polynomials in y.  This
helper constructs those polynomials exactly and bounds the uncertainty caused
by the certified rational interval for pi.  Since y~1/r, the termwise width
bound is maximal at r=11, so one calculation covers all modes 22..4000.

The separate analytic truncation from the audited polynomial certificate is

    ||h-h_32||_infty < 6.1e-14,
    ||Delta K_arch||_2 <= 1.22e-13.

Thus the pi/polynomial evaluation uncertainty shown here is negligible next to
the dimension-free analytic tail.
"""
from fractions import Fraction
from math import comb,factorial

N=32
RMIN=11


def atan_interval(x,K):
    s=Fraction(0)
    for k in range(K+1):
        t=x**(2*k+1)/(2*k+1)
        s += t if k%2==0 else -t
    rem=x**(2*K+3)/(2*K+3)
    return (s,s+rem) if (K+1)%2==0 else (s-rem,s)


def pi_interval():
    a,b=atan_interval(Fraction(1,5),12)
    c,d=atan_interval(Fraction(1,239),3)
    return 16*a-4*d,16*b-4*c


def bernoulli_numbers(nmax):
    A=[Fraction(0) for _ in range(nmax+1)]
    B=[]
    for m in range(nmax+1):
        A[m]=Fraction(1,m+1)
        for j in range(m,0,-1):
            A[j-1]=j*(A[j-1]-A[j])
        B.append(A[0])
    return B


def h_coefficients():
    B=bernoulli_numbers(2*N)
    E={0:1}
    for n in range(1,N+1):
        E[2*n]=-sum(comb(2*n,2*k)*E[2*k] for k in range(n))
    a=[Fraction(0) for _ in range(2*N+1)]
    # sech(t/2)
    for r in range(N+1):
        p=2*r
        a[p]+=Fraction(1,4)*Fraction(E[p],factorial(p))*Fraction(1,2**p)
    # csch(t/2)-2/t
    for r in range(1,N+1):
        p=2*r-1
        c=Fraction(2*(1-2**(2*r-1)),1)*B[2*r]/factorial(2*r)
        a[p]+=Fraction(1,4)*c*Fraction(1,2**p)
    return a


def padd(a,b):
    out=a.copy()
    for k,v in b.items(): out[k]=out.get(k,Fraction(0))+v
    return {k:v for k,v in out.items() if v}


def pscale(a,c): return {k:v*c for k,v in a.items() if v*c}
def py(a): return {k+1:v for k,v in a.items()}


def HD_polynomials():
    coeff=h_coefficients()
    I=[{} for _ in range(len(coeff)+2)]
    J=[{} for _ in range(len(coeff)+2)]
    for p in range(1,len(coeff)+2):
        I[p]=pscale(py(J[p-1]),-p)
        J[p]=padd({1:Fraction(-2**p)},pscale(py(I[p-1]),p))
    H={}; D={}
    for p,a in enumerate(coeff):
        H=padd(H,pscale(J[p],a))
        bracket=padd(padd(pscale(I[p],2),pscale(I[p+1],-1)),py(J[p]))
        D=padd(D,pscale(bracket,-a))
    return H,D


def polynomial_interval_width_bound(poly,r=RMIN):
    pilo,pihi=pi_interval()
    ylo=Fraction(1,r*pihi)
    yhi=Fraction(1,r*pilo)
    # For each monomial c*y^k the endpoint width is |c|(yhi^k-ylo^k).
    # Summing absolute widths is valid without relying on cancellation.  Every
    # term decreases as r increases, so r=RMIN is a uniform bound.
    return sum(abs(c)*(yhi**k-ylo**k) for k,c in poly.items())


def report():
    H,D=HD_polynomials()
    Hwidth=polynomial_interval_width_bound(H)
    Dwidth=polynomial_interval_width_bound(D)
    print('nonzero powers in H polynomial =',len(H))
    print('nonzero powers in D polynomial =',len(D))
    print('uniform H_32 pi-interval width <',float(Hwidth))
    print('uniform D_32 pi-interval width <',float(Dwidth))
    print('audited analytic arch operator tail <= 1.22e-13')
    assert float(Hwidth) < 9.3e-23
    assert float(Dwidth) < 1.3e-23


if __name__=='__main__':
    report()
