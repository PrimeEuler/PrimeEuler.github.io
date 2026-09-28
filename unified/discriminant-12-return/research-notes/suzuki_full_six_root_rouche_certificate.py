#!/usr/bin/env python3
"""Candidate final six-root Riesz/Rouche certificate for Lane A.

Goal
----
Certify, sector by sector, that the full infinite generalized pencil
    F(z)=A-z B_sm
has exactly six algebraic roots in |z|<0.02.

Architecture
------------
1. Keep the first 12 parity coordinates.
2. Eliminate the finite positive buffer through M=12001/12002 by the
   source-faithful displacement-rank-two LDL plus exact pole
   Sherman-Morrison update.
3. Evaluate the resulting 12x12 analytic Schur matrix on 32 roots of unity
   on |z|=0.02.
4. Use analyticity in |z|<0.05 and a Cauchy/Fourier alias bound to obtain a
   uniform lower bound for sigma_min on the entire contour, not only the
   sample nodes.
5. Reconstruct the dressed finite-to-remote coupling on the same 32 nodes.
   Bound the explicit remote rows through 20000 by Fourier coefficients and
   the remaining far tail by the already-audited inverse-power envelope.
6. Use the remote coercivity floor Re F_RR(z) >= gamma I to bound the exact
   infinite Schur correction.
7. If
       ||Delta S_remote|| < inf_{|z|=.02} sigma_min(S_M(z)),
   the matrix Rouche homotopy preserves the determinant winding.
8. Compute the finite winding from the certified nonvanishing Fourier
   reconstruction.  The target is winding 6.

This script is intentionally fail-closed and carries widened public caps.
It does not claim reality of the six roots; it certifies algebraic
multiplicity in the complex disk.  A separate Krein/reality gate is needed
if all six roots are to be certified real.
"""
from __future__ import annotations

import gc
import math
import mpmath as mp
import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import (
    cusp_diag,
    prime_diag,
    arch_diag,
    z_source_faithful,
    pole_vector,
)

RADIUS = 0.02
OUTER_RADIUS = 0.05
NSAMP = 32
DENSE_GRID = 65536
EXPLICIT_STOP = 20000
MODEL_RESERVE = 1.0e-7
REMOTE_CROSS_CAP = 20.0
Z_FAR_CAP = 8.0

CUT = {
    "even-v": 12001,
    "odd-v": 12002,
}
REMOTE_START = {
    "even-v": 12003,
    "odd-v": 12004,
}

# Widened public caps.  These are intended to leave visible room beyond
# the source-thread midpoint values.
FINITE_CONTOUR_FLOOR = {
    "even-v": 0.00300,
    "odd-v": 0.00175,
}
EXPLICIT_REMOTE_NORM_CAP = {
    "even-v": 0.053,
    "odd-v": 0.043,
}
FAR_REMOTE_NORM_CAP = {
    "even-v": 0.076,
    "odd-v": 0.064,
}
REMOTE_GAMMA_FLOOR = {
    "even-v": 4.50,
    "odd-v": 4.50,
}
REMOTE_SCHUR_CAP = {
    "even-v": 0.00195,
    "odd-v": 0.00135,
}
ROUCHE_MARGIN_FLOOR = {
    "even-v": 0.00100,
    "odd-v": 0.00035,
}

# Analytic outer-disk majorants used only to bound 32-point Fourier alias.
BUFFER_B_FLOOR = {
    "even-v": math.log(25.0/4.0)-math.pi/2.0,
    "odd-v": math.log(26.0/4.0)-math.pi/2.0,
}
BUFFER_ENDPOINT_FLOOR = {
    "even-v": 1.0e-6,
    "odd-v": 1.0e-6,
}
CORE_BUFFER_COUPLING_CAP = {
    "even-v": 1.20,
    "odd-v": 0.90,
}
SCHUR_OUTER_CAP = 250.0
GRAPH_OUTER_CAP = 150.0
Y_OUTER_CAP = REMOTE_CROSS_CAP*GRAPH_OUTER_CAP

def modes_for(sector,stop):
    return np.arange(1 if sector=="even-v" else 2,stop+1,2,dtype=int)

def base_diag(ns):
    ns=np.asarray(ns,dtype=int)
    return (
        cusp_diag(ns)
        +prime_diag(ns)
        +np.array([arch_diag(int(n)) for n in ns])
    )

def offdiag_complex(m1,m2,z1,z2):
    m=np.asarray(m1,dtype=float)[:,None]
    n=np.asarray(m2,dtype=float)[None,:]
    den=m*m-n*n
    out=np.zeros(den.shape,dtype=np.complex128)
    mask=den!=0.0
    num=z1[:,None]*n-m*z2[None,:]
    out[mask]=(2.0/math.pi)*num[mask]/den[mask]
    return out

def structured_ldl_complex(modes,z,diag):
    modes=np.asarray(modes,dtype=float)
    x=modes*modes
    u=np.asarray(z,dtype=np.complex128).copy()
    v=modes.astype(np.complex128).copy()
    d=np.asarray(diag,dtype=np.complex128).copy()
    n=len(modes)
    L=np.eye(n,dtype=np.complex128)
    D=np.empty(n,dtype=np.complex128)
    for k in range(n):
        piv=d[k]
        if abs(piv)<1.0e-12:
            raise RuntimeError(("small pole-free pivot",k,piv))
        D[k]=piv
        if k+1<n:
            b=(
                (2.0/math.pi)
                *(u[k]*v[k+1:]-v[k]*u[k+1:])
                /(x[k]-x[k+1:])
            )
            ell=b/piv
            L[k+1:,k]=ell
            d[k+1:]-=b*ell
            u[k+1:]-=ell*u[k]
            v[k+1:]-=ell*v[k]
    return L,D

def ldl_solve_complex(L,D,rhs):
    rhs=np.asarray(rhs,dtype=np.complex128)
    one=rhs.ndim==1
    if one:
        rhs=rhs[:,None]
    y=rhs.copy()
    n=L.shape[0]
    for i in range(n):
        if i:
            y[i]-=L[i,:i]@y[:i]
    y/=D[:,None]
    x=y.copy()
    for i in range(n-1,-1,-1):
        if i+1<n:
            x[i]-=L[i+1:,i]@x[i+1:]
    return x[:,0] if one else x

def finite_graph(sector,zparam):
    modes=modes_for(sector,CUT[sector])
    z0=z_source_faithful(modes)
    d0=base_diag(modes)
    nc=12
    core,buf=modes[:nc],modes[nc:]
    z=z0-zparam*math.pi/2.0
    d=d0-zparam*(np.log(modes/4.0)-1.0/(2.0*modes))

    C0=offdiag_complex(core,core,z[:nc],z[:nc])
    np.fill_diagonal(C0,d[:nc])
    R0=offdiag_complex(core,buf,z[:nc],z[nc:])

    L,D=structured_ldl_complex(buf,z[nc:],d[nc:])

    p,alpha=pole_vector(modes,sector)
    pc,pf=p[:nc],p[nc:]
    C=C0+alpha*np.outer(pc,pc)
    R=R0+alpha*np.outer(pc,pf)

    W0=ldl_solve_complex(L,D,R.T)
    yp=ldl_solve_complex(L,D,pf)
    den=1.0+alpha*(pf@yp)
    if abs(den)<0.5:
        raise RuntimeError(("small pole denominator",sector,zparam,den))

    X=W0-alpha*np.outer(yp,pf@W0)/den
    S=C-R@X
    graph=np.vstack([np.eye(nc,dtype=np.complex128),-X])

    del L,D,W0,yp
    gc.collect()

    return modes,z,p,alpha,S,graph

def direct_remote_rows(sector,zparam,modes,zfinite,pfinite,alpha,graph):
    ns=np.arange(
        REMOTE_START[sector],
        EXPLICIT_STOP+1,
        2,
        dtype=int,
    )
    zn=z_source_faithful(ns)-zparam*math.pi/2.0
    A0=offdiag_complex(ns,modes,zn,zfinite)
    pn,_=pole_vector(ns,sector)
    return A0@graph+alpha*pn[:,None]*(pfinite@graph)[None,:]

def dft_coeff(samples):
    return np.fft.fft(samples,axis=0)/samples.shape[0]

def analytic_alias_cap(M):
    q=RADIUS/OUTER_RADIUS
    return 2.0*M*q**NSAMP/(1.0-q)

def fourier_operator_sup(coeff,alias):
    total=0.0
    for k in range(coeff.shape[0]):
        total+=float(np.linalg.svd(coeff[k],compute_uv=False)[0])
    return total+alias

def fourier_matrix_dense(coeff):
    # Evaluate the degree-(NSAMP-1) analytic Fourier polynomial.
    mins=math.inf
    dets=[]
    deriv=sum(
        k*float(np.linalg.norm(coeff[k],2))
        for k in range(1,coeff.shape[0])
    )
    for start in range(0,DENSE_GRID,2048):
        idx=np.arange(start,min(start+2048,DENSE_GRID))
        th=2.0*math.pi*idx/DENSE_GRID
        E=np.exp(1j*np.outer(th,np.arange(coeff.shape[0])))
        vals=np.einsum("tk,kij->tij",E,coeff,optimize=True)
        for M in vals:
            sv=float(np.linalg.svd(M,compute_uv=False)[-1])
            if sv<mins:
                mins=sv
        del vals,E
    angular_halfstep=math.pi/DENSE_GRID
    return mins-deriv*angular_halfstep,deriv

def winding_from_coeff(coeff):
    n=8192
    th=2.0*math.pi*np.arange(n)/n
    E=np.exp(1j*np.outer(th,np.arange(coeff.shape[0])))
    vals=np.einsum("tk,kij->tij",E,coeff,optimize=True)
    det=np.linalg.det(vals)
    phase=np.unwrap(np.angle(np.r_[det,det[0]]))
    increments=np.diff(phase)
    if np.max(np.abs(increments))>=0.25:
        raise RuntimeError(("phase mesh too coarse",np.max(np.abs(increments))))
    w=(phase[-1]-phase[0])/(2.0*math.pi)
    wi=int(round(w))
    if abs(w-wi)>=1.0e-8:
        raise RuntimeError(("noninteger winding replay",w))
    return wi,float(np.max(np.abs(increments)))

def far_sums(N,power):
    return N**(-power)+1.0/(2.0*(power-1)*N**(power-1))

def uniform_far_bound(sector,modes,Wcoeff,leadcoeff):
    N=EXPLICIT_STOP+1
    if sector=="odd-v" and N%2:
        N+=1
    if sector=="even-v" and N%2==0:
        N+=1

    qmax=float(np.max(modes))/float(N)
    if qmax>=1:
        raise RuntimeError("far expansion invalid")

    # Uniform entrywise majorant of the Fourier interpolant.
    Wabs=np.sum(np.abs(Wcoeff),axis=0)

    Bvec=(
        (2.0/math.pi)
        *Z_FAR_CAP/(1.0-qmax*qmax)
        *np.sum(np.abs(modes[:,None])*Wabs,axis=0)
    )

    # zfinite itself is bounded by |z0|+R*pi/2 on the contour.
    zabs=np.abs(z_source_faithful(modes))+RADIUS*math.pi/2.0
    p,alpha=pole_vector(modes,sector)
    g=math.cosh(0.5) if sector=="even-v" else math.sinh(0.5)
    pWabs=np.abs(p)@Wabs

    Cvec=(
        (2.0/math.pi)/(1.0-qmax*qmax)
        *np.sum(np.abs((modes.astype(float)**2*zabs)[:,None])*Wabs,axis=0)
        +abs(alpha)*(4.0*g/math.pi**3)*pWabs
    )

    leadcap=sum(
        float(np.linalg.norm(leadcoeff[k]))
        for k in range(leadcoeff.shape[0])
    )

    # Fourier alias of W contributes at most common-cross-cap * alias_W.
    aliasW=analytic_alias_cap(GRAPH_OUTER_CAP)
    leadcap+=REMOTE_CROSS_CAP*aliasW

    root=(
        leadcap*math.sqrt(far_sums(N,2))
        +float(np.linalg.norm(Bvec))*math.sqrt(far_sums(N,4))
        +float(np.linalg.norm(Cvec))*math.sqrt(far_sums(N,6))
        +REMOTE_CROSS_CAP*aliasW
    )
    return root

def tail_floor_interval(sector):
    iv=mp.iv
    iv.dps=80
    N=iv.mpf(REMOTE_START[sector])
    pi=iv.pi
    s2=N**-2+1/(2*N)
    c=2/pi**3+6/pi**4
    a=2*c/pi
    cd=2/pi**2+2/pi**3+2/pi**4+6/pi**5
    cusp=(
        2/pi**2*s2
        +2*a*iv.sqrt(pi**2/12*(N**-6+1/(10*N**5)))
        +cd*iv.sqrt(N**-4+1/(6*N**3))
    )
    q=2/pi
    z3=iv.mpf(str(mp.zeta(3)))
    m4=z3*q**3/(4*(1-q)**3)
    cr=iv.mpf(19)/12+4*m4
    arch=4*cr/pi**2*s2

    out=iv.mpf("0.98")*(iv.log(N/4)-pi/2)-iv.mpf("2.05")-cusp-arch
    if sector=="odd-v":
        sh=(iv.exp(iv.mpf(".5"))-iv.exp(-iv.mpf(".5")))/2
        out-=32*sh**2/pi**2*s2
    return out

def one_sector(sector):
    theta=2.0*math.pi*np.arange(NSAMP)/NSAMP
    Ssamples=np.empty((NSAMP,12,12),dtype=np.complex128)

    modes0=modes_for(sector,CUT[sector])
    nremote=len(np.arange(REMOTE_START[sector],EXPLICIT_STOP+1,2))
    Ysamples=np.empty((NSAMP,nremote,12),dtype=np.complex128)
    Wsamples=np.empty((NSAMP,len(modes0),12),dtype=np.complex128)
    leadsamples=np.empty((NSAMP,12),dtype=np.complex128)

    for j,th in enumerate(theta):
        zparam=RADIUS*np.exp(1j*th)
        modes,zfinite,pfinite,alpha,S,W=finite_graph(sector,zparam)
        Ssamples[j]=S
        Wsamples[j]=W

        Y=direct_remote_rows(
            sector,zparam,modes,zfinite,pfinite,alpha,W
        )
        Ysamples[j]=Y

        g=math.cosh(0.5) if sector=="even-v" else math.sinh(0.5)
        leadsamples[j]=(
            -(2.0/math.pi)*(zfinite@W)
            +alpha*(4.0*g/math.pi)*(pfinite@W)
        )

    Scoef=dft_coeff(Ssamples)
    Ycoef=dft_coeff(Ysamples)
    Wcoef=dft_coeff(Wsamples)
    leadcoef=dft_coeff(leadsamples)

    salias=analytic_alias_cap(SCHUR_OUTER_CAP)+MODEL_RESERVE
    minpoly,deriv=fourier_matrix_dense(Scoef)
    finite_floor=minpoly-salias
    if finite_floor<=FINITE_CONTOUR_FLOOR[sector]:
        raise RuntimeError((
            "finite contour floor",
            sector,finite_floor,FINITE_CONTOUR_FLOOR[sector]
        ))

    winding,phase_step=winding_from_coeff(Scoef)
    if winding!=6:
        raise RuntimeError(("finite winding",sector,winding))

    yalias=analytic_alias_cap(Y_OUTER_CAP)+MODEL_RESERVE
    yexplicit=fourier_operator_sup(Ycoef,yalias)
    if yexplicit>=EXPLICIT_REMOTE_NORM_CAP[sector]:
        raise RuntimeError((
            "explicit remote norm cap",
            sector,yexplicit,EXPLICIT_REMOTE_NORM_CAP[sector]
        ))

    far=uniform_far_bound(sector,modes0,Wcoef,leadcoef)+MODEL_RESERVE
    if far>=FAR_REMOTE_NORM_CAP[sector]:
        raise RuntimeError((
            "far remote norm cap",
            sector,far,FAR_REMOTE_NORM_CAP[sector]
        ))

    giv=tail_floor_interval(sector)
    if not giv>mp.iv.mpf(str(REMOTE_GAMMA_FLOOR[sector])):
        raise RuntimeError(("remote gamma",sector,giv))

    gramcap=(
        EXPLICIT_REMOTE_NORM_CAP[sector]**2
        +FAR_REMOTE_NORM_CAP[sector]**2
    )
    correction=gramcap/REMOTE_GAMMA_FLOOR[sector]+MODEL_RESERVE
    if correction>=REMOTE_SCHUR_CAP[sector]:
        raise RuntimeError((
            "remote Schur cap",
            sector,correction,REMOTE_SCHUR_CAP[sector]
        ))

    margin=FINITE_CONTOUR_FLOOR[sector]-REMOTE_SCHUR_CAP[sector]
    if margin<=ROUCHE_MARGIN_FLOOR[sector]:
        raise RuntimeError(("Rouche margin",sector,margin))

    return dict(
        sector=sector,
        finite_floor=finite_floor,
        finite_public_floor=FINITE_CONTOUR_FLOOR[sector],
        finite_winding=winding,
        max_phase_step=phase_step,
        explicit_remote_norm=yexplicit,
        far_remote_norm=far,
        remote_gamma_interval=giv,
        remote_schur_cap=REMOTE_SCHUR_CAP[sector],
        rouche_margin=margin,
        fourier_alias=salias,
        fourier_derivative=deriv,
    )

def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    for row in rows:
        print("\n",row["sector"])
        for k,v in row.items():
            if k!="sector":
                print(k,"=",v)

    print("\nTHEOREM: winding det F(z) on |z|=0.02 is 6 in both parity sectors.")
    print("Hence each full infinite parity pencil has exactly six algebraic roots")
    print("in the complex disk |z|<0.02, counted with algebraic multiplicity.")
    print("Guardrail: this certificate alone does not prove that all six are real.")

if __name__=="__main__":
    main()
