#!/usr/bin/env python3
"""Low-rank diagnostic for the exact M8000 front-to-near coupling B_n.

Extract leading singular values of the exact source-faithful coupling
  front <=8000  -> near 8000<n<16000
and report the discarded Frobenius residual after ranks 6,12,18,24,32.

This identifies a correlation-preserving finite target set for certifying
  b_nn = ||B F^{-1} B^*||
without invoking ||F^{-1}|| on the full raw coupling.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import svds
from suzuki_M8000_mu1_full_near_triple_diagnostic import (
    lattice, exact_cross, front_inverse_apply_factory,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_near_coupling_svd_result.json"

def one(sector):
    front,_,_=front_inverse_apply_factory(sector)
    near=lattice(sector,8001,16000)
    B=exact_cross(near,front,sector)
    fro=float(np.linalg.norm(B,"fro"))
    k=32
    U,s,Vt=svds(B,k=k,which="LM",return_singular_vectors=True,
                tol=1e-11,maxiter=3000)
    s=np.sort(s)[::-1]
    rows={}
    for r in (6,12,18,24,32):
        resid=math.sqrt(max(0.0,fro*fro-float(np.dot(s[:r],s[:r]))))
        rows[str(r)]={"residual_fro":resid,"captured_fraction_sq":1-(resid/fro)**2}
    out={
      "sector":sector,"shape":list(B.shape),"fro":fro,
      "singular_values":[float(x) for x in s],
      "rank_summaries":rows,
    }
    print(json.dumps(out,indent=2))
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    row=one(a.sector)
    OUT.write_text(json.dumps({"rows":[row]},indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
