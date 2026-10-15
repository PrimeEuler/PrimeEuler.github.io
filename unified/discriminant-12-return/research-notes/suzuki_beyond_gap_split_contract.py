#!/usr/bin/env python3
"""Emit the exact direct-middle/far index split after the v14.405 compact support."""

import argparse
import json
from fractions import Fraction
from pathlib import Path

U = 1_040_383
K = 42


def sector_record(name: str, parity_offset: int) -> dict:
    compact_last_index = U - 1
    direct_middle_first_index = U
    direct_middle_last_index = 2 * U - 1
    far_first_index = 2 * U
    mode = lambda index: 2 * index + parity_offset
    ratio = Fraction(mode(compact_last_index), mode(far_first_index))
    assert ratio < Fraction(1, 2)
    return {
        "sector": name,
        "compact_last_index": compact_last_index,
        "compact_last_mode": mode(compact_last_index),
        "direct_middle_first_index": direct_middle_first_index,
        "direct_middle_first_mode": mode(direct_middle_first_index),
        "direct_middle_last_index": direct_middle_last_index,
        "direct_middle_last_mode": mode(direct_middle_last_index),
        "direct_middle_row_count": U,
        "far_first_index": far_first_index,
        "far_first_mode": mode(far_first_index),
        "compact_to_far_endpoint_ratio": f"{ratio.numerator}/{ratio.denominator}",
        "compact_to_far_endpoint_ratio_lt_one_half": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = {
        "schema": "cone.beyond-gap-direct-middle-far-split.v1",
        "compact_index_count": U,
        "moment_order": K,
        "geometric_power": 2 * K,
        "half_power_upper": "1/19342813113834066795298816",
        "sectors": [sector_record("even-v", 1), sector_record("odd-v", 2)],
        "direct_middle_rows_evaluated": False,
        "beyond_gap_residual_evaluated": False,
        "whole_action_evaluated": False,
        "stationary_cone_closed": False,
        "infinite_capacity_tail_closed": False,
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
