#!/usr/bin/env python3
"""Shardable off-support compact action on the v14.447 direct-middle block."""
from pathlib import Path
from fractions import Fraction as F
import argparse, gc, hashlib, json

import suzuki_gap_extended_compact_action as base
from suzuki_certified_remote_z import evaluate as evaluate_remote_z
from suzuki_compact_component_rectangle import channels
from suzuki_exact_integer_source_action import norm2, sqrt_upper
from suzuki_exact_outward_certificate import read_snapshot
from suzuki_frozen_trial_far_outward import add, atan_recip, constant, enclose, hyperbolic, neg, recip, times
from suzuki_full_stationary_source_transport import PINS, combine
from suzuki_wider_correction_rhs import floor
from suzuki_wider_correction_finite_lift import writebuffer

U = 1_040_383
KBITS = 256
S = 1 << KBITS


def shard_range(shard, shards):
    assert 0 <= shard < shards and shards > 0
    q, r = divmod(U, shards)
    count = q + (shard < r)
    first = U + shard * q + min(shard, r)
    assert first >= U and first + count <= 2 * U
    return first, count


def load_components(root, near_root, gap_root, source_root, old_finite_root, candidate_root, sector):
    stem = f"joint-256000-{sector}.trace-256000.full"
    snapshot = root / (stem + ".zip")
    assert base.sha(snapshot.read_bytes()) == PINS[sector][0]
    _, s, V, _ = read_snapshot(snapshot)
    start = s["modes"][0]
    source = base.load_json(source_root / f"full-stationary-source-{sector}.json", base.SOURCE[sector])
    Z = combine(V, [F(q) for q in source["q_rational"]])
    assert norm2(Z) == F(source["rational"]["represented_full_stationary_vector_norm2"])
    lift_cert = base.load_json(gap_root / f"gap-correction-finite-lift-{sector}.json", base.GAP_LIFT[sector])
    lift = base.read_buffer(gap_root, lift_cert["lift_buffer"])
    near_cert = base.load_json(near_root / f"near-seed-refinement-{sector}.json", base.NEAR[sector])
    near = base.read_buffer(near_root, near_cert["buffers"]["refined-near-trial"])
    old_near_root = near_root.parent / "near_trial_rhs_witness_v14_238"
    old_near = base.load_json(old_near_root / f"new-near-trial-rhs-{sector}.json", base.OLD_NEAR_RHS[sector])
    znear = base.read_buffer(old_near_root, old_near["buffers"]["action-z-near"])
    old_finite = base.load_json(old_finite_root / f"wide-compact-near-middle-window-{sector}.json", base.OLD_FINITE[sector])
    zold = base.read_buffer(old_finite_root, old_finite["patch_input_z_buffer"])
    old_patch = base.read_raw_candidate(candidate_root / f"{sector}-wider-correction.bin", base.OLD_CAND[sector], base.OLD_COUNT)
    gap_rhs = base.load_json(gap_root / f"gap-correction-RHS-{sector}.json", base.GAP_RHS[sector])
    zgap = base.read_buffer(gap_root, gap_rhs["buffers"]["correction-input-z"])
    gap_patch = base.read_raw_candidate(candidate_root / f"{sector}-gap-correction.bin", base.GAP_CAND[sector], base.GAP_COUNT, width=17)
    front_bits = max(Z["bits"], lift["bits"])
    front = {"bits": front_bits, "values": [
        (a << (front_bits - Z["bits"])) - (b << (front_bits - lift["bits"]))
        for a, b in zip(Z["values"], lift["values"])
    ]}
    components = [
        {"name": "front", "offset": 0, "x": front, "z": {"bits": s["z"]["bits"], "values": s["z"]["values"]}},
        {"name": "near", "offset": base.N, "x": near, "z": znear},
        {"name": "patch1", "offset": base.OLD_OFFSET, "x": old_patch, "z": zold},
        {"name": "patch2", "offset": base.GAP_OFFSET, "x": gap_patch, "z": zgap},
    ]
    assert sum(len(c["x"]["values"]) for c in components) == U
    assert max(c["offset"] + len(c["x"]["values"]) - 1 for c in components) == U - 1
    return s, start, components, lift_cert


def run(root, near_root, gap_root, source_root, old_finite_root, candidate_root,
        sector, output_root, shard, shards):
    first, count = shard_range(shard, shards)
    s, start, components, lift_cert = load_components(
        root, near_root, gap_root, source_root, old_finite_root, candidate_root, sector
    )
    assert first > max(c["offset"] + len(c["x"]["values"]) - 1 for c in components)
    modes = [2 * i + start for i in range(first, first + count)]
    zout, zradii = [], []
    for r, mode in enumerate(modes):
        z = evaluate_remote_z(mode, output_bits=KBITS, action_precision=True)
        lo, hi = F(z["lower_rational"]), F(z["upper_rational"])
        point = floor((lo + hi) / 2, KBITS)
        zout.append(point)
        zradii.append(max(F(point, S) - lo, hi - F(point, S)))
        if (r + 1) % 16000 == 0:
            print(sector, shard, "certified output-z rows", r + 1, "/", count, flush=True)

    cbits, cv = s["c"]["bits"], s["c"]["values"][0]
    cpoint = F(cv, 1 << cbits)
    max_xz = max(c["x"]["bits"] + max(c["z"]["bits"], KBITS) for c in components)
    mix_bits = cbits + 1 + KBITS + max_xz
    vbits = max(c["x"]["bits"] + KBITS for c in components)
    mixed = [0] * count
    vtotal = [0] * count
    direct_checks = []
    sample_r = sorted(set((0, count // 2, count - 1)))
    for cpt in components:
        x, z = cpt["x"]["values"], cpt["z"]["values"]
        xb, zb = cpt["x"]["bits"], cpt["z"]["bits"]
        u, v = channels(x, [a * b for a, b in zip(x, z)], start, cpt["offset"], first, count, KBITS)
        sv = mix_bits - (cbits + 1 + KBITS + xb + KBITS)
        su = mix_bits - (cbits + 1 + zb + xb + KBITS)
        vv = vbits - (xb + KBITS)
        assert min(sv, su, vv) >= 0
        for r in range(count):
            mixed[r] += (cv * zout[r] * v[r]) << sv
            mixed[r] -= (cv * u[r]) << su
            vtotal[r] += v[r] << vv
        for r in sample_r:
            i = first + r
            du, dv = base.direct_channel_row(cpt, start, i)
            assert du == u[r] and dv == v[r]
            direct_checks.append({"component": cpt["name"], "output_index": i,
                                  "physical_mode": 2 * i + start,
                                  "output_outside_component_support": True,
                                  "direct_channel_match": True})
        del u, v
        gc.collect()

    pi = enclose(add(times(constant(16), atan_recip(5)), neg(times(constant(4), atan_recip(239)))))
    li = base.enclosure(*times(times(constant(4), enclose(hyperbolic(start == 2))), recip(pi)), 256)
    ti = base.enclosure(*times(recip(pi), recip(pi)), 256)
    Lpoint, tpoint = base.midpoint(li, 256), base.midpoint(ti, 256)
    pbits = s["pole"]["bits"]
    P = F(sum(a * b for a, b in zip(s["pole"]["values"], components[0]["x"]["values"])),
          1 << (pbits + components[0]["x"]["bits"]))
    for cpt in components[1:]:
        for j, xv in enumerate(cpt["x"]["values"]):
            mode = 2 * (cpt["offset"] + j) + start
            pv = floor(Lpoint * mode / (mode * mode + tpoint), 256)
            P += F(pv * xv, 1 << (256 + cpt["x"]["bits"]))
    alpha = s["alpha"]
    output = []
    z_error2 = F(0)
    for r, mode in enumerate(modes):
        point = F(mixed[r], 1 << mix_bits)
        prow = F(floor(Lpoint * mode / (mode * mode + tpoint), 256), S)
        point += alpha * prow * P
        output.append(floor(point, KBITS))
        vrow = F(vtotal[r], 1 << vbits)
        z_error2 += (abs(cpoint) * zradii[r] * abs(vrow) / 2) ** 2

    l1 = sum(F(sum(abs(v) for v in c["x"]["values"]), 1 << c["x"]["bits"]) for c in components)
    rowsqrt = sqrt_upper(F(count), 256)
    z_error = sqrt_upper(z_error2, 256)
    parameter_error = F("1e-34") * l1 * rowsqrt
    reciprocal_rounding = F(40, S) * l1 * rowsqrt
    output_rounding = rowsqrt * F(1, S)
    physical_error = z_error + parameter_error + reciprocal_rounding + output_rounding
    assert physical_error < F("3e-11")
    output_root.mkdir(parents=True, exist_ok=True)
    buffer = writebuffer(output_root, f"{sector}-shard-{shard}-of-{shards}", "direct-middle-compact-action", output, KBITS)
    values = {"output_z_interval_action_charge_upper": z_error,
              "offdiagonal_and_pole_parameter_charge_upper": parameter_error,
              "reciprocal_kernel_rounding_charge_upper": reciprocal_rounding,
              "final_row_rounding_charge_upper": output_rounding,
              "complete_direct_middle_compact_action_error_upper": physical_error}
    return {"schema": "cone.direct-middle-off-support-compact-action-shard.v1",
            "sector": sector, "shard": shard, "shards": shards,
            "first_output_index": first, "last_output_index": first + count - 1,
            "first_output_mode": modes[0], "last_output_mode": modes[-1],
            "complete_output_rows": count, "buffer": buffer,
            "rational": {k: str(v) for k, v in values.items()},
            "display_approximate": {k: float(v) for k, v in values.items()},
            "direct_component_rows": direct_checks,
            "new_physical_output_z_evaluated_for_every_row": True,
            "compact_input_output_support_disjoint": True,
            "artificial_Hankel_self_compensation_applied": False,
            "raw_physical_diagonal_applied": False,
            "full_compact_pole_pairing_included_once": True,
            "original_infinite_seed_action_included": False,
            "direct_middle_residual_evaluated": False,
            "whole_action_evaluated": False,
            "infinite_capacity_tail_closed": False,
            "input_pins": {"snapshot_sha256": PINS[sector][0],
                           "new_gap_lift_certificate_sha256": base.GAP_LIFT[sector],
                           "new_gap_lift_buffer_sha256": lift_cert["lift_buffer"]["sha256"]}}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    for name in ("root", "near-root", "gap-root", "source-root", "old-finite-root", "candidate-root", "output-root"):
        p.add_argument("--" + name, type=Path)
    p.add_argument("--sector", choices=tuple(base.SOURCE))
    p.add_argument("--shard", type=int, required=True)
    p.add_argument("--shards", type=int, default=4)
    a = p.parse_args()
    assert all(getattr(a, n.replace("-", "_")) is not None for n in
               ("root", "near-root", "gap-root", "source-root", "old-finite-root", "candidate-root", "output-root", "sector"))
    d = run(a.root, a.near_root, a.gap_root, a.source_root, a.old_finite_root,
            a.candidate_root, a.sector, a.output_root, a.shard, a.shards)
    path = a.output_root / f"direct-middle-compact-action-{a.sector}-shard-{a.shard}-of-{a.shards}.json"
    path.write_text(json.dumps(d, indent=2, sort_keys=True) + "\n")
    print(json.dumps(d["display_approximate"], sort_keys=True), flush=True)
