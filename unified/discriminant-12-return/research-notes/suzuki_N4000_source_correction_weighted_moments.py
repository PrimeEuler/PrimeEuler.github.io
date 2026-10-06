#!/usr/bin/env python3
"""Weighted moments of the correlated source-solution correction at N=4000.

For the refined LDDD source trial x with residual r=A x-f, use the same
Feshbach decomposition as the capacity residual-energy diagnostic:

  y_Q ~= D^{-1} r_Q,
  r_red = r-A y_Q,
  c_P = S^{-1} W^T r_red.

Then A^{-1}r is represented (up to the already-reported Q/graph residuals) by

  delta = y_Q + W c_P.

Since x_exact = x-delta, the weighted absolute moment error obeys

  |S_a(x_exact)-S_a(x)| <= sum a_m |delta_m|

for positive weights a_m.

Report this correction for
  S23 = sum m^23 |x_m|,
  Sz22 = sum |z_m| m^22 |x_m|.

Arch-200 is used to align with the final exact-source audit.
Diagnostic only: final outward promotion must charge the tiny Q solve/graph
residual and arithmetic/source formation of delta.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import mpmath as mp
import numpy as np

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis,full_source_matrix,
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement,dd_project,form_Ktilde,form_trial,
    mp_inverse_split,refine_once,residuals_dd,solve_correction,
)
from suzuki_ldd_remote_source_lead_diagnostic import dd_linear_combination
from suzuki_ldd_source_operator import (
    LD,add as dd_add,dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,ldd_to_mpf,
    matvec as dd_matvec,norm2 as dd_norm2,sub as dd_sub,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"N4000_source_correction_weighted_moments_result.json"
N=4000
DPS=180

def modes_for(sector):
    return np.arange(1 if sector=="even-v" else 2,N+1,2,dtype=int)

def one_sector(sector):
    modes=modes_for(sector)
    P,_=frozen_protected_basis(sector,modes)
    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])
    A,f=full_source_matrix(modes,sector)
    op,proj,gamma,evals,Y0,yf0,initial=build_double_complement(
        A,P,Gi,f,rtol=2e-14
    )
    data=hp_parity_data(
        modes,sector,dps=DPS,arch_terms=200,correction_terms=50
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
    K=form_Ktilde(data,Uh,Ul,AUh,AUl,DPS)
    with mp.workdps(DPS):
        S=K[:6,:6];g=-K[:6,6];h=-K[6,6]
        w=mp.lu_solve(S,g)
        G=h+(g.T*w)[0]
        C=1/G
        coeffs=[w[j] for j in range(6)]+[mp.mpf(1)]
    xh,xl=dd_linear_combination(Uh,Ul,coeffs)
    Axh,Axl=dd_matvec(data,xh,xl)
    rh,rl=dd_sub(Axh,Axl,data.source_hi,data.source_lo)
    qh,ql=dd_project(P,Gih,Gil,rh,rl)

    # Q inverse action + one refinement.
    y0=solve_correction(op,proj,np.asarray(qh+ql,dtype=float),rtol=2e-14)
    yh=np.asarray(y0,dtype=LD);yl=np.zeros_like(yh,dtype=LD)
    yh,yl=dd_project(P,Gih,Gil,yh,yl)
    Ayh,Ayl=dd_matvec(data,yh,yl)
    qAyh,qAyl=dd_project(P,Gih,Gil,Ayh,Ayl)
    eyh,eyl=dd_sub(qAyh,qAyl,qh,ql)
    dy=solve_correction(op,proj,-np.asarray(eyh+eyl,dtype=float),rtol=2e-14)
    yh,yl=dd_add(yh,yl,np.asarray(dy,dtype=LD),np.zeros_like(yh,dtype=LD))
    yh,yl=dd_project(P,Gih,Gil,yh,yl)

    Ayh,Ayl=dd_matvec(data,yh,yl)
    remh,reml=dd_sub(rh,rl,Ayh,Ayl)
    gh,gl=dd_dot_columns(Uh[:,:6],Ul[:,:6],remh[:,None],reml[:,None])
    with mp.workdps(DPS):
        gr=mp.matrix([ldd_to_mpf(gh[i,0],gl[i,0]) for i in range(6)])
        cp=mp.lu_solve(S,gr)
    ph,pl=dd_linear_combination(
        Uh[:,:6],Ul[:,:6],[cp[j] for j in range(6)]
    )
    dh,dl=dd_add(yh,yl,ph,pl)

    with mp.workdps(DPS):
        mm=[mp.mpf(int(m)) for m in modes]
        zz=[abs(ldd_to_mpf(data.z_hi[i],data.z_lo[i])) for i in range(len(modes))]
        xx=[abs(ldd_to_mpf(xh[i],xl[i])) for i in range(len(modes))]
        dd=[abs(ldd_to_mpf(dh[i],dl[i])) for i in range(len(modes))]
        s23=mp.fsum(m**23*v for m,v in zip(mm,xx))
        sz22=mp.fsum(z*m**22*v for m,z,v in zip(mm,zz,xx))
        e23=mp.fsum(m**23*v for m,v in zip(mm,dd))
        ez22=mp.fsum(z*m**22*v for m,z,v in zip(mm,zz,dd))
        row={
          "sector":sector,
          "capacity":mp.nstr(C,70),
          "trial_S23":mp.nstr(s23,70),
          "trial_Sz22":mp.nstr(sz22,70),
          "correction_S23":mp.nstr(e23,70),
          "correction_Sz22":mp.nstr(ez22,70),
          "correction_over_trial_S23":mp.nstr(e23/s23,50),
          "correction_over_trial_Sz22":mp.nstr(ez22/sz22,50),
          "protected_correction_coefficients":[mp.nstr(cp[j],60) for j in range(6)],
          "q_solve_residual_after":dd_norm2(
             *dd_project(P,Gih,Gil,*dd_sub(
                 *dd_matvec(data,yh,yl),qh,ql
             ))
          ),
          "joint_trial_residual_max":max(n1),
          "guardrail":"Midpoint correlated correction; outward residual/arithmetic inflation pending."
        }
    print(json.dumps(row,indent=2))
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    row=one_sector(a.sector)
    OUT.write_text(json.dumps({"rows":[row]},indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
