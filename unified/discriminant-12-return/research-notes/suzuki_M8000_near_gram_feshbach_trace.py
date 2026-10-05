#!/usr/bin/env python3
"""Correlated Feshbach trace bound for the v14.041 near Gram.

For F = certified M8000, mu=1 front and B = exact front-to-near coupling,

    H = B F^{-1} B^* >= 0,
    b_nn = ||H|| <= tr(H).

Using the frozen six-plane P, Euclidean Q projector, graph W=P-Y and protected
Schur S=W^* F W,

    tr(H)
      = tr(B_Q F_qq^{-1} B_Q^*) + tr(S^{-1} G^*G),
        G = B W,

hence

    tr(H)
      <= ||Q B^*||_F^2 / delta + tr(S^{-1} G^*G),

where delta is the theorem-level v14.031 complement floor.

This script evaluates that correlated decomposition with the same refined
LDDD graph W used by v14.034.  It is a diagnostic producer: the ledger still
must add outward arithmetic/source charges before promoting a public trace cap.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import mpmath as mp
import numpy as np

from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_M3999_frozen_p4_source_capacity_midpoint import full_source_matrix
from suzuki_M8000_mu1_full_near_triple_diagnostic import lattice, exact_cross
from suzuki_ldd_refined_capacity_bracket import (
    dd_matrix_to_mp, dd_project, mp_inverse_split, solve_correction,
)
from suzuki_ldd_source_operator import (
    LD, add as dd_add, dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data, matvec as dd_matvec,
    sub as dd_sub,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_near_gram_feshbach_trace_result.json"
DPS=180
DELTA={
 "even-v":mp.mpf("7.795385618610192746e-6"),
 "odd-v":mp.mpf("3.262507025086259604e-5"),
}
TRACE_REF={"even-v":0.33855199236977396,"odd-v":0.39609381086028483}

def shifted_matvec(data,Xh,Xl,shell_start):
    yh,yl=dd_matvec(data,Xh,Xl)
    yh=yh.copy(); yl=yl.copy()
    yh[shell_start:]-=Xh[shell_start:]
    yl[shell_start:]-=Xl[shell_start:]
    return yh,yl

def graph_state(sector):
    base_modes,modes,P,_,_=embedded_protected_basis(sector)
    shell_start=len(base_modes)
    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A,_=full_source_matrix(modes,sector)
    H=A.copy()
    idx=np.arange(shell_start,len(modes))
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
        if info!=0: raise RuntimeError((sector,"graph CG",j,info))
        Y0[:,j]=proj(y)

    data=hp_parity_data(modes,sector,dps=DPS,arch_terms=160,correction_terms=50)
    Yh=Y0.astype(LD); Yl=np.zeros_like(Yh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)

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
    HWh,HWl=shifted_matvec(data,Wh,Wl,shell_start)

    Sh,Sl=dd_dot_columns(Wh,Wl,HWh,HWl)
    with mp.workdps(DPS):
        S=dd_matrix_to_mp(Sh,Sl)
        S=(S+S.T)/2
    return modes,P,Gi,Wh,Wl,S

def mp_from_ld_matrix(A):
    A=np.asarray(A,dtype=LD)
    M=mp.matrix(A.shape[0],A.shape[1])
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            M[i,j]=mp.mpf(str(A[i,j]))
    return M

def one_sector(sector):
    modes,P,Gi,Wh,Wl,S=graph_state(sector)
    near=lattice(sector,8001,16000)
    B=exact_cross(near,modes,sector)

    # Orthogonal projection identity:
    # ||Q B^T||_F^2 = ||B||_F^2 - tr(Gi (BP)^T(BP)).
    BP=B@P
    Bf2=LD(np.sum(np.asarray(B,dtype=LD)**2,dtype=LD))
    Mpt=np.asarray(BP,dtype=LD).T@np.asarray(BP,dtype=LD)
    GiLD=np.asarray(Gi,dtype=LD)
    captured=LD(np.trace(GiLD@Mpt))
    qf2=max(LD(0),Bf2-captured)

    # Correlated graph target. Long-double multiply preserves the small
    # B(P-Y) cancellation substantially better than binary64.
    W=np.asarray(Wh+Wl,dtype=LD)
    G=np.asarray(B,dtype=LD)@W
    GtG=np.asarray(G.T@G,dtype=LD)

    with mp.workdps(DPS):
        GG=mp_from_ld_matrix(GtG)
        Sinv=S**-1
        protected=mp.fsum(
            Sinv[i,j]*GG[j,i]
            for i in range(6) for j in range(6)
        )
        complement=mp.mpf(str(qf2))/DELTA[sector]
        upper=complement+protected

    row={
      "sector":sector,
      "near_dimension":len(near),
      "B_fro_sq_midpoint":str(Bf2),
      "P_captured_fro_sq_midpoint":str(captured),
      "QBstar_fro_sq_midpoint":str(qf2),
      "complement_trace_upper_using_certified_delta":mp.nstr(complement,60),
      "protected_trace_midpoint":mp.nstr(protected,60),
      "feshbach_trace_upper_midpoint_inputs":mp.nstr(upper,60),
      "independent_structured_trace_reference":TRACE_REF[sector],
      "ratio_to_reference":float(upper/mp.mpf(str(TRACE_REF[sector]))),
      "public_target_trace_cap":0.5,
      "below_public_target_midpoint_inputs":bool(upper<mp.mpf("0.5")),
      "guardrail":(
        "Certified delta is consumed, but B/source formation, graph W and "
        "6x6 protected trace still use midpoint/LDDD values. This establishes "
        "a correlated outward-certification target, not yet a theorem."
      )
    }
    print("\n",json.dumps(row,indent=2))
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    args=ap.parse_args()
    row=one_sector(args.sector)
    OUT.write_text(json.dumps({"rows":[row]},indent=2,sort_keys=True)+"\n")
    print("wrote",OUT)

if __name__=="__main__":
    main()
