#!/usr/bin/env python3
"""Exact-rational prime trigonometric/source error certificate.

This continues suzuki_prime_base_rational_certificate.py.  It turns the
certified intervals for pi*log(q) into sin/cos intervals using exact Fraction
Taylor polynomials, propagates those base-rotation errors through r<=2000, and
adds rational sqrt(q) brackets for the von Mangoldt weights.

No scipy/mpmath transcendental routine is used in the certificate arithmetic.
The outputs are source-enclosure bounds, not by themselves a matrix positivity
certificate.
"""
from fractions import Fraction
from math import factorial

QS=(2,3,4,5,7)
LOG_K={2:12,3:19,4:26,5:32,7:46}
VM_SOURCE={2:2,3:3,4:2,5:5,7:7}
RMAX=2000
TAYLOR_DEGREE=40

SQRT_BRACKETS={
    2:(Fraction(141421356237,10**11),Fraction(141421356238,10**11)),
    3:(Fraction(173205080756,10**11),Fraction(173205080757,10**11)),
    4:(Fraction(2),Fraction(2)),
    5:(Fraction(223606797749,10**11),Fraction(223606797750,10**11)),
    7:(Fraction(264575131106,10**11),Fraction(264575131107,10**11)),
}


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


def log_interval(q,K):
    x=Fraction(q-1,q+1)
    s=Fraction(0)
    for k in range(K+1):
        s += 2*x**(2*k+1)/(2*k+1)
    rem=2*x**(2*K+3)/(2*K+3)/(1-x*x)
    return s,s+rem


def mul_pos(a,b):
    return a[0]*b[0],a[1]*b[1]


def div_pos(a,b):
    return a[0]/b[1],a[1]/b[0]


def trig_base(alpha,degree=TAYLOR_DEGREE):
    lo,hi=alpha
    a=(lo+hi)/2
    rho=(hi-lo)/2
    s=Fraction(0); c=Fraction(0)
    for j in range(degree+1):
        if 2*j+1<=degree:
            s += (-1 if j%2 else 1)*a**(2*j+1)/factorial(2*j+1)
        if 2*j<=degree:
            c += (-1 if j%2 else 1)*a**(2*j)/factorial(2*j)
    A=max(abs(lo),abs(hi))
    rem=A**(degree+1)/factorial(degree+1)
    rad=rho+rem
    return (s-rad,s+rad),(c-rad,c+rad),rad


def report():
    p=pi_interval()
    logs={q:log_interval(q,LOG_K[q]) for q in (2,3,5,7)}
    logs[4]=(2*logs[2][0],2*logs[2][1])

    for q,(lo,hi) in SQRT_BRACKETS.items():
        if q==4:
            assert lo==hi==2
        else:
            assert lo*lo < q < hi*hi

    weights={q:div_pos(logs[VM_SOURCE[q]],SQRT_BRACKETS[q]) for q in QS}
    power_err={}
    for q in QS:
        alpha=mul_pos(p,logs[q])
        _,_,rad=trig_base(alpha)
        # If every sin/cos entry is within rad, the 2x2 rotation matrix
        # perturbation has Frobenius (hence operator) norm <=2*rad.
        eta=2.0*float(rad)
        power_err[q]=RMAX*eta*(1.0+eta)**(RMAX-1)
        print('q',q,
              'alpha width',float(alpha[1]-alpha[0]),
              'r<=2000 trig error',power_err[q],
              'weight width',float(weights[q][1]-weights[q][0]))

    seq_err=0.0
    for q in QS:
        wlo,whi=weights[q]
        seq_err += float(whi)*power_err[q] + 0.5*float(whi-wlo)
    print('uniform prime-sequence error <',seq_err)

    # Prime diagonal S_nn=(2-ell)cos(r alpha)+sin(r alpha)/(r*pi), r>=11.
    pi_lo=float(p[0]); pi_hi=float(p[1])
    diag_err=0.0
    for q in QS:
        llo,lhi=map(float,logs[q])
        lrad=(lhi-llo)/2.0
        eps=power_err[q]
        coeff=max(abs(2.0-llo),abs(2.0-lhi))
        inv_lo=1.0/(11.0*pi_hi)
        inv_hi=1.0/(11.0*pi_lo)
        inv_rad=(inv_hi-inv_lo)/2.0
        Serr=(coeff*eps + lrad*(1.0+eps)
              + eps*inv_hi + (1.0+eps)*inv_rad)
        Sabs=coeff+inv_hi
        wlo,whi=map(float,weights[q])
        wrad=(whi-wlo)/2.0
        diag_err += whi*Serr + wrad*Sabs
    print('uniform full prime-diagonal error <',diag_err)

    assert max(power_err.values()) < 6e-10
    assert seq_err < 1e-9
    assert diag_err < 4e-10


if __name__=='__main__':
    report()
