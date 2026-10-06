#!/usr/bin/env python3
"""Parameterized arch-200 frozen-N=4000 embedded-P4 capacity extension.

Same carrier and solver as suzuki_embedded_p4_ldd_capacity_extension.py,
but forces the high-precision LDDD scalar producer to arch_terms=200.
Reported target capacities are load-bearing; eta fields emitted by the base
producer still use its arch-160 BASE_CAP and must not be consumed.
"""
from __future__ import annotations
import argparse
from pathlib import Path

import suzuki_M8000_embedded_p4_ldd_capacity as gate

_orig_hp=gate.hp_parity_data
def hp200(modes,sector,dps=180,arch_terms=160,correction_terms=50):
    return _orig_hp(
        modes,sector,dps=dps,arch_terms=200,correction_terms=correction_terms
    )

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--target-max",type=int,required=True)
    a=ap.parse_args()
    if a.target_max<=gate.BASE_MAX or a.target_max%2:
        raise SystemExit("target-max must be even and >4000")
    gate.TARGET_MAX=int(a.target_max)
    gate.hp_parity_data=hp200
    gate.OUT=Path(__file__).resolve().parent/f"embedded_p4_ldd_capacity_arch200_M{a.target_max}_result.json"
    gate.main()

if __name__=="__main__":
    main()
