#!/usr/bin/env python3
"""Gravity v15.878: additive replay after Audit/Gravity v15.877 label overlap.

External Audit Round 567 already claimed the globally shared v15.877
ledger number when Gravity's v15.877 Gertsenshtein scientific producer
was committed. Keep BOTH historical records unchanged. This unique
v15.878 entry executes the scientific script from a path relative to
this file for reproducibility and version distinction.
"""
from pathlib import Path
import runpy
parent=Path(__file__).resolve().parent
source=parent/"k4_einstein_maxwell_gertsenshtein_v15_877.py"
assert source.exists(),"Expected historical Gravity v15.877 producer"
runpy.run_path(str(source),run_name="__main__")
print("PASS Gravity v15.878 historical-number reconciliation replay")
