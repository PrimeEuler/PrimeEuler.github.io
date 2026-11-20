#!/usr/bin/env python3
"""Canonical Gravity v15.1266 launcher for additive composition gate.
External Audit Round 620 canonically owns v15.1265. The earlier
additively committed v15.1265-source-named integration script remains
untouched and is loaded here by explicit stable file path.
This run may take time/memory for the 48^3 Fourier mode grid.
"""
from pathlib import Path
import runpy

ROOT=Path(__file__).resolve().parent
PARENT=ROOT/"k4_maxwell_periodic_full_tide_zero_nonzero_weld_v15_1265.py"
if not PARENT.is_file():
    raise FileNotFoundError(PARENT)
module=runpy.run_path(str(PARENT),run_name="_v15_1265_library")
run=module["run_pair"]
if __name__=="__main__":
    rows=[run(N,tf=1.08) for N in (32,40,48)]
    assert all(r["full_trace_max_abs_error"]<3e-12 for r in rows)
    print("PASS canonical v15.1266 periodic-cell homogeneous+inhomogeneous tidal composition")
    print("No claim of continuum convergence or causal detector prediction.")
