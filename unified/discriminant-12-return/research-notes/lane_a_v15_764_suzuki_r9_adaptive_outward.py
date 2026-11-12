#!/usr/bin/env python3
"""Exact R9 x=1 adaptive outward test: unweighted, then one update on failure."""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import hashlib
import json
import resource
import time
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product

import numpy as np

BASE_SOURCE = (
    "unified/discriminant-12-return/research-notes/"
    "lane_a_v15_664_suzuki_r3_outward_degree4_certificate.py"
)
spec = spec_from_file_location("base", BASE_SOURCE)
base = module_from_spec(spec)
spec.loader.exec_module(base)

R = 9
X = F(1)
BATCH_ROWS = 128
TARGET4 = F(41, 10) ** 4
EXPECTED_CUTS = (2 * R + 3) * (2 * R + 1) ** 3


def cut_interval(k):
    value = (F(), F())
    for ki, q in zip(k, (2, 3, 5, 7)):
        value = base.add(value, base.scale(base.LS[q], -ki))
    return base.mod2(value)


def exact_arc_containing_x():
    cuts = []
    for k0 in range(-R - 1, R + 2):
        for k1, k2, k3 in product(range(-R, R + 1), repeat=3):
            cuts.append(cut_interval((k0, k1, k2, k3)))
    cuts.sort(key=lambda z: z[0])
    assert len(cuts) == len(base.producer.cuts(R)) == EXPECTED_CUTS == 144039
    for left, right in zip(cuts, cuts[1:]):
        assert left[1] < right[0]
    candidates = [(i, l, r) for i, (l, r) in enumerate(zip(cuts, cuts[1:]))
                  if l[1] < X < r[0]]
    assert len(candidates) == 1
    index, left, right = candidates[0]
    assert X > left[1] + base.MARGIN
    assert X < right[0] - base.MARGIN
    return index, left, right


def stored_row_norm_upper(matrix):
    k = int(np.diff(matrix.indptr).max())
    observed = float(np.asarray(abs(matrix).sum(axis=1)).ravel().max())
    return F.from_float(observed) / (1 - base.gamma(k)), k


def stream_b4(b, vector, m, perturb, condition):
    result = np.empty(b.shape[0], dtype=np.float64)
    global_upper = F()
    global_observed = F()
    arithmetic_at_argmax = F()
    max_arithmetic = F()
    global_argmax = None
    peak_nnz = [0, 0, 0, 0]
    max_row_lengths = [0, 0, 0, 0]
    for first in range(0, b.shape[0], BATCH_ROWS):
        last = min(first + BATCH_ROWS, b.shape[0])
        block = b[first:last, :]
        arithmetic = F()
        _, k0 = stored_row_norm_upper(block)
        peak_nnz[0] = max(peak_nnz[0], int(block.nnz))
        max_row_lengths[0] = max(max_row_lengths[0], k0)
        for stage in range(1, 4):
            c_input, k_input = stored_row_norm_upper(block)
            arithmetic = arithmetic * m + base.gamma(2 * k_input) * c_input * m
            block = block @ b
            _, kj = stored_row_norm_upper(block)
            peak_nnz[stage] = max(peak_nnz[stage], int(block.nnz))
            max_row_lengths[stage] = max(max_row_lengths[stage], kj)
        max_arithmetic = max(max_arithmetic, arithmetic)
        raw = np.asarray(abs(block) @ vector).ravel()
        result[first:last] = raw
        ratios = raw / vector[first:last]
        local = int(ratios.argmax())
        observed = F.from_float(float(ratios[local]))
        stored_upper = observed / (1 - base.gamma(2 * kj + 1))
        true_upper = stored_upper + condition * (arithmetic + perturb)
        if true_upper > global_upper:
            global_upper = true_upper
            global_observed = observed
            arithmetic_at_argmax = arithmetic
            global_argmax = first + local
    return result, {
        "peak_nnz_by_stage": peak_nnz,
        "max_row_lengths_by_stage": max_row_lengths,
        "observed_at_argmax": float(global_observed),
        "certified_argmax": global_argmax,
        "arithmetic_error_at_argmax_batch": float(arithmetic_at_argmax),
        "max_arithmetic_error_any_batch": float(max_arithmetic),
        "outward_b4": float(global_upper),
        "outward_fourth_root": float(global_upper) ** 0.25,
        "pass": global_upper < TARGET4,
    }


if __name__ == "__main__":
    started = time.time()
    arc_index, left, right = exact_arc_containing_x()
    ordering_seconds = time.time() - started
    b = base.producer.assemble(R, float(X))
    m, _ = stored_row_norm_upper(b)
    perturb = (m + base.E) ** 4 - m ** 4

    ones = np.ones(b.shape[0], dtype=np.float64)
    unweighted_started = time.time()
    raw, unweighted = stream_b4(b, ones, m, perturb, F(1))
    unweighted_seconds = time.time() - unweighted_started

    weight = None
    weighted = None
    weight_sha = None
    condition = None
    weighted_seconds = 0.0
    if not unweighted["pass"]:
        assert np.all(np.isfinite(raw)) and np.all(raw > 0)
        weight = raw / raw.max()
        weight_sha = hashlib.sha256(weight.tobytes(order="C")).hexdigest()
        condition = F.from_float(float(weight.max())) / F.from_float(float(weight.min()))
        weighted_started = time.time()
        _, weighted = stream_b4(b, weight, m, perturb, condition)
        weighted_seconds = time.time() - weighted_started

    summary = {
        "radius": R,
        "exact_cut_count": EXPECTED_CUTS,
        "exact_arc_index_containing_x1": arc_index,
        "left_margin_float": float(X - left[1]),
        "right_margin_float": float(right[0] - X),
        "dimension": int(b.shape[0]),
        "b_nnz": int(b.nnz),
        "batch_rows": BATCH_ROWS,
        "batches": (b.shape[0] + BATCH_ROWS - 1) // BATCH_ROWS,
        "coefficient_perturbation": float(perturb),
        "unweighted": unweighted,
        "weight_updates": 0 if weight is None else 1,
        "weight_sha256": weight_sha,
        "weight_condition": None if condition is None else float(condition),
        "weighted": weighted,
        "target4": float(TARGET4),
        "final_pass": unweighted["pass"] or weighted["pass"],
        "ordering_seconds": ordering_seconds,
        "unweighted_seconds": unweighted_seconds,
        "weighted_seconds": weighted_seconds,
        "total_seconds": time.time() - started,
        "ru_maxrss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "formed_global_b2_or_b4": False,
        "scope": "one_exact_R9_arc_adaptive_only_no_C9_or_C16",
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print("STATUS=R9_ADAPTIVE_OUTWARD_PASS" if summary["final_pass"]
          else "STATUS=R9_ONE_UPDATE_FAIL_CONTINUE_ADAPTIVELY")
