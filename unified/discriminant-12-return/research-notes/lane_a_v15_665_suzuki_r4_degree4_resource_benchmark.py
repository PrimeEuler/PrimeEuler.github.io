#!/usr/bin/env python3
"""Suzuki R=4 degree-four positive-polynomial resource benchmark.

Evaluates 32 deterministically and evenly spaced v15.650 candidate arcs.
The purpose is to measure sparse B^2/B^4 time and memory before deciding
whether an exhaustive outward R=4 certificate is resource-effective.

All cut and matrix arithmetic is binary64.  This is NOT an exhaustive
statement, NOT an outward certificate, and NOT a radius-16 bound.
Run from the repository root with OPENBLAS_NUM_THREADS=1.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import json
import resource
import time
from importlib.util import module_from_spec, spec_from_file_location

import numpy as np

PRODUCER = (
    "unified/discriminant-12-return/research-notes/"
    "lane_a_v15_657_suzuki_positive_polynomial_small_radius_probe.py"
)
spec = spec_from_file_location("v15657", PRODUCER)
producer = module_from_spec(spec)
spec.loader.exec_module(producer)

RADIUS = 4
SAMPLE_COUNT = 32
CUTS = producer.cuts(RADIUS)
ARC_COUNT = len(CUTS)
assert ARC_COUNT == (2 * RADIUS + 3) * (2 * RADIUS + 1) ** 3 == 8019
INDICES = [i * ARC_COUNT // SAMPLE_COUNT for i in range(SAMPLE_COUNT)]
assert len(set(INDICES)) == SAMPLE_COUNT


def midpoint(i):
    left = CUTS[i]
    right = CUTS[(i + 1) % ARC_COUNT] + (2 if i + 1 == ARC_COUNT else 0)
    return float(((left + right) / 2) % 2)


def evaluate(i):
    x = midpoint(i)
    start = time.perf_counter()
    b = producer.assemble(RADIUS, x)
    t_b = time.perf_counter()
    defect = b - b.T
    assert (np.max(np.abs(defect.data)) if defect.nnz else 0) < 2e-13
    b2 = b @ b
    t_b2 = time.perf_counter()
    b4 = b2 @ b2
    t_b4 = time.perf_counter()
    row4 = float(np.asarray(abs(b4).sum(axis=1)).ravel().max())
    return {
        "index": i,
        "x": x,
        "b_nnz": int(b.nnz),
        "b2_nnz": int(b2.nnz),
        "b4_nnz": int(b4.nnz),
        "b4_row_sum": row4,
        "degree4_value": row4 ** 0.25,
        "assemble_seconds": t_b - start,
        "b2_seconds": t_b2 - t_b,
        "b4_seconds": t_b4 - t_b2,
        "total_seconds": t_b4 - start,
        "maxrss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
    }


if __name__ == "__main__":
    started = time.perf_counter()
    rows = []
    for i in INDICES:
        result = evaluate(i)
        rows.append(result)
        print("ARC", json.dumps(result, sort_keys=True), flush=True)
    elapsed = time.perf_counter() - started
    totals = np.array([r["total_seconds"] for r in rows])
    summary = {
        "radius": RADIUS,
        "arc_count": ARC_COUNT,
        "sample_count": SAMPLE_COUNT,
        "sample_indices": INDICES,
        "max_degree4_value": max(r["degree4_value"] for r in rows),
        "max_degree4_arc_index": max(rows, key=lambda r: r["degree4_value"])["index"],
        "max_b4_nnz": max(r["b4_nnz"] for r in rows),
        "median_total_seconds_per_arc": float(np.median(totals)),
        "max_total_seconds_per_arc": float(np.max(totals)),
        "serial_exhaustive_seconds_estimate_from_median": float(np.median(totals) * ARC_COUNT),
        "observed_process_maxrss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "wall_seconds": elapsed,
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print("STATUS=BINARY64_FIXED_SAMPLE_RESOURCE_BENCHMARK_ONLY")
    print("NO_EXHAUSTIVE_STATEMENT")
    print("NO_OUTWARD_NORM_CERTIFICATE")
