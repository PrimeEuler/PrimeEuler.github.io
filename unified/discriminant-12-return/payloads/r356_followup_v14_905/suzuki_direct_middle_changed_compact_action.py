#!/usr/bin/env python3
"""Changed support-aware compact action on the direct-middle block (v14.544).

Five compact components on support [0, 2U), U = 1,040,383:
  front  = original whole source - v14.543 fresh lift   (offset 0)
  near   = refined Near trial                           (offset 128000)
  patch1 = v14.341 wider finite correction              (offset 256000)
  patch2 = v14.399 gap correction                        (offset 520192)
  delta  = v14.500 direct-middle delta                   (offset U)
Output rows U..2U-1 are owned by delta, so the on-support assembly of
suzuki_gap_extended_compact_action applies with owner = delta for every
row: the artificial Hankel self interaction of the delta component is
removed exactly once and the raw physical diagonal is added exactly once.
The v14.354 charge and the global source + v14.403 lift transport charge
were each charged exactly once in v14.442 and are NOT charged again here.
The original infinite seed action is deliberately separate.  No residual
is evaluated.  Modes: prep | shard | stitch | --self-check.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, gc, hashlib, json

import suzuki_gap_extended_compact_action as base
from suzuki_certified_remote_diagonal import evaluate as evaluate_diagonal
from suzuki_certified_remote_z import enclosure, midpoint, radius
from suzuki_compact_component_rectangle import channels, verify as rectangle_verify
from suzuki_compact_action_self_diagonal import verify as self_diagonal_verify
from suzuki_exact_integer_source_action import norm2, sqrt_upper
from suzuki_exact_outward_certificate import read_snapshot
from suzuki_frozen_trial_far_outward import (
    add, atan_recip, constant, enclose, hyperbolic, neg, recip, times,
)
from suzuki_full_stationary_source_transport import PINS, combine
from suzuki_wider_correction_rhs import floor
from suzuki_wider_correction_finite_lift import writebuffer

U = 1_040_383
KBITS = 256
S = 1 << KBITS

LIFT_CERT_SHA256 = {
    "even-v": "d3ea64364f8ca69b569ed9f981828048bd80448d3dc6055934b50e6a278fa263",
    "odd-v": "6c52c4fd7eaa615582375e455588164316254ced57cfb9b4a90d5b82bd5fa95f",
}
LIFT_BUFFER_SHA256 = {
    "even-v": "d3fd00e05bd19709811086ec246764feb36379dc52ec410798d2a01d8e1bf237",
    "odd-v": "a852b54e22ef62d029528c9856f24a5ea6fb9618c99725ccdb052b5a562a739c",
}
DM_RHS_CERT_SHA256 = {
    "even-v": "d56eaf3ade699c5c85ad3ae954c5817c3e58045c6894268b3e49e6a7b2ad55ad",
    "odd-v": "19c67577d032366253625a0f12ed08c217d10c0245fdd03e4bb6ce953cfb2884",
}
DELTA_SHA256 = {
    "even-v": "c5b6845303cb059ca9a1ed79a628c4ba135fd49f2012b5fc011b0aeb14d12bb2",
    "odd-v": "e9efaf914390a6edda7076ad1a1dfa7da5a398246895bc76e00cbb21b682f776",
}
DM_INPUT_Z_SHA256 = {
    "even-v": "0e9e889c915a55267bcf81f9c39d9aed0d768dc857e5bcbf0731f503e6a3ed7f",
    "odd-v": "4ba2d312191080a3d302704ef14e9479a7fab913401c508fb22cfe0dbab87c21",
}

CHARGE_ACCOUNTING_STATEMENT = (
    "Charge accounting: the v14.354 Hankel self-diagonal correction charge "
    "and the global source + v14.403 lift transport charge were each charged "
    "exactly once in ledger v14.442 and are not charged again in this "
    "composition. No term in this certificate's error budget is, contains, "
    "or repeats either charge. The Hankel self-interaction removal and "
    "raw-diagonal insertion applied to the delta component are evaluation "
    "procedures of this compact action under the v14.544 frozen contract, "
    "not repetitions of the v14.354 error charge."
)

SCOPE_FLAGS = {
    "support_aware": True,
    "output_rows_owned_by_delta_component": True,
    "artificial_Hankel_self_removed_once": True,
    "raw_physical_diagonal_included_once": True,
    "full_compact_pole_pairing_included_once": True,
    "original_infinite_seed_action_included": False,
    "direct_middle_residual_evaluated": False,
    "whole_action_evaluated": False,
    "stationary_acceptance_met": False,
    "infinite_capacity_tail_closed": False,
    "v14_354_charge_repeated": False,
    "global_source_v14_403_transport_charge_repeated": False,
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    return sha(Path(path).read_bytes())


def producer_pins():
    import suzuki_compact_component_rectangle as rect_mod
    import suzuki_compact_action_self_diagonal as sd_mod
    import suzuki_wider_correction_rhs as wr_mod
    import suzuki_wider_correction_finite_lift as wl_mod
    return {
        "changed_producer_sha256": file_sha(__file__),
        "base_gap_extended_compact_action_sha256": file_sha(base.__file__),
        "compact_component_rectangle_sha256": file_sha(rect_mod.__file__),
        "compact_action_self_diagonal_sha256": file_sha(sd_mod.__file__),
        "wider_correction_rhs_sha256": file_sha(wr_mod.__file__),
        "wider_correction_finite_lift_sha256": file_sha(wl_mod.__file__),
    }


def shard_range(shard, shards):
    assert 0 <= shard < shards and shards > 0
    q, r = divmod(U, shards)
    count = q + (shard < r)
    first = U + shard * q + min(shard, r)
    assert first >= U and first + count <= 2 * U
    return first, count


def load_components(root, near_root, gap_root, source_root, old_finite_root,
                    candidate_root, lift_root, rhs_root, delta_root, sector):
    stem = f"joint-256000-{sector}.trace-256000.full"
    snapshot = root / (stem + ".zip")
    assert base.sha(snapshot.read_bytes()) == PINS[sector][0]
    _, s, V, _ = read_snapshot(snapshot)
    assert len(s["modes"]) == base.N and s["modes"][0] in (1, 2)
    start = s["modes"][0]

    source = base.load_json(source_root / f"full-stationary-source-{sector}.json",
                            base.SOURCE[sector])
    Z = combine(V, [F(q) for q in source["q_rational"]])
    assert norm2(Z) == F(source["rational"]["represented_full_stationary_vector_norm2"])

    lift_cert = base.load_json(lift_root / f"direct-middle-finite-lift-{sector}.json",
                               LIFT_CERT_SHA256[sector])
    assert lift_cert["schema"] == "cone.certified-direct-middle-delta-finite-lift.v1"
    assert lift_cert["rhs_certificate_sha256"] == DM_RHS_CERT_SHA256[sector]
    assert lift_cert["lift_buffer"]["sha256"] == LIFT_BUFFER_SHA256[sector]
    lift = base.read_buffer(lift_root, lift_cert["lift_buffer"])
    assert len(lift["values"]) == base.N

    near_cert = base.load_json(near_root / f"near-seed-refinement-{sector}.json",
                               base.NEAR[sector])
    near = base.read_buffer(near_root, near_cert["buffers"]["refined-near-trial"])
    old_near_root = near_root.parent / "near_trial_rhs_witness_v14_238"
    old_near = base.load_json(old_near_root / f"new-near-trial-rhs-{sector}.json",
                              base.OLD_NEAR_RHS[sector])
    znear = base.read_buffer(old_near_root, old_near["buffers"]["action-z-near"])

    old_finite = base.load_json(
        old_finite_root / f"wide-compact-near-middle-window-{sector}.json",
        base.OLD_FINITE[sector])
    assert old_finite["candidate_sha256"] == base.OLD_CAND[sector]
    zold = base.read_buffer(old_finite_root, old_finite["patch_input_z_buffer"])
    old_patch = base.read_raw_candidate(
        candidate_root / f"{sector}-wider-correction.bin", base.OLD_CAND[sector],
        base.OLD_COUNT)

    gap_rhs = base.load_json(gap_root / f"gap-correction-RHS-{sector}.json",
                             base.GAP_RHS[sector])
    assert gap_rhs["candidate_point_sha256"] == base.GAP_CAND[sector]
    assert gap_rhs["candidate_count"] == base.GAP_COUNT
    assert gap_rhs["candidate_first_mode"] == 2 * base.GAP_OFFSET + start
    assert gap_rhs["candidate_last_mode"] == 2 * (base.GAP_OFFSET + base.GAP_COUNT - 1) + start
    zgap = base.read_buffer(gap_root, gap_rhs["buffers"]["correction-input-z"])
    gap_patch = base.read_raw_candidate(
        candidate_root / f"{sector}-gap-correction.bin", base.GAP_CAND[sector],
        base.GAP_COUNT, width=17)

    dm_rhs = base.load_json(rhs_root / f"direct-middle-complete-RHS-{sector}.json",
                            DM_RHS_CERT_SHA256[sector])
    assert dm_rhs["schema"] == "cone.direct-middle-delta-complete-finite-rhs.v1"
    assert dm_rhs["snapshot_sha256"] == PINS[sector][0]
    assert dm_rhs["candidate_point_sha256"] == DELTA_SHA256[sector]
    zspec = dm_rhs["buffers"]["correction-input-z"]
    assert zspec["sha256"] == DM_INPUT_Z_SHA256[sector]
    assert zspec["count"] == U and zspec["bits"] == 160
    zdelta = base.read_buffer(rhs_root, zspec)

    delta_cert_raw = (delta_root / f"dm-correction-{sector}.json").read_bytes()
    delta_cert = json.loads(delta_cert_raw)
    assert delta_cert["schema"] == "cone.sandbox-dm-correction-candidate.v1"
    dspec = delta_cert["buffer"]
    assert dspec["sha256"] == DELTA_SHA256[sector]
    assert dspec["count"] == U and dspec["bits"] == 160
    delta = base.read_buffer(delta_root, dspec)

    front_bits = max(Z["bits"], lift["bits"])
    front = {"bits": front_bits, "values": [
        (a << (front_bits - Z["bits"])) - (b << (front_bits - lift["bits"]))
        for a, b in zip(Z["values"], lift["values"])
    ]}
    components = [
        {"name": "front", "offset": 0, "x": front,
         "z": {"bits": s["z"]["bits"], "values": s["z"]["values"]}},
        {"name": "near", "offset": base.N, "x": near, "z": znear},
        {"name": "patch1", "offset": base.OLD_OFFSET, "x": old_patch, "z": zold},
        {"name": "patch2", "offset": base.GAP_OFFSET, "x": gap_patch, "z": zgap},
        {"name": "delta", "offset": U, "x": delta, "z": zdelta},
    ]
    assert [(c["offset"], len(c["x"]["values"])) for c in components] == [
        (0, base.N), (base.N, base.N), (base.OLD_OFFSET, base.OLD_COUNT),
        (base.GAP_OFFSET, base.GAP_COUNT), (U, U)
    ]
    assert all(len(c["x"]["values"]) == len(c["z"]["values"]) for c in components)

    pins = {
        "snapshot_sha256": PINS[sector][0],
        "full_source_certificate_sha256": base.SOURCE[sector],
        "fresh_lift_certificate_sha256": LIFT_CERT_SHA256[sector],
        "fresh_lift_buffer_sha256": LIFT_BUFFER_SHA256[sector],
        "near_trial_certificate_sha256": base.NEAR[sector],
        "near_trial_buffer_sha256": near_cert["buffers"]["refined-near-trial"]["sha256"],
        "near_rhs_witness_certificate_sha256": base.OLD_NEAR_RHS[sector],
        "near_action_z_sha256": old_near["buffers"]["action-z-near"]["sha256"],
        "old_finite_compact_certificate_sha256": base.OLD_FINITE[sector],
        "old_patch_candidate_sha256": base.OLD_CAND[sector],
        "old_patch_input_z_sha256": old_finite["patch_input_z_buffer"]["sha256"],
        "gap_rhs_certificate_sha256": base.GAP_RHS[sector],
        "gap_patch_candidate_sha256": base.GAP_CAND[sector],
        "gap_correction_input_z_sha256": gap_rhs["buffers"]["correction-input-z"]["sha256"],
        "direct_middle_rhs_certificate_sha256": DM_RHS_CERT_SHA256[sector],
        "delta_candidate_buffer_sha256": DELTA_SHA256[sector],
        "delta_correction_input_z_sha256": DM_INPUT_Z_SHA256[sector],
    }
    return s, start, components, pins


def component_table(components):
    return [[c["name"], c["offset"], len(c["x"]["values"]),
             c["x"]["bits"], c["z"]["bits"]] for c in components]


def lt_points(start):
    pi = enclose(add(times(constant(16), atan_recip(5)),
                     neg(times(constant(4), atan_recip(239)))))
    li = enclosure(*times(times(constant(4), enclose(hyperbolic(start == 2))),
                          recip(pi)), 256)
    ti = enclosure(*times(recip(pi), recip(pi)), 256)
    Lpoint, tpoint = midpoint(li, 256), midpoint(ti, 256)
    assert radius(li, Lpoint) < F(2, S) and radius(ti, tpoint) < F(2, S)
    return Lpoint, tpoint


def prep(roots, sector, work_root):
    s, start, components, pins = load_components(*roots, sector)
    Lpoint, tpoint = lt_points(start)
    pbits = s["pole"]["bits"]
    front = components[0]
    P = F(sum(a * b for a, b in zip(s["pole"]["values"], front["x"]["values"])),
          1 << (pbits + front["x"]["bits"]))
    for cpt in components[1:]:
        xb = cpt["x"]["bits"]
        for j, xv in enumerate(cpt["x"]["values"]):
            mode = 2 * (cpt["offset"] + j) + start
            pv = floor(Lpoint * mode / (mode * mode + tpoint), 256)
            P += F(pv * xv, 1 << (256 + xb))
    l1 = sum(F(sum(abs(v) for v in c["x"]["values"]), 1 << c["x"]["bits"])
             for c in components)
    xnorm2 = sum(norm2(c["x"]) for c in components)
    d = {
        "schema": "cone.direct-middle-changed-compact-action-prep.v1",
        "sector": sector,
        "pole_pairing_P": str(P),
        "compact_l1": str(l1),
        "represented_compact_norm2": str(xnorm2),
        "Lpoint": str(Lpoint),
        "tpoint": str(tpoint),
        "component_offsets_counts": component_table(components),
        "input_pins": pins,
        "producer_pins": producer_pins(),
    }
    work_root.mkdir(parents=True, exist_ok=True)
    path = work_root / f"prep-{sector}.json"
    path.write_text(json.dumps(d, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"sector": sector, "prep": str(path),
                      "P_digits": len(str(P.numerator)),
                      "l1_approx": float(l1)}, sort_keys=True), flush=True)
    return d


def run_shard(roots, sector, output_root, work_root, shard, shards):
    first, count = shard_range(shard, shards)
    prep_path = work_root / f"prep-{sector}.json"
    prep_raw = prep_path.read_bytes()
    prep_d = json.loads(prep_raw)
    assert prep_d["sector"] == sector
    s, start, components, pins = load_components(*roots, sector)
    assert pins == prep_d["input_pins"]
    assert component_table(components) == prep_d["component_offsets_counts"]
    P, l1 = F(prep_d["pole_pairing_P"]), F(prep_d["compact_l1"])
    Lpoint, tpoint = F(prep_d["Lpoint"]), F(prep_d["tpoint"])

    delta = components[4]
    dx, dz = delta["x"]["values"], delta["z"]["values"]
    dxb, dzb = delta["x"]["bits"], delta["z"]["bits"]
    zout = dz[first - U: first - U + count]
    assert len(zout) == count
    zout_bits = dzb

    cbits, cv = s["c"]["bits"], s["c"]["values"][0]
    assert abs(F(cv, 1 << cbits)) < 1
    max_xz = max(c["x"]["bits"] + max(c["z"]["bits"], zout_bits) for c in components)
    mix_bits = cbits + 1 + KBITS + max_xz
    mixed = [0] * count
    direct_checks = []
    sample_r = sorted(set((0, count // 2, count - 1)))
    for cpt in components:
        x, z = cpt["x"]["values"], cpt["z"]["values"]
        xb, zb = cpt["x"]["bits"], cpt["z"]["bits"]
        zx = [a * b for a, b in zip(x, z)]
        print(sector, "shard", shard, cpt["name"], "channels begin", flush=True)
        u, v = channels(x, zx, start, cpt["offset"], first, count, KBITS)
        print(sector, "shard", shard, cpt["name"], "channels complete", flush=True)
        sv = mix_bits - (cbits + 1 + zout_bits + xb + KBITS)
        su = mix_bits - (cbits + 1 + zb + xb + KBITS)
        assert sv >= 0 and su >= 0
        for r in range(count):
            mixed[r] += (cv * zout[r] * v[r]) << sv
            mixed[r] -= (cv * u[r]) << su
        for r in sample_r:
            i = first + r
            du, dv = base.direct_channel_row(cpt, start, i)
            assert du == u[r] and dv == v[r]
            direct_checks.append({
                "component": cpt["name"],
                "output_index": i,
                "physical_mode": 2 * i + start,
                "output_relative_to_component_support":
                    "inside" if cpt["offset"] <= i < cpt["offset"] + len(x) else "outside",
                "direct_channel_match": True,
            })
        del zx, u, v
        gc.collect()

    # Owner compensation: remove the artificial Hankel self interaction of
    # the delta component exactly once (z_out == z_in == dz[j] on owner rows,
    # so this is compensate_self at integer scale, as in the base producer).
    shift_self = mix_bits - (cbits + dzb + KBITS + dxb)
    assert shift_self >= 0
    for r in range(count):
        i = first + r
        j = i - U
        recip_self = S // (2 * (2 * i + start))
        mixed[r] += (cv * dz[j] * recip_self * dx[j]) << shift_self

    alpha = s["alpha"]
    output = []
    diagonal_error2 = F(0)
    for r in range(count):
        i = first + r
        mode = 2 * i + start
        point = F(mixed[r], 1 << mix_bits)
        prow = F(floor(Lpoint * mode / (mode * mode + tpoint), 256), S)
        point += alpha * prow * P
        diagonal = evaluate_diagonal(mode)
        dlo, dhi = F(diagonal["lower_rational"]), F(diagonal["upper_rational"])
        dp = (dlo + dhi) / 2
        j = i - U
        xi = F(dx[j], 1 << dxb)
        point += dp * xi
        diagonal_error2 += (max(dp - dlo, dhi - dp) * abs(xi)) ** 2
        output.append(floor(point, KBITS))
        if (r + 1) % 16000 == 0:
            print(sector, "shard", shard, "changed compact rows",
                  r + 1, "/", count, flush=True)

    rowsqrt = sqrt_upper(F(count), 256)
    diagonal_error = sqrt_upper(diagonal_error2, 256)
    parameter_error = F("1e-34") * l1 * rowsqrt
    reciprocal_rounding = F(40, S) * l1 * rowsqrt
    output_rounding = rowsqrt * F(1, S)
    physical_error = (diagonal_error + parameter_error +
                      reciprocal_rounding + output_rounding)
    assert physical_error < F("3e-11")

    output_root.mkdir(parents=True, exist_ok=True)
    buffer = writebuffer(output_root, f"{sector}-shard-{shard}-of-{shards}",
                         "direct-middle-changed-compact-action", output, KBITS)
    values = {
        "diagonal_interval_action_charge_upper": diagonal_error,
        "offdiagonal_and_pole_parameter_charge_upper": parameter_error,
        "reciprocal_kernel_rounding_charge_upper": reciprocal_rounding,
        "final_row_rounding_charge_upper": output_rounding,
        "complete_changed_direct_middle_compact_action_error_upper": physical_error,
    }
    d = {
        "schema": "cone.direct-middle-changed-compact-action-shard.v1",
        "sector": sector, "shard": shard, "shards": shards,
        "first_output_index": first, "last_output_index": first + count - 1,
        "first_output_mode": 2 * first + start,
        "last_output_mode": 2 * (first + count - 1) + start,
        "complete_output_rows": count, "buffer": buffer,
        "rational": {k: str(v) for k, v in values.items()},
        "display_approximate": {k: float(v) for k, v in values.items()},
        "direct_component_rows": direct_checks,
        "component_offsets_counts": component_table(components),
        "input_pins": pins,
        "prep_artifact_sha256": sha(prep_raw),
        "charge_accounting_statement": CHARGE_ACCOUNTING_STATEMENT,
        **SCOPE_FLAGS,
    }
    path = output_root / f"direct-middle-changed-compact-action-{sector}-shard-{shard}-of-{shards}.json"
    path.write_text(json.dumps(d, indent=2, sort_keys=True) + "\n")
    print(json.dumps(d["display_approximate"], sort_keys=True), flush=True)
    return d


def stitch(sector, output_root, work_root, shards):
    prep_d = json.loads((work_root / f"prep-{sector}.json").read_text())
    certs, raws = [], []
    for shard in range(shards):
        cpath = output_root / f"direct-middle-changed-compact-action-{sector}-shard-{shard}-of-{shards}.json"
        craw = cpath.read_bytes()
        cert = json.loads(craw)
        assert cert["schema"] == "cone.direct-middle-changed-compact-action-shard.v1"
        assert (cert["sector"], cert["shard"], cert["shards"]) == (sector, shard, shards)
        spec = cert["buffer"]
        braw = (output_root / spec["file"]).read_bytes()
        assert len(braw) == spec["bytes"] and sha(braw) == spec["sha256"]
        assert spec["count"] == cert["complete_output_rows"]
        for k, v in SCOPE_FLAGS.items():
            assert cert[k] is v, (k, shard)
        assert cert["charge_accounting_statement"] == CHARGE_ACCOUNTING_STATEMENT
        assert cert["input_pins"] == prep_d["input_pins"]
        certs.append((cert, craw))
        raws.append(braw)
    firsts = [c["first_output_index"] for c, _ in certs]
    lasts = [c["last_output_index"] for c, _ in certs]
    assert firsts[0] == U and lasts[-1] == 2 * U - 1
    seams = sum(1 for a, b in zip(lasts, firsts[1:]) if a + 1 == b)
    assert seams == shards - 1
    assert sum(c["complete_output_rows"] for c, _ in certs) == U
    widths = {c["buffer"]["width"] for c, _ in certs}
    assert len(widths) == 1, widths
    width = widths.pop()
    stitched = b"".join(raws)
    assert len(stitched) == U * width
    stitched_name = f"{sector}-direct-middle-changed-compact-action.bin"
    (output_root / stitched_name).write_bytes(stitched)
    buffer = {"file": stitched_name, "bits": KBITS, "width": width,
              "count": U, "bytes": len(stitched), "sha256": sha(stitched)}

    keys = ["diagonal_interval_action_charge_upper",
            "offdiagonal_and_pole_parameter_charge_upper",
            "reciprocal_kernel_rounding_charge_upper",
            "final_row_rounding_charge_upper"]
    terms = {}
    for k in keys:
        terms[k] = sqrt_upper(sum(F(c["rational"][k]) ** 2 for c, _ in certs), 256)
    complete = sum(terms.values())
    assert complete < F("3e-11")
    values = {**terms,
              "complete_changed_direct_middle_compact_action_error_upper": complete}
    d = {
        "schema": "cone.direct-middle-changed-compact-action.v1",
        "sector": sector,
        "definition": (
            "changed compact component = (Z_full - v14.543 fresh lift) + "
            "refined Near + v14.341 patch + v14.399 gap patch + v14.500 "
            "direct-middle delta; original infinite seed action separate"
        ),
        "U": U,
        "first_output_index": U, "last_output_index": 2 * U - 1,
        "first_output_mode": certs[0][0]["first_output_mode"],
        "last_output_mode": certs[-1][0]["last_output_mode"],
        "complete_output_rows": U,
        "shards": shards,
        "shard_coverage": [
            {"shard": c["shard"], "first_output_index": c["first_output_index"],
             "last_output_index": c["last_output_index"],
             "rows": c["complete_output_rows"],
             "certificate_sha256": sha(craw), "buffer": c["buffer"]}
            for c, craw in certs
        ],
        "complete_contiguous_coverage": True,
        "seams_checked": seams,
        "buffer": buffer,
        "rational": {k: str(v) for k, v in values.items()},
        "display_approximate": {k: float(v) for k, v in values.items()},
        "represented_compact_norm_upper": str(
            sqrt_upper(F(prep_d["represented_compact_norm2"]), 256)),
        "represented_compact_l1": prep_d["compact_l1"],
        "component_offsets_counts": prep_d["component_offsets_counts"],
        "input_pins": prep_d["input_pins"],
        "producer_pins": prep_d["producer_pins"],
        "self_checks": {
            "component_rectangle_rows_verified": rectangle_verify(),
            "mixed_scale_split_rows_verified": base.small_split_checks(),
            "self_diagonal_rows_verified": self_diagonal_verify(),
        },
        "charge_accounting_statement": CHARGE_ACCOUNTING_STATEMENT,
        "changed_direct_middle_compact_output_rows_evaluated": True,
        **SCOPE_FLAGS,
    }
    path = output_root / f"direct-middle-changed-compact-action-{sector}.json"
    path.write_text(json.dumps(d, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"sector": sector, "buffer_sha256": buffer["sha256"],
                      "width": width, "complete_error_upper": float(complete)},
                     sort_keys=True), flush=True)
    return d


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--self-check", action="store_true")
    p.add_argument("--mode", choices=("prep", "shard", "stitch"))
    for name in ("root", "near-root", "gap-root", "source-root", "old-finite-root",
                 "candidate-root", "lift-root", "rhs-root", "delta-root",
                 "output-root", "work-root"):
        p.add_argument("--" + name, type=Path)
    p.add_argument("--sector", choices=tuple(base.SOURCE))
    p.add_argument("--shard", type=int)
    p.add_argument("--shards", type=int, default=4)
    a = p.parse_args()
    if a.self_check:
        print(json.dumps({
            "component_rectangle_rows_verified": rectangle_verify(),
            "mixed_scale_split_rows_verified": base.small_split_checks(),
            "self_diagonal_rows_verified": self_diagonal_verify(),
        }, sort_keys=True))
    else:
        roots = (a.root, a.near_root, a.gap_root, a.source_root,
                 a.old_finite_root, a.candidate_root, a.lift_root,
                 a.rhs_root, a.delta_root)
        if a.mode == "prep":
            assert all(v is not None for v in roots) and a.sector and a.work_root
            prep(roots, a.sector, a.work_root)
        elif a.mode == "shard":
            assert all(v is not None for v in roots) and a.sector
            assert a.output_root and a.work_root and a.shard is not None
            run_shard(roots, a.sector, a.output_root, a.work_root,
                      a.shard, a.shards)
        elif a.mode == "stitch":
            assert a.sector and a.output_root and a.work_root
            stitch(a.sector, a.output_root, a.work_root, a.shards)
        else:
            raise SystemExit("--mode required")
