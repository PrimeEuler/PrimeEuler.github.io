#!/usr/bin/env python3
"""Fresh rho=0.10 M3999 normalized remote residual-Gram replay.

Uses the frozen exact-dyadic positive six-planes from
suzuki_endpoint_M3999_frozen_six_direction_inputs.py and reconstructs the
source-faithful endpoint finite solve from
suzuki_endpoint_M3999_midpoint_effective_core.py.

For each parity:
  * W = [Q ; -F_FF^{-1} F_FC Q] is the dressed finite six-plane;
  * residual rows to the remote coordinate tail are accumulated directly from
    the first remote mode through 16001/16000;
  * an eight-level inverse-power expansion is used from there through 2,000,000;
  * H = L0^{-1} G L0^{-T} is the normalized residual Gram;
  * a coarse inverse-power envelope beyond two million is also reported.

The far envelope uses the deliberately coarse remote generator bound |Z_n|<=8.
It is a midpoint/certification-target envelope until the transcendental
bound and floating-point accumulation are replayed outward.

No infinite endpoint inertia theorem is promoted by this script.
"""
from __future__ import annotations

import math
import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import (
    RHO,
    endpoint_data,
    offdiag,
    pole_vector,
    structured_ldl_solve,
    z_source_faithful,
)
from suzuki_endpoint_M3999_frozen_six_direction_inputs import (
    EVEN_Q_HEX,
    EVEN_L0_HEX,
    ODD_Q_HEX,
    ODD_L0_HEX,
    floats,
)


PI = math.pi
KEXP = 8
EXPLICIT_STOP = 2_000_000
Z_FAR_BOUND = 8.0


def finite_payload(sector):
    if sector == "even-v":
        core=np.arange(5,24,2,dtype=int)
        buffer_=np.arange(25,4000,2,dtype=int)
        Q=floats(EVEN_Q_HEX)
        L0=floats(EVEN_L0_HEX)
    elif sector == "odd-v":
        core=np.arange(6,25,2,dtype=int)
        buffer_=np.arange(26,4001,2,dtype=int)
        Q=floats(ODD_Q_HEX)
        L0=floats(ODD_L0_HEX)
    else:
        raise ValueError(sector)

    modes=np.concatenate([core,buffer_])
    z,diag=endpoint_data(modes)
    nc=10
    zc,zf=z[:nc],z[nc:]
    dc,df=diag[:nc],diag[nc:]

    R0=offdiag(buffer_,core,zf,zc)
    p,alpha=pole_vector(modes,sector)
    pc,pf=p[:nc],p[nc:]
    RFC=R0+alpha*np.outer(pf,pc)

    rhs=np.column_stack([RFC,pf])
    X0,piv=structured_ldl_solve(
        df,
        zf,
        buffer_.astype(float),
        buffer_.astype(float)**2,
        rhs,
    )
    X0B,U=X0[:,:10],X0[:,10]
    den=1.0+alpha*(pf@U)
    X=X0B-alpha*np.outer(U,pf@X0B)/den

    W=np.vstack([Q,-X@Q])
    pW=p@W
    return {
        "sector":sector,
        "modes":modes.astype(float),
        "z":z.astype(float),
        "p":p.astype(float),
        "alpha":alpha,
        "Q":Q,
        "L0":L0,
        "W":W,
        "pW":pW,
        "pivots":piv,
        "woodbury_denominator":den,
    }


def tail_z_endpoint(ns):
    return z_source_faithful(ns)-RHO*PI/2.0


def direct_rows(payload,ns):
    ns=np.asarray(ns,dtype=float)
    zn=tail_z_endpoint(ns)
    modes=payload["modes"]
    z=payload["z"]
    W=payload["W"]

    den=ns[:,None]**2-modes[None,:]**2
    A0=(2.0/PI)*(
        zn[:,None]*modes[None,:]
        -ns[:,None]*z[None,:]
    )/den

    pn,_=pole_vector(ns,payload["sector"])
    return (
        A0@W
        +payload["alpha"]*pn[:,None]*payload["pW"][None,:]
    )


def inverse_power_moments(payload):
    j=payload["modes"].astype(np.longdouble)
    W=payload["W"].astype(np.longdouble)
    z=payload["z"].astype(np.longdouble)

    aa=[]
    bb=[]
    for k in range(KEXP):
        aa.append(np.sum((j**(2*k+1))[:,None]*W,axis=0))
        bb.append(np.sum((z*j**(2*k))[:,None]*W,axis=0))
    return np.array(aa),np.array(bb)


def expanded_rows(payload,ns,aa,bb):
    nn=np.asarray(ns,dtype=np.longdouble)
    zn=tail_z_endpoint(np.asarray(ns,dtype=float)).astype(np.longdouble)
    d=6
    R=np.zeros((len(nn),d),dtype=np.longdouble)
    pild=np.longdouble(PI)

    for k in range(KEXP):
        R += (np.longdouble(2)/pild)*(
            zn[:,None]*aa[k][None,:]/nn[:,None]**(2*k+2)
            -bb[k][None,:]/nn[:,None]**(2*k+1)
        )

    pn,_=pole_vector(np.asarray(ns,dtype=float),payload["sector"])
    R += (
        np.longdouble(payload["alpha"])
        *pn.astype(np.longdouble)[:,None]
        *payload["pW"].astype(np.longdouble)[None,:]
    )
    return np.asarray(R,dtype=float)


def normalized_gram(payload):
    sector=payload["sector"]
    start=4001 if sector=="even-v" else 4002
    direct_stop=16001 if sector=="even-v" else 16000

    G=np.zeros((6,6),dtype=float)

    for st in range(start,direct_stop+1,2000):
        en=min(st+1998,direct_stop)
        ns=np.arange(st,en+1,2,dtype=float)
        R=direct_rows(payload,ns)
        G+=R.T@R

    aa,bb=inverse_power_moments(payload)
    st=direct_stop+2
    while st<=EXPLICIT_STOP:
        en=min(st+199998,EXPLICIT_STOP)
        if (en-st)%2:
            en-=1
        ns=np.arange(st,en+1,2,dtype=float)
        R=expanded_rows(payload,ns,aa,bb)
        G+=R.T@R
        st=en+2

    L0=payload["L0"]
    H=np.linalg.solve(L0,G)@np.linalg.inv(L0.T)
    H=(H+H.T)/2
    return G,H


def far_envelope(payload):
    sector=payload["sector"]
    L0=payload["L0"]
    T=np.linalg.inv(L0.T)

    W=payload["W"]@T
    pW=payload["p"]@W
    modes=payload["modes"]
    z=payload["z"]
    alpha=payload["alpha"]

    if sector=="even-v":
        N=2_000_001.0
        g=math.cosh(0.5)
    else:
        N=2_000_002.0
        g=math.sinh(0.5)

    rho=np.max(modes)/N

    leading=(
        -(2.0/PI)*(z@W)
        +alpha*(4.0*g/PI)*pW
    )

    B=(
        (2.0/PI)*Z_FAR_BOUND/(1-rho*rho)
        *np.sum(np.abs(modes[:,None]*W),axis=0)
    )

    C=(
        (2.0/PI)/(1-rho*rho)
        *np.sum(np.abs((modes*modes*z)[:,None]*W),axis=0)
        +abs(alpha)*(4.0*g/PI**3)*np.abs(pW)
    )

    def S(power):
        return (
            N**(-power)
            +1.0/(2.0*(power-1)*N**(power-1))
        )

    root=(
        np.linalg.norm(leading)*math.sqrt(S(2))
        +np.linalg.norm(B)*math.sqrt(S(4))
        +np.linalg.norm(C)*math.sqrt(S(6))
    )
    return {
        "bound":root*root,
        "leading":leading,
        "leading_norm2":float(leading@leading),
        "B_norm":float(np.linalg.norm(B)),
        "C_norm":float(np.linalg.norm(C)),
    }


def report_one(sector):
    p=finite_payload(sector)
    G,H=normalized_gram(p)
    vals,U=np.linalg.eigh(H)
    far=far_envelope(p)

    leading=far["leading"]
    overlap=abs(float(
        (leading/np.linalg.norm(leading))@U[:,-1]
    ))

    print("\nsector =",sector)
    print("buffer min pole-free pivot =",float(np.min(p["pivots"])))
    print("pole Woodbury denominator =",p["woodbury_denominator"])
    print("normalized H through 2M =")
    print(H)
    print("normalized H eigenvalues through 2M =",vals)
    print("lambda_max(H_explicit) =",vals[-1])
    print("second eigenvalue =",vals[-2])
    print("leading normalized 1/n coefficient norm^2 =",far["leading_norm2"])
    print("dominant-eigenvector / leading-channel overlap =",overlap)
    print("far normalized Gram envelope =",far["bound"])
    print("explicit + far scalar ceiling =",vals[-1]+far["bound"])

    return vals[-1],far["bound"],overlap


def main():
    even=report_one("even-v")
    odd=report_one("odd-v")

    # Midpoint regression targets.
    assert abs(even[0]-0.17738742092868218)<5e-12
    assert abs(odd[0]-0.012096498661467095)<5e-12
    assert even[1]<3.81e-4
    assert odd[1]<2.59e-5
    assert even[2]>0.99999999
    assert odd[2]>0.99999999

    print("\nPASS midpoint frozen-coordinate remote residual-Gram replay")
    print(
        "GUARDRAIL: explicit accumulation and far envelope are not yet "
        "outward-rounded interval certificates."
    )


if __name__=="__main__":
    main()
