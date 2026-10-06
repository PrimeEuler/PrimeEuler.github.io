#!/usr/bin/env python3
"""M=16000 arch-200 correlated capacity residual-energy replay.

Thin wrapper around the audited M8000 arch-200 diagnostic, changing only the
zero-extended frozen-P4 target cutoff to 16000 and the output path.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path

import suzuki_M8000_embedded_p4_ldd_capacity as capgate
capgate.TARGET_MAX=16000

import suzuki_M8000_capacity_variational_residual_energy_arch200 as diag

diag.OUT=Path(__file__).resolve().parent/"M16000_capacity_variational_residual_energy_arch200_result.json"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    row=diag.one_sector(a.sector)
    diag.OUT.write_text(json.dumps({"rows":[row]},indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
