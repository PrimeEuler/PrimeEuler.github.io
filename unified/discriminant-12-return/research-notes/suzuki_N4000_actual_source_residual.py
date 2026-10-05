#!/usr/bin/env python3
"""Residual of the actually reconstructed N=4000 source solution.

The K=10 absolute moments must be bounded on the actual source vector x_N,
not by separately triangle-bounding the seven Feshbach columns.  Reconstruct
x_N exactly as the v14.020 producer does, split it back into LDDD coordinates,
and evaluate

    r = A x_N - f

with the source-faithful LDDD matvec.

Report ||r||_2 and the weighted Cauchy-Schwarz error coefficients
    ||m^23||_2, || |z| m^22 ||_2,
so that any certified Euclidean solution-error bound ||dx|| immediately yields
outward moment increments.

Diagnostic only until paired with an exact finite-section coercivity/error
bound for x_N.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp
import numpy as np

from suzuki_N4000_far_geometric_remainder_diagnostic import reconstruct_source
from suzuki_ldd_source_operator import (
    LD, hp_parity_data_ld as hp_parity_data, matvec as dd_matvec,
    split_mpf_ld, sub as dd_sub, norm2 as dd_norm2, ldd_to_mpf,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"N4000_actual_source_residual_result.json"
DPS=180

def one_sector(sector):
    st=reconstruct_source(sector)
    modes=st["modes"]
    data=hp_parity_data(modes,sector,dps=DPS,arch_terms=160,correction_terms=50)
    xh=np.empty(len(modes),dtype=LD); xl=np.empty(len(modes),dtype=LD)
    for i,x in enumerate(st["xmp"]):
        xh[i],xl[i]=split_mpf_ld(x)
    Axh,Axl=dd_matvec(data,xh,xl)
    rh,rl=dd_sub(Axh,Axl,data.source_hi,data.source_lo)
    rnorm=dd_norm2(rh,rl)

    with mp.workdps(DPS):
        mm=[mp.mpf(int(m)) for m in modes]
        zz=[abs(ldd_to_mpf(data.z_hi[i],data.z_lo[i])) for i in range(len(modes))]
        w23=mp.sqrt(mp.fsum(m**46 for m in mm))
        wz22=mp.sqrt(mp.fsum((z*m**22)**2 for m,z in zip(mm,zz)))
        xnorm=mp.sqrt(mp.fsum(abs(x)**2 for x in st["xmp"]))
        row={
          "sector":sector,
          "capacity":mp.nstr(st["C"],70),
          "x_l2_midpoint":mp.nstr(xnorm,60),
          "actual_source_residual_l2":rnorm,
          "weight23_l2":mp.nstr(w23,60),
          "weightz22_l2":mp.nstr(wz22,60),
          "moment_error_if_dx_1e3_S23":mp.nstr(w23*mp.mpf("1e3"),50),
          "moment_error_if_dx_1e3_Sz22":mp.nstr(wz22*mp.mpf("1e3"),50),
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
