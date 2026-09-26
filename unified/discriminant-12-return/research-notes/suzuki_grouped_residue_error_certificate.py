#!/usr/bin/env python3
"""Uniform grouped-residue error certificate over |delta| <= 0.02.

Exact grouped residue:
    G(delta) = C(delta)^* P4 C(delta),

numerical grouped residue:
    Ghat(delta) = C(delta)^* Phat4 C(delta),

where Phat4 is the orthogonal projector onto the residual-certified numerical
four-space of v13.824/v13.825.

For equal-rank orthogonal projectors,
    ||P4-Phat4|| = ||sin Theta||.

Hence
    -epsP C^*C <= G-Ghat <= epsP C^*C
and
    ||G-Ghat|| <= epsP ||C||^2.

This script certifies a uniform cap for
    C(delta)=B_T^{-1/2} F_TC(delta)
through a finite B_T-energy solve plus an infinite residual correction.

The frozen/certified projector-error inputs are:
    even-v: epsP < 0.332,
    odd-v : epsP < 0.361.

No individual residue, low-core zero count, kappa0, kappa1, RH, or GRH claim
is made here.
"""
from __future__ import annotations

import math
import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import (
    offdiag,
    pole_vector,
    z_source_faithful,
)
from suzuki_tail_P4_residual_basis_certificate import (
    BETA_CAP,
)


DELTA0 = 0.02
EXPLICIT_STOP = 2_000_000
DIRECT_STOP = {"even-v": 16001, "odd-v": 16000}
K_B = 16

EPS_SOURCE = 2.1e-13
U64 = 2.0**-53
ULD = float(np.finfo(np.longdouble).eps / 2)

PROJECTOR_ERROR_CAP = {
    "even-v": 0.332,
    "odd-v": 0.361,
}

FINITE_B_FLOOR = {
    "even-v": 0.0414,
    "odd-v": 0.2399,
}
X_NORM_CAP = {
    "even-v": 0.28,
    "odd-v": 0.24,
}
SOLVE_RESIDUAL_CAP = {
    "even-v": 1.0e-16,
    "odd-v": 1.5e-16,
}
TRIAL_ENERGY_NORM_CAP = {
    "even-v": 0.072,
    "odd-v": 0.201,
}
POINT_REMOTE_CAP = {
    "even-v": 0.00770,
    "odd-v": 0.01280,
}
FAR_REMOTE_CAP = {
    "even-v": 0.00460,
    "odd-v": 0.00100,
}
REMOTE_TOTAL_CAP = {
    "even-v": 0.0130,
    "odd-v": 0.0147,
}
COUPLING_SQUARED_CAP = {
    "even-v": 0.0256,
    "odd-v": 0.0416,
}
COUPLING_NORM_CAP = {
    "even-v": 0.160,
    "odd-v": 0.204,
}
GROUPED_RESIDUE_ERROR_CAP = {
    "even-v": 0.0086,
    "odd-v": 0.0152,
}


def gamma_n(n, u):
    nu=n*u
    if nu >= 1:
        raise RuntimeError("gamma_n invalid")
    return nu/(1-nu)


def layout(sector):
    if sector=="even-v":
        core=np.array([1,3],dtype=int)
        tail=np.arange(5,4000,2,dtype=int)
    else:
        core=np.array([2,4],dtype=int)
        tail=np.arange(6,4001,2,dtype=int)
    return core,tail


def smooth_bulk(modes):
    m=np.asarray(modes,dtype=float)
    B=-1.0/(m[:,None]+m[None,:])
    np.fill_diagonal(B,np.log(m/4.0)-1.0/(2.0*m))
    return B


def coupling_rows(sector, core, rows, delta):
    core=np.asarray(core,dtype=float)
    rows=np.asarray(rows,dtype=float)

    zc=z_source_faithful(core)
    zr=z_source_faithful(rows)

    n=rows[:,None]
    m=core[None,:]

    A=(2.0/math.pi)*(zr[:,None]*m-n*zc[None,:])/(n*n-m*m)

    pr,alpha=pole_vector(rows,sector)
    pc,_=pole_vector(core,sector)
    A+=alpha*pr[:,None]*pc[None,:]

    B=-1.0/(n+m)
    return A-delta*B


def rhs_residual_outward(A,B,Y):
    A=np.asarray(A,dtype=np.longdouble)
    B=np.asarray(B,dtype=np.longdouble)
    Y=np.asarray(Y,dtype=np.longdouble)

    AY=A@Y
    R=B-AY
    rp=np.sqrt(np.sum(R*R,dtype=np.longdouble))

    E=(
        np.longdouble(gamma_n(A.shape[1],ULD))
        *(np.abs(A)@np.abs(Y))
        +np.longdouble(ULD)/(1-np.longdouble(ULD))
        *(np.abs(B)+np.abs(AY))
    )
    ee=np.sqrt(np.sum(E*E,dtype=np.longdouble))
    return float(np.nextafter(rp+ee,np.longdouble(np.inf)))


def b_moments(tail,X):
    j=tail.astype(np.longdouble)
    W=X.astype(np.longdouble)
    out=[]
    for k in range(K_B):
        out.append(np.sum(((-j)**k)[:,None]*W,axis=0))
    return np.array(out)


def b_expanded_rows(ns,moments):
    nn=np.asarray(ns,dtype=np.longdouble)
    R=np.zeros((len(nn),2),dtype=np.longdouble)
    for k in range(K_B):
        R-=moments[k][None,:]/nn[:,None]**(k+1)
    return np.asarray(R,dtype=float)


def b_expansion_remainder_bound(tail,X,start):
    j=tail.astype(float)
    ratio=float(np.max(j))/float(start)
    if ratio >= 1:
        raise RuntimeError("invalid Hilbert expansion ratio")

    coeff=np.sum(
        np.abs(X)*(j[:,None]**K_B),
        axis=0,
    )/(1-ratio)

    p=2*K_B+2
    S=(
        start**(-p)
        +1.0/(2.0*(p-1)*start**(p-1))
    )
    cols=coeff*math.sqrt(S)
    return float(np.linalg.norm(cols))


def explicit_remote_residual(sector,core,tail,X,delta):
    start=int(tail[-1])+2
    stop=DIRECT_STOP[sector]

    G=np.zeros((2,2),dtype=float)

    for st in range(start,stop+1,2000):
        en=min(st+1998,stop)
        if (en-st)%2:
            en-=1
        if en<st:
            continue

        ns=np.arange(st,en+1,2,dtype=float)
        F=coupling_rows(sector,core,ns,delta)
        B=-1.0/(ns[:,None]+tail.astype(float)[None,:])
        R=F-B@X
        G+=R.T@R

    moments=b_moments(tail,X)
    expansion_remainder=b_expansion_remainder_bound(
        tail,X,stop+2
    )

    st=stop+2
    while st<=EXPLICIT_STOP:
        en=min(st+199998,EXPLICIT_STOP)
        if (en-st)%2:
            en-=1

        ns=np.arange(st,en+1,2,dtype=float)
        F=coupling_rows(sector,core,ns,delta)
        BX=b_expanded_rows(ns,moments)
        R=F-BX
        G+=R.T@R
        st=en+2

    point=math.sqrt(
        max(0.0,float(np.linalg.eigvalsh((G+G.T)/2)[-1]))
    )
    return point,expansion_remainder


def same_parity_sum_bound(N,p):
    return N**(-p)+1.0/(2.0*(p-1)*N**(p-1))


def far_coupling_frobenius(sector,core,N):
    zc=z_source_faithful(core)
    pc,alpha=pole_vector(core,sector)
    g=math.cosh(0.5) if sector=="even-v" else math.sinh(0.5)

    S2=same_parity_sum_bound(N,2)
    S4=same_parity_sum_bound(N,4)

    cols=[]
    for m,z,p in zip(core.astype(float),zc,pc):
        ratio=1.0/(1.0-(m/N)**2)
        a=(
            (2.0/math.pi)*ratio*abs(z)
            +abs(alpha)*(4.0*g/math.pi)*abs(p)
            +DELTA0
        )
        b=(16.0*m/math.pi)*ratio
        cols.append(
            a*math.sqrt(S2)+b*math.sqrt(S4)
        )

    return float(np.linalg.norm(cols))


def far_hilbert_times_X(tail,X,N):
    S2=same_parity_sum_bound(N,2)
    l1=np.sum(np.abs(X),axis=0)
    cols=l1*math.sqrt(S2)
    return float(np.linalg.norm(cols))


def certify_endpoint(sector,delta):
    core,tail=layout(sector)
    B=smooth_bulk(tail)
    F=coupling_rows(sector,core,tail,delta)

    L=np.linalg.cholesky(B)
    X=np.linalg.solve(L.T,np.linalg.solve(L,F))

    solve_resid=rhs_residual_outward(B,F,X)
    if solve_resid >= SOLVE_RESIDUAL_CAP[sector]:
        raise RuntimeError(("finite B solve residual cap",sector,delta,solve_resid))

    xnorm=float(np.linalg.norm(X,2))
    if xnorm >= X_NORM_CAP[sector]:
        raise RuntimeError(("X norm cap",sector,delta,xnorm))

    E=(X.T@B@X)
    E=(E+E.T)/2.0
    energy_norm=math.sqrt(
        max(0.0,float(np.linalg.eigvalsh(E)[-1]))
    )
    if energy_norm >= TRIAL_ENERGY_NORM_CAP[sector]:
        raise RuntimeError(("trial energy cap",sector,delta,energy_norm))

    point,exp_rem=explicit_remote_residual(
        sector,core,tail,X,delta
    )
    if point+exp_rem >= POINT_REMOTE_CAP[sector]:
        raise RuntimeError(("point remote cap",sector,delta,point,exp_rem))

    N=2_000_001 if sector=="even-v" else 2_000_002
    farF=far_coupling_frobenius(sector,core,N)
    farBX=far_hilbert_times_X(tail,X,N)
    far=farF+farBX
    if far >= FAR_REMOTE_CAP[sector]:
        raise RuntimeError(("far remote cap",sector,delta,far))

    remote_total=(
        POINT_REMOTE_CAP[sector]
        +FAR_REMOTE_CAP[sector]
        +EPS_SOURCE
    )
    if remote_total >= REMOTE_TOTAL_CAP[sector]:
        raise RuntimeError(("remote total cap",sector,delta,remote_total))

    # Full energy identity for a finite-support trial solve X:
    #
    # F^* B_T^{-1} F
    # = X^* B_FF X + X^* r_F + r_F^* X + r^* B_T^{-1} r.
    #
    # The exact full residual is bounded by the finite solve residual,
    # the remote residual, and the inherited source/operator reserve.
    total_residual=(
        REMOTE_TOTAL_CAP[sector]
        +SOLVE_RESIDUAL_CAP[sector]
        +EPS_SOURCE
    )

    c2=(
        TRIAL_ENERGY_NORM_CAP[sector]**2
        +2.0*X_NORM_CAP[sector]*(
            SOLVE_RESIDUAL_CAP[sector]+EPS_SOURCE
        )
        +(total_residual**2)/BETA_CAP[sector]
    )

    if c2 >= COUPLING_SQUARED_CAP[sector]:
        raise RuntimeError(("coupling squared cap",sector,delta,c2))

    if math.sqrt(c2) >= COUPLING_NORM_CAP[sector]:
        raise RuntimeError(("coupling norm cap",sector,delta,math.sqrt(c2)))

    return {
        "delta":delta,
        "solve_residual":solve_resid,
        "X_norm":xnorm,
        "trial_energy_norm":energy_norm,
        "point_remote":point,
        "expansion_remainder":exp_rem,
        "far_F":farF,
        "far_BX":farBX,
        "far_total":far,
        "c2_bound":c2,
        "c_bound":math.sqrt(c2),
    }


def certify_sector(sector):
    # Norm of an affine operator-valued map is convex, so the uniform
    # maximum over [-DELTA0,DELTA0] occurs at one of the two endpoints.
    left=certify_endpoint(sector,-DELTA0)
    right=certify_endpoint(sector,+DELTA0)

    c2=COUPLING_SQUARED_CAP[sector]
    epsP=PROJECTOR_ERROR_CAP[sector]
    residue_error=epsP*c2

    if residue_error >= GROUPED_RESIDUE_ERROR_CAP[sector]:
        raise RuntimeError(("grouped residue error cap",sector,residue_error))

    return {
        "sector":sector,
        "left":left,
        "right":right,
        "uniform_C2_cap":c2,
        "uniform_C_cap":COUPLING_NORM_CAP[sector],
        "projector_error_cap":epsP,
        "grouped_residue_error":residue_error,
        "grouped_residue_error_cap":GROUPED_RESIDUE_ERROR_CAP[sector],
    }


def main():
    rows=[
        certify_sector("even-v"),
        certify_sector("odd-v"),
    ]

    for row in rows:
        print("\nsector =",row["sector"])
        for side in ("left","right"):
            print(side,row[side])
        print("uniform ||C||^2 cap =",row["uniform_C2_cap"])
        print("uniform ||C|| cap =",row["uniform_C_cap"])
        print("projector error cap =",row["projector_error_cap"])
        print("computed grouped residue error =",row["grouped_residue_error"])
        print("public grouped residue error cap =",row["grouped_residue_error_cap"])

    print("\nPASS grouped-residue projector-error certificate")
    print(
        "For all |delta|<=0.02, "
        "||C^*(P4-Phat4)C|| is below the reported sector cap."
    )
    print(
        "The stronger Loewner enclosure "
        "-epsP C^*C <= G-Ghat <= epsP C^*C also holds."
    )


if __name__=="__main__":
    main()
