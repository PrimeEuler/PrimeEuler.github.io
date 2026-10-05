#!/usr/bin/env python3
"""Row-sum/trace diagnostic for the full exact near Gram Hn=B F^{-1} B^*.

Uses the same structured binary64 front inverse as the full-near midpoint
diagnostic, but processes target columns in chunks so H need not be stored.

Reports:
  max_i sum_j |H_ij|,
  trace(H),
  max diagonal,
which indicate whether a direct Schur/Gershgorin cap can certify b_nn.

Diagnostic only because the structured front inverse is near singular in
binary64; independent LDDD/Feshbach certification remains required.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np

from suzuki_M8000_mu1_full_near_triple_diagnostic import (
    lattice, exact_cross, front_inverse_apply_factory,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_near_gram_rowsum_diagnostic_result.json"
CHUNK=100

def one_sector(sector):
    front,Finv,meta=front_inverse_apply_factory(sector)
    near=lattice(sector,8001,16000)
    B=exact_cross(near,front,sector)
    rowsum=np.zeros(len(near),dtype=float)
    tr=0.0
    dmax=0.0
    for a in range(0,len(near),CHUNK):
        b=min(a+CHUNK,len(near))
        X=Finv(B[a:b].T)
        Hc=B@X
        rowsum[a:b] += 0.0  # columns are accumulated below for every row
        rowsum += np.sum(np.abs(Hc),axis=1)
        # Hc[:,j-a] corresponds global column j
        for jj,j in enumerate(range(a,b)):
            v=float(Hc[j,jj])
            tr+=v
            dmax=max(dmax,v)
        print(sector,"Gram columns",b,"/",len(near))
    row={
      "sector":sector,**meta,
      "near_dimension":len(near),
      "max_absolute_row_sum":float(np.max(rowsum)),
      "median_absolute_row_sum":float(np.median(rowsum)),
      "trace":float(tr),
      "max_diagonal":float(dmax),
      "target_b_cap":0.25,
      "rowsum_below_025":bool(np.max(rowsum)<0.25),
      "guardrail":"Binary64 structured-inverse diagnostic only."
    }
    print("\n",json.dumps(row,indent=2))
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    args=ap.parse_args()
    row=one_sector(args.sector)
    OUT.write_text(json.dumps({"rows":[row]},indent=2,sort_keys=True)+"\n")
    print("wrote",OUT)

if __name__=="__main__":
    main()
