#!/usr/bin/env python3
"""Exact-rational prime source certificate for the M=16001 replay.

Extends the earlier r<=2000 certificate to r<=8000 and deliberately
OVER-resolves pi, log(q), sqrt(q), and the base trigonometric rotations so the
prime-source enclosure is negligible relative to the 2e-13 global source
operator budget of ledger v13.357.

All certification arithmetic is fractions.Fraction / integer arithmetic.
Floating conversion is used only for human-readable printing after exact
rational assertions have passed.  No scipy/mpmath transcendental call enters
the certificate.
"""
from fractions import Fraction
from math import factorial, isqrt

QS=(2,3,4,5,7)
VM_SOURCE={2:2,3:3,4:2,5:5,7:7}
RMAX=8000
TAYLOR_DEGREE=120
# Chosen so each log interval is < 1e-45.
LOG_K={2:44,3:71,5:122,7:172}
SQRT_DIGITS=50


def atan_interval(x,K):
    s=Fraction(0)
    for k in range(K+1):
        t=x**(2*k+1)/(2*k+1)
        s += t if k%2==0 else -t
    rem=x**(2*K+3)/(2*K+3)
    return (s,s+rem) if (K+1)%2==0 else (s-rem,s)


def pi_interval():
    # Machin: pi=16 atan(1/5)-4 atan(1/239).
    a,b=atan_interval(Fraction(1,5),30)
    c,d=atan_interval(Fraction(1,239),10)
    return 16*a-4*d,16*b-4*c


def log_interval(q,K):
    x=Fraction(q-1,q+1)
    s=Fraction(0)
    for k in range(K+1):
        s += 2*x**(2*k+1)/(2*k+1)
    rem=2*x**(2*K+3)/(2*K+3)/(1-x*x)
    return s,s+rem


def sqrt_interval(q,digits=SQRT_DIGITS):
    D=10**digits
    a=isqrt(q*D*D)
    lo,hi=Fraction(a,D),Fraction(a+1,D)
    assert lo*lo < q < hi*hi
    return lo,hi


def mul_pos(a,b): return a[0]*b[0],a[1]*b[1]
def div_pos(a,b): return a[0]/b[1],a[1]/b[0]


def trig_base_radius(alpha,degree=TAYLOR_DEGREE):
    # Taylor at the exact-rational interval midpoint.  |sin'|,|cos'|<=1
    # charges the input-radius rho; the Taylor remainder is bounded by
    # A^(degree+1)/(degree+1)! on the whole positive alpha interval.
    lo,hi=alpha
    rho=(hi-lo)/2
    A=max(abs(lo),abs(hi))
    return rho + A**(degree+1)/factorial(degree+1)


def report():
    p=pi_interval()
    logs={q:log_interval(q,LOG_K[q]) for q in (2,3,5,7)}
    logs[4]=(2*logs[2][0],2*logs[2][1])
    sq={q:sqrt_interval(q) for q in (2,3,5,7)}
    sq[4]=(Fraction(2),Fraction(2))
    weights={q:div_pos(logs[VM_SOURCE[q]],sq[q]) for q in QS}

    power_err={}
    alpha_width={}
    for q in QS:
        alpha=mul_pos(p,logs[q])
        alpha_width[q]=alpha[1]-alpha[0]
        # 2*rad bounds the 2x2 rotation perturbation in Frobenius/operator norm.
        eta=2*trig_base_radius(alpha)
        # Exact telescoping power bound: ||R^r-R0^r|| <= r eta (1+eta)^(r-1).
        power_err[q]=RMAX*eta*(1+eta)**(RMAX-1)

    # Uniform error in the weighted prime sequence used by the off-diagonal source.
    seq_err=sum((weights[q][1]*power_err[q]+(weights[q][1]-weights[q][0])/2
                 for q in QS),Fraction(0))

    # Prime diagonal S_nn=(2-ell)cos(r alpha)+sin(r alpha)/(r*pi), r>=11.
    invpi=(1/p[1],1/p[0])
    diag_err=Fraction(0)
    for q in QS:
        llo,lhi=logs[q]
        lrad=(lhi-llo)/2
        eps=power_err[q]
        coeff=max(abs(2-llo),abs(2-lhi))
        inv_lo=invpi[0]/11
        inv_hi=invpi[1]/11
        inv_rad=(inv_hi-inv_lo)/2
        Serr=coeff*eps+lrad*(1+eps)+eps*inv_hi+(1+eps)*inv_rad
        Sabs=coeff+inv_hi
        wlo,whi=weights[q]
        wrad=(whi-wlo)/2
        diag_err += whi*Serr+wrad*Sabs

    # Conservative conversion for the M16001 7991-dimensional finite-high block:
    # allow TWO prime-sequence errors in any off-diagonal entry, then use
    # ||E||_2 <= N max_ij |E_ij|.  Diagonal uses diag_err directly.
    entry_err=max(2*seq_err,diag_err)
    matrix_err=7991*entry_err

    # Exact rational assertions; decimals below are display only.
    assert p[1]-p[0] < Fraction(3,10**45)
    assert max(alpha_width.values()) < Fraction(1,10**44)
    assert max(power_err.values()) < Fraction(8,10**41)
    assert seq_err < Fraction(14,10**41)       # 1.4e-40
    assert diag_err < Fraction(8,10**41)       # 8e-41
    assert entry_err < Fraction(28,10**41)     # 2.8e-40
    assert matrix_err < Fraction(23,10**36)    # 2.3e-35? see printed exact value
    # Stronger useful comparison to v13.357's 2e-13 source budget.
    assert matrix_err < Fraction(1,10**34)

    print('RMAX =',RMAX)
    print('pi width <',float(p[1]-p[0]))
    for q in QS:
        print('q',q,'alpha width <',float(alpha_width[q]),
              'r<=8000 rotation error <',float(power_err[q]),
              'weight width <',float(weights[q][1]-weights[q][0]))
    print('uniform weighted prime-sequence error <',float(seq_err))
    print('uniform prime-diagonal error <',float(diag_err))
    print('conservative prime entry radius <',float(entry_err))
    print('conservative 7991x7991 prime operator error <',float(matrix_err))
    print('PASS: exact-rational r<=8000 prime recurrence enclosure is negligible for M16001')


if __name__=='__main__':
    report()
