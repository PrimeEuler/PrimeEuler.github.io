#!/usr/bin/env python3
"""Compose the v14.403 gap-refined compact action with the original seed action.

This consumer is intentionally inert until explicit hashes for the newly
returned 912383-row compact-action certificate and point buffer are supplied.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, base64, hashlib, json

from suzuki_returned_tail_residual_composition import read, upper, norm, write

S = 1 << 256
FINITE_COUNT = 392192
GAP_COUNT = 520191
COUNT = FINITE_COUNT + GAP_COUNT

SOURCE = {
    "even-v": "40fcbd9ba5745598fa0e8d98a5da43b7c088411c8fdcb4c6d0dcae10a0b9dc80",
    "odd-v": "41fdeb3af0ab1d00bc154cc7111b62d28d5e75365de795ce4a970f779e25138f",
}
NEW_LIFT = {
    "even-v": "4d49b475c4a6b97de137258d7b53415b914aec8fa1a0fb52f8b6400ba214bfb3",
    "odd-v": "f2f2a9e3c018902198a8a9b7df5e91bba42a81de4bd1334cffaa1e2fb0cf0daf",
}
GAP_RHS = {
    "even-v": "42c71d7e017eadc08a6ebe20045f6d6e83bbe3523e17ba282903eccf08edc075",
    "odd-v": "1309bec0a4568684f3631a2d88a278ba711c8496960491e5a81428a8fb5b30b3",
}
OLD_CAND = {
    "even-v": "fdf93112802fe28ef53efa804be760a0fc17abc404993c8b2af6c33b1b5aba05",
    "odd-v": "b772ab850121daf0bd85afd01e26fee9f72d14b940c4145ae7643734435f8967",
}
GAP_CAND = {
    "even-v": "171883d6c8e41e9a92f88bea4fa96b70f538ada49ea296876e1f06aebe1f9da6",
    "odd-v": "f3a9b9a06efb728ee8ed51b4294fbd406d0b9bad8248831d03b3c4586f846a66",
}
TAIL1 = {
    "even-v": "af8ddb14f7499856b55a1904d715157cb6047ba46982ab3502b4b36d48fc8490",
    "odd-v": "38c1dbd4c95fa810eebe1c7c001b90107305e69785e919c1e2703e83f8e29604",
}
GAP_SEED_BUFFER = {
    "even-v": "00c1651f1013f821d3135f136bb91a9196792ff9663b4762d7d80a42dbc66af6",
    "odd-v": "675138c2ff20728945989bd14aa8c1a004a54229847a9664de4992a0d972c413",
}
SELF_TERM = {
    "even-v": (F("7.477876064972278e-11"), F("5.949974071695278e-12")),
    "odd-v": (F("7.471369690680121e-11"), F("5.937109576528497e-12")),
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def pinned(path, pin):
    raw = path.read_bytes()
    assert sha(raw) == pin
    return json.loads(raw)


def decode(raw, spec):
    assert spec["bits"] == 256 and spec["width"] == 30
    assert len(raw) == spec["bytes"] == spec["count"] * spec["width"]
    assert sha(raw) == spec["sha256"]
    return [
        int.from_bytes(raw[i:i + spec["width"]], "little", signed=True)
        for i in range(0, len(raw), spec["width"])
    ]


def load_finite_seed(tail1_root, tail23_root, sector):
    start = 1 if sector == "even-v" else 2
    t1 = pinned(tail1_root / f"region1-close-plus-far-action-{sector}.json", TAIL1[sector])
    sp = t1["composed_action_buffer"]
    near = decode((tail1_root / sp["file"]).read_bytes(), sp)
    assert len(near) == 128000
    assert t1["output_first_mode"] == 256000 + start
    assert t1["far_input_action_included_once"] and t1["far_pole_included_once"]
    errors = [F(t1["rational"]["composed_region1_action_l2_error_upper"])]

    manifest, manifest_sha = read(tail23_root, "manifest.json")
    points = list(near)
    certificate_sha = [TAIL1[sector]]
    for region, count, first in (
        (2, 256000, 512000 + start),
        (3, 8192, 1024000 + start),
    ):
        cert, cert_sha = read(tail23_root, f"region{region}-action-{sector}.json")
        spec = cert["point_buffer"]
        transfer = manifest["buffers"][spec["file"]]
        raw = base64.b64decode(
            b"".join((tail23_root / p).read_bytes() for p in transfer["parts"]),
            validate=True,
        )
        assert len(raw) == transfer["bytes"] == spec["bytes"]
        assert sha(raw) == transfer["sha256"] == spec["sha256"]
        assert spec["count"] == cert["output_count"] == count
        assert cert["output_first_mode"] == first
        assert F((first + 2 * (count - 1)) ** 2, cert["tail_start"] ** 2) < F("0.258063")
        points.extend(decode(raw, spec))
        errors.append(F(cert["rational"]["complete_l2_error_upper"]))
        certificate_sha.append(cert_sha)

    assert len(points) == FINITE_COUNT
    original_error = upper(sum(e * e for e in errors))
    self2, self3 = SELF_TERM[sector]
    corrected_error = original_error + self2 + self3
    return points, corrected_error, {
        "region1_certificate_sha256": certificate_sha[0],
        "region2_certificate_sha256": certificate_sha[1],
        "region3_certificate_sha256": certificate_sha[2],
        "tail23_manifest_sha256": manifest_sha,
        "uncorrected_disjoint_seed_error_upper": str(original_error),
        "v14_354_region2_self_term_upper": str(self2),
        "v14_354_region3_self_term_upper": str(self3),
        "corrected_finite_seed_error_upper": str(corrected_error),
    }


def load_gap_seed(gap_seed_root, sector):
    start = 1 if sector == "even-v" else 2
    cert_raw = (gap_seed_root / f"gap-action-{sector}.json").read_bytes()
    cert = json.loads(cert_raw)
    assert cert["schema"] == "cone.infinite-seed-gap-action.v1"
    assert cert["sector"] == sector
    assert cert["output_count"] == GAP_COUNT
    assert cert["output_first_mode"] == 1040384 + start
    assert cert["output_last_mode"] == 2080764 + start
    assert cert["self_rows_excluded_with_represented_reciprocal"]
    assert cert["endpoint_ratio_le_quarter"]
    spec = cert["point_buffer"]
    assert spec["sha256"] == GAP_SEED_BUFFER[sector]

    manifest_raw = (gap_seed_root / "manifest.json").read_bytes()
    manifest = json.loads(manifest_raw)
    transfer = manifest["buffers"][spec["file"]]
    raw = base64.b64decode(
        b"".join((gap_seed_root / p).read_bytes() for p in transfer["parts"]),
        validate=True,
    )
    assert len(raw) == transfer["bytes"] == spec["bytes"]
    assert sha(raw) == transfer["sha256"] == spec["sha256"]
    points = decode(raw, spec)
    assert len(points) == GAP_COUNT
    error = F(cert["rational"]["complete_l2_error_upper"])
    assert error < F("1e-12")
    return points, error, sha(cert_raw), sha(manifest_raw)


def run(
    compact_root,
    compact_cert_sha,
    compact_buffer_sha,
    tail1_root,
    tail23_root,
    gap_seed_root,
    source_root,
    lift_root,
    sector,
    out,
):
    start = 1 if sector == "even-v" else 2
    shift = start - 1

    cert = pinned(compact_root / f"gap-extended-compact-action-{sector}.json", compact_cert_sha)
    spec = cert["buffer"]
    assert cert["schema"] == "cone.gap-extended-compact-action.v1"
    assert cert["sector"] == sector
    assert cert["new_gap_lift_certificate_sha256"] == NEW_LIFT[sector]
    assert cert["gap_rhs_certificate_sha256"] == GAP_RHS[sector]
    assert cert["old_patch_candidate_sha256"] == OLD_CAND[sector]
    assert cert["gap_patch_candidate_sha256"] == GAP_CAND[sector]
    assert cert["raw_physical_diagonal_included_once"]
    assert cert["artificial_Hankel_self_removed_once"]
    assert not cert["original_infinite_seed_action_included"]
    assert cert["gap_extended_compact_output_rows_evaluated"]
    assert cert["first_output_mode"] == 256000 + start
    assert cert["last_output_mode"] == 2080764 + start
    assert cert["complete_output_rows"] == COUNT
    assert spec["count"] == COUNT and spec["sha256"] == compact_buffer_sha
    compact = decode((compact_root / spec["file"]).read_bytes(), spec)

    finite_seed, finite_seed_error, finite_meta = load_finite_seed(
        tail1_root, tail23_root, sector
    )
    gap_seed, gap_seed_error, gap_seed_cert_sha, gap_seed_manifest_sha = load_gap_seed(
        gap_seed_root, sector
    )
    seed = finite_seed + gap_seed
    assert len(seed) == len(compact) == COUNT

    first = 256000 + start
    residual = [
        S // (first + 2 * i - shift) - a - b
        for i, (a, b) in enumerate(zip(compact, seed))
    ]

    source = pinned(source_root / f"full-stationary-source-{sector}.json", SOURCE[sector])
    lift = pinned(lift_root / f"gap-correction-finite-lift-{sector}.json", NEW_LIFT[sector])
    assert lift["schema"] == "cone.certified-gap-correction-finite-lift.v1"
    assert lift["finite_lift_certified"]
    assert lift["rhs_certificate_sha256"] == GAP_RHS[sector]

    transport_source = F(source["rational"]["whole_remote_source_transport_upper"])
    transport_lift = F(lift["rational"]["finite_lift_remote_action_charge_upper"])
    transport = transport_source + transport_lift

    compact_error = F(cert["rational"]["complete_gap_extended_compact_action_error_upper"])
    assert compact_error < F("3e-11")
    seed_error = upper(finite_seed_error * finite_seed_error + gap_seed_error * gap_seed_error)
    bare_error = upper(F(COUNT)) / S
    physical_error = compact_error + seed_error + bare_error

    point_lo, point_hi = norm(residual)
    physical_lo = max(F(0), point_lo - physical_error)
    physical_hi = point_hi + physical_error
    schur_lo = max(F(0), physical_lo - transport)
    schur_hi = physical_hi + transport

    allowance = F(0)
    if schur_hi < F("3e-5"):
        q = (F("3e-5") - transport) ** 2 - physical_hi ** 2
        assert q > 0
        allowance = max(F(0), upper(q) - F(1, S))
        assert allowance * allowance <= q

    finite_lo, finite_hi = norm(residual[:FINITE_COUNT])
    gap_lo, gap_hi = norm(residual[FINITE_COUNT:])

    out.mkdir(parents=True, exist_ok=True)
    buffer = write(out, sector, "gap-extended-residual", residual)
    values = {
        "whole_912383_point_norm_lower": point_lo,
        "whole_912383_point_norm_upper": point_hi,
        "finite_block_point_norm_lower": finite_lo,
        "finite_block_point_norm_upper": finite_hi,
        "gap_block_point_norm_lower": gap_lo,
        "gap_block_point_norm_upper": gap_hi,
        "new_compact_action_error_upper": compact_error,
        "corrected_original_seed_finite_error_upper": finite_seed_error,
        "original_seed_gap_error_upper": gap_seed_error,
        "disjoint_original_seed_error_upper": seed_error,
        "bare_source_floor_error_upper": bare_error,
        "complete_912383_physical_error_upper": physical_error,
        "physical_residual_lower": physical_lo,
        "physical_residual_upper": physical_hi,
        "source_transport_upper": transport_source,
        "new_lift_transport_upper": transport_lift,
        "global_source_and_new_lift_transport_once": transport,
        "finite_plus_gap_Schur_residual_lower": schur_lo,
        "finite_plus_gap_Schur_residual_upper": schur_hi,
        "certified_beyond_gap_physical_residual_allowance": allowance,
    }
    return {
        "schema": "cone.gap-extended-residual-composition.v1",
        "sector": sector,
        "new_compact_certificate_sha256": compact_cert_sha,
        "new_compact_buffer_sha256": compact_buffer_sha,
        "source_certificate_sha256": SOURCE[sector],
        "new_lift_certificate_sha256": NEW_LIFT[sector],
        "gap_seed_certificate_sha256": gap_seed_cert_sha,
        "gap_seed_manifest_sha256": gap_seed_manifest_sha,
        "gap_seed_buffer_sha256": GAP_SEED_BUFFER[sector],
        "finite_seed_provenance": finite_meta,
        "buffer": buffer,
        "rational": {k: str(v) for k, v in values.items()},
        "display_approximate": {k: float(v) for k, v in values.items()},
        "source_bare_formula": "1/n" if start == 1 else "1/(n-1)",
        "v14_354_self_term_charged_once_to_inherited_finite_seed_error": True,
        "gap_seed_self_rows_already_excluded": True,
        "global_transport_added_once": True,
        "finite_plus_gap_upper_below_3e_minus5": schur_hi < F("3e-5"),
        "finite_plus_gap_lower_above_3e_minus5": schur_lo > F("3e-5"),
        "beyond_gap_residual_evaluated": False,
        "whole_residual_acceptance_certified": False,
        "stationary_acceptance_met": False,
        "infinite_capacity_tail_closed": False,
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    for name in (
        "compact-root",
        "tail1-root",
        "tail23-root",
        "gap-seed-root",
        "source-root",
        "lift-root",
        "output-root",
    ):
        p.add_argument("--" + name, type=Path, required=True)
    p.add_argument("--compact-certificate-sha256", required=True)
    p.add_argument("--compact-buffer-sha256", required=True)
    p.add_argument("--sector", choices=tuple(SOURCE), required=True)
    a = p.parse_args()
    d = run(
        a.compact_root,
        a.compact_certificate_sha256,
        a.compact_buffer_sha256,
        a.tail1_root,
        a.tail23_root,
        a.gap_seed_root,
        a.source_root,
        a.lift_root,
        a.sector,
        a.output_root,
    )
    path = a.output_root / f"gap-extended-residual-{a.sector}.json"
    path.write_text(json.dumps(d, indent=2, sort_keys=True) + "\n")
    print(json.dumps(d["display_approximate"], sort_keys=True), flush=True)
