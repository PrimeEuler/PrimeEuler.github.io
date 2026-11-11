#!/usr/bin/env python3
"""R6 streamed-weight step convergence with outward replay at checkpoints.

Uses the audited v15.715 exact x=1 arc and row-streamed signed-B^4 pipeline.
At selected construction steps, independently applies the audited v15.699
directed-rounding replay.  The aim is to determine a reproducible sufficient
step count before scaling radius; this remains one R6 arc, not C6 or C16.
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
    "lane_a_v15_715_suzuki_r6_fully_streamed_scaling.py"
)
spec = spec_from_file_location("gate", SOURCE)
gate = module_from_spec(spec)
spec.loader.exec_module(gate)

CHECKPOINTS = (0, 1, 2, 3, 4, 5, 8, 10, 15, 20, 30, 40)


def outward_validate(b, weight, m, perturb):
    condition = F.from_float(float(weight.max())) / F.from_float(float(weight.min()))
    global_upper = F()
    global_observed = F()
    arithmetic_at_argmax = F()
    global_argmax = None
    peak_nnz = [0, 0, 0, 0]
    max_row_lengths = [0, 0, 0, 0]
    started = time.time()

    for first in range(0, b.shape[0], gate.BATCH_ROWS):
        last = min(first + gate.BATCH_ROWS, b.shape[0])
        block = b[first:last, :]
        arithmetic = F()
        _, k0 = gate.stored_row_norm_upper(block)
        peak_nnz[0] = max(peak_nnz[0], int(block.nnz))
        max_row_lengths[0] = max(max_row_lengths[0], k0)
        for stage in range(1, 4):
            c_input, k_input = gate.stored_row_norm_upper(block)
            arithmetic = (
                arithmetic * m
                + gate.base.gamma(2 * k_input) * c_input * m
            )
            block = block @ b
            _, kj = gate.stored_row_norm_upper(block)
            peak_nnz[stage] = max(peak_nnz[stage], int(block.nnz))
            max_row_lengths[stage] = max(max_row_lengths[stage], kj)

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

    return {
        "weight_sha256": hashlib.sha256(weight.tobytes(order="C")).hexdigest(),
        "weight_condition": float(condition),
        "observed_at_argmax": float(global_observed),
        "certified_argmax": global_argmax,
        "arithmetic_error_at_argmax_batch": float(arithmetic_at_argmax),
        "outward_weighted_b4": float(global_upper),
        "outward_fourth_root": float(global_upper) ** 0.25,
        "pass": global_upper < gate.TARGET4,
        "validation_seconds": time.time() - started,
        "peak_nnz_by_stage": peak_nnz,
        "max_row_lengths_by_stage": max_row_lengths,
    }


if __name__ == "__main__":
    started = time.time()
    arc_index, left, right = gate.exact_arc_containing_x()
    assert arc_index == 16477
    b = gate.base.producer.assemble(gate.R, float(gate.X))
    m, _ = gate.stored_row_norm_upper(b)
    perturb = (m + gate.base.E) ** 4 - m ** 4
    weight = np.ones(b.shape[0], dtype=np.float64)
    rows = []
    construction_seconds = 0.0
    construction_peak_nnz = [0, 0, 0, 0]

    for step in range(max(CHECKPOINTS) + 1):
        if step in CHECKPOINTS:
            row = {"step": step, **outward_validate(b, weight, m, perturb)}
            rows.append(row)
            print("CHECKPOINT", json.dumps(row, sort_keys=True), flush=True)
        if step == max(CHECKPOINTS):
            break
        tick = time.time()
        weight, peak = gate.streamed_abs_b4_matvec(b, weight)
        construction_seconds += time.time() - tick
        assert np.all(np.isfinite(weight)) and np.all(weight > 0)
        weight /= weight.max()
        construction_peak_nnz = [
            max(a, z) for a, z in zip(construction_peak_nnz, peak)
        ]

    passing = [row["step"] for row in rows if row["pass"]]
    first_pass = min(passing) if passing else None
    summary = {
        "radius": gate.R,
        "arc_index": arc_index,
        "left_margin_float": float(gate.X - left[1]),
        "right_margin_float": float(right[0] - gate.X),
        "dimension": int(b.shape[0]),
        "b_nnz": int(b.nnz),
        "checkpoints": list(CHECKPOINTS),
        "first_passing_checkpoint": first_pass,
        "all_reported_from_first_pass_onward_pass": (
            first_pass is not None
            and all(row["pass"] for row in rows if row["step"] >= first_pass)
        ),
        "construction_peak_nnz_by_stage": construction_peak_nnz,
        "construction_seconds": construction_seconds,
        "total_seconds": time.time() - started,
        "ru_maxrss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "formed_global_b2_or_b4": False,
        "scope": "one_exact_R6_arc_only_no_C6_or_C16",
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print("STATUS=R6_STREAMED_STEP_CONVERGENCE_MEASURED")
