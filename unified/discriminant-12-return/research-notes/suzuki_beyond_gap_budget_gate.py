#!/usr/bin/env python3
"""Exact v14.442 certificate-derived budget for a future beyond-gap residual.

This script DOES NOT evaluate the beyond-gap operator or certify closure.
It verifies exact Fraction arithmetic and emits sufficient physical-tail
requirements using already deposited certified finite-plus-gap bounds.
"""
import json
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parents[2] / "payloads/gap_extended_residual_return_v14_442"
# Source files currently deposited at repository root 'payloads', not research-notes/payloads.
if not BASE.exists():
    BASE = Path(__file__).resolve().parents[3] / "payloads/gap_extended_residual_return_v14_442"
CAP = F(3, 100000)


def run(sector):
    p = BASE / f"gap-extended-residual-{sector}.json"
    d = json.loads(p.read_bytes())
    assert d["sector"] == sector and d["finite_plus_gap_upper_below_3e_minus5"]
    assert not d["beyond_gap_residual_evaluated"]
    assert not d["whole_residual_acceptance_certified"]
    r = {k: F(v) for k, v in d["rational"].items()}
    f = r["whole_912383_point_norm_upper"]
    e = r["complete_912383_physical_error_upper"]
    t = r["global_source_and_new_lift_transport_once"]
    p_hi = r["physical_residual_upper"]
    s_hi = r["finite_plus_gap_Schur_residual_upper"]
    a = r["certified_beyond_gap_physical_residual_allowance"]
    assert f + e == p_hi
    assert p_hi + t == s_hi < CAP
    q = (CAP - t) ** 2 - p_hi ** 2
    assert q > 0 and a > 0 and a * a <= q
    # Sufficient condition: a certified bound on the *physical*
    # beyond-gap residual <= a (including all far-moment and tail errors).
    # Source and lift transport t charged only once globally, and supports disjoint.
    assert p_hi * p_hi + a * a <= (CAP - t) ** 2
    return {
        "sector": sector,
        "finite_plus_gap_schur_upper_approx": float(s_hi),
        "source_plus_lift_transport_once_approx": float(t),
        "new_beyond_gap_physical_residual_budget_approx": float(a),
        "budget_rational": str(a),
        "budget_squared_rational": str(a * a),
        "sufficient_condition": "certified beyond-gap physical L2 <= budget, disjoint support, global transport once",
        "beyond_gap_evaluated": False,
        "whole_acceptance_claimed": False,
    }


if __name__ == "__main__":
    print(json.dumps({s: run(s) for s in ("even-v", "odd-v")}, indent=2))
