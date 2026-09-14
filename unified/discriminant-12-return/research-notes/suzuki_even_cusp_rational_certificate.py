#!/usr/bin/env python3
"""Exact-rational certificate for the even-mode Suzuki cusp scalars.

For n even, x=n*pi has sin(x)=0 and cos(x)=1 exactly.  Therefore

    Si(x)=pi/2-F(x),  Ci(x)=-G(x),

where the standard auxiliary functions have Laplace representations

    F(x)=int_0^inf exp(-x t)/(1+t^2) dt,
    G(x)=int_0^inf t exp(-x t)/(1+t^2) dt.

Expanding 1/(1+t^2) by the finite geometric identity gives rigorous finite
inverse-power expansions with remainder bounded by the first omitted Laplace
moment.  The logarithm log(n/4) is range-reduced to e*log(2)+log(y), 1<=y<2,
and log(y) is enclosed by the positive atanh series with x<1/3.

All interval endpoints are Fractions.  No scipy/mpmath special function is
used.  This certifies the scalar source intervals; matrix assembly and the
archimedean/prime channels are separate proof obligations.
"""
from fractions import Fraction
from math import factorial

NMIN=22
NMAX=4000
LOG_K=18
FG_M=4


def atan_interval(x,K):
    s=Fraction(0)
    for k in range(K+1):
        term=x**(2*k+1)/(2*k+1)
        s += term if k%2==0 else -term
    rem=x**(2*K+3)/(2*K+3)
    return (s,s+rem) if (K+1)%2==0 else (s-rem,s)


def pi_interval():
    a,b=atan_interval(Fraction(1,5),12)
    c,d=atan_interval(Fraction(1,239),3)
    return 16*a-4*d,16*b-4*c


def atanh_log_interval(y,K=LOG_K):
    x=(y-1)/(y+1)
    assert 0 <= x < Fraction(1,3)+Fraction(1,10**30)
    s=Fraction(0)
    for k in range(K+1):
        s += 2*x**(2*k+1)/(2*k+1)
    rem=2*x**(2*K+3)/(2*K+3)/(1-x*x)
    return s,s+rem


def iadd(a,b): return a[0]+b[0],a[1]+b[1]
def ineg(a): return -a[1],-a[0]
def iscale(a,c): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])

def idiv(a,b):
    assert b[0]>0
    vals=(a[0]/b[0],a[0]/b[1],a[1]/b[0],a[1]/b[1])
    return min(vals),max(vals)


def reciprocal_power_interval(x,k):
    assert x[0]>0
    return Fraction(1,x[1]**k),Fraction(1,x[0]**k)


PI=pi_interval()
LOG2=atanh_log_interval(Fraction(2))


def log_n_over_4_interval(n):
    y=Fraction(n,4)
    e=0
    while y>=2:
        y/=2; e+=1
    while y<1:
        y*=2; e-=1
    return iadd(iscale(LOG2,e),atanh_log_interval(y))


def FG_interval(n,m=FG_M):
    x=(n*PI[0],n*PI[1])
    F=(Fraction(0),Fraction(0))
    G=(Fraction(0),Fraction(0))
    for k in range(m+1):
        F=iadd(F,iscale(reciprocal_power_interval(x,2*k+1),(-1)**k*factorial(2*k)))
        G=iadd(G,iscale(reciprocal_power_interval(x,2*k+2),(-1)**k*factorial(2*k+1)))
    # Geometric identity remainder integrated against exp(-x t).
    rf=Fraction(factorial(2*m+2),1)/x[0]**(2*m+3)
    rg=Fraction(factorial(2*m+3),1)/x[0]**(2*m+4)
    F=(F[0]-rf,F[1]+rf)
    G=(G[0]-rg,G[1]+rg)
    return F,G,x


def report():
    max_log=max_Si=max_cusp=0.0
    arg_log=arg_Si=arg_cusp=None
    for n in range(NMIN,NMAX+1,2):
        L=log_n_over_4_interval(n)
        F,G,x=FG_interval(n)
        Si=iadd(iscale(PI,Fraction(1,2)),ineg(F))
        # cusp = log(n/4)-Ci-Si/x = log(n/4)+G-Si/x
        cusp=iadd(iadd(L,G),ineg(idiv(Si,x)))
        lw=float(L[1]-L[0])
        sw=float(Si[1]-Si[0])
        cw=float(cusp[1]-cusp[0])
        if lw>max_log: max_log,arg_log=lw,n
        if sw>max_Si: max_Si,arg_Si=sw,n
        if cw>max_cusp: max_cusp,arg_cusp=cw,n
    print('max log(n/4) width =',max_log,'at n=',arg_log)
    print('max Si(n*pi) width =',max_Si,'at n=',arg_Si)
    print('max cusp diagonal width =',max_cusp,'at n=',arg_cusp)
    assert max_log < 1.4e-19
    assert max_Si < 4.3e-14
    assert max_cusp < 7.4e-15


if __name__=='__main__':
    report()
