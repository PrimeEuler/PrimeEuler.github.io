#!/usr/bin/env python3
"""Compatibility wrapper for the deterministic rank-24 Feshbach producer.

The canonical implementation is now
    suzuki_M8000_near_rank24_feshbach.py
which fixes the ARPACK start vector and forces single-thread linear algebra
before NumPy/SciPy import.  This wrapper remains only so older workflows and
audit references continue to resolve to the same numerical implementation.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

from suzuki_M8000_near_rank24_feshbach import one_sector

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_near_rank24_feshbach_deterministic_result.json"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    row=one_sector(a.sector)
    OUT.write_text(json.dumps({"rows":[row]},indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
