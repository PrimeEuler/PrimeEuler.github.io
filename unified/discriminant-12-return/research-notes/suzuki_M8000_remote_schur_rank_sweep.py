#!/usr/bin/env python3
"""Deterministic rank sweep for the M=8000 remote-Schur near-block compression.

At rmax=16000 the K=10 separated-tail channels are inactive, so the discrepancy
from the theorem M8000->M16000 shell isolates the rank-r approximation of the
exact 8000<n<16000 front-to-near coupling (plus tiny FFT/CG arithmetic).

For each requested rank and sector, run the canonical remote-Schur diagnostic,
compare eta_tail_midpoint to the promoted v14.059 theorem midpoint, and report
absolute/relative error.  This is a diagnostic acceptance gate only.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import suzuki_M8000_remote_schur_fft_diagnostic as base

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_remote_schur_rank_sweep_result.json"
TARGET={
 "even-v":0.0036404008257719944,
 "odd-v":0.003617497467397701,
}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    ap.add_argument("--rank",type=int,required=True)
    a=ap.parse_args()
    if not (1<=a.rank<3999):
        raise SystemExit("rank out of range")
    base.RANK=int(a.rank)
    row=base.one(a.sector,16000)
    target=TARGET[a.sector]
    err=row["eta_tail_midpoint"]-target
    out={
      "sector":a.sector,
      "rank":a.rank,
      "eta_remote":row["eta_tail_midpoint"],
      "eta_theorem_midpoint":target,
      "signed_error":err,
      "absolute_error":abs(err),
      "relative_error":abs(err)/abs(target),
      "cg_residual_l2":row["cg_residual_l2"],
      "front_target_residual":row["front_target_residual"],
      "guardrail":"Diagnostic rank acceptance against v14.059 theorem midpoint."
    }
    print(json.dumps(out,indent=2))
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
