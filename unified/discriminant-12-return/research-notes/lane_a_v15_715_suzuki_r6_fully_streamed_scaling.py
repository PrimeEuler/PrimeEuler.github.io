#!/usr/bin/env python3
"""Measured R6 fully streamed weight construction and outward x=1 replay.

This is the audited v15.704 row-streamed signed-B^4 architecture at radius 6.
It proves exact-log branch bookkeeping for the unique cut arc containing x=1,
constructs a 40-step positive weight without global B^2/B^4, and applies the
v15.699 stagewise directed-rounding recurrence.  One R6 arc only: no C6/C16.
"""
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

SOURCE = (
    "unified/discriminant-12-return/research-notes/"
    "lane_a_v15_664_suzuki_r3_outward_degree4_certificate.py"
)
spec = spec_from_file_location("base", SOURCE)
base = module_from_spec(spec)
spec.loader.exec_module(base)

R = 6
X = F(1)
BATCH_ROWS = 128
POWER_STEPS = 40
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
    assert len(cuts) == len(base.producer.cuts(R)) == 32955
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
    """Upper bound the exact row-sum norm of a binary64 CSR matrix."""
    k = int(np.diff(matrix.indptr).max())
    observed = float(np.asarray(abs(matrix).sum(axis=1)).ravel().max())
    return F.from_float(observed) / (1 - base.gamma(k)), k


def streamed_abs_b4_matvec(b, vector):
    """Return fl(|fl(((B_rows B)B)B)| vector) without global B4."""
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
    arc_index, left, right = exact_arc_containing_x()
    b = base.producer.assemble(R, float(X))

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
            print("CHECKPOINT", step, checkpoint_hashes[str(step)], flush=True)
    construction_seconds = time.time() - construction_started

    weight_sha = hashlib.sha256(weight.tobytes(order="C")).hexdigest()
    condition = F.from_float(float(weight.max())) / F.from_float(float(weight.min()))
    m, _ = stored_row_norm_upper(b)
    perturb = (m + base.E) ** 4 - m ** 4

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
        _, k0 = stored_row_norm_upper(block)
        validation_peak_nnz[0] = max(validation_peak_nnz[0], int(block.nnz))
        max_row_lengths[0] = max(max_row_lengths[0], k0)

        for stage in range(1, 4):
            c_input, k_input = stored_row_norm_upper(block)
            arithmetic = arithmetic * m + base.gamma(2 * k_input) * c_input * m
            block = block @ b
            _, kj = stored_row_norm_upper(block)
            validation_peak_nnz[stage] = max(
                validation_peak_nnz[stage], int(block.nnz)
            )
            max_row_lengths[stage] = max(max_row_lengths[stage], kj)
        max_arithmetic = max(max_arithmetic, arithmetic)

        ratios = np.asarray(abs(block) @ weight).ravel() / weight[first:last]
        local = int(ratios.argmax())
        observed = F.from_float(float(ratios[local]))
        stored_upper = observed / (1 - base.gamma(2 * kj + 1))
        true_upper = stored_upper + condition * (arithmetic + perturb)
        if true_upper > global_upper:
            global_upper = true_upper
            global_observed = observed
            arithmetic_at_argmax = arithmetic
            global_argmax = first + local
    validation_seconds = time.time() - validation_started

    summary = {
        "radius": R,
        "exact_arc_index_containing_x1": arc_index,
        "exact_left_upper_float": float(left[1]),
        "exact_right_lower_float": float(right[0]),
        "left_margin_float": float(X - left[1]),
        "right_margin_float": float(right[0] - X),
        "dimension": int(b.shape[0]),
        "b_nnz": int(b.nnz),
        "batch_rows": BATCH_ROWS,
        "batches": (b.shape[0] + BATCH_ROWS - 1) // BATCH_ROWS,
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
    print("STATUS=R6_FULLY_STREAMED_OUTWARD_ONE_ARC_PASS" if global_upper < TARGET4
          else "STATUS=R6_FULLY_STREAMED_OUTWARD_ONE_ARC_FAIL")
    print("ONE_R6_ARC_ONLY_NO_C6_OR_C16_CERTIFICATE")
