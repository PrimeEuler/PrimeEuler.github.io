#!/usr/bin/env python3
"""Re-Ritz replay of the v13.988 graph-corrected P4 carrier.

The v13.988 residual-cross payload contains X_R satisfying, up to its
separately certified KKT residual,

    B^(1/2) X_R ~= Dhat^{-1} K,

so v13.979 identifies Z-X_R as the first graph-corrected carrier in original
coordinates.  This diagnostic does *not* perform a second KKT solve.  It:

  1. loads the unchanged G_B-normalized v13.974 carrier Z and v13.988 X_R;
  2. forms W = Z-X_R;
  3. re-orthonormalizes/re-Rayleigh-Ritzes the four-dimensional span in the
     exact finite A,B matrices through the frozen 16001/16002 cutoff;
  4. evaluates the finite residual operator norm;
  5. reuses the audited explicit-remote + far-tail machinery to bound the
     infinite residual of the re-Ritzed carrier;
  6. reports the transformed B^{-1/2} residual and the corresponding 0.08
     moat-only subspace-angle diagnostic.

This is a replay/diagnostic of the landed payload.  It makes no Xi, RH/GRH,
source-energy, or convergence claim.
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

# Public pre-correction transformed residual caps used by v13.979.
OLD_RHO_CAP = {
    "even-v": 0.00580,
    "odd-v": 0.00880,
}

# Ideal exact-graph a-priori bounds from v13.979.  The landed X_R is only
# residual-certified, so these are comparison targets, not assertions.
IDEAL_GRAPH_RHO_TARGET = {
    "even-v": 3.778e-5,
    "odd-v": 1.025e-3,
}

MOAT = 0.08


def canonical_signs(Q: np.ndarray) -> np.ndarray:
    signs = np.ones(Q.shape[1])
    for j in range(Q.shape[1]):
        i = int(np.argmax(np.abs(Q[:, j])))
        if Q[i, j] < 0:
            signs[j] = -1.0
    return signs


def one_sector(sector: str) -> dict:
    d = sector_data(sector)
    if "XR" not in d:
        raise FileNotFoundError(f"{sector}: v13.988 X_R payload is missing")

    modes = np.asarray(d["modes"], dtype=int)
    Z0 = np.asarray(d["Z"], dtype=float)
    XR = np.asarray(d["XR"], dtype=float)

    # v13.979/v13.988 first graph-corrected carrier in original coordinates.
    W = Z0 - XR

    AW, BW = apply_A_B(modes, W, sector)
    G = (W.T @ BW + BW.T @ W) / 2.0
    H = (W.T @ AW + AW.T @ W) / 2.0

    geig = np.linalg.eigvalsh(G)
    if geig[0] <= 0:
        raise RuntimeError((sector, "graph-corrected B Gram is not positive", geig))

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
    point_G = (finite_G + remote_G)
    point_G = (point_G + point_G.T) / 2.0
    remote_residual = math.sqrt(
        max(0.0, float(np.linalg.eigvalsh(remote_G)[-1]))
    )
    point_residual = math.sqrt(
        max(0.0, float(np.linalg.eigvalsh(point_G)[-1]))
    )

    far = far_residual_bound(sector, modes, Z, theta)

    # Same outward architecture as the audited P4 residual-basis certificate:
    # point operator norm + far Minkowski tail + arithmetic/source reserve.
    euclidean_cap = (
        point_residual
        + far
        + ARITH_RESERVE
        + EPS_SOURCE / math.sqrt(BETA_CAP[sector])
    )
    transformed_cap = euclidean_cap / math.sqrt(BETA_CAP[sector])

    borth = float(np.linalg.norm(Z.T @ BZ - np.eye(4), 2))
    sin_cap = transformed_cap / MOAT

    return {
        "sector": sector,
        "modes": int(len(modes)),
        "last_mode": int(modes[-1]),
        "graph_correction_2norm": float(np.linalg.norm(XR, 2)),
        "pre_reritz_B_gram_eigenvalues": [float(x) for x in geig],
        "reritz_values": [float(x) for x in theta],
        "reritz_B_orthogonality_defect": borth,
        "finite_residual_operator": finite_residual,
        "explicit_remote_residual_operator": remote_residual,
        "point_total_residual_operator": point_residual,
        "far_residual_bound": float(far),
        "total_euclidean_residual_cap": float(euclidean_cap),
        "transformed_residual_cap": float(transformed_cap),
        "old_public_transformed_residual_cap": OLD_RHO_CAP[sector],
        "contraction_ratio_vs_old_public_cap": float(
            transformed_cap / OLD_RHO_CAP[sector]
        ),
        "v13_979_ideal_exact_graph_target": IDEAL_GRAPH_RHO_TARGET[sector],
        "ratio_vs_ideal_exact_graph_target": float(
            transformed_cap / IDEAL_GRAPH_RHO_TARGET[sector]
        ),
        "moat_only_sin_theta_cap": float(sin_cap),
        "moat_only_angle_deg_cap": (
            float(math.degrees(math.asin(sin_cap)))
            if sin_cap < 1.0 else None
        ),
    }


def main() -> None:
    rows = [one_sector("even-v"), one_sector("odd-v")]
    out = {row["sector"]: row for row in rows}
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("v13.988 graph-corrected P4 re-Ritz replay")
    for row in rows:
        print("\nsector =", row["sector"])
        for key, value in row.items():
            if key != "sector":
                print(key, "=", value)

    print("\nwrote", OUT)
    print(
        "GUARDRAIL: replay/diagnostic only; no Xi, RH/GRH, source-energy, "
        "or a->infinity claim follows."
    )


if __name__ == "__main__":
    main()
