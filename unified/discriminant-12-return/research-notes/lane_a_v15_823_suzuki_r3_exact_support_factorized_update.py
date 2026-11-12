#!/usr/bin/env python3
"""R3 exact-support cancellation-aware adjacent-arc update test.

Additive successor to v15.814.  It fixes that witness's cwd-sensitive import,
derives the crossed-cut support from v15.650's four exact corners, replaces
only those entries, and then row-streams the signed five-word factorization.
This tests a method on two R3 transitions; it is not C3 or C16.
"""
import hashlib
import json
import time
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
from pathlib import Path

import numpy as np

SOURCE_NAME = "lane_a_v15_800_suzuki_r3_norm_transport_obstruction.py"
HERE = Path(__file__).resolve().parent
SOURCE_CANDIDATES = (
    HERE / SOURCE_NAME,
    HERE.parent / "research-notes" / SOURCE_NAME,
)
SOURCE = next((path for path in SOURCE_CANDIDATES if path.is_file()), None)
if SOURCE is None:
    raise FileNotFoundError(f"cannot locate {SOURCE_NAME}: {SOURCE_CANDIDATES}")
spec = spec_from_file_location("base", SOURCE)
base = module_from_spec(spec)
spec.loader.exec_module(base)

BATCH_ROWS = 128


def labeled_cuts():
    cuts = []
    for k0 in range(-base.R - 1, base.R + 2):
        for k1, k2, k3 in product(range(-base.R, base.R + 1), repeat=3):
            label = (k0, k1, k2, k3)
            cuts.append((base.cut_interval(label), label))
    cuts.sort(key=lambda item: item[0][0])
    assert [item[0] for item in cuts] == base.exact_cuts()
    return cuts


def exact_affected_positions(label):
    """Return aggregate matrix positions whose word has label as a corner."""
    radius = base.R
    width = 2 * radius + 1
    sites = np.indices((width,) * 4, dtype=np.int16).reshape(4, -1).T
    h = sites.astype(np.int32) - radius
    positions = set()
    word_positions = 0
    for q, r in combinations(base.Q, 2):
        vq = np.asarray(base.V[q])
        vr = np.asarray(base.V[r])
        for sigma, tau in product((-1, 1), repeat=2):
            jump = tau * vr - sigma * vq
            source = sites - jump
            mask = np.all((source >= 0) & (source < width), axis=1)
            for row in np.flatnonzero(mask):
                hh = h[row]
                corners = (hh, hh + sigma * vq, hh - tau * vr,
                           hh + sigma * vq - tau * vr)
                if any(tuple(corner) == label for corner in corners):
                    col = np.ravel_multi_index(source[row], (width,) * 4)
                    positions.add((int(row), int(col)))
                    word_positions += 1
    assert word_positions <= 160
    return positions, word_positions


def localized_neighbor(b0, full_b1, positions):
    """Use direct neighbor values exactly on proven affected positions only."""
    b1 = b0.tolil(copy=True)
    for row, col in positions:
        b1[row, col] = full_b1[row, col]
    b1 = b1.tocsr()
    b1.eliminate_zeros()
    d = b1 - b0
    d.eliminate_zeros()
    residue = full_b1 - b1
    residue.eliminate_zeros()
    residue_max = float(abs(residue).max()) if residue.nnz else 0.0
    return b1, d, residue_max, int(residue.nnz)


def row_chain(chain, first, last, norms):
    block = chain[0][first:last, :]
    error = F()
    peak = [int(block.nnz)]
    for right in chain[1:]:
        c_input, k_input = base.unweighted_row_upper(block)
        m_right = norms[id(right)]
        error = error * m_right + base.gamma(2 * k_input) * c_input * m_right
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
    perturb = (m1 + base.E) ** 4 - m1 ** 4
    return stored + condition * (r4 + perturb), b14, time.time() - started


def factorized_outward(b0, b1, weight, condition):
    started = time.time()
    d = b1 - b0
    d.eliminate_zeros()
    norms = {id(matrix): base.unweighted_row_upper(matrix)[0]
             for matrix in (b0, b1, d)}
    m1 = norms[id(b1)]
    perturb = (m1 + base.E) ** 4 - m1 ** 4
    chains = ((b0, b0, b0, b0), (d, b0, b0, b0),
              (b1, d, b0, b0), (b1, b1, d, b0),
              (b1, b1, b1, d))
    global_upper = F()
    global_observed = F()
    global_argmax = None
    max_arithmetic = F()
    max_final_row_length = 0
    peak_nnz = [[0] * 4 for _ in chains]
    combined_reference = []
    for first in range(0, b0.shape[0], BATCH_ROWS):
        last = min(first + BATCH_ROWS, b0.shape[0])
        blocks, errors, final_norms = [], [], []
        for word_index, chain in enumerate(chains):
            block, error, c_final, peaks = row_chain(chain, first, last, norms)
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
            global_upper, global_observed = upper, observed
            global_argmax = first + local
    return {
        "upper": global_upper, "observed": global_observed,
        "argmax": global_argmax, "max_arithmetic": max_arithmetic,
        "peak_nnz_by_word_and_stage": peak_nnz,
        "max_final_row_length": max_final_row_length,
        "combined": np.vstack([x.toarray() for x in combined_reference]),
        "seconds": time.time() - started, "d_nnz": int(d.nnz),
    }


if __name__ == "__main__":
    maximum_state_error = base.certify_word_state_tolerance()
    labeled = labeled_cuts()
    cuts = [item[0] for item in labeled]
    anchors = [i for i, (left, right) in enumerate(zip(cuts, cuts[1:]))
               if left[1] < 1 < right[0]]
    assert anchors == [1543]
    b0 = base.assemble(base.R, 1.0)
    b02 = b0 @ b0
    b04 = b02 @ b02
    weight = np.asarray(abs(b04) @ np.ones(b0.shape[0])).ravel()
    assert np.all(np.isfinite(weight)) and np.all(weight > 0)
    weight /= weight.max()
    weight_sha = hashlib.sha256(weight.tobytes(order="C")).hexdigest()
    condition = F.from_float(float(weight.max())) / F.from_float(float(weight.min()))
    results = []
    for neighbor, boundary in ((1542, 1543), (1544, 1544)):
        x = base.midpoint(cuts, neighbor)
        full_b1 = base.assemble(base.R, x)
        label = labeled[boundary][1]
        positions, word_positions = exact_affected_positions(label)
        b1, d, residue_max, residue_nnz = localized_neighbor(
            b0, full_b1, positions)
        assert d.nnz <= 160
        assert residue_max < 2e-15
        direct, b14, direct_seconds = direct_outward(b1, weight, condition)
        factorized = factorized_outward(b0, b1, weight, condition)
        discrepancy = float(np.max(np.abs(factorized["combined"] - b14.toarray())))
        results.append({
            "neighbor_arc": neighbor, "crossed_cut_index": boundary,
            "crossed_label": label, "x": x,
            "affected_word_positions": word_positions,
            "affected_aggregate_positions": len(positions),
            "localized_d_nnz": int(d.nnz),
            "full_subtraction_d_nnz": int((full_b1 - b0).nnz),
            "unchanged_entry_roundoff_residue_nnz": residue_nnz,
            "unchanged_entry_roundoff_residue_max": residue_max,
            "direct_outward_b4": float(direct),
            "direct_fourth_root": float(direct) ** 0.25,
            "factorized_outward_b4": float(factorized["upper"]),
            "factorized_fourth_root": float(factorized["upper"]) ** 0.25,
            "factorized_argmax": factorized["argmax"],
            "max_arithmetic_allowance": float(factorized["max_arithmetic"]),
            "max_final_row_length": factorized["max_final_row_length"],
            "peak_nnz_by_word_and_stage": factorized["peak_nnz_by_word_and_stage"],
            "max_binary64_entry_discrepancy_vs_direct_b14": discrepancy,
            "direct_seconds": direct_seconds,
            "factorized_seconds": factorized["seconds"],
            "factorized_to_direct_time_ratio": factorized["seconds"] / direct_seconds,
            "pass": factorized["upper"] < base.TARGET,
        })
    summary = {
        "radius": base.R, "cut_count": len(cuts), "anchor_arc": 1543,
        "dimension": int(b0.shape[0]), "weight_sha256": weight_sha,
        "weight_condition": float(condition),
        "max_exact_word_state_error": float(maximum_state_error),
        "results": results, "target4": float(base.TARGET),
        "source_path": str(SOURCE),
        "method": "exact_crossed_corner_support_then_signed_five_word_update",
        "scope": "R3_two_adjacent_arcs_only_no_C3_no_C16",
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print("STATUS=EXACT_SUPPORT_FACTORIZED_PASS"
          if all(result["pass"] for result in results)
          else "STATUS=METHOD_FAIL_NOT_SPECTRAL_LOWER_BOUND")
