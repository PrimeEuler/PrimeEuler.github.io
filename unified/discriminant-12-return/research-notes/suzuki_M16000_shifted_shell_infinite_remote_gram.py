#!/usr/bin/env python3
"""Run the shifted-shell infinite remote-Gram gate with M=16000.

The frozen N=4000 protected carrier is unchanged.  Only the finite front
cutoff is extended from 8000 to 16000 before the infinite remote tail is
attached.
"""
from pathlib import Path

import suzuki_M8000_embedded_p4_ldd_capacity as capgate
import suzuki_M8000_shifted_shell_infinite_remote_gram as gate

capgate.TARGET_MAX=16000
gate.OUT=(
    Path(__file__).resolve().parent
    / "M16000_shifted_shell_infinite_remote_gram_result.json"
)

if __name__=="__main__":
    gate.main()
