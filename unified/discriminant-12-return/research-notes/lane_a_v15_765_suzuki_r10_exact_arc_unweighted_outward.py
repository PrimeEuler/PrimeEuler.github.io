#!/usr/bin/env python3
"""Exact R10 x=1 arc and unweighted streamed outward baseline.

Builds the full exact-log R10 cut ordering, certifies the unique arc containing
x=1, and applies the audited row-streamed signed-B^4 directed-rounding
recurrence with the all-ones weight.  Failure is only an unweighted-method
obstruction, not a spectral lower bound.  One exact arc only.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import json
import resource
import time
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product

import numpy as np

SOURCE = (
    "unified/discriminant-12-return/research-notes/"
    "lane_a_v15_664_suzuki_r3_outward_degree4_certificate.py"
)
spec = spec_from_file_location("base", SOURCE)
base = module_from_spec(spec)
spec.loader.exec_module(base)

R = 10
X = F(1)
BATCH_ROWS = 128
TARGET4 = F(41, 10) ** 4


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
    expected = (2 * R + 3) * (2 * R + 1) ** 3
    assert len(cuts) == len(base.producer.cuts(R)) == expected == 213003
    for left, right in zip(cuts, cuts[1:]):
        assert left[1] < right[0]
    candidates = [
        (index, left, right)
        for index, (left, right) in enumerate(zip(cuts, cuts[1:]))
        if left[1] < X < right[0]
    ]
    assert len(candidates) == 1
    index, left, right = candidates[0]
    assert X > left[1] + base.MARGIN
    assert X < right[0] - base.MARGIN
    return index, left, right


def stored_row_norm_upper(matrix):
    k = int(np.diff(matrix.indptr).max())
    observed = float(np.asarray(abs(matrix).sum(axis=1)).ravel().max())
    return F.from_float(observed) / (1 - base.gamma(k)), k


if __name__ == "__main__":
    started = time.time()
    arc_index, left, right = exact_arc_containing_x()
    ordering_seconds = time.time() - started
    b = base.producer.assemble(R, float(X))
    m, _ = stored_row_norm_upper(b)
    perturb = (m + base.E) ** 4 - m ** 4

    global_upper = F()
    global_observed = F()
    arithmetic_at_argmax = F()
    max_arithmetic = F()
    global_argmax = None
    peak_nnz = [0, 0, 0, 0]
    max_row_lengths = [0, 0, 0, 0]
    validation_started = time.time()

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
        ratios = np.asarray(abs(block).sum(axis=1)).ravel()
        local = int(ratios.argmax())
        observed = F.from_float(float(ratios[local]))
        stored_upper = observed / (1 - base.gamma(2 * kj + 1))
        true_upper = stored_upper + arithmetic + perturb
        if true_upper > global_upper:
            global_upper = true_upper
            global_observed = observed
            arithmetic_at_argmax = arithmetic
            global_argmax = first + local

    summary = {
        "radius": R,
        "exact_cut_count": 213003,
        "exact_arc_index_containing_x1": arc_index,
        "exact_left_upper_float": float(left[1]),
        "exact_right_lower_float": float(right[0]),
        "left_margin_float": float(X - left[1]),
        "right_margin_float": float(right[0] - X),
        "dimension": int(b.shape[0]),
        "b_nnz": int(b.nnz),
        "batch_rows": BATCH_ROWS,
        "batches": (b.shape[0] + BATCH_ROWS - 1) // BATCH_ROWS,
        "peak_nnz_by_stage": peak_nnz,
        "max_row_lengths_by_stage": max_row_lengths,
        "observed_at_argmax": float(global_observed),
        "certified_argmax": global_argmax,
        "arithmetic_error_at_argmax_batch": float(arithmetic_at_argmax),
        "max_arithmetic_error_any_batch": float(max_arithmetic),
        "coefficient_perturbation": float(perturb),
        "outward_unweighted_b4": float(global_upper),
        "outward_fourth_root": float(global_upper) ** 0.25,
        "target4": float(TARGET4),
        "pass": global_upper < TARGET4,
        "ordering_seconds": ordering_seconds,
        "validation_seconds": time.time() - validation_started,
        "total_seconds": time.time() - started,
        "ru_maxrss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "formed_global_b2_or_b4": False,
        "scope": "one_exact_R10_arc_unweighted_method_only_no_C10_or_C16",
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print("STATUS=R10_UNWEIGHTED_OUTWARD_PASS" if global_upper < TARGET4
          else "STATUS=R10_UNWEIGHTED_METHOD_FAIL_NOT_SPECTRAL_LOWER_BOUND")

