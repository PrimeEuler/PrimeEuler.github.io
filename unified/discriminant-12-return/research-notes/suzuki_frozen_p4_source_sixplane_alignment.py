#!/usr/bin/env python3
"""Compare the frozen P4 carrier with the high-precision source-active resonance plane.

The theorem-scale capacity architecture needs a fixed six-plane:
  two low source-active coordinate directions + four resonance directions.

Rather than regenerate a new basis at M3999/4000, this gate asks whether the
already-frozen/audited four-column P4 carrier can serve as those four resonance
directions.

At the source-faithful N=192 checkpoint:
  * build the high-precision normalized-resonance four-plane from the rho=0
    producer;
  * restrict the frozen p4_payload Z carrier to the same tail modes;
  * compare principal angles;
  * build the six-plane from the two low coordinates plus frozen-P4 tail;
  * eliminate its Euclidean orthogonal complement at high precision;
  * compare the resulting capacities with the ideal high-precision six-plane
    capacity from the v13.1000 producer.

Diagnostic only: finite N=192.  This tests a basis-freezing choice; it does not
certify the M3999/4000 complement or infinite tail.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from suzuki_form_core_bulk_subtracted_resonance import (
    parity_components,
    resonance_basis,
    source_overlap,
)

HERE = Path(__file__).resolve().parent
P4ROOT = HERE / "p4_payload"
OUT = HERE / "frozen_p4_source_sixplane_alignment_result.json"


def mp_from_np(A):
    A = np.asarray(A)
    return mp.matrix([[mp.mpf(repr(float(A[i, j]))) for j in range(A.shape[1])]
                      for i in range(A.shape[0])])


def mp_vec(x):
    return mp.matrix([mp.mpf(repr(float(v))) for v in np.asarray(x).ravel()])


def principal_angles(Q1, Q2):
    s = np.linalg.svd(Q1.T @ Q2, compute_uv=False)
    s = np.clip(s, -1.0, 1.0)
    ang = np.degrees(np.arccos(s))
    return s, ang


def fixed_p4_tail_basis(sector: str, max_mode: int):
    root = P4ROOT / sector
    modes = np.load(root / "modes.npy").astype(int)
    Z = np.load(root / "Z.npy")

    mask = modes <= max_mode
    modes_cut = modes[mask]
    Zcut = Z[mask, :]

    # The P4 payload begins at mode 5/6, exactly the tail after the two low
    # source-active coordinates.
    q, r = np.linalg.qr(Zcut, mode="reduced")
    if np.min(np.abs(np.diag(r))) < 1.0e-12:
        raise RuntimeError((sector, "restricted frozen P4 lost rank", np.diag(r)))
    return modes_cut, q


def capacity_with_fixed_sixplane(max_mode: int, sector: str, Qtail: np.ndarray):
    ns, _, _, _, _, full = parity_components(max_mode, sector)
    n = len(ns)
    if Qtail.shape[0] != n - 2:
        raise RuntimeError((sector, Qtail.shape, n))

    # P = first two coordinates + fixed tail four-plane.
    P = np.zeros((n, 6), dtype=float)
    P[0, 0] = 1.0
    P[1, 1] = 1.0
    P[2:, 2:] = Qtail

    Qall, _ = np.linalg.qr(P, mode="complete")
    Qp = Qall[:, :6]
    Qq = Qall[:, 6:]

    Qp_mp = mp_from_np(Qp)
    Qq_mp = mp_from_np(Qq)

    A = full
    f = mp.matrix([source_overlap(k) for k in ns])

    App = Qp_mp.T * A * Qp_mp
    Ep = Qq_mp.T * A * Qp_mp
    D = Qq_mp.T * A * Qq_mp

    fp = Qp_mp.T * f
    fq = Qq_mp.T * f

    valsD, _ = mp.eigsy((D + D.T) / 2)
    if valsD[0] <= 0:
        return {
            "complement_positive": False,
            "complement_min": mp.nstr(valsD[0], 40),
        }

    Y = mp.lu_solve(D, Ep)
    yf = mp.lu_solve(D, fq)

    S = (App - Ep.T * Y)
    S = (S + S.T) / 2
    g = fp - Ep.T * yf
    h = (fq.T * yf)[0]

    valsS, _ = mp.eigsy(S)
    w = mp.lu_solve(S, g)
    r = (g.T * w)[0]
    G = h + r
    C = 1 / G

    return {
        "complement_positive": True,
        "complement_min": mp.nstr(valsD[0], 50),
        "complement_max": mp.nstr(valsD[-1], 50),
        "complement_condition": mp.nstr(valsD[-1] / valsD[0], 30),
        "S6_eigenvalues": [mp.nstr(valsS[j], 50) for j in range(6)],
        "h": mp.nstr(h, 50),
        "protected_energy": mp.nstr(r, 50),
        "energy": mp.nstr(G, 50),
        "capacity": mp.nstr(C, 50),
        "h_over_G": mp.nstr(h / G, 30),
    }


def one_sector(max_mode: int, sector: str):
    data = parity_components(max_mode, sector)
    ns = data[0]
    ideal = resonance_basis(data, max_mode, howmany=4, core_dim=2)

    modes_cut, frozen = fixed_p4_tail_basis(sector, max_mode)
    expected = np.array(ns[2:], dtype=int)
    if not np.array_equal(modes_cut, expected):
        raise RuntimeError((sector, "mode mismatch", modes_cut[:5], expected[:5]))

    s, angles = principal_angles(ideal, frozen)

    fixed_cap = capacity_with_fixed_sixplane(max_mode, sector, frozen)
    ideal_cap = capacity_with_fixed_sixplane(max_mode, sector, ideal)

    row = {
        "sector": sector,
        "max_mode": max_mode,
        "principal_cosines": [float(x) for x in s],
        "principal_angles_deg": [float(x) for x in angles],
        "max_principal_angle_deg": float(np.max(angles)),
        "frozen": fixed_cap,
        "ideal": ideal_cap,
    }

    if fixed_cap.get("complement_positive") and ideal_cap.get("complement_positive"):
        Cf = mp.mpf(fixed_cap["capacity"])
        Ci = mp.mpf(ideal_cap["capacity"])
        row["capacity_ratio_frozen_over_ideal"] = mp.nstr(Cf / Ci, 40)
        row["capacity_relative_difference"] = mp.nstr(abs(Cf - Ci) / abs(Ci), 30)

    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-mode", type=int, default=192)
    parser.add_argument("--dps", type=int, default=80)
    args = parser.parse_args()

    with mp.workdps(args.dps):
        rows = [one_sector(args.max_mode, s) for s in ("even-v", "odd-v")]
        out = {
            "max_mode": args.max_mode,
            "dps": args.dps,
            "rows": rows,
            "guardrail": (
                "Finite N=192 basis-freezing diagnostic only; no theorem-scale "
                "M3999/4000 or infinite-tail claim."
            ),
        }
        OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

        for row in rows:
            print("\nsector =", row["sector"])
            print("principal cosines =", row["principal_cosines"])
            print("principal angles deg =", row["principal_angles_deg"])
            print("max angle =", row["max_principal_angle_deg"])
            print("frozen =", row["frozen"])
            print("ideal =", row["ideal"])
            print(
                "capacity frozen/ideal =",
                row.get("capacity_ratio_frozen_over_ideal"),
            )
            print(
                "capacity relative difference =",
                row.get("capacity_relative_difference"),
            )

        print("\nwrote", OUT)
        print("GUARDRAIL:", out["guardrail"])


if __name__ == "__main__":
    main()
