#!/usr/bin/env python3
"""Gravity v15.837: additive historical version-collision reconciliation.

External Audit Round 562 used ledger version v15.836 while gravity's
free-tensor causal-front script and separate ledger used v15.836.
Both committed objects remain unchanged and correctly attributed.
This additive uniquely numbered wrapper reexecutes the original gravity
v15.836 script and preserves its exact scientific result.
"""
from pathlib import Path
import runpy
path=Path(__file__).with_name("k4_remote_tensor_causal_front_v15_836.py")
assert path.is_file()
runpy.run_path(str(path),run_name="__main__")
print("PASS gravity v15.837 exact historical v15.836 tensor-front replay")
