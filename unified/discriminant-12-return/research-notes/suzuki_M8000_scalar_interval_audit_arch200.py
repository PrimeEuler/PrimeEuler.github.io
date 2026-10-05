#!/usr/bin/env python3
"""Interval audit of the arch-200 scalar source-faithful producer through mode 8000.\n\nSame proof architecture as the successful M8000 scalar interval audit, but\nwith 200 archimedean coefficients. The v14.015 geometric tail formula gives\n|E_arch(n)|<4.24e-40/n^2, eight orders tighter than the arch-160 public cap.\n

Purpose
-------
The protected mu=1 Schur block has an even-sector pivot near 5.7e-30, so the
legacy 2e-13 whole-operator uncertainty is intentionally not used there.

This replay encloses the scalar ingredients of the exact source-faithful
operator directly:

  * Im psi(1/4+i n pi/4) from a symmetric interval-loggamma derivative,
    with an explicit O(h^2) polygamma bound;
  * Si(n pi), Ci(n pi) from rigorous power series for n<=192 and
    integration-by-parts asymptotics with explicit integral remainders above;
  * the prime terms by direct interval elementary arithmetic;
  * the 160-term arch diagonal by an exact-rational Bernoulli recurrence,
    widened by the v14.015 analytic truncation 3e-32/n^2;
  * the finite exponential z-correction, with a geometric omitted-tail bound;
  * the rank-one pole vector and 2/pi directly.

The script compares these exact intervals with the LDDD midpoint payload
actually used by the M8000 mu=1 Feshbach replay and reports uniform absolute
scalar representation errors.

No 4000x4000 interval matrix is formed.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb, factorial
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from suzuki_M8000_embedded_p4_ldd_capacity import parity_modes, TARGET_MAX
from suzuki_doubledouble_source_operator import QS
from suzuki_ldd_source_operator import (
    hp_parity_data_ld as hp_parity_data,
    ldd_to_mpf,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_scalar_interval_audit_arch200_result.json"

IVDPS=420
MPDPS=180
LOW_SERIES_MAX=192
LOW_SERIES_TERMS=1100
ASYM_TERMS=40
ARCH_TERMS=200
CORR_TERMS=50

# Exact Bernoulli numbers and exact-rational arch coefficients.
def bernoulli_numbers(n):
    B=[Fraction(1,1)]
    for m in range(1,n+1):
        s=sum(Fraction(comb(m+1,k),1)*B[k] for k in range(m))
        B.append(-s/Fraction(m+1,1))
    return B

_B=bernoulli_numbers(ARCH_TERMS+2)

def bernpoly_fraction(n,x=Fraction(3,4)):
    return sum(
        Fraction(comb(n,k),1)*_B[k]*x**(n-k)
        for k in range(n+1)
    )

_ARCH_COEFF=[
    bernpoly_fraction(r+1)*Fraction(2**r,factorial(r+1))
    for r in range(ARCH_TERMS+1)
]


def ivfrac(q: Fraction):
    return mp.iv.mpf(q.numerator)/q.denominator


def sym(rad):
    return mp.iv.mpf([-1,1])*rad


def upper_float(x):
    return float(x.b)


def abs_error_bound(interval_value, midpoint):
    pt=mp.iv.mpf(mp.nstr(midpoint,160))
    return upper_float(abs(interval_value-pt))


def digamma_im_iv(n: int):
    # Central derivative of log Gamma in the real direction.
    h=mp.iv.mpf("1e-120")
    a=mp.iv.mpf("0.25")
    y=mp.iv.mpf(n)*mp.iv.pi/4
    z=mp.iv.mpc(a,y)
    d=(mp.iv.loggamma(z+h)-mp.iv.loggamma(z-h))/(2*h)

    # Central-difference error <= h^2 sup|psi''|/6.
    # psi''(w)=-2 sum_{k>=0}(w+k)^-3 and Re w >= 1/4-h.
    a0=mp.iv.mpf("0.249999999999999999999999999999999999999")
    psi2_bound=2*(a0**-3 + 1/(2*a0**2))
    err=h*h*psi2_bound/6
    return d.imag + sym(err)


def si_ci_power_iv(n: int):
    x=mp.iv.mpf(n)*mp.iv.pi
    x2=x*x

    # Si
    si=x
    term=x
    k=0
    for _ in range(LOW_SERIES_TERMS):
        ratio=-x2*(2*k+1)/((2*k+3)**2*(2*k+2))
        term=term*ratio
        k+=1
        si+=term
    ratio=-x2*(2*k+1)/((2*k+3)**2*(2*k+2))
    nxt=term*ratio
    # At K=1100 and n<=192, the absolute ratios are <0.08 and decreasing.
    si+=sym(2*abs(nxt))

    # Ci = gamma + log x + sum_{k>=1} (-1)^k x^(2k)/(2k(2k)!).
    ci=mp.iv.euler+mp.iv.log(x)
    k=1
    term=-x2/4
    ci+=term
    for _ in range(LOW_SERIES_TERMS-1):
        ratio=-x2*(2*k)/((2*k+2)**2*(2*k+1))
        term=term*ratio
        k+=1
        ci+=term
    ratio=-x2*(2*k)/((2*k+2)**2*(2*k+1))
    nxt=term*ratio
    ci+=sym(2*abs(nxt))
    return si,ci


def si_ci_asym_iv(n: int):
    x=mp.iv.mpf(n)*mp.iv.pi
    eps=1 if n%2==0 else -1

    # J = int_x^inf sin(t)/t dt at x=n*pi:
    # eps * sum (-1)^k (2k)!/x^(2k+1) + remainder.
    js=mp.iv.mpf(0)
    gs=mp.iv.mpf(0)
    for k in range(ASYM_TERMS):
        js += ((-1)**k)*factorial(2*k)/x**(2*k+1)
        gs += ((-1)**k)*factorial(2*k+1)/x**(2*k+2)

    # Repeated integration by parts leaves coefficient (2K)! times an
    # integral of t^-(2K+1), whose absolute value is <=
    # (2K-1)!/x^(2K).
    rem=mp.iv.mpf(factorial(2*ASYM_TERMS-1))/x**(2*ASYM_TERMS)
    si=mp.iv.pi/2 - eps*js + sym(rem)
    ci=-eps*gs + sym(rem)
    return si,ci


_SICI_CACHE={}
def si_ci_iv(n: int):
    if n not in _SICI_CACHE:
        if n<=LOW_SERIES_MAX:
            _SICI_CACHE[n]=si_ci_power_iv(n)
        else:
            _SICI_CACHE[n]=si_ci_asym_iv(n)
    return _SICI_CACHE[n]


def arch_truncated_iv(n: int):
    k=mp.iv.mpf(n)*mp.iv.pi/2
    eps=-1 if n%2 else 1
    C=[mp.iv.mpf(0)]*(ARCH_TERMS+2)
    S=[mp.iv.mpf(0)]*(ARCH_TERMS+2)
    S[0]=(1-eps)/k
    for r in range(1,ARCH_TERMS+2):
        C[r]=-r*S[r-1]/k
        S[r]=-(mp.iv.mpf(2)**r)*eps/k+r*C[r-1]/k

    total=mp.iv.mpf(0)
    for r in range(ARCH_TERMS+1):
        total += ivfrac(_ARCH_COEFF[r])*(2*C[r]-C[r+1]+S[r]/k)
    return -total


def exact_scalar_intervals(n: int, sector: str):
    nn=mp.iv.mpf(n)
    k=nn*mp.iv.pi/2
    parity=1 if n%2==0 else -1

    # Prime constants.
    weights=(
        mp.iv.log(2)/mp.iv.sqrt(2),
        mp.iv.log(3)/mp.iv.sqrt(3),
        mp.iv.log(2)/2,
        mp.iv.log(5)/mp.iv.sqrt(5),
        mp.iv.log(7)/mp.iv.sqrt(7),
    )
    prime_sine=mp.iv.mpf(0)
    for q,w in zip(QS,weights):
        prime_sine += w*mp.iv.sin(nn*mp.iv.pi*mp.iv.log(q)/2)

    # Digamma imaginary part and finite exponential correction.
    psi_im=digamma_im_iv(n)
    corr=mp.iv.mpf(0)
    for j in range(CORR_TERMS):
        a=mp.iv.mpf(2*j)+mp.iv.mpf("0.5")
        corr += mp.iv.exp(-2*a)/(a*a+k*k)
    a0=mp.iv.mpf("100.5")
    corr_tail=(
        nn*mp.iv.pi*mp.iv.exp(-201)
        /(a0*a0)
        /(1-mp.iv.exp(-4))
    )
    z=2*prime_sine+psi_im-parity*nn*mp.iv.pi*corr
    z += sym(corr_tail)

    # Diagonal.
    si,ci=si_ci_iv(n)
    cusp=mp.iv.log(nn/4)-ci-si/(nn*mp.iv.pi)
    prime_diag=mp.iv.mpf(0)
    for q,w in zip(QS,weights):
        prime_diag -= w*(
            (2-mp.iv.log(q))*mp.iv.cos(nn*mp.iv.pi*mp.iv.log(q)/2)
            + mp.iv.sin(nn*mp.iv.pi*mp.iv.log(q)/2)/k
        )

    arch=arch_truncated_iv(n)
    # v14.015 analytic tail, deliberately rounded to the public 3e-32/n^2.
    arch += sym(mp.iv.mpf("3e-32")/(nn*nn))
    diag=cusp+prime_diag+arch

    half=mp.iv.mpf("0.5")
    eh=mp.iv.exp(half)
    emh=mp.iv.exp(-half)
    if sector=="even-v":
        g=(eh+emh)/2
    else:
        g=(eh-emh)/2
    pole=2*k*g/(k*k+mp.iv.mpf("0.25"))

    return z,diag,pole


def one_sector(sector: str):
    modes=parity_modes(sector,TARGET_MAX)
    data=hp_parity_data(
        modes,sector,dps=MPDPS,arch_terms=ARCH_TERMS,correction_terms=CORR_TERMS
    )

    max_z=(0.0,None)
    max_d=(0.0,None)
    max_p=(0.0,None)

    for i,n in enumerate(modes):
        z,d,p=exact_scalar_intervals(int(n),sector)
        zm=ldd_to_mpf(data.z_hi[i],data.z_lo[i])
        dm=ldd_to_mpf(data.diag_hi[i],data.diag_lo[i])
        pm=ldd_to_mpf(data.pole_hi[i],data.pole_lo[i])
        ez=abs_error_bound(z,zm)
        ed=abs_error_bound(d,dm)
        ep=abs_error_bound(p,pm)
        if ez>max_z[0]: max_z=(ez,int(n))
        if ed>max_d[0]: max_d=(ed,int(n))
        if ep>max_p[0]: max_p=(ep,int(n))
        if (i+1)%500==0:
            print(sector,"checked",i+1,"/",len(modes),
                  "max z",max_z,"max diag",max_d)

    # c=2/pi representation error.
    cm=ldd_to_mpf(data.c_hi,data.c_lo)
    ec=abs_error_bound(2/mp.iv.pi,cm)

    row={
        "sector":sector,
        "dimension":len(modes),
        "last_mode":int(modes[-1]),
        "max_z_abs_error":{"value":max_z[0],"mode":max_z[1]},
        "max_diag_abs_error":{"value":max_d[0],"mode":max_d[1]},
        "max_pole_abs_error":{"value":max_p[0],"mode":max_p[1]},
        "two_over_pi_abs_error":ec,
    }
    print("\n",sector,row)
    return row


def main():
    old=mp.iv.dps
    mp.iv.dps=IVDPS
    mp.mp.dps=MPDPS
    try:
        rows=[one_sector("even-v"),one_sector("odd-v")]
    finally:
        mp.iv.dps=old
    out={
        "iv_dps":IVDPS,
        "mp_dps":MPDPS,
        "low_series_max":LOW_SERIES_MAX,
        "low_series_terms":LOW_SERIES_TERMS,
        "asym_terms":ASYM_TERMS,
        "rows":rows,
        "theorem_scope":(
            "Reported errors enclose the exact scalar producer relative to the "
            "LDDD midpoint, including the public v14.015 arch truncation and "
            "the omitted exponential correction tail."
        ),
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)


if __name__=="__main__":
    main()
