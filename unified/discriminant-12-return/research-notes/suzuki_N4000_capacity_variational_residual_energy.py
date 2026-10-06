#!/usr/bin/env python3
"""Correlated Feshbach residual-energy diagnostic for N=4000 capacity.

For the reconstructed source trial x from the LDDD seven-column reduction,
    r = A x - f.
The variational identity gives
    G - J(x) = r^T A^{-1} r >= 0.

A global ||A^{-1}|| bound is useless because the protected six-plane is
near-null.  Instead eliminate the frozen complement Q:
    y = D^{-1} r_Q,
    r_red = r - A y,
and use the refined graph columns W with Schur form S=W^T A W:
    r^T A^{-1} r
      = r_Q^T D^{-1} r_Q
        + (W^T r_red)^T S^{-1}(W^T r_red)
when y and W are exact eliminators.

This replay evaluates the correlated midpoint quantity with the same LDDD
operator/refinement architecture.  It also reports the Q-solve residual, so
an outward follow-up can charge the inexact elimination quadratically using a
certified complement floor.

Diagnostic only: no capacity theorem is promoted here.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import mpmath as mp
import numpy as np

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis, full_source_matrix,
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement, dd_matrix_to_mp, dd_project, form_Ktilde,
    form_trial, mp_inverse_split, refine_once, residuals_dd, solve_correction,
)
from suzuki_ldd_source_operator import (
    LD, add as dd_add, dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data, ldd_to_mpf,
    matvec as dd_matvec, norm2 as dd_norm2, split_mpf_ld, sub as dd_sub,
)
from suzuki_ldd_remote_source_lead_diagnostic import dd_linear_combination

HERE=Path(__file__).resolve().parent
OUT=HERE/"N4000_capacity_variational_residual_energy_result.json"
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
        modes,sector,dps=DPS,arch_terms=160,correction_terms=50
    )

    Yh=Y0.astype(LD); Yl=np.zeros_like(Yh,dtype=LD)
    yfh=yf0.astype(LD); yfl=np.zeros_like(yfh,dtype=LD)
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
        S=Kt[:6,:6]
        g=-Kt[:6,6]
        h=-Kt[6,6]
        w=mp.lu_solve(S,g)
        G=h+(g.T*w)[0]
        C=1/G
        coeffs=[w[j] for j in range(6)]+[mp.mpf(1)]

    # Reconstruct x as an LDDD linear combination of stable trial columns.
    xh,xl=dd_linear_combination(Uh,Ul,coeffs)
    Axh,Axl=dd_matvec(data,xh,xl)
    rh,rl=dd_sub(Axh,Axl,data.source_hi,data.source_lo)
    qh,ql=dd_project(P,Gih,Gil,rh,rl)

    # Midpoint Q inverse action; refine once against the LDDD operator.
    qfloat=np.asarray(qh+ql,dtype=float)
    y0=solve_correction(op,proj,qfloat,rtol=2e-14)
    yh=np.asarray(y0,dtype=LD)
    yl=np.zeros_like(yh,dtype=LD)
    yh,yl=dd_project(P,Gih,Gil,yh,yl)

    Ayh,Ayl=dd_matvec(data,yh,yl)
    # Q residual of A y - r_Q.
    qAyh,qAyl=dd_project(P,Gih,Gil,Ayh,Ayl)
    eyh,eyl=dd_sub(qAyh,qAyl,qh,ql)
    # One correction with opposite sign.
    dy=solve_correction(op,proj,-np.asarray(eyh+eyl,dtype=float),rtol=2e-14)
    yh,yl=dd_add(yh,yl,np.asarray(dy,dtype=LD),np.zeros_like(yh,dtype=LD))
    yh,yl=dd_project(P,Gih,Gil,yh,yl)

    Ayh,Ayl=dd_matvec(data,yh,yl)
    qAyh,qAyl=dd_project(P,Gih,Gil,Ayh,Ayl)
    eyh,eyl=dd_sub(qAyh,qAyl,qh,ql)
    qsolve_res=dd_norm2(eyh,eyl)

    # Complement energy r_Q^T y.
    eh,el=dd_dot_columns(qh[:,None],ql[:,None],yh[:,None],yl[:,None])

    # Reduced protected remainder r - A y, paired with graph W=U[:,:6].
    remh,reml=dd_sub(rh,rl,Ayh,Ayl)
    gh,gl=dd_dot_columns(Uh[:,:6],Ul[:,:6],remh[:,None],reml[:,None])

    with mp.workdps(DPS):
        eQ=ldd_to_mpf(eh[0,0],el[0,0])
        gr=mp.matrix([ldd_to_mpf(gh[i,0],gl[i,0]) for i in range(6)])
        eP=(gr.T*mp.lu_solve(S,gr))[0]
        etot=eQ+eP
        rel=etot/G

        vals,_=mp.eigsy((S+S.T)/2)
        row={
          "sector":sector,
          "capacity_midpoint":mp.nstr(C,70),
          "source_energy_G":mp.nstr(G,70),
          "full_source_residual_l2":dd_norm2(rh,rl),
          "q_source_residual_l2":dd_norm2(qh,ql),
          "q_solve_residual_l2_after":qsolve_res,
          "complement_energy_midpoint":mp.nstr(eQ,70),
          "reduced_protected_rhs_l2":mp.nstr(mp.sqrt((gr.T*gr)[0]),60),
          "protected_energy_midpoint":mp.nstr(eP,70),
          "total_residual_energy_midpoint":mp.nstr(etot,70),
          "residual_energy_over_G":mp.nstr(rel,50),
          "S_min_midpoint":mp.nstr(vals[0],60),
          "complement_floor_midpoint":gamma,
          "joint_trial_residual_max":max(n1),
          "guardrail":"Correlated midpoint residual energy; outward arithmetic/source charges pending."
        }
    print("\n",json.dumps(row,indent=2))
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
