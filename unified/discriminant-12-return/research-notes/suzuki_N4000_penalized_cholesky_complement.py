#!/usr/bin/env python3
"""Direct penalized-Cholesky certificate target for the N=4000 frozen complement.

For each parity finite section A_N and the identical frozen six-column P,
define
    H_L = A_N + Lambda P P^T.
On Ran(P)^perp the penalty vanishes, so any lower bound H_L >= delta I gives
A_N|_Q >= delta I.

This reuses the v14.029/v14.031 audited certificate architecture:
  * binary64 dense Cholesky,
  * longdouble comparison recursion for ||L^{-1}||_inf,
  * lambda_min(LL^T) >= 1/(n ||L^{-1}||_inf^2),
  * standard Cholesky backward error gamma_{n+1} ||L||_F^2,
  * established dimension-free source/operator allowance 2.1e-13.

The target needed downstream is only delta > 1e-3.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis, full_source_matrix,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"N4000_penalized_cholesky_complement_result.json"
U=2.0**-53
EPS_SOURCE=2.1e-13
TARGET=1e-3

def gamma_n(n,u=U):
    nu=n*u
    if nu>=1: raise RuntimeError("gamma invalid")
    return nu/(1-nu)

def linv_inf_recursion(L):
    n=L.shape[0]
    y=np.empty(n,dtype=np.longdouble)
    for i in range(n):
        s=np.longdouble(0) if i==0 else np.dot(
            np.abs(L[i,:i].astype(np.longdouble)),y[:i]
        )
        y[i]=(np.longdouble(1)+s)/np.longdouble(L[i,i])
    return float(np.max(y))*(1+1e-12)

def modes_for(sector):
    return np.arange(1 if sector=="even-v" else 2,4001,2,dtype=int)

def one_sector(sector):
    modes=modes_for(sector)
    P,_=frozen_protected_basis(sector,modes)
    A,_=full_source_matrix(modes,sector)
    rows=[]
    for lam in (0.1,1.0,10.0,100.0):
        H=(A+lam*(P@P.T))
        H=(H+H.T)/2
        row={"Lambda":lam}
        try:
            L=np.linalg.cholesky(H)
        except np.linalg.LinAlgError as e:
            row.update(cholesky=False,error=str(e)); rows.append(row); continue
        linv=linv_inf_recursion(L)
        n=len(modes)
        factor=1/(n*linv*linv)
        g=gamma_n(n+1)
        fro2=float(np.sum(L*L,dtype=np.float64))
        back=g*fro2
        lower=factor-back-EPS_SOURCE
        row.update({
          "cholesky":True,
          "linv_inf_bound_padded":linv,
          "factor_lower_bound":factor,
          "cholesky_backward_budget":back,
          "source_operator_uncertainty":EPS_SOURCE,
          "exact_lower_bound_conservative":lower,
          "passes_1e3":bool(lower>TARGET),
          "min_cholesky_diag":float(np.min(np.diag(L))),
          "L_frob_sq":fro2,
        })
        print(sector,"Lambda",lam,"lower",lower,"PASS target",lower>TARGET)
        rows.append(row)
    best=max((r.get("exact_lower_bound_conservative",-1) for r in rows))
    out={"sector":sector,"dimension":len(modes),"target":TARGET,"best_lower":best,"rows":rows}
    if best<=TARGET:
        raise RuntimeError((sector,"failed target",best))
    return out

def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    OUT.write_text(json.dumps({"rows":rows},indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
