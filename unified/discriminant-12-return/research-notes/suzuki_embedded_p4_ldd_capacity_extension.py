#!/usr/bin/env python3
"""Parameterized wrapper for the frozen-N=4000 embedded-P4 LDDD capacity gate.

This reuses the v14.013 implementation without changing the protected plane.
Only the target finite cutoff is changed.  The purpose is a convergence
profile, not carrier regeneration.

Examples:
  python suzuki_embedded_p4_ldd_capacity_extension.py --target-max 12000
  python suzuki_embedded_p4_ldd_capacity_extension.py --target-max 16000
"""
from __future__ import annotations

import argparse
from pathlib import Path

import suzuki_M8000_embedded_p4_ldd_capacity as gate


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target-max", type=int, required=True)
    args = ap.parse_args()

    if args.target_max <= gate.BASE_MAX:
        raise SystemExit("target-max must exceed the frozen base cutoff 4000")
    if args.target_max % 2 != 0:
        raise SystemExit("target-max must be even so both parity sections end naturally")

    gate.TARGET_MAX = int(args.target_max)
    gate.OUT = (
        Path(__file__).resolve().parent
        / f"embedded_p4_ldd_capacity_M{args.target_max}_result.json"
    )
    gate.main()


if __name__ == "__main__":
    main()
