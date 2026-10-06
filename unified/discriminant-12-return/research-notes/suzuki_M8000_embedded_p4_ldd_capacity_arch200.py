#!/usr/bin/env python3
"""Arch-200 replay of the M=8000 embedded-P4 LDDD capacity reduction.

This is a thin theorem-target wrapper around the canonical
suzuki_M8000_embedded_p4_ldd_capacity producer.  It changes only the
high-precision scalar producer from arch_terms=160 to arch_terms=200.

The embedded frozen six-plane, binary64 complement correction solver,
LDDD residual refinement, and 7x7 augmented reduction are otherwise
identical to the canonical producer.

The output is still a numerical producer.  A separate outward budget consumes
v14.031's certified complement floors in place of the midpoint gamma and the
successful arch-200 scalar interval audit.
"""
from __future__ import annotations
import gc, json
from pathlib import Path
import mpmath as mp

import suzuki_M8000_embedded_p4_ldd_capacity as base

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_embedded_p4_ldd_capacity_arch200_result.json"
DPS=base.DPS

_orig_hp=base.hp_parity_data
def hp200(modes,sector,dps=180,arch_terms=160,correction_terms=50):
    return _orig_hp(
        modes,sector,dps=dps,arch_terms=200,correction_terms=correction_terms
    )
base.hp_parity_data=hp200

def main():
    rows=[base.one_sector("even-v"),base.one_sector("odd-v")]
    with mp.workdps(DPS):
        Ce=mp.mpf(rows[0]["capacity_midpoint_variational"])
        Co=mp.mpf(rows[1]["capacity_midpoint_variational"])
        summary={
          "Ce_arch200":mp.nstr(Ce,70),
          "Co_arch200":mp.nstr(Co,70),
          "q_arch200":mp.nstr(Ce/Co,60),
          "kappa_arch200":mp.nstr((Co-Ce)/(Co+Ce),60),
        }
    out={
      "arch_terms":200,
      "rows":rows,
      "summary":summary,
      "guardrail":(
        "Arch-200 numerical producer. Outward certification must replace the "
        "midpoint complement gamma by the v14.031 certified floor and consume "
        "the arch-200 scalar interval audit."
      )
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nARCH200 SUMMARY")
    print(json.dumps(summary,indent=2))
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
