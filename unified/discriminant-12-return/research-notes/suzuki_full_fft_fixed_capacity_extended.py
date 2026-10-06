#!/usr/bin/env python3
"""Capacity-only extension of the calibrated fixed full-lattice FFT solver.

This deliberately reuses solve_state() from suzuki_full_fft_fixed_capacity_replay
unchanged.  The only extension is allowing M=32000 or 64000, where there is no
pre-existing theorem target.  This halves the high-precision work relative to
the combined capacity+M11 producer and is intended to expose the finite shell
midpoint sooner.

Diagnostic only: no outward rounding and no theorem promotion.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import suzuki_full_fft_fixed_capacity_replay as base

HERE=Path(__file__).resolve().parent
OUT=HERE/"M_full_fft_fixed_capacity_extended_result.json"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    ap.add_argument("--cutoff",type=int,choices=[32000,64000],required=True)
    a=ap.parse_args()
    # solve_state expects a target only for display/error fields.  Register NaN
    # without touching any operator, solve, refinement, or capacity arithmetic.
    base.TARGET[(a.sector,a.cutoff)]=float("nan")
    row=base.solve_state(a.sector,a.cutoff)
    row["guardrail"]=(
        "Capacity-only fixed full-lattice FFT midpoint beyond 16k; "
        "same calibrated solver, no outward rounding or infinite-tail claim."
    )
    print(json.dumps(row,indent=2),flush=True)
    OUT.write_text(json.dumps(row,indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
