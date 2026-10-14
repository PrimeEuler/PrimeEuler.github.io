#!/usr/bin/env python3
import hashlib
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

BITS = 256
S = 1 << BITS
COUNT_GAP = 520191
THRESHOLD = F(3, 100000)

ROOT = Path("payload_parts")
ARTIFACT = {"even-v": Path("artifact_even"), "odd-v": Path("artifact_odd")}
SELF_TERM_ENVELOPE = {
    "even-v": F("7.477876064972278e-11") + F("5.949974071695278e-12"),
    "odd-v": F("7.471369690680121e-11") + F("5.937109576528497e-12"),
}


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def upper(q):
    assert q >= 0
    n = q.numerator * S * S
    d = q.denominator
    k = isqrt(n // d)
    if k * k * d < n:
        k += 1
    return F(k, S)


def norm_from_sum_squares(sum_squares):
    q = F(sum_squares, S * S)
    hi = upper(q)
    lo = max(F(0), hi - F(1, S))
    assert lo * lo <= q <= hi * hi
    return lo, hi


def decode(path, spec):
    raw = path.read_bytes()
    assert len(raw) == spec["bytes"] == spec["count"] * spec["width"]
    assert sha256(raw) == spec["sha256"]
    assert spec["bits"] == BITS and spec["width"] == 30
    return [
        int.from_bytes(raw[i:i + spec["width"]], "little", signed=True)
        for i in range(0, len(raw), spec["width"])
    ]


def write_buffer(path, values):
    width = max(1, (max(abs(v).bit_length() for v in values) + 8) // 8)
    raw = b"".join(v.to_bytes(width, "little", signed=True) for v in values)
    path.write_bytes(raw)
    return {
        "file": path.name,
        "bits": BITS,
        "width": width,
        "count": len(values),
        "bytes": len(raw),
        "sha256": sha256(raw),
    }


def finite_values(root, cert):
    values = []
    for label in ("Near", "Middle", "Far-window"):
        spec = cert["buffers"][label]
        values.extend(decode(root / spec["file"], spec))
    assert len(values) == 392192
    return values


def compose(sector):
    start = 1 if sector == "even-v" else 2
    shift = start - 1
    compact_cert_path = ROOT / f"wider-compact-gap-{sector}.json"
    seed_cert_path = ROOT / f"gap-action-{sector}.json"
    finite_cert_path = ARTIFACT[sector] / f"wider-finite-residual-{sector}.json"
    compact_cert = json.loads(compact_cert_path.read_text())
    seed_cert = json.loads(seed_cert_path.read_text())
    finite_cert = json.loads(finite_cert_path.read_text())

    assert compact_cert["first_output_mode"] == seed_cert["output_first_mode"]
    assert compact_cert["last_output_mode"] == seed_cert["output_last_mode"]
    assert compact_cert["complete_output_rows"] == seed_cert["output_count"] == COUNT_GAP
    assert compact_cert["diagonal_absent_beyond_support"]
    assert not compact_cert["original_infinite_seed_action_included"]
    assert seed_cert["self_rows_excluded_with_represented_reciprocal"]
    assert not seed_cert["whole_infinite_action_evaluated"]

    compact = decode(
        ROOT / f"{sector}-wider-compact-gap-action.bin",
        compact_cert["buffer"],
    )
    seed = decode(
        ROOT / f"{sector}-gap-action.bin",
        seed_cert["point_buffer"],
    )
    first = seed_cert["output_first_mode"]
    residual = [
        S // (first + 2 * i - shift) - a - b
        for i, (a, b) in enumerate(zip(compact, seed))
    ]
    gap_sum_squares = sum(v * v for v in residual)
    gap_lo, gap_hi = norm_from_sum_squares(gap_sum_squares)
    compact_error = F(compact_cert["rational"]["complete_compact_gap_error_upper"])
    seed_error = F(seed_cert["rational"]["complete_l2_error_upper"])
    source_floor = upper(F(COUNT_GAP)) / S
    gap_error = compact_error + seed_error + source_floor
    gap_physical_lo = max(F(0), gap_lo - gap_error)
    gap_physical_hi = gap_hi + gap_error

    finite = finite_values(ARTIFACT[sector], finite_cert)
    finite_sum_squares = sum(v * v for v in finite)
    assert norm_from_sum_squares(finite_sum_squares) == (
        F(finite_cert["rational"]["finite_point_norm_lower"]),
        F(finite_cert["rational"]["finite_point_norm_upper"]),
    )
    combined_lo, combined_hi = norm_from_sum_squares(finite_sum_squares + gap_sum_squares)
    finite_error_uncorrected = F(
        finite_cert["rational"]["complete_finite_physical_error_upper"]
    )
    self_term_envelope = SELF_TERM_ENVELOPE[sector]
    finite_error = finite_error_uncorrected + self_term_envelope
    combined_physical_error = upper(finite_error * finite_error + gap_error * gap_error)
    combined_physical_lo = max(F(0), combined_lo - combined_physical_error)
    combined_physical_hi = combined_hi + combined_physical_error
    transport = F(finite_cert["rational"]["global_source_and_new_lift_transport_once"])
    schur_lo = max(F(0), combined_physical_lo - transport)
    schur_hi = combined_physical_hi + transport

    q = (THRESHOLD - transport) ** 2 - combined_physical_hi ** 2
    beyond_gap_allowance = F(0)
    if q > 0:
        beyond_gap_allowance = max(F(0), upper(q) - F(1, S))
        assert beyond_gap_allowance * beyond_gap_allowance <= q

    output = Path("composition_output")
    output.mkdir(exist_ok=True)
    gap_buffer = write_buffer(output / f"{sector}-wider-gap-residual.bin", residual)
    rational = {
        "gap_point_norm_lower": gap_lo,
        "gap_point_norm_upper": gap_hi,
        "compact_gap_action_error_upper": compact_error,
        "original_seed_gap_action_error_upper": seed_error,
        "gap_bare_source_floor_error_upper": source_floor,
        "complete_gap_physical_error_upper": gap_error,
        "gap_physical_residual_lower": gap_physical_lo,
        "gap_physical_residual_upper": gap_physical_hi,
        "finite_plus_gap_point_norm_lower": combined_lo,
        "finite_plus_gap_point_norm_upper": combined_hi,
        "v14_353_finite_physical_error_upper_before_v14_354": finite_error_uncorrected,
        "v14_354_region_2_and_3_self_term_envelope_once": self_term_envelope,
        "corrected_complete_finite_physical_error_upper": finite_error,
        "quadrature_combined_disjoint_physical_error_upper": combined_physical_error,
        "finite_plus_gap_physical_residual_lower": combined_physical_lo,
        "finite_plus_gap_physical_residual_upper": combined_physical_hi,
        "global_source_and_new_lift_transport_once": transport,
        "finite_plus_gap_Schur_residual_lower": schur_lo,
        "finite_plus_gap_Schur_residual_upper": schur_hi,
        "certified_beyond_gap_physical_residual_allowance": beyond_gap_allowance,
    }
    result = {
        "schema": "cone.wider-finite-plus-gap-residual-composition.v1",
        "sector": sector,
        "finite_residual_certificate_sha256": sha256(finite_cert_path.read_bytes()),
        "compact_gap_certificate_sha256": sha256(compact_cert_path.read_bytes()),
        "original_seed_gap_certificate_sha256": sha256(seed_cert_path.read_bytes()),
        "compact_gap_buffer_sha256": compact_cert["buffer"]["sha256"],
        "original_seed_gap_buffer_sha256": seed_cert["point_buffer"]["sha256"],
        "gap_residual_buffer": gap_buffer,
        "source_bare_formula": "1/n" if sector == "even-v" else "1/(n-1)",
        "gap_first_output_mode": first,
        "gap_last_output_mode": seed_cert["output_last_mode"],
        "gap_rows": COUNT_GAP,
        "finite_rows": len(finite),
        "evaluated_rows": len(finite) + COUNT_GAP,
        "v14_354_correction_carried_exactly_once": True,
        "correction_accounting": (
            "v14.353 finite buffers retain the v14.327 Region-2/Region-3 artificial "
            "self term, so the v14.354 sectorwise Region-2 plus Region-3 upper "
            "envelope is charged once to the finite physical error and nowhere "
            "else; compact gap has no diagonal beyond compact support; the "
            "v14.393 original-seed gap buffer excludes represented self rows and "
            "includes its raw diagonal"
        ),
        "rational": {k: str(v) for k, v in rational.items()},
        "display_approximate": {k: float(v) for k, v in rational.items()},
        "finite_plus_gap_upper_below_3e_minus5": schur_hi < THRESHOLD,
        "whole_infinite_residual_evaluated": False,
        "whole_residual_acceptance_certified": False,
        "stationary_acceptance_met": False,
        "infinite_capacity_tail_closed": False,
    }
    cert_path = output / f"finite-plus-gap-residual-{sector}.json"
    cert_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


if __name__ == "__main__":
    report = {sector: compose(sector) for sector in ("even-v", "odd-v")}
    print(json.dumps(
        {s: d["display_approximate"] for s, d in report.items()},
        indent=2,
        sort_keys=True,
    ))
