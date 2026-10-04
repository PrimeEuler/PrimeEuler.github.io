#!/usr/bin/env python3
"""Test the first arithmetic subleading term in the N=3072 remote residual.

For remote n above the finite source solution support,

  r_n = f_n - (A x_N)_n

has the expansion

  r_n = L_N/n
        - (2/pi) <m,x_N> z_n/n^2
        + O(n^-3),

because

  (z_n m - n z_m)/(n^2-m^2)
   = -z_m/n + z_n m/n^2 - z_m m^2/n^3 + ...

The second term is arithmetic/oscillatory through z_n.  This script
reconstructs the LDDD N=3072 source solution, evaluates the moment
<m,x_N>, and compares the standalone remote-shell quadratic energy of:
  * one-term L/n;
  * two-term L/n - (2/pi)<m,x> z_n/n^2;
against the exact nested capacity increment through M=4000.

It also checks a few actual high-precision remote rows inside the shell.

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
OUT = HERE / "M3072_4000_two_term_remote_model_result.json"


def one_sector(sector: str, dps: int = 120):
    state = refined_solution(sector, dps=dps)
    modes = state["modes"]
    shell = parity_shell(sector)

    with mp.workdps(dps):
        moment_m = mp.fsum(
            mp.mpf(int(m)) * x
            for m, x in zip(modes, state["xmp"])
        )
        L = state["L"]
        Cn = CAP[sector][N]
        Cm = CAP[sector][M]
        eta_exact = Cn/Cm - 1

    z_shell, _ = endpoint_data(shell, sign=-1, rho=0.0)
    nf = shell.astype(float)
    Lf = float(L)
    M1f = float(moment_m)

    r1 = Lf / nf
    r2 = r1 - (2.0/np.pi) * M1f * z_shell / (nf*nf)

    D1, den = tail_solve(shell, sector, r1)
    D2, den2 = tail_solve(shell, sector, r2)
    if abs(den-den2) > 1e-12:
        raise RuntimeError("Woodbury denominator mismatch")

    eta1 = float(Cn) * float(r1 @ D1)
    eta2 = float(Cn) * float(r2 @ D2)

    # Three direct mp rows inside the actual shell.
    idx = [0, len(shell)//2, len(shell)-1]
    checks = []
    for j in idx:
        n = int(shell[j])
        rr = direct_remote_residual_mp(
            n, sector, modes, state["xmp"], state["zmp"], state["pmp"]
        )
        a1 = L / mp.mpf(n)
        zn = mp.mpf(str(z_shell[j]))
        a2 = a1 - (2/mp.pi)*moment_m*zn/(mp.mpf(n)**2)
        checks.append({
            "n": n,
            "actual": mp.nstr(rr, 50),
            "one_term": mp.nstr(a1, 50),
            "two_term": mp.nstr(a2, 50),
            "one_term_relative_error": mp.nstr((a1-rr)/rr, 30),
            "two_term_relative_error": mp.nstr((a2-rr)/rr, 30),
        })

    return {
        "sector": sector,
        "moment_m_dot_x": mp.nstr(moment_m, 60),
        "L": mp.nstr(L, 60),
        "C_N": mp.nstr(Cn, 60),
        "eta_exact": mp.nstr(eta_exact, 50),
        "eta_one_term_D": eta1,
        "eta_two_term_D": eta2,
        "one_term_fraction_of_exact": eta1/float(eta_exact),
        "two_term_fraction_of_exact": eta2/float(eta_exact),
        "two_minus_one": eta2-eta1,
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
        "eta_exact_odd_minus_even": float(mp.mpf(o["eta_exact"])-mp.mpf(e["eta_exact"])),
        "one_term_odd_minus_even": o["eta_one_term_D"]-e["eta_one_term_D"],
        "two_term_odd_minus_even": o["eta_two_term_D"]-e["eta_two_term_D"],
    }

    out = {
        "rows": rows,
        "paired": paired,
        "guardrail": "Midpoint two-term asymptotic diagnostic only.",
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("\nPAIRED")
    print(json.dumps(paired, indent=2))
    print("\nwrote", OUT)


if __name__ == "__main__":
    main()
