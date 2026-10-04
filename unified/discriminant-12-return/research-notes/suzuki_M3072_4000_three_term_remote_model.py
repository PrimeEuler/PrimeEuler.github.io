#!/usr/bin/env python3
"""Three-term remote residual model on the N=3072 -> M=4000 shell.

Using the exact large-n expansion of the source-faithful row,

  r_n
   = L/n
     - (2/pi) <m,x> z_n/n^2
     + B3/n^3
     + O(z_n/n^4) + O(n^-5),

where

  B3 = f3 + (2/pi)<m^2 z,x> + alpha*(4 g/pi^3)<p,x>,

and
  f3_even = -16 cosh(1)/pi^3,
  f3_odd  = +16 sinh(1)/pi^3.

This tests whether the first three explicit source moments account for the
remote shell correction and parity difference.

Guardrail: midpoint diagnostic only.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from suzuki_M3072_4000_remote_residual_decomposition import (
    CAP,
    M,
    N,
    parity_shell,
    refined_solution,
    tail_solve,
)
from suzuki_ldd_remote_source_lead_diagnostic import direct_remote_residual_mp
from suzuki_endpoint_M3999_midpoint_effective_core import endpoint_data

HERE = Path(__file__).resolve().parent
OUT = HERE / "M3072_4000_three_term_remote_model_result.json"


def one_sector(sector: str, dps: int = 180):
    state = refined_solution(sector, dps=dps)
    modes = state["modes"]
    shell = parity_shell(sector)

    with mp.workdps(dps):
        M1 = mp.fsum(
            mp.mpf(int(m)) * x
            for m, x in zip(modes, state["xmp"])
        )
        Z2 = mp.fsum(
            (mp.mpf(int(m))**2) * z * x
            for m, z, x in zip(modes, state["zmp"], state["xmp"])
        )
        Px = mp.fsum(p*x for p, x in zip(state["pmp"], state["xmp"]))

        L = state["L"]
        if sector == "even-v":
            alpha = mp.mpf(2)
            g0 = mp.cosh(mp.mpf("0.5"))
            f3 = -16*mp.cosh(1)/(mp.pi**3)
        else:
            alpha = mp.mpf(-2)
            g0 = mp.sinh(mp.mpf("0.5"))
            f3 = 16*mp.sinh(1)/(mp.pi**3)

        B3 = f3 + (2/mp.pi)*Z2 + alpha*(4*g0/(mp.pi**3))*Px

        Cn = CAP[sector][N]
        Cm = CAP[sector][M]
        eta_exact = Cn/Cm - 1

    z_shell, _ = endpoint_data(shell, sign=-1, rho=0.0)
    nf = shell.astype(float)

    Lf = float(L)
    M1f = float(M1)
    B3f = float(B3)

    r1 = Lf/nf
    r2 = r1 - (2.0/np.pi)*M1f*z_shell/(nf*nf)
    r3 = r2 + B3f/(nf**3)

    D1, den = tail_solve(shell, sector, r1)
    D2, den2 = tail_solve(shell, sector, r2)
    D3, den3 = tail_solve(shell, sector, r3)
    if max(abs(den-den2), abs(den-den3)) > 1e-12:
        raise RuntimeError("Woodbury denominator mismatch")

    eta1 = float(Cn) * float(r1 @ D1)
    eta2 = float(Cn) * float(r2 @ D2)
    eta3 = float(Cn) * float(r3 @ D3)

    idx = [0, len(shell)//2, len(shell)-1]
    checks = []
    for j in idx:
        n = int(shell[j])
        nn = mp.mpf(n)
        rr = direct_remote_residual_mp(
            n, sector, modes, state["xmp"], state["zmp"], state["pmp"]
        )
        zn = mp.mpf(str(z_shell[j]))
        a1 = L/nn
        a2 = a1 - (2/mp.pi)*M1*zn/(nn**2)
        a3 = a2 + B3/(nn**3)
        checks.append({
            "n": n,
            "actual": mp.nstr(rr, 50),
            "one_term": mp.nstr(a1, 50),
            "two_term": mp.nstr(a2, 50),
            "three_term": mp.nstr(a3, 50),
            "one_relerr": mp.nstr((a1-rr)/rr, 30),
            "two_relerr": mp.nstr((a2-rr)/rr, 30),
            "three_relerr": mp.nstr((a3-rr)/rr, 30),
        })

    return {
        "sector": sector,
        "M1_moment": mp.nstr(M1, 60),
        "Z2_moment": mp.nstr(Z2, 60),
        "Px_moment": mp.nstr(Px, 60),
        "L": mp.nstr(L, 60),
        "B3": mp.nstr(B3, 60),
        "eta_exact": mp.nstr(eta_exact, 50),
        "eta_one_term_D": eta1,
        "eta_two_term_D": eta2,
        "eta_three_term_D": eta3,
        "one_fraction_exact": eta1/float(eta_exact),
        "two_fraction_exact": eta2/float(eta_exact),
        "three_fraction_exact": eta3/float(eta_exact),
        "three_minus_two": eta3-eta2,
        "woodbury_denominator": den,
        "remote_row_checks": checks,
    }


def main():
    rows = []
    for sector in ("even-v", "odd-v"):
        print("\n===", sector, "===")
        row = one_sector(sector)
        rows.append(row)
        for k, v in row.items():
            if k != "sector":
                print(k, "=", v)

    e, o = rows
    paired = {
        "eta_exact_odd_minus_even": float(
            mp.mpf(o["eta_exact"])-mp.mpf(e["eta_exact"])
        ),
        "one_term_odd_minus_even": (
            o["eta_one_term_D"]-e["eta_one_term_D"]
        ),
        "two_term_odd_minus_even": (
            o["eta_two_term_D"]-e["eta_two_term_D"]
        ),
        "three_term_odd_minus_even": (
            o["eta_three_term_D"]-e["eta_three_term_D"]
        ),
    }

    out = {
        "rows": rows,
        "paired": paired,
        "guardrail": "Midpoint three-term asymptotic diagnostic only.",
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("\nPAIRED")
    print(json.dumps(paired, indent=2))
    print("\nwrote", OUT)


if __name__ == "__main__":
    main()
