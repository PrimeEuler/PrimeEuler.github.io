#!/usr/bin/env python3
"""Full replay of the v13.990 remote-tail moment cancellation on the M3 carrier.

This gate starts from the landed v13.988 graph-correction payload, reconstructs
the v13.996 M3 shell-extended/re-Ritzed carrier, appends the v13.990 finite
constant tail chosen to cancel the exact signed 1/n residual moment at the
current Ritz values, and then performs the operation that matters:

  * B-orthonormalize / Rayleigh-Ritz the moment-cancelled span again;
  * recompute the finite residual;
  * recompute the explicit remote residual through 2,000,000;
  * recompute the analytic far-tail bound;
  * recompute the *post-Ritz* leading 1/n moment.

The purpose is to test whether the exact pre-Ritz cancellation survives the
required re-Ritz step.  If the post-Ritz leading moment is nonzero, v13.990's
construction remains a valid fixed-theta cancellation, but the next carrier
must be made self-consistent (post-Ritz correction / fixed-point update)
before a fresh KKT/Feshbach payload is proof-grade.

No Xi, RH/GRH, source-energy, or a->infinity claim is made here.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import (
    pole_vector,
    z_source_faithful,
)
from suzuki_kkt_remote_residual_certificate import sector_data
from suzuki_p4_graph_remote_shell_extension import reritz_span, metrics
from suzuki_tail_P4_residual_basis_certificate import (
    solve_graph_shell,
    second_stage_ritz,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "p4_moment_cancelled_reritz_result.json"

M3 = {"even-v": 24001, "odd-v": 24002}
# Keep the replay tractable while giving the finite constant correction a
# substantial shell.  This extends M3 by 4000 same-parity modes.
M4 = {"even-v": 32001, "odd-v": 32002}


def leading_vector(sector: str, modes: np.ndarray, theta: np.ndarray, Z: np.ndarray):
    """Exact signed 1/n coefficient of A Z - B Z diag(theta) in remote rows."""
    z = z_source_faithful(modes)
    p, alpha = pole_vector(modes, sector)
    g = math.cosh(0.5) if sector == "even-v" else math.sinh(0.5)
    return (
        -(2.0 / math.pi) * (z @ Z)
        + alpha * (4.0 * g / math.pi) * (p @ Z)
        + np.sum(Z, axis=0) * theta
    )


def finite_extension_amplitudes(
    sector: str,
    modes: np.ndarray,
    theta: np.ndarray,
    Z: np.ndarray,
    new_modes: np.ndarray,
):
    """v13.990 constant-shell amplitudes cancelling L_theta columnwise."""
    lead = leading_vector(sector, modes, theta, Z)

    zt = z_source_faithful(new_modes)
    pt, alpha = pole_vector(new_modes, sector)
    g = math.cosh(0.5) if sector == "even-v" else math.sinh(0.5)

    common = (
        -(2.0 / math.pi) * float(np.sum(zt))
        + alpha * (4.0 * g / math.pi) * float(np.sum(pt))
    )
    denom = common + theta * float(len(new_modes))
    if np.min(np.abs(denom)) < 1.0e-8:
        raise RuntimeError((sector, "moment-cancellation denominator too small", denom))

    c = -lead / denom
    return lead, denom, c


def one_sector(sector: str):
    d = sector_data(sector)
    if "XR" not in d:
        raise FileNotFoundError(f"{sector}: v13.988 X_R payload is missing")

    # ----- Reconstruct the v13.996 M3 carrier -----
    modes2 = np.asarray(d["modes"], dtype=int)
    Z0 = np.asarray(d["Z"], dtype=float)
    XR = np.asarray(d["XR"], dtype=float)

    theta2, Z2, AZ2, BZ2 = reritz_span(sector, modes2, Z0 - XR)

    shell3 = np.arange(int(modes2[-1]) + 2, M3[sector] + 1, 2, dtype=int)
    tails3 = [
        solve_graph_shell(
            modes2,
            Z2[:, j],
            sector,
            float(theta2[j]),
            shell3,
        )
        for j in range(4)
    ]
    Y3 = np.column_stack(tails3)

    modes3 = np.concatenate([modes2, shell3])
    X3 = np.vstack([Z2, -Y3])
    theta3, Z3, AZ3, BZ3, _, defect3 = second_stage_ritz(sector, modes3, X3)
    m3 = metrics(sector, modes3, theta3, Z3, AZ3, BZ3)

    # ----- Apply the v13.990 fixed-theta moment cancellation -----
    shell4 = np.arange(int(modes3[-1]) + 2, M4[sector] + 1, 2, dtype=int)
    lead3, denom, c = finite_extension_amplitudes(
        sector, modes3, theta3, Z3, shell4
    )
    Y4 = np.ones((len(shell4), 1), dtype=float) @ c[None, :]

    modes4 = np.concatenate([modes3, shell4])
    X4 = np.vstack([Z3, Y4])

    # At the *old* theta3 values this should cancel to roundoff exactly.
    pre_reritz_lead = leading_vector(sector, modes4, theta3, X4)

    # ----- The decisive test: re-Ritz the corrected span -----
    theta4, Z4, AZ4, BZ4, _, defect4 = second_stage_ritz(sector, modes4, X4)
    m4 = metrics(sector, modes4, theta4, Z4, AZ4, BZ4)
    post_reritz_lead = leading_vector(sector, modes4, theta4, Z4)

    if float(np.max(np.abs(theta4))) >= 0.02:
        ritz_window_status = "FAIL"
    else:
        ritz_window_status = "PASS"

    def ratio(key):
        a = float(m3[key])
        b = float(m4[key])
        return b / a if a != 0.0 else None

    return {
        "sector": sector,
        "M3": {
            "modes": int(len(modes3)),
            "last_mode": int(modes3[-1]),
            "theta": [float(x) for x in theta3],
            "B_orthogonality_defect": float(defect3),
            "lead_vector": [float(x) for x in lead3],
            "lead_2norm": float(np.linalg.norm(lead3)),
            "metrics": m3,
        },
        "moment_extension": {
            "start_mode": int(shell4[0]),
            "end_mode": int(shell4[-1]),
            "dimension": int(len(shell4)),
            "denominator": [float(x) for x in denom],
            "amplitudes": [float(x) for x in c],
            "tail_coefficient_2norms": [
                float(abs(cj) * math.sqrt(len(shell4))) for cj in c
            ],
            "pre_reritz_lead_vector": [float(x) for x in pre_reritz_lead],
            "pre_reritz_lead_2norm": float(np.linalg.norm(pre_reritz_lead)),
        },
        "M4_reritz": {
            "modes": int(len(modes4)),
            "last_mode": int(modes4[-1]),
            "theta": [float(x) for x in theta4],
            "ritz_window_status": ritz_window_status,
            "B_orthogonality_defect": float(defect4),
            "post_reritz_lead_vector": [float(x) for x in post_reritz_lead],
            "post_reritz_lead_2norm": float(np.linalg.norm(post_reritz_lead)),
            "metrics": m4,
        },
        "ratios_M4_over_M3": {
            "finite_residual_operator": ratio("finite_residual_operator"),
            "explicit_remote_residual_operator": ratio(
                "explicit_remote_residual_operator"
            ),
            "point_total_residual_operator": ratio("point_total_residual_operator"),
            "far_residual_bound": ratio("far_residual_bound"),
            "transformed_residual_cap": ratio("transformed_residual_cap"),
        },
        "gate": {
            "pre_reritz_moment_cancelled": bool(
                np.linalg.norm(pre_reritz_lead) < 1.0e-10
            ),
            "post_reritz_moment_still_cancelled": bool(
                np.linalg.norm(post_reritz_lead) < 1.0e-8
            ),
            "ritz_values_inside_0p02": bool(np.max(np.abs(theta4)) < 0.02),
        },
    }


def main():
    rows = [one_sector("even-v"), one_sector("odd-v")]
    out = {row["sector"]: row for row in rows}
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("v13.990 M3 -> moment-cancelled M4 re-Ritz replay")
    for row in rows:
        print("\nsector =", row["sector"])
        print("M3 theta =", row["M3"]["theta"])
        print("M3 lead 2-norm =", row["M3"]["lead_2norm"])
        print("tail amplitudes =", row["moment_extension"]["amplitudes"])
        print(
            "pre-reritz lead 2-norm =",
            row["moment_extension"]["pre_reritz_lead_2norm"],
        )
        print("M4 theta =", row["M4_reritz"]["theta"])
        print(
            "post-reritz lead 2-norm =",
            row["M4_reritz"]["post_reritz_lead_2norm"],
        )
        print("gate =", row["gate"])
        print("M4/M3 residual ratios =", row["ratios_M4_over_M3"])
        print(
            "M3 transformed residual =",
            row["M3"]["metrics"]["transformed_residual_cap"],
        )
        print(
            "M4 transformed residual =",
            row["M4_reritz"]["metrics"]["transformed_residual_cap"],
        )
        print(
            "M3 far bound =",
            row["M3"]["metrics"]["far_residual_bound"],
        )
        print(
            "M4 far bound =",
            row["M4_reritz"]["metrics"]["far_residual_bound"],
        )

    print("\nwrote", OUT)
    print(
        "GUARDRAIL: carrier replay only.  A fresh KKT/Feshbach payload is "
        "proof-grade only after this post-Ritz gate is understood."
    )


if __name__ == "__main__":
    main()
