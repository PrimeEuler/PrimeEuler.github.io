#!/usr/bin/env python3
"""Outward physical-parameter charge for the v14.277 compact Far action.

This consumer deliberately charges only the compact component.  It does not
evaluate the infinite seed-tail action or a residual norm.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

from suzuki_exact_integer_source_action import sqrt_upper


PINS = {
    "even-v": "93295c99ebaf579db0a942833a3222c78b4d3df1d3f7679b93beb6a5721c9df0",
    "odd-v": "5fcf693b58689629cd8990e071eeecf066c22d59da231c7bbbc69d854d1eaa64",
}


def tail_upper(a, p):
    """Spacing-two first-term-plus-integral upper bound."""
    assert p > 1
    return F(1, a**p) + F(1, 2 * (p - 1) * a ** (p - 1))


def load(path, pin):
    raw = path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == pin
    return json.loads(raw)


def run(root, sector):
    pin = PINS[sector]
    path = root / f"infinite-seed-compact-far-{sector}.json"
    action = load(path, pin)
    assert action["schema"] == "cone.infinite-seed-lift-compact-far-action.v1"
    assert action["sector"] == sector
    assert action["infinite_seed_tail_action_included"] is False
    assert action["physical_scalar_parameter_errors_included"] is False
    assert action["retained_point_coefficients_evaluated"] is True

    count = 256000
    a = action["far_first_mode"]
    xnorm = F(action["rational"]["combined_support_norm_upper"])
    l1 = sqrt_upper(F(count), 256) * xnorm
    n_inv_l2 = sqrt_upper(tail_upper(a, 2), 256)

    # v14.248's source-faithful component bounds apply unchanged to this
    # compact vector: displacement <=2e-38 ||x||_1/n and pole
    # <=5e-38 ||x||_1/n.  The published total 1e-36 envelope retains ample
    # room for their cross terms and is intentionally not tightened here.
    displacement = F("2e-38") * l1 * n_inv_l2
    pole = F("5e-38") * l1 * n_inv_l2
    combined = F("1e-36") * l1 * n_inv_l2
    assert displacement + pole <= combined

    values = {
        "compact_support_l1_upper": l1,
        "spacing_two_inverse_n_l2_upper": n_inv_l2,
        "displacement_parameter_charge_upper": displacement,
        "pole_parameter_charge_upper": pole,
        "combined_physical_parameter_charge_upper": combined,
    }
    return {
        "schema": "cone.infinite-seed-compact-far-parameter-charge.v1",
        "sector": sector,
        "compact_far_action_sha256": pin,
        "compact_far_action_file": path.name,
        "far_first_mode": a,
        "support_coordinate_count": count,
        "bound": "pointwise compact-action perturbation <= 1e-36*||x||_1/n",
        "tail_bound": "sum_{k>=0}(a+2k)^-2 <= a^-2+(2a)^-1",
        "component_contract": {
            "displacement_pointwise_coefficient": "2e-38",
            "pole_pointwise_coefficient": "5e-38",
            "retained_combined_pointwise_coefficient": "1e-36",
        },
        "rational": {key: str(value) for key, value in values.items()},
        "display_approximate": {
            key: float(values[key])
            for key in (
                "displacement_parameter_charge_upper",
                "pole_parameter_charge_upper",
                "combined_physical_parameter_charge_upper",
            )
        },
        "physical_scalar_parameter_errors_included_for_compact_far_action": True,
        "infinite_seed_tail_action_included": False,
        "near_middle_output_rows_evaluated": False,
        "whole_residual_norm_evaluated": False,
        "stationary_acceptance_met": False,
        "infinite_capacity_tail_closed": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--sector", choices=sorted(PINS), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.root, args.sector)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["display_approximate"], sort_keys=True))
