#!/usr/bin/env python3
"""Fully streamed R5 weight construction and outward one-arc replay.

Constructs the 40-step positive weight using row batches of signed B^4,
discarding every batch after its contribution to |B^4|w.  No global B^2 or
B^4 is formed.  The final weight is then certified with the independently
audited v15.699 stagewise outward recurrence.  One R5 arc only; no C5/C16.
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
    "lane_a_v15_699_suzuki_r5_streamed_b4_outward_one_arc.py"
)
spec = spec_from_file_location("gate", SOURCE)
gate = module_from_spec(spec)
spec.loader.exec_module(gate)

R = 5
ANCHOR = 8651
BATCH_ROWS = 128
POWER_STEPS = 40
TARGET4 = F(41, 10) ** 4


def streamed_abs_b4_matvec(b, vector):
    """Return fl(|fl(((B_rows B)B)B)| vector) without storing global B4."""
    result = np.empty(b.shape[0], dtype=np.float64)
    peak_nnz = [0, 0, 0, 0]
    for first in range(0, b.shape[0], BATCH_ROWS):
        last = min(first + BATCH_ROWS, b.shape[0])
        block = b[first:last, :]
        peak_nnz[0] = max(peak_nnz[0], int(block.nnz))
        for stage in range(1, 4):
            block = block @ b
            peak_nnz[stage] = max(peak_nnz[stage], int(block.nnz))
        result[first:last] = np.asarray(abs(block) @ vector).ravel()
    return result, peak_nnz


if __name__ == "__main__":
    started = time.time()
    x_fraction = gate.chart.certified_midpoint(ANCHOR)
    assert x_fraction == 1
    b = gate.chart.base.producer.assemble(R, float(x_fraction))

    weight = np.ones(b.shape[0], dtype=np.float64)
    checkpoint_hashes = {}
    construction_peak_nnz = [0, 0, 0, 0]
    construction_started = time.time()
    for step in range(1, POWER_STEPS + 1):
        weight, peak = streamed_abs_b4_matvec(b, weight)
        assert np.all(np.isfinite(weight)) and np.all(weight > 0)
        weight /= weight.max()
        construction_peak_nnz = [
            max(a, z) for a, z in zip(construction_peak_nnz, peak)
        ]
        if step in (1, 10, 20, 30, 40):
            checkpoint_hashes[str(step)] = hashlib.sha256(
                weight.tobytes(order="C")
            ).hexdigest()
    construction_seconds = time.time() - construction_started

    weight_sha = hashlib.sha256(weight.tobytes(order="C")).hexdigest()
    condition = F.from_float(float(weight.max())) / F.from_float(float(weight.min()))
    m, _ = gate.stored_row_norm_upper(b)
    perturb = (m + gate.chart.base.E) ** 4 - m ** 4

    global_upper = F()
    global_observed = F()
    arithmetic_at_argmax = F()
    max_arithmetic = F()
    global_argmax = None
    validation_peak_nnz = [0, 0, 0, 0]
    max_row_lengths = [0, 0, 0, 0]
    validation_started = time.time()

    for first in range(0, b.shape[0], BATCH_ROWS):
        last = min(first + BATCH_ROWS, b.shape[0])
        block = b[first:last, :]
        arithmetic = F()
        _, k0 = gate.stored_row_norm_upper(block)
        validation_peak_nnz[0] = max(validation_peak_nnz[0], int(block.nnz))
        max_row_lengths[0] = max(max_row_lengths[0], k0)

        for stage in range(1, 4):
            c_input, k_input = gate.stored_row_norm_upper(block)
            arithmetic = (
                arithmetic * m
                + gate.chart.base.gamma(2 * k_input) * c_input * m
            )
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
        stored_upper = observed / (1 - gate.chart.base.gamma(2 * kj + 1))
        true_upper = stored_upper + condition * (arithmetic + perturb)
        if true_upper > global_upper:
            global_upper = true_upper
            global_observed = observed
            arithmetic_at_argmax = arithmetic
            global_argmax = first + local
    validation_seconds = time.time() - validation_started

    summary = {
        "anchor": ANCHOR,
        "midpoint_numerator": x_fraction.numerator,
        "midpoint_denominator": x_fraction.denominator,
        "dimension": int(b.shape[0]),
        "b_nnz": int(b.nnz),
        "batch_rows": BATCH_ROWS,
        "power_steps": POWER_STEPS,
        "checkpoint_weight_sha256": checkpoint_hashes,
        "weight_sha256": weight_sha,
        "weight_condition": float(condition),
        "construction_peak_nnz_by_stage": construction_peak_nnz,
        "validation_peak_nnz_by_stage": validation_peak_nnz,
        "max_row_lengths_by_stage": max_row_lengths,
        "observed_at_certified_argmax": float(global_observed),
        "certified_argmax": global_argmax,
        "arithmetic_error_at_certified_argmax_batch": float(arithmetic_at_argmax),
        "max_arithmetic_error_any_batch": float(max_arithmetic),
        "coefficient_perturbation": float(perturb),
        "outward_weighted_b4": float(global_upper),
        "outward_fourth_root": float(global_upper) ** 0.25,
        "target4": float(TARGET4),
        "pass": global_upper < TARGET4,
        "construction_seconds": construction_seconds,
        "validation_seconds": validation_seconds,
        "total_seconds": time.time() - started,
        "ru_maxrss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "formed_global_b2_or_b4": False,
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print("STATUS=FULLY_STREAMED_WEIGHT_OUTWARD_ONE_ARC_PASS" if global_upper < TARGET4
          else "STATUS=FULLY_STREAMED_WEIGHT_OUTWARD_ONE_ARC_FAIL")
    print("NO_GLOBAL_B2_OR_B4_FORMED")
    print("ONE_ARC_ONLY_NO_C5_OR_C16_CERTIFICATE")
