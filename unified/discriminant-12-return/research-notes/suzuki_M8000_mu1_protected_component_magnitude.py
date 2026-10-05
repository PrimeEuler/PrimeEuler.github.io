#!/usr/bin/env python3
"""Positive pre-cancellation magnitude for the M8000 mu=1 protected form.

The LDDD rounding proof must be charged against arithmetic components before
cancellation, not merely |H_ij| after cancellation.

For the exact midpoint source-faithful column j, define the positive
component majorant

 offdiag:
   |c| (|z_i| n_j + |z_j| n_i)/|n_i^2-n_j^2|
   + |alpha| |p_i p_j|,

 diag:
   |d_j| + |alpha| p_j^2 + 1_{j in shifted shell}.

For the same refined graph vectors W used by the successful mu=1 replay,
compute

   Qcomp = |W|^T H_component |W|,

using long-double positive accumulation.  This is a diagnostic magnitude
producer; the ledger proof applies a deliberately much larger public cap.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_M3999_frozen_p4_source_capacity_midpoint import full_source_matrix
from suzuki_ldd_refined_capacity_bracket import (
    dd_project, mp_inverse_split, solve_correction,
)
from suzuki_ldd_source_operator import (
    LD, add as dd_add, dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data, ldd_to_mpf,
    sub as dd_sub, matvec as dd_matvec,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_mu1_protected_component_magnitude_result.json"
DPS=180

def shifted_matvec(data,Xh,Xl,shell_start):
    yh,yl=dd_matvec(data,Xh,Xl)
    yh=yh.copy(); yl=yl.copy()
    yh[shell_start:]-=Xh[shell_start:]
    yl[shell_start:]-=Xl[shell_start:]
    return yh,yl

def one_sector(sector):
    base_modes,modes,P,_,_=embedded_protected_basis(sector)
    shell_start=len(base_modes)
    n=len(modes)
    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A,_=full_source_matrix(modes,sector)
    H=A.copy()
    idx=np.arange(shell_start,n)
    H[idx,idx]-=1.0

    def proj(x):
        return x-P@(Gi@(P.T@x))
    from scipy.sparse.linalg import LinearOperator,cg
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

    # One LDDD residual refinement, identical to protected arithmetic replay.
    Wh,Wl=dd_sub(P,np.zeros_like(P,dtype=LD),Yh,Yl)
    HWh,HWl=shifted_matvec(data,Wh,Wl,shell_start)
    Rh,Rl=dd_project(P,Gih,Gil,HWh,HWl)
    for j in range(6):
        delta=solve_correction(op,proj,Rh[:,j]+Rl[:,j],rtol=2e-14)
        Yh[:,j],Yl[:,j]=dd_add(
            Yh[:,j],Yl[:,j],delta,np.zeros_like(delta,dtype=LD)
        )
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    Wh,Wl=dd_sub(P,np.zeros_like(P,dtype=LD),Yh,Yl)

    W=np.asarray(Wh+Wl,dtype=LD)
    absW=np.abs(W)
    mm=modes.astype(LD)
    z=np.asarray(data.z_hi+data.z_lo,dtype=LD)
    p=np.asarray(data.pole_hi+data.pole_lo,dtype=LD)
    d=np.asarray(data.diag_hi+data.diag_lo,dtype=LD)
    c=abs(LD(data.c_hi+data.c_lo))
    alpha=abs(LD(data.alpha))

    T=np.zeros((n,6),dtype=LD)
    max_component_row=LD(0)
    row_sums=np.zeros(n,dtype=LD)
    for j in range(n):
        nj=mm[j]
        den=np.abs(mm*mm-nj*nj)
        safe=den.copy(); safe[j]=LD(1)
        col=c*(np.abs(z)*nj+abs(z[j])*mm)/safe + alpha*np.abs(p*p[j])
        diag=abs(d[j])+alpha*abs(p[j]*p[j])
        if j>=shell_start:
            diag+=LD(1)
        col[j]=diag
        row_sums+=col
        T+=col[:,None]*absW[j,:]

    Q=absW.T@T
    qmax=float(np.max(Q))
    rowmax=float(np.max(row_sums))
    out={
        "sector":sector,
        "dimension":n,
        "shell_start":shell_start,
        "Q_component_max":qmax,
        "Q_component_matrix":np.asarray(Q,dtype=float).tolist(),
        "component_row_sum_max":rowmax,
        "public_Q_component_cap_candidate":32.0,
        "cap_inflation_factor":32.0/qmax,
    }
    if not qmax<32:
        raise RuntimeError(("component magnitude cap failed",sector,qmax))
    print("\n",sector)
    print("Qcomp max =",qmax)
    print("component row max =",rowmax)
    print("cap inflation =",32.0/qmax)
    return out

def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    out={"rows":rows,"guardrail":"Positive midpoint magnitude diagnostic; public theorem cap is 32."}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
