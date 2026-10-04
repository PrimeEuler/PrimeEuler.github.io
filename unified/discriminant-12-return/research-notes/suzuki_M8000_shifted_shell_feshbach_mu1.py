#!/usr/bin/env python3
"""Probe a common Euclidean shell-Schur floor mu=1 at N=4000 -> M=8000."""
from pathlib import Path
import suzuki_M8000_shifted_shell_feshbach_ldd as gate

gate.TARGET_MU["even-v"]=1.0
gate.TARGET_MU["odd-v"]=1.0
gate.OUT=Path(__file__).resolve().parent/"M8000_shifted_shell_feshbach_mu1_result.json"

if __name__=="__main__":
    gate.main()
