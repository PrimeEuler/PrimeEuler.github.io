#!/usr/bin/env python3
"""Outward streamed signed-B4 evaluation at the audited R5 x=1 arc.

The local weight is the frozen 40-step weight from the materialized reference.
Each output-row batch computes (((B_rows @ B) @ B) @ B), taking absolute
values only after the signed B4 entries are accumulated.  A stagewise sparse
matmul forward-error recurrence encloses the sequential binary64 path.  This
certifies one R5 arc only and does not solve streamed weight construction.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import hashlib
import json
import time
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location

import numpy as np

SOURCE = (
    "unified/discriminant-12-return/research-notes/"
    "lane_a_v15_677_suzuki_r5_adaptive_weight_chart_window.py"
)
spec = spec_from_file_location("chart", SOURCE)
chart = module_from_spec(spec)
spec.loader.exec_module(chart)

R = 5
ANCHOR = 8651
BATCH_ROWS = 128
TARGET4 = F(41, 10) ** 4
assert chart.certified_midpoint(ANCHOR) == 1


def stored_row_norm_upper(matrix):
    """Upper bound the exact row-sum norm of a binary64 CSR matrix."""
    k = int(np.diff(matrix.indptr).max())
    observed = float(np.asarray(abs(matrix).sum(axis=1)).ravel().max())
    return F.from_float(observed) / (1 - chart.base.gamma(k)), k


if __name__ == "__main__":
    started = time.time()
    x_fraction, b, b2, b4 = chart.assemble_powers(ANCHOR)
    weight, _, weight_sha = chart.local_weight(abs(b4))
    condition = F.from_float(float(weight.max())) / F.from_float(float(weight.min()))
    assert weight_sha == hashlib.sha256(weight.tobytes(order="C")).hexdigest()
    materialized_reference = chart.evaluate_powers(
        ANCHOR, x_fraction, b, b2, b4, weight, condition
    )
    m, kb = stored_row_norm_upper(b)
    perturb = (m + chart.base.E) ** 4 - m ** 4

    global_upper = F()
    global_observed = F()
    arithmetic_at_argmax = F()
    max_arithmetic_any_batch = F()
    global_argmax = None
    max_batch_nnz = [0, 0, 0, 0]
    max_row_lengths = [0, 0, 0, 0]
    batches = 0

    for first in range(0, b.shape[0], BATCH_ROWS):
        last = min(first + BATCH_ROWS, b.shape[0])
        block = b[first:last, :]
        arithmetic = F()
        max_batch_nnz[0] = max(max_batch_nnz[0], int(block.nnz))
        _, k0 = stored_row_norm_upper(block)
        max_row_lengths[0] = max(max_row_lengths[0], k0)

        # If C_j=fl(C_{j-1} B), c_j=||C_j||_inf and k_j is the
        # maximum stored row length, then the standard dot-product bound gives
        #   ||C_j-C_{j-1}B||_inf <= gamma(2 k_{j-1}) c_{j-1} m.
        # Hence e_j <= e_{j-1} m + gamma(2 k_{j-1}) c_{j-1} m.
        # All c's are themselves rounded upward by the row-sum gamma bound.
        for stage in range(1, 4):
            c_input, k_input = stored_row_norm_upper(block)
            arithmetic = (
                arithmetic * m
                + chart.base.gamma(2 * k_input) * c_input * m
            )
            block = block @ b
            _, kj = stored_row_norm_upper(block)
            max_batch_nnz[stage] = max(max_batch_nnz[stage], int(block.nnz))
            max_row_lengths[stage] = max(max_row_lengths[stage], kj)
        max_arithmetic_any_batch = max(max_arithmetic_any_batch, arithmetic)

        ratios = np.asarray(abs(block) @ weight).ravel() / weight[first:last]
        local = int(ratios.argmax())
        observed = F.from_float(float(ratios[local]))
        stored_upper = observed / (1 - chart.base.gamma(2 * kj + 1))
        true_upper = stored_upper + condition * (arithmetic + perturb)
        if true_upper > global_upper:
            global_upper = true_upper
            global_observed = observed
            arithmetic_at_argmax = arithmetic
            global_argmax = first + local
        batches += 1

    summary = {
        "anchor": ANCHOR,
        "midpoint_numerator": x_fraction.numerator,
        "midpoint_denominator": x_fraction.denominator,
        "dimension": int(b.shape[0]),
        "batch_rows": BATCH_ROWS,
        "batches": batches,
        "b_nnz": int(b.nnz),
        "materialized_b4_nnz_for_weight_only": int(b4.nnz),
        "max_batch_nnz_by_stage": max_batch_nnz,
        "max_row_lengths_by_stage": max_row_lengths,
        "weight_condition": float(condition),
        "weight_sha256": weight_sha,
        "observed_at_certified_argmax": float(global_observed),
        "certified_argmax": global_argmax,
        "arithmetic_error_at_certified_argmax_batch": float(arithmetic_at_argmax),
        "max_arithmetic_error_any_batch": float(max_arithmetic_any_batch),
        "coefficient_perturbation": float(perturb),
        "outward_weighted_b4": float(global_upper),
        "outward_fourth_root": float(global_upper) ** 0.25,
        "materialized_outward_weighted_b4": materialized_reference[
            "outward_weighted_b4"
        ],
        "streamed_minus_materialized_outward": (
            float(global_upper) - materialized_reference["outward_weighted_b4"]
        ),
        "target4": float(TARGET4),
        "pass": global_upper < TARGET4,
        "seconds": time.time() - started,
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print("STATUS=OUTWARD_STREAMED_SIGNED_B4_ONE_ARC_PASS" if global_upper < TARGET4
          else "STATUS=OUTWARD_STREAMED_SIGNED_B4_ONE_ARC_FAIL")
    print("WEIGHT_CONSTRUCTION_STILL_MATERIALIZES_B4")
    print("ONE_ARC_ONLY_NO_C5_OR_C16_CERTIFICATE")
