#!/usr/bin/env python3
"""Long-double double-double (LDDD) source-faithful operator engine.

On the audited x86 CI runner np.longdouble has a 64-bit significand.  A
two-component expansion in that arithmetic supplies roughly 38 decimal digits,
enough to move the absolute arithmetic floor well below the 1e-30 even-sector
capacity scalar while retaining the vectorized displacement-rank matvec.

This module mirrors suzuki_doubledouble_source_operator.py but stores each
component as np.longdouble and uses Dekker splitting with 2^32+1.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

import mpmath as mp
import numpy as np

from suzuki_doubledouble_source_operator import (
    QS,
    arch_coefficients,
    arch_diag_series,
)

LD=np.longdouble
SPLIT_LD=LD(4294967297.0)  # 2^32+1 for a 64-bit significand.


def ld_string(x):
    return np.format_float_scientific(
        LD(x), precision=40, unique=False, trim="k"
    )


def split_mpf_ld(x):
    hi=LD(mp.nstr(x,100))
    lo_mp=x-mp.mpf(ld_string(hi))
    lo=LD(mp.nstr(lo_mp,100))
    return hi,lo


def ldd_to_mpf(hi,lo):
    return mp.mpf(ld_string(hi))+mp.mpf(ld_string(lo))


def two_sum(a,b):
    a=np.asarray(a,dtype=LD)
    b=np.asarray(b,dtype=LD)
    s=a+b
    bb=s-a
    e=(a-(s-bb))+(b-bb)
    return s,e


def two_prod(a,b):
    a=np.asarray(a,dtype=LD)
    b=np.asarray(b,dtype=LD)
    p=a*b
    ca=SPLIT_LD*a
    ah=ca-(ca-a)
    al=a-ah
    cb=SPLIT_LD*b
    bh=cb-(cb-b)
    bl=b-bh
    e=((ah*bh-p)+ah*bl+al*bh)+al*bl
    return p,e


def add(ah,al,bh,bl):
    s,e=two_sum(ah,bh)
    t=np.asarray(al,dtype=LD)+np.asarray(bl,dtype=LD)+e
    return two_sum(s,t)


def sub(ah,al,bh,bl):
    return add(ah,al,-np.asarray(bh,dtype=LD),-np.asarray(bl,dtype=LD))


def mul_d(ah,al,b):
    p,e=two_prod(ah,b)
    e=e+np.asarray(al,dtype=LD)*np.asarray(b,dtype=LD)
    return two_sum(p,e)


def mul(ah,al,bh,bl):
    p,e=two_prod(ah,bh)
    ah=np.asarray(ah,dtype=LD); al=np.asarray(al,dtype=LD)
    bh=np.asarray(bh,dtype=LD); bl=np.asarray(bl,dtype=LD)
    e=e+ah*bl+al*bh+al*bl
    return two_sum(p,e)


def div_d(ah,al,b):
    b=np.asarray(b,dtype=LD)
    q1=np.asarray(ah,dtype=LD)/b
    ph,pl=two_prod(q1,b)
    rh,rl=sub(ah,al,ph,pl)
    q2=(rh+rl)/b
    return add(q1,LD(0),q2,LD(0))


@dataclass
class LDDParityData:
    modes: np.ndarray
    z_hi: np.ndarray
    z_lo: np.ndarray
    diag_hi: np.ndarray
    diag_lo: np.ndarray
    pole_hi: np.ndarray
    pole_lo: np.ndarray
    source_hi: np.ndarray
    source_lo: np.ndarray
    c_hi: np.longdouble
    c_lo: np.longdouble
    alpha: np.longdouble


def hp_parity_data_ld(
    modes,
    sector: str,
    dps: int=180,
    arch_terms: int=160,
    correction_terms: int=50,
):
    modes=np.asarray(modes,dtype=int)
    if np.finfo(np.longdouble).nmant < 63:
        raise RuntimeError(
            ("longdouble significand too small",np.finfo(np.longdouble))
        )

    with mp.workdps(dps):
        ws=(
            mp.log(2)/mp.sqrt(2),
            mp.log(3)/mp.sqrt(3),
            mp.log(2)/2,
            mp.log(5)/mp.sqrt(5),
            mp.log(7)/mp.sqrt(7),
        )
        coeffs=arch_coefficients(arch_terms)
        c_hi,c_lo=split_mpf_ld(2/mp.pi)

        z_hi=np.empty(len(modes),dtype=LD)
        z_lo=np.empty(len(modes),dtype=LD)
        d_hi=np.empty(len(modes),dtype=LD)
        d_lo=np.empty(len(modes),dtype=LD)
        p_hi=np.empty(len(modes),dtype=LD)
        p_lo=np.empty(len(modes),dtype=LD)
        f_hi=np.empty(len(modes),dtype=LD)
        f_lo=np.empty(len(modes),dtype=LD)

        for i,nn in enumerate(modes):
            n=mp.mpf(int(nn))
            k=n*mp.pi/2
            parity=mp.mpf(1 if int(nn)%2==0 else -1)

            prime_sine=mp.fsum(
                w*mp.sin(n*mp.pi*mp.log(q)/2)
                for q,w in zip(QS,ws)
            )
            corr=mp.fsum(
                mp.e**(-2*(2*j+mp.mpf("0.5")))/
                ((2*j+mp.mpf("0.5"))**2+k*k)
                for j in range(correction_terms)
            )
            z=(
                2*prime_sine
                +mp.im(mp.digamma(mp.mpf("0.25")+1j*n*mp.pi/4))
                -parity*n*mp.pi*corr
            )

            cusp=(
                mp.log(n/4)
                -mp.ci(n*mp.pi)
                -mp.si(n*mp.pi)/(n*mp.pi)
            )
            prime_diag=-mp.fsum(
                w*((2-mp.log(q))*mp.cos(n*mp.pi*mp.log(q)/2)
                +mp.sin(n*mp.pi*mp.log(q)/2)/k)
                for q,w in zip(QS,ws)
            )
            arch=arch_diag_series(int(nn),coeffs)
            diag=cusp+prime_diag+arch

            if sector=="even-v":
                pole=2*k*mp.cosh(mp.mpf("0.5"))/(k*k+mp.mpf("0.25"))
                alpha=LD(2)
            elif sector=="odd-v":
                pole=2*k*mp.sinh(mp.mpf("0.5"))/(k*k+mp.mpf("0.25"))
                alpha=LD(-2)
            else:
                raise ValueError(sector)

            sign=mp.mpf(-1 if int(nn)%2 else 1)
            source=k*(mp.e**(-1)-sign*mp.e)/(1+k*k)

            z_hi[i],z_lo[i]=split_mpf_ld(z)
            d_hi[i],d_lo[i]=split_mpf_ld(diag)
            p_hi[i],p_lo[i]=split_mpf_ld(pole)
            f_hi[i],f_lo[i]=split_mpf_ld(source)

        return LDDParityData(
            modes=modes.copy(),
            z_hi=z_hi,z_lo=z_lo,
            diag_hi=d_hi,diag_lo=d_lo,
            pole_hi=p_hi,pole_lo=p_lo,
            source_hi=f_hi,source_lo=f_lo,
            c_hi=c_hi,c_lo=c_lo,
            alpha=alpha,
        )


def column(data:LDDParityData,j:int):
    modes=data.modes.astype(LD)
    n=LD(data.modes[j])

    t1h,t1l=mul_d(data.z_hi,data.z_lo,n)
    t2h,t2l=mul_d(data.z_hi[j],data.z_lo[j],modes)
    nh,nl=sub(t1h,t1l,t2h,t2l)

    den=modes*modes-n*n
    safe=den.copy()
    safe[j]=LD(1)
    qh,ql=div_d(nh,nl,safe)
    ah,al=mul(data.c_hi,data.c_lo,qh,ql)

    ph,pl=mul(
        data.pole_hi,data.pole_lo,
        data.pole_hi[j],data.pole_lo[j],
    )
    ph,pl=mul_d(ph,pl,data.alpha)
    ah,al=add(ah,al,ph,pl)

    p2h,p2l=mul(
        data.pole_hi[j],data.pole_lo[j],
        data.pole_hi[j],data.pole_lo[j],
    )
    p2h,p2l=mul_d(p2h,p2l,data.alpha)
    dh,dl=add(data.diag_hi[j],data.diag_lo[j],p2h,p2l)
    ah[j]=dh; al[j]=dl
    return ah,al


def matvec(data:LDDParityData,X_hi,X_lo=None):
    X_hi=np.asarray(X_hi,dtype=LD)
    one=X_hi.ndim==1
    if one:
        X_hi=X_hi[:,None]
    if X_lo is None:
        X_lo=np.zeros_like(X_hi,dtype=LD)
    else:
        X_lo=np.asarray(X_lo,dtype=LD)
        if X_lo.ndim==1:
            X_lo=X_lo[:,None]

    n,r=X_hi.shape
    Yh=np.zeros((n,r),dtype=LD)
    Yl=np.zeros((n,r),dtype=LD)
    for j in range(n):
        ah,al=column(data,j)
        ph,pl=mul(
            ah[:,None],al[:,None],
            X_hi[j,:][None,:],X_lo[j,:][None,:],
        )
        Yh,Yl=add(Yh,Yl,ph,pl)
    return (Yh[:,0],Yl[:,0]) if one else (Yh,Yl)


def dot_columns(X_hi,X_lo,Y_hi,Y_lo):
    X_hi=np.asarray(X_hi,dtype=LD)
    Y_hi=np.asarray(Y_hi,dtype=LD)
    if X_hi.ndim==1: X_hi=X_hi[:,None]
    if Y_hi.ndim==1: Y_hi=Y_hi[:,None]
    if X_lo is None: X_lo=np.zeros_like(X_hi,dtype=LD)
    else: X_lo=np.asarray(X_lo,dtype=LD)
    if Y_lo is None: Y_lo=np.zeros_like(Y_hi,dtype=LD)
    else: Y_lo=np.asarray(Y_lo,dtype=LD)

    rx=X_hi.shape[1]; ry=Y_hi.shape[1]
    H=np.zeros((rx,ry),dtype=LD)
    L=np.zeros((rx,ry),dtype=LD)
    for i in range(X_hi.shape[0]):
        for a in range(rx):
            ph,pl=mul(
                X_hi[i,a],X_lo[i,a],
                Y_hi[i,:],Y_lo[i,:],
            )
            H[a,:],L[a,:]=add(H[a,:],L[a,:],ph,pl)
    return H,L


def norm2(hi,lo):
    hi=np.asarray(hi,dtype=LD).ravel()
    lo=np.asarray(lo,dtype=LD).ravel()
    sh=LD(0); sl=LD(0)
    for i in range(len(hi)):
        ph,pl=mul(hi[i],lo[i],hi[i],lo[i])
        sh,sl=add(sh,sl,ph,pl)
    return float(np.sqrt(sh+sl,dtype=LD))
