#!/usr/bin/env python3
"""Self-consistent remote-moment cancellation for the M3 carrier.

The naive v13.990 construction cancels the leading 1/n residual moment at the
*old* Ritz values, then a subsequent re-Ritz changes the reduced operator and
can reintroduce the moment.

For a trial four-column span X define

    G = X^T B X,
    H = X^T A X,
    T = G^{-1} H.

If c0 is the row functional supplying the A-side 1/n coefficient and s is
the all-ones row, then the leading residual row is

    L(X) = c0^T X + (s^T X) T.

This quantity is basis-covariant: for X -> X V,

    L(XV) = L(X) V.

Therefore L(X)=0 is a *subspace-invariant* constraint and survives subsequent
B-orthonormalization and Rayleigh-Ritz rotation exactly.

We restrict X to the v13.989 M3 carrier plus one constant finite shell with
four amplitudes c=(c1,...,c4), and solve the resulting four nonlinear equations
L(X(c))=0.  The expensive A/B action is performed once on a five-column basis;
the nonlinear root iterations then use only 5x5 contractions.

This is a numerical gate.  No Xi, RH/GRH, source-energy, or convergence claim.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh
from scipy.optimize import root

from suzuki_endpoint_M3999_midpoint_effective_core import (
    pole_vector,
    z_source_faithful,
)
from suzuki_kkt_remote_residual_certificate import sector_data
from suzuki_p4_graph_remote_shell_extension import reritz_span, metrics
from suzuki_tail_P4_residual_basis_certificate import (
    apply_A_B,
    solve_graph_shell,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "p4_self_consistent_moment_reritz_result.json"

M3 = {"even-v": 24001, "odd-v": 24002}
M4 = {"even-v": 32001, "odd-v": 32002}


def canonical_signs(Q: np.ndarray) -> np.ndarray:
    signs = np.ones(Q.shape[1])
    for j in range(Q.shape[1]):
        i = int(np.argmax(np.abs(Q[:, j])))
        if Q[i, j] < 0:
            signs[j] = -1.0
    return signs


def lead_functional_vector(sector: str, modes: np.ndarray) -> np.ndarray:
    z = z_source_faithful(modes)
    p, alpha = pole_vector(modes, sector)
    g = math.cosh(0.5) if sector == "even-v" else math.sinh(0.5)
    return (
        -(2.0 / math.pi) * z
        + alpha * (4.0 * g / math.pi) * p
    )


def leading_row(
    sector: str,
    modes: np.ndarray,
    X: np.ndarray,
    T: np.ndarray,
) -> np.ndarray:
    ell = lead_functional_vector(sector, modes)
    return ell @ X + (np.sum(X, axis=0) @ T)


def build_m3(sector: str):
    d = sector_data(sector)
    if "XR" not in d:
        raise FileNotFoundError(f"{sector}: v13.988 X_R payload is missing")

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

    AX3, BX3 = apply_A_B(modes3, X3, sector)
    G3 = (X3.T @ BX3 + BX3.T @ X3) / 2.0
    H3 = (X3.T @ AX3 + AX3.T @ X3) / 2.0
    theta3, V3 = eigh(H3, G3, check_finite=False)

    raw = X3 @ V3
    signs = canonical_signs(raw)
    Z3 = raw * signs[None, :]
    AZ3 = (AX3 @ V3) * signs[None, :]
    BZ3 = (BX3 @ V3) * signs[None, :]

    return modes3, theta3, Z3, AZ3, BZ3


def naive_start(sector, modes3, theta3, Z3, shell4):
    ell3 = lead_functional_vector(sector, modes3)
    lead3 = ell3 @ Z3 + np.sum(Z3, axis=0) * theta3

    ell4 = lead_functional_vector(sector, shell4)
    common = float(np.sum(ell4))
    denom = common + theta3 * float(len(shell4))
    return -lead3 / denom


def one_sector(sector: str):
    modes3, theta3, Z3, AZ3, BZ3 = build_m3(sector)
    m3 = metrics(sector, modes3, theta3, Z3, AZ3, BZ3)

    shell4 = np.arange(int(modes3[-1]) + 2, M4[sector] + 1, 2, dtype=int)
    modes4 = np.concatenate([modes3, shell4])

    # Five-column basis K = [padded M3 carrier | constant shell vector].
    K = np.zeros((len(modes4), 5), dtype=float)
    K[: len(modes3), :4] = Z3
    K[len(modes3) :, 4] = 1.0

    AK, BK = apply_A_B(modes4, K, sector)
    G5 = (K.T @ BK + BK.T @ K) / 2.0
    H5 = (K.T @ AK + AK.T @ K) / 2.0

    ell5 = lead_functional_vector(sector, modes4) @ K
    sum5 = np.sum(K, axis=0)

    c0 = naive_start(sector, modes3, theta3, Z3, shell4)

    def contractions(c):
        C = np.vstack([np.eye(4), np.asarray(c, dtype=float)[None, :]])
        G = (C.T @ G5 @ C + (C.T @ G5 @ C).T) / 2.0
        H = (C.T @ H5 @ C + (C.T @ H5 @ C).T) / 2.0
        T = np.linalg.solve(G, H)
        L = ell5 @ C + (sum5 @ C) @ T
        return C, G, H, T, L

    def fun(c):
        return contractions(c)[-1]

    sol = root(fun, c0, method="hybr", tol=1.0e-11)
    c = np.asarray(sol.x, dtype=float)
    C, G, H, T, Lroot = contractions(c)

    # Re-Ritz the same solved subspace using its exact 4x4 generalized pair.
    theta4, V = eigh(H, G, check_finite=False)
    raw = (K @ C) @ V
    signs = canonical_signs(raw)
    Z4 = raw * signs[None, :]
    AZ4 = ((AK @ C) @ V) * signs[None, :]
    BZ4 = ((BK @ C) @ V) * signs[None, :]

    post = leading_row(
        sector,
        modes4,
        Z4,
        np.diag(theta4),
    )
    m4 = metrics(sector, modes4, theta4, Z4, AZ4, BZ4)

    finite_R = AZ4 - BZ4 * theta4[None, :]
    finite_residual = float(
        math.sqrt(
            max(
                0.0,
                float(
                    np.linalg.eigvalsh(
                        (finite_R.T @ finite_R + (finite_R.T @ finite_R).T)
                        / 2.0
                    )[-1]
                ),
            )
        )
    )

    return {
        "sector": sector,
        "root": {
            "success": bool(sol.success),
            "status": int(sol.status),
            "message": str(sol.message),
            "nfev": int(sol.nfev),
            "initial_amplitudes": [float(x) for x in c0],
            "amplitudes": [float(x) for x in c],
            "amplitude_2norm": float(np.linalg.norm(c)),
            "root_lead_vector": [float(x) for x in Lroot],
            "root_lead_2norm": float(np.linalg.norm(Lroot)),
        },
        "M3": {
            "theta": [float(x) for x in theta3],
            "lead_2norm": float(
                np.linalg.norm(
                    lead_functional_vector(sector, modes3) @ Z3
                    + np.sum(Z3, axis=0) * theta3
                )
            ),
            "metrics": m3,
        },
        "M4_self_consistent": {
            "modes": int(len(modes4)),
            "last_mode": int(modes4[-1]),
            "theta": [float(x) for x in theta4],
            "inside_0p02": bool(np.max(np.abs(theta4)) < 0.02),
            "post_reritz_lead_vector": [float(x) for x in post],
            "post_reritz_lead_2norm": float(np.linalg.norm(post)),
            "B_orthogonality_defect": float(
                np.linalg.norm(Z4.T @ BZ4 - np.eye(4), 2)
            ),
            "finite_residual_operator_replay": finite_residual,
            "metrics": m4,
        },
        "gate": {
            "root_converged": bool(sol.success),
            "subspace_invariant_moment_closed": bool(np.linalg.norm(post) < 1.0e-8),
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

    print("Self-consistent M3 -> M4 moment-constrained Ritz replay")
    for row in rows:
        print("\nsector =", row["sector"])
        print("root =", row["root"])
        print("M3 theta =", row["M3"]["theta"])
        print("M4 theta =", row["M4_self_consistent"]["theta"])
        print(
            "post-reritz lead 2-norm =",
            row["M4_self_consistent"]["post_reritz_lead_2norm"],
        )
        print(
            "M3 transformed residual =",
            row["M3"]["metrics"]["transformed_residual_cap"],
        )
        print(
            "M4 transformed residual =",
            row["M4_self_consistent"]["metrics"]["transformed_residual_cap"],
        )
        print(
            "M3 far bound =",
            row["M3"]["metrics"]["far_residual_bound"],
        )
        print(
            "M4 far bound =",
            row["M4_self_consistent"]["metrics"]["far_residual_bound"],
        )
        print("gate =", row["gate"])

    print("\nwrote", OUT)
    print(
        "GUARDRAIL: self-consistent carrier gate only; KKT/Feshbach rebuild "
        "comes only after this carrier passes."
    )


if __name__ == "__main__":
    main()
