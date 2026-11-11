#!/usr/bin/env python3
"""Outward exact-cut stratified R=5 local-weight probe.

At 12 deterministic anchors spanning all 17,303 cut arcs, recompute a positive
40-step |B^4| weight, certify the anchor, and test transport through at most
four right neighbors.  This is a stratified resource/architecture gate, not
an exhaustive C5/C16 certificate.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import json
import time
from importlib.util import module_from_spec, spec_from_file_location

SOURCE = (
    "unified/discriminant-12-return/research-notes/"
    "lane_a_v15_677_suzuki_r5_adaptive_weight_chart_window.py"
)
spec = spec_from_file_location("chart", SOURCE)
chart = module_from_spec(spec)
spec.loader.exec_module(chart)

SAMPLE_COUNT = 12
MAX_RIGHT = 4
INDICES = [j * chart.ARC_COUNT // SAMPLE_COUNT for j in range(SAMPLE_COUNT)]
assert len(set(INDICES)) == SAMPLE_COUNT
assert INDICES[-1] + MAX_RIGHT < chart.ARC_COUNT


if __name__ == "__main__":
    started = time.time()
    print("R", chart.R, "ARC_COUNT", chart.ARC_COUNT,
          "SAMPLE_COUNT", SAMPLE_COUNT, "MAX_RIGHT", MAX_RIGHT)
    print("INDICES", INDICES)
    samples = []
    evaluations = 0
    for anchor in INDICES:
        x_fraction, b, b2, b4 = chart.assemble_powers(anchor)
        weight, condition, digest = chart.local_weight(abs(b4))
        anchor_row = chart.evaluate_powers(
            anchor, x_fraction, b, b2, b4, weight, condition
        )
        evaluations += 1
        last_pass = anchor if anchor_row["pass"] else None
        boundary_failure = None
        transported = []
        if anchor_row["pass"]:
            for index in range(anchor + 1, anchor + MAX_RIGHT + 1):
                row = chart.evaluate(index, weight, condition)
                evaluations += 1
                transported.append(row)
                if not row["pass"]:
                    boundary_failure = row
                    break
                last_pass = index
        sample = {
            "anchor": anchor,
            "anchor_midpoint_numerator": x_fraction.numerator,
            "anchor_midpoint_denominator": x_fraction.denominator,
            "anchor_result": anchor_row,
            "weight_condition": float(condition),
            "weight_sha256": digest,
            "last_pass": last_pass,
            "certified_width_with_cap": (
                0 if last_pass is None else last_pass - anchor + 1
            ),
            "right_cap_reached": (
                last_pass == anchor + MAX_RIGHT and boundary_failure is None
            ),
            "boundary_failure": boundary_failure,
            "transported": transported,
        }
        samples.append(sample)
        print("SAMPLE", json.dumps(sample, sort_keys=True), flush=True)
    anchor_roots = [s["anchor_result"]["outward_fourth_root"] for s in samples]
    widths = [s["certified_width_with_cap"] for s in samples]
    print("SUMMARY", json.dumps({
        "indices": INDICES,
        "sample_count": SAMPLE_COUNT,
        "all_anchors_pass": all(s["anchor_result"]["pass"] for s in samples),
        "anchor_root_min": min(anchor_roots),
        "anchor_root_max": max(anchor_roots),
        "certified_widths_with_cap": widths,
        "right_cap_reached_count": sum(s["right_cap_reached"] for s in samples),
        "evaluations": evaluations,
        "seconds": time.time() - started,
        "target4": float(chart.TARGET4),
    }, sort_keys=True))
    print("STATUS=OUTWARD_STRATIFIED_EXACT_CUT_R5_PROBE")
    print("NO_EXHAUSTIVE_C5_OR_C16_CERTIFICATE")
