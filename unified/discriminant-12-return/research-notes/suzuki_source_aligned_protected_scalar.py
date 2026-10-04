#!/usr/bin/env python3
"""Source-align the protected six-plane and reduce capacity to one scalar.

Starting from the same exact N=192 six-plane decomposition used in
suzuki_protected_sixplane_capacity_decomposition.py, rotate the protected
coordinates so that

    g6 = ||g6|| e1.

Writing the rotated protected Schur matrix as

    [ a   c^T ]
    [ c    D5  ],

the protected source energy is exactly

    r = ||g6||^2 / s,
    s = a - c^T D5^{-1} c,

provided D5 is invertible.  The protected rank-one capacity crossing is

    alpha_* = 1/r = s / ||g6||^2.

The full capacity including the already-eliminated stiff-source background h
is

    C = alpha_* / (1 + alpha_* h).

Thus, once the source-orthogonal five-plane is certified positive, the entire
capacity crossing is one scalar sign test.

Diagnostic only: finite N=192 high-precision section.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

from suzuki_form_core_bulk_subtracted_resonance import (
    parity_components,
    source_overlap,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "source_aligned_protected_scalar_result.json"


def vec(entries):
    return mp.matrix(entries)


def householder_source(g):
    n = g.rows
    normg = mp.sqrt((g.T * g)[0])
    u = g / normg
    e1 = mp.matrix(n, 1)
    e1[0] = 1
    v = e1 - u
    vv = (v.T * v)[0]
    if abs(vv) < mp.eps * 100:
        H = mp.eye(n)
    else:
        H = mp.eye(n) - (2 / vv) * (v * v.T)
    # H e1 = u, hence H^T g = normg e1.
    return H, normg


def one_sector(max_mode: int, sector: str):
    ns, _, _, _, _, full = parity_components(max_mode, sector)
    n = len(ns)
    core_dim = 2
    nc = n - core_dim

    A_cc = full[:core_dim, :core_dim]
    A_ct = full[:core_dim, core_dim:]
    A_tt = full[core_dim:, core_dim:]
    f = vec([source_overlap(k) for k in ns])
    f_c = f[:core_dim, :]
    f_t = f[core_dim:, :]

    # Tail spectral P4/Q split.
    lam, U = mp.eigsy((A_tt + A_tt.T) / 2)
    order = sorted(range(nc), key=lambda j: abs(lam[j]))
    ids_p = order[:4]
    ids_q = order[4:]

    U_p = mp.matrix(nc, 4)
    U_q = mp.matrix(nc, nc - 4)
    for j, idx in enumerate(ids_p):
        for i in range(nc):
            U_p[i, j] = U[i, idx]
    for j, idx in enumerate(ids_q):
        for i in range(nc):
            U_q[i, j] = U[i, idx]

    lam_p = [lam[j] for j in ids_p]
    lam_q = [lam[j] for j in ids_q]

    A_cp = A_ct * U_p
    A_cq = A_ct * U_q
    fp = U_p.T * f_t
    fq = U_q.T * f_t

    App = mp.matrix(6)
    for i in range(2):
        for j in range(2):
            App[i, j] = A_cc[i, j]
    for i in range(2):
        for j in range(4):
            App[i, 2 + j] = A_cp[i, j]
            App[2 + j, i] = A_cp[i, j]
    for j in range(4):
        App[2 + j, 2 + j] = lam_p[j]

    E = mp.matrix(nc - 4, 6)
    for iq in range(nc - 4):
        for j in range(2):
            E[iq, j] = A_cq[j, iq]

    fP = mp.matrix(6, 1)
    for j in range(2):
        fP[j] = f_c[j]
    for j in range(4):
        fP[2 + j] = fp[j]

    Dinv_fq = mp.matrix(nc - 4, 1)
    Dinv_E = mp.matrix(nc - 4, 6)
    for i in range(nc - 4):
        if lam_q[i] <= 0:
            raise RuntimeError((sector, "stiff complement not positive"))
        Dinv_fq[i] = fq[i] / lam_q[i]
        for j in range(6):
            Dinv_E[i, j] = E[i, j] / lam_q[i]

    S6 = (App - E.T * Dinv_E)
    S6 = (S6 + S6.T) / 2
    g6 = fP - E.T * Dinv_fq
    h = (fq.T * Dinv_fq)[0]

    H, gnorm = householder_source(g6)
    R = H.T * S6 * H
    R = (R + R.T) / 2

    a = R[0, 0]
    c = R[1:, 0]
    D5 = R[1:, 1:]
    vals5, _ = mp.eigsy(D5)
    if vals5[0] <= 0:
        raise RuntimeError((sector, "source-orthogonal five-plane nonpositive"))

    z = mp.lu_solve(D5, c)
    correction = (c.T * z)[0]
    scalar_s = a - correction
    alpha = scalar_s / (gnorm * gnorm)
    r = 1 / alpha
    C = alpha / (1 + alpha * h)
    G = h + r

    # Direct protected check.
    w6 = mp.lu_solve(S6, g6)
    r_direct = (g6.T * w6)[0]
    rel_r = abs(r - r_direct) / abs(r_direct)

    vals6, _ = mp.eigsy(S6)

    return {
        "sector": sector,
        "max_mode": max_mode,
        "g_norm": mp.nstr(gnorm, 50),
        "source_axis_raw_a": mp.nstr(a, 50),
        "source_axis_feshbach_correction": mp.nstr(correction, 50),
        "source_axis_scalar_s": mp.nstr(scalar_s, 50),
        "cancellation_ratio_correction_over_a": mp.nstr(correction / a, 40),
        "fiveplane_eigenvalues": [mp.nstr(vals5[j], 50) for j in range(5)],
        "fiveplane_min_eigenvalue": mp.nstr(vals5[0], 50),
        "S6_min_eigenvalue": mp.nstr(vals6[0], 50),
        "fiveplane_to_scalar_separation": mp.nstr(vals5[0] / scalar_s, 40),
        "alpha_core_crossing": mp.nstr(alpha, 50),
        "stiff_source_background_h": mp.nstr(h, 50),
        "alpha_times_h": mp.nstr(alpha * h, 40),
        "capacity": mp.nstr(C, 50),
        "energy": mp.nstr(G, 50),
        "protected_energy_r": mp.nstr(r, 50),
        "protected_energy_direct": mp.nstr(r_direct, 50),
        "protected_energy_relative_defect": mp.nstr(rel_r, 30),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-mode", type=int, default=192)
    parser.add_argument("--dps", type=int, default=80)
    args = parser.parse_args()

    with mp.workdps(args.dps):
        even = one_sector(args.max_mode, "even-v")
        odd = one_sector(args.max_mode, "odd-v")
        Ce = mp.mpf(even["capacity"])
        Co = mp.mpf(odd["capacity"])
        q = Ce / Co
        kappa = (Co - Ce) / (Co + Ce)

        out = {
            "even": even,
            "odd": odd,
            "projective": {
                "Ce_over_Co": mp.nstr(q, 50),
                "kappa": mp.nstr(kappa, 50),
            },
            "guardrail": (
                "Finite N=192 source-aligned protected scalar diagnostic only."
            ),
        }
        OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

        for row in (even, odd):
            print("\nsector =", row["sector"])
            for k, v in row.items():
                if k != "sector":
                    print(k, "=", v)

        print("\nCe/Co =", out["projective"]["Ce_over_Co"])
        print("kappa =", out["projective"]["kappa"])
        print("wrote", OUT)


if __name__ == "__main__":
    main()
