#!/usr/bin/env python3
"""Build a complete finite-front RHS after the frozen v14.500 direct-middle delta.

This producer reconstructs and hash-checks the repository chunk archives.  It
updates the exact v14.403 complete RHS; it does not reuse the v14.403 lift and
does not claim action or residual acceptance.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json

from suzuki_exact_integer_source_action import convolution, sqrt_upper
from suzuki_bulk_action_z import evaluate
from suzuki_frozen_trial_far_outward import (
    atan_recip, hyperbolic, add, times, neg, constant, recip, enclose,
)
from suzuki_certified_remote_z import enclosure, midpoint, radius

N = 128000
M = 1040383
OFFSET = 1040383
S = 1 << 256
SNAPSHOT_SHA256 = {
    "even-v": "da7189749abb6872e28e2af6c189c609248bc094428db21ee0cafa5e68c2deb5",
    "odd-v": "6ba7a15aafacebdf0eb4e8b035370f4a7588d63133031e99a8a882779f20a453",
}
BASE_CERT_SHA256 = {
    "even-v": "42c71d7e017eadc08a6ebe20045f6d6e83bbe3523e17ba282903eccf08edc075",
    "odd-v": "1309bec0a4568684f3631a2d88a278ba711c8496960491e5a81428a8fb5b30b3",
}
CANDIDATE_SHA256 = {
    "even-v": "c5b6845303cb059ca9a1ed79a628c4ba135fd49f2012b5fc011b0aeb14d12bb2",
    "odd-v": "e9efaf914390a6edda7076ad1a1dfa7da5a398246895bc76e00cbb21b682f776",
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def floor(q, bits=256):
    return q.numerator * (1 << bits) // q.denominator


def load_json(path, expected=None):
    raw = path.read_bytes()
    if expected is not None:
        assert sha(raw) == expected
    return json.loads(raw)


def chunked_raw(root, spec, name_key="name"):
    parts = []
    offset = 0
    for part in spec["chunks"]:
        raw = (root / part[name_key]).read_bytes()
        assert len(raw) == part["bytes"] and sha(raw) == part["sha256"]
        if "offset" in part:
            assert part["offset"] == offset
        parts.append(raw)
        offset += len(raw)
    raw = b"".join(parts)
    assert len(raw) == spec["bytes"] and sha(raw) == spec["sha256"]
    return raw


def integers(raw, width, count):
    assert len(raw) == width * count
    return [int.from_bytes(raw[j:j + width], "little", signed=True)
            for j in range(0, len(raw), width)]


def write_buffer(root, sector, label, values, bits):
    width = (max(abs(v).bit_length() for v in values) + 8) // 8
    raw = b"".join(v.to_bytes(width, "little", signed=True) for v in values)
    name = f"{sector}-{label}.bin"
    (root / name).write_bytes(raw)
    return {"file": name, "bits": bits, "width": width, "count": len(values),
            "bytes": len(raw), "sha256": sha(raw)}


def rectangular_transpose(y, zy, start, n=N, offset=OFFSET, bits=256):
    m = len(y)
    scale = 1 << bits
    h = [0] + [scale // (2 * q) for q in range(1, offset + m)]
    g = [scale // (2 * (q + start)) for q in range(offset + m + n - 1)]
    ty = convolution(y[::-1], h, offset + m - n, n)[::-1]
    tz = convolution(zy[::-1], h, offset + m - n, n)[::-1]
    hy = convolution(y[::-1], g, offset + m - 1, n)
    hz = convolution(zy[::-1], g, offset + m - 1, n)
    return [a - b for a, b in zip(tz, hz)], [a + b for a, b in zip(ty, hy)]


def self_check():
    checked = 0
    bits = 40
    scale = 1 << bits
    c = F(2, 3)
    for start in (1, 2):
        for n in (2, 3, 7):
            for m in (3, 7, 11):
                offset = 4 * n + 3
                y = [(-1) ** j * (j + 2) for j in range(m)]
                z = [(-1) ** j * (j % 5 + 1) for j in range(m)]
                u, v = rectangular_transpose(y, [a * b for a, b in zip(y, z)],
                                             start, n, offset, bits)
                for i in range(n):
                    nf = 2 * i + start
                    zf = (-1) ** i * (i % 7 + 1)
                    direct = c * sum(
                        F((zf * (2 * (offset + j) + start) - nf * z[j]) * y[j],
                          nf * nf - (2 * (offset + j) + start) ** 2)
                        for j in range(m)
                    )
                    point = c * F(u[i] - zf * v[i], 2 * scale)
                    assert abs(point - direct) <= F(20, scale) * sum(abs(a) for a in y)
                    checked += 1
    return checked


def run(snapshot, base_root, candidate_root, sector, out):
    base_manifest = load_json(base_root / "manifest.json")
    candidate_manifest = load_json(candidate_root / "manifest.json")
    base_cert_name = f"gap-correction-RHS-{sector}.json"
    base = load_json(base_root / base_cert_name, BASE_CERT_SHA256[sector])
    base_spec = base_manifest["buffers"][base["buffers"]["lift-rhs"]["file"]]
    assert base_spec["sha256"] == base["buffers"]["lift-rhs"]["sha256"]
    old_rhs = integers(chunked_raw(base_root, base_spec), base_spec["width"], N)

    candidate_spec = dict(candidate_manifest["buffers"][sector])
    candidate_file = candidate_spec["file"]
    candidate_spec["sha256"] = candidate_manifest["files"][candidate_file]["sha256"]
    assert candidate_spec["sha256"] == CANDIDATE_SHA256[sector]
    delta = integers(chunked_raw(candidate_root, candidate_spec, "file"),
                     candidate_spec["width"], M)

    raw_snapshot = snapshot.read_bytes()
    assert sha(raw_snapshot) == SNAPSHOT_SHA256[sector]
    from suzuki_exact_outward_certificate import read_snapshot
    _, state, _, _ = read_snapshot(snapshot)
    start = 1 if sector == "even-v" else 2
    assert state["modes"][0] == start and len(state["modes"]) == N
    first = 2 * OFFSET + start
    last = first + 2 * (M - 1)
    assert (first, last) == ((2080767, 4161531) if start == 1 else (2080768, 4161532))

    correction_norm = sqrt_upper(F(sum(v * v for v in delta), 1 << 320), 256)
    trial_norm = F(base["rational"]["new_whole_trial_norm_upper"]) + correction_norm
    assert trial_norm < F("0.002")

    pi = enclose(add(times(constant(16), atan_recip(5)),
                     neg(times(constant(4), atan_recip(239)))))
    li = enclosure(*times(times(constant(4), enclose(hyperbolic(start == 2))), recip(pi)), 256)
    ti = enclosure(*times(recip(pi), recip(pi)), 256)
    L = midpoint(li, 256)
    t = midpoint(ti, 256)
    assert 0 < L < 2 and 0 < t < 1
    assert radius(li, L) < F(2, S) and radius(ti, t) < F(2, S)

    z = []
    pole = []
    max_z_error = F(0)
    for j in range(M):
        mode = first + 2 * j
        enclosure_z = evaluate(mode)
        lo, hi = F(enclosure_z["lower_rational"]), F(enclosure_z["upper_rational"])
        zp = floor((lo + hi) / 2, 160)
        max_z_error = max(max_z_error, abs(lo - F(zp, 1 << 160)),
                          abs(hi - F(zp, 1 << 160)))
        z.append(zp)
        pole.append(floor(L * mode / (mode * mode + t)))
        if (j + 1) % 16000 == 0:
            print(sector, "direct-middle correction physical-z rows", j + 1, "/", M, flush=True)
    assert max_z_error < F("1e-39") and max(abs(v) for v in z) < 8 * (1 << 160)

    zy = [a * b for a, b in zip(z, delta)]
    u, v = rectangular_transpose(delta, zy, start)
    P = F(sum(a * b for a, b in zip(pole, delta)), 1 << 416)
    c = F(state["c"]["values"][0], 1 << state["c"]["bits"])
    updated = []
    checks = []
    for i in range(N):
        zf = F(state["z"]["values"][i], 1 << state["z"]["bits"])
        pf = F(state["pole"]["values"][i], 1 << state["pole"]["bits"])
        q = c * (F(u[i], 1 << 576) - zf * F(v[i], 1 << 416)) / 2 + state["alpha"] * pf * P
        updated.append(old_rhs[i] + floor(q))
        if i in (0, N // 2, N - 1):
            du = sum((S // (2 * (OFFSET + j - i)) -
                      S // (2 * (OFFSET + j + i + start))) * zy[j] for j in range(M))
            dv = sum((S // (2 * (OFFSET + j - i)) +
                      S // (2 * (OFFSET + j + i + start))) * delta[j] for j in range(M))
            assert du == u[i] and dv == v[i]
            checks.append({"front_index": i, "all_1040383_correction_inputs_match": True})

    l1 = F(sum(abs(v) for v in delta), 1 << 160)
    eps = F(1, S)
    row_error = ((F("21e-38") + 19 * eps) * l1 +
                 2 * F("1e-38") * abs(P) + 16 * eps * l1 + eps)
    error = sqrt_upper(F(N), 256) * row_error + F(base["rational"]["physical_lift_rhs_error_upper"])
    assert error < F("4e-30")

    out.mkdir(parents=True, exist_ok=True)
    z_buffer = write_buffer(out, sector, "direct-middle-input-z", z, 160)
    rhs_buffer = write_buffer(out, sector, "direct-middle-complete-lift-rhs", updated, 256)
    return {
        "schema": "cone.direct-middle-delta-complete-finite-rhs.v1",
        "sector": sector,
        "snapshot_sha256": SNAPSHOT_SHA256[sector],
        "base_v14_403_rhs_certificate_sha256": BASE_CERT_SHA256[sector],
        "candidate_point_sha256": CANDIDATE_SHA256[sector],
        "candidate_bits": 160,
        "candidate_count": M,
        "candidate_first_mode": first,
        "candidate_last_mode": last,
        "buffers": {"lift-rhs": rhs_buffer, "correction-input-z": z_buffer},
        "rational": {
            "direct_middle_correction_norm_upper": str(correction_norm),
            "new_whole_trial_norm_upper": str(trial_norm),
            "physical_lift_rhs_error_upper": str(error),
            "maximum_correction_input_z_error": str(max_z_error),
        },
        "complete_direct_front_checks": checks,
        "small_exact_physical_kernel_checks": self_check(),
        "display_approximate": {
            "correction_norm": float(correction_norm),
            "trial_norm_upper": float(trial_norm),
            "RHS_error": float(error),
        },
        "all_128000_new_RHS_rows_evaluated": True,
        "finite_correction_preserves_domain": True,
        "new_finite_lift_certified": False,
        "new_residual_evaluated": False,
        "whole_residual_acceptance_certified": False,
        "infinite_capacity_tail_closed": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--snapshot", type=Path)
    parser.add_argument("--base-root", type=Path)
    parser.add_argument("--candidate-root", type=Path)
    parser.add_argument("--sector", choices=("even-v", "odd-v"))
    parser.add_argument("--output-root", type=Path)
    args = parser.parse_args()
    if args.self_check:
        print(json.dumps({"exact_physical_kernel_rows_verified": self_check()}))
    else:
        assert all(v is not None for v in (args.snapshot, args.base_root,
                                           args.candidate_root, args.sector,
                                           args.output_root))
        result = run(args.snapshot, args.base_root, args.candidate_root,
                     args.sector, args.output_root)
        cert = args.output_root / f"direct-middle-complete-RHS-{args.sector}.json"
        cert.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        print(json.dumps(result["display_approximate"]), flush=True)
