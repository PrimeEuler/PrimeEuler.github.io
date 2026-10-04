#!/usr/bin/env python3
"""Remote 1/n coefficient of the LDDD-refined finite source solution.

For the finite Galerkin source solution x_N,

    r_n = f_n - (A x_N)_n

has a source-faithful large-n expansion

    r_n = L_N/n + O(log(n)/n^2).

The exact leading coefficient is

    L_N = f_lead
          + (2/pi)<z,x_N>
          - alpha*(4*g0/pi)<p,x_N>,

where g0=cosh(1/2) in even-v and sinh(1/2) in odd-v, while
f_lead=4*cosh(1)/pi in even-v and -4*sinh(1)/pi in odd-v.

This diagnostic reconstructs x_N from the same refined protected/complement
state used by v14.008, evaluates L_N in longdouble double-double arithmetic,
and reports the projectively normalized coefficient

    A_N := C_N * L_N^2.

If A_N has a common parity limit, the leading remote source-energy correction
is common-mode and cancels from the capacity quotient at first order.

Direct high-precision remote rows at several multiples of the cutoff verify
the asymptotic sign/coefficient.

Guardrail: finite-section diagnostic only.  No remote Schur inverse
approximation or infinite-tail theorem is asserted.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis,
    full_source_matrix,
)
from suzuki_doubledouble_source_operator import QS
from suzuki_ldd_source_operator import (
    LD,
    add as dd_add,
    dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,
    ldd_to_mpf as dd_to_mpf,
    mul as dd_mul,
    split_mpf_ld as split_mpf,
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement,
    dd_matrix_to_mp,
    dd_project,
    form_Ktilde,
    form_trial,
    mp_inverse_split,
    refine_once,
    residuals_dd,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "ldd_remote_source_lead_diagnostic_result.json"


def z_remote_mp(n: int, correction_terms: int = 50):
    nmp = mp.mpf(n)
    weights = (
        mp.log(2) / mp.sqrt(2),
        mp.log(3) / mp.sqrt(3),
        mp.log(2) / 2,
        mp.log(5) / mp.sqrt(5),
        mp.log(7) / mp.sqrt(7),
    )
    prime = mp.fsum(
        w * mp.sin(nmp * mp.pi * mp.log(q) / 2)
        for q, w in zip(QS, weights)
    )
    k = nmp * mp.pi / 2
    parity = mp.mpf(1 if n % 2 == 0 else -1)
    corr = mp.fsum(
        mp.e ** (-2 * (2*j + mp.mpf("0.5")))
        /
        ((2*j + mp.mpf("0.5"))**2 + k*k)
        for j in range(correction_terms)
    )
    return (
        2 * prime
        + mp.im(mp.digamma(mp.mpf("0.25") + 1j*nmp*mp.pi/4))
        - parity*nmp*mp.pi*corr
    )


def source_mp(n: int):
    nmp = mp.mpf(n)
    k = nmp * mp.pi / 2
    parity = mp.mpf(1 if n % 2 == 0 else -1)
    return k * (mp.e**(-1) - parity*mp.e) / (1 + k*k)


def pole_mp(n: int, sector: str):
    k = mp.mpf(n) * mp.pi / 2
    if sector == "even-v":
        return 2*k*mp.cosh(mp.mpf("0.5"))/(k*k+mp.mpf("0.25"))
    if sector == "odd-v":
        return 2*k*mp.sinh(mp.mpf("0.5"))/(k*k+mp.mpf("0.25"))
    raise ValueError(sector)


def dd_linear_combination(Uh, Ul, coeffs):
    n, r = Uh.shape
    xh = np.zeros(n, dtype=LD)
    xl = np.zeros(n, dtype=LD)
    for j in range(r):
        ch, cl = split_mpf(coeffs[j])
        ph, pl = dd_mul(Uh[:, j], Ul[:, j], ch, cl)
        xh, xl = dd_add(xh, xl, ph, pl)
    return xh, xl


def dd_dot_to_mp(ah, al, bh, bl):
    H, L = dd_dot_columns(
        np.asarray(ah)[:, None],
        np.asarray(al)[:, None],
        np.asarray(bh)[:, None],
        np.asarray(bl)[:, None],
    )
    return dd_to_mpf(H[0, 0], L[0, 0])


def same_parity_remote(last_mode: int, factor: int, sector: str):
    n = int(factor * last_mode)
    want_even = sector == "odd-v"
    if (n % 2 == 0) != want_even:
        n += 1
    if n <= last_mode:
        n = last_mode + 2
    return n


def direct_remote_residual_mp(
    n: int,
    sector: str,
    modes: np.ndarray,
    xmp,
    zmp,
    pmp,
):
    nmp = mp.mpf(n)
    zn = z_remote_mp(n)
    pn = pole_mp(n, sector)
    alpha = mp.mpf(2 if sector == "even-v" else -2)

    s = mp.fsum(
        (
            (mp.mpf(2)/mp.pi)
            * (zn*mp.mpf(int(m)) - nmp*zj)
            / (nmp*nmp - mp.mpf(int(m))**2)
            + alpha * pn * pj
        ) * xj
        for m, xj, zj, pj in zip(modes, xmp, zmp, pmp)
    )
    return source_mp(n) - s


def refined_source_state(max_mode: int, sector: str, dps: int):
    modes = np.arange(
        1 if sector == "even-v" else 2,
        max_mode + 1,
        2,
        dtype=int,
    )
    P, _ = frozen_protected_basis(sector, modes)

    Gh, Gl = dd_dot_columns(P, None, P, None)
    Gih, Gil, Gi_mp = mp_inverse_split(Gh, Gl, dps)
    Gi = np.array(
        [[float(Gi_mp[i, j]) for j in range(6)] for i in range(6)]
    )

    A, f = full_source_matrix(modes, sector)
    op, proj, gamma, evals, Y0, yf0, initial_res = build_double_complement(
        A, P, Gi, f, rtol=2e-14
    )

    data = hp_parity_data(
        modes,
        sector,
        dps=dps,
        arch_terms=160,
        correction_terms=50,
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
        S = Kt[:6, :6]
        g = -Kt[:6, 6]
        h = -Kt[6, 6]
        w = mp.lu_solve(S, g)
        G = h + (g.T*w)[0]
        C = 1/G

        coeffs = [w[j] for j in range(6)] + [mp.mpf(1)]
        xh, xl = dd_linear_combination(Uh, Ul, coeffs)

        zx = dd_dot_to_mp(data.z_hi, data.z_lo, xh, xl)
        px = dd_dot_to_mp(data.pole_hi, data.pole_lo, xh, xl)

        alpha = mp.mpf(2 if sector == "even-v" else -2)
        if sector == "even-v":
            f_lead = 4*mp.cosh(1)/mp.pi
            g0 = mp.cosh(mp.mpf("0.5"))
        else:
            f_lead = -4*mp.sinh(1)/mp.pi
            g0 = mp.sinh(mp.mpf("0.5"))

        L = f_lead + (2/mp.pi)*zx - alpha*(4*g0/mp.pi)*px
        normalized = C * L * L

        xmp = [dd_to_mpf(xh[i], xl[i]) for i in range(len(modes))]
        zmp = [dd_to_mpf(data.z_hi[i], data.z_lo[i]) for i in range(len(modes))]
        pmp = [dd_to_mpf(data.pole_hi[i], data.pole_lo[i]) for i in range(len(modes))]

        samples = []
        for fac in (2, 4, 8):
            nn = same_parity_remote(int(modes[-1]), fac, sector)
            rr = direct_remote_residual_mp(
                nn, sector, modes, xmp, zmp, pmp
            )
            samples.append({
                "n": nn,
                "residual": mp.nstr(rr, 50),
                "n_times_residual": mp.nstr(mp.mpf(nn)*rr, 50),
                "ratio_to_L": mp.nstr(mp.mpf(nn)*rr/L, 40),
            })

        return {
            "sector": sector,
            "max_mode_requested": max_mode,
            "last_mode": int(modes[-1]),
            "dimension": len(modes),
            "capacity": mp.nstr(C, 60),
            "energy": mp.nstr(G, 60),
            "source_solution_2norm_diagnostic": mp.nstr(
                mp.sqrt(mp.fsum(v*v for v in xmp)), 40
            ),
            "z_dot_x": mp.nstr(zx, 60),
            "pole_dot_x": mp.nstr(px, 60),
            "remote_leading_coefficient_L": mp.nstr(L, 60),
            "C_times_L_squared": mp.nstr(normalized, 60),
            "initial_max_joint_residual": max(norms0),
            "refined_max_joint_residual": max(norms1),
            "complement_floor_midpoint": gamma,
            "remote_row_checks": samples,
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cuts", default="768,1536,3072,4000")
    ap.add_argument("--dps", type=int, default=180)
    args = ap.parse_args()

    cuts = [int(x) for x in args.cuts.split(",") if x.strip()]
    rows = []

    for cut in cuts:
        print("\n=== cutoff", cut, "===")
        for sector in ("even-v", "odd-v"):
            row = refined_source_state(cut, sector, args.dps)
            rows.append(row)
            print("\nsector =", sector)
            print("C =", row["capacity"])
            print("L =", row["remote_leading_coefficient_L"])
            print("C L^2 =", row["C_times_L_squared"])
            print("remote checks =", row["remote_row_checks"])

    # Pair the parity-normalized leading coefficients.
    pairs = []
    for cut in cuts:
        ee = next(r for r in rows if r["max_mode_requested"] == cut and r["sector"] == "even-v")
        oo = next(r for r in rows if r["max_mode_requested"] == cut and r["sector"] == "odd-v")
        Ae = mp.mpf(ee["C_times_L_squared"])
        Ao = mp.mpf(oo["C_times_L_squared"])
        pairs.append({
            "cutoff": cut,
            "A_even": mp.nstr(Ae, 60),
            "A_odd": mp.nstr(Ao, 60),
            "A_odd_minus_even": mp.nstr(Ao-Ae, 60),
            "A_odd_over_even": mp.nstr(Ao/Ae, 50) if Ae != 0 else None,
        })

    out = {
        "cuts": cuts,
        "dps": args.dps,
        "rows": rows,
        "paired_normalized_leads": pairs,
        "guardrail": (
            "Finite-section remote-leading-coefficient diagnostic only. "
            "No remote Schur inverse or infinite-tail theorem is asserted."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("\npaired normalized leading coefficients")
    print(json.dumps(pairs, indent=2))
    print("\nwrote", OUT)
    print("GUARDRAIL:", out["guardrail"])


if __name__ == "__main__":
    main()
