#!/usr/bin/env python3
"""Protected source-capacity/core-crossing diagnostic.

Uses the audited v13.801 high-precision source/Feshbach implementation
unchanged as the numerical producer, then rewrites its output in the exact
rank-one-capacity variables of v13.994.

For each parity:

    G = h + r,

where
    h = tail source background,
    r = protected two-mode core source energy.

The full source capacity is
    C = 1/G.

After Schur elimination of the tail, the exact rank-one coefficient acting on
the protected core at the capacity crossing is
    alpha_* = C/(1-C h) = 1/r.

Thus the dimensionless quantity C h = h/G measures how much the tail
background moves the full capacity threshold away from the pure protected-core
threshold.

Diagnostic only: no cutoff-convergence, infinite-tail, Xi, RH/GRH claim.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

from suzuki_form_core_bulk_subtracted_resonance import (
    parity_components,
    source_feshbach,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "source_capacity_core_crossing_result.json"


def one_sector(max_mode: int, sector: str):
    data = parity_components(max_mode, sector)
    src = source_feshbach(data, max_mode)

    G = src["energy_full"]
    h = src["tail_energy"]
    r = src["core_energy"]

    C = 1 / G
    alpha = 1 / r
    Ch = C * h

    return {
        "sector": sector,
        "max_mode": int(max_mode),
        "energy_full": mp.nstr(G, 50),
        "tail_background_h": mp.nstr(h, 50),
        "protected_core_energy_r": mp.nstr(r, 50),
        "decomposition_relative_defect": mp.nstr(abs(G - h - r) / abs(G), 30),
        "capacity_C": mp.nstr(C, 50),
        "core_crossing_alpha": mp.nstr(alpha, 50),
        "C_times_h": mp.nstr(Ch, 30),
        "alpha_over_C_minus_1": mp.nstr(alpha / C - 1, 30),
        "tail_first4_energy_fraction": mp.nstr(src["tail_energy_4_fraction"], 30),
        "core_low_direction_energy_fraction": mp.nstr(src["core_low_fraction"], 30),
        "core_schur_eigenvalues": [
            mp.nstr(src["schur_vals"][i], 40)
            for i in range(len(src["schur_vals"]))
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-mode", type=int, default=192)
    parser.add_argument("--dps", type=int, default=70)
    args = parser.parse_args()

    with mp.workdps(args.dps):
        even = one_sector(args.max_mode, "even-v")
        odd = one_sector(args.max_mode, "odd-v")

        Ce = mp.mpf(even["capacity_C"])
        Co = mp.mpf(odd["capacity_C"])
        q = Ce / Co
        kappa = (Co - Ce) / (Co + Ce)

        out = {
            "max_mode": int(args.max_mode),
            "dps": int(args.dps),
            "even": even,
            "odd": odd,
            "projective": {
                "capacity_ratio_even_over_odd": mp.nstr(q, 50),
                "kappa_from_capacities": mp.nstr(kappa, 50),
            },
            "guardrail": (
                "Finite-cutoff protected/Feshbach diagnostic only; "
                "no infinite-cutoff or Xi claim."
            ),
        }
        OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

        for row in (even, odd):
            print("\nsector =", row["sector"])
            for key in (
                "energy_full",
                "tail_background_h",
                "protected_core_energy_r",
                "decomposition_relative_defect",
                "capacity_C",
                "core_crossing_alpha",
                "C_times_h",
                "alpha_over_C_minus_1",
                "tail_first4_energy_fraction",
                "core_low_direction_energy_fraction",
                "core_schur_eigenvalues",
            ):
                print(key, "=", row[key])

        print("\ncapacity ratio Ce/Co =", out["projective"]["capacity_ratio_even_over_odd"])
        print("kappa =", out["projective"]["kappa_from_capacities"])
        print("wrote", OUT)
        print("GUARDRAIL:", out["guardrail"])


if __name__ == "__main__":
    main()
