#!/usr/bin/env python3
"""Fixed full-lattice FFT replay of the frozen-P4 capacity.

Purpose: remove both global near-block SVD compression and nested inexact
Schur matvecs.  A single fixed LinearOperator is used throughout CG:

    D_def = Q A_fft Q + P G_P^{-1} P^T.

The source-faithful off-diagonal action is the exact Toeplitz/Hankel identity;
the diagonal uses the arch recurrence at ARCH=200.  After the binary64 solve,
the existing LDDD/arch-200 residual machinery performs one refinement and
assembles the protected Schur scalar in high precision.

First gate: M=8000 and M=16000 must reproduce the already-promoted finite
capacity data before this route is used beyond 16000.

Diagnostic only: FFT/source arithmetic is not outward-rounded here.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.sparse.linalg import LinearOperator,cg,eigsh

from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import embedded_P,modes_for
from suzuki_kkt_remote_residual_certificate import source_rows
from suzuki_ldd_refined_capacity_bracket import (
    dd_project,form_Ktilde,form_trial,mp_inverse_split,refine_once,residuals_dd,
)
from suzuki_ldd_source_operator import LD,dot_columns as dd_dot_columns,hp_parity_data_ld as hp_parity_data
from suzuki_remote_fft_matvec_validation import fft_offdiag,arch_diag_vector
from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data,pole_vector,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M_full_fft_fixed_capacity_replay_result.json"
DPS=180
ARCH=200
TARGET={
  ("even-v",8000): 7.527204146095217e-30,
  ("even-v",16000):7.499901498486917e-30,
  ("odd-v",8000):  2.170029381845773e-25,
  ("odd-v",16000): 2.1622076013239955e-25,
}
ETA_TARGET={
  "even-v":0.0036404008257719944,
  "odd-v":0.003617497467397701,
}

def fixed_operator(modes,sector,P,Gi):
    modes=np.asarray(modes,dtype=int)
    # Full-lattice acceptance gate: use the exact source-faithful diagonal
    # producer.  The vectorized arch recurrence is only stable in the high
    # remote regime and overflows at low n when pushed to ARCH=200.
    z,diag=endpoint_data(modes,sign=-1,rho=0.0)
    p,alpha=pole_vector(modes,sector)
    f=source_rows(modes,sector)

    def raw_mv(x):
        x=np.asarray(x,dtype=float)
        if x.ndim==1:
            return fft_offdiag(modes,z,x)+diag*x+alpha*p*float(p@x)
        return np.column_stack([raw_mv(x[:,j]) for j in range(x.shape[1])])

    def proj(x):
        x=np.asarray(x,dtype=float)
        return x-P@(Gi@(P.T@x))

    def mv(x):
        q=proj(x)
        return proj(raw_mv(q))+P@(Gi@(P.T@x))

    op=LinearOperator((len(modes),len(modes)),matvec=mv,dtype=float)
    return raw_mv,proj,op,f

def solve_state(sector,maxmode):
    modes=modes_for(sector,maxmode)
    P=embedded_P(sector,modes)

    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    raw_mv,proj,op,f=fixed_operator(modes,sector,P,Gi)

    # The protected directions have eigenvalue 1 in the deflated operator;
    # the smallest eigenvalue is therefore the complement floor if <1.
    evals=np.sort(eigsh(op,k=4,which="SA",return_eigenvectors=False,tol=1e-11))
    gamma=float(evals[0])

    E=proj(raw_mv(P))
    fQ=proj(f)
    rhs=np.column_stack([E,fQ])
    sol=np.empty_like(rhs)
    init_res=[]
    iters=[]
    for j in range(7):
        cnt=[0]
        x,info=cg(op,rhs[:,j],rtol=2e-14,atol=0,maxiter=20000,
                  callback=lambda _:cnt.__setitem__(0,cnt[0]+1))
        if info!=0:
            raise RuntimeError(("fixed FFT initial CG failed",sector,maxmode,j,info))
        sol[:,j]=proj(x)
        init_res.append(float(np.linalg.norm(rhs[:,j]-op@sol[:,j])))
        iters.append(cnt[0])

    Yh=sol[:,:6].astype(LD);Yl=np.zeros_like(Yh,dtype=LD)
    yfh=sol[:,6].astype(LD);yfl=np.zeros_like(yfh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    yfh,yfl=dd_project(P,Gih,Gil,yfh,yfl)

    data=hp_parity_data(modes,sector,dps=DPS,arch_terms=ARCH,correction_terms=50)
    Uh,Ul=form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,n0=residuals_dd(data,P,Gih,Gil,Uh,Ul)

    # Refinement uses the same fixed FFT operator as the initial solve.
    Yh,Yl,yfh,yfl=refine_once(op,proj,Yh,Yl,yfh,yfl,Rh,Rl)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    yfh,yfl=dd_project(P,Gih,Gil,yfh,yfl)
    Uh,Ul=form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,n1=residuals_dd(data,P,Gih,Gil,Uh,Ul)

    K=form_Ktilde(data,Uh,Ul,AUh,AUl,DPS)
    with mp.workdps(DPS):
        S=K[:6,:6];g=-K[:6,6];h=-K[6,6]
        vals,_=mp.eigsy((S+S.T)/2)
        w=mp.lu_solve(S,g)
        G=h+(g.T*w)[0]
        C=1/G

    Ct=TARGET[(sector,maxmode)]
    row={
      "sector":sector,"maxmode":maxmode,"dimension":len(modes),
      "capacity_fft_fixed":float(C),
      "capacity_theorem_target":Ct,
      "capacity_signed_error":float(C)-Ct,
      "capacity_relative_error":abs(float(C)-Ct)/abs(Ct),
      "complement_floor":gamma,
      "smallest_deflated_eigs":[float(x) for x in evals],
      "initial_cg_iters":iters,
      "initial_recomputed_residual_max":max(init_res),
      "ldd_residual_before_refine_max":max(n0),
      "ldd_residual_after_refine_max":max(n1),
      "protected_S_min_eig":mp.nstr(vals[0],30),
      "guardrail":"Fixed full-lattice FFT midpoint diagnostic; no outward rounding or infinite-tail claim."
    }
    print(json.dumps(row,indent=2),flush=True)
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    rows=[solve_state(a.sector,8000),solve_state(a.sector,16000)]
    C8=rows[0]["capacity_fft_fixed"]; C16=rows[1]["capacity_fft_fixed"]
    eta=C8/C16-1.0
    summary={
      "sector":a.sector,
      "eta_fft_fixed":eta,
      "eta_theorem_target":ETA_TARGET[a.sector],
      "eta_signed_error":eta-ETA_TARGET[a.sector],
      "eta_absolute_error":abs(eta-ETA_TARGET[a.sector]),
    }
    print(json.dumps(summary,indent=2),flush=True)
    OUT.write_text(json.dumps({"rows":rows,"summary":summary},indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
