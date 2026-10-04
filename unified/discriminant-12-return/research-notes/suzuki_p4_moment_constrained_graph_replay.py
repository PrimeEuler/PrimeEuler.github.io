#!/usr/bin/env python3
"""Moment-constrained graph-shell replay for the M3 carrier.

For each M3 Ritz column q with Ritz value theta, choose a fresh remote-shell
tail x_tail=-y.  The ordinary graph solve enforces the shell eigen-equation

    D_theta y = R_theta^T q.

We add the exact leading-moment constraint

    ell_theta^T y = L_theta(q),

so the full extended vector q-y has zero signed 1/n residual moment while
remaining as close as possible, in the D_theta quadratic form, to the graph
solution.  The KKT equations are

    D_theta y + ell_theta mu = R_theta^T q,
    ell_theta^T y = L_theta(q).

Because D_theta is the same structured shell operator already used by the
audited graph extension, this is a one-constraint rank-one correction of the
unconstrained graph solve.

After all four constrained shell solves we re-Rayleigh-Ritz the span and run
the same finite + explicit-remote + far residual metric as v13.996.

Numerical gate only; no Xi, RH/GRH, source-energy, or convergence claim.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data,
    ldl_solve,
    offdiag,
    pole_vector,
    structured_ldl,
    z_source_faithful,
)
from suzuki_p4_graph_remote_shell_extension import metrics
from suzuki_p4_self_consistent_moment_reritz import build_m3
from suzuki_tail_P4_residual_basis_certificate import second_stage_ritz

HERE = Path(__file__).resolve().parent
OUT = HERE / "p4_moment_constrained_graph_result.json"

M4 = {"even-v": 32001, "odd-v": 32002}


def lead_base(sector: str, modes: np.ndarray) -> np.ndarray:
    z = z_source_faithful(modes)
    p, alpha = pole_vector(modes, sector)
    g = math.cosh(0.5) if sector == "even-v" else math.sinh(0.5)
    return (
        -(2.0 / math.pi) * z
        + alpha * (4.0 * g / math.pi) * p
    )


def constrained_graph_shell(old_modes, q, sector, theta, new_modes):
    theta = float(theta)

    z_old, _ = endpoint_data(old_modes, sign=-1, rho=theta)
    z_new, d_new = endpoint_data(new_modes, sign=-1, rho=theta)
    R0 = offdiag(old_modes, new_modes, z_old, z_new)

    Lfac, Dfac = structured_ldl(new_modes, z_new, d_new)

    all_modes = np.concatenate([old_modes, new_modes])
    p, alpha = pole_vector(all_modes, sector)
    p_old = p[: len(old_modes)]
    p_new = p[len(old_modes) :]

    rhs = R0.T @ q + alpha * p_new * float(p_old @ q)

    yp = ldl_solve(Lfac, Dfac, p_new)
    pole_den = 1.0 + alpha * float(p_new @ yp)
    if pole_den <= 0:
        raise RuntimeError(("pole denominator failed", sector, theta, pole_den))

    def solve_D(v):
        x0 = ldl_solve(Lfac, Dfac, v)
        return x0 - alpha * yp * float(p_new @ x0) / pole_den

    y0 = solve_D(rhs)

    ell_old = lead_base(sector, old_modes) + theta
    ell_new = lead_base(sector, new_modes) + theta
    target = float(ell_old @ q)

    v = solve_D(ell_new)
    denom = float(ell_new @ v)
    if abs(denom) < 1.0e-12:
        raise RuntimeError(("moment KKT denominator too small", sector, theta, denom))

    mu = (float(ell_new @ y0) - target) / denom
    y = y0 - v * mu

    constraint_error = float(ell_new @ y - target)
    shell_residual = rhs - (
        # D_theta y, reconstructed from the KKT identity to avoid another
        # dense shell application:
        rhs - ell_new * mu
    )
    # shell_residual == ell_new * mu algebraically.
    shell_residual_norm = float(np.linalg.norm(ell_new * mu))

    return y, {
        "theta": theta,
        "target_lead": target,
        "unconstrained_tail_lead": float(ell_new @ y0),
        "denominator": denom,
        "mu": float(mu),
        "constraint_error": constraint_error,
        "shell_residual_norm_from_multiplier": shell_residual_norm,
        "unconstrained_tail_2norm": float(np.linalg.norm(y0)),
        "constrained_tail_2norm": float(np.linalg.norm(y)),
        "correction_2norm": float(np.linalg.norm(y - y0)),
    }


def post_lead(sector, modes, theta, Z):
    return (
        lead_base(sector, modes) @ Z
        + np.sum(Z, axis=0) * theta
    )


def one_sector(sector: str):
    modes3, theta3, Z3, AZ3, BZ3 = build_m3(sector)
    m3 = metrics(sector, modes3, theta3, Z3, AZ3, BZ3)

    shell4 = np.arange(int(modes3[-1]) + 2, M4[sector] + 1, 2, dtype=int)
    tails = []
    diagnostics = []
    for j in range(4):
        y, row = constrained_graph_shell(
            modes3,
            Z3[:, j],
            sector,
            theta3[j],
            shell4,
        )
        tails.append(y)
        diagnostics.append(row)

    Y = np.column_stack(tails)
    modes4 = np.concatenate([modes3, shell4])
    X4 = np.vstack([Z3, -Y])

    pre = post_lead(sector, modes4, theta3, X4)

    theta4, Z4, AZ4, BZ4, _, defect4 = second_stage_ritz(sector, modes4, X4)
    post = post_lead(sector, modes4, theta4, Z4)
    m4 = metrics(sector, modes4, theta4, Z4, AZ4, BZ4)

    return {
        "sector": sector,
        "M3": {
            "theta": [float(x) for x in theta3],
            "lead_2norm": float(np.linalg.norm(post_lead(sector, modes3, theta3, Z3))),
            "metrics": m3,
        },
        "constrained_shell": {
            "start_mode": int(shell4[0]),
            "end_mode": int(shell4[-1]),
            "dimension": int(len(shell4)),
            "columns": diagnostics,
            "pre_reritz_lead_vector": [float(x) for x in pre],
            "pre_reritz_lead_2norm": float(np.linalg.norm(pre)),
        },
        "M4_reritz": {
            "theta": [float(x) for x in theta4],
            "inside_0p02": bool(np.max(np.abs(theta4)) < 0.02),
            "B_orthogonality_defect": float(defect4),
            "post_reritz_lead_vector": [float(x) for x in post],
            "post_reritz_lead_2norm": float(np.linalg.norm(post)),
            "metrics": m4,
        },
        "gate": {
            "pre_reritz_moment_closed": bool(np.linalg.norm(pre) < 1.0e-8),
            "post_reritz_moment_closed": bool(np.linalg.norm(post) < 1.0e-8),
            "ritz_values_inside_0p02": bool(np.max(np.abs(theta4)) < 0.02),
            "transformed_residual_below_M3": bool(
                m4["transformed_residual_cap"] < m3["transformed_residual_cap"]
            ),
        },
    }


def main():
    rows = [one_sector("even-v"), one_sector("odd-v")]
    out = {row["sector"]: row for row in rows}
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("M3 -> M4 moment-constrained graph-shell replay")
    for row in rows:
        print("\nsector =", row["sector"])
        print("M3 theta =", row["M3"]["theta"])
        for j, col in enumerate(row["constrained_shell"]["columns"]):
            print("col", j, "=", col)
        print(
            "pre-reritz lead 2-norm =",
            row["constrained_shell"]["pre_reritz_lead_2norm"],
        )
        print("M4 theta =", row["M4_reritz"]["theta"])
        print(
            "post-reritz lead 2-norm =",
            row["M4_reritz"]["post_reritz_lead_2norm"],
        )
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
        print("gate =", row["gate"])

    print("\nwrote", OUT)
    print(
        "GUARDRAIL: carrier gate only; no KKT/Feshbach rebuild is promoted "
        "unless the carrier geometry and residuals remain certifiable."
    )


if __name__ == "__main__":
    main()
