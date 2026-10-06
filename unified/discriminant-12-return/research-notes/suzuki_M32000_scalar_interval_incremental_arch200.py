#!/usr/bin/env python3
"""Incremental arch-200 scalar interval audit on 16000 < n <= 32000.

The full through-16000 replay is already certified.  This script checks only
new modes and compares their exact interval-vs-LDDD representation errors to
the promoted through-16000 uniform caps.  If every extension maximum is below
the corresponding old cap, those caps remain valid through 32000.

No matrix interval is formed.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp
import numpy as np

import suzuki_M8000_scalar_interval_audit_arch200 as audit
from suzuki_ldd_source_operator import hp_parity_data_ld as hp_parity_data, ldd_to_mpf

HERE=Path(__file__).resolve().parent
OUT=HERE/"M32000_scalar_interval_incremental_arch200_result.json"
LO=16000
HI=32000

OLD={
 "even-v":{"z":5.862773801458821e-39,"d":4.317700732362615e-37,
           "p":7.365230177656668e-40,"c":6.740593794183538e-42},
 "odd-v":{"z":5.876097431412404e-39,"d":1.1754198692159515e-38,
          "p":4.987119893996533e-41,"c":6.740593794183538e-42},
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
    old=OLD[sector]
    row={
      "sector":sector,"first_mode":int(ns[0]),"last_mode":int(ns[-1]),
      "dimension":len(ns),
      "extension_max_z":{"value":mz[0],"mode":mz[1]},
      "extension_max_diag":{"value":md[0],"mode":md[1]},
      "extension_max_pole":{"value":mpole[0],"mode":mpole[1]},
      "old_caps":old,
      "passes_old_z_cap":mz[0] <= old["z"],
      "passes_old_diag_cap":md[0] <= old["d"],
      "passes_old_pole_cap":mpole[0] <= old["p"],
    }
    row["passes_all_old_caps"]=all(
      row[k] for k in ("passes_old_z_cap","passes_old_diag_cap","passes_old_pole_cap")
    )
    print(json.dumps(row,indent=2),flush=True)
    return row

def main():
    oldiv=mp.iv.dps
    mp.iv.dps=audit.IVDPS
    mp.mp.dps=audit.MPDPS
    try:
        rows=[one("even-v"),one("odd-v")]
    finally:
        mp.iv.dps=oldiv
    out={"lo_exclusive":LO,"hi_inclusive":HI,"rows":rows,
         "passes_all":all(r["passes_all_old_caps"] for r in rows)}
    print(json.dumps(out,indent=2),flush=True)
    if not out["passes_all"]:
        raise RuntimeError(("through-16000 scalar caps do not transport unchanged",rows))
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
