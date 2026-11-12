#!/usr/bin/env python3
"""R3 cancellation-aware factorized adjacent-arc update test.

Imports the independently audited v15.800 exact machinery.  For each arc
adjacent to the x=1 anchor, row-streams the five signed words

  B0^4, D B0^3, B1 D B0^2, B1^2 D B0, B1^3 D

and takes absolute values only after their signed sum.  Directed-rounding and
coefficient-perturbation allowances enclose the result.  This tests a method,
not C3 or C16.
"""
import hashlib
import json
import time
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location

import numpy as np

SOURCE = "lane_a_v15_800_suzuki_r3_norm_transport_obstruction.py"
spec = spec_from_file_location("base", SOURCE)
base = module_from_spec(spec)
spec.loader.exec_module(base)

BATCH_ROWS = 128


def row_chain(chain, first, last, norms):
    block = chain[0][first:last, :]
    error = F()
    peak = [int(block.nnz)]
    for right in chain[1:]:
        c_input, k_input = base.unweighted_row_upper(block)
        m_right = norms[id(right)]
        error = (error * m_right
                 + base.gamma(2 * k_input) * c_input * m_right)
        block = block @ right
        peak.append(int(block.nnz))
    c_final, _ = base.unweighted_row_upper(block)
    return block, error, c_final, peak


def direct_outward(b1, weight, condition):
    started = time.time()
    b12 = b1 @ b1
    b14 = b12 @ b12
    m1, k1 = base.unweighted_row_upper(b1)
    c12, k2 = base.unweighted_row_upper(b12)
    stored, _ = base.weighted_row_upper(b14, weight)
    r2 = base.gamma(2 * k1) * m1 * m1
    r4 = r2 * (m1 * m1 + c12) + base.gamma(2 * k2) * c12 * c12
    perturb = (m1 + base.E)**4 - m1**4
    upper = stored + condition * (r4 + perturb)
    return upper, b14, time.time() - started


def factorized_outward(b0, b1, weight, condition):
    started = time.time()
    d = b1 - b0
    norms = {}
    for matrix in (b0, b1, d):
        norms[id(matrix)] = base.unweighted_row_upper(matrix)[0]
    m1 = norms[id(b1)]
    perturb = (m1 + base.E)**4 - m1**4
    chains = (
        (b0, b0, b0, b0),
        (d, b0, b0, b0),
        (b1, d, b0, b0),
        (b1, b1, d, b0),
        (b1, b1, b1, d),
    )

    global_upper = F()
    global_observed = F()
    global_argmax = None
    max_arithmetic = F()
    peak_nnz = [[0, 0, 0, 0] for _ in chains]
    max_final_row_length = 0
    combined_reference = []

    for first in range(0, b0.shape[0], BATCH_ROWS):
        last = min(first + BATCH_ROWS, b0.shape[0])
        blocks = []
        errors = []
        final_norms = []
        for word_index, chain in enumerate(chains):
            block, error, c_final, peaks = row_chain(
                chain, first, last, norms)
            blocks.append(block)
            errors.append(error)
            final_norms.append(c_final)
            for stage, value in enumerate(peaks):
                peak_nnz[word_index][stage] = max(
                    peak_nnz[word_index][stage], value)

        combined = blocks[0]
        for block in blocks[1:]:
            combined = combined + block
        combined_reference.append(combined)

        addition = base.gamma(len(blocks)) * sum(final_norms, F())
        arithmetic = sum(errors, F()) + addition
        max_arithmetic = max(max_arithmetic, arithmetic)

        k = int(np.diff(combined.indptr).max())
        max_final_row_length = max(max_final_row_length, k)
        ratios = np.asarray(abs(combined) @ weight).ravel() / weight[first:last]
        local = int(ratios.argmax())
        observed = F.from_float(float(ratios[local]))
        stored = observed / (1 - base.gamma(2 * k + 1))
        upper = stored + condition * (arithmetic + perturb)
        if upper > global_upper:
            global_upper = upper
            global_observed = observed
            global_argmax = first + local

    return {
        "upper": global_upper,
        "observed": global_observed,
        "argmax": global_argmax,
        "max_arithmetic": max_arithmetic,
        "peak_nnz_by_word_and_stage": peak_nnz,
        "max_final_row_length": max_final_row_length,
        "combined": np.vstack([x.toarray() for x in combined_reference]),
        "seconds": time.time() - started,
        "d_nnz": int(d.nnz),
    }


if __name__ == "__main__":
    maximum_state_error = base.certify_word_state_tolerance()
    cuts = base.exact_cuts()
    candidates = [i for i, (left, right) in
                  enumerate(zip(cuts, cuts[1:]))
                  if left[1] < 1 < right[0]]
    assert candidates == [1543]

    b0 = base.assemble(base.R, 1.0)
    b02 = b0 @ b0
    b04 = b02 @ b02
    weight = np.asarray(abs(b04) @ np.ones(b0.shape[0])).ravel()
    assert np.all(np.isfinite(weight)) and np.all(weight > 0)
    weight /= weight.max()
    weight_sha = hashlib.sha256(weight.tobytes(order="C")).hexdigest()
    condition = (F.from_float(float(weight.max()))
                 / F.from_float(float(weight.min())))

    results = []
    for neighbor in (1542, 1544):
        x = base.midpoint(cuts, neighbor)
        b1 = base.assemble(base.R, x)
        direct, b14, direct_seconds = direct_outward(b1, weight, condition)
        factorized = factorized_outward(b0, b1, weight, condition)
        discrepancy = float(np.max(np.abs(factorized["combined"] - b14.toarray())))
        results.append({
            "neighbor_arc": neighbor,
            "x": x,
            "d_nnz": factorized["d_nnz"],
            "direct_outward_b4": float(direct),
            "direct_fourth_root": float(direct) ** 0.25,
            "factorized_observed_b4": float(factorized["observed"]),
            "factorized_outward_b4": float(factorized["upper"]),
            "factorized_fourth_root": float(factorized["upper"]) ** 0.25,
            "factorized_argmax": factorized["argmax"],
            "max_arithmetic_allowance": float(factorized["max_arithmetic"]),
            "max_final_row_length": factorized["max_final_row_length"],
            "peak_nnz_by_word_and_stage":
                factorized["peak_nnz_by_word_and_stage"],
            "max_binary64_entry_discrepancy_vs_direct_b14": discrepancy,
            "direct_seconds": direct_seconds,
            "factorized_seconds": factorized["seconds"],
            "pass": factorized["upper"] < base.TARGET,
        })

    summary = {
        "radius": base.R,
        "cut_count": len(cuts),
        "anchor_arc": 1543,
        "dimension": int(b0.shape[0]),
        "weight_sha256": weight_sha,
        "weight_condition": float(condition),
        "max_exact_word_state_error": float(maximum_state_error),
        "results": results,
        "target4": float(base.TARGET),
        "method":
            "signed_five_word_factorized_update_absolute_value_only_at_end",
        "scope": "R3_two_adjacent_arcs_only_no_C3_no_C16",
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print("STATUS=FACTORIZED_UPDATE_PASS"
          if all(result["pass"] for result in results)
          else "STATUS=FACTORIZED_UPDATE_FAIL_NOT_SPECTRAL_LOWER_BOUND")
