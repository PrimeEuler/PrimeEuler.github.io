#!/usr/bin/env python3
"""Pre-cancellation magnitude diagnostic for the N=4000 arch-200 capacity reduction.

Build the same seven refined trial columns U=[W_1,...,W_6,y_f] used by the
LDDD capacity bracket, but evaluate positive component majorants before any
cancellation.  These magnitudes are the correct scale for a rigorous
error-free-transformation (EFT) rounding envelope on the 7x7 augmented K.

For source-faithful A:
 offdiag component majorant
   |c| (|z_i| n_j + |z_j| n_i)/|n_i^2-n_j^2|
   + |alpha| |p_i p_j|,
 diag
   |d_i| + |alpha| p_i^2.

Report:
  QG_max = max_ab |U_a|^T A_component |U_b|,
  Qq_max = max_a sum_i |U_ia| |f_i|,
  QK_max = conservative max positive magnitude entering Ktilde,
           max(QG_max, QG_max+Qq_max, QG_max+2 Qq_max).

Diagnostic only; this measures the magnitude scale but does not itself prove
a finite-arithmetic constant.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis, full_source_matrix,
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement, dd_project, form_trial, mp_inverse_split,
    refine_once, residuals_dd,
)
from suzuki_ldd_source_operator import (
    LD, dot_columns as dd_dot_columns, hp_parity_data_ld as hp_parity_data,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"N4000_capacity_component_magnitude_result.json"
N=4000
DPS=180
CHUNK=200

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

    U=np.asarray(Uh+Ul,dtype=LD)
    absU=np.abs(U)
    mm=modes.astype(LD)
    z=np.asarray(data.z_hi+data.z_lo,dtype=LD)
    p=np.asarray(data.pole_hi+data.pole_lo,dtype=LD)
    d=np.asarray(data.diag_hi+data.diag_lo,dtype=LD)
    fs=np.asarray(data.source_hi+data.source_lo,dtype=LD)
    c=abs(LD(data.c_hi+data.c_lo))
    alpha=abs(LD(data.alpha))

    # T = A_component @ |U| without materializing the dense majorant.
    T=np.zeros_like(absU,dtype=LD)
    row_sums=np.zeros(len(modes),dtype=LD)
    for j in range(len(modes)):
        nj=mm[j]
        den=np.abs(mm*mm-nj*nj)
        safe=den.copy(); safe[j]=LD(1)
        col=c*(np.abs(z)*nj+abs(z[j])*mm)/safe + alpha*np.abs(p*p[j])
        col[j]=abs(d[j])+alpha*abs(p[j]*p[j])
        row_sums += col
        T += col[:,None]*absU[j,:]
        if (j+1)%500==0:
            print(sector,"component columns",j+1,"/",len(modes))

    QG=absU.T@T
    Qq=absU.T@np.abs(fs)
    qg=float(np.max(QG))
    qq=float(np.max(Qq))
    qk=max(qg,qg+qq,qg+2*qq)

    row={
      "sector":sector,
      "dimension":len(modes),
      "QG_max":qg,
      "Qq_max":qq,
      "QK_max":qk,
      "QG_matrix":np.asarray(QG,dtype=float).tolist(),
      "Qq_vector":np.asarray(Qq,dtype=float).tolist(),
      "component_row_sum_max":float(np.max(row_sums)),
      "refined_trial_max_abs":float(np.max(absU)),
      "complement_floor_midpoint":gamma,
      "guardrail":"Positive midpoint magnitude producer; no outward arithmetic theorem."
    }
    print("\n",json.dumps(row,indent=2))
    return row

def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    OUT.write_text(json.dumps({"rows":rows},indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
