#!/usr/bin/env python3
"""Probe the paired remote operators: coercivity, paired differences, K values.

Builds D_e, D_o (the explicit remote diagonal+kernel blocks, WITHOUT the
Schur correction which needs finite data) on paired windows, and computes:
  - lambda_min (coercivity probe)
  - ||D_o - D_e||_2 on the paired index space
  - K_p = <u, D_p^{-1} u> (diagonal-approx tail kernel)
All deterministic.
"""
from __future__ import annotations
import numpy as np
from infinite_tail_producer import (
    paired_modes, z_parity, diag_n, pole_n, alpha, kernel, diag_kernel,
    C_TWO_OVER_PI,
)

rng = np.random.default_rng(0)  # NOT used for the math; only if needed


def build_D(modes, sector, zcache):
    J = len(modes)
    D = np.zeros((J, J))
    for i, n in enumerate(modes):
        D[i, i] = diag_kernel(n, sector)
        for j, m in enumerate(modes):
            if i != j:
                D[i, j] = kernel(n, m, sector, zcache)
    return D


def main():
    N = 16000
    J = 400  # window size for probing
    ns, ms = paired_modes(N, J)
    zcache = {}
    for n in ns:
        zcache[(n, "even")] = z_parity(n, "even")
    for m in ms:
        zcache[(m, "odd")] = z_parity(m, "odd")

    De = build_D(ns, "even", zcache)
    Do = build_D(ms, "odd", zcache)

    # symmetrize (kernel should be symmetric; enforce for eig)
    De = 0.5 * (De + De.T)
    Do = 0.5 * (Do + Do.T)

    le = np.linalg.eigvalsh(De)
    lo = np.linalg.eigvalsh(Do)
    print(f"window J={J} at N={N}")
    print(f"  lambda_min(De)={le[0]:.6f}  lambda_max(De)={le[-1]:.6f}")
    print(f"  lambda_min(Do)={lo[0]:.6f}  lambda_max(Do)={lo[-1]:.6f}")
    print(f"  diag range De: [{np.diag(De).min():.4f},{np.diag(De).max():.4f}]")
    print(f"  diag range Do: [{np.diag(Do).min():.4f},{np.diag(Do).max():.4f}]")

    # paired difference operator norm
    Delta = Do - De
    s = np.linalg.svd(Delta, compute_uv=False)
    print(f"  ||Do-De||_2 = {s[0]:.6e}")
    print(f"  ||Do-De||_F = {np.linalg.norm(Delta,'fro'):.6e}")
    # diagonal of Delta
    dd = np.diag(Delta)
    print(f"  diag(Delta): min={dd.min():.4e} max={dd.max():.4e} (expect O(1/n))")
    print(f"  1/n_j at j=0: {1/ns[0]:.4e}")

    # K_p = <u, D_p^{-1} u>, u(n)=1/n
    ue = 1.0 / np.array(ns, dtype=float)
    uo = 1.0 / np.array(ms, dtype=float)
    Ke = ue @ np.linalg.solve(De, ue)
    Ko = uo @ np.linalg.solve(Do, uo)
    print(f"  K_e(window)={Ke:.6e}  K_o(window)={Ko:.6e}")
    print(f"  K_o-K_e = {Ko-Ke:.6e}")
    # diagonal approx: sum 1/(n^2 d_n)
    Ke_d = sum(1.0 / (n * n * diag_kernel(n, "even")) for n in ns)
    Ko_d = sum(1.0 / (m * m * diag_kernel(m, "odd")) for m in ms)
    print(f"  K_e(diag)={Ke_d:.6e}  K_o(diag)={Ko_d:.6e}")

    # ||u|| and ||w||=||D^{-1}u||
    we = np.linalg.solve(De, ue)
    wo = np.linalg.solve(Do, uo)
    print(f"  ||u_e||={np.linalg.norm(ue):.4e} ||w_e||={np.linalg.norm(we):.4e}")
    print(f"  ||u_o||={np.linalg.norm(uo):.4e} ||w_o||={np.linalg.norm(wo):.4e}")
    print(f"  ||D_e^-1||={1/le[0]:.4e} ||D_o^-1||={1/lo[0]:.4e}")


if __name__ == "__main__":
    main()
