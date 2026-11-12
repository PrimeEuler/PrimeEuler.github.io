#!/usr/bin/env python3
"""Exact R14 x=1 arc and unweighted streamed outward prerequisite.

Reuses the frozen audited recurrence with R set to 14, reconstructs the full
exact-log cut ordering, certifies the unique x=1 arc, and evaluates the
all-ones Collatz row bound for signed B^4 with directed-rounding charges.
Failure is only an unweighted-method obstruction, not a spectral lower bound.
One exact R14 arc only; no C14 or C16 claim.
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
    "lane_a_v15_775_suzuki_r13_exact_arc_unweighted_outward.py"
)
spec = spec_from_file_location("r13", SOURCE)
r13 = module_from_spec(spec)
spec.loader.exec_module(r13)
gate = r13.gate
gate.R = 14


def cut_interval(k):
    value = (F(), F())
    for ki, q in zip(k, (2, 3, 5, 7)):
        value = gate.base.add(value, gate.base.scale(gate.base.LS[q], -ki))
    return gate.base.mod2(value)


def exact_arc_containing_x():
    cuts = []
    for k0 in range(-gate.R - 1, gate.R + 2):
        for k1, k2, k3 in product(range(-gate.R, gate.R + 1), repeat=3):
            cuts.append(cut_interval((k0, k1, k2, k3)))
    cuts.sort(key=lambda z: z[0])
    expected = (2 * gate.R + 3) * (2 * gate.R + 1) ** 3
    assert len(cuts) == len(gate.base.producer.cuts(gate.R)) == expected == 756059
    for left, right in zip(cuts, cuts[1:]):
        assert left[1] < right[0]
    candidates = [
        (index, left, right)
        for index, (left, right) in enumerate(zip(cuts, cuts[1:]))
        if left[1] < gate.X < right[0]
    ]
    assert len(candidates) == 1
    index, left, right = candidates[0]
    assert gate.X > left[1] + gate.base.MARGIN
    assert gate.X < right[0] - gate.base.MARGIN
    return index, left, right


if __name__ == "__main__":
    started = time.time()
    arc_index, left, right = exact_arc_containing_x()
    ordering_seconds = time.time() - started
    assert arc_index == 378029
    b = gate.base.producer.assemble(gate.R, float(gate.X))
    m, _ = gate.stored_row_norm_upper(b)
    perturb = (m + gate.base.E) ** 4 - m ** 4

    global_upper = F()
    global_observed = F()
    arithmetic_at_argmax = F()
    max_arithmetic = F()
    global_argmax = None
    peak_nnz = [0, 0, 0, 0]
    max_row_lengths = [0, 0, 0, 0]
    validation_started = time.time()

    for first in range(0, b.shape[0], gate.BATCH_ROWS):
        last = min(first + gate.BATCH_ROWS, b.shape[0])
        block = b[first:last, :]
        arithmetic = F()
        _, k0 = gate.stored_row_norm_upper(block)
        peak_nnz[0] = max(peak_nnz[0], int(block.nnz))
        max_row_lengths[0] = max(max_row_lengths[0], k0)
        for stage in range(1, 4):
            c_input, k_input = gate.stored_row_norm_upper(block)
            arithmetic = arithmetic * m + gate.base.gamma(2 * k_input) * c_input * m
            block = block @ b
            _, kj = gate.stored_row_norm_upper(block)
            peak_nnz[stage] = max(peak_nnz[stage], int(block.nnz))
            max_row_lengths[stage] = max(max_row_lengths[stage], kj)
        max_arithmetic = max(max_arithmetic, arithmetic)
        ratios = np.asarray(abs(block).sum(axis=1)).ravel()
        local = int(ratios.argmax())
        observed = F.from_float(float(ratios[local]))
        stored_upper = observed / (1 - gate.base.gamma(2 * kj + 1))
        true_upper = stored_upper + arithmetic + perturb
        if true_upper > global_upper:
            global_upper = true_upper
            global_observed = observed
            arithmetic_at_argmax = arithmetic
            global_argmax = first + local

    summary = {
        "radius": gate.R,
        "exact_cut_count": 756059,
        "exact_arc_index_containing_x1": arc_index,
        "exact_left_upper_float": float(left[1]),
        "exact_right_lower_float": float(right[0]),
        "left_margin_float": float(gate.X - left[1]),
        "right_margin_float": float(right[0] - gate.X),
        "dimension": int(b.shape[0]),
        "b_nnz": int(b.nnz),
        "batch_rows": gate.BATCH_ROWS,
        "batches": (b.shape[0] + gate.BATCH_ROWS - 1) // gate.BATCH_ROWS,
        "peak_nnz_by_stage": peak_nnz,
        "max_row_lengths_by_stage": max_row_lengths,
        "observed_at_argmax": float(global_observed),
        "certified_argmax": global_argmax,
        "arithmetic_error_at_argmax_batch": float(arithmetic_at_argmax),
        "max_arithmetic_error_any_batch": float(max_arithmetic),
        "coefficient_perturbation": float(perturb),
        "outward_unweighted_b4": float(global_upper),
        "outward_fourth_root": float(global_upper) ** 0.25,
        "target4": float(gate.TARGET4),
        "pass": global_upper < gate.TARGET4,
        "ordering_seconds": ordering_seconds,
        "validation_seconds": time.time() - validation_started,
        "total_seconds": time.time() - started,
        "ru_maxrss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "formed_global_b2_or_b4": False,
        "scope": "one_exact_R14_arc_unweighted_method_only_no_C14_or_C16",
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print("STATUS=R14_UNWEIGHTED_OUTWARD_PASS" if global_upper < gate.TARGET4
          else "STATUS=R14_UNWEIGHTED_METHOD_FAIL_NOT_SPECTRAL_LOWER_BOUND")
