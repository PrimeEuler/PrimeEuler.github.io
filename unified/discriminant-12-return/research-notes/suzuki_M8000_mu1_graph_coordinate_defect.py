#!/usr/bin/env python3
"""Protected-coordinate defect of the refined M8000 mu=1 graph vectors.

For the represented correction Y and W=P-Y, report the LDDD protected
coordinate defect P^T Y.  This is used only to verify that W has an
invertible protected coordinate matrix and, if desired, to reproject to an
exact graph by a tiny congruence.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp
import numpy as np

from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_M3999_frozen_p4_source_capacity_midpoint import full_source_matrix
from suzuki_ldd_refined_capacity_bracket import (
    dd_matrix_to_mp, dd_project, mp_inverse_split, solve_correction,
)
from suzuki_ldd_source_operator import (
    LD, add as dd_add, dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data, matvec as dd_matvec,
    sub as dd_sub,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_mu1_graph_coordinate_defect_result.json"
DPS=180

def shifted_matvec(data,Xh,Xl,shell_start):
    yh,yl=dd_matvec(data,Xh,Xl)
    yh=yh.copy(); yl=yl.copy()
    yh[shell_start:]-=Xh[shell_start:]
    yl[shell_start:]-=Xl[shell_start:]
    return yh,yl

def one_sector(sector):
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
        if info!=0: raise RuntimeError((sector,j,info))
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

    Ph,Pl=dd_dot_columns(P,None,Yh,Yl)
    Bh,Bl=dd_dot_columns(P,None,P,None)
    # P^T W = G - P^T Y.
    CWh,CWl=(Bh-Ph),(Bl-Pl)

    with mp.workdps(DPS):
        PY=dd_matrix_to_mp(Ph,Pl)
        G=dd_matrix_to_mp(Bh,Bl)
        PW=dd_matrix_to_mp(CWh,CWl)
        defect=max(abs(PY[i,j]) for i in range(6) for j in range(6))
        Ginv=G**-1
        B=Ginv*PW
        Be=B-mp.eye(6)
        bdef=max(abs(Be[i,j]) for i in range(6) for j in range(6))
        svals=mp.svd(B,compute_uv=False)
        smin=min(svals)

    row={
        "sector":sector,
        "max_abs_PtY":mp.nstr(defect,70),
        "max_abs_protected_coordinate_minus_identity":mp.nstr(bdef,70),
        "protected_coordinate_smin":mp.nstr(smin,70),
        "invertible":bool(smin>mp.mpf("0.999999999999")),
    }
    print("\n",sector,row)
    if not row["invertible"]:
        raise RuntimeError(("protected coordinate not safely invertible",row))
    return row

def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    out={"rows":rows}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
