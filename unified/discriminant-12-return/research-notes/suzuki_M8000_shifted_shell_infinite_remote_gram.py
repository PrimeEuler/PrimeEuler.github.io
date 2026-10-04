#!/usr/bin/env python3
"""Infinite remote-Gram diagnostic for the shifted M=8000 shell floor.

Goal
----
For N=4000, test positivity of

    F_mu = A - mu * Pi_{n>N}

on the full infinite parity space, with
    mu_e = 0.10,
    mu_o = 0.40.

The finite front through M=8000 is reduced by the unchanged frozen N=4000
six-plane exactly as in suzuki_M8000_shifted_shell_feshbach_ldd.py.

Let W be the six dressed protected directions after eliminating the stiff
finite complement.  For the remote tail n>M, let R be their source-faithful
residual row operator.  If the raw remote block satisfies

    D_remote - mu I >= gamma_far I,

then its self-energy obeys

    R^* (D_remote-mu I)^(-1) R <= gamma_far^(-1) R^*R.

Thus a sufficient protected lower matrix is

    S_inf_lower
      = S_front_lower
        - gamma_far^(-1) G_remote_upper.

This script:
  * rebuilds the shifted finite front and one LDDD refinement;
  * forms the 6x6 finite Loewner lower matrix;
  * accumulates the remote Gram directly to ~16000;
  * uses an 8-level inverse-power expansion through 2,000,000;
  * adds a coarse analytic far envelope with |z_n|<=8;
  * uses the source-faithful rho=0 raw-tail coercivity formula, minus mu.

Diagnostic/certification target only: explicit Gram accumulation is not yet
outward-rounded.  The remote coercivity interval formula itself is outward.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from suzuki_M8000_embedded_p4_ldd_capacity import (
    DPS,
    embedded_protected_basis,
)
from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    full_source_matrix,
    pole_vector,
    z_source_faithful,
)
from suzuki_M8000_shifted_shell_feshbach_ldd import (
    TARGET_MU,
    shifted_binary_matrix,
    coupling_residuals,
    form_variational,
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement,
    dd_project,
    mp_inverse_split,
    residual_gram_mp,
    solve_correction,
)
from suzuki_ldd_source_operator import (
    LD,
    add as dd_add,
    dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,
    sub as dd_sub,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_shifted_shell_infinite_remote_gram_result.json"

PI=math.pi
KEXP=8
EXPLICIT_STOP=2_000_000
Z_FAR_BOUND=8.0


def zeta3_interval(M=20000):
    iv=mp.iv
    s=iv.mpf(0)
    for k in range(1,M+1):
        x=iv.mpf(k)
        s += 1/x**3
    lo=1/(2*iv.mpf(M+1)**2)
    hi=1/(2*iv.mpf(M)**2)
    return iv.mpf([s.a+lo.a,s.b+hi.b])


def raw_remote_floor_interval(sector, start, mu):
    """Outward raw floor for A_remote - mu I at rho=0."""
    iv=mp.iv
    iv.dps=80
    n=iv.mpf(start)
    pi=iv.pi
    s2=n**-2+1/(2*n)

    c=2/pi**3+6/pi**4
    aa=2*c/pi
    cd=2/pi**2+2/pi**3+2/pi**4+6/pi**5
    cusp=(
        2/pi**2*s2
        +2*aa*iv.sqrt(pi**2/12*(n**-6+1/(10*n**5)))
        +cd*iv.sqrt(n**-4+1/(6*n**3))
    )

    z3=zeta3_interval()
    q=2/pi
    m4=z3*q**3/(4*(1-q)**3)
    cr=iv.mpf(19)/12+4*m4
    arch=4*cr/pi**2*s2

    out=(
        iv.log(n/4)-pi/2
        -iv.mpf("2.05")
        -cusp
        -arch
        -iv.mpf(str(mu))
    )
    if sector=="odd-v":
        sh=(iv.exp(iv.mpf(".5"))-iv.exp(-iv.mpf(".5")))/2
        out -= 32*sh**2/pi**2*s2
    return out


def rebuild_front(sector,mu):
    base_modes,modes,P,_,_=embedded_protected_basis(sector)
    shell_start=len(base_modes)

    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A,_=full_source_matrix(modes,sector)
    Ashift=shifted_binary_matrix(A,shell_start,mu)
    zrhs=np.zeros(len(modes),dtype=float)
    op,proj,gamma,evals,Y0,_,_=build_double_complement(
        Ashift,P,Gi,zrhs,rtol=2e-14
    )
    if gamma<=0:
        raise RuntimeError((sector,"shifted complement failed",gamma))

    data=hp_parity_data(
        modes,sector,dps=DPS,arch_terms=160,correction_terms=50
    )

    Yh=Y0.astype(LD)
    Yl=np.zeros_like(Yh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)

    for step in range(2):
        Wh,Wl=dd_sub(P,np.zeros_like(P,dtype=LD),Yh,Yl)
        AWh,AWl,Rh,Rl,norms=coupling_residuals(
            data,P,Gih,Gil,Wh,Wl,shell_start,mu
        )
        if step==0:
            for j in range(6):
                rhs=Rh[:,j]+Rl[:,j]
                delta=solve_correction(op,proj,rhs,rtol=2e-14)
                Yh[:,j],Yl[:,j]=dd_add(
                    Yh[:,j],Yl[:,j],
                    delta,np.zeros_like(delta,dtype=LD)
                )
            Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)

    St=form_variational(Wh,Wl,AWh,AWl,DPS)
    RR=residual_gram_mp(Rh,Rl,DPS)
    with mp.workdps(DPS):
        SL=(St-RR/mp.mpf(str(gamma)))
        SL=(SL+SL.T)/2

    # Convert dressed W to float for the remote-row diagnostic.
    W=np.asarray(Wh+Wl,dtype=float)
    return dict(
        modes=modes.astype(float),
        W=W,
        SL=SL,
        comp_gamma=gamma,
        comp_eigs=evals,
        final_res=max(norms),
    )


def remote_rows(payload,sector,ns):
    ns=np.asarray(ns,dtype=float)
    modes=payload["modes"]
    W=payload["W"]

    zf=z_source_faithful(modes)
    zn=z_source_faithful(ns)
    den=ns[:,None]**2-modes[None,:]**2
    A0=(2.0/PI)*(
        zn[:,None]*modes[None,:]
        -ns[:,None]*zf[None,:]
    )/den

    pfin,alpha=pole_vector(modes,sector)
    pn,_=pole_vector(ns,sector)
    pW=pfin@W
    return A0@W+alpha*pn[:,None]*pW[None,:]


def inverse_power_moments(payload):
    j=payload["modes"].astype(np.longdouble)
    W=payload["W"].astype(np.longdouble)
    z=z_source_faithful(payload["modes"]).astype(np.longdouble)

    aa=[]
    bb=[]
    for k in range(KEXP):
        aa.append(np.sum((j**(2*k+1))[:,None]*W,axis=0))
        bb.append(np.sum((z*j**(2*k))[:,None]*W,axis=0))
    return np.array(aa),np.array(bb)


def expanded_rows(payload,sector,ns,aa,bb):
    nn=np.asarray(ns,dtype=np.longdouble)
    zn=z_source_faithful(np.asarray(ns,dtype=float)).astype(np.longdouble)
    R=np.zeros((len(nn),6),dtype=np.longdouble)
    pild=np.longdouble(PI)

    for k in range(KEXP):
        R += (np.longdouble(2)/pild)*(
            zn[:,None]*aa[k][None,:]/nn[:,None]**(2*k+2)
            -bb[k][None,:]/nn[:,None]**(2*k+1)
        )

    modes=payload["modes"]
    pfin,alpha=pole_vector(modes,sector)
    pW=pfin@payload["W"]
    pn,_=pole_vector(np.asarray(ns,dtype=float),sector)
    R += (
        np.longdouble(alpha)
        *pn.astype(np.longdouble)[:,None]
        *pW.astype(np.longdouble)[None,:]
    )
    return np.asarray(R,dtype=float)


def remote_gram(payload,sector):
    start=8001 if sector=="even-v" else 8002
    direct_stop=16001 if sector=="even-v" else 16000
    G=np.zeros((6,6),dtype=float)

    for st in range(start,direct_stop+1,2000):
        en=min(st+1998,direct_stop)
        ns=np.arange(st,en+1,2,dtype=float)
        R=remote_rows(payload,sector,ns)
        G+=R.T@R

    aa,bb=inverse_power_moments(payload)
    st=direct_stop+2
    while st<=EXPLICIT_STOP:
        en=min(st+199998,EXPLICIT_STOP)
        if (en-st)%2:
            en-=1
        ns=np.arange(st,en+1,2,dtype=float)
        R=expanded_rows(payload,sector,ns,aa,bb)
        G+=R.T@R
        st=en+2
    return (G+G.T)/2


def far_envelope(payload,sector):
    W=payload["W"]
    modes=payload["modes"]
    z=z_source_faithful(modes)
    pfin,alpha=pole_vector(modes,sector)
    pW=pfin@W

    if sector=="even-v":
        N=2_000_001.0
        g=math.cosh(.5)
    else:
        N=2_000_002.0
        g=math.sinh(.5)

    ratio=np.max(modes)/N
    leading=-(2.0/PI)*(z@W)+alpha*(4.0*g/PI)*pW

    B=(
        (2.0/PI)*Z_FAR_BOUND/(1-ratio*ratio)
        *np.sum(np.abs(modes[:,None]*W),axis=0)
    )
    C=(
        (2.0/PI)/(1-ratio*ratio)
        *np.sum(np.abs((modes*modes*z)[:,None]*W),axis=0)
        +abs(alpha)*(4.0*g/PI**3)*np.abs(pW)
    )

    def S(power):
        return N**(-power)+1.0/(2.0*(power-1)*N**(power-1))

    root=(
        np.linalg.norm(leading)*math.sqrt(S(2))
        +np.linalg.norm(B)*math.sqrt(S(4))
        +np.linalg.norm(C)*math.sqrt(S(6))
    )
    return dict(
        gram_operator_bound=root*root,
        leading_norm2=float(leading@leading),
        B_norm=float(np.linalg.norm(B)),
        C_norm=float(np.linalg.norm(C)),
    )


def one_sector(sector):
    mu=TARGET_MU[sector]
    payload=rebuild_front(sector,mu)
    G=remote_gram(payload,sector)
    far=far_envelope(payload,sector)

    start=8001 if sector=="even-v" else 8002
    giv=raw_remote_floor_interval(sector,start,mu)
    # Conservative scalar floor taken from interval lower endpoint.
    glow=float(giv.a)

    with mp.workdps(DPS):
        Gmp=mp.matrix(6)
        for i in range(6):
            for j in range(6):
                Gmp[i,j]=mp.mpf(str(G[i,j]))
        Ginfl=Gmp+mp.mpf(str(far["gram_operator_bound"]))*mp.eye(6)
        Sinf=(payload["SL"]-Ginfl/mp.mpf(str(glow)))
        Sinf=(Sinf+Sinf.T)/2
        vals,_=mp.eigsy(Sinf)
        vals_front,_=mp.eigsy(payload["SL"])

    print("\n",sector)
    print("mu =",mu)
    print("raw remote gamma interval =",giv)
    print("remote Gram eigs explicit =",np.linalg.eigvalsh(G))
    print("far scalar Gram envelope =",far["gram_operator_bound"])
    print("front protected min =",mp.nstr(vals_front[0],50))
    print("infinite lower protected min =",mp.nstr(vals[0],50))

    return {
        "sector":sector,
        "mu":mu,
        "raw_remote_gamma_interval":str(giv),
        "raw_remote_gamma_lower_float":glow,
        "finite_complement_floor_midpoint":payload["comp_gamma"],
        "finite_final_max_ldd_residual":payload["final_res"],
        "finite_protected_lower_min":mp.nstr(vals_front[0],60),
        "remote_gram_explicit_eigenvalues":[
            float(x) for x in np.linalg.eigvalsh(G)
        ],
        "remote_gram_far_operator_bound":far["gram_operator_bound"],
        "remote_leading_norm2":far["leading_norm2"],
        "infinite_protected_lower_eigenvalues":[
            mp.nstr(vals[j],60) for j in range(6)
        ],
        "infinite_protected_lower_min":mp.nstr(vals[0],60),
        "positive_diagnostic":bool(vals[0]>0),
    }


def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    out={
        "rows":rows,
        "guardrail":(
            "Diagnostic/certification target. Raw remote coercivity is outward "
            "interval arithmetic; finite front is LDDD with midpoint stiff "
            "complement floor; explicit remote Gram accumulation is not yet "
            "outward-rounded. No theorem is promoted by this script alone."
        ),
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)


if __name__=="__main__":
    main()
