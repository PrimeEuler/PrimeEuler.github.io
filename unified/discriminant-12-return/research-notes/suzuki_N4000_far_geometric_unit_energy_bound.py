#!/usr/bin/env python3
"""Uniform unit-energy far geometric remainder bound after signed moments.

This is the sharp replacement for the unusable absolute C_rho experiment in
v14.019.

Freeze the validated N=4000 source solution.  For remote same-parity modes
n>=2N, expand only the Cauchy denominator

    1/(n^2-m^2)

through moment order K, retaining the signed moment channels exactly.
The remaining off-diagonal geometric tail obeys, with r=m/n<=1/2,

 |R_K(n)| <= (2/pi)/(1-1/4) [
      ZMAX * S_{2K+3} / n^(2K+4)
      + SZ_{2K+2} / n^(2K+3)
 ],

where
  S_j  = sum m^j |x_m|,
  SZ_j = sum |z_m| m^j |x_m|.

The source and pole pieces are retained exactly and contribute no geometric
remainder here.

Multiplying by sqrt(C_N) gives the unit-energy row remainder.  This script
converts the row envelope into a rigorous same-parity l2 sum bound using

 sum_{n=n0,n0+2,...} n^{-p}
 <= n0^{-p} + [2(p-1)]^{-1} n0^{-(p-1)}.

It reports K=0..10 at far starts 2N and 4N.

Guardrail: the geometric inequality is exact for the frozen numerical x_N.
The finite source moments/capacity are still midpoint LDDD values rather than
outward intervals; the output is a sharp certificate target, not final proof.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

from suzuki_N4000_far_geometric_remainder_diagnostic import (
    N,
    DPS,
    reconstruct_source,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "N4000_far_geometric_unit_energy_bound_result.json"

ZMAX = mp.mpf(8)
MAX_K = 10


def parity_sum_power_bound(n0: mp.mpf, p: int):
    return n0**(-p) + n0**(-(p-1)) / (2 * (p-1))


def one_sector(sector: str):
    state = reconstruct_source(sector)
    with mp.workdps(DPS):
        sqrtC = mp.sqrt(state["C"])
        modes = [mp.mpf(int(m)) for m in state["modes"]]
        ax = [abs(x) for x in state["xmp"]]
        az = [abs(z) for z in state["zmp"]]

        rows = []
        for far_factor in (2, 4):
            n0 = mp.mpf(far_factor * N)
            rmax = mp.mpf(N) / n0
            denom = 1 / (1-rmax*rmax)

            for K in range(MAX_K + 1):
                jz = 2*K + 2
                jm = 2*K + 3

                SZ = mp.fsum(
                    zz * (m**jz) * xx
                    for m, zz, xx in zip(modes, az, ax)
                )
                S = mp.fsum(
                    (m**jm) * xx
                    for m, xx in zip(modes, ax)
                )

                # Unit-energy envelope:
                # |sqrt(C) R(n)| <= A/n^(2K+3) + B/n^(2K+4).
                A = sqrtC * (2/mp.pi) * denom * SZ
                B = sqrtC * (2/mp.pi) * denom * ZMAX * S
                pA = 2*K + 3

                # Square via (a+b)^2 <= 2a^2+2b^2.
                l2sq = (
                    2*A*A*parity_sum_power_bound(n0, 2*pA)
                    +
                    2*B*B*parity_sum_power_bound(n0, 2*(pA+1))
                )
                row0 = A/n0**pA + B/n0**(pA+1)

                rows.append({
                    "far_factor": far_factor,
                    "far_start": int(n0),
                    "K": K,
                    "moment_power_z_abs": jz,
                    "moment_power_plain_abs": jm,
                    "A_unit": mp.nstr(A, 50),
                    "B_unit": mp.nstr(B, 50),
                    "unit_row_bound_at_far_start": mp.nstr(row0, 50),
                    "unit_l2_sq_bound": mp.nstr(l2sq, 50),
                    "unit_l2_bound": mp.nstr(mp.sqrt(l2sq), 50),
                })

        return {
            "sector": sector,
            "capacity": mp.nstr(state["C"], 60),
            "sqrt_capacity": mp.nstr(sqrtC, 50),
            "rows": rows,
        }


def main():
    sectors = [one_sector("even-v"), one_sector("odd-v")]
    out = {
        "N": N,
        "ZMAX": str(ZMAX),
        "max_K": MAX_K,
        "sectors": sectors,
        "guardrail": (
            "Exact geometric inequality for the frozen numerical N=4000 source "
            "solution; finite moments/capacity remain midpoint LDDD values."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True)+"\n")

    for sec in sectors:
        print("\nsector =", sec["sector"])
        for row in sec["rows"]:
            if row["K"] in (0,2,4,6,8,10):
                print(
                    "far", row["far_factor"],
                    "K", row["K"],
                    "row0", row["unit_row_bound_at_far_start"],
                    "l2", row["unit_l2_bound"],
                )
    print("\nwrote", OUT)
    print("GUARDRAIL:", out["guardrail"])


if __name__ == "__main__":
    main()
