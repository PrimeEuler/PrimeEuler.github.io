#!/usr/bin/env python3
"""Apples-to-apples re-Ritz replay of the v13.988 graph-corrected P4 carrier.

The v13.988 payload contains the finite constrained graph correction X_R.
This diagnostic compares, in *the same infinite-residual metric*:

  baseline:  the unchanged G_B-normalized v13.974 carrier Z;
  corrected: the first graph-corrected span Z-X_R.

Each span is independently B-orthonormalized/re-Rayleigh-Ritzed through the
frozen 16001/16002 cutoff, then charged with the same audited explicit-remote
and far-tail residual machinery from the P4 basis certificate.

This avoids comparing the full infinite replay against intermediate/local
rho caps from v13.979.  No Xi, RH/GRH, source-energy, or convergence claim is
made.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh

from suzuki_kkt_remote_residual_certificate import sector_data
from suzuki_tail_P4_residual_basis_certificate import (
    apply_A_B,
    explicit_remote_gram,
    far_residual_bound,
    BETA_CAP,
    ARITH_RESERVE,
    EPS_SOURCE,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "p4_graph_corrected_reritz_result.json"
MOAT = 0.08


def canonical_signs(Q: np.ndarray) -> np.ndarray:
    signs = np.ones(Q.shape[1])
    for j in range(Q.shape[1]):
        i = int(np.argmax(np.abs(Q[:, j])))
        if Q[i, j] < 0:
            signs[j] = -1.0
    return signs


def reritz_metrics(sector: str, modes: np.ndarray, W: np.ndarray) -> dict:
    AW, BW = apply_A_B(modes, W, sector)
    G = (W.T @ BW + BW.T @ W) / 2.0
    H = (W.T @ AW + AW.T @ W) / 2.0

    geig = np.linalg.eigvalsh(G)
    if geig[0] <= 0:
        raise RuntimeError((sector, "B Gram is not positive", geig))

    theta, V = eigh(H, G, check_finite=False)
    raw = W @ V
    signs = canonical_signs(raw)

    Z = raw * signs[None, :]
    AZ = (AW @ V) * signs[None, :]
    BZ = (BW @ V) * signs[None, :]

    finite_R = AZ - BZ * theta[None, :]
    finite_G = finite_R.T @ finite_R
    finite_G = (finite_G + finite_G.T) / 2.0
    finite_residual = math.sqrt(
        max(0.0, float(np.linalg.eigvalsh(finite_G)[-1]))
    )

    remote_G = explicit_remote_gram(sector, modes, Z, theta)
    remote_G = (remote_G + remote_G.T) / 2.0
    point_G = (finite_G + remote_G)
    point_G = (point_G + point_G.T) / 2.0

    remote_residual = math.sqrt(
        max(0.0, float(np.linalg.eigvalsh(remote_G)[-1]))
    )
    point_residual = math.sqrt(
        max(0.0, float(np.linalg.eigvalsh(point_G)[-1]))
    )
    far = far_residual_bound(sector, modes, Z, theta)

    euclidean_cap = (
        point_residual
        + far
        + ARITH_RESERVE
        + EPS_SOURCE / math.sqrt(BETA_CAP[sector])
    )
    transformed_cap = euclidean_cap / math.sqrt(BETA_CAP[sector])
    sin_cap = transformed_cap / MOAT

    return {
        "pre_reritz_B_gram_eigenvalues": [float(x) for x in geig],
        "reritz_values": [float(x) for x in theta],
        "reritz_B_orthogonality_defect": float(
            np.linalg.norm(Z.T @ BZ - np.eye(4), 2)
        ),
        "finite_residual_operator": float(finite_residual),
        "explicit_remote_residual_operator": float(remote_residual),
        "point_total_residual_operator": float(point_residual),
        "far_residual_bound": float(far),
        "total_euclidean_residual_cap": float(euclidean_cap),
        "transformed_residual_cap": float(transformed_cap),
        "moat_only_sin_theta_cap": float(sin_cap),
        "moat_only_angle_deg_cap": (
            float(math.degrees(math.asin(sin_cap)))
            if sin_cap < 1.0 else None
        ),
    }


def one_sector(sector: str) -> dict:
    d = sector_data(sector)
    if "XR" not in d:
        raise FileNotFoundError(f"{sector}: v13.988 X_R payload is missing")

    modes = np.asarray(d["modes"], dtype=int)
    Z0 = np.asarray(d["Z"], dtype=float)
    XR = np.asarray(d["XR"], dtype=float)

    baseline = reritz_metrics(sector, modes, Z0)
    corrected = reritz_metrics(sector, modes, Z0 - XR)

    def ratio(key: str) -> float:
        return float(corrected[key] / baseline[key])

    return {
        "sector": sector,
        "modes": int(len(modes)),
        "last_mode": int(modes[-1]),
        "graph_correction_2norm": float(np.linalg.norm(XR, 2)),
        "baseline": baseline,
        "corrected": corrected,
        "ratios_corrected_over_baseline": {
            "finite_residual_operator": ratio("finite_residual_operator"),
            "explicit_remote_residual_operator": ratio(
                "explicit_remote_residual_operator"
            ),
            "point_total_residual_operator": ratio(
                "point_total_residual_operator"
            ),
            "far_residual_bound": ratio("far_residual_bound"),
            "transformed_residual_cap": ratio("transformed_residual_cap"),
        },
    }


def main() -> None:
    rows = [one_sector("even-v"), one_sector("odd-v")]
    out = {row["sector"]: row for row in rows}
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("v13.988 graph-corrected P4 apples-to-apples re-Ritz replay")
    for row in rows:
        print("\nsector =", row["sector"])
        print("modes =", row["modes"], "last_mode =", row["last_mode"])
        print("graph_correction_2norm =", row["graph_correction_2norm"])
        for label in ("baseline", "corrected"):
            print("\n", label)
            for key, value in row[label].items():
                print(key, "=", value)
        print("\n corrected/baseline ratios")
        for key, value in row["ratios_corrected_over_baseline"].items():
            print(key, "=", value)

    print("\nwrote", OUT)
    print(
        "GUARDRAIL: same-metric replay only; no Xi, RH/GRH, source-energy, "
        "or a->infinity claim follows."
    )


if __name__ == "__main__":
    main()
