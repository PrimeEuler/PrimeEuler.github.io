#!/usr/bin/env python3
"""Finite-64k Schur K diagnostic for the N=32000 paired remote problem.

For each parity, solve the full finite A_{<=64000} problem with RHS g that is
zero on modes <=32000 and equals the paired u_j=1/n_j on the remote near
block.  The remote block of A^{-1}g is exactly the finite Schur inverse
w_p = S_{p,32k}^{(64k)-1} u.

We never form S explicitly.  Using the frozen six-plane graph/Feshbach
decomposition with one LDDD refinement:
    A^{-1} = C_Q^{-1} + W S_P^{-1} W^T
on the complement/protected splitting, hence
    K_p = <g,A^{-1}g>
        = <g,C_Q^{-1}Qg> + (W^T g)^T S_P^{-1}(W^T g).

Once both parity K values are available, the paired finite-Schur remainder is
    <w_o,Rosc w_e> = K_e - K_o - C_S K_o K_e
under DeltaS=S_o-S_e=C_S u u^T + Rosc.

Diagnostic only: finite cutoff 64k, midpoint source arithmetic.  It does
include the finite-front Schur correction exactly within that cutoff.
"""
from __future__ import annotations
import argparse, json
import mpmath as mp
import numpy as np
from scipy.sparse.linalg import cg

from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import embedded_P,modes_for
from suzuki_full_fft_fixed_capacity_replay import fixed_operator,DPS,ARCH
from suzuki_ldd_refined_capacity_bracket import (
    dd_project,dd_matrix_to_mp,mp_inverse_split,solve_correction
)
from suzuki_ldd_source_operator import (
    LD,add as dd_add,dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,matvec as dd_matvec,
    norm2 as dd_norm2,sub as dd_sub,
)

N=32000
MAXMODE=64000

def graph_residual(data,P,Gih,Gil,Yh,Yl):
    Wh,Wl=dd_sub(P,np.zeros_like(P,dtype=LD),Yh,Yl)
    AWh,AWl=dd_matvec(data,Wh,Wl)
    Rh,Rl=dd_project(P,Gih,Gil,AWh,AWl)
    norms=[dd_norm2(Rh[:,j],Rl[:,j]) for j in range(6)]
    return Wh,Wl,AWh,AWl,Rh,Rl,norms

def target_residual(data,P,Gih,Gil,xh,xl,gh,gl):
    Axh,Axl=dd_matvec(data,xh,xl)
    rh,rl=dd_sub(Axh,Axl,gh,gl)
    rh,rl=dd_project(P,Gih,Gil,rh,rl)
    return Axh,Axl,rh,rl,dd_norm2(rh,rl)

def one(sector):
    modes=modes_for(sector,MAXMODE)
    P=embedded_P(sector,modes)

    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    raw_mv,proj,op,_=fixed_operator(modes,sector,P,Gi)
    E=proj(raw_mv(P))

    # Graph solve CY=E.
    Y0=np.empty_like(E)
    git=[]
    for j in range(6):
        cnt=[0]
        y,info=cg(op,E[:,j],rtol=2e-14,atol=0.0,maxiter=30000,
                  callback=lambda _:cnt.__setitem__(0,cnt[0]+1))
        if info!=0: raise RuntimeError((sector,"graph",j,info))
        Y0[:,j]=proj(y);git.append(cnt[0])

    # Paired remote RHS.
    g=np.zeros(len(modes),dtype=float)
    mask=modes>N
    if sector=="even-v":
        g[mask]=1.0/modes[mask].astype(float)
    else:
        g[mask]=1.0/(modes[mask].astype(float)-1.0)
    rhs=proj(g)
    cnt=[0]
    q0,info=cg(op,rhs,rtol=2e-14,atol=0.0,maxiter=30000,
               callback=lambda _:cnt.__setitem__(0,cnt[0]+1))
    if info!=0: raise RuntimeError((sector,"target",info))
    q0=proj(q0)

    data=hp_parity_data(modes,sector,dps=DPS,arch_terms=ARCH,correction_terms=50)
    Yh=Y0.astype(LD);Yl=np.zeros_like(Yh,dtype=LD)
    qh=q0.astype(LD);ql=np.zeros_like(qh,dtype=LD)
    gh=g.astype(LD);gl=np.zeros_like(gh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    qh,ql=dd_project(P,Gih,Gil,qh,ql)

    Wh,Wl,AWh,AWl,RYh,RYl,rY0=graph_residual(data,P,Gih,Gil,Yh,Yl)
    Aqh,Aql,Rqh,Rql,rq0=target_residual(data,P,Gih,Gil,qh,ql,gh,gl)

    # One LDDD-driven correction using the same fixed complement solver.
    for j in range(6):
        delta=solve_correction(op,proj,RYh[:,j]+RYl[:,j],rtol=2e-14)
        Yh[:,j],Yl[:,j]=dd_add(
            Yh[:,j],Yl[:,j],delta,np.zeros_like(delta,dtype=LD)
        )
    delta=solve_correction(op,proj,-(Rqh+Rql),rtol=2e-14)
    qh,ql=dd_add(qh,ql,delta,np.zeros_like(delta,dtype=LD))
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    qh,ql=dd_project(P,Gih,Gil,qh,ql)

    Wh,Wl,AWh,AWl,RYh,RYl,rY1=graph_residual(data,P,Gih,Gil,Yh,Yl)
    Aqh,Aql,Rqh,Rql,rq1=target_residual(data,P,Gih,Gil,qh,ql,gh,gl)

    Sh,Sl=dd_dot_columns(Wh,Wl,AWh,AWl)
    bh,bl=dd_dot_columns(Wh,Wl,gh[:,None],gl[:,None])
    hh,hl=dd_dot_columns(gh[:,None],gl[:,None],qh[:,None],ql[:,None])

    with mp.workdps(DPS):
        S=dd_matrix_to_mp(Sh,Sl); S=(S+S.T)/2
        b=dd_matrix_to_mp(bh,bl)
        h=dd_matrix_to_mp(hh,hl)[0,0]
        a=mp.lu_solve(S,b)
        protected=(b.T*a)[0]
        K=h+protected
        vals,_=mp.eigsy(S)

    row={
      "sector":sector,
      "maxmode":MAXMODE,
      "dimension":len(modes),
      "remote_dimension":int(np.sum(mask)),
      "graph_cg_iters":git,
      "target_cg_iters":cnt[0],
      "graph_ldd_residual_before":max(rY0),
      "graph_ldd_residual_after":max(rY1),
      "target_ldd_residual_before":rq0,
      "target_ldd_residual_after":rq1,
      "protected_S_min":mp.nstr(vals[0],50),
      "K_complement":mp.nstr(h,70),
      "K_protected":mp.nstr(protected,70),
      "K_total":mp.nstr(K,70),
      "guardrail":"finite-64k midpoint diagnostic; not outward/infinite-tail theorem"
    }
    print(json.dumps(row,indent=2),flush=True)
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    one(a.sector)

if __name__=="__main__":
    main()

# anchor-export trigger: no mathematical change
# git-ref trigger: no mathematical change\n