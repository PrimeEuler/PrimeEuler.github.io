#!/usr/bin/env python3
"""Deterministic rank-24 correlated Feshbach replay for v14.041 b_nn.\n\nThis preserves the original producer but fixes ARPACK starting vector v0, so\nrepeat runs of the certificate diagnostic are reproducible. Original script\nis intentionally left untouched for provenance.\n

Let B be the exact source-faithful midpoint coupling from the certified
M=8000 shifted front into the finite near shell 8000<n<16000.

Compute a rank-r SVD
    B = U Sigma V^T + E,   r=24.

For T=V Sigma (front x r), the main self-energy is
    H_r = U (T^T F^{-1} T) U^T,
so ||H_r|| = lambda_max(M_r), M_r=T^T F^{-1}T.

M_r is evaluated with the same frozen-six-plane LDDD/Feshbach architecture
as the audited v14.033 four-channel theorem.

For the residual E, use the positive trace bound
    ||E F^{-1} E^T|| <= tr(...)
      <= ||E||_F^2/delta + tr(S^{-1}(E W)^T(E W)),
where delta is the theorem v14.031 complement floor and W,S are the refined
graph/protected Schur objects.

Finally, block PSD Cauchy-Schwarz gives
    ||B F^{-1}B^T||
      <= (sqrt(||H_r||)+sqrt(||H_E||))^2.

Diagnostic only: SVD/source formation and the rank-24 target Gram still need
outward arithmetic padding before promotion.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.sparse.linalg import cg,LinearOperator,svds

from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_M3999_frozen_p4_source_capacity_midpoint import full_source_matrix
from suzuki_M8000_mu1_full_near_triple_diagnostic import lattice, exact_cross
from suzuki_ldd_refined_capacity_bracket import (
    dd_matrix_to_mp,dd_project,mp_inverse_split,solve_correction,
)
from suzuki_ldd_source_operator import (
    LD,add as dd_add,dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,matvec as dd_matvec,
    norm2 as dd_norm2,sub as dd_sub,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_near_rank24_feshbach_deterministic_result.json"
DPS=180
RANK=24
DELTA={
 "even-v":mp.mpf("7.795385618610192746e-6"),
 "odd-v":mp.mpf("3.262507025086259604e-5"),
}
BREF={"even-v":0.18322086510504215,"odd-v":0.2033562711723558}

def shifted_matvec(data,Xh,Xl,shell_start):
    yh,yl=dd_matvec(data,Xh,Xl)
    yh=yh.copy();yl=yl.copy()
    yh[shell_start:]-=Xh[shell_start:]
    yl[shell_start:]-=Xl[shell_start:]
    return yh,yl

def mp_matrix_from_ld(A):
    A=np.asarray(A,dtype=LD)
    M=mp.matrix(A.shape[0],A.shape[1])
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            M[i,j]=mp.mpf(str(A[i,j]))
    return M

def one_sector(sector):
    base_modes,modes,P,_,_=embedded_protected_basis(sector)
    shell_start=len(base_modes);n=len(modes)

    # Exact nominal near coupling and rank-24 decomposition.
    near=lattice(sector,8001,16000)
    B=exact_cross(near,modes,sector)
    U,s,Vt=svds(B,k=RANK,which="LM",return_singular_vectors=True,
                tol=1e-11,maxiter=5000)
    order=np.argsort(s)[::-1]
    U=U[:,order];s=s[order];Vt=Vt[order,:]
    Br=(U*s[None,:])@Vt
    Eres=B-Br
    eres_fro=float(np.linalg.norm(Eres,"fro"))
    T=Vt.T*s[None,:]

    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A,_=full_source_matrix(modes,sector)
    Ash=A.copy()
    Ash[shell_start:,shell_start:]-=np.eye(n-shell_start)

    def proj(x):
        return x-P@(Gi@(P.T@x))
    def comp_mv(x):
        q=proj(np.asarray(x,dtype=float))
        return proj(Ash@q)+P@(Gi@(P.T@x))
    op=LinearOperator((n,n),matvec=comp_mv,dtype=float)

    # Graph solve.
    AP=Ash@P; Ec=proj(AP)
    Y0=np.empty_like(Ec)
    for j in range(6):
        y,info=cg(op,Ec[:,j],rtol=2e-14,atol=0.0,maxiter=30000)
        if info!=0: raise RuntimeError((sector,"graph CG",j,info))
        Y0[:,j]=proj(y)

    # Rank-24 complement target solves.
    X0=np.empty((n,RANK),dtype=float)
    init=[]
    for j in range(RANK):
        rhs=proj(T[:,j])
        x,info=cg(op,rhs,rtol=2e-14,atol=0.0,maxiter=30000)
        if info!=0: raise RuntimeError((sector,"target CG",j,info))
        x=proj(x)
        X0[:,j]=x
        init.append(float(np.linalg.norm(rhs-comp_mv(x))))

    data=hp_parity_data(modes,sector,dps=DPS,arch_terms=160,correction_terms=50)
    Yh=Y0.astype(LD);Yl=np.zeros_like(Yh,dtype=LD)
    Xh=X0.astype(LD);Xl=np.zeros_like(Xh,dtype=LD)
    Th=np.asarray(T,dtype=LD);Tl=np.zeros_like(Th,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    Xh,Xl=dd_project(P,Gih,Gil,Xh,Xl)

    def graph_res():
        Wh,Wl=dd_sub(P,np.zeros_like(P,dtype=LD),Yh,Yl)
        AWh,AWl=shifted_matvec(data,Wh,Wl,shell_start)
        Rh,Rl=dd_project(P,Gih,Gil,AWh,AWl)
        return Wh,Wl,AWh,AWl,Rh,Rl,[dd_norm2(Rh[:,j],Rl[:,j]) for j in range(6)]
    def target_res():
        AXh,AXl=shifted_matvec(data,Xh,Xl,shell_start)
        Rh,Rl=dd_sub(AXh,AXl,Th,Tl)
        Rh,Rl=dd_project(P,Gih,Gil,Rh,Rl)
        return AXh,AXl,Rh,Rl,[dd_norm2(Rh[:,j],Rl[:,j]) for j in range(RANK)]

    # One refinement, as in the validated four-channel producer.
    Wh,Wl,AWh,AWl,RYh,RYl,ny0=graph_res()
    AXh,AXl,RXh,RXl,nx0=target_res()
    for j in range(6):
        d=solve_correction(op,proj,RYh[:,j]+RYl[:,j],rtol=2e-14)
        Yh[:,j],Yl[:,j]=dd_add(Yh[:,j],Yl[:,j],d,np.zeros_like(d,dtype=LD))
    for j in range(RANK):
        d=solve_correction(op,proj,-(RXh[:,j]+RXl[:,j]),rtol=2e-14)
        Xh[:,j],Xl[:,j]=dd_add(Xh[:,j],Xl[:,j],d,np.zeros_like(d,dtype=LD))
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    Xh,Xl=dd_project(P,Gih,Gil,Xh,Xl)

    Wh,Wl,AWh,AWl,RYh,RYl,ny=graph_res()
    AXh,AXl,RXh,RXl,nx=target_res()

    Sh,Sl=dd_dot_columns(Wh,Wl,AWh,AWl)
    gh,gl=dd_dot_columns(Wh,Wl,Th,Tl)
    hh,hl=dd_dot_columns(Th,Tl,Xh,Xl)

    with mp.workdps(DPS):
        S=dd_matrix_to_mp(Sh,Sl);S=(S+S.T)/2
        g=dd_matrix_to_mp(gh,gl)
        h=dd_matrix_to_mp(hh,hl);h=(h+h.T)/2
        Sinvg=mp.matrix(6,RANK)
        for j in range(RANK):
            sol=mp.lu_solve(S,g[:,j])
            for i in range(6): Sinvg[i,j]=sol[i]
        M=h+g.T*Sinvg;M=(M+M.T)/2
        vals,_=mp.eigsy(M)
        bmain=max(vals)

        # Residual self-energy trace bound.
        W=np.asarray(Wh+Wl,dtype=LD)
        EW=np.asarray(Eres,dtype=LD)@W
        EWtEW=mp_matrix_from_ld(EW.T@EW)
        Sinv=S**-1
        prot=mp.fsum(Sinv[i,j]*EWtEW[j,i] for i in range(6) for j in range(6))
        comp=mp.mpf(str(eres_fro))**2/DELTA[sector]
        eres_energy=max(mp.mpf("0"),comp+prot)
        btotal=(mp.sqrt(max(mp.mpf("0"),bmain))+mp.sqrt(eres_energy))**2

    row={
      "sector":sector,"rank":RANK,
      "near_dimension":len(near),
      "singular_values":[float(x) for x in s],
      "residual_fro_explicit":eres_fro,
      "max_initial_target_residual":max(init),
      "max_ldd_target_residual_before":max(nx0),
      "max_ldd_target_residual_after":max(nx),
      "max_graph_residual_after":max(ny),
      "main_gram_lambda_max":mp.nstr(bmain,60),
      "residual_complement_energy_upper":mp.nstr(comp,50),
      "residual_protected_trace_midpoint":mp.nstr(prot,50),
      "residual_self_energy_trace_upper_midpoint_inputs":mp.nstr(eres_energy,50),
      "combined_psd_cs_bound":mp.nstr(btotal,60),
      "independent_full_b_midpoint_reference":BREF[sector],
      "ratio_to_reference":float(btotal/mp.mpf(str(BREF[sector]))),
      "public_target_b_nn":0.25,
      "below_025_midpoint_inputs":bool(btotal<mp.mpf("0.25")),
      "guardrail":(
        "Correlation-preserving rank-24 diagnostic. Outward promotion must "
        "charge SVD decomposition/source formation, target residuals, exact "
        "front perturbation and residual EW arithmetic."
      )
    }
    print("\n",json.dumps(row,indent=2))
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    row=one_sector(a.sector)
    OUT.write_text(json.dumps({"rows":[row]},indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
