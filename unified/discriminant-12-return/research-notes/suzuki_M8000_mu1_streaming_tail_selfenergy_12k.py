#!/usr/bin/env python3
"""Short 12k wrapper for the streaming mu=1 tail self-energy diagnostic."""
from pathlib import Path
import suzuki_M8000_mu1_streaming_tail_selfenergy as gate

gate.MAX_MODE=12000
gate.CHECKPOINTS=(9000,10000,11000,12000)
gate.OUT=Path(__file__).resolve().parent/"M8000_mu1_streaming_tail_selfenergy_12k_result.json"

if __name__=="__main__":
    gate.main()
