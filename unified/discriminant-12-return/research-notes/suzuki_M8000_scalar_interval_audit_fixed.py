#!/usr/bin/env python3
"""Compatibility wrapper for the M8000 scalar interval audit.

mpmath 1.4.1's interval context does not expose cosh/sinh methods.
Define them from exp using interval arithmetic, then run the unchanged audit.
"""
import mpmath as mp

if not hasattr(mp.iv, "cosh"):
    mp.iv.cosh = lambda x: (mp.iv.exp(x) + mp.iv.exp(-x)) / 2
if not hasattr(mp.iv, "sinh"):
    mp.iv.sinh = lambda x: (mp.iv.exp(x) - mp.iv.exp(-x)) / 2

import suzuki_M8000_scalar_interval_audit as audit

if __name__ == "__main__":
    audit.main()
