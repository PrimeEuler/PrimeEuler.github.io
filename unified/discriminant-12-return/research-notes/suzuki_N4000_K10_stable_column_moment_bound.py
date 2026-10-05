#!/usr/bin/env python3
"""Stable seven-column upper bounds for the N=4000 K=10 absolute moments.

Avoid reconstructing the near-null global source vector before certification.
Use the stable decomposition

    x = y_f + sum_{k=1}^6 w_k W_k,

where each W_k and y_f is a separately residual-refined complement column and
w solves the 6x6 protected reduced system.

For any positive weight a_m,

    sum a_m |x_m|
      <= sum a_m |y_f,m| + sum_k |w_k| sum a_m |W_{m,k}|.

Compute this triangle upper for:
    S23   = sum m^23 |x_m|,
    Sz22  = sum |z_m| m^22 |x_m|.

Also report each column's weighted moment and the protected coefficients.
This is a midpoint/stability payload; the ledger adds outward column and
small-matrix perturbation factors.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp
import numpy as np

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis, full_source_matrix,
)
from suzuki_ldd_source_operator import (
    LD, dot_columns as dd_dot_columns, hp_parity_data_ld as hp_parity_data,
    ldd_to_mpf,
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement, dd_project, form_Ktilde, form_trial,
    mp_inverse_split, refine_once, residuals_dd,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"N4000_K10_stable_column_moment_bound_result.json"
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
    AUh,AUl,Rh,Rl,norms0=residuals_dd(data,P,Gih,Gil,Uh,Ul)
    Yh,Yl,yfh,yfl=refine_once(op,proj,Yh,Yl,yfh,yfl,Rh,Rl)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    yfh,yfl=dd_project(P,Gih,Gil,yfh,yfl)

    Uh,Ul=form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,norms1=residuals_dd(data,P,Gih,Gil,Uh,Ul)
    Kt=form_Ktilde(data,Uh,Ul,AUh,AUl,DPS)

    with mp.workdps(DPS):
        S=Kt[:6,:6]; g=-Kt[:6,6]; h=-Kt[6,6]
        w=mp.lu_solve(S,g)
        G=h+(g.T*w)[0]
        C=1/G

        mm=[mp.mpf(int(m)) for m in modes]
        zz=[abs(ldd_to_mpf(data.z_hi[i],data.z_lo[i]))
            for i in range(len(modes))]

        cols=[]
        for j in range(7):
            vals=[abs(ldd_to_mpf(Uh[i,j],Ul[i,j])) for i in range(len(modes))]
            s23=mp.fsum((m**23)*v for m,v in zip(mm,vals))
            sz22=mp.fsum(z*(m**22)*v for m,z,v in zip(mm,zz,vals))
            l2=mp.sqrt(mp.fsum(v*v for v in vals))
            cols.append((s23,sz22,l2))

        tri23=cols[6][0]+mp.fsum(abs(w[j])*cols[j][0] for j in range(6))
        triz22=cols[6][1]+mp.fsum(abs(w[j])*cols[j][1] for j in range(6))
        tril2=cols[6][2]+mp.fsum(abs(w[j])*cols[j][2] for j in range(6))

        row={
          "sector":sector,
          "capacity":mp.nstr(C,70),
          "sqrt_capacity":mp.nstr(mp.sqrt(C),60),
          "protected_coefficients":[mp.nstr(w[j],70) for j in range(6)],
          "max_abs_protected_coefficient":mp.nstr(max(abs(w[j]) for j in range(6)),60),
          "column_S23":[mp.nstr(x[0],70) for x in cols],
          "column_Sz22":[mp.nstr(x[1],70) for x in cols],
          "column_l2":[mp.nstr(x[2],60) for x in cols],
          "triangle_S23_upper_midpoint":mp.nstr(tri23,70),
          "triangle_Sz22_upper_midpoint":mp.nstr(triz22,70),
          "triangle_l2_upper_midpoint":mp.nstr(tril2,60),
          "joint_residuals_after":[float(x) for x in norms1],
          "joint_residual_max_after":max(norms1),
          "complement_floor_midpoint_diagnostic":gamma,
        }
    print("\n",sector)
    print("max |w| =",row["max_abs_protected_coefficient"])
    print("triangle S23 =",row["triangle_S23_upper_midpoint"])
    print("triangle Sz22 =",row["triangle_Sz22_upper_midpoint"])
    print("triangle l2 =",row["triangle_l2_upper_midpoint"])
    print("joint residual max =",row["joint_residual_max_after"])
    return row

def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    out={"N":N,"dps":DPS,"rows":rows,
         "guardrail":"Stable seven-column triangle midpoint payload; outward perturbation factors pending."}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
