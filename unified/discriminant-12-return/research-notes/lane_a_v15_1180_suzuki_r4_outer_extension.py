#!/usr/bin/env python3
"""Block-partitioned R4 exact-support coverage with periodic direct rebasing.

Starting from the x=1 anchor, constructs through 640 exact cuts in either
direction and certifies only the outer extension, steps 513 through 640,
using the four signed mixed update words.
Arithmetic error is accumulated for four updates, then the current B^4 block
is recomputed directly and the error recurrence is restarted from that direct
word certificate.  Every reached state is independently recomputed
row-streamingly for validation.  This is not an all-arc C4/C16 certificate.
"""
import hashlib
import json
import time
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import numpy as np

STEPS = 640
START_STEP = 512
REBASE_INTERVAL = 4
RESULT_NAME = "lane_a_v15_1180_suzuki_r4_outer_extension_certificate.json"
SOURCE_NAME = "lane_a_v15_842_suzuki_r4_streamed_exact_support_scaling.py"
HERE = Path(__file__).resolve().parent
SOURCE_CANDIDATES = (HERE / SOURCE_NAME,
                     HERE.parent / "research-notes" / SOURCE_NAME)
SOURCE = next((p for p in SOURCE_CANDIDATES if p.is_file()), None)
if SOURCE is None:
    raise FileNotFoundError(f"cannot locate {SOURCE_NAME}: {SOURCE_CANDIDATES}")
spec = spec_from_file_location("prev", SOURCE)
prev = module_from_spec(spec)
spec.loader.exec_module(prev)
base = prev.base


def build_sequence(b_anchor, labeled, cuts, anchor, direction):
    matrices = [b_anchor]
    metadata = []
    current = b_anchor
    for step in range(1, STEPS + 1):
        target = anchor + direction * step
        boundary = target if direction > 0 else target + 1
        label = labeled[boundary][1]
        positions, word_positions = prev.affected_positions(label)
        full_next = base.assemble(prev.RADIUS, base.midpoint(cuts, target))
        next_matrix, d, residue_max, residue_nnz = prev.localized_neighbor(
            current, full_next, positions)
        assert d.nnz <= 160 and residue_max < 2e-15
        metadata.append({
            "step": step, "arc": target, "crossed_cut": boundary,
            "crossed_label": label,
            "affected_word_positions": word_positions,
            "affected_aggregate_positions": len(positions),
            "d_nnz": int(d.nnz),
            "naive_d_nnz": int((full_next - current).nnz),
            "roundoff_residue_max": residue_max,
            "roundoff_residue_nnz": residue_nnz,
        })
        matrices.append(next_matrix)
        current = next_matrix
    return matrices, metadata


def direct_validations(matrices, weight, condition):
    results = []
    for matrix in matrices[1:]:
        result = prev.direct_stream(matrix, weight, condition)
        results.append(result)
    return results


def inplace_sweep(matrices, weight, condition):
    started = time.perf_counter()
    transitions = []
    for left, right in zip(matrices, matrices[1:]):
        d = right - left
        d.eliminate_zeros()
        transitions.append((left, right, d))

    global_upper = [F() for _ in transitions]
    global_observed = [F() for _ in transitions]
    global_argmax = [None for _ in transitions]
    max_cumulative_arithmetic = [F() for _ in transitions]
    max_row_length = [0 for _ in transitions]
    max_direct_discrepancy = [0.0 for _ in transitions]
    update_seconds = [0.0 for _ in transitions]
    rebase_seconds = [0.0 for _ in transitions]
    rebase_before_update = [False for _ in transitions]
    max_rebase_arithmetic = [F() for _ in transitions]
    peak_nnz = [[[0] * 4 for _ in range(4)] for _ in transitions]

    anchor = matrices[0]
    anchor_norm = base.unweighted_row_upper(anchor)[0]
    anchor_norms = {id(anchor): anchor_norm}
    for first in range(0, anchor.shape[0], prev.BATCH_ROWS):
        last = min(first + prev.BATCH_ROWS, anchor.shape[0])
        current_block, cumulative_error, current_c, _ = prev.row_word(
            (anchor, anchor, anchor, anchor), first, last, anchor_norms)
        # The extension begins from an independently rebuilt step-512 state.
        # Count that exact restart as the rebase before extension step 513.
        if transitions:
            rebase_before_update[0] = True
            max_rebase_arithmetic[0] = max(
                max_rebase_arithmetic[0], cumulative_error)

        for si, (left, right, d) in enumerate(transitions):
            norms = {id(matrix): base.unweighted_row_upper(matrix)[0]
                     for matrix in (left, right, d)}
            if si and si % REBASE_INTERVAL == 0:
                tick = time.perf_counter()
                current_block, cumulative_error, current_c, _ = prev.row_word(
                    (left, left, left, left), first, last,
                    {id(left): norms[id(left)]})
                rebase_seconds[si] += time.perf_counter() - tick
                rebase_before_update[si] = True
                max_rebase_arithmetic[si] = max(
                    max_rebase_arithmetic[si], cumulative_error)
            chains = ((d, left, left, left),
                      (right, d, left, left),
                      (right, right, d, left),
                      (right, right, right, d))
            blocks, errors, finals = [], [], []
            tick = time.perf_counter()
            for wi, chain in enumerate(chains):
                block, error, c_final, peaks = prev.row_word(
                    chain, first, last, norms)
                blocks.append(block)
                errors.append(error)
                finals.append(c_final)
                peak_nnz[si][wi] = [max(a, b) for a, b in
                                    zip(peak_nnz[si][wi], peaks)]
            combined = current_block
            for block in blocks:
                combined = combined + block
            update_seconds[si] += time.perf_counter() - tick

            addition = base.gamma(5) * (current_c + sum(finals, F()))
            cumulative_error += sum(errors, F()) + addition
            max_cumulative_arithmetic[si] = max(
                max_cumulative_arithmetic[si], cumulative_error)

            direct_block, _, _, _ = prev.row_word(
                (right, right, right, right), first, last,
                {id(right): norms[id(right)]})
            difference = combined - direct_block
            difference.eliminate_zeros()
            discrepancy = float(abs(difference).max()) if difference.nnz else 0.0
            max_direct_discrepancy[si] = max(
                max_direct_discrepancy[si], discrepancy)

            current_c, _ = base.unweighted_row_upper(combined)
            k = int(np.diff(combined.indptr).max())
            max_row_length[si] = max(max_row_length[si], k)
            ratios = (np.asarray(abs(combined) @ weight).ravel()
                      / weight[first:last])
            local = int(ratios.argmax())
            observed = F.from_float(float(ratios[local]))
            stored = observed / (1 - base.gamma(2 * k + 1))
            m_right = norms[id(right)]
            perturb = (m_right + base.E) ** 4 - m_right ** 4
            upper = stored + condition * (cumulative_error + perturb)
            if upper > global_upper[si]:
                global_upper[si] = upper
                global_observed[si] = observed
                global_argmax[si] = first + local
            current_block = combined

    elapsed = time.perf_counter() - started
    return [{
        "outward_b4": float(global_upper[i]),
        "fourth_root": float(global_upper[i]) ** 0.25,
        "argmax": global_argmax[i],
        "max_cumulative_arithmetic": float(max_cumulative_arithmetic[i]),
        "max_row_length": max_row_length[i],
        "max_entry_discrepancy_vs_direct": max_direct_discrepancy[i],
        "update_seconds": update_seconds[i],
        "rebase_before_update": rebase_before_update[i],
        "rebase_seconds": rebase_seconds[i],
        "max_rebase_arithmetic": float(max_rebase_arithmetic[i]),
        "peak_nnz_by_update_word": peak_nnz[i],
        "pass": global_upper[i] < base.TARGET,
    } for i in range(len(transitions))], elapsed


if __name__ == "__main__":
    max_state_error = base.certify_word_state_tolerance()
    labeled = prev.labeled_cuts()
    cuts = [item[0] for item in labeled]
    anchors = [i for i, (left, right) in enumerate(zip(cuts, cuts[1:]))
               if left[1] < 1 < right[0]]
    assert anchors == [4009]
    anchor = anchors[0]
    b_anchor = base.assemble(prev.RADIUS, 1.0)
    weight, weight_seconds, _ = prev.streamed_anchor_weight(b_anchor)
    weight_sha = hashlib.sha256(weight.tobytes(order="C")).hexdigest()
    condition = F.from_float(float(weight.max())) / F.from_float(float(weight.min()))

    directions = []
    for direction in (-1, 1):
        matrices, metadata = build_sequence(
            b_anchor, labeled, cuts, anchor, direction)
        extension_matrices = matrices[START_STEP:]
        extension_metadata = metadata[START_STEP:]
        assert extension_matrices[0] is matrices[START_STEP]
        assert extension_metadata[0]["step"] == START_STEP + 1
        direct = direct_validations(extension_matrices, weight, condition)
        sweep, elapsed = inplace_sweep(extension_matrices, weight, condition)
        for meta, direct_result, sweep_result in zip(
                extension_metadata, direct, sweep):
            meta.update({
                "direct_outward_b4": float(direct_result["upper"]),
                "direct_fourth_root": float(direct_result["upper"]) ** 0.25,
                "direct_seconds": direct_result["seconds"],
                "sweep": sweep_result,
                "sweep_minus_direct_b4": (sweep_result["outward_b4"]
                                           - float(direct_result["upper"])),
            })
        directions.append({
            "direction": direction, "states": extension_metadata,
            "inplace_total_seconds": elapsed,
            "all_pass": all(
                item["sweep"]["pass"] for item in extension_metadata),
        })

    states = []
    for direction in directions:
        for state in direction["states"]:
            sweep = state["sweep"]
            states.append({
                "direction": direction["direction"],
                "step": state["step"],
                "arc": state["arc"],
                "crossed_cut": state["crossed_cut"],
                "crossed_label": state["crossed_label"],
                "d_nnz": state["d_nnz"],
                "roundoff_residue_max": state["roundoff_residue_max"],
                "direct_outward_b4": state["direct_outward_b4"],
                "direct_fourth_root": state["direct_fourth_root"],
                "propagated_outward_b4": sweep["outward_b4"],
                "propagated_fourth_root": sweep["fourth_root"],
                "max_cumulative_arithmetic":
                    sweep["max_cumulative_arithmetic"],
                "max_rebase_arithmetic": sweep["max_rebase_arithmetic"],
                "max_entry_discrepancy_vs_direct":
                    sweep["max_entry_discrepancy_vs_direct"],
                "sweep_minus_direct_b4": state["sweep_minus_direct_b4"],
                "rebase_before_update": sweep["rebase_before_update"],
                "pass": sweep["pass"],
            })

    certificate = {
        "radius": prev.RADIUS, "dimension": int(b_anchor.shape[0]),
        "matrix_nnz": int(b_anchor.nnz), "cut_count": len(cuts),
        "anchor_arc": anchor, "steps_each_direction": STEPS,
        "start_step_exclusive": START_STEP,
        "rebase_interval": REBASE_INTERVAL,
        "batch_rows": prev.BATCH_ROWS, "weight_sha256": weight_sha,
        "weight_condition": float(condition),
        "max_exact_word_state_error": float(max_state_error),
        "target4": float(base.TARGET), "states": states,
        "method": "R4_periodic_direct_rebase_exact_support_sweep",
        "scope": "256_outer_extension_transitions_only_no_C4_no_C16",
    }
    certificate_text = json.dumps(
        certificate, sort_keys=True, indent=2) + "\n"
    (HERE / RESULT_NAME).write_text(certificate_text, encoding="utf-8")
    certificate_sha = hashlib.sha256(
        certificate_text.encode("utf-8")).hexdigest()

    summary = {
        "radius": prev.RADIUS,
        "dimension": int(b_anchor.shape[0]),
        "cut_count": len(cuts),
        "anchor_arc": anchor,
        "steps_each_direction": STEPS,
        "start_step_exclusive": START_STEP,
        "rebase_interval": REBASE_INTERVAL,
        "state_count": len(states),
        "min_arc": min(state["arc"] for state in states),
        "max_arc": max(state["arc"] for state in states),
        "max_exact_support": max(state["d_nnz"] for state in states),
        "max_direct_fourth_root":
            max(state["direct_fourth_root"] for state in states),
        "max_propagated_fourth_root":
            max(state["propagated_fourth_root"] for state in states),
        "max_propagated_b4":
            max(state["propagated_outward_b4"] for state in states),
        "max_cumulative_arithmetic":
            max(state["max_cumulative_arithmetic"] for state in states),
        "max_rebase_arithmetic":
            max(state["max_rebase_arithmetic"] for state in states),
        "max_entry_discrepancy":
            max(state["max_entry_discrepancy_vs_direct"] for state in states),
        "max_sweep_minus_direct_b4":
            max(state["sweep_minus_direct_b4"] for state in states),
        "rebase_arcs":
            [state["arc"] for state in states
             if state["rebase_before_update"]],
        "all_pass": all(state["pass"] for state in states),
        "weight_sha256": weight_sha,
        "weight_condition": float(condition),
        "weight_seconds": weight_seconds,
        "target4": float(base.TARGET),
        "direct_seconds_total":
            sum(state["direct_seconds"] for direction in directions
                for state in direction["states"]),
        "update_seconds_total":
            sum(state["sweep"]["update_seconds"] for direction in directions
                for state in direction["states"]),
        "rebase_seconds_total":
            sum(state["sweep"]["rebase_seconds"] for direction in directions
                for state in direction["states"]),
        "inplace_seconds_total":
            sum(direction["inplace_total_seconds"] for direction in directions),
        "certificate": RESULT_NAME,
        "certificate_sha256": certificate_sha,
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print("STATUS=R4_BLOCK_COVERAGE_PASS"
          if all(item["all_pass"] for item in directions)
          else "STATUS=R4_BLOCK_METHOD_FAIL_NOT_SPECTRAL_LOWER_BOUND")

