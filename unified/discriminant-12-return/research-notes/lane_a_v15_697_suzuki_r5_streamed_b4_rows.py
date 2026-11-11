#!/usr/bin/env python3
"""Cancellation-preserving streamed B^4-row benchmark at the audited R5 anchor.

Compares materialized B^4 against row batches computed as
(((B[rows,:] @ B) @ B) @ B).  Absolute values are taken only after all signed
products in each B^4 entry have been accumulated.  This tests a memory-bounded
architecture; it is not yet an outward certificate because the sequential
floating-point multiplication path needs its own error enclosure.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import gc
import hashlib
import json
import time
from importlib.util import module_from_spec, spec_from_file_location

import numpy as np

SOURCE = (
    "unified/discriminant-12-return/research-notes/"
    "lane_a_v15_677_suzuki_r5_adaptive_weight_chart_window.py"
)
spec = spec_from_file_location("chart", SOURCE)
chart = module_from_spec(spec)
spec.loader.exec_module(chart)

ANCHOR = 8651
BATCH_ROWS = 128
assert chart.certified_midpoint(ANCHOR) == 1


if __name__ == "__main__":
    total_started = time.time()
    x_fraction, b, b2, b4 = chart.assemble_powers(ANCHOR)
    weight, condition, weight_sha = chart.local_weight(abs(b4))
    reference_started = time.time()
    reference_ratios = np.asarray(abs(b4) @ weight).ravel() / weight
    reference_seconds = time.time() - reference_started
    reference_max = float(reference_ratios.max())
    reference_argmax = int(reference_ratios.argmax())

    streamed_max = -np.inf
    streamed_argmax = None
    max_entry_difference = 0.0
    max_ratio_difference = 0.0
    max_batch_nnz = [0, 0, 0, 0]
    streamed_started = time.time()
    batches = 0
    for first in range(0, b.shape[0], BATCH_ROWS):
        last = min(first + BATCH_ROWS, b.shape[0])
        block = b[first:last, :]
        max_batch_nnz[0] = max(max_batch_nnz[0], int(block.nnz))
        for stage in range(1, 4):
            block = block @ b
            max_batch_nnz[stage] = max(max_batch_nnz[stage], int(block.nnz))
        streamed_ratios = np.asarray(abs(block) @ weight).ravel() / weight[first:last]
        local = int(streamed_ratios.argmax())
        if float(streamed_ratios[local]) > streamed_max:
            streamed_max = float(streamed_ratios[local])
            streamed_argmax = first + local
        ratio_difference = float(
            np.max(np.abs(streamed_ratios - reference_ratios[first:last]))
        )
        max_ratio_difference = max(max_ratio_difference, ratio_difference)
        delta = block - b4[first:last, :]
        if delta.nnz:
            max_entry_difference = max(
                max_entry_difference, float(np.max(np.abs(delta.data)))
            )
        batches += 1
    streamed_seconds = time.time() - streamed_started

    summary = {
        "anchor": ANCHOR,
        "midpoint_numerator": x_fraction.numerator,
        "midpoint_denominator": x_fraction.denominator,
        "dimension": int(b.shape[0]),
        "b_nnz": int(b.nnz),
        "b2_nnz": int(b2.nnz),
        "materialized_b4_nnz": int(b4.nnz),
        "batch_rows": BATCH_ROWS,
        "batches": batches,
        "max_batch_nnz_by_stage": max_batch_nnz,
        "weight_condition": float(condition),
        "weight_sha256": weight_sha,
        "reference_max": reference_max,
        "reference_argmax": reference_argmax,
        "streamed_max": streamed_max,
        "streamed_argmax": streamed_argmax,
        "max_entry_difference": max_entry_difference,
        "max_ratio_difference": max_ratio_difference,
        "reference_seconds": reference_seconds,
        "streamed_seconds": streamed_seconds,
        "total_seconds": time.time() - total_started,
        "exact_binary64_max_match": (
            streamed_max == reference_max and streamed_argmax == reference_argmax
        ),
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print("MATERIALIZED_B4_BYTES_ESTIMATE",
          int(b4.data.nbytes + b4.indices.nbytes + b4.indptr.nbytes))
    print("WEIGHT_BYTES", weight.nbytes,
          "WEIGHT_SHA256", hashlib.sha256(weight.tobytes(order="C")).hexdigest())
    print("STATUS=CANCELLATION_PRESERVING_STREAMED_B4_ARCHITECTURE_PROBE")
    print("NO_OUTWARD_STREAMING_ERROR_CERTIFICATE")
    print("NO_C5_OR_C16_CERTIFICATE")
    del b2, b4, weight, reference_ratios
    gc.collect()
