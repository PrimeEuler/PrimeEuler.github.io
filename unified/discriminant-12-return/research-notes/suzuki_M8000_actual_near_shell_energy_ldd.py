#!/usr/bin/env python3
"""Direct LDDD/Feshbach energy of the actual N=4000 -> M=8000 shell residual.

For the N=4000 Galerkin source solution x_N, form the exact represented shell
residual
    r_Q = f_Q - B x_N
on 4000<n<=8000.  Embed b=(0,r_Q) in the M=8000 space and evaluate
    H_shell = b^T A_M^{-1} b = r_Q^T S^{-1} r_Q
through the frozen-six-plane LDDD/Feshbach solver.

Then
    eta_shell = C_N H_shell
must equal the nested finite-section correction C_N/C_M-1 for the same
represented operator.  This is the correlation-preserving near-shell object
required by v14.017/v14.047.

Midpoint diagnostic first.  Residual-Gram data and theorem complement floors
are reported so the same producer can be upgraded to an outward interval.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.sparse.linalg import cg

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis, full_source_matrix,
)
from suzuki_N4000_far_geometric_remainder_diagnostic import reconstruct_source
from suzuki_ldd_M11_direct_difference import (
    generic_residuals, generic_Ktilde, energy_from_K,
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement, dd_project, form_trial, mp_inverse_split,
    residual_gram_mp,
)
from suzuki_ldd_source_operator import (
    LD, add as dd_add, dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data, ldd_to_mpf,
    matvec as dd_matvec, split_mpf_ld, sub as dd_sub,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_actual_near_shell_energy_ldd_result.json"
N=4000
M=8000
DPS=180

# Fresh arch-160 midpoint capacities from successful current-code replays.
CM={
 "even-v":mp.mpf("7.52720430896005992680627889508998548359678187022160231662354e-30"),
 "odd-v": mp.mpf("2.17002938184649282297034949985322034115574187993309818036262e-25"),
}

# Theorem lower floors inherited from v14.031 shifted front; unshifted A is
# larger by +Pi_shell, so these remain valid for the same frozen Q-space.
DELTA_Q={
 "even-v":mp.mpf("7.795385618610192746e-6"),
 "odd-v": mp.mpf("3.262507025086259604e-5"),
}

def modes_for(sector,maxmode):
    return np.arange(1 if sector=="even-v" else 2,maxmode+1,2,dtype=int)

def actual_shell_rhs(sector):
    state=reconstruct_source(sector)
    modesM=modes_for(sector,M)
    nN=len(state["modes"])
    dataM=hp_parity_data(modesM,sector,dps=DPS,arch_terms=160,correction_terms=50)

    xh=np.zeros(len(modesM),dtype=LD)
    xl=np.zeros(len(modesM),dtype=LD)
    for i,x in enumerate(state["xmp"]):
        xh[i],xl[i]=split_mpf_ld(x)

    Axh,Axl=dd_matvec(dataM,xh,xl)
    bh,bl=dd_sub(dataM.source_hi,dataM.source_lo,Axh,Axl)

    # Exact block RHS is (0,r_Q).  Retained residual is finite-solve noise and
    # must not be reintroduced as part of the shell correction.
    bh[:nN]=LD(0); bl[:nN]=LD(0)

    return state,modesM,dataM,bh,bl,nN

def one_sector(sector):
    state,modes,data,bh,bl,nN=actual_shell_rhs(sector)
    P,_=frozen_protected_basis(sector,modes)

    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A,_=full_source_matrix(modes,sector)
    bfloat=np.array([float(ldd_to_mpf(bh[i],bl[i])) for i in range(len(modes))])
    op,proj,gamma,evals,Y0,yb0,initial=build_double_complement(
        A,P,Gi,bfloat,rtol=2e-14
    )

    Yh=Y0.astype(LD); Yl=np.zeros_like(Yh,dtype=LD)
    ybh=yb0.astype(LD); ybl=np.zeros_like(ybh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    ybh,ybl=dd_project(P,Gih,Gil,ybh,ybl)

    history=[]
    for step in range(2):
        Uh,Ul=form_trial(P,Yh,Yl,ybh,ybl)
        AUh,AUl,Rh,Rl,norms=generic_residuals(
            data,P,Gih,Gil,Uh,Ul,bh,bl
        )
        history.append(norms)
        print(sector,"refinement",step,"max residual",max(norms))
        if step==0:
            for j in range(6):
                rhs=Rh[:,j]+Rl[:,j]
                d,info=cg(op,rhs,rtol=2e-14,atol=0.0,maxiter=30000)
                if info!=0: raise RuntimeError((sector,"coupling",j,info))
                d=proj(d)
                Yh[:,j],Yl[:,j]=dd_add(
                    Yh[:,j],Yl[:,j],d,np.zeros_like(d,dtype=LD)
                )
            rhs=-(Rh[:,6]+Rl[:,6])
            d,info=cg(op,rhs,rtol=2e-14,atol=0.0,maxiter=30000)
            if info!=0: raise RuntimeError((sector,"rhs",info))
            d=proj(d)
            ybh,ybl=dd_add(ybh,ybl,d,np.zeros_like(d,dtype=LD))
            Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
            ybh,ybl=dd_project(P,Gih,Gil,ybh,ybl)

    K=generic_Ktilde(Uh,Ul,AUh,AUl,bh,bl,DPS)
    RR=residual_gram_mp(Rh,Rl,DPS)

    with mp.workdps(DPS):
        H=energy_from_K(K)
        Cn=state["C"]
        eta=Cn*H
        eta_ref=Cn/CM[sector]-1
        rrmax=max(mp.eigsy(RR)[0])
        qerr=rrmax/DELTA_Q[sector]
        eta_qerr=Cn*qerr

        # Shell-RHS represented norm; useful for later exact-source perturbation.
        br2=mp.fsum(
            ldd_to_mpf(bh[i],bl[i])**2 for i in range(nN,len(modes))
        )
        row={
          "sector":sector,
          "dimension_M":len(modes),
          "shell_dimension":len(modes)-nN,
          "C_N_reconstructed":mp.nstr(Cn,70),
          "C_M_reference":mp.nstr(CM[sector],70),
          "H_shell_midpoint":mp.nstr(H,70),
          "eta_shell_midpoint":mp.nstr(eta,70),
          "eta_nested_capacity_reference":mp.nstr(eta_ref,70),
          "eta_mid_minus_reference":mp.nstr(eta-eta_ref,50),
          "shell_rhs_l2":mp.nstr(mp.sqrt(br2),50),
          "complement_floor_midpoint":gamma,
          "theorem_Q_floor_used_for_error":mp.nstr(DELTA_Q[sector],30),
          "residual_history":history,
          "residual_gram_norm":mp.nstr(rrmax,50),
          "quadratic_residual_error_upper":mp.nstr(qerr,50),
          "eta_residual_error_upper":mp.nstr(eta_qerr,50),
        }
    print("\n",sector)
    for k,v in row.items():
        if k not in ("sector","residual_history"): print(k,"=",v)
    return row

def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    with mp.workdps(DPS):
        de=mp.mpf(rows[0]["eta_shell_midpoint"])
        do=mp.mpf(rows[1]["eta_shell_midpoint"])
        re=mp.mpf(rows[0]["eta_nested_capacity_reference"])
        ro=mp.mpf(rows[1]["eta_nested_capacity_reference"])
        pair={
          "eta_odd_minus_even_midpoint":mp.nstr(do-de,70),
          "eta_odd_minus_even_nested_reference":mp.nstr(ro-re,70),
          "difference_between_pair_values":mp.nstr((do-de)-(ro-re),50),
        }
    out={"rows":rows,"paired":pair,
         "guardrail":"Midpoint correlated near-shell producer; exact-source/LDDD outward form budget pending."}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nPAIRED")
    for k,v in pair.items(): print(k,"=",v)
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
