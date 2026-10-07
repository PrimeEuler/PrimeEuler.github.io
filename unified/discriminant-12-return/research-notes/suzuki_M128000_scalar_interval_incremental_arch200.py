#!/usr/bin/env python3
"""Incremental arch-200 scalar interval audit on 64000 < n <= 128000.

Reuses the promoted public scalar caps and the validated M64000 incremental
audit machinery, changing only the octave endpoints.  FAIL CLOSED if any
new mode exceeds a public cap.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import mpmath as mp

import suzuki_M64000_scalar_interval_incremental_arch200 as base

base.LO = 64000
base.HI = 128000
base.OUT = Path(__file__).resolve().parent / "M128000_scalar_interval_incremental_arch200_result.json"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    oldiv=mp.iv.dps
    mp.iv.dps=base.audit.IVDPS
    mp.mp.dps=base.audit.MPDPS
    try:
        row=base.one(a.sector)
    finally:
        mp.iv.dps=oldiv
    base.OUT.write_text(json.dumps(row,indent=2,sort_keys=True)+"\n")
    if not row["passes_all_public_caps"]:
        raise RuntimeError(("public scalar caps do not transport through 128k",row))

if __name__=="__main__":
    main()
