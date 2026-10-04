#!/usr/bin/env python3
"""Regulated direct pre-KKT projective source quotient.

The raw rho=0 full finite sections are almost singular already at modest
cutoff because the P4 near-kernel is real geometry.  Therefore this replay
does not invert that raw section.

Instead use the audited endpoint shift convention

    F^-_rho = A - rho B_sm.

Setting rho=-delta gives

    A_delta = A + delta B_sm,

which regularizes the near-null generalized spectrum while preserving the
same source-faithful displacement-rank + parity-pole structure.

For each parity, cutoff, and delta>0 compute

    G_p,N(delta) = f^T A_delta^{-1} f

directly in the full parity section, before KKT/Feshbach elimination, and form

    kappa_N(delta)
      = (G_e,N(delta)-G_o,N(delta))
        /(G_e,N(delta)+G_o,N(delta)).

This is a numerical projective diagnostic only.  It does not identify any
particular delta with the exact Suzuki Xi scalar, and it does not promote the
delta->0 or N->infinity limit without a separate theorem.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.linalg import solve_triangular

from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data,
    pole_vector,
    structured_ldl,
)
from suzuki_kkt_remote_residual_certificate import source_rows

HERE = Path(__file__).resolve().parent
OUT = HERE / "pre_kkt_regulated_projective_quotient_result.json"

MAX_LAST = {"even-v": 3999, "odd-v": 4000}
CUTS = [499, 999, 1999, 3999]
DELTAS = [1e-1, 5e-2, 2e-2, 1e-2, 5e-3, 2e-3, 1e-3, 5e-4, 2e-4, 1e-4]


def fast_ldl_solve(L, D, rhs):
    y = solve_triangular(
        L,
        np.asarray(rhs, dtype=float),
        lower=True,
        unit_diagonal=True,
        check_finite=False,
    )
    y = y / D
    return solve_triangular(
        L.T,
        y,
        lower=False,
        unit_diagonal=True,
        check_finite=False,
    )


def modes_for(sector):
    if sector == "even-v":
        return np.arange(1, MAX_LAST[sector] + 1, 2, dtype=int)
    return np.arange(2, MAX_LAST[sector] + 1, 2, dtype=int)


def base_data(sector):
    modes = modes_for(sector)
    z0, d0 = endpoint_data(modes, sign=-1, rho=0.0)
    p, alpha = pole_vector(modes, sector)
    f = source_rows(modes, sector)
    bdiag = np.log(modes.astype(float) / 4.0) - 1.0 / (2.0 * modes.astype(float))
    return modes, z0, d0, p, float(alpha), f, bdiag


def solve_prefix(L, D, p, alpha, f, nvec):
    LL = L[:nvec, :nvec]
    DD = D[:nvec]
    pp = p[:nvec]
    ff = f[:nvec]

    x0 = fast_ldl_solve(LL, DD, ff)
    yp = fast_ldl_solve(LL, DD, pp)
    den = 1.0 + alpha * float(pp @ yp)

    # Do not hard-fail: the point of the delta sweep is to measure how close
    # the section is getting to the parity pole singularity.
    x = x0 - alpha * yp * float(pp @ x0) / den
    G = float(ff @ x)

    return {
        "energy": G,
        "pole_woodbury_denominator": float(den),
        "polefree_min_abs_pivot": float(np.min(np.abs(DD))),
        "solution_2norm": float(np.linalg.norm(x)),
    }


def one_sector_delta(sector, delta, base):
    modes, z0, d0, p, alpha, f, bdiag = base

    # endpoint_data(sign=-1,rho=-delta):
    #   z = z0 + delta*pi/2
    #   diag = d0 + delta*(log(n/4)-1/(2n))
    z = z0 + float(delta) * np.pi / 2.0
    diag = d0 + float(delta) * bdiag
    L, D = structured_ldl(modes, z, diag)

    rows = []
    for cut in CUTS:
        last = cut if sector == "even-v" else cut + 1
        nvec = int(np.searchsorted(modes, last, side="right"))
        r = solve_prefix(L, D, p, alpha, f, nvec)
        r.update(
            {
                "delta": float(delta),
                "last_mode": int(modes[nvec - 1]),
                "dimension": int(nvec),
            }
        )
        rows.append(r)
    return rows


def main():
    bases = {s: base_data(s) for s in ("even-v", "odd-v")}
    by_sector = {"even-v": [], "odd-v": []}

    for delta in DELTAS:
        print("\ndelta =", delta)
        for sector in ("even-v", "odd-v"):
            rows = one_sector_delta(sector, delta, bases[sector])
            by_sector[sector].append(rows)
            print(
                sector,
                [
                    (
                        r["last_mode"],
                        r["energy"],
                        r["pole_woodbury_denominator"],
                    )
                    for r in rows
                ],
            )

    combined = []
    for idelta, delta in enumerate(DELTAS):
        for icut, cut in enumerate(CUTS):
            e = by_sector["even-v"][idelta][icut]
            o = by_sector["odd-v"][idelta][icut]
            Ge = float(e["energy"])
            Go = float(o["energy"])
            Fm = Ge + Go
            Fp = Ge - Go
            kap = Fp / Fm
            combined.append(
                {
                    "delta": float(delta),
                    "cut": int(cut),
                    "dimension_each": int(e["dimension"]),
                    "G_even": Ge,
                    "G_odd": Go,
                    "F_minus_i": Fm,
                    "F_plus_i": Fp,
                    "kappa": kap,
                    "odd_over_even_energy": Go / Ge,
                    "inside_schur_interval": bool(abs(kap) < 1.0),
                    "even_pole_denominator": float(e["pole_woodbury_denominator"]),
                    "odd_pole_denominator": float(o["pole_woodbury_denominator"]),
                }
            )

    # Delta-direction differences at fixed cutoff.
    for cut in CUTS:
        rows = [r for r in combined if r["cut"] == cut]
        rows.sort(key=lambda r: r["delta"], reverse=True)
        for j in range(1, len(rows)):
            rows[j]["delta_kappa_from_previous_delta"] = (
                rows[j]["kappa"] - rows[j - 1]["kappa"]
            )

    # Cutoff-direction differences at fixed delta.
    for delta in DELTAS:
        rows = [r for r in combined if r["delta"] == float(delta)]
        rows.sort(key=lambda r: r["cut"])
        for j in range(1, len(rows)):
            rows[j]["delta_kappa_from_previous_cut"] = (
                rows[j]["kappa"] - rows[j - 1]["kappa"]
            )

    out = {
        "method": "full finite section of A + delta B_sm before KKT/Feshbach",
        "deltas": DELTAS,
        "cuts": CUTS,
        "even": by_sector["even-v"],
        "odd": by_sector["odd-v"],
        "combined": combined,
        "guardrail": (
            "Numerical regulated finite-section diagnostic only. "
            "No delta->0, N->infinity, Xi, RH/GRH, or exact kappa claim."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("\nprojective table")
    for cut in CUTS:
        print("\ncut =", cut)
        for delta in DELTAS:
            row = next(
                r for r in combined
                if r["cut"] == cut and r["delta"] == float(delta)
            )
            print(
                "delta =", delta,
                "kappa =", repr(row["kappa"]),
                "Ge =", repr(row["G_even"]),
                "Go =", repr(row["G_odd"]),
                "den_e =", repr(row["even_pole_denominator"]),
                "den_o =", repr(row["odd_pole_denominator"]),
            )

    print("\nwrote", OUT)
    print(
        "GUARDRAIL: regulated finite-section projective diagnostic only."
    )


if __name__ == "__main__":
    main()
