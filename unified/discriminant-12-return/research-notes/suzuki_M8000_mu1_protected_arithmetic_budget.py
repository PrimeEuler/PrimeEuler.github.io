#!/usr/bin/env python3
"""Arithmetic-magnitude budget for the M8000 mu=1 protected 6x6 block.

Reconstruct the same one-step LDDD graph vectors used by the successful
M8000 shifted-front gate and report:
  * the final 6x6 variational matrix W^* H W;
  * the residual Gram and protected eigenvalues;
  * ||W||_F^2;
  * Qabs = |W|^T |H_nom| |W|, entrywise absolute accumulation.

Qabs is the natural magnitude factor for a conservative LDDD rounding bound.
With u_ld=2^-64, a model C*n*u_ld^2*Qabs can be compared directly with the
5.7e-30 even protected pivot.

Diagnostic only: this script does not choose the final LDDD error constant.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp
import numpy as np

from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_M3999_frozen_p4_source_capacity_midpoint import full_source_matrix
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement, dd_matrix_to_mp, dd_project, mp_inverse_split,
    solve_correction,
)
from suzuki_ldd_source_operator import (
    LD, add as dd_add, dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data, matvec as dd_matvec,
    norm2 as dd_norm2, sub as dd_sub,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_mu1_protected_arithmetic_budget_result.json"
DPS=180
ULD=mp.mpf(2)**-64


def shifted_matvec(data,Xh,Xl,shell_start):
    Yh,Yl=dd_matvec(data,Xh,Xl)
    Yh=Yh.copy(); Yl=Yl.copy()
    Yh[shell_start:]-=Xh[shell_start:]
    Yl[shell_start:]-=Xl[shell_start:]
    return Yh,Yl


def one_sector(sector):
    base_modes,modes,P,_,_=embedded_protected_basis(sector)
    shell_start=len(base_modes)
    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A,_=full_source_matrix(modes,sector)
    H=A.copy()
    idx=np.arange(shell_start,len(modes))
    H[idx,idx]-=1.0
    H=(H+H.T)/2

    # Binary64 correction operator on the shifted front.
    def proj(x):
        return x-P@(Gi@(P.T@x))
    from scipy.sparse.linalg import LinearOperator, cg
    def comp_mv(x):
        q=proj(np.asarray(x,dtype=float))
        return proj(H@q)+P@(Gi@(P.T@x))
    op=LinearOperator(H.shape,matvec=comp_mv,dtype=float)

    E=proj(H@P)
    Y0=np.empty_like(E)
    for j in range(6):
        y,info=cg(op,E[:,j],rtol=2e-14,atol=0.0,maxiter=30000)
        if info!=0: raise RuntimeError((sector,j,info))
        Y0[:,j]=proj(y)

    data=hp_parity_data(modes,sector,dps=DPS,arch_terms=160,correction_terms=50)
    Yh=Y0.astype(LD); Yl=np.zeros_like(Yh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)

    history=[]
    for step in range(2):
        Wh,Wl=dd_sub(P,np.zeros_like(P,dtype=LD),Yh,Yl)
        HWh,HWl=shifted_matvec(data,Wh,Wl,shell_start)
        Rh,Rl=dd_project(P,Gih,Gil,HWh,HWl)
        norms=[dd_norm2(Rh[:,j],Rl[:,j]) for j in range(6)]
        history.append(norms)
        if step==0:
            for j in range(6):
                delta=solve_correction(op,proj,Rh[:,j]+Rl[:,j],rtol=2e-14)
                Yh[:,j],Yl[:,j]=dd_add(
                    Yh[:,j],Yl[:,j],delta,np.zeros_like(delta,dtype=LD)
                )
            Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)

    Wh,Wl=dd_sub(P,np.zeros_like(P,dtype=LD),Yh,Yl)
    HWh,HWl=shifted_matvec(data,Wh,Wl,shell_start)
    Rh,Rl=dd_project(P,Gih,Gil,HWh,HWl)

    Sh,Sl=dd_dot_columns(Wh,Wl,HWh,HWl)
    RRh,RRl=dd_dot_columns(Rh,Rl,Rh,Rl)

    with mp.workdps(DPS):
        S=dd_matrix_to_mp(Sh,Sl); S=(S+S.T)/2
        RR=dd_matrix_to_mp(RRh,RRl); RR=(RR+RR.T)/2
        seigs,_=mp.eigsy(S)
        rreigs,_=mp.eigsy(RR)

    W=np.asarray(Wh+Wl,dtype=float)
    # Binary64 absolute-contribution magnitude only.
    Qabs=np.abs(W).T@(np.abs(H)@np.abs(W))
    wfrob2=float(np.sum(W*W))

    with mp.workdps(80):
        factors={}
        for C in (100,1000,10000):
            factors[str(C)]=mp.nstr(
                mp.mpf(C)*len(modes)*(ULD**2)*mp.mpf(str(np.max(Qabs))),40
            )

    return {
        "sector":sector,
        "dimension":len(modes),
        "final_residual_norms":[float(x) for x in history[-1]],
        "protected_matrix":[[mp.nstr(S[i,j],70) for j in range(6)] for i in range(6)],
        "protected_eigenvalues":[mp.nstr(seigs[i],70) for i in range(6)],
        "residual_gram_max_eigenvalue":mp.nstr(rreigs[-1],60),
        "W_frobenius_squared":wfrob2,
        "Qabs_max":float(np.max(Qabs)),
        "Qabs_matrix":Qabs.tolist(),
        "candidate_C_n_u2_Qabs_bounds":factors,
    }


def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    out={"rows":rows,"guardrail":"Arithmetic magnitude diagnostic only."}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    for r in rows:
        print("\n",r["sector"])
        print("protected eigs =",r["protected_eigenvalues"])
        print("residual Gram max =",r["residual_gram_max_eigenvalue"])
        print("W frob^2 =",r["W_frobenius_squared"])
        print("Qabs max =",r["Qabs_max"])
        print("candidate errors =",r["candidate_C_n_u2_Qabs_bounds"])
    print("wrote",OUT)


if __name__=="__main__":
    main()
