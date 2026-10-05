#!/usr/bin/env python3
"""One-row wrapper for the exact M8000 near-boundary correlated Gram.

A single diagonal energy b_n^* F^{-1} b_n is already a lower bound on the
full near-shell Schur correction norm.  This fast gate tests the first far
mode only in each parity.
"""
from pathlib import Path
import suzuki_M8000_mu1_exact_near_rows_gram as gate

gate.RCOUNT=1  # trigger replay after workflow installation
gate.OUT=Path(__file__).resolve().parent/"M8000_mu1_first_near_row_energy_result.json"

if __name__=="__main__":
    gate.main()
