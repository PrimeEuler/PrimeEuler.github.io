#!/usr/bin/env python3
"""Actual N=4000 K=10 absolute moments of the refined source vector.

This is a midpoint/correlation diagnostic, not yet an outward certificate.
Unlike the seven-column triangle surrogate, reconstruct the actual LDDD-refined
source x_N first and only then take |x_m|.  Report the two quantities consumed
by v14.022/v14.047:

    S23   = sum m^23 |x_m|,
    Sz22  = sum |z_m| m^22 |x_m|.

Also report the resulting v14.047 far-remainder functional using the current
midpoint sqrt(C).  The purpose is to determine the outward inflation headroom
available for a correlated source-vector interval.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp

from suzuki_N4000_far_geometric_remainder_diagnostic import reconstruct_source

HERE=Path(__file__).resolve().parent
OUT=HERE/"N4000_K10_actual_absolute_moments_result.json"
DPS=180

def one_sector(sector):
    state=reconstruct_source(sector)
    with mp.workdps(DPS):
        modes=[mp.mpf(int(m)) for m in state["modes"]]
        ax=[abs(x) for x in state["xmp"]]
        az=[abs(z) for z in state["zmp"]]
        s23=mp.fsum(m**23*x for m,x in zip(modes,ax))
        sz22=mp.fsum(z*m**22*x for m,z,x in zip(modes,az,ax))
        sqrtc=mp.sqrt(state["C"])
        # v14.047 coefficient before the 0.46 energy factor.
        u10_proxy=sqrtc*(mp.mpf("1.37e-89")*sz22+mp.mpf("1.58e-92")*s23)
        far_cross_proxy=mp.mpf("0.46")*u10_proxy
        row={
          "sector":sector,
          "capacity":mp.nstr(state["C"],70),
          "sqrt_capacity":mp.nstr(sqrtc,60),
          "S23_actual_midpoint":mp.nstr(s23,70),
          "Sz22_actual_midpoint":mp.nstr(sz22,70),
          "v14047_U10_proxy":mp.nstr(u10_proxy,60),
          "v14047_far_cross_proxy":mp.nstr(far_cross_proxy,60),
          "S23_headroom_to_2p9e98":mp.nstr(mp.mpf("2.9e98")/s23,40),
          "Sz22_headroom_to_3p4e95":mp.nstr(mp.mpf("3.4e95")/sz22,40),
          "refined_max_joint_residual":state["refined_max_joint_residual"],
        }
    print("\n",sector)
    for k,v in row.items():
        if k!="sector": print(k,"=",v)
    return row

def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    OUT.write_text(json.dumps({"rows":rows},indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)
    print("GUARDRAIL: midpoint actual-source moments; outward source-vector error pending.")

if __name__=="__main__":
    main()
