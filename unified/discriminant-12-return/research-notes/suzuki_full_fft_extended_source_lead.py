#!/usr/bin/env python3
"""Source-only 64k fixed-FFT finite data: C_N, L_N, A_N=C_N L_N^2.

This is a lighter split of suzuki_full_fft_extended_finite_data.py.  It uses
exactly the same calibrated fixed full-lattice FFT operator and accepted LDDD
source refinement, but omits the additional w1/M11 response.  Purpose: expose
Delta A_64k independently while the full M11 producer continues.

Diagnostic midpoint only; no outward rounding or infinite-tail claim.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.sparse.linalg import cg

from suzuki_full_fft_fixed_capacity_replay import fixed_operator,DPS,ARCH
from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import embedded_P,modes_for
from suzuki_ldd_refined_capacity_bracket import (
    dd_project,form_Ktilde,form_trial,mp_inverse_split,refine_once,residuals_dd,
)
from suzuki_ldd_source_operator import LD,dot_columns as dd_dot_columns,hp_parity_data_ld as hp_parity_data
from suzuki_ldd_remote_source_lead_diagnostic import dd_linear_combination,dd_dot_to_mp

HERE=Path(__file__).resolve().parent
OUT=HERE/"full_fft_extended_source_lead_result.json"

def solve_one(sector,cutoff):
    modes=modes_for(sector,cutoff)
    P=embedded_P(sector,modes)
    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    raw_mv,proj,op,f=fixed_operator(modes,sector,P,Gi)
    data=hp_parity_data(modes,sector,dps=DPS,arch_terms=ARCH,correction_terms=50)

    E=proj(raw_mv(P))
    rhs=np.column_stack([E,proj(f)])
    sol=np.empty_like(rhs)
    init_res=[]; iters=[]
    for j in range(rhs.shape[1]):
        cnt=[0]
        x,info=cg(op,rhs[:,j],rtol=2e-14,atol=0,maxiter=30000,
                  callback=lambda _:cnt.__setitem__(0,cnt[0]+1))
        if info!=0:
            raise RuntimeError(("fixed FFT CG failed",sector,cutoff,j,info))
        sol[:,j]=proj(x)
        init_res.append(float(np.linalg.norm(rhs[:,j]-op@sol[:,j])))
        iters.append(cnt[0])

    Yh=sol[:,:6].astype(LD); Yl=np.zeros_like(Yh,dtype=LD)
    yfh=sol[:,6].astype(LD); yfl=np.zeros_like(yfh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    yfh,yfl=dd_project(P,Gih,Gil,yfh,yfl)

    Uh,Ul=form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,r0=residuals_dd(data,P,Gih,Gil,Uh,Ul)
    Yh,Yl,yfh,yfl=refine_once(op,proj,Yh,Yl,yfh,yfl,Rh,Rl)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    yfh,yfl=dd_project(P,Gih,Gil,yfh,yfl)
    Uh,Ul=form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,r1=residuals_dd(data,P,Gih,Gil,Uh,Ul)

    K=form_Ktilde(data,Uh,Ul,AUh,AUl,DPS)
    with mp.workdps(DPS):
        S=K[:6,:6]; g=-K[:6,6]; h=-K[6,6]
        w=mp.lu_solve(S,g)
        G=h+(g.T*w)[0]
        C=1/G
        coeff=[w[j] for j in range(6)]+[mp.mpf(1)]
        xh,xl=dd_linear_combination(Uh,Ul,coeff)
        zx=dd_dot_to_mp(data.z_hi,data.z_lo,xh,xl)
        px=dd_dot_to_mp(data.pole_hi,data.pole_lo,xh,xl)
        alpha=mp.mpf(2 if sector=="even-v" else -2)
        if sector=="even-v":
            f_lead=4*mp.cosh(1)/mp.pi; g0=mp.cosh(mp.mpf("0.5"))
        else:
            f_lead=-4*mp.sinh(1)/mp.pi; g0=mp.sinh(mp.mpf("0.5"))
        L=f_lead+(2/mp.pi)*zx-alpha*(4*g0/mp.pi)*px
        Aamp=C*L*L

    row={
      "sector":sector,"cutoff":cutoff,"dimension":len(modes),
      "capacity_C":mp.nstr(C,60),
      "remote_leading_L":mp.nstr(L,60),
      "sign_L":1 if L>0 else -1 if L<0 else 0,
      "A_C_times_L_squared":mp.nstr(Aamp,60),
      "z_dot_source":mp.nstr(zx,60),
      "pole_dot_source":mp.nstr(px,60),
      "initial_cg_iters":iters,
      "initial_recomputed_residual_max":max(init_res),
      "source_ldd_residual_before_refine_max":max(r0),
      "source_ldd_residual_after_refine_max":max(r1),
      "guardrail":"Source-only fixed-FFT midpoint; no M11, no outward radius, no infinite-tail claim."
    }
    print(json.dumps(row,indent=2),flush=True)
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    ap.add_argument("--cutoff",type=int,default=64000,choices=[32000,64000])
    a=ap.parse_args()
    row=solve_one(a.sector,a.cutoff)
    OUT.write_text(json.dumps(row,indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
