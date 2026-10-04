#!/usr/bin/env python3
"""Direct Euclidean shell-Schur floor scan for N=4000 -> M=8000.

For the finite M-section split as retained N plus shell Q,

    A_M = [[A_N, B^T],
           [B,   D ]],

with A_N positive, the shell Schur complement is

    S_Q = D - B A_N^{-1} B^T.

For any mu,

    S_Q - mu I > 0

iff

    A_M - mu * Pi_Q > 0,

where Pi_Q is the Euclidean coordinate projector onto the new shell.

This script tests positivity of A_M - mu Pi_Q through the unchanged frozen
N=4000 six-plane:
  * certify the midpoint Euclidean orthogonal-complement floor numerically;
  * eliminate that complement;
  * inspect the resulting 6x6 protected Schur matrix.

A bisection locates the finite-shell midpoint crossing mu_*.

Diagnostic only: binary64 operator assembly / eigsh / CG are used here to
identify the scale.  A later LDDD/outward replay is required for promotion.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import LinearOperator, cg, eigsh

from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_M3999_frozen_p4_source_capacity_midpoint import full_source_matrix
from suzuki_ldd_refined_capacity_bracket import double_projector

HERE = Path(__file__).resolve().parent
OUT = HERE / "M8000_shell_schur_floor_scan_result.json"


def reduced_gate(A, P, Gi, shell_start, mu, eig_tol=1e-10):
    n = A.shape[0]
    proj = double_projector(P, Gi)
    shell_mask = np.zeros(n, dtype=float)
    shell_mask[shell_start:] = 1.0

    def ashift_mv(x):
        x = np.asarray(x, dtype=float)
        if x.ndim == 1:
            return A @ x - mu * shell_mask * x
        return A @ x - mu * shell_mask[:, None] * x

    def comp_mv(x):
        qx = proj(x)
        return proj(ashift_mv(qx)) + P @ (Gi @ (P.T @ x))

    op = LinearOperator((n, n), matvec=comp_mv, dtype=float)
    ceigs = np.sort(
        eigsh(op, k=2, which="SA", return_eigenvectors=False, tol=eig_tol)
    )
    cmin = float(ceigs[0])

    AP = ashift_mv(P)
    E = proj(AP)
    App = P.T @ AP

    Y = np.empty_like(E)
    residuals = []
    iters = []
    for j in range(P.shape[1]):
        count = [0]
        def cb(_):
            count[0] += 1
        y, info = cg(
            op, E[:, j], rtol=2e-13, atol=0.0, maxiter=30000, callback=cb
        )
        if info != 0:
            raise RuntimeError(("CG failed", mu, j, info))
        y = proj(y)
        Y[:, j] = y
        residuals.append(float(np.linalg.norm(E[:, j] - comp_mv(y))))
        iters.append(count[0])

    S = App - E.T @ Y
    S = (S + S.T) / 2
    seigs = np.linalg.eigvalsh(S)
    smin = float(seigs[0])

    return {
        "mu": float(mu),
        "complement_low_eigs": [float(x) for x in ceigs],
        "complement_min": cmin,
        "protected_eigenvalues": [float(x) for x in seigs],
        "protected_min": smin,
        "max_cg_residual": max(residuals),
        "cg_iterations": iters,
        "positive_midpoint": bool(cmin > 0 and smin > 0),
    }


def one_sector(sector, lo, hi, steps):
    base_modes, modes, P, _, _ = embedded_protected_basis(sector)
    A, _ = full_source_matrix(modes, sector)
    G = P.T @ P
    Gi = np.linalg.inv(G)
    shell_start = len(base_modes)

    probes = []
    # Initial endpoints plus a few interior probes.
    for mu in np.linspace(lo, hi, 5):
        row = reduced_gate(A, P, Gi, shell_start, float(mu))
        probes.append(row)
        print(sector, "probe", mu,
              "comp", row["complement_min"],
              "Smin", row["protected_min"],
              "pos", row["positive_midpoint"])

    a, b = lo, hi
    ra = reduced_gate(A, P, Gi, shell_start, a)
    rb = reduced_gate(A, P, Gi, shell_start, b)
    if not ra["positive_midpoint"]:
        raise RuntimeError((sector, "lower endpoint not positive", ra))
    if rb["positive_midpoint"]:
        raise RuntimeError((sector, "upper endpoint still positive", rb))

    history = []
    for _ in range(steps):
        m = (a + b) / 2
        rm = reduced_gate(A, P, Gi, shell_start, m)
        history.append(rm)
        if rm["positive_midpoint"]:
            a = m
        else:
            b = m

    rlo = reduced_gate(A, P, Gi, shell_start, a)
    rhi = reduced_gate(A, P, Gi, shell_start, b)
    return {
        "sector": sector,
        "base_last_mode": int(base_modes[-1]),
        "target_last_mode": int(modes[-1]),
        "dimension": len(modes),
        "shell_dimension": len(modes)-len(base_modes),
        "probes": probes,
        "bisection_steps": steps,
        "mu_positive_midpoint_lower": a,
        "mu_nonpositive_midpoint_upper": b,
        "lower_gate": rlo,
        "upper_gate": rhi,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--steps", type=int, default=16)
    args = ap.parse_args()

    # Even embedded complement itself is ~0.155, so bracket below it.
    even = one_sector("even-v", 0.0, 0.15, args.steps)
    # Odd embedded complement is ~0.532.
    odd = one_sector("odd-v", 0.0, 0.50, args.steps)

    out = {
        "rows": [even, odd],
        "guardrail": (
            "Finite M8000 midpoint diagnostic only. The crossing is found by "
            "binary64 shifted-complement/Feshbach positivity; no outward "
            "exact-source interval or infinite-tail attachment is asserted."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("\nSUMMARY")
    print("even floor bracket",
          even["mu_positive_midpoint_lower"],
          even["mu_nonpositive_midpoint_upper"])
    print("odd floor bracket",
          odd["mu_positive_midpoint_lower"],
          odd["mu_nonpositive_midpoint_upper"])
    print("wrote", OUT)


if __name__ == "__main__":
    main()
