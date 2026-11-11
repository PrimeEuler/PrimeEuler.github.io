#!/usr/bin/env python3
"""R=5 fixed-weight signed-B^4 Collatz resource probe.

Builds one deterministic positive weight from 40 power steps on |B^4| at
the v15.668 anchor, then evaluates an outward weighted row bound on 32 fixed
R=5 arcs.  This is a sampled architecture test, not an exhaustive C5 bound.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import hashlib
import json
import time
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location

import numpy as np

BASE = (
    "unified/discriminant-12-return/research-notes/"
    "lane_a_v15_664_suzuki_r3_outward_degree4_certificate.py"
)
spec = spec_from_file_location("base", BASE)
base = module_from_spec(spec)
spec.loader.exec_module(base)

R = 5
ANCHOR_TARGET = 0.05145728861651011
POWER_STEPS = 40
SAMPLE_COUNT = 32
CUTS = base.producer.cuts(R)
ARC_COUNT = len(CUTS)
assert ARC_COUNT == 17303
INDICES = [j * ARC_COUNT // SAMPLE_COUNT for j in range(SAMPLE_COUNT)]


def midpoint(index):
    wrap = index + 1 == ARC_COUNT
    right = CUTS[(index + 1) % ARC_COUNT] + (2 if wrap else 0)
    return float(((CUTS[index] + right) / 2) % 2)


anchor_index = int(np.searchsorted(CUTS, ANCHOR_TARGET) - 1) % ARC_COUNT
anchor_b = base.producer.assemble(R, midpoint(anchor_index))
anchor_b2 = anchor_b @ anchor_b
anchor_abs_b4 = abs(anchor_b2 @ anchor_b2)
weight = np.ones(anchor_b.shape[0], dtype=np.float64)
for _ in range(POWER_STEPS):
    weight = np.asarray(anchor_abs_b4 @ weight).ravel()
    weight /= weight.max()
assert np.all(weight > 0)
weight_condition = F.from_float(float(weight.max())) / F.from_float(float(weight.min()))
weight_sha256 = hashlib.sha256(weight.tobytes(order="C")).hexdigest()
del anchor_b, anchor_b2, anchor_abs_b4


def observed_row_sum(matrix):
    k = int(np.diff(matrix.indptr).max())
    value = float(np.asarray(abs(matrix).sum(axis=1)).ravel().max())
    return F.from_float(value), k


def evaluate(index):
    x = midpoint(index)
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

    # Each weighted row uses k4 multiplications and k4-1 additions, followed
    # by one division by the positive stored float weight.
    ratios = np.asarray(abs(b4) @ weight).ravel() / weight
    observed = F.from_float(float(ratios.max()))
    stored_upper = observed / (1 - base.gamma(2 * k4 + 1))
    true_upper = stored_upper + weight_condition * (r4 + perturb)
    return {
        "index": index,
        "x": x,
        "b4_nnz": int(b4.nnz),
        "k4": k4,
        "observed_weighted_b4": float(observed),
        "outward_weighted_b4": float(true_upper),
        "outward_fourth_root": float(true_upper) ** 0.25,
        "seconds": time.time() - started,
    }


if __name__ == "__main__":
    print("ANCHOR_INDEX", anchor_index, "ANCHOR_MIDPOINT", midpoint(anchor_index))
    print("POWER_STEPS", POWER_STEPS, "WEIGHT_MIN", weight.min(),
          "WEIGHT_MAX", weight.max(), "WEIGHT_CONDITION", float(weight_condition))
    print("WEIGHT_SHA256", weight_sha256)
    rows = []
    for index in INDICES:
        row = evaluate(index)
        rows.append(row)
        print("ARC", json.dumps(row, sort_keys=True), flush=True)
    best = max(rows, key=lambda z: z["outward_weighted_b4"])
    print("SUMMARY", json.dumps({
        "arc_count": ARC_COUNT,
        "sample_count": SAMPLE_COUNT,
        "indices": INDICES,
        "maximum": best,
        "target4": 4.10 ** 4,
        "all_sampled_pass": best["outward_weighted_b4"] < 4.10 ** 4,
    }, sort_keys=True))
    print("STATUS=OUTWARD_FIXED_SAMPLE_ARCHITECTURE_PROBE_ONLY")
    print("NO_EXHAUSTIVE_C5_OR_C16_CERTIFICATE")
