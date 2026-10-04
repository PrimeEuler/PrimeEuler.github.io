#!/usr/bin/env python3
"""High-precision protected six-plane source-capacity decomposition.

Purpose
-------
The source-capacity gate at a=1, lambda=0 is controlled by:
  * two low/source-active parity modes;
  * four near-zero tail resonance directions;
while the remaining tail complement is stiff.

This script makes that split explicitly at the already-audited N=192
high-precision checkpoint.  It uses the source-faithful mpmath matrix producer
from suzuki_form_core_bulk_subtracted_resonance.py.

For each parity:
  1. split P_low = first two basis vectors and tail T;
  2. diagonalize the tail T at high precision;
  3. retain its four smallest eigenvectors as P4;
  4. eliminate the orthogonal stiff complement Q exactly in its tail
     eigenbasis;
  5. assemble the protected six-dimensional Schur matrix S6 and source g6;
  6. compute
         G = h_Q + g6^T S6^{-1} g6,
     and compare against the direct full solve.

This is the architecture intended for the theorem-scale M3999/4000 gate:
only the stiff complement is inverted.  The dangerous six-plane is never
treated perturbatively.

Diagnostic only: N=192 finite section, no infinite-tail or Xi claim.
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
OUT = HERE / "protected_sixplane_capacity_decomposition_result.json"


def vec(entries):
    return mp.matrix(entries)


def one_sector(max_mode: int, sector: str):
    ns, _, _, _, _, full = parity_components(max_mode, sector)
    n = len(ns)
    if n <= 6:
        raise RuntimeError("section too small")

    core_dim = 2
    nc = n - core_dim

    A_cc = full[:core_dim, :core_dim]
    A_ct = full[:core_dim, core_dim:]
    A_tt = full[core_dim:, core_dim:]
    f = vec([source_overlap(k) for k in ns])
    f_c = f[:core_dim, :]
    f_t = f[core_dim:, :]

    # Direct reference.
    x_full = mp.lu_solve(full, f)
    G_direct = (f.T * x_full)[0]

    # High-precision tail spectral split.
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

    # Protected coordinates: [low 2 ; tail P4].
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
    # Q-to-low coupling.
    for iq in range(nc - 4):
        for j in range(2):
            E[iq, j] = A_cq[j, iq]
    # Tail eigenbasis makes Q-to-P4 coupling zero.

    fP = mp.matrix(6, 1)
    for j in range(2):
        fP[j] = f_c[j]
    for j in range(4):
        fP[2 + j] = fp[j]

    # Eliminate stiff Q exactly because D_Q is diagonal in this basis.
    Dinv_fq = mp.matrix(nc - 4, 1)
    Dinv_E = mp.matrix(nc - 4, 6)
    for i in range(nc - 4):
        if lam_q[i] <= 0:
            raise RuntimeError(
                (sector, "stiff complement not positive", i, mp.nstr(lam_q[i], 30))
            )
        Dinv_fq[i] = fq[i] / lam_q[i]
        for j in range(6):
            Dinv_E[i, j] = E[i, j] / lam_q[i]

    S6 = App - E.T * Dinv_E
    S6 = (S6 + S6.T) / 2
    g6 = fP - E.T * Dinv_fq
    hQ = (fq.T * Dinv_fq)[0]

    w6 = mp.lu_solve(S6, g6)
    G6 = hQ + (g6.T * w6)[0]

    vals6, V6 = mp.eigsy(S6)
    c6 = V6.T * g6
    terms6 = [c6[j] ** 2 / vals6[j] for j in range(6)]
    order6 = sorted(range(6), key=lambda j: abs(terms6[j]), reverse=True)

    # Useful stiffness and exact-decomposition diagnostics.
    min_q = min(lam_q)
    max_q = max(lam_q)
    protected_energy = (g6.T * w6)[0]
    rel_defect = abs(G6 - G_direct) / abs(G_direct)

    return {
        "sector": sector,
        "max_mode": max_mode,
        "dimension": n,
        "tail_protected_eigenvalues": [mp.nstr(x, 50) for x in lam_p],
        "stiff_complement_min_eigenvalue": mp.nstr(min_q, 50),
        "stiff_complement_max_eigenvalue": mp.nstr(max_q, 50),
        "stiff_complement_condition": mp.nstr(max_q / min_q, 30),
        "S6_eigenvalues": [mp.nstr(vals6[j], 50) for j in range(6)],
        "source_coordinates_in_S6_eigenbasis": [
            mp.nstr(c6[j], 40) for j in range(6)
        ],
        "S6_energy_terms": [mp.nstr(terms6[j], 50) for j in range(6)],
        "S6_energy_term_order": order6,
        "stiff_source_background_hQ": mp.nstr(hQ, 50),
        "protected_energy": mp.nstr(protected_energy, 50),
        "full_energy_from_sixplane": mp.nstr(G6, 50),
        "full_energy_direct": mp.nstr(G_direct, 50),
        "relative_decomposition_defect": mp.nstr(rel_defect, 30),
        "capacity": mp.nstr(1 / G6, 50),
        "hQ_over_G": mp.nstr(hQ / G6, 30),
        "protected_fraction": mp.nstr(protected_energy / G6, 30),
        "dominant_S6_energy_fraction": mp.nstr(
            terms6[order6[0]] / protected_energy, 30
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-mode", type=int, default=192)
    parser.add_argument("--dps", type=int, default=80)
    args = parser.parse_args()

    with mp.workdps(args.dps):
        rows = [
            one_sector(args.max_mode, "even-v"),
            one_sector(args.max_mode, "odd-v"),
        ]
        even, odd = rows
        Ce = mp.mpf(even["capacity"])
        Co = mp.mpf(odd["capacity"])
        q = Ce / Co
        kappa = (Co - Ce) / (Co + Ce)

        out = {
            "max_mode": args.max_mode,
            "dps": args.dps,
            "even": even,
            "odd": odd,
            "projective": {
                "capacity_ratio_even_over_odd": mp.nstr(q, 50),
                "kappa": mp.nstr(kappa, 50),
            },
            "guardrail": (
                "Finite N=192 high-precision protected-six-plane diagnostic; "
                "no infinite-tail, theorem-scale M3999, or Xi promotion."
            ),
        }
        OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

        for row in rows:
            print("\nsector =", row["sector"])
            for key in (
                "tail_protected_eigenvalues",
                "stiff_complement_min_eigenvalue",
                "stiff_complement_condition",
                "S6_eigenvalues",
                "stiff_source_background_hQ",
                "protected_energy",
                "full_energy_from_sixplane",
                "full_energy_direct",
                "relative_decomposition_defect",
                "hQ_over_G",
                "protected_fraction",
                "dominant_S6_energy_fraction",
            ):
                print(key, "=", row[key])

        print(
            "\ncapacity ratio Ce/Co =",
            out["projective"]["capacity_ratio_even_over_odd"],
        )
        print("kappa =", out["projective"]["kappa"])
        print("wrote", OUT)
        print("GUARDRAIL:", out["guardrail"])


if __name__ == "__main__":
    main()
