#!/usr/bin/env python3
"""Direct pre-KKT finite-section projective source quotient.

This replay works in the full source-faithful parity basis before any
arbitrary-carrier Feshbach/KKT elimination.

For each parity and nested finite cutoff N, form the pole-free structured
matrix K_N using the audited displacement-rank generator and diagonal, then
add the exact parity rank-one pole

    A_N = K_N + alpha p p^T.

For the exact finite-section source coefficients f_N=<psi_n,e^x>, solve

    A_N x_N = f_N

with structured LDL plus Sherman-Morrison and compute

    G_{p,N} = f_N^T x_N.

The finite-section deficiency-overlap quotient is then

    kappa_N = (G_{e,N}-G_{o,N})/(G_{e,N}+G_{o,N}).

This is the full finite-section version of the v13.993 projective quotient:
no numerical-carrier complement, no KKT inverse action, and no tiny 6x6
inverse enters the computation.

Guardrails:
- diagnostic finite-section sequence only;
- no finite-to-infinite convergence theorem is asserted;
- no Xi/RH/GRH conclusion is asserted;
- the source operator is the rho=0 source-faithful matrix used by the KKT
  residual architecture.
"""
from __future__ import annotations

import json
import math
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
OUT = HERE / "pre_kkt_finite_section_projective_quotient_result.json"

# Largest same-parity section used in this diagnostic.
MAX_LAST = {
    "even-v": 7999,
    "odd-v": 8000,
}

# Nested physical Fourier-mode cutoffs.  The odd cutoff is one larger so
# both parity sectors contain the same number of basis vectors.
CUTS = [499, 999, 1999, 3999, 7999]


def fast_ldl_solve(L: np.ndarray, D: np.ndarray, rhs: np.ndarray) -> np.ndarray:
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


def parity_setup(sector: str):
    if sector == "even-v":
        modes = np.arange(1, MAX_LAST[sector] + 1, 2, dtype=int)
    else:
        modes = np.arange(2, MAX_LAST[sector] + 1, 2, dtype=int)

    # rho=0 is the source operator.  sign is immaterial when rho=0.
    z, diag = endpoint_data(modes, sign=-1, rho=0.0)
    L, D = structured_ldl(modes, z, diag)
    p, alpha = pole_vector(modes, sector)
    f = source_rows(modes, sector)

    return modes, L, D, p, float(alpha), f


def one_prefix(
    modes: np.ndarray,
    L: np.ndarray,
    D: np.ndarray,
    p: np.ndarray,
    alpha: float,
    f: np.ndarray,
    nvec: int,
):
    mm = modes[:nvec]
    LL = L[:nvec, :nvec]
    DD = D[:nvec]
    pp = p[:nvec]
    ff = f[:nvec]

    x0 = fast_ldl_solve(LL, DD, ff)
    yp = fast_ldl_solve(LL, DD, pp)

    q = float(pp @ yp)
    den = 1.0 + alpha * q
    if abs(den) < 1.0e-14:
        raise RuntimeError(("pole Woodbury denominator too small", int(mm[-1]), den))

    x = x0 - alpha * yp * float(pp @ x0) / den
    energy = float(ff @ x)

    # Algebraic residual in the pole-free solve is represented by the LDL
    # factorization itself.  Report scale diagnostics that do not require
    # constructing the dense A_N.
    return {
        "last_mode": int(mm[-1]),
        "dimension": int(nvec),
        "energy": energy,
        "pole_woodbury_denominator": den,
        "polefree_min_abs_pivot": float(np.min(np.abs(DD))),
        "solution_2norm": float(np.linalg.norm(x)),
        "source_2norm": float(np.linalg.norm(ff)),
    }


def main():
    data = {}
    setups = {}

    for sector in ("even-v", "odd-v"):
        print("\nbuilding", sector)
        modes, L, D, p, alpha, f = parity_setup(sector)
        setups[sector] = (modes, L, D, p, alpha, f)

        rows = []
        for cut in CUTS:
            last = cut if sector == "even-v" else cut + 1
            nvec = int(np.searchsorted(modes, last, side="right"))
            row = one_prefix(modes, L, D, p, alpha, f, nvec)
            rows.append(row)
            print(
                sector,
                "last_mode =", row["last_mode"],
                "dim =", row["dimension"],
                "G =", repr(row["energy"]),
                "woodbury =", repr(row["pole_woodbury_denominator"]),
            )
        data[sector] = rows

    combined = []
    for erow, orow in zip(data["even-v"], data["odd-v"]):
        Ge = float(erow["energy"])
        Go = float(orow["energy"])
        den = Ge + Go
        kap = (Ge - Go) / den
        q = Go / Ge
        combined.append(
            {
                "even_last_mode": int(erow["last_mode"]),
                "odd_last_mode": int(orow["last_mode"]),
                "dimension_each": int(erow["dimension"]),
                "G_even": Ge,
                "G_odd": Go,
                "F_minus_i": den,
                "F_plus_i": Ge - Go,
                "kappa": kap,
                "odd_over_even_energy": q,
                "inside_schur_interval": bool(abs(kap) < 1.0),
            }
        )

    for j in range(1, len(combined)):
        combined[j]["delta_kappa_from_previous"] = (
            combined[j]["kappa"] - combined[j - 1]["kappa"]
        )

    out = {
        "method": (
            "full source-faithful rho=0 finite parity sections; structured "
            "pole-free LDL plus exact rank-one pole Sherman-Morrison"
        ),
        "cutoffs": CUTS,
        "even": data["even-v"],
        "odd": data["odd-v"],
        "combined": combined,
        "guardrail": (
            "Finite-section diagnostic only. No finite-to-infinite convergence, "
            "Xi, RH/GRH, or exact kappa claim."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("\ncombined projective quotient")
    for row in combined:
        print(
            "N =", row["even_last_mode"],
            "Ge =", repr(row["G_even"]),
            "Go =", repr(row["G_odd"]),
            "kappa =", repr(row["kappa"]),
            "q=Go/Ge =", repr(row["odd_over_even_energy"]),
            "Schur =", row["inside_schur_interval"],
            "delta =", row.get("delta_kappa_from_previous"),
        )

    print("\nwrote", OUT)
    print(
        "GUARDRAIL: direct finite-section projective diagnostic only; "
        "the tail/convergence theorem remains separate."
    )


if __name__ == "__main__":
    main()
