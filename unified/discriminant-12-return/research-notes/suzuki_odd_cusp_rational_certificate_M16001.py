#!/usr/bin/env python3
"""Exact-rational odd-mode Si/Ci cusp certificate through M=16001.

For odd n and x=n*pi, Si(x)=pi/2+F(x), Ci(x)=G(x), where F,G are the
standard Laplace auxiliary functions. Finite geometric division gives rigorous
inverse-power expansions with first-omitted-moment remainders.

Targets n=21,23,...,16001, the finite-high band in the M16001 even replay.
All endpoints are Fraction values; no scipy/mpmath special function enters.
"""
from fractions import Fraction
from math import factorial
NMIN=21; NMAX=16001; FG_M=12; LOG_K=48

def atan_interval(x,K):
    s=Fraction(0)
    for k in range(K+1):
        t=x**(2*k+1)/(2*k+1); s += t if k%2==0 else -t
    rem=x**(2*K+3)/(2*K+3)
    return (s,s+rem) if (K+1)%2==0 else (s-rem,s)
def pi_interval():
    a,b=atan_interval(Fraction(1,5),30); c,d=atan_interval(Fraction(1,239),10)
    return 16*a-4*d,16*b-4*c
def atanh_log_interval(y,K=LOG_K):
    x=(y-1)/(y+1); assert 0<=x<=Fraction(1,3)
    s=sum((2*x**(2*k+1)/(2*k+1) for k in range(K+1)),Fraction(0))
    rem=2*x**(2*K+3)/(2*K+3)/(1-x*x); return s,s+rem
def iadd(a,b): return a[0]+b[0],a[1]+b[1]
def ineg(a): return -a[1],-a[0]
def iscale(a,c): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def idiv(a,b):
    assert b[0]>0; v=(a[0]/b[0],a[0]/b[1],a[1]/b[0],a[1]/b[1]); return min(v),max(v)
def rp(x,k): return Fraction(1,x[1]**k),Fraction(1,x[0]**k)
PI=pi_interval(); LOG2=atanh_log_interval(Fraction(2))
def log_n_over_4_interval(n):
    y=Fraction(n,4); e=0
    while y>=2: y/=2; e+=1
    while y<1: y*=2; e-=1
    return iadd(iscale(LOG2,e),atanh_log_interval(y))
def FG_interval(n,m=FG_M):
    x=(n*PI[0],n*PI[1]); F=(Fraction(0),Fraction(0)); G=F
    for j in range(m):
        F=iadd(F,iscale(rp(x,2*j+1),(-1)**j*factorial(2*j)))
        G=iadd(G,iscale(rp(x,2*j+2),(-1)**j*factorial(2*j+1)))
    rf=Fraction(factorial(2*m),1)/x[0]**(2*m+1)
    rg=Fraction(factorial(2*m+1),1)/x[0]**(2*m+2)
    return (F[0]-rf,F[1]+rf),(G[0]-rg,G[1]+rg),x
def cusp_interval(n):
    L=log_n_over_4_interval(n); F,G,x=FG_interval(n)
    Si=iadd(iscale(PI,Fraction(1,2)),F)
    C=iadd(iadd(L,ineg(G)),ineg(idiv(Si,x)))
    return Si,G,C
def report():
    maxima={k:(Fraction(0),None) for k in ('Si','Ci','cusp')}
    for n in range(NMIN,NMAX+1,2):
        for key,I in zip(('Si','Ci','cusp'),cusp_interval(n)):
            w=I[1]-I[0]
            if w>maxima[key][0]: maxima[key]=(w,n)
    for key,(w,n) in maxima.items(): print('max',key,'width <',float(w),'at n',n)
    si_radius=maxima['Si'][0]/2; diag_radius=maxima['cusp'][0]/2
    matrix_bound=Fraction(7991)*2*max(si_radius,diag_radius)
    print('cusp Si/source radius <',float(si_radius))
    print('cusp diagonal radius <',float(diag_radius))
    print('conservative 7991x7991 cusp operator bound <',float(matrix_bound))
    assert maxima['Si'][0] < Fraction(5,10**22)
    assert maxima['Ci'][0] < Fraction(2,10**22)
    assert maxima['cusp'][0] < Fraction(2,10**22)
    assert matrix_bound < Fraction(4,10**18)
    print('PASS: certified odd-mode cusp reconstruction covers n=21..16001')
if __name__=='__main__': report()
