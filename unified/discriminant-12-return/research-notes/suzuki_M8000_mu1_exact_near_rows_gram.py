#!/usr/bin/env python3
"""Exact correlated Gram for the first near-boundary far rows at M=8000, mu=1.

For the certified shifted finite front F, let b_n be the exact source-faithful
coupling row from front modes m<=8000 to one far mode n>8000.

This script computes, for the first R same-parity far modes,

    G_ij = b_{n_i}^* F^{-1} b_{n_j}

using the same frozen-P4 protected/complement Feshbach architecture as
v14.033.  This preserves the near-null correlation and never uses ||F^-1||.

The largest eigenvalue of this finite principal Gram is a lower diagnostic on
this exact near-boundary contribution and is replayed only after the workflow
exists on the branch.  It is a lower diagnostic on
the exact near-shell Schur correction norm.  It is not an upper certificate
for the full shell.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.sparse.linalg import cg, LinearOperator

from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_M3999_frozen_p4_source_capacity_midpoint import full_source_matrix
from suzuki_ldd_refined_capacity_bracket import (
    dd_matrix_to_mp, dd_project, mp_inverse_split, solve_correction,
)
from suzuki_ldd_source_operator import (
    LD, add as dd_add, dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data, ldd_to_mpf, split_mpf_ld,
    matvec as dd_matvec, norm2 as dd_norm2, sub as dd_sub,
)
from suzuki_ldd_remote_source_lead_diagnostic import z_remote_mp, pole_mp

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_mu1_exact_near_rows_gram_result.json"
DPS=180
RCOUNT=16  # replay trigger after workflow installation

def shifted_data_matvec(data,xh,xl,shell_start):
    yh,yl=dd_matvec(data,xh,xl)
    yh=yh.copy(); yl=yl.copy()
    yh[shell_start:]-=xh[shell_start:]
    yl[shell_start:]-=xl[shell_start:]
    return yh,yl

def exact_targets_dd(data,modes,sector,ns):
    r=len(ns); n=len(modes)
    Bh=np.empty((n,r),dtype=LD); Bl=np.empty((n,r),dtype=LD)
    with mp.workdps(DPS):
        c=mp.mpf(2)/mp.pi
        alpha=mp.mpf(2 if sector=="even-v" else -2)
        mm=[mp.mpf(int(x)) for x in modes]
        zm=[ldd_to_mpf(data.z_hi[i],data.z_lo[i]) for i in range(n)]
        pm=[ldd_to_mpf(data.pole_hi[i],data.pole_lo[i]) for i in range(n)]
        for j,n0 in enumerate(ns):
            nn=mp.mpf(int(n0))
            zn=z_remote_mp(int(n0))
            pn=pole_mp(int(n0),sector)
            for i,m in enumerate(mm):
                v=c*(zn*m-nn*zm[i])/(nn*nn-m*m)+alpha*pn*pm[i]
                Bh[i,j],Bl[i,j]=split_mpf_ld(v)
    return Bh,Bl

def one_sector(sector):
    base_modes,modes,P,_,_=embedded_protected_basis(sector)
    shell_start=len(base_modes)
    n=len(modes)
    start=int(modes[-1])+2
    ns=np.arange(start,start+2*RCOUNT,2,dtype=int)

    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A,_=full_source_matrix(modes,sector)
    Ash=A.copy()
    Ash[shell_start:,shell_start:]-=np.eye(n-shell_start)
    data=hp_parity_data(modes,sector,dps=DPS,arch_terms=160,correction_terms=50)
    Bh,Bl=exact_targets_dd(data,modes,sector,ns)
    Bfloat=np.asarray(Bh+Bl,dtype=float)

    def proj(x):
        return x-P@(Gi@(P.T@x))
    def comp_mv(x):
        q=proj(np.asarray(x,dtype=float))
        return proj(Ash@q)+P@(Gi@(P.T@x))
    op=LinearOperator((n,n),matvec=comp_mv,dtype=float)

    AP=Ash@P
    E=proj(AP)
    Y0=np.empty_like(E)
    for j in range(6):
        y,info=cg(op,E[:,j],rtol=2e-14,atol=0,maxiter=30000)
        if info!=0: raise RuntimeError((sector,"graph",j,info))
        Y0[:,j]=proj(y)

    X0=np.empty((n,RCOUNT),dtype=float)
    init=[]
    for j in range(RCOUNT):
        rhs=proj(Bfloat[:,j])
        x,info=cg(op,rhs,rtol=2e-14,atol=0,maxiter=30000)
        if info!=0: raise RuntimeError((sector,"target",j,info))
        x=proj(x); X0[:,j]=x
        init.append(float(np.linalg.norm(rhs-comp_mv(x))))

    Yh=Y0.astype(LD); Yl=np.zeros_like(Yh,dtype=LD)
    Xh=X0.astype(LD); Xl=np.zeros_like(Xh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    Xh,Xl=dd_project(P,Gih,Gil,Xh,Xl)

    def graph_res():
        Wh,Wl=dd_sub(P,np.zeros_like(P,dtype=LD),Yh,Yl)
        AWh,AWl=shifted_data_matvec(data,Wh,Wl,shell_start)
        Rh,Rl=dd_project(P,Gih,Gil,AWh,AWl)
        return Wh,Wl,AWh,AWl,Rh,Rl,[dd_norm2(Rh[:,j],Rl[:,j]) for j in range(6)]
    def target_res():
        AXh,AXl=shifted_data_matvec(data,Xh,Xl,shell_start)
        Rh,Rl=dd_sub(AXh,AXl,Bh,Bl)
        Rh,Rl=dd_project(P,Gih,Gil,Rh,Rl)
        return AXh,AXl,Rh,Rl,[dd_norm2(Rh[:,j],Rl[:,j]) for j in range(RCOUNT)]

    for step in range(2):
        Wh,Wl,AWh,AWl,RYh,RYl,ny=graph_res()
        AXh,AXl,RXh,RXl,nx=target_res()
        print(sector,"step",step,"graph",max(ny),"target",max(nx))
        if step==0:
            for j in range(6):
                delta=solve_correction(op,proj,RYh[:,j]+RYl[:,j],rtol=2e-14)
                Yh[:,j],Yl[:,j]=dd_add(Yh[:,j],Yl[:,j],
                    delta,np.zeros_like(delta,dtype=LD))
            for j in range(RCOUNT):
                delta=solve_correction(op,proj,-(RXh[:,j]+RXl[:,j]),rtol=2e-14)
                Xh[:,j],Xl[:,j]=dd_add(Xh[:,j],Xl[:,j],
                    delta,np.zeros_like(delta,dtype=LD))
            Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
            Xh,Xl=dd_project(P,Gih,Gil,Xh,Xl)

    Wh,Wl,AWh,AWl,RYh,RYl,ny=graph_res()
    AXh,AXl,RXh,RXl,nx=target_res()

    Sh,Sl=dd_dot_columns(Wh,Wl,AWh,AWl)
    gh,gl=dd_dot_columns(Wh,Wl,Bh,Bl)
    hh,hl=dd_dot_columns(Bh,Bl,Xh,Xl)
    with mp.workdps(DPS):
        S=dd_matrix_to_mp(Sh,Sl); S=(S+S.T)/2
        g=dd_matrix_to_mp(gh,gl)
        h=dd_matrix_to_mp(hh,hl); h=(h+h.T)/2
        Sinvg=mp.matrix(6,RCOUNT)
        for j in range(RCOUNT):
            sol=mp.lu_solve(S,g[:,j])
            for i in range(6): Sinvg[i,j]=sol[i]
        G=h+g.T*Sinvg; G=(G+G.T)/2
        vals,_=mp.eigsy(G)
        diag=[G[j,j] for j in range(RCOUNT)]
        return {
          "sector":sector,
          "remote_modes":[int(x) for x in ns],
          "initial_target_residual_max":max(init),
          "final_graph_residual_max":max(ny),
          "final_target_residual_max":max(nx),
          "gram_eigenvalues":[mp.nstr(vals[j],50) for j in range(RCOUNT)],
          "gram_lambda_max":mp.nstr(vals[RCOUNT-1],60),
          "gram_trace":mp.nstr(mp.fsum(diag),60),
          "diagonal_energies":[mp.nstr(v,40) for v in diag],
        }

def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    out={
      "rows":rows,
      "guardrail":(
        "Finite principal correlated Gram diagnostic. lambda_max is a lower "
        "diagnostic for the full near-shell correction norm, not an upper bound."
      )
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    for r in rows:
        print("\n",r["sector"],"lambda max",r["gram_lambda_max"],
              "trace",r["gram_trace"])
    print("wrote",OUT)

if __name__=="__main__":
    main()
