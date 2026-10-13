#!/usr/bin/env python3
"""Full new compact action on Near/Middle/Far-window with the wider patch.
Original infinite seed action remains a separate unchanged component.
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
from suzuki_wider_correction_rhs import floor
from suzuki_wider_correction_finite_lift import writebuffer
from suzuki_compact_action_self_diagonal import compensate_self, verify as physical_self_checks


SOURCE = {
    "even-v": "40fcbd9ba5745598fa0e8d98a5da43b7c088411c8fdcb4c6d0dcae10a0b9dc80",
    "odd-v": "41fdeb3af0ab1d00bc154cc7111b62d28d5e75365de795ce4a970f779e25138f",
}
LIFT = {
    "even-v": "98df9edfee779854e540192a2941d43e44ab85556598c6b76b7d48f0e0e50df3",
    "odd-v": "99a741a41932261569db364698f5998a52204fdf1aad872e972afa0857075075",
}
NEAR = {
    "even-v": "cca920b7b5f20fd856807166fdc08cce82f4b108f61831c34f19da29e366f42b",
    "odd-v": "85a45f5fa1e5bedc8100c69a3fd4c31324c10aa30bc635a1e61d9a24ac93c6ba",
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


def run(root, near_root, lift_root, source_root, candidate_root, sector, output_root):
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

    lift_path = lift_root / f"wider-correction-finite-lift-{sector}.json"
    lift_cert = load_json(lift_path, LIFT[sector])
    lift = read_buffer(lift_root, lift_cert["lift_buffer"])

    near_path = near_root / f"near-seed-refinement-{sector}.json"
    near_cert = load_json(near_path, NEAR[sector])
    y = read_buffer(near_root, near_cert["buffers"]["refined-near-trial"])
    old_near_root=near_root.parent / "near_trial_rhs_witness_v14_238"
    old_near=load_json(old_near_root / f"new-near-trial-rhs-{sector}.json", {"even-v":"7183ea82d33db24ece4cbb4c73e7ff84a001fe1783c565dc90dcd7fac498af45","odd-v":"3865461f0f672a0b04a9511cc49527f28316fc5c5ed551fb10b813cd9c3f2480"}[sector])
    znear = read_buffer(old_near_root, old_near["buffers"]["action-z-near"])

    xbits = max(Z["bits"], lift["bits"], y["bits"])
    zbits = max(s["z"]["bits"], znear["bits"])
    x = [
        (a << (xbits - Z["bits"])) - (b << (xbits - lift["bits"]))
        for a, b in zip(Z["values"], lift["values"])
    ] + [a << (xbits - y["bits"]) for a in y["values"]]
    zin = [a << (zbits - s["z"]["bits"]) for a in s["z"]["values"]] + [
        a << (zbits - znear["bits"]) for a in znear["values"]
    ]
    raw=(candidate_root/f"{sector}-wider-correction.bin").read_bytes()
    candidate_pin={"even-v":"fdf93112802fe28ef53efa804be760a0fc17abc404993c8b2af6c33b1b5aba05","odd-v":"b772ab850121daf0bd85afd01e26fee9f72d14b940c4145ae7643734435f8967"}[sector]
    assert len(raw)==4755456 and sha(raw)==candidate_pin
    delta=[int.from_bytes(raw[j:j+18],"little",signed=True) for j in range(0,len(raw),18)]
    x += [a << (xbits-160) for a in delta]
    max_remote_z_error=F("1e-39")
    patchz=[]
    output_root.mkdir(parents=True,exist_ok=True)
    for j in range(len(delta)):
        mode=2*(2*nfront+j)+start
        row=evaluate_z(mode);lo,hi=F(row["lower_rational"]),F(row["upper_rational"])
        zp=floor((lo+hi)/2,zbits);rep=F(zp,1<<zbits)
        assert max(abs(lo-rep),abs(hi-rep))<max_remote_z_error and abs(rep)<8
        patchz.append(zp)
        if (j+1)%16000==0:print(sector,"fresh wider compact input z",j+1,"/",len(delta),flush=True)
    zin += patchz
    assert len(x)==len(zin)==2*nfront+264192
    assert max(abs(a) for a in zin[:nfront])<11*(1<<zbits)
    assert max(abs(a) for a in zin[nfront:])<8*(1<<zbits)
    patch_z_buffer=writebuffer(output_root,sector,"wide-patch-input-z",patchz,zbits)
    zx = [a * b for a, b in zip(zin, x)]
    first=nfront
    count=len(x)-nfront
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
        # Output modes are on the same complete input lattice. Reuse the
        # freshly/certificate-verified represented scalar, not a display.
        zp=F(zin[i],1<<zbits)
        point = c * (zp * F(v[r], 1 << (xbits + 256))
                     - F(u[r], 1 << (zbits + xbits + 256))) / 2
        prow = F(floor(Lpoint * mode / (mode * mode + tpoint), 256), 1 << 256)
        point += alpha * prow * P
        if i < len(x):
            diagonal = evaluate_diagonal(mode)
            dlo, dhi = F(diagonal["lower_rational"]), F(diagonal["upper_rational"])
            dp = (dlo + dhi) / 2
            xi = F(x[i], 1 << xbits)
            point=compensate_self(point,c,zp,F(zin[i],1<<zbits),xi,F(floor(F(1,2*mode),256),1<<256))
            point += dp * xi
            diagonal_error2 += (max(dp - dlo, dhi - dp) * abs(xi)) ** 2
        output.append(floor(point, 256))

        if r in (0, nfront // 2, nfront - 1, 2 * nfront, count - 1):
            du = sum((0 if i == j else floor(F(1, 2 * (i - j)), 256)) * zx[j]
                     + floor(F(1, 2 * (i + j + start)), 256) * zx[j]
                     for j in range(len(x)))
            dv = sum((0 if i == j else floor(F(1, 2 * (i - j)), 256)) * x[j]
                     - floor(F(1, 2 * (i + j + start)), 256) * x[j]
                     for j in range(len(x)))
            assert du == u[r] and dv == v[r]
            direct_checks.append({"output_index": i, "physical_mode": mode,
                                  "all_520192_compact_inputs_match": True})
        if (r + 1) % 16000 == 0:
            print(sector, "complete compact Near/Middle rows", r + 1, "/", count, flush=True)

    xnorm = sqrt_upper(F(sum(a * a for a in x), 1 << (2 * xbits)), 256)
    l1 = sqrt_upper(F(len(x)), 256) * xnorm
    rowsqrt = sqrt_upper(F(count), 256)
    diagonal_error = sqrt_upper(diagonal_error2, 256)
    parameter_error = F("1e-34") * l1 * rowsqrt
    # Each of the two rounded reciprocal channels costs <eps and
    # |z_output|+|z_input|<19, so 20*eps*||x||_1 per row is uniform.
    reciprocal_rounding = F(40, 1 << 256) * l1 * rowsqrt
    output_rounding = rowsqrt * F(1, 1 << 256)
    physical_error = diagonal_error + parameter_error + reciprocal_rounding + output_rounding
    assert physical_error < F("3e-11")

    output_root.mkdir(parents=True, exist_ok=True)
    buffer = writebuffer(output_root, sector, "wide-compact-near-middle-window-action", output, 256)
    values = {
        "diagonal_interval_action_charge_upper": diagonal_error,
        "offdiagonal_and_pole_parameter_charge_upper": parameter_error,
        "reciprocal_kernel_rounding_charge_upper": reciprocal_rounding,
        "final_row_rounding_charge_upper": output_rounding,
        "complete_compact_near_middle_window_action_error_upper": physical_error,
    }
    return {
        "schema": "cone.wider-compact-near-middle-window-action.v1",
        "sector": sector,
        "snapshot_sha256": PINS[sector][0],
        "full_source_certificate_sha256": SOURCE[sector],
        "actual_CI_lift_certificate_sha256": LIFT[sector],
        "actual_CI_lift_sha256": lift_cert["lift_buffer"]["sha256"],
        "near_trial_certificate_sha256": NEAR[sector],
        "definition": "compact component: x_front=Z_full-v14.345_lift; x_Near=refined_y; x_MiddleWindow=delta_y; original infinite seed tail separate",
        "candidate_sha256":candidate_pin,
        "patch_input_z_buffer":patch_z_buffer,
        "artificial_Hankel_self_removed_with_same_reciprocal":True,
        "independent_exact_physical_self_rows_verified":physical_self_checks(),
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
        "compact_near_middle_window_output_rows_evaluated": True,
        "whole_residual_norm_evaluated": False,
        "stationary_acceptance_met": False,
        "infinite_capacity_tail_closed": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    for name in ("root", "near-root", "lift-root", "source-root", "candidate-root", "output-root"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--sector", choices=sorted(SOURCE), required=True)
    args = parser.parse_args()
    result = run(args.root, args.near_root, args.lift_root, args.source_root, args.candidate_root,
                 args.sector, args.output_root)
    path = args.output_root / f"wide-compact-near-middle-window-{args.sector}.json"
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["display_approximate"], sort_keys=True), flush=True)


