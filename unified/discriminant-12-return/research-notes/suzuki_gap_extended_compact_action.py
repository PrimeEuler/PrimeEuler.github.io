#!/usr/bin/env python3
"""Support-aware compact action for the v14.403 gap-refined trial.

The compact vector is assembled from four disjoint components while each keeps
its native dyadic scale:
  Front = original whole source - v14.403 fresh lift,
  Near = refined Near trial,
  Patch-1 = v14.341 wider finite correction,
  Patch-2 = v14.399 gap correction.
The unchanged original infinite seed action is deliberately separate.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, gc, hashlib, json

from suzuki_certified_remote_diagonal import evaluate as evaluate_diagonal
from suzuki_certified_remote_z import enclosure, midpoint, radius
from suzuki_compact_component_rectangle import channels, verify as rectangle_verify
from suzuki_exact_integer_source_action import norm2, sqrt_upper
from suzuki_exact_outward_certificate import read_snapshot
from suzuki_frozen_trial_far_outward import (
    add, atan_recip, constant, enclose, hyperbolic, neg, recip, times,
)
from suzuki_full_stationary_source_transport import PINS, combine
from suzuki_wider_correction_rhs import floor
from suzuki_wider_correction_finite_lift import writebuffer

N = 128000
OLD_OFFSET = 2 * N
OLD_COUNT = 264192
GAP_OFFSET = OLD_OFFSET + OLD_COUNT
GAP_COUNT = 520191
FIRST = N
COUNT = GAP_OFFSET + GAP_COUNT - FIRST
KBITS = 256
S = 1 << KBITS

SOURCE = {
    "even-v": "40fcbd9ba5745598fa0e8d98a5da43b7c088411c8fdcb4c6d0dcae10a0b9dc80",
    "odd-v": "41fdeb3af0ab1d00bc154cc7111b62d28d5e75365de795ce4a970f779e25138f",
}
NEAR = {
    "even-v": "cca920b7b5f20fd856807166fdc08cce82f4b108f61831c34f19da29e366f42b",
    "odd-v": "85a45f5fa1e5bedc8100c69a3fd4c31324c10aa30bc635a1e61d9a24ac93c6ba",
}
OLD_FINITE = {
    "even-v": "91ac66062b89bedcd3d04c09bd04330c2a6285167f119bca33231370a7473e18",
    "odd-v": "8c8394d88d20c1bfa8848c0a3b3291d982a3bd5b6732f4b53d696cac0e78da73",
}
OLD_CAND = {
    "even-v": "fdf93112802fe28ef53efa804be760a0fc17abc404993c8b2af6c33b1b5aba05",
    "odd-v": "b772ab850121daf0bd85afd01e26fee9f72d14b940c4145ae7643734435f8967",
}
GAP_RHS = {
    "even-v": "42c71d7e017eadc08a6ebe20045f6d6e83bbe3523e17ba282903eccf08edc075",
    "odd-v": "1309bec0a4568684f3631a2d88a278ba711c8496960491e5a81428a8fb5b30b3",
}
GAP_LIFT = {
    "even-v": "4d49b475c4a6b97de137258d7b53415b914aec8fa1a0fb52f8b6400ba214bfb3",
    "odd-v": "f2f2a9e3c018902198a8a9b7df5e91bba42a81de4bd1334cffaa1e2fb0cf0daf",
}
GAP_CAND = {
    "even-v": "171883d6c8e41e9a92f88bea4fa96b70f538ada49ea296876e1f06aebe1f9da6",
    "odd-v": "f3a9b9a06efb728ee8ed51b4294fbd406d0b9bad8248831d03b3c4586f846a66",
}
OLD_NEAR_RHS = {
    "even-v": "7183ea82d33db24ece4cbb4c73e7ff84a001fe1783c565dc90dcd7fac498af45",
    "odd-v": "3865461f0f672a0b04a9511cc49527f28316fc5c5ed551fb10b813cd9c3f2480",
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load_json(path, pin):
    raw = path.read_bytes()
    assert sha(raw) == pin, (path, sha(raw), pin)
    return json.loads(raw)


def read_buffer(root, spec):
    raw = (root / spec["file"]).read_bytes()
    assert len(raw) == spec["bytes"] and sha(raw) == spec["sha256"]
    width = spec["width"]
    values = [
        int.from_bytes(raw[j:j + width], "little", signed=True)
        for j in range(0, len(raw), width)
    ]
    assert len(values) == spec["count"]
    return {"bits": spec["bits"], "values": values}


def read_raw_candidate(path, pin, count, width=18, bits=160):
    raw = path.read_bytes()
    assert len(raw) == count * width and sha(raw) == pin
    values = [
        int.from_bytes(raw[j:j + width], "little", signed=True)
        for j in range(0, len(raw), width)
    ]
    assert len(values) == count
    return {"bits": bits, "values": values}


def direct_channel_row(component, start, i):
    """Direct integer recomputation of one rounded rectangular row."""
    x = component["x"]["values"]
    z = component["z"]["values"]
    offset = component["offset"]
    du = 0
    dv = 0
    for j, (xj, zj) in enumerate(zip(x, z)):
        q = offset + j
        t = 0 if i == q else S // (2 * (i - q))
        h = S // (2 * (i + q + start))
        du += (t + h) * zj * xj
        dv += (t - h) * xj
    return du, dv


def small_split_checks():
    """Verify native-scale component splitting against the original kernel."""
    checked = 0
    c = F(2, 3)
    for start in (1, 2):
        specs = [
            (0, 7, 5, [3, -2, 5], [2, -1, 4]),
            (3, 11, 9, [-4, 6], [7, -3]),
        ]
        for first in (0, 2, 4):
            count = 5
            pieces = []
            for offset, xb, zb, x, z in specs:
                u, v = channels(x, [a * b for a, b in zip(x, z)], start, offset, first, count, KBITS)
                pieces.append((offset, xb, zb, x, z, u, v))
            for r, i in enumerate(range(first, first + count)):
                zo = F(i + 5, 13)
                point = F(0)
                direct = F(0)
                n = 2 * i + start
                for offset, xb, zb, x, z, u, v in pieces:
                    piece = c * (zo * F(v[r], 1 << (xb + KBITS))
                                 - F(u[r], 1 << (zb + xb + KBITS))) / 2
                    if offset <= i < offset + len(x):
                        j = i - offset
                        piece += c * (zo + F(z[j], 1 << zb)) * F(S // (2 * n), S) * F(x[j], 1 << xb) / 2
                    point += piece
                    for j, (xj, zj) in enumerate(zip(x, z)):
                        q = offset + j
                        if i == q:
                            continue
                        m = 2 * q + start
                        direct += c * (zo * m - n * F(zj, 1 << zb)) * F(xj, 1 << xb) / (n * n - m * m)
                assert abs(point - direct) <= F(200, S) * sum(
                    abs(F(xj, 1 << xb)) for _, xb, _, x, _ in specs for xj in x
                )
                checked += 1
    return checked


def run(root, near_root, gap_root, source_root, old_finite_root, candidate_root, sector, output_root):
    assert COUNT == 912383 and GAP_OFFSET == 520192 and GAP_OFFSET + GAP_COUNT == 1040383
    stem = f"joint-256000-{sector}.trace-256000.full"
    snapshot = root / (stem + ".zip")
    assert sha(snapshot.read_bytes()) == PINS[sector][0]
    _, s, V, _ = read_snapshot(snapshot)
    assert len(s["modes"]) == N and s["modes"][0] in (1, 2)
    start = s["modes"][0]

    source = load_json(source_root / f"full-stationary-source-{sector}.json", SOURCE[sector])
    Z = combine(V, [F(q) for q in source["q_rational"]])
    assert norm2(Z) == F(source["rational"]["represented_full_stationary_vector_norm2"])

    lift_cert = load_json(gap_root / f"gap-correction-finite-lift-{sector}.json", GAP_LIFT[sector])
    assert lift_cert["schema"] == "cone.certified-gap-correction-finite-lift.v1"
    assert lift_cert["rhs_certificate_sha256"] == GAP_RHS[sector]
    lift = read_buffer(gap_root, lift_cert["lift_buffer"])

    near_cert = load_json(near_root / f"near-seed-refinement-{sector}.json", NEAR[sector])
    near = read_buffer(near_root, near_cert["buffers"]["refined-near-trial"])
    old_near_root = near_root.parent / "near_trial_rhs_witness_v14_238"
    old_near = load_json(old_near_root / f"new-near-trial-rhs-{sector}.json", OLD_NEAR_RHS[sector])
    znear = read_buffer(old_near_root, old_near["buffers"]["action-z-near"])

    old_finite = load_json(old_finite_root / f"wide-compact-near-middle-window-{sector}.json", OLD_FINITE[sector])
    assert old_finite["candidate_sha256"] == OLD_CAND[sector]
    zold = read_buffer(old_finite_root, old_finite["patch_input_z_buffer"])
    old_patch = read_raw_candidate(candidate_root / f"{sector}-wider-correction.bin", OLD_CAND[sector], OLD_COUNT)

    gap_rhs = load_json(gap_root / f"gap-correction-RHS-{sector}.json", GAP_RHS[sector])
    assert gap_rhs["candidate_point_sha256"] == GAP_CAND[sector]
    assert gap_rhs["candidate_count"] == GAP_COUNT
    assert gap_rhs["candidate_first_mode"] == 2 * GAP_OFFSET + start
    assert gap_rhs["candidate_last_mode"] == 2 * (GAP_OFFSET + GAP_COUNT - 1) + start
    zgap = read_buffer(gap_root, gap_rhs["buffers"]["correction-input-z"])
    gap_patch = read_raw_candidate(
        candidate_root / f"{sector}-gap-correction.bin", GAP_CAND[sector], GAP_COUNT, width=17
    )

    front_bits = max(Z["bits"], lift["bits"])
    front = {
        "bits": front_bits,
        "values": [
            (a << (front_bits - Z["bits"])) - (b << (front_bits - lift["bits"]))
            for a, b in zip(Z["values"], lift["values"])
        ],
    }
    components = [
        {"name": "front", "offset": 0, "x": front, "z": {"bits": s["z"]["bits"], "values": s["z"]["values"]}},
        {"name": "near", "offset": N, "x": near, "z": znear},
        {"name": "patch1", "offset": OLD_OFFSET, "x": old_patch, "z": zold},
        {"name": "patch2", "offset": GAP_OFFSET, "x": gap_patch, "z": zgap},
    ]
    assert [(cpt["offset"], len(cpt["x"]["values"])) for cpt in components] == [
        (0, N), (N, N), (OLD_OFFSET, OLD_COUNT), (GAP_OFFSET, GAP_COUNT)
    ]
    assert all(len(cpt["x"]["values"]) == len(cpt["z"]["values"]) for cpt in components)

    zout_bits = max(cpt["z"]["bits"] for cpt in components[1:])
    zout = []
    owners = []
    for cpt in components[1:]:
        shift = zout_bits - cpt["z"]["bits"]
        zout.extend(v << shift for v in cpt["z"]["values"])
        owners.extend([cpt] * len(cpt["z"]["values"]))
    assert len(zout) == len(owners) == COUNT

    cbits = s["c"]["bits"]
    cv = s["c"]["values"][0]
    cpoint = F(cv, 1 << cbits)
    assert abs(cpoint) < 1
    max_xz = max(cpt["x"]["bits"] + max(cpt["z"]["bits"], zout_bits) for cpt in components)
    mix_bits = cbits + 1 + KBITS + max_xz
    mixed = [0] * COUNT
    direct_checks = []
    sample_r = (0, COUNT // 2, COUNT - 1)

    for cpt in components:
        x = cpt["x"]["values"]
        z = cpt["z"]["values"]
        xb = cpt["x"]["bits"]
        zb = cpt["z"]["bits"]
        zx = [a * b for a, b in zip(x, z)]
        print(sector, cpt["name"], "four exact component convolutions begin", flush=True)
        u, v = channels(x, zx, start, cpt["offset"], FIRST, COUNT, KBITS)
        print(sector, cpt["name"], "component convolutions complete", flush=True)
        sv = mix_bits - (cbits + 1 + zout_bits + xb + KBITS)
        su = mix_bits - (cbits + 1 + zb + xb + KBITS)
        assert sv >= 0 and su >= 0
        for r in range(COUNT):
            mixed[r] += (cv * zout[r] * v[r]) << sv
            mixed[r] -= (cv * u[r]) << su
        for r in sample_r:
            i = FIRST + r
            du, dv = direct_channel_row(cpt, start, i)
            assert du == u[r] and dv == v[r]
            direct_checks.append({
                "component": cpt["name"],
                "output_index": i,
                "physical_mode": 2 * i + start,
                "all_component_inputs_match": True,
            })
        del zx, u, v
        gc.collect()

    for r, cpt in enumerate(owners):
        i = FIRST + r
        j = i - cpt["offset"]
        xb = cpt["x"]["bits"]
        zb = cpt["z"]["bits"]
        xv = cpt["x"]["values"][j]
        zv = cpt["z"]["values"][j]
        recip_self = S // (2 * (2 * i + start))
        shift = mix_bits - (cbits + zb + KBITS + xb)
        assert shift >= 0
        mixed[r] += (cv * zv * recip_self * xv) << shift

    pi = enclose(add(times(constant(16), atan_recip(5)), neg(times(constant(4), atan_recip(239)))))
    li = enclosure(*times(times(constant(4), enclose(hyperbolic(start == 2))), recip(pi)), 256)
    ti = enclosure(*times(recip(pi), recip(pi)), 256)
    Lpoint, tpoint = midpoint(li, 256), midpoint(ti, 256)
    assert radius(li, Lpoint) < F(2, S) and radius(ti, tpoint) < F(2, S)

    pbits = s["pole"]["bits"]
    P = F(sum(a * b for a, b in zip(s["pole"]["values"], front["values"])), 1 << (pbits + front_bits))
    for cpt in components[1:]:
        xb = cpt["x"]["bits"]
        for j, xv in enumerate(cpt["x"]["values"]):
            mode = 2 * (cpt["offset"] + j) + start
            pv = floor(Lpoint * mode / (mode * mode + tpoint), 256)
            P += F(pv * xv, 1 << (256 + xb))

    alpha = s["alpha"]
    output = []
    diagonal_error2 = F(0)
    for r, cpt in enumerate(owners):
        i = FIRST + r
        mode = 2 * i + start
        point = F(mixed[r], 1 << mix_bits)
        prow = F(floor(Lpoint * mode / (mode * mode + tpoint), 256), S)
        point += alpha * prow * P
        diagonal = evaluate_diagonal(mode)
        dlo, dhi = F(diagonal["lower_rational"]), F(diagonal["upper_rational"])
        dp = (dlo + dhi) / 2
        j = i - cpt["offset"]
        xi = F(cpt["x"]["values"][j], 1 << cpt["x"]["bits"])
        point += dp * xi
        diagonal_error2 += (max(dp - dlo, dhi - dp) * abs(xi)) ** 2
        output.append(floor(point, 256))
        if (r + 1) % 16000 == 0:
            print(sector, "gap-extended compact rows", r + 1, "/", COUNT, flush=True)

    xnorm2 = sum(norm2(cpt["x"]) for cpt in components)
    xnorm = sqrt_upper(xnorm2, 256)
    l1 = sum(
        F(sum(abs(v) for v in cpt["x"]["values"]), 1 << cpt["x"]["bits"])
        for cpt in components
    )
    rowsqrt = sqrt_upper(F(COUNT), 256)
    diagonal_error = sqrt_upper(diagonal_error2, 256)
    parameter_error = F("1e-34") * l1 * rowsqrt
    reciprocal_rounding = F(40, S) * l1 * rowsqrt
    output_rounding = rowsqrt * F(1, S)
    physical_error = diagonal_error + parameter_error + reciprocal_rounding + output_rounding
    assert physical_error < F("3e-11")

    output_root.mkdir(parents=True, exist_ok=True)
    buffer = writebuffer(output_root, sector, "gap-extended-compact-action", output, 256)
    values = {
        "represented_compact_norm_upper": xnorm,
        "represented_compact_l1": l1,
        "diagonal_interval_action_charge_upper": diagonal_error,
        "offdiagonal_and_pole_parameter_charge_upper": parameter_error,
        "reciprocal_kernel_rounding_charge_upper": reciprocal_rounding,
        "final_row_rounding_charge_upper": output_rounding,
        "complete_gap_extended_compact_action_error_upper": physical_error,
    }
    return {
        "schema": "cone.gap-extended-compact-action.v1",
        "sector": sector,
        "snapshot_sha256": PINS[sector][0],
        "full_source_certificate_sha256": SOURCE[sector],
        "new_gap_lift_certificate_sha256": GAP_LIFT[sector],
        "new_gap_lift_buffer_sha256": lift_cert["lift_buffer"]["sha256"],
        "near_trial_certificate_sha256": NEAR[sector],
        "old_finite_compact_certificate_sha256": OLD_FINITE[sector],
        "old_patch_candidate_sha256": OLD_CAND[sector],
        "gap_rhs_certificate_sha256": GAP_RHS[sector],
        "gap_patch_candidate_sha256": GAP_CAND[sector],
        "definition": (
            "compact component = (Z_full-v14.403 lift) + refined Near + "
            "v14.341 patch + v14.399 gap patch; original infinite seed action separate"
        ),
        "component_offsets_counts": [
            [cpt["name"], cpt["offset"], len(cpt["x"]["values"]), cpt["x"]["bits"], cpt["z"]["bits"]]
            for cpt in components
        ],
        "first_output_mode": 2 * FIRST + start,
        "last_output_mode": 2 * (FIRST + COUNT - 1) + start,
        "complete_output_rows": COUNT,
        "buffer": buffer,
        "rational": {k: str(v) for k, v in values.items()},
        "display_approximate": {k: float(v) for k, v in values.items()},
        "direct_component_rows": direct_checks,
        "independent_component_rectangle_rows_verified": rectangle_verify(),
        "mixed_scale_split_rows_verified": small_split_checks(),
        "raw_physical_diagonal_included_once": True,
        "artificial_Hankel_self_removed_once": True,
        "physical_scalar_parameter_errors_included": True,
        "original_infinite_seed_action_included": False,
        "gap_extended_compact_output_rows_evaluated": True,
        "whole_residual_norm_evaluated": False,
        "stationary_acceptance_met": False,
        "infinite_capacity_tail_closed": False,
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--self-check", action="store_true")
    for name in (
        "root", "near-root", "gap-root", "source-root",
        "old-finite-root", "candidate-root", "output-root",
    ):
        p.add_argument("--" + name, type=Path)
    p.add_argument("--sector", choices=tuple(SOURCE))
    a = p.parse_args()
    if a.self_check:
        print(json.dumps({
            "component_rectangle_rows": rectangle_verify(),
            "mixed_scale_split_rows": small_split_checks(),
        }, sort_keys=True))
    else:
        assert all(
            getattr(a, name.replace("-", "_")) is not None
            for name in (
                "root", "near-root", "gap-root", "source-root",
                "old-finite-root", "candidate-root", "output-root", "sector",
            )
        )
        d = run(
            a.root, a.near_root, a.gap_root, a.source_root, a.old_finite_root,
            a.candidate_root, a.sector, a.output_root,
        )
        path = a.output_root / f"gap-extended-compact-action-{a.sector}.json"
        path.write_text(json.dumps(d, indent=2, sort_keys=True) + "\n")
        print(json.dumps(d["display_approximate"], sort_keys=True), flush=True)
