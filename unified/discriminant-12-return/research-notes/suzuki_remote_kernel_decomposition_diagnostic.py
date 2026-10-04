#!/usr/bin/env python3
"""Decompose the remote shell kernel seen by the normalized 1/n source tail.

For nested cutoffs N<M the exact finite-section source energies satisfy

    eta_{p;N->M}
      = (G_{p,M}-G_{p,N})/G_{p,N}
      = C_{p,N}/C_{p,M} - 1.

From v14.010 the finite source residual has leading form

    r_n ~ L_{p,N}/n,

and

    A_{p,N} := C_{p,N} L_{p,N}^2

is the squared 1/n amplitude after unit-energy normalization.

Define the empirically exact finite-shell effective kernel

    J_eff = eta / A.

Compare it with three source-faithful standalone shell models:
  (i) diagonal-only full diagonal;
  (ii) pole-free displacement/Cauchy tail block;
  (iii) full tail block including the parity rank-one pole.

This isolates whether the remaining discrepancy is already explained by
remote self-interaction or instead by Schur feedback through the retained
finite section.

Guardrail: diagnostic only.  The standalone shell inverse is NOT the exact
remote Schur complement.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data,
    ldl_solve,
    pole_vector,
    structured_ldl,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "remote_kernel_decomposition_diagnostic_result.json"

# LDDD midpoint capacities from v14.009.
CAP = {
    "even-v": {
        768: 7.81150178500978097079543563962406418952313164705873806866684e-30,
        1536: 7.70211941132473704542439486847448519398860307258897405441969e-30,
        3072: 7.60517660046981743730761773326432114842733975365269163351943e-30,
        4000: 7.5773007563692575306680936106689123586265630100827471120927e-30,
    },
    "odd-v": {
        768: 2.25601114835191553540647817691535258288951264233098262232427e-25,
        1536: 2.22168649473138414602470415510519526743883973071685010069676e-25,
        3072: 2.19248446398439423563170694421551363762978394343163246988626e-25,
        4000: 2.1845239838296620020805542670090522874748063437543145074951e-25,
    },
}

# A_N = C_N L_N^2 from v14.010.
AMP = {
    "even-v": {
        768: 432.156670577312286330712102701658277181434236682737758644765,
        1536: 574.384619858809749933033692270413556869004404360705298957474,
        3072: 741.223122085242646432914370540044628084596431843652882727887,
        4000: 802.991233306815743575233822525369891539735468205297660034446,
    },
    "odd-v": {
        768: 438.390301808444202155055176442843425255950461612003881542287,
        1536: 580.457255141011481655672112173523975203208406124140936891622,
        3072: 743.282149917092836120954929100970204032784034903597812497081,
        4000: 802.28091527530283140246652079478628408730187818341125579338,
    },
}


def parity_shell(sector: str, N: int, M: int):
    start = 1 if sector == "even-v" else 2
    all_modes = np.arange(start, M + 1, 2, dtype=int)
    return all_modes[all_modes > N]


def full_tail_solve(modes, sector, rhs):
    z, diag = endpoint_data(modes, sign=-1, rho=0.0)
    L, D = structured_ldl(modes, z, diag)

    y0 = ldl_solve(L, D, rhs)
    p, alpha = pole_vector(modes, sector)
    yp = ldl_solve(L, D, p)
    den = 1.0 + alpha * float(p @ yp)
    y = y0 - alpha * yp * float(p @ y0) / den

    return {
        "J_polefree": float(rhs @ y0),
        "J_full_tail": float(rhs @ y),
        "woodbury_denominator": float(den),
        "pole_correction": float(rhs @ (y - y0)),
        "diag": diag,
        "p": p,
        "alpha": alpha,
        "polefree_min_pivot": float(np.min(D)),
        "polefree_max_pivot": float(np.max(D)),
    }


def one_shell(sector: str, N: int, M: int):
    modes = parity_shell(sector, N, M)
    if len(modes) == 0:
        raise RuntimeError(("empty shell", sector, N, M))

    u = 1.0 / modes.astype(float)
    data = full_tail_solve(modes, sector, u)

    diag_full = data["diag"] + data["alpha"] * data["p"] ** 2
    J_diag = float(np.sum((u * u) / diag_full))

    Cn = CAP[sector][N]
    Cm = CAP[sector][M]
    A = AMP[sector][N]

    eta_exact = Cn / Cm - 1.0
    J_eff = eta_exact / A

    row = {
        "sector": sector,
        "N": N,
        "M": M,
        "first_shell_mode": int(modes[0]),
        "last_shell_mode": int(modes[-1]),
        "shell_dimension": int(len(modes)),
        "C_N": Cn,
        "C_M": Cm,
        "A_N": A,
        "eta_exact_from_capacities": eta_exact,
        "J_eff_exact_shell": J_eff,
        "J_diag": J_diag,
        "J_polefree": data["J_polefree"],
        "J_full_tail": data["J_full_tail"],
        "pole_correction": data["pole_correction"],
        "woodbury_denominator": data["woodbury_denominator"],
        "polefree_min_pivot": data["polefree_min_pivot"],
        "polefree_max_pivot": data["polefree_max_pivot"],
    }

    for key in ("J_diag", "J_polefree", "J_full_tail"):
        row[key + "_over_J_eff"] = row[key] / J_eff
        row[key + "_relative_error_vs_J_eff"] = (row[key] - J_eff) / J_eff

    return row


def main():
    shells = [(768, 1536), (1536, 3072), (3072, 4000)]
    rows = []
    for N, M in shells:
        for sector in ("even-v", "odd-v"):
            row = one_shell(sector, N, M)
            rows.append(row)
            print("\n", sector, N, "->", M)
            for k in (
                "eta_exact_from_capacities",
                "J_eff_exact_shell",
                "J_diag",
                "J_polefree",
                "J_full_tail",
                "J_diag_over_J_eff",
                "J_polefree_over_J_eff",
                "J_full_tail_over_J_eff",
                "pole_correction",
                "woodbury_denominator",
            ):
                print(k, "=", row[k])

    paired = []
    for N, M in shells:
        e = next(r for r in rows if r["N"] == N and r["M"] == M and r["sector"] == "even-v")
        o = next(r for r in rows if r["N"] == N and r["M"] == M and r["sector"] == "odd-v")
        paired.append({
            "N": N,
            "M": M,
            "J_eff_odd_over_even": o["J_eff_exact_shell"] / e["J_eff_exact_shell"],
            "J_full_tail_odd_over_even": o["J_full_tail"] / e["J_full_tail"],
            "J_diag_odd_over_even": o["J_diag"] / e["J_diag"],
            "eta_odd_minus_even": (
                o["eta_exact_from_capacities"] - e["eta_exact_from_capacities"]
            ),
            "A_odd_over_even_at_N": AMP["odd-v"][N] / AMP["even-v"][N],
        })

    out = {
        "rows": rows,
        "paired": paired,
        "guardrail": (
            "Diagnostic only. J_eff is exact for the finite capacity increment, "
            "but J_diag/J_polefree/J_full_tail are standalone remote-shell "
            "models, not certified Schur complements."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("\nPAIRED")
    print(json.dumps(paired, indent=2))
    print("\nwrote", OUT)
    print("GUARDRAIL:", out["guardrail"])


if __name__ == "__main__":
    main()
