#!/usr/bin/env python3
"""One streamed signed-B4 weight update at the exact R13 x=1 arc.

Uses the independently confirmed v15.775 exact branch under External Audit
Round 553 authorization. Starting from ones, forms one row-streamed signed-B4
absolute-value weight update, freezes its bytes, then applies the audited
directed-rounding outward replay. One exact R13 arc only; no C13 or C16 claim.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import hashlib
import json
import resource
import time
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location

import numpy as np

SOURCE = (
    "unified/discriminant-12-return/research-notes/"
    "lane_a_v15_775_suzuki_r13_exact_arc_unweighted_outward.py"
)
spec = spec_from_file_location("gate13", SOURCE)
gate13 = module_from_spec(spec)
spec.loader.exec_module(gate13)
gate = gate13.gate


def streamed_abs_b4_matvec(b, vector):
    result = np.empty(b.shape[0], dtype=np.float64)
    peak_nnz = [0, 0, 0, 0]
    for first in range(0, b.shape[0], gate.BATCH_ROWS):
        last = min(first + gate.BATCH_ROWS, b.shape[0])
        block = b[first:last, :]
        peak_nnz[0] = max(peak_nnz[0], int(block.nnz))
        for stage in range(1, 4):
            block = block @ b
            peak_nnz[stage] = max(peak_nnz[stage], int(block.nnz))
        result[first:last] = np.asarray(abs(block) @ vector).ravel()
    return result, peak_nnz


if __name__ == "__main__":
    started = time.time()
    arc_index, left, right = gate13.exact_arc_containing_x()
    assert arc_index == 285403
    b = gate.base.producer.assemble(gate.R, float(gate.X))
    m, _ = gate.stored_row_norm_upper(b)
    perturb = (m + gate.base.E) ** 4 - m ** 4

    construction_started = time.time()
    weight, construction_peak_nnz = streamed_abs_b4_matvec(
        b, np.ones(b.shape[0], dtype=np.float64)
    )
    assert np.all(np.isfinite(weight)) and np.all(weight > 0)
    weight /= weight.max()
    construction_seconds = time.time() - construction_started
    weight_sha = hashlib.sha256(weight.tobytes(order="C")).hexdigest()
    condition = F.from_float(float(weight.max())) / F.from_float(float(weight.min()))

    global_upper = F()
    global_observed = F()
    arithmetic_at_argmax = F()
    max_arithmetic = F()
    global_argmax = None
    validation_peak_nnz = [0, 0, 0, 0]
    max_row_lengths = [0, 0, 0, 0]
    validation_started = time.time()

    for first in range(0, b.shape[0], gate.BATCH_ROWS):
        last = min(first + gate.BATCH_ROWS, b.shape[0])
        block = b[first:last, :]
        arithmetic = F()
        _, k0 = gate.stored_row_norm_upper(block)
        validation_peak_nnz[0] = max(validation_peak_nnz[0], int(block.nnz))
        max_row_lengths[0] = max(max_row_lengths[0], k0)
        for stage in range(1, 4):
            c_input, k_input = gate.stored_row_norm_upper(block)
            arithmetic = arithmetic * m + gate.base.gamma(2 * k_input) * c_input * m
            block = block @ b
            _, kj = gate.stored_row_norm_upper(block)
            validation_peak_nnz[stage] = max(
                validation_peak_nnz[stage], int(block.nnz)
            )
            max_row_lengths[stage] = max(max_row_lengths[stage], kj)
        max_arithmetic = max(max_arithmetic, arithmetic)

        ratios = np.asarray(abs(block) @ weight).ravel() / weight[first:last]
        local = int(ratios.argmax())
        observed = F.from_float(float(ratios[local]))
        stored_upper = observed / (1 - gate.base.gamma(2 * kj + 1))
        true_upper = stored_upper + condition * (arithmetic + perturb)
        if true_upper > global_upper:
            global_upper = true_upper
            global_observed = observed
            arithmetic_at_argmax = arithmetic
            global_argmax = first + local

    summary = {
        "radius": gate.R,
        "exact_arc_index_containing_x1": arc_index,
        "left_margin_float": float(gate.X - left[1]),
        "right_margin_float": float(right[0] - gate.X),
        "dimension": int(b.shape[0]),
        "b_nnz": int(b.nnz),
        "weight_updates": 1,
        "weight_sha256": weight_sha,
        "weight_condition": float(condition),
        "construction_peak_nnz_by_stage": construction_peak_nnz,
        "validation_peak_nnz_by_stage": validation_peak_nnz,
        "max_row_lengths_by_stage": max_row_lengths,
        "observed_at_argmax": float(global_observed),
        "certified_argmax": global_argmax,
        "arithmetic_error_at_argmax_batch": float(arithmetic_at_argmax),
        "max_arithmetic_error_any_batch": float(max_arithmetic),
        "coefficient_perturbation": float(perturb),
        "outward_weighted_b4": float(global_upper),
        "outward_fourth_root": float(global_upper) ** 0.25,
        "target4": float(gate.TARGET4),
        "pass": global_upper < gate.TARGET4,
        "construction_seconds": construction_seconds,
        "validation_seconds": time.time() - validation_started,
        "total_seconds": time.time() - started,
        "ru_maxrss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "formed_global_b2_or_b4": False,
        "scope": "one_exact_R13_arc_only_no_C13_or_C16",
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print("STATUS=R13_ONE_UPDATE_OUTWARD_PASS" if global_upper < gate.TARGET4
          else "STATUS=R13_ONE_UPDATE_OUTWARD_FAIL_CONTINUE_ADAPTIVELY")
