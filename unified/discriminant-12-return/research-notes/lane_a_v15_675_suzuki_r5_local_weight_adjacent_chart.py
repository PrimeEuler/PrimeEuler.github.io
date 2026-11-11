#!/usr/bin/env python3
"""Outward fixed-local-weight chart on adjacent exact R=5 cut arcs.

The positive weight is frozen from 40 power steps on |B^4| at the v15.671
center arc x=1.  The same weight is then tested on a contiguous window of
neighboring v15.650 exact cut arcs.  Every reported PASS is an individual
weighted-Collatz upper certificate; this is not an exhaustive C5/C16 bound.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import hashlib
import json
import time
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product

import numpy as np

BASE = (
    "unified/discriminant-12-return/research-notes/"
    "lane_a_v15_664_suzuki_r3_outward_degree4_certificate.py"
)
spec = spec_from_file_location("base", BASE)
base = module_from_spec(spec)
spec.loader.exec_module(base)

R = 5
CENTER = 8651
RADIUS = 8
POWER_STEPS = 40
TARGET4 = F(41, 10) ** 4
CUTS = base.producer.cuts(R)
ARC_COUNT = len(CUTS)
assert ARC_COUNT == 17303
assert 0 <= CENTER - RADIUS and CENTER + RADIUS + 1 < ARC_COUNT


def cut_interval(k):
    value = (F(), F())
    for ki, q in zip(k, (2, 3, 5, 7)):
        value = base.add(value, base.scale(base.LS[q], -ki))
    return base.mod2(value)


# Certify the full R=5 ordering, then certify every binary64 chart midpoint
# lies strictly inside its intended exact-log cut arc with the audited margin.
EXACT_CUTS = []
for k0 in range(-R - 1, R + 2):
    for k1, k2, k3 in product(range(-R, R + 1), repeat=3):
        EXACT_CUTS.append(cut_interval((k0, k1, k2, k3)))
EXACT_CUTS.sort(key=lambda z: z[0])
for left, right in zip(EXACT_CUTS, EXACT_CUTS[1:]):
    assert left[1] < right[0]
assert len(EXACT_CUTS) == ARC_COUNT


def certified_midpoint(index):
    midpoint = (float(CUTS[index]) + float(CUTS[index + 1])) / 2
    midpoint_fraction = F.from_float(midpoint)
    assert midpoint_fraction > EXACT_CUTS[index][1] + base.MARGIN
    assert midpoint_fraction < EXACT_CUTS[index + 1][0] - base.MARGIN
    return midpoint_fraction


def observed_row_sum(matrix):
    k = int(np.diff(matrix.indptr).max())
    value = float(np.asarray(abs(matrix).sum(axis=1)).ravel().max())
    return F.from_float(value), k


center_midpoint = certified_midpoint(CENTER)
assert center_midpoint == 1
center_b = base.producer.assemble(R, float(center_midpoint))
center_b2 = center_b @ center_b
center_abs_b4 = abs(center_b2 @ center_b2)
weight = np.ones(center_b.shape[0], dtype=np.float64)
for _ in range(POWER_STEPS):
    weight = np.asarray(center_abs_b4 @ weight).ravel()
    weight /= weight.max()
assert np.all(weight > 0)
weight_condition = F.from_float(float(weight.max())) / F.from_float(float(weight.min()))
weight_sha256 = hashlib.sha256(weight.tobytes(order="C")).hexdigest()
del center_b, center_b2, center_abs_b4


def evaluate(index):
    x_fraction = certified_midpoint(index)
    x = float(x_fraction)
    started = time.time()
    b = base.producer.assemble(R, x)
    b2 = b @ b
    b4 = b2 @ b2
    obs1, k1 = observed_row_sum(b)
    obs2, k2 = observed_row_sum(b2)
    k4 = int(np.diff(b4.indptr).max())
    m = obs1 / (1 - base.gamma(k1))
    c2 = obs2 / (1 - base.gamma(k2))
    r2 = base.gamma(2 * k1) * m * m
    r4 = r2 * (m * m + c2) + base.gamma(2 * k2) * c2 * c2
    perturb = (m + base.E) ** 4 - m ** 4
    ratios = np.asarray(abs(b4) @ weight).ravel() / weight
    observed = F.from_float(float(ratios.max()))
    stored_upper = observed / (1 - base.gamma(2 * k4 + 1))
    true_upper = stored_upper + weight_condition * (r4 + perturb)
    return {
        "index": index,
        "midpoint_numerator": x_fraction.numerator,
        "midpoint_denominator": x_fraction.denominator,
        "midpoint_float": x,
        "outward_weighted_b4": float(true_upper),
        "outward_fourth_root": float(true_upper) ** 0.25,
        "pass": true_upper < TARGET4,
        "seconds": time.time() - started,
    }


if __name__ == "__main__":
    print("R", R, "ARC_COUNT", ARC_COUNT, "CENTER", CENTER, "RADIUS", RADIUS)
    print("POWER_STEPS", POWER_STEPS, "WEIGHT_MIN", weight.min(),
          "WEIGHT_MAX", weight.max(), "WEIGHT_CONDITION", float(weight_condition))
    print("WEIGHT_SHA256", weight_sha256)
    rows = []
    for index in range(CENTER - RADIUS, CENTER + RADIUS + 1):
        row = evaluate(index)
        rows.append(row)
        print("ARC", json.dumps(row, sort_keys=True), flush=True)
    worst = max(rows, key=lambda z: z["outward_weighted_b4"])
    by_index = {row["index"]: row for row in rows}
    component_left = CENTER
    while by_index[component_left - 1]["pass"]:
        component_left -= 1
    component_right = CENTER
    while by_index[component_right + 1]["pass"]:
        component_right += 1
    print("SUMMARY", json.dumps({
        "first_index": rows[0]["index"],
        "last_index": rows[-1]["index"],
        "arc_count": len(rows),
        "all_pass": all(row["pass"] for row in rows),
        "center_pass_component": [component_left, component_right],
        "center_pass_component_arc_count": component_right - component_left + 1,
        "left_boundary_failure": by_index[component_left - 1],
        "right_boundary_failure": by_index[component_right + 1],
        "target4": float(TARGET4),
        "worst": worst,
    }, sort_keys=True))
    print("STATUS=OUTWARD_CONTIGUOUS_LOCAL_WEIGHT_CHART")
    print("NO_EXHAUSTIVE_C5_OR_C16_CERTIFICATE")
