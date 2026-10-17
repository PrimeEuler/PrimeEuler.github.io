#!/usr/bin/env python3
"""Produce and exactly replay fresh finite lifts for the v14.539 RHS return.

The two v14.539 RHS certificates and their lift-RHS buffers are pinned below.
This module never accepts a substitute RHS and never reuses a v14.403 lift.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import json

from suzuki_new_finite_lift import produce
from suzuki_exact_outward_certificate import (
    read_snapshot, support_dot, subtract, operator_radius,
)
from suzuki_exact_integer_source_action import ExactSource, norm2, dot, sqrt_upper
from suzuki_full_stationary_source_transport import PINS
from suzuki_trace_congruence_replay import inv, mul, tr

N = 128000
SNAPSHOT_SHA256 = {
    "even-v": "da7189749abb6872e28e2af6c189c609248bc094428db21ee0cafa5e68c2deb5",
    "odd-v": "6ba7a15aafacebdf0eb4e8b035370f4a7588d63133031e99a8a882779f20a453",
}
CANDIDATE_SHA256 = {
    "even-v": "c5b6845303cb059ca9a1ed79a628c4ba135fd49f2012b5fc011b0aeb14d12bb2",
    "odd-v": "e9efaf914390a6edda7076ad1a1dfa7da5a398246895bc76e00cbb21b682f776",
}
RHS_CERT_SHA256 = {
    "even-v": "d56eaf3ade699c5c85ad3ae954c5817c3e58045c6894268b3e49e6a7b2ad55ad",
    "odd-v": "19c67577d032366253625a0f12ed08c217d10c0245fdd03e4bb6ce953cfb2884",
}
RHS_POINT_SHA256 = {
    "even-v": "2fb4363ff1ad6a12fb6428eb80dd4aab90365662e79ff90f4ac0c826d7b5d658",
    "odd-v": "e8d1e795c2df50c66bb9c972797c50af1581f31288c4550a3a1e307ef06d13a2",
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def integers(raw, width):
    assert width > 0 and len(raw) % width == 0
    return [int.from_bytes(raw[j:j + width], "little", signed=True)
            for j in range(0, len(raw), width)]


def write_buffer(root, sector, label, values, bits):
    width = (max(abs(v).bit_length() for v in values) + 8) // 8
    raw = b"".join(v.to_bytes(width, "little", signed=True) for v in values)
    name = f"{sector}-{label}.bin"
    (root / name).write_bytes(raw)
    return {"file": name, "bits": bits, "width": width,
            "count": len(values), "bytes": len(raw), "sha256": sha(raw)}


def self_check():
    assert set(SNAPSHOT_SHA256) == set(CANDIDATE_SHA256) == set(RHS_CERT_SHA256) == set(RHS_POINT_SHA256) == set(PINS)
    checked = 0
    for sector in SNAPSHOT_SHA256:
        assert PINS[sector][0] == SNAPSHOT_SHA256[sector]
        for table in (SNAPSHOT_SHA256, CANDIDATE_SHA256,
                      RHS_CERT_SHA256, RHS_POINT_SHA256):
            value = table[sector]
            assert len(value) == 64
            int(value, 16)
            checked += 1
    return {"sectors": 2, "hash_bindings_checked": checked,
            "rhs_rows_per_sector": N, "old_v14_403_lift_reused": False}


def load(root, rhs_root, sector):
    stem = f"joint-256000-{sector}.trace-256000.full"
    snapshot = root / (stem + ".zip")
    primary_raw = (root / (stem + ".certificate.json")).read_bytes()
    assert sha(snapshot.read_bytes()) == SNAPSHOT_SHA256[sector] == PINS[sector][0]
    assert sha(primary_raw) == PINS[sector][1]
    meta, state, V, P = read_snapshot(snapshot)
    primary = json.loads(primary_raw)
    assert primary["all_six_numerical_targets_met"]
    assert all(primary["checks_exact"].values())

    cert_name = f"direct-middle-complete-RHS-{sector}.json"
    rhs_raw = (rhs_root / cert_name).read_bytes()
    assert sha(rhs_raw) == RHS_CERT_SHA256[sector]
    cert = json.loads(rhs_raw)
    spec = cert["buffers"]["lift-rhs"]
    rhs = (rhs_root / spec["file"]).read_bytes()
    assert len(rhs) == spec["bytes"] == N * spec["width"]
    assert sha(rhs) == spec["sha256"] == RHS_POINT_SHA256[sector]

    assert cert["schema"] == "cone.direct-middle-delta-complete-finite-rhs.v1"
    assert cert["sector"] == sector
    assert cert["snapshot_sha256"] == SNAPSHOT_SHA256[sector]
    assert cert["candidate_point_sha256"] == CANDIDATE_SHA256[sector]
    assert cert["all_128000_new_RHS_rows_evaluated"]
    assert cert["finite_correction_preserves_domain"]
    assert spec["bits"] == 256 and spec["count"] == N
    assert F(cert["rational"]["physical_lift_rhs_error_upper"]) < F("4e-30")
    assert F(cert["rational"]["new_whole_trial_norm_upper"]) < F("0.002")
    assert not cert["new_finite_lift_certified"]
    assert not cert["new_residual_evaluated"]
    assert not cert["whole_residual_acceptance_certified"]
    assert not cert["infinite_capacity_tail_closed"]

    g = {"bits": spec["bits"], "values": integers(rhs, spec["width"])}
    assert len(g["values"]) == N
    return meta, state, V, P, primary, cert, g, sha(rhs_raw)


def certify(ctx, Z, sector, spec):
    meta, state, V, P, primary, cert, g, rhs_sha = ctx
    print(sector, "exact direct-middle physical finite lift certification", flush=True)
    residual = subtract(ExactSource(state, meta["kernel_bits"]).action(Z), g)
    gram = [[dot(a, b) for b in P] for a in P]
    gram_inverse = inv(gram)
    projected = [[support_dot(p, residual)] for p in P]
    q2 = norm2(residual) - mul(tr(projected), mul(gram_inverse, projected))[0][0]
    assert q2 >= 0
    protected2 = sum(dot(v, residual) ** 2 for v in V[:6])
    lift_norm = sqrt_upper(norm2(Z), 192)
    graph_norm = sqrt_upper(F(primary["graph_vector_norm2_rational"]), 192)
    radius, _, _ = operator_radius(state, meta["kernel_bits"])
    assert radius == F(primary["operator_radius_rational"])
    input_error = radius * lift_norm + F(cert["rational"]["physical_lift_rhs_error_upper"])
    q_upper = sqrt_upper(q2, 192) + input_error
    protected_upper = sqrt_upper(protected2, 192) + graph_norm * input_error

    matrix = [[F(x) for x in row] for row in primary["M_point_decimal"]]
    J = [row[:6] for row in matrix[:6]]
    gamma = F("2.37e-13" if sector == "even-v" else "4.15e-12")
    rho = F(primary["relative_trace_fro_upper_rational"])
    nu = rho / (1 - rho)
    bounds = {key: F(value) for key, value in primary["bounds_rational"].items()}
    f = bounds["graph_residual_fro"] / (1 - rho)
    j_floor = min(J[i][i] - sum(abs(J[i][k]) for k in range(6) if k != i)
                  for i in range(6))
    matrix_norm = max(sum(abs(value) for value in row) for row in matrix)
    assembly = (bounds["assembly_J"] + 2 * bounds["assembly_beta"] +
                bounds["assembly_eta"])
    graph_floor = j_floor - (bounds["assembly_J"] +
                             nu * (2 + nu) * (matrix_norm + assembly) +
                             f * f / gamma)
    assert graph_floor > 0

    energy = (q_upper * q_upper / gamma +
              (protected_upper / (1 - rho) + f * q_upper / gamma) ** 2 /
              graph_floor)
    grid = 1 << 192
    energy = F(-((-energy.numerator * grid) // energy.denominator), grid)
    charge = 22 * sqrt_upper(energy, 192)
    assert charge < F("2e-10")
    values = {
        "represented_lift_norm2": norm2(Z),
        "point_projected_residual_norm2": q2,
        "point_protected_dot_norm2": protected2,
        "physical_projected_residual_upper": q_upper,
        "physical_protected_dot_upper": protected_upper,
        "operator_radius": radius,
        "rhs_input_error_upper": F(cert["rational"]["physical_lift_rhs_error_upper"]),
        "combined_operator_and_rhs_input_error_upper": input_error,
        "graph_floor": graph_floor,
        "inverse_energy_error_upper": energy,
        "finite_lift_remote_action_charge_upper": charge,
    }
    return {
        "schema": "cone.certified-direct-middle-delta-finite-lift.v1",
        "sector": sector,
        "snapshot_sha256": SNAPSHOT_SHA256[sector],
        "primary_certificate_sha256": PINS[sector][1],
        "rhs_certificate_sha256": rhs_sha,
        "rhs_point_sha256": cert["buffers"]["lift-rhs"]["sha256"],
        "candidate_point_sha256": CANDIDATE_SHA256[sector],
        "lift_buffer": spec,
        "rational": {key: str(value) for key, value in values.items()},
        "display_approximate": {
            "energy_error": float(energy),
            "finite_lift_remote_action_charge": float(charge),
            "lift_norm": float(lift_norm),
        },
        "all_128000_physical_residual_coordinates_certified": True,
        "all_six_protected_components_retained": True,
        "physical_RHS_and_operator_errors_included_once": True,
        "finite_lift_certified": True,
        "finite_lift_action_charge_below_2e_minus10": charge < F("2e-10"),
        "old_v14_403_lift_reused": False,
        "whole_action_evaluated": False,
        "new_residual_evaluated": False,
        "whole_residual_acceptance_certified": False,
        "stationary_acceptance_met": False,
        "infinite_capacity_tail_closed": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-check", action="store_true")
    parser.add_argument("--root", type=Path)
    parser.add_argument("--rhs-root", type=Path)
    parser.add_argument("--output-root", type=Path)
    parser.add_argument("--sector", choices=tuple(PINS))
    parser.add_argument("--mode", choices=("produce", "replay"), default="produce")
    args = parser.parse_args()
    if args.self_check:
        print(json.dumps(self_check(), sort_keys=True))
        return
    assert all(value is not None for value in
               (args.root, args.rhs_root, args.output_root, args.sector))
    ctx = load(args.root, args.rhs_root, args.sector)
    args.output_root.mkdir(parents=True, exist_ok=True)
    cert_path = args.output_root / f"direct-middle-finite-lift-{args.sector}.json"
    if args.mode == "produce":
        Z = produce(ctx, args.sector)
        spec = write_buffer(args.output_root, args.sector,
                            "direct-middle-finite-lift", Z["values"], Z["bits"])
    else:
        previous = json.loads(cert_path.read_text())
        spec = previous["lift_buffer"]
        raw = (args.output_root / spec["file"]).read_bytes()
        assert len(raw) == spec["bytes"] and sha(raw) == spec["sha256"]
        Z = {"bits": spec["bits"], "values": integers(raw, spec["width"])}
        assert len(Z["values"]) == N
    result = certify(ctx, Z, args.sector, spec)
    serialized = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.mode == "produce":
        cert_path.write_text(serialized)
    else:
        assert cert_path.read_text() == serialized, "independent exact replay disagrees"
    print(json.dumps(result["display_approximate"], sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
