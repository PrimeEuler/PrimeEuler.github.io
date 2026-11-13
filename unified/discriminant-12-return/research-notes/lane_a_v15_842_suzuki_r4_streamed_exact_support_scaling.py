#!/usr/bin/env python3
"""R4 memory-bounded exact-support factorized update scaling gate.

Constructs the anchor weight and all fourth-power rows in batches.  Compares
direct B1^4 recomputation with the signed five-word identity and separately
times the cached B0^4 anchor word versus the four update words.  This is a
two-transition R4 method/resource test, not C4 or C16.
"""
import hashlib
import json
import time
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
from pathlib import Path

import numpy as np

RADIUS = 4
BATCH_ROWS = 64
SOURCE_NAME = "lane_a_v15_800_suzuki_r3_norm_transport_obstruction.py"
HERE = Path(__file__).resolve().parent
SOURCE_CANDIDATES = (HERE / SOURCE_NAME,
                     HERE.parent / "research-notes" / SOURCE_NAME)
SOURCE = next((p for p in SOURCE_CANDIDATES if p.is_file()), None)
if SOURCE is None:
    raise FileNotFoundError(f"cannot locate {SOURCE_NAME}: {SOURCE_CANDIDATES}")
spec = spec_from_file_location("base", SOURCE)
base = module_from_spec(spec)
spec.loader.exec_module(base)
base.R = RADIUS


def labeled_cuts():
    cuts = []
    for k0 in range(-RADIUS - 1, RADIUS + 2):
        for k1, k2, k3 in product(range(-RADIUS, RADIUS + 1), repeat=3):
            label = (k0, k1, k2, k3)
            cuts.append((base.cut_interval(label), label))
    cuts.sort(key=lambda item: item[0][0])
    assert len(cuts) == (2 * RADIUS + 3) * (2 * RADIUS + 1) ** 3
    for left, right in zip(cuts, cuts[1:]):
        assert left[0][1] < right[0][0]
    return cuts


def affected_positions(label):
    width = 2 * RADIUS + 1
    sites = np.indices((width,) * 4, dtype=np.int16).reshape(4, -1).T
    h = sites.astype(np.int32) - RADIUS
    positions = set()
    word_positions = 0
    for q, r in combinations(base.Q, 2):
        vq, vr = np.asarray(base.V[q]), np.asarray(base.V[r])
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


def row_word(chain, first, last, norms):
    block = chain[0][first:last, :]
    error = F()
    peaks = [int(block.nnz)]
    for right in chain[1:]:
        c_input, k_input = base.unweighted_row_upper(block)
        m_right = norms[id(right)]
        error = error * m_right + base.gamma(2 * k_input) * c_input * m_right
        block = block @ right
        peaks.append(int(block.nnz))
    c_final, _ = base.unweighted_row_upper(block)
    return block, error, c_final, peaks


def streamed_anchor_weight(b0):
    started = time.perf_counter()
    norms = {id(b0): base.unweighted_row_upper(b0)[0]}
    weight = np.empty(b0.shape[0])
    ones = np.ones(b0.shape[0])
    peak = [0] * 4
    for first in range(0, b0.shape[0], BATCH_ROWS):
        last = min(first + BATCH_ROWS, b0.shape[0])
        block, _, _, peaks = row_word((b0, b0, b0, b0), first, last, norms)
        weight[first:last] = np.asarray(abs(block) @ ones).ravel()
        peak = [max(a, b) for a, b in zip(peak, peaks)]
    assert np.all(np.isfinite(weight)) and np.all(weight > 0)
    weight /= weight.max()
    return weight, time.perf_counter() - started, peak


def direct_stream(b1, weight, condition):
    started = time.perf_counter()
    norms = {id(b1): base.unweighted_row_upper(b1)[0]}
    m1 = norms[id(b1)]
    perturb = (m1 + base.E) ** 4 - m1 ** 4
    global_upper = F()
    global_observed = F()
    argmax = None
    max_arithmetic = F()
    max_row_length = 0
    peak = [0] * 4
    for first in range(0, b1.shape[0], BATCH_ROWS):
        last = min(first + BATCH_ROWS, b1.shape[0])
        block, arithmetic, _, peaks = row_word(
            (b1, b1, b1, b1), first, last, norms)
        peak = [max(a, b) for a, b in zip(peak, peaks)]
        max_arithmetic = max(max_arithmetic, arithmetic)
        k = int(np.diff(block.indptr).max())
        max_row_length = max(max_row_length, k)
        ratios = np.asarray(abs(block) @ weight).ravel() / weight[first:last]
        local = int(ratios.argmax())
        observed = F.from_float(float(ratios[local]))
        stored = observed / (1 - base.gamma(2 * k + 1))
        upper = stored + condition * (arithmetic + perturb)
        if upper > global_upper:
            global_upper, global_observed = upper, observed
            argmax = first + local
    return {"upper": global_upper, "observed": global_observed,
            "argmax": argmax, "max_arithmetic": max_arithmetic,
            "max_row_length": max_row_length, "peak_nnz": peak,
            "seconds": time.perf_counter() - started}


def factorized_stream(b0, b1, weight, condition):
    started = time.perf_counter()
    d = b1 - b0
    d.eliminate_zeros()
    norms = {id(matrix): base.unweighted_row_upper(matrix)[0]
             for matrix in (b0, b1, d)}
    m1 = norms[id(b1)]
    perturb = (m1 + base.E) ** 4 - m1 ** 4
    chains = ((b0, b0, b0, b0), (d, b0, b0, b0),
              (b1, d, b0, b0), (b1, b1, d, b0),
              (b1, b1, b1, d))
    word_seconds = [0.0] * 5
    peaks = [[0] * 4 for _ in chains]
    global_upper = F()
    global_observed = F()
    argmax = None
    max_arithmetic = F()
    max_row_length = 0
    for first in range(0, b0.shape[0], BATCH_ROWS):
        last = min(first + BATCH_ROWS, b0.shape[0])
        blocks, errors, finals = [], [], []
        for wi, chain in enumerate(chains):
            tick = time.perf_counter()
            block, error, c_final, word_peak = row_word(
                chain, first, last, norms)
            word_seconds[wi] += time.perf_counter() - tick
            blocks.append(block)
            errors.append(error)
            finals.append(c_final)
            peaks[wi] = [max(a, b) for a, b in zip(peaks[wi], word_peak)]
        combined = blocks[0]
        for block in blocks[1:]:
            combined = combined + block
        addition = base.gamma(5) * sum(finals, F())
        arithmetic = sum(errors, F()) + addition
        max_arithmetic = max(max_arithmetic, arithmetic)
        k = int(np.diff(combined.indptr).max())
        max_row_length = max(max_row_length, k)
        ratios = np.asarray(abs(combined) @ weight).ravel() / weight[first:last]
        local = int(ratios.argmax())
        observed = F.from_float(float(ratios[local]))
        stored = observed / (1 - base.gamma(2 * k + 1))
        upper = stored + condition * (arithmetic + perturb)
        if upper > global_upper:
            global_upper, global_observed = upper, observed
            argmax = first + local
    total = time.perf_counter() - started
    return {"upper": global_upper, "observed": global_observed,
            "argmax": argmax, "max_arithmetic": max_arithmetic,
            "max_row_length": max_row_length, "peak_nnz": peaks,
            "word_seconds": word_seconds,
            "anchor_word_seconds": word_seconds[0],
            "update_words_seconds": sum(word_seconds[1:]),
            "total_seconds": total, "d_nnz": int(d.nnz)}


if __name__ == "__main__":
    maximum_state_error = base.certify_word_state_tolerance()
    labeled = labeled_cuts()
    cuts = [item[0] for item in labeled]
    anchors = [i for i, (left, right) in enumerate(zip(cuts, cuts[1:]))
               if left[1] < 1 < right[0]]
    assert len(anchors) == 1
    anchor = anchors[0]
    b0 = base.assemble(RADIUS, 1.0)
    weight, weight_seconds, weight_peak = streamed_anchor_weight(b0)
    weight_sha = hashlib.sha256(weight.tobytes(order="C")).hexdigest()
    condition = F.from_float(float(weight.max())) / F.from_float(float(weight.min()))
    results = []
    for neighbor, boundary in ((anchor - 1, anchor), (anchor + 1, anchor + 1)):
        x = base.midpoint(cuts, neighbor)
        full_b1 = base.assemble(RADIUS, x)
        label = labeled[boundary][1]
        positions, word_positions = affected_positions(label)
        b1, d, residue_max, residue_nnz = localized_neighbor(
            b0, full_b1, positions)
        assert d.nnz <= 160 and residue_max < 2e-15
        direct = direct_stream(b1, weight, condition)
        factor = factorized_stream(b0, b1, weight, condition)
        results.append({
            "neighbor_arc": neighbor, "crossed_cut_index": boundary,
            "crossed_label": label, "x": x,
            "affected_word_positions": word_positions,
            "affected_aggregate_positions": len(positions),
            "localized_d_nnz": int(d.nnz),
            "full_subtraction_d_nnz": int((full_b1 - b0).nnz),
            "roundoff_residue_nnz": residue_nnz,
            "roundoff_residue_max": residue_max,
            "direct_outward_b4": float(direct["upper"]),
            "direct_fourth_root": float(direct["upper"]) ** 0.25,
            "direct_seconds": direct["seconds"],
            "direct_peak_nnz": direct["peak_nnz"],
            "factorized_outward_b4": float(factor["upper"]),
            "factorized_fourth_root": float(factor["upper"]) ** 0.25,
            "factorized_total_seconds": factor["total_seconds"],
            "factorized_anchor_word_seconds": factor["anchor_word_seconds"],
            "factorized_update_words_seconds": factor["update_words_seconds"],
            "factorized_word_seconds": factor["word_seconds"],
            "factorized_peak_nnz": factor["peak_nnz"],
            "factorized_to_direct_ratio": factor["total_seconds"] / direct["seconds"],
            "update_only_to_direct_ratio": factor["update_words_seconds"] / direct["seconds"],
            "direct_pass": direct["upper"] < base.TARGET,
            "factorized_pass": factor["upper"] < base.TARGET,
        })
    summary = {
        "radius": RADIUS, "dimension": int(b0.shape[0]),
        "matrix_nnz": int(b0.nnz), "cut_count": len(cuts),
        "anchor_arc": anchor, "batch_rows": BATCH_ROWS,
        "weight_sha256": weight_sha, "weight_condition": float(condition),
        "weight_seconds": weight_seconds, "weight_peak_nnz": weight_peak,
        "max_exact_word_state_error": float(maximum_state_error),
        "target4": float(base.TARGET), "results": results,
        "method": "R4_row_streamed_exact_support_signed_update_scaling",
        "scope": "two_adjacent_R4_transitions_no_C4_no_C16",
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print("STATUS=R4_SCALING_METHOD_PASS"
          if all(r["direct_pass"] and r["factorized_pass"] for r in results)
          else "STATUS=METHOD_FAIL_NOT_SPECTRAL_LOWER_BOUND")
