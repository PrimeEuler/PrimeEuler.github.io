#!/usr/bin/env python3
"""Adaptive outward weighted-B4 chart-cover benchmark on an exact R=5 window.

Greedy rule: at the first uncovered arc, recompute a 40-step positive weight
from |B^4|, extend that frozen weight rightward through consecutive certified
PASS arcs, and restart at the first failure.  The deterministic 33-arc window
is a resource/architecture gate only, not an exhaustive C5/C16 certificate.
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
WINDOW_RADIUS = 16
FIRST = CENTER - WINDOW_RADIUS
LAST = CENTER + WINDOW_RADIUS
POWER_STEPS = 40
TARGET4 = F(41, 10) ** 4
CUTS = base.producer.cuts(R)
ARC_COUNT = len(CUTS)
assert ARC_COUNT == 17303
assert 0 <= FIRST <= LAST + 1 < ARC_COUNT


def cut_interval(k):
    value = (F(), F())
    for ki, q in zip(k, (2, 3, 5, 7)):
        value = base.add(value, base.scale(base.LS[q], -ki))
    return base.mod2(value)


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


def assemble_powers(index):
    x_fraction = certified_midpoint(index)
    b = base.producer.assemble(R, float(x_fraction))
    b2 = b @ b
    b4 = b2 @ b2
    return x_fraction, b, b2, b4


def local_weight(absolute_b4):
    weight = np.ones(absolute_b4.shape[0], dtype=np.float64)
    for _ in range(POWER_STEPS):
        weight = np.asarray(absolute_b4 @ weight).ravel()
        weight /= weight.max()
    assert np.all(weight > 0)
    condition = F.from_float(float(weight.max())) / F.from_float(float(weight.min()))
    digest = hashlib.sha256(weight.tobytes(order="C")).hexdigest()
    return weight, condition, digest


def evaluate_powers(index, x_fraction, b, b2, b4, weight, condition):
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
    true_upper = stored_upper + condition * (r4 + perturb)
    return {
        "index": index,
        "midpoint_numerator": x_fraction.numerator,
        "midpoint_denominator": x_fraction.denominator,
        "outward_weighted_b4": float(true_upper),
        "outward_fourth_root": float(true_upper) ** 0.25,
        "pass": true_upper < TARGET4,
    }


def evaluate(index, weight, condition):
    x_fraction, b, b2, b4 = assemble_powers(index)
    return evaluate_powers(index, x_fraction, b, b2, b4, weight, condition)


if __name__ == "__main__":
    started = time.time()
    print("R", R, "ARC_COUNT", ARC_COUNT, "WINDOW", FIRST, LAST,
          "WINDOW_ARCS", LAST - FIRST + 1, "POWER_STEPS", POWER_STEPS)
    charts = []
    index = FIRST
    local_anchor_failure = None
    evaluations = 0
    while index <= LAST:
        anchor = index
        x_fraction, b, b2, b4 = assemble_powers(anchor)
        weight, condition, digest = local_weight(abs(b4))
        anchor_row = evaluate_powers(anchor, x_fraction, b, b2, b4, weight, condition)
        evaluations += 1
        print("ANCHOR", json.dumps({
            "anchor": anchor,
            "weight_condition": float(condition),
            "weight_sha256": digest,
            "anchor_result": anchor_row,
        }, sort_keys=True), flush=True)
        if not anchor_row["pass"]:
            local_anchor_failure = anchor_row
            break
        last_pass = anchor
        boundary_failure = None
        index = anchor + 1
        while index <= LAST:
            row = evaluate(index, weight, condition)
            evaluations += 1
            print("EXTEND", json.dumps({"anchor": anchor, "result": row},
                                       sort_keys=True), flush=True)
            if not row["pass"]:
                boundary_failure = row
                break
            last_pass = index
            index += 1
        charts.append({
            "anchor": anchor,
            "last_pass": last_pass,
            "covered_arcs": last_pass - anchor + 1,
            "weight_condition": float(condition),
            "weight_sha256": digest,
            "anchor_fourth_root": anchor_row["outward_fourth_root"],
            "boundary_failure": boundary_failure,
        })
        print("CHART", json.dumps(charts[-1], sort_keys=True), flush=True)
        if boundary_failure is None:
            index = LAST + 1
        else:
            index = boundary_failure["index"]
    print("SUMMARY", json.dumps({
        "window": [FIRST, LAST],
        "window_arcs": LAST - FIRST + 1,
        "chart_count": len(charts),
        "charts": charts,
        "evaluations": evaluations,
        "locally_certified_cover": local_anchor_failure is None and index > LAST,
        "local_anchor_failure": local_anchor_failure,
        "seconds": time.time() - started,
        "target4": float(TARGET4),
    }, sort_keys=True))
    print("STATUS=ADAPTIVE_EXACT_CUT_WINDOW_BENCHMARK")
    print("NO_EXHAUSTIVE_C5_OR_C16_CERTIFICATE")
