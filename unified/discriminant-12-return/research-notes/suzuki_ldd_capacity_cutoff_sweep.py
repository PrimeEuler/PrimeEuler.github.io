#!/usr/bin/env python3
"""Nested-cutoff LDDD capacity sweep.

Purpose
-------
Measure the finite-section convergence law of the source capacities using the
same frozen P4 carrier and LDDD residual-refinement bracket that passed the
v14.008 precision gate.

This is deliberately diagnostic.  The goal is to identify the asymptotic
cutoff law that the remote-tail theorem must certify, not to extrapolate a
theorem from numerics.

For geometric cutoffs N, report:
  * C_e(N), C_o(N);
  * q_N = C_e/C_o and kappa_N = (C_o-C_e)/(C_o+C_e);
  * successive capacity increments;
  * empirical p from
        |C_N-C_{2N}| / |C_{2N}-C_{4N}| ~= 2^p;
  * Richardson-style diagnostic extrapolation using that empirical p.

Guardrail: no extrapolated value is promoted.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import mpmath as mp

from suzuki_ldd_refined_capacity_bracket import one_sector

HERE = Path(__file__).resolve().parent
OUT = HERE / "ldd_capacity_cutoff_sweep_result.json"

DEFAULT_CUTS = [192, 384, 768, 1536, 3072, 4000]


def as_mpf(row, key):
    v = row[key]
    if v is None:
        raise RuntimeError(("missing capacity", row["sector"], key))
    return mp.mpf(v)


def empirical_orders(values, cuts):
    out = []
    # Use consecutive doubling triples only.
    for i in range(len(cuts) - 2):
        n0, n1, n2 = cuts[i:i+3]
        if n1 != 2*n0 or n2 != 2*n1:
            continue
        c0, c1, c2 = values[i:i+3]
        d0 = c0 - c1
        d1 = c1 - c2
        if d0 == 0 or d1 == 0 or d0*d1 <= 0:
            out.append({
                "N": n0,
                "p": None,
                "reason": "increments vanish or change sign",
            })
            continue
        p = mp.log(abs(d0/d1), 2)
        if p <= 0:
            cinf = None
        else:
            cinf = c2 - d1 / (mp.power(2, p) - 1)
        out.append({
            "N": n0,
            "p": mp.nstr(p, 40),
            "Cinf_diagnostic": mp.nstr(cinf, 60) if cinf is not None else None,
            "d_N_2N": mp.nstr(d0, 60),
            "d_2N_4N": mp.nstr(d1, 60),
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cuts", default=",".join(str(x) for x in DEFAULT_CUTS))
    ap.add_argument("--dps", type=int, default=180)
    ap.add_argument("--refinements", type=int, default=1)
    args = ap.parse_args()

    cuts = [int(x) for x in args.cuts.split(",") if x.strip()]
    rows = []

    with mp.workdps(args.dps):
        for cut in cuts:
            print("\n=== cutoff", cut, "===")
            even = one_sector(cut, "even-v", args.dps, args.refinements)
            odd = one_sector(cut, "odd-v", args.dps, args.refinements)

            Ce = as_mpf(even, "capacity_midpoint_variational")
            Co = as_mpf(odd, "capacity_midpoint_variational")
            q = Ce / Co
            kap = (Co - Ce) / (Co + Ce)

            row = {
                "cutoff": cut,
                "even": even,
                "odd": odd,
                "Ce": mp.nstr(Ce, 60),
                "Co": mp.nstr(Co, 60),
                "q": mp.nstr(q, 60),
                "kappa": mp.nstr(kap, 60),
            }
            if rows:
                p = rows[-1]
                row["delta_Ce_from_previous"] = mp.nstr(
                    Ce - mp.mpf(p["Ce"]), 60
                )
                row["delta_Co_from_previous"] = mp.nstr(
                    Co - mp.mpf(p["Co"]), 60
                )
                row["delta_kappa_from_previous"] = mp.nstr(
                    kap - mp.mpf(p["kappa"]), 60
                )

            rows.append(row)
            print("Ce =", row["Ce"])
            print("Co =", row["Co"])
            print("q  =", row["q"])
            print("kap=", row["kappa"])

        Ce_vals = [mp.mpf(r["Ce"]) for r in rows]
        Co_vals = [mp.mpf(r["Co"]) for r in rows]
        kap_vals = [mp.mpf(r["kappa"]) for r in rows]

        out = {
            "cuts": cuts,
            "dps": args.dps,
            "refinements": args.refinements,
            "rows": rows,
            "empirical_orders": {
                "even_capacity": empirical_orders(Ce_vals, cuts),
                "odd_capacity": empirical_orders(Co_vals, cuts),
                "kappa": empirical_orders(kap_vals, cuts),
            },
            "guardrail": (
                "Finite-section convergence diagnostic only. Empirical powers "
                "and extrapolations are not proofs and are not promoted."
            ),
        }
        OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("\nEmpirical orders:")
    print(json.dumps(out["empirical_orders"], indent=2))
    print("\nwrote", OUT)
    print("GUARDRAIL:", out["guardrail"])


if __name__ == "__main__":
    main()
