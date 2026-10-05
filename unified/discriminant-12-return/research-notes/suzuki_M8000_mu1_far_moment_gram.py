#!/usr/bin/env python3
"""Shifted-front far moment Gram for proving S_{p,4000} > I.

We already have a finite LDDD/Feshbach diagnostic that

    A_8000 - Pi_{4000<n<=8000} > 0

for both parities at mu=1.

To extend this to the infinite shifted operator

    A_infty - Pi_{n>4000},

split at M=8000.  The far Schur block is

    D_far - I - B_far F^{-1} B_far^*,

where

    F = A_8000 - Pi_{4000<n<=8000}.

This script computes the first four correlated signed-moment coefficients

    M_ij^(shift) = w_i^T F^{-1} w_j

with the unchanged frozen P4/Feshbach architecture, and combines them with
same-parity far scalar norms on n>8000.

If the resulting four-channel Schur budget plus the geometric remainder lies
below the rigorous raw far floor minus 1, then the infinite shifted operator
is positive and therefore

    S_{p,4000} > I.

Diagnostic only: the present script uses midpoint LDDD coefficients and reports
residuals.  Promotion requires outward interval propagation.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.sparse.linalg import cg, LinearOperator

from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_M3999_frozen_p4_source_capacity_midpoint import full_source_matrix
from suzuki_N4000_remote_coupling_moment_gram_ldd import channel_matrix_dd
from suzuki_ldd_refined_capacity_bracket import (
    dd_matrix_to_mp,
    dd_project,
    mp_inverse_split,
    solve_correction,
)
from suzuki_ldd_source_operator import (
    LD,
    add as dd_add,
    dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,
    matvec as dd_matvec,
    norm2 as dd_norm2,
    sub as dd_sub,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_mu1_far_moment_gram_result.json"
DPS=180


def shifted_data_matvec(data, modes, xh, xl, shell_start):
    yh,yl=dd_matvec(data,xh,xl)
    # subtract mu=1 on 4000<n<=8000
    yh2=yh.copy()
    yl2=yl.copy()
    yh2[shell_start:]-=xh[shell_start:]
    yl2[shell_start:]-=xl[shell_start:]
    return yh2,yl2


def one_sector(sector):
    base_modes,modes,P,_,_=embedded_protected_basis(sector)
    shell_start=len(base_modes)
    n=len(modes)

    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A,_=full_source_matrix(modes,sector)
    Ash=A.copy()
    Ash[shell_start:,shell_start:]-=np.eye(n-shell_start)

    data=hp_parity_data(
        modes,sector,dps=DPS,arch_terms=160,correction_terms=50
    )
    Bh,Bl=channel_matrix_dd(data,modes,sector)
    Bfloat=np.asarray(Bh+Bl,dtype=float)

    def proj(x):
        return x-P@(Gi@(P.T@x))

    def comp_mv(x):
        q=proj(np.asarray(x,dtype=float))
        return proj(Ash@q)+P@(Gi@(P.T@x))

    op=LinearOperator((n,n),matvec=comp_mv,dtype=float)

    # Graph/coupling solve for the frozen six-plane.
    AP=Ash@P
    E=proj(AP)
    Y0=np.empty_like(E)
    for j in range(6):
        y,info=cg(op,E[:,j],rtol=2e-14,atol=0.0,maxiter=30000)
        if info!=0: raise RuntimeError((sector,"coupling CG",j,info))
        Y0[:,j]=proj(y)

    X0=np.empty((n,4),dtype=float)
    init=[]
    for j in range(4):
        rhs=proj(Bfloat[:,j])
        x,info=cg(op,rhs,rtol=2e-14,atol=0.0,maxiter=30000)
        if info!=0: raise RuntimeError((sector,"target CG",j,info))
        x=proj(x)
        X0[:,j]=x
        init.append(float(np.linalg.norm(rhs-comp_mv(x))))

    Yh=Y0.astype(LD); Yl=np.zeros_like(Yh,dtype=LD)
    Xh=X0.astype(LD); Xl=np.zeros_like(Xh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    Xh,Xl=dd_project(P,Gih,Gil,Xh,Xl)

    def coupling_res():
        Wh,Wl=dd_sub(P,np.zeros_like(P,dtype=LD),Yh,Yl)
        AWh,AWl=shifted_data_matvec(data,modes,Wh,Wl,shell_start)
        Rh,Rl=dd_project(P,Gih,Gil,AWh,AWl)
        return Wh,Wl,AWh,AWl,Rh,Rl,[dd_norm2(Rh[:,j],Rl[:,j]) for j in range(6)]

    def target_res():
        AXh,AXl=shifted_data_matvec(data,modes,Xh,Xl,shell_start)
        Rh,Rl=dd_sub(AXh,AXl,Bh,Bl)
        Rh,Rl=dd_project(P,Gih,Gil,Rh,Rl)
        return AXh,AXl,Rh,Rl,[dd_norm2(Rh[:,j],Rl[:,j]) for j in range(4)]

    history=[]
    for step in range(2):
        Wh,Wl,AWh,AWl,RYh,RYl,ny=coupling_res()
        AXh,AXl,RXh,RXl,nx=target_res()
        history.append({"coupling":ny,"targets":nx})
        print(sector,"step",step,"max coupling",max(ny),"max target",max(nx))
        if step==0:
            for j in range(6):
                delta=solve_correction(op,proj,RYh[:,j]+RYl[:,j],rtol=2e-14)
                Yh[:,j],Yl[:,j]=dd_add(
                    Yh[:,j],Yl[:,j],delta,np.zeros_like(delta,dtype=LD)
                )
            for j in range(4):
                delta=solve_correction(op,proj,-(RXh[:,j]+RXl[:,j]),rtol=2e-14)
                Xh[:,j],Xl[:,j]=dd_add(
                    Xh[:,j],Xl[:,j],delta,np.zeros_like(delta,dtype=LD)
                )
            Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
            Xh,Xl=dd_project(P,Gih,Gil,Xh,Xl)

    Wh,Wl,AWh,AWl,RYh,RYl,ny=coupling_res()
    AXh,AXl,RXh,RXl,nx=target_res()

    Sh,Sl=dd_dot_columns(Wh,Wl,AWh,AWl)
    gh,gl=dd_dot_columns(Wh,Wl,Bh,Bl)
    hh,hl=dd_dot_columns(Bh,Bl,Xh,Xl)

    with mp.workdps(DPS):
        S=dd_matrix_to_mp(Sh,Sl); S=(S+S.T)/2
        g=dd_matrix_to_mp(gh,gl)
        h=dd_matrix_to_mp(hh,hl); h=(h+h.T)/2
        Sinvg=mp.matrix(6,4)
        for j in range(4):
            sol=mp.lu_solve(S,g[:,j])
            for i in range(6): Sinvg[i,j]=sol[i]
        M=h+g.T*Sinvg
        M=(M+M.T)/2
        vals,_=mp.eigsy(M)

        n0=mp.mpf(8001 if sector=="even-v" else 8002)
        def psum(p):
            return n0**(-p)+n0**(-(p-1))/(2*(p-1))
        fnorm=[
            mp.sqrt(psum(2)),
            8*mp.sqrt(psum(4)),
            mp.sqrt(psum(6)),
            8*mp.sqrt(psum(8)),
        ]
        far_abs=mp.fsum(
            abs(M[i,j])*fnorm[i]*fnorm[j]
            for i in range(4) for j in range(4)
        )

        return {
            "sector":sector,
            "dimension":n,
            "base_dimension":shell_start,
            "initial_target_residuals":init,
            "ldd_residual_history":history,
            "final_max_coupling_residual":max(ny),
            "final_max_target_residual":max(nx),
            "M_midpoint":[[mp.nstr(M[i,j],70) for j in range(4)] for i in range(4)],
            "M_eigenvalues":[mp.nstr(vals[j],50) for j in range(4)],
            "far_scalar_norm_upper":[mp.nstr(v,50) for v in fnorm],
            "far_four_channel_abs_operator_bound":mp.nstr(far_abs,60),
        }


def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    out={
      "mu":1.0,
      "front":8000,
      "rows":rows,
      "guardrail":(
        "Shifted-front far Schur diagnostic only. M coefficients and residual "
        "effects are not yet promoted as outward exact-source intervals."
      )
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    for r in rows:
        print("\n",r["sector"])
        print("M eigs =",r["M_eigenvalues"])
        print("far bound =",r["far_four_channel_abs_operator_bound"])
        print("max target residual =",r["final_max_target_residual"])
    print("wrote",OUT)


if __name__=="__main__":
    main()
