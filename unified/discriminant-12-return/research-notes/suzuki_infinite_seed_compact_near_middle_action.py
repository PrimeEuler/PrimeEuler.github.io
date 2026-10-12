#!/usr/bin/env python3
"""Complete compact-component action on R<n<=4R for the infinite seed.

The represented compact input is the same hash-bound vector as v14.277:
x_front=Z_full-lift_CI and x_Near=y.  This consumer evaluates every
Near/Middle output row by exact signed integer convolution.  The infinite
seed-tail action is deliberately separate.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

from suzuki_bulk_action_z import evaluate as evaluate_z
from suzuki_certified_remote_diagonal import evaluate as evaluate_diagonal
from suzuki_certified_remote_z import enclosure, midpoint, radius
from suzuki_exact_integer_source_action import convolution, norm2, sqrt_upper
from suzuki_exact_outward_certificate import read_snapshot
from suzuki_frozen_trial_far_outward import (
    add, atan_recip, constant, enclose, hyperbolic, neg, recip, times,
)
from suzuki_full_stationary_source_transport import PINS, combine
from suzuki_near_trial_lift_rhs import floor, writebuffer


SOURCE = {
    "even-v": "40fcbd9ba5745598fa0e8d98a5da43b7c088411c8fdcb4c6d0dcae10a0b9dc80",
    "odd-v": "41fdeb3af0ab1d00bc154cc7111b62d28d5e75365de795ce4a970f779e25138f",
}
LIFT = {
    "even-v": "94dd0622383505bf891adfaa73cda4c53ffd6d7865357720284c2b5cafd4dc31",
    "odd-v": "5e52f9ed934e85a9ed77859400a7b10b79fddbd4059b2cf5d0b98f9ece30c6b8",
}
NEAR = {
    "even-v": "7183ea82d33db24ece4cbb4c73e7ff84a001fe1783c565dc90dcd7fac498af45",
    "odd-v": "3865461f0f672a0b04a9511cc49527f28316fc5c5ed551fb10b813cd9c3f2480",
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load_json(path, pin):
    raw = path.read_bytes()
    assert sha(raw) == pin
    return json.loads(raw)


def read_buffer(root, spec):
    raw = (root / spec["file"]).read_bytes()
    assert sha(raw) == spec["sha256"] and len(raw) == spec["bytes"]
    width = spec["width"]
    values = [
        int.from_bytes(raw[j:j + width], "little", signed=True)
        for j in range(0, len(raw), width)
    ]
    assert len(values) == spec["count"]
    return {"bits": spec["bits"], "values": values}


def rectangular_sums(x, zx, start, first, count, kernel_bits=256):
    """Return T_zx+H_zx and T_x-H_x on consecutive output indices."""
    m = len(x)
    scale = 1 << kernel_bits
    offset = m - 1
    last = first + count - 1
    h = [0] * (last + offset + 1)
    for k in range(-offset, last + 1):
        if k:
            h[k + offset] = floor(F(1, 2 * k), kernel_bits)
    g = [floor(F(1, 2 * (q + start)), kernel_bits)
         for q in range(last + m)]
    tx = convolution(x, h, first + offset, count)
    tzx = convolution(zx, h, first + offset, count)
    hx = convolution(x[::-1], g, first + m - 1, count)
    hzx = convolution(zx[::-1], g, first + m - 1, count)
    return [a + b for a, b in zip(tzx, hzx)], [a - b for a, b in zip(tx, hx)]


def algebra_checks():
    checked = 0
    bits = 18
    scale = 1 << bits
    for start in (1, 2):
        for m in (3, 6, 9):
            x = [(-1) ** j * (j + 2) for j in range(m)]
            z = [(j - 4) for j in range(m)]
            zx = [a * b for a, b in zip(z, x)]
            first, count = m // 2, m + 3
            u, v = rectangular_sums(x, zx, start, first, count, bits)
            for r, i in enumerate(range(first, first + count)):
                du = sum((0 if i == j else floor(F(1, 2 * (i - j)), bits)) * zx[j]
                         + floor(F(1, 2 * (i + j + start)), bits) * zx[j]
                         for j in range(m))
                dv = sum((0 if i == j else floor(F(1, 2 * (i - j)), bits)) * x[j]
                         - floor(F(1, 2 * (i + j + start)), bits) * x[j]
                         for j in range(m))
                assert u[r] == du and v[r] == dv
                checked += 1
    return checked


def run(root, near_root, lift_root, source_root, sector, output_root):
    stem = f"joint-256000-{sector}.trace-256000.full"
    snapshot = root / (stem + ".zip")
    assert sha(snapshot.read_bytes()) == PINS[sector][0]
    _, s, V, _ = read_snapshot(snapshot)
    nfront = len(s["modes"])
    assert nfront == 128000
    start = s["modes"][0]

    source_path = source_root / f"full-stationary-source-{sector}.json"
    source = load_json(source_path, SOURCE[sector])
    Z = combine(V, [F(q) for q in source["q_rational"]])
    assert norm2(Z) == F(source["rational"]["represented_full_stationary_vector_norm2"])

    lift_path = lift_root / f"infinite-seed-finite-lift-{sector}.json"
    lift_cert = load_json(lift_path, LIFT[sector])
    lift = read_buffer(lift_root, lift_cert["lift_buffer"])

    near_path = near_root / f"new-near-trial-rhs-{sector}.json"
    near_cert = load_json(near_path, NEAR[sector])
    y = read_buffer(near_root, near_cert["buffers"]["trial-near"])
    znear = read_buffer(near_root, near_cert["buffers"]["action-z-near"])

    xbits = max(Z["bits"], lift["bits"], y["bits"])
    zbits = max(s["z"]["bits"], znear["bits"])
    x = [
        (a << (xbits - Z["bits"])) - (b << (xbits - lift["bits"]))
        for a, b in zip(Z["values"], lift["values"])
    ] + [a << (xbits - y["bits"]) for a in y["values"]]
    zin = [a << (zbits - s["z"]["bits"]) for a in s["z"]["values"]] + [
        a << (zbits - znear["bits"]) for a in znear["values"]
    ]
    zx = [a * b for a, b in zip(zin, x)]
    assert len(x) == len(zin) == 2 * nfront

    first = nfront
    count = 3 * nfront
    print(sector, "four exact rectangular convolutions begin", flush=True)
    u, v = rectangular_sums(x, zx, start, first, count)
    print(sector, "four exact rectangular convolutions complete", flush=True)

    pi = enclose(add(times(constant(16), atan_recip(5)), neg(times(constant(4), atan_recip(239)))))
    li = enclosure(*times(times(constant(4), enclose(hyperbolic(start == 2))), recip(pi)), 256)
    ti = enclosure(*times(recip(pi), recip(pi)), 256)
    Lpoint, tpoint = midpoint(li, 256), midpoint(ti, 256)
    assert radius(li, Lpoint) < F(2, 1 << 256)
    assert radius(ti, tpoint) < F(2, 1 << 256)

    pfront = s["pole"]["values"]
    pbits = s["pole"]["bits"]
    P = F(sum(a * b for a, b in zip(pfront, x[:nfront])), 1 << (pbits + xbits))
    for j, value in enumerate(x[nfront:]):
        mode = 2 * (nfront + j) + start
        P += F(floor(Lpoint * mode / (mode * mode + tpoint), 256) * value,
               1 << (256 + xbits))

    c = F(s["c"]["values"][0], 1 << s["c"]["bits"])
    alpha = s["alpha"]
    assert abs(c) < 1
    output = []
    diagonal_error2 = F(0)
    direct_checks = []
    kernel_scale = 1 << 256
    for r, i in enumerate(range(first, first + count)):
        mode = 2 * i + start
        zrow = evaluate_z(mode)
        zlo, zhi = F(zrow["lower_rational"]), F(zrow["upper_rational"])
        zp = F(floor((zlo + zhi) / 2, zbits), 1 << zbits)
        assert max(zp - zlo, zhi - zp) < F("1e-39") and abs(zp) < 8
        point = c * (zp * F(v[r], 1 << (xbits + 256))
                     - F(u[r], 1 << (zbits + xbits + 256))) / 2
        prow = F(floor(Lpoint * mode / (mode * mode + tpoint), 256), 1 << 256)
        point += alpha * prow * P
        if i < 2 * nfront:
            diagonal = evaluate_diagonal(mode)
            dlo, dhi = F(diagonal["lower_rational"]), F(diagonal["upper_rational"])
            dp = (dlo + dhi) / 2
            xi = F(x[i], 1 << xbits)
            point += dp * xi
            diagonal_error2 += (max(dp - dlo, dhi - dp) * abs(xi)) ** 2
        output.append(floor(point, 256))

        if r in (0, nfront // 2, nfront - 1, 2 * nfront, count - 1):
            du = sum((0 if i == j else floor(F(1, 2 * (i - j)), 256)) * zx[j]
                     + floor(F(1, 2 * (i + j + start)), 256) * zx[j]
                     for j in range(2 * nfront))
            dv = sum((0 if i == j else floor(F(1, 2 * (i - j)), 256)) * x[j]
                     - floor(F(1, 2 * (i + j + start)), 256) * x[j]
                     for j in range(2 * nfront))
            assert du == u[r] and dv == v[r]
            direct_checks.append({"output_index": i, "physical_mode": mode,
                                  "all_256000_compact_inputs_match": True})
        if (r + 1) % 16000 == 0:
            print(sector, "complete compact Near/Middle rows", r + 1, "/", count, flush=True)

    xnorm = sqrt_upper(F(sum(a * a for a in x), 1 << (2 * xbits)), 256)
    l1 = sqrt_upper(F(2 * nfront), 256) * xnorm
    rowsqrt = sqrt_upper(F(count), 256)
    diagonal_error = sqrt_upper(diagonal_error2, 256)
    parameter_error = F("1e-34") * l1 * rowsqrt
    # Each of the two rounded reciprocal channels costs <eps and
    # |z_output|+|z_input|<19, so 20*eps*||x||_1 per row is uniform.
    reciprocal_rounding = F(20, 1 << 256) * l1 * rowsqrt
    output_rounding = rowsqrt * F(1, 1 << 256)
    physical_error = diagonal_error + parameter_error + reciprocal_rounding + output_rounding
    assert physical_error < F("3e-11")

    output_root.mkdir(parents=True, exist_ok=True)
    buffer = writebuffer(output_root, sector, "compact-near-middle-action", output, 256)
    values = {
        "diagonal_interval_action_charge_upper": diagonal_error,
        "offdiagonal_and_pole_parameter_charge_upper": parameter_error,
        "reciprocal_kernel_rounding_charge_upper": reciprocal_rounding,
        "final_row_rounding_charge_upper": output_rounding,
        "complete_compact_near_middle_action_error_upper": physical_error,
    }
    return {
        "schema": "cone.infinite-seed-compact-near-middle-action.v1",
        "sector": sector,
        "snapshot_sha256": PINS[sector][0],
        "full_source_certificate_sha256": SOURCE[sector],
        "actual_CI_lift_certificate_sha256": LIFT[sector],
        "actual_CI_lift_sha256": lift_cert["lift_buffer"]["sha256"],
        "near_trial_certificate_sha256": NEAR[sector],
        "definition": "compact component only: x_front=Z_full-lift_CI; x_Near=y; infinite seed tail separate",
        "first_output_mode": 2 * first + start,
        "last_output_mode": 2 * (first + count - 1) + start,
        "complete_output_rows": count,
        "buffer": buffer,
        "rational": {key: str(value) for key, value in values.items()},
        "display_approximate": {key: float(value) for key, value in values.items()},
        "direct_complete_rows": direct_checks,
        "small_rectangular_rows_verified": algebra_checks(),
        "exact_signed_toeplitz_hankel_convolutions": 4,
        "physical_scalar_parameter_errors_included": True,
        "infinite_seed_tail_action_included": False,
        "compact_near_middle_output_rows_evaluated": True,
        "whole_residual_norm_evaluated": False,
        "stationary_acceptance_met": False,
        "infinite_capacity_tail_closed": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    for name in ("root", "near-root", "lift-root", "source-root", "output-root"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--sector", choices=sorted(SOURCE), required=True)
    args = parser.parse_args()
    result = run(args.root, args.near_root, args.lift_root, args.source_root,
                 args.sector, args.output_root)
    path = args.output_root / f"infinite-seed-compact-near-middle-{args.sector}.json"
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["display_approximate"], sort_keys=True), flush=True)
