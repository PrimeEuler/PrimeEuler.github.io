#!/usr/bin/env python3
"""Compute a crude rigorous-formula candidate C_rho for the normalized far residual.

For the finite N=4000 source solution x_N and remote n>=2N, retain exactly

    r_n = L/n - (2/pi)<m,x_N> z_n/n^2 + rho_n.

Using |z_n|<=ZMAX and m/n<=1/2, the denominator remainder gives

 |rho_n| <= C_raw / n^3,

with

 C_raw <= C_source
        + (8/(3*pi)) [
              sum_m |z_m| m^2 |x_m|
            + (ZMAX/(2N)) sum_m m^3 |x_m|
          ]
        + |alpha| (4 g/pi^3) |<p,x_m>|.

The source term is bounded by
    C_source = 4 |f_lead|/pi^2.

For the unit-energy residual used by v14.016,
    y_N = sqrt(C_N) x_N,
so
    |rho_tilde_n| <= C_rho / n^3,
    C_rho = sqrt(C_N) C_raw.

This is intentionally crude and uses absolute values only after the
sign-carrying L/n and z_n/n^2 terms have been retained.  It is designed as
the finite residual constant requested in v14.016/v14.017.

Diagnostic/candidate bound: it still inherits the finite-section midpoint
source solution unless paired with the final outward finite-data enclosure.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from suzuki_ldd_remote_source_lead_diagnostic import (
    dd_linear_combination,
    dd_dot_to_mp,
)
from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis,
    full_source_matrix,
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement,
    dd_project,
    form_Ktilde,
    form_trial,
    mp_inverse_split,
    refine_once,
    residuals_dd,
)
from suzuki_ldd_source_operator import (
    LD,
    dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,
    ldd_to_mpf,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "N4000_normalized_far_residual_constant_result.json"
N = 4000
ZMAX = mp.mpf(8)


def refined_state(sector: str, dps: int = 180):
    modes = np.arange(
        1 if sector == "even-v" else 2,
        N + 1,
        2,
        dtype=int,
    )
    P, _ = frozen_protected_basis(sector, modes)
    Gh, Gl = dd_dot_columns(P, None, P, None)
    Gih, Gil, Gi_mp = mp_inverse_split(Gh, Gl, dps)
    Gi = np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A, f = full_source_matrix(modes, sector)
    op, proj, gamma, evals, Y0, yf0, initial_res = build_double_complement(
        A, P, Gi, f, rtol=2e-14
    )
    data = hp_parity_data(
        modes, sector, dps=dps, arch_terms=160, correction_terms=50
    )

    Yh = Y0.astype(LD)
    Yl = np.zeros_like(Yh, dtype=LD)
    yfh = yf0.astype(LD)
    yfl = np.zeros_like(yfh, dtype=LD)
    Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)
    yfh, yfl = dd_project(P, Gih, Gil, yfh, yfl)

    Uh, Ul = form_trial(P, Yh, Yl, yfh, yfl)
    AUh, AUl, Rh, Rl, norms0 = residuals_dd(
        data, P, Gih, Gil, Uh, Ul
    )
    Yh, Yl, yfh, yfl = refine_once(
        op, proj, Yh, Yl, yfh, yfl, Rh, Rl
    )
    Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)
    yfh, yfl = dd_project(P, Gih, Gil, yfh, yfl)
    Uh, Ul = form_trial(P, Yh, Yl, yfh, yfl)
    AUh, AUl, Rh, Rl, norms1 = residuals_dd(
        data, P, Gih, Gil, Uh, Ul
    )
    Kt = form_Ktilde(data, Uh, Ul, AUh, AUl, dps)

    with mp.workdps(dps):
        S = Kt[:6,:6]
        gvec = -Kt[:6,6]
        h = -Kt[6,6]
        w = mp.lu_solve(S, gvec)
        G = h + (gvec.T*w)[0]
        C = 1/G
        coeffs = [w[j] for j in range(6)] + [mp.mpf(1)]
        xh, xl = dd_linear_combination(Uh, Ul, coeffs)
        xmp = [ldd_to_mpf(xh[i], xl[i]) for i in range(len(modes))]
        zmp = [ldd_to_mpf(data.z_hi[i], data.z_lo[i]) for i in range(len(modes))]
        pmp = [ldd_to_mpf(data.pole_hi[i], data.pole_lo[i]) for i in range(len(modes))]

        return modes, xmp, zmp, pmp, C, gamma, max(norms1)


def one_sector(sector: str, dps: int = 180):
    modes, x, z, p, C, gamma, rnorm = refined_state(sector, dps)
    with mp.workdps(dps):
        if sector == "even-v":
            alpha = mp.mpf(2)
            gp = mp.cosh(mp.mpf("0.5"))
            f_lead = 4*mp.cosh(1)/mp.pi
        else:
            alpha = mp.mpf(-2)
            gp = mp.sinh(mp.mpf("0.5"))
            f_lead = -4*mp.sinh(1)/mp.pi

        s_zm2 = mp.fsum(abs(zi) * (mp.mpf(int(m))**2) * abs(xi)
                        for m,zi,xi in zip(modes,z,x))
        s_m3 = mp.fsum((mp.mpf(int(m))**3) * abs(xi)
                       for m,xi in zip(modes,x))
        px = mp.fsum(pi*xi for pi,xi in zip(p,x))

        C_source = 4*abs(f_lead)/(mp.pi**2)
        C_cauchy = (mp.mpf(8)/(3*mp.pi)) * (
            s_zm2 + (ZMAX/(2*N))*s_m3
        )
        C_pole = abs(alpha) * (4*gp/(mp.pi**3)) * abs(px)
        C_raw = C_source + C_cauchy + C_pole
        C_rho = mp.sqrt(C) * C_raw

        # Useful asymptotic tail norms for n>=2N on one parity lattice.
        n0 = mp.mpf(2*N)
        # Crude sum over same parity: sum n^-6 <= 1/(2) * integral_{n0-2}∞ x^-6 dx
        tail_l2_sq_bound = (C_rho**2) / (10 * (n0-2)**5)

        return {
            "sector": sector,
            "capacity": mp.nstr(C, 60),
            "sqrt_capacity": mp.nstr(mp.sqrt(C), 50),
            "C_source_raw": mp.nstr(C_source, 50),
            "sum_abs_z_m2_x": mp.nstr(s_zm2, 50),
            "sum_abs_m3_x": mp.nstr(s_m3, 50),
            "pole_dot_x": mp.nstr(px, 50),
            "C_cauchy_raw": mp.nstr(C_cauchy, 50),
            "C_pole_raw": mp.nstr(C_pole, 50),
            "C_raw": mp.nstr(C_raw, 60),
            "C_rho_unit_energy": mp.nstr(C_rho, 60),
            "far_rho_l2_sq_bound_n_ge_2N": mp.nstr(tail_l2_sq_bound, 60),
            "midpoint_complement_floor": gamma,
            "refined_joint_residual": rnorm,
        }


def main():
    rows = [one_sector("even-v"), one_sector("odd-v")]
    out = {
        "N": N,
        "far_start": 2*N,
        "ZMAX": str(ZMAX),
        "rows": rows,
        "guardrail": (
            "Crude finite-data C_rho candidate. Formula is analytic once the "
            "finite moments/capacity are outward enclosed; current values use "
            "the validated LDDD midpoint source solution."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True)+"\n")
    for row in rows:
        print("\nsector =", row["sector"])
        for k,v in row.items():
            if k != "sector":
                print(k, "=", v)
    print("\nwrote", OUT)


if __name__ == "__main__":
    main()
