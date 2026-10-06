#!/usr/bin/env python3
"""Incremental arch-200 scalar interval audit on 32000 < n <= 64000.

The 16000<n<=32000 extension was already replayed.  Its only apparent failure
came from comparing against a tighter internal pre-promotion z cap; the public
v14.058 theorem cap is |Delta z|<5.88e-39 and contains the observed 32k
extension maximum 5.877332881956699e-39.

This script checks only new modes 32000<n<=64000 against the promoted public
caps.  Matrix intervals are not formed.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import mpmath as mp
import numpy as np

import suzuki_M8000_scalar_interval_audit_arch200 as audit
from suzuki_ldd_source_operator import hp_parity_data_ld as hp_parity_data, ldd_to_mpf

HERE=Path(__file__).resolve().parent
OUT=HERE/"M64000_scalar_interval_incremental_arch200_result.json"
LO=32000
HI=64000

# Public promoted caps from v14.058/v14.059.  The z cap is intentionally the
# displayed theorem cap, not a tighter internal maximum from the 16k producer.
CAPS={
 "even-v":{"z":5.88e-39,"d":4.318e-37,"p":7.366e-40},
 "odd-v":{"z":5.88e-39,"d":1.176e-38,"p":4.988e-41},
}

def modes(sector):
    start=LO+1 if sector=="even-v" else LO+2
    return np.arange(start,HI+1,2,dtype=int)

def one(sector):
    ns=modes(sector)
    data=hp_parity_data(ns,sector,dps=audit.MPDPS,
                        arch_terms=audit.ARCH_TERMS,
                        correction_terms=audit.CORR_TERMS)
    mz=(0.0,None); md=(0.0,None); mpole=(0.0,None)
    for i,n in enumerate(ns):
        z,d,p=audit.exact_scalar_intervals(int(n),sector)
        ez=audit.abs_error_bound(z,ldd_to_mpf(data.z_hi[i],data.z_lo[i]))
        ed=audit.abs_error_bound(d,ldd_to_mpf(data.diag_hi[i],data.diag_lo[i]))
        ep=audit.abs_error_bound(p,ldd_to_mpf(data.pole_hi[i],data.pole_lo[i]))
        if ez>mz[0]: mz=(ez,int(n))
        if ed>md[0]: md=(ed,int(n))
        if ep>mpole[0]: mpole=(ep,int(n))
        if (i+1)%500==0:
            print(sector,"checked",i+1,"/",len(ns),"max",mz,md,flush=True)
    caps=CAPS[sector]
    row={
      "sector":sector,"first_mode":int(ns[0]),"last_mode":int(ns[-1]),
      "dimension":len(ns),
      "extension_max_z":{"value":mz[0],"mode":mz[1]},
      "extension_max_diag":{"value":md[0],"mode":md[1]},
      "extension_max_pole":{"value":mpole[0],"mode":mpole[1]},
      "public_caps":caps,
      "passes_z_cap":mz[0] <= caps["z"],
      "passes_diag_cap":md[0] <= caps["d"],
      "passes_pole_cap":mpole[0] <= caps["p"],
    }
    row["passes_all_public_caps"]=all(
      row[k] for k in ("passes_z_cap","passes_diag_cap","passes_pole_cap")
    )
    print(json.dumps(row,indent=2),flush=True)
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    oldiv=mp.iv.dps
    mp.iv.dps=audit.IVDPS
    mp.mp.dps=audit.MPDPS
    try:
        row=one(a.sector)
    finally:
        mp.iv.dps=oldiv
    OUT.write_text(json.dumps(row,indent=2,sort_keys=True)+"\n")
    if not row["passes_all_public_caps"]:
        raise RuntimeError(("public v14.058 scalar caps do not transport through 64k",row))

if __name__=="__main__":
    main()
