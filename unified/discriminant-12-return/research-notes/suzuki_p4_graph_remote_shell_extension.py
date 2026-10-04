#!/usr/bin/env python3
"""Remote-shell completion test for the v13.988 graph-corrected P4 carrier.

The same-metric replay shows that Z-X_R nearly annihilates the residual inside
the frozen 16001/16002 window but leaves the infinite residual dominated by
omitted rows.  This diagnostic attacks exactly that obstruction:

  1. re-Ritz the v13.988 corrected span Z-X_R at M2=16001/16002;
  2. extend each of the four re-Ritz columns through a fresh structured
     generalized-eigenvector graph solve to M3=24001/24002;
  3. re-Ritz the M3 span;
  4. charge the remaining infinite residual using the same audited explicit
     remote and far-tail machinery.

This is a numerical gate only.  It does not freeze a new carrier and makes no
Xi, RH/GRH, source-energy, or convergence claim.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh

from suzuki_kkt_remote_residual_certificate import sector_data
from suzuki_endpoint_M3999_midpoint_effective_core import (
    z_source_faithful,
    pole_vector,
)
from suzuki_tail_P4_residual_basis_certificate import (
    apply_A_B,
    solve_graph_shell,
    second_stage_ritz,
    explicit_remote_gram,
    far_residual_bound,
    BETA_CAP,
    ARITH_RESERVE,
    EPS_SOURCE,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "p4_graph_remote_shell_extension_result.json"
M3 = {"even-v": 24001, "odd-v": 24002}
MOAT = 0.08


def canonical_signs(Q: np.ndarray) -> np.ndarray:
    signs = np.ones(Q.shape[1])
    for j in range(Q.shape[1]):
        i = int(np.argmax(np.abs(Q[:, j])))
        if Q[i, j] < 0:
            signs[j] = -1.0
    return signs


def far_leading_data(sector, modes, theta, Z):
    """Exact signed 1/n coefficient of (A Z - B Z Theta) in remote rows."""
    z = z_source_faithful(modes)
    p, alpha = pole_vector(modes, sector)
    g = math.cosh(0.5) if sector == "even-v" else math.sinh(0.5)

    s0 = np.sum(Z, axis=0)
    aconst = (
        -(2.0 / math.pi) * (z @ Z)
        + alpha * (4.0 * g / math.pi) * (p @ Z)
    )
    lead = aconst + s0 * theta

    theta_cancel = np.full(4, np.nan)
    mask = np.abs(s0) > 1.0e-14
    theta_cancel[mask] = -aconst[mask] / s0[mask]

    N = 2_000_001.0 if sector == "even-v" else 2_000_002.0
    S2 = N**(-2) + 1.0 / (2.0 * N)
    lead_only_far = float(np.linalg.norm(lead) * math.sqrt(S2))

    return {
        "sum_coefficients": [float(x) for x in s0],
        "lead_vector": [float(x) for x in lead],
        "lead_2norm": float(np.linalg.norm(lead)),
        "theta_canceling_lead": [float(x) for x in theta_cancel],
        "theta_cancel_shift": [float(x) for x in (theta_cancel - theta)],
        "lead_only_far_bound_at_2m": lead_only_far,
    }


def metrics(sector, modes, theta, Z, AZ, BZ):
    finite_R = AZ - BZ * theta[None, :]
    finite_G = finite_R.T @ finite_R
    finite_G = (finite_G + finite_G.T) / 2.0

    remote_G = explicit_remote_gram(sector, modes, Z, theta)
    remote_G = (remote_G + remote_G.T) / 2.0
    point_G = (finite_G + remote_G)
    point_G = (point_G + point_G.T) / 2.0

    finite = math.sqrt(max(0.0, float(np.linalg.eigvalsh(finite_G)[-1])))
    remote = math.sqrt(max(0.0, float(np.linalg.eigvalsh(remote_G)[-1])))
    point = math.sqrt(max(0.0, float(np.linalg.eigvalsh(point_G)[-1])))
    far = far_residual_bound(sector, modes, Z, theta)

    euclidean = (
        point
        + far
        + ARITH_RESERVE
        + EPS_SOURCE / math.sqrt(BETA_CAP[sector])
    )
    transformed = euclidean / math.sqrt(BETA_CAP[sector])
    sin_cap = transformed / MOAT

    leading = far_leading_data(sector, modes, theta, Z)

    return {
        "modes": int(len(modes)),
        "last_mode": int(modes[-1]),
        "ritz_values": [float(x) for x in theta],
        "B_orthogonality_defect": float(
            np.linalg.norm(Z.T @ BZ - np.eye(4), 2)
        ),
        "finite_residual_operator": float(finite),
        "explicit_remote_residual_operator": float(remote),
        "point_total_residual_operator": float(point),
        "far_residual_bound": float(far),
        "far_leading_asymptotic": leading,
        "lead_fraction_of_far_bound": float(
            leading["lead_only_far_bound_at_2m"] / far
        ),
        "total_euclidean_residual_cap": float(euclidean),
        "transformed_residual_cap": float(transformed),
        "moat_only_sin_theta_cap": float(sin_cap),
        "moat_only_angle_deg_cap": (
            float(math.degrees(math.asin(sin_cap)))
            if sin_cap < 1.0 else None
        ),
    }


def reritz_span(sector, modes, W):
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
    return theta, Z, AZ, BZ


def one_sector(sector: str):
    d = sector_data(sector)
    if "XR" not in d:
        raise FileNotFoundError(f"{sector}: v13.988 X_R payload is missing")

    modes2 = np.asarray(d["modes"], dtype=int)
    Z0 = np.asarray(d["Z"], dtype=float)
    XR = np.asarray(d["XR"], dtype=float)

    # M2 graph-corrected/re-Ritzed carrier.
    theta2, Z2, AZ2, BZ2 = reritz_span(sector, modes2, Z0 - XR)
    m2 = metrics(sector, modes2, theta2, Z2, AZ2, BZ2)

    new_modes = np.arange(int(modes2[-1]) + 2, M3[sector] + 1, 2, dtype=int)
    tails = []
    for j in range(4):
        tails.append(
            solve_graph_shell(
                modes2,
                Z2[:, j],
                sector,
                float(theta2[j]),
                new_modes,
            )
        )
    Y = np.column_stack(tails)

    modes3 = np.concatenate([modes2, new_modes])
    X = np.vstack([Z2, -Y])

    theta3, Z3, AZ3, BZ3, _, defect3 = second_stage_ritz(
        sector, modes3, X
    )
    m3 = metrics(sector, modes3, theta3, Z3, AZ3, BZ3)
    # second_stage_ritz already reports this; keep a replay check.
    m3["second_stage_reported_B_defect"] = float(defect3)

    def ratio(key):
        return float(m3[key] / m2[key])

    return {
        "sector": sector,
        "shell_start_mode": int(new_modes[0]),
        "shell_end_mode": int(new_modes[-1]),
        "shell_dimension": int(len(new_modes)),
        "shell_extension_2norm": float(np.linalg.norm(Y, 2)),
        "M2_corrected": m2,
        "M3_shell_extended": m3,
        "ratios_M3_over_M2": {
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


def main():
    rows = [one_sector("even-v"), one_sector("odd-v")]
    out = {row["sector"]: row for row in rows}
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("P4 graph-corrected remote-shell completion replay")
    for row in rows:
        print("\nsector =", row["sector"])
        print(
            "shell =",
            row["shell_start_mode"],
            "..",
            row["shell_end_mode"],
            "dimension =",
            row["shell_dimension"],
        )
        print("shell_extension_2norm =", row["shell_extension_2norm"])
        for label in ("M2_corrected", "M3_shell_extended"):
            print("\n", label)
            for key, value in row[label].items():
                print(key, "=", value)
        print("\n M3/M2 ratios")
        for key, value in row["ratios_M3_over_M2"].items():
            print(key, "=", value)

    print("\nwrote", OUT)
    print(
        "GUARDRAIL: remote-shell diagnostic only; no Xi, RH/GRH, "
        "source-energy, or a->infinity claim follows."
    )


if __name__ == "__main__":
    main()
