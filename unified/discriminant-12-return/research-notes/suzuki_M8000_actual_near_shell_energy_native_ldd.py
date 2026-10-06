#!/usr/bin/env python3
"""Native-LDDD N=4000 -> M=8000 near-shell energy replay.

This repairs the diagnostic weakness of
  suzuki_M8000_actual_near_shell_energy_ldd.py:
that script reconstructed x_N as arbitrary-precision scalars and then split
the huge near-null source vector back into longdouble pairs before forming
the M=8000 shell RHS.  The re-split loses the carefully preserved seven-column
LDDD cancellation.

Here x_N remains a native hi/lo LDDD linear combination from the N=4000
refined trial basis all the way into the M=8000 matvec.

For the same represented arch-160 operator, the exact nested identity is
    eta_{N->M} = C_N/C_M - 1.
Agreement with that identity is the primary validation gate.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.sparse.linalg import cg

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis, full_source_matrix,
)
from suzuki_ldd_M11_direct_difference import (
    generic_residuals, generic_Ktilde, energy_from_K,
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement, dd_project, form_Ktilde, form_trial,
    mp_inverse_split, refine_once, residual_gram_mp, residuals_dd,
)
from suzuki_ldd_remote_source_lead_diagnostic import dd_linear_combination
from suzuki_ldd_source_operator import (
    LD, add as dd_add, dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data, ldd_to_mpf,
    sub as dd_sub,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_actual_near_shell_energy_native_ldd_result.json"
N=4000
M=8000
DPS=180

CM={
 "even-v":mp.mpf("7.52720430896005992680627889508998548359678187022160231662354e-30"),
 "odd-v": mp.mpf("2.17002938184649282297034949985322034115574187993309818036262e-25"),
}
DELTA_Q={
 "even-v":mp.mpf("7.795385618610192746e-6"),
 "odd-v": mp.mpf("3.262507025086259604e-5"),
}

def modes_for(sector,maxmode):
    return np.arange(1 if sector=="even-v" else 2,maxmode+1,2,dtype=int)

def native_source_N(sector):
    modes=modes_for(sector,N)
    P,_=frozen_protected_basis(sector,modes)
    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A,f=full_source_matrix(modes,sector)
    op,proj,gamma,evals,Y0,yf0,initial=build_double_complement(
        A,P,Gi,f,rtol=2e-14
    )
    data=hp_parity_data(
        modes,sector,dps=DPS,arch_terms=160,correction_terms=50
    )
    Yh=Y0.astype(LD);Yl=np.zeros_like(Yh,dtype=LD)
    yfh=yf0.astype(LD);yfl=np.zeros_like(yfh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    yfh,yfl=dd_project(P,Gih,Gil,yfh,yfl)

    Uh,Ul=form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,n0=residuals_dd(data,P,Gih,Gil,Uh,Ul)
    Yh,Yl,yfh,yfl=refine_once(op,proj,Yh,Yl,yfh,yfl,Rh,Rl)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    yfh,yfl=dd_project(P,Gih,Gil,yfh,yfl)

    Uh,Ul=form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,n1=residuals_dd(data,P,Gih,Gil,Uh,Ul)
    Kt=form_Ktilde(data,Uh,Ul,AUh,AUl,DPS)
    with mp.workdps(DPS):
        S=Kt[:6,:6];g=-Kt[:6,6];h=-Kt[6,6]
        w=mp.lu_solve(S,g)
        G=h+(g.T*w)[0]
        C=1/G
        coeffs=[w[j] for j in range(6)]+[mp.mpf(1)]
    xh,xl=dd_linear_combination(Uh,Ul,coeffs)
    return modes,C,xh,xl,max(n1)

def shell_rhs_native(sector):
    modesN,Cn,xNh,xNl,resN=native_source_N(sector)
    modesM=modes_for(sector,M)
    nN=len(modesN)
    dataM=hp_parity_data(
        modesM,sector,dps=DPS,arch_terms=160,correction_terms=50
    )
    xh=np.zeros(len(modesM),dtype=LD)
    xl=np.zeros(len(modesM),dtype=LD)
    xh[:nN]=xNh; xl[:nN]=xNl

    from suzuki_ldd_source_operator import matvec as dd_matvec
    Axh,Axl=dd_matvec(dataM,xh,xl)
    bh,bl=dd_sub(dataM.source_hi,dataM.source_lo,Axh,Axl)
    bh[:nN]=LD(0);bl[:nN]=LD(0)
    return modesM,dataM,Cn,bh,bl,nN,resN

def one_sector(sector):
    modes,data,Cn,bh,bl,nN,resN=shell_rhs_native(sector)
    P,_=frozen_protected_basis(sector,modes)
    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A,_=full_source_matrix(modes,sector)
    bfloat=np.asarray(bh+bl,dtype=float)
    op,proj,gamma,evals,Y0,yb0,initial=build_double_complement(
        A,P,Gi,bfloat,rtol=2e-14
    )
    Yh=Y0.astype(LD);Yl=np.zeros_like(Yh,dtype=LD)
    ybh=yb0.astype(LD);ybl=np.zeros_like(ybh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    ybh,ybl=dd_project(P,Gih,Gil,ybh,ybl)

    history=[]
    for step in range(2):
        Uh,Ul=form_trial(P,Yh,Yl,ybh,ybl)
        AUh,AUl,Rh,Rl,norms=generic_residuals(
            data,P,Gih,Gil,Uh,Ul,bh,bl
        )
        history.append(norms)
        if step==0:
            for j in range(6):
                d,info=cg(op,Rh[:,j]+Rl[:,j],rtol=2e-14,atol=0,maxiter=30000)
                if info!=0: raise RuntimeError((sector,"coupling",j,info))
                d=proj(d)
                Yh[:,j],Yl[:,j]=dd_add(
                    Yh[:,j],Yl[:,j],d,np.zeros_like(d,dtype=LD)
                )
            d,info=cg(op,-(Rh[:,6]+Rl[:,6]),rtol=2e-14,atol=0,maxiter=30000)
            if info!=0: raise RuntimeError((sector,"rhs",info))
            d=proj(d)
            ybh,ybl=dd_add(ybh,ybl,d,np.zeros_like(d,dtype=LD))
            Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
            ybh,ybl=dd_project(P,Gih,Gil,ybh,ybl)

    K=generic_Ktilde(Uh,Ul,AUh,AUl,bh,bl,DPS)
    RR=residual_gram_mp(Rh,Rl,DPS)
    with mp.workdps(DPS):
        H=energy_from_K(K)
        eta=Cn*H
        eta_ref=Cn/CM[sector]-1
        rrmax=max(mp.eigsy(RR)[0])
        qerr=rrmax/DELTA_Q[sector]
        row={
          "sector":sector,
          "C_N_native":mp.nstr(Cn,70),
          "C_M_reference":mp.nstr(CM[sector],70),
          "eta_shell_native":mp.nstr(eta,70),
          "eta_nested_reference":mp.nstr(eta_ref,70),
          "eta_difference":mp.nstr(eta-eta_ref,60),
          "relative_identity_defect":mp.nstr(
              abs(eta-eta_ref)/max(abs(eta_ref),mp.mpf("1e-300")),50
          ),
          "N_source_joint_residual_max":resN,
          "M_shell_residual_history":history,
          "M_shell_residual_gram_norm":mp.nstr(rrmax,50),
          "M_shell_quadratic_residual_energy_bound":mp.nstr(qerr,50),
          "M_shell_eta_quadratic_residual_bound":mp.nstr(Cn*qerr,50),
          "shell_rhs_l2":mp.nstr(mp.sqrt(mp.fsum(
              ldd_to_mpf(bh[i],bl[i])**2 for i in range(nN,len(modes))
          )),50),
        }
    print("\n",sector)
    for k,v in row.items():
        if k not in ("sector","M_shell_residual_history"): print(k,"=",v)
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v","both"],default="both")
    a=ap.parse_args()
    sectors=["even-v","odd-v"] if a.sector=="both" else [a.sector]
    rows=[one_sector(s) for s in sectors]
    OUT.write_text(json.dumps({"rows":rows},indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
