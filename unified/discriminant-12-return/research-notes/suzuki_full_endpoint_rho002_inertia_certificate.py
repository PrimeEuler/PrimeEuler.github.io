#!/usr/bin/env python3
"""Full rho=0.02 endpoint inertia certificate in both parity sectors.

Minus endpoint:
  * imports the exact tail theorem ind_-(F^-_tail)=4;
  * certifies an infinite positive subspace of codimension four by enlarging
    the finite effective core from 10 to 12 coordinates and freezing its
    eight positive directions;
  * replays finite-buffer conditioning, remote Gram through two million, and
    analytic far tail with widened fail-closed caps.

Plus endpoint:
  * imports exact tail positivity F^+_tail>0;
  * exhibits a compactly supported two-dimensional strict negative subspace.
    Since the positive tail itself has codimension two, this proves full
    negative index exactly two.

Frozen payloads are consumed unchanged.
"""
from __future__ import annotations
import math
import mpmath as mp
import numpy as np

import suzuki_endpoint_M3999_rho002_adversarial_audit as A
from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data, offdiag, pole_vector, structured_ldl,
)
from suzuki_full_endpoint_rho002_frozen_carriers import (
    EVEN_MINUS_QPOS_HEX, EVEN_MINUS_LPOS_HEX,
    ODD_MINUS_QPOS_HEX, ODD_MINUS_LPOS_HEX,
    EVEN_PLUS_MODES, EVEN_PLUS_QNEG_HEX, EVEN_PLUS_LNEG_HEX,
    ODD_PLUS_MODES, ODD_PLUS_QNEG_HEX, ODD_PLUS_LNEG_HEX,
    floats, verify,
)

EPS_F=A.EPS_F
RHO=0.02
REMOTE_CROSS_CAP=20.0
REPLAY_ARITH_CAP=1.0e-8

MINUS_FINITE_CAPS={
    "even-v": dict(K=1.08,resid=1.55e-15,ref=1.40e-15),
    "odd-v":  dict(K=.82,resid=1.45e-15,ref=1.40e-15),
}
MINUS_REMOTE_CAPS={
    "even-v": dict(Hexp=.0490,Hfar=1.20e-4,invL=11.2,W=11.2,Y=.225,epsY=2.5e-6),
    "odd-v":  dict(Hexp=.0250,Hfar=7.00e-5,invL=18.8,W=18.8,Y=.165,epsY=4.0e-6),
}
GAMMA_LOWER={
    "even-v":3.18003114023348,
    "odd-v":3.18016610573875,
}

PUBLIC_MINUS_TERMINAL={
    "even-v":3.1308,
    "odd-v":3.1550,
}
PUBLIC_MINUS_NORMALIZED={
    "even-v":0.9845,
    "odd-v":0.9920,
}
PUBLIC_PLUS_NEG={
    "even-v":0.0071916,
    "odd-v":0.0006165,
}


def full12_layout(sector):
    if sector=="even-v":
        return np.arange(1,24,2,dtype=int), np.arange(25,4000,2,dtype=int)
    return np.arange(2,25,2,dtype=int), np.arange(26,4001,2,dtype=int)


def dense_polefree(modes,z,diag):
    M=offdiag(modes,modes,z,z)
    np.fill_diagonal(M,diag)
    return M


def build_full12_minus(sector):
    core,buffer_=full12_layout(sector)
    modes=np.concatenate([core,buffer_])
    z,diag=endpoint_data(modes,sign=-1,rho=RHO)
    nc=len(core)
    zc,zf=z[:nc],z[nc:]
    dc,df=diag[:nc],diag[nc:]

    C0=offdiag(core,core,zc,zc); np.fill_diagonal(C0,dc)
    R0=offdiag(core,buffer_,zc,zf)

    p,alpha=pole_vector(modes,sector)
    pc,pf=p[:nc],p[nc:]

    C=C0+alpha*np.outer(pc,pc)
    R=R0+alpha*np.outer(pc,pf)

    A0=dense_polefree(buffer_,zf,df)
    L,D=structured_ldl(buffer_,zf,df)

    return dict(
        sector=sector,sign=-1,core=core,buffer=buffer_,
        modes=modes.astype(float),z=z,C=C,R=R,A0=A0,
        Afull=A0+alpha*np.outer(pf,pf),L=L,D=D,
        p=p,pf=pf,alpha=alpha,
    )


def audit_minus_positive(sector,Q,Lref):
    block=build_full12_minus(sector)
    cap=MINUS_FINITE_CAPS[sector]

    bc=A.buffer_condition(block)

    BQ=block["R"].T@Q
    Y=A.solve_full(block,BQ)

    Kactual=float(np.linalg.norm(BQ,"fro"))
    residual=A.rhs_residual_outward(block["Afull"],BQ,Y)
    ref=A.reference_defect(block["C"],block["R"],Q,Y,Lref,False)

    if Kactual>=cap["K"] or residual>=cap["resid"] or ref>=cap["ref"]:
        raise RuntimeError(("minus finite cap failed",sector,Kactual,residual,ref))

    q2=max(float(np.linalg.norm(Q,2)**2),1.00000000000001)
    lmin=float(np.linalg.eigvalsh(Lref@Lref.T)[0])

    eps_source=A.source_schur_bound(EPS_F,cap["K"],bc["mu"],q2)
    eps_solve=cap["K"]/bc["mu"]*cap["resid"]
    eps_total=cap["ref"]+eps_source+eps_solve

    normalized=1.0-eps_total/lmin
    if normalized<=0:
        raise RuntimeError(("minus finite positivity failed",sector,normalized))

    audit=dict(
        kind="full-minus-pos",sector=sector,block=block,Q=Q,L0=Lref,Y=Y,
        buffer=bc,Kactual=Kactual,residual=residual,ref=ref,lmin=lmin,
        normalized_lower=normalized,
    )

    payload=A.dressed(audit)
    H=A.normalized_gram(payload)
    lam=float(np.linalg.eigvalsh(H)[-1])
    far,invL,Wnorm=A.far_envelope(payload)

    rcap=MINUS_REMOTE_CAPS[sector]
    if lam>=rcap["Hexp"] or far>=rcap["Hfar"]:
        raise RuntimeError(("minus remote H cap failed",sector,lam,far))
    if invL>=rcap["invL"] or Wnorm>=rcap["W"]:
        raise RuntimeError(("minus conditioning cap failed",sector,invL,Wnorm))

    giv=A.tail_floor_interval(-1,sector)
    glow=GAMMA_LOWER[sector]
    if not giv>mp.iv.mpf(str(glow)):
        raise RuntimeError(("minus gamma cap failed",sector,giv))

    dx=(
        EPS_F/(bc["mu"]-EPS_F)
        +EPS_F*cap["K"]/(bc["mu"]*(bc["mu"]-EPS_F))
        +cap["resid"]/bc["mu"]
    )*rcap["invL"]

    epsY=(
        REMOTE_CROSS_CAP*dx
        +EPS_F*rcap["W"]
        +REPLAY_ARITH_CAP
    )
    if epsY>=rcap["epsY"]:
        raise RuntimeError(("minus epsY cap failed",sector,epsY))

    if math.sqrt(rcap["Hexp"]+rcap["Hfar"])>=rcap["Y"]:
        raise RuntimeError(("minus Y cap failed",sector))

    Hupper=(
        rcap["Hexp"]+rcap["Hfar"]
        +2*rcap["Y"]*rcap["epsY"]
        +rcap["epsY"]**2
    )

    terminal=glow*normalized-Hupper
    normpost=normalized-Hupper/glow

    if terminal<=PUBLIC_MINUS_TERMINAL[sector]:
        raise RuntimeError(("minus terminal theorem margin",sector,terminal))
    if normpost<=PUBLIC_MINUS_NORMALIZED[sector]:
        raise RuntimeError(("minus normalized theorem margin",sector,normpost))

    return dict(
        Kactual=Kactual,residual=residual,reference_defect=ref,
        buffer_floor=bc["mu_exact"],lmin=lmin,
        finite_normalized=normalized,
        Hexplicit=lam,Hfar=far,invL=invL,Wnorm=Wnorm,
        gamma_interval=giv,gamma_lower=glow,
        derived_epsY=epsY,Hupper=Hupper,
        terminal_margin=terminal,normalized_post=normpost,
    )


def plus_trial_matrix(sector,modes,Q):
    modes=np.asarray(modes,dtype=int)
    z,diag=endpoint_data(modes,sign=+1,rho=RHO)
    M=offdiag(modes,modes,z,z)
    np.fill_diagonal(M,diag)
    p,alpha=pole_vector(modes,sector)
    M+=alpha*np.outer(p,p)
    M=(M+M.T)/2
    return Q.T@M@Q


def audit_plus_negative(sector,modes,Q,Lref):
    G=plus_trial_matrix(sector,modes,Q)
    reference=-Lref@Lref.T
    defect=float(np.linalg.norm(G-reference,2))

    # Fixed numerical subspace: exact-vs-nominal full-form perturbation.
    q2=max(float(np.linalg.norm(Q,2)**2),1.00000000000001)
    total=defect+q2*EPS_F+1.0e-14

    lmin=float(np.linalg.eigvalsh(Lref@Lref.T)[0])
    raw=lmin-total

    if defect>=1.0e-15:
        raise RuntimeError(("plus reference defect",sector,defect))
    if raw<=PUBLIC_PLUS_NEG[sector]:
        raise RuntimeError(("plus negative theorem margin",sector,raw))

    return dict(
        reference_defect=defect,
        reference_lmin=lmin,
        total_error=total,
        negative_margin=raw,
        restricted_eigenvalues=np.linalg.eigvalsh(G),
    )


def main():
    verify()
    A.prove_far_generator()
    A.common_cross_cap_check()

    minus={
        "even-v":audit_minus_positive(
            "even-v",floats(EVEN_MINUS_QPOS_HEX),floats(EVEN_MINUS_LPOS_HEX)
        ),
        "odd-v":audit_minus_positive(
            "odd-v",floats(ODD_MINUS_QPOS_HEX),floats(ODD_MINUS_LPOS_HEX)
        ),
    }

    plus={
        "even-v":audit_plus_negative(
            "even-v",EVEN_PLUS_MODES,
            floats(EVEN_PLUS_QNEG_HEX),floats(EVEN_PLUS_LNEG_HEX)
        ),
        "odd-v":audit_plus_negative(
            "odd-v",ODD_PLUS_MODES,
            floats(ODD_PLUS_QNEG_HEX),floats(ODD_PLUS_LNEG_HEX)
        ),
    }

    for sec in ("even-v","odd-v"):
        print("\nsector =",sec)
        print("minus positive codim-4 certificate =",minus[sec])
        print("plus negative 2-plane certificate =",plus[sec])

    print("\nTHEOREM")
    print("minus full endpoint: ind_-=4, kernel=0 in both parities")
    print("plus  full endpoint: ind_-=2, kernel=0 in both parities")
    print("signed endpoint spectral flow = 4-2 = 2 in each parity")
    print(
        "Guardrail: signed Pontryagin spectral flow is not by itself "
        "an ordinary six-root multiplicity theorem."
    )


if __name__=="__main__":
    main()
