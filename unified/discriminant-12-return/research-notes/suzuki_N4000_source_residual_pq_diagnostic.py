#!/usr/bin/env python3
"""P/Q decomposition of the reconstructed N=4000 source residual.

The direct K=10 moment payload only needs an l2 source-solution error below
~6e14 in the difficult even sector.  The raw residual alone is misleading
because the full operator is near-null only on the frozen protected six-plane.

Reconstruct x_N exactly as the v14.020 producer does, evaluate r=A x_N-f in
LDDD arithmetic, and split r into the frozen protected P coordinates and
Euclidean complement Q.  Report:
  ||r||_2, ||P^T r||_2, ||Q r||_2,
and the individual protected coordinates.

Diagnostic only: converting these residual components to an outward solution
error still requires certified complement and protected inverse bounds.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp
import numpy as np

from suzuki_N4000_far_geometric_remainder_diagnostic import reconstruct_source
from suzuki_M3999_frozen_p4_source_capacity_midpoint import frozen_protected_basis
from suzuki_ldd_refined_capacity_bracket import dd_project, mp_inverse_split
from suzuki_ldd_source_operator import (
    LD, dot_columns as dd_dot_columns, hp_parity_data_ld as hp_parity_data,
    matvec as dd_matvec, split_mpf_ld, sub as dd_sub, norm2 as dd_norm2,
    ldd_to_mpf,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"N4000_source_residual_pq_diagnostic_result.json"
DPS=180

def one_sector(sector):
    st=reconstruct_source(sector)
    modes=st["modes"]
    P,_=frozen_protected_basis(sector,modes)
    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)

    data=hp_parity_data(modes,sector,dps=DPS,arch_terms=160,correction_terms=50)
    xh=np.empty(len(modes),dtype=LD)
    xl=np.empty(len(modes),dtype=LD)
    for i,x in enumerate(st["xmp"]):
        xh[i],xl[i]=split_mpf_ld(x)

    Axh,Axl=dd_matvec(data,xh,xl)
    rh,rl=dd_sub(Axh,Axl,data.source_hi,data.source_lo)
    qh,ql=dd_project(P,Gih,Gil,rh,rl)
    ch,cl=dd_dot_columns(P,None,rh,rl)

    with mp.workdps(DPS):
        coords=[ldd_to_mpf(ch[i],cl[i]) for i in range(6)]
        pnorm=mp.sqrt(mp.fsum(abs(c)**2 for c in coords))
        row={
          "sector":sector,
          "capacity":mp.nstr(st["C"],70),
          "full_residual_l2":dd_norm2(rh,rl),
          "q_residual_l2":dd_norm2(qh,ql),
          "p_coordinate_l2":mp.nstr(pnorm,60),
          "p_coordinates":[mp.nstr(c,70) for c in coords],
          "q_over_full":dd_norm2(qh,ql)/dd_norm2(rh,rl),
        }
    print("\n",sector)
    for k,v in row.items():
        if k!="sector": print(k,"=",v)
    return row

def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    OUT.write_text(json.dumps({"rows":rows},indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
