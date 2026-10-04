#!/usr/bin/env python3
"""Separated far-tail geometric remainder diagnostic from the frozen N=4000 source solve.

v14.011 established that the immediate shell cannot be treated by a moment
expansion because m/n can approach 1.  This diagnostic instead freezes the
validated N=4000 finite source solution and samples only remote rows n>=16000,
so that

    max_{m<=4000} m/n <= 1/4.

For remote n,

    (z_n m - n z_m)/(n^2-m^2)

is expanded using

    1/(1-r^2) = sum_{j=0}^K r^(2j)
                + r^(2K+2)/(1-r^2),  r=m/n.

Define moments

    M_{2j+1} = sum_m m^(2j+1) x_m,
    Z_{2j}   = sum_m z_m m^(2j) x_m.

Then the K-th off-diagonal truncation is

    (2/pi) [
      z_n sum_{j=0}^K M_{2j+1}/n^(2j+2)
      -     sum_{j=0}^K Z_{2j}/n^(2j+1)
    ].

The source term and rank-one pole term are retained exactly.  The script:
  * reconstructs the N=4000 LDDD-refined source solution;
  * evaluates exact high-precision remote rows at 4N,5N,6N,8N,12N,16N;
  * compares K=0..4 moment truncations;
  * computes the exact geometric-series absolute remainder bound for the
    frozen numerical x_N.

Guardrail: the algebraic remainder formula is exact for the frozen numerical
payload, but x_N and scalar producer are not outward interval enclosures here.
This is a diagnostic/check-target for the analytic far-tail proof.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis,
    full_source_matrix,
)
from suzuki_ldd_source_operator import (
    LD,
    dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,
    ldd_to_mpf as dd_to_mpf,
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
from suzuki_ldd_remote_source_lead_diagnostic import (
    dd_linear_combination,
    direct_remote_residual_mp,
    pole_mp,
    source_mp,
    z_remote_mp,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "N4000_far_geometric_remainder_diagnostic_result.json"

N = 4000
DPS = 180
MAX_K = 4
SAMPLE_FACTORS = (4, 5, 6, 8, 12, 16)

CAP = {
    "even-v": mp.mpf(
        "7.5773007563692575306680936106689123586265630100827471120927e-30"
    ),
    "odd-v": mp.mpf(
        "2.1845239838296620020805542670090522874748063437543145074951e-25"
    ),
}


def parity_modes(sector: str):
    start = 1 if sector == "even-v" else 2
    return np.arange(start, N + 1, 2, dtype=int)


def reconstruct_source(sector: str):
    modes = parity_modes(sector)
    P, _ = frozen_protected_basis(sector, modes)

    Gh, Gl = dd_dot_columns(P, None, P, None)
    Gih, Gil, Gi_mp = mp_inverse_split(Gh, Gl, DPS)
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
        dps=DPS,
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
    Kt = form_Ktilde(data, Uh, Ul, AUh, AUl, DPS)

    with mp.workdps(DPS):
        S = Kt[:6, :6]
        g = -Kt[:6, 6]
        h = -Kt[6, 6]
        w = mp.lu_solve(S, g)
        G = h + (g.T * w)[0]
        C = 1 / G

        rel = abs(C - CAP[sector]) / CAP[sector]
        if rel > mp.mpf("1e-8"):
            raise RuntimeError(
                (
                    sector,
                    "N4000 capacity replay failed",
                    mp.nstr(C, 60),
                    mp.nstr(CAP[sector], 60),
                    mp.nstr(rel, 20),
                )
            )

        coeffs = [w[j] for j in range(6)] + [mp.mpf(1)]
        xh, xl = dd_linear_combination(Uh, Ul, coeffs)

        xmp = [dd_to_mpf(xh[i], xl[i]) for i in range(len(modes))]
        zmp = [
            dd_to_mpf(data.z_hi[i], data.z_lo[i])
            for i in range(len(modes))
        ]
        pmp = [
            dd_to_mpf(data.pole_hi[i], data.pole_lo[i])
            for i in range(len(modes))
        ]

    return {
        "modes": modes,
        "xmp": xmp,
        "zmp": zmp,
        "pmp": pmp,
        "C": C,
        "capacity_replay_relative_error": rel,
        "gamma_midpoint": gamma,
        "refined_max_joint_residual": max(norms1),
    }


def same_parity_n(sector: str, raw: int):
    # even-v uses odd Fourier modes; odd-v uses even Fourier modes.
    want_even = sector == "odd-v"
    n = int(raw)
    if (n % 2 == 0) != want_even:
        n += 1
    return n


def moments(state):
    with mp.workdps(DPS):
        out_M = []
        out_Z = []
        modes = [mp.mpf(int(m)) for m in state["modes"]]
        for j in range(MAX_K + 1):
            Mj = mp.fsum(
                (m ** (2*j + 1)) * x
                for m, x in zip(modes, state["xmp"])
            )
            Zj = mp.fsum(
                z * (m ** (2*j)) * x
                for m, z, x in zip(modes, state["zmp"], state["xmp"])
            )
            out_M.append(Mj)
            out_Z.append(Zj)
        P = mp.fsum(
            p*x for p, x in zip(state["pmp"], state["xmp"])
        )
    return out_M, out_Z, P


def approx_row(n: int, sector: str, Ms, Zs, P, K: int):
    with mp.workdps(DPS):
        nn = mp.mpf(n)
        zn = z_remote_mp(n)
        off = (2/mp.pi) * (
            zn * mp.fsum(
                Ms[j] / (nn ** (2*j + 2))
                for j in range(K + 1)
            )
            -
            mp.fsum(
                Zs[j] / (nn ** (2*j + 1))
                for j in range(K + 1)
            )
        )
        alpha = mp.mpf(2 if sector == "even-v" else -2)
        return source_mp(n) - off - alpha*pole_mp(n, sector)*P


def geometric_remainder_bound(n: int, state, K: int):
    """Exact absolute geometric-tail bound for frozen numerical x_N."""
    with mp.workdps(DPS):
        nn = mp.mpf(n)
        zn = abs(z_remote_mp(n))
        total = mp.mpf("0")
        rmax = mp.mpf(int(state["modes"][-1])) / nn
        if rmax >= 1:
            raise RuntimeError(("invalid far sample", n, rmax))

        for m0, x, z in zip(
            state["modes"], state["xmp"], state["zmp"]
        ):
            m = mp.mpf(int(m0))
            ratio = m/nn
            geom = ratio**(2*K+2) / (1-ratio**2)
            term = (
                zn * m/(nn**2)
                + abs(z)/nn
            ) * abs(x) * geom
            total += term

        return (2/mp.pi)*total, rmax


def one_sector(sector: str):
    print("\nreconstructing", sector)
    state = reconstruct_source(sector)
    Ms, Zs, P = moments(state)

    samples = []
    for fac in SAMPLE_FACTORS:
        n = same_parity_n(sector, fac*N)
        exact = direct_remote_residual_mp(
            n,
            sector,
            state["modes"],
            state["xmp"],
            state["zmp"],
            state["pmp"],
        )
        row = {
            "n": n,
            "factor": fac,
            "exact_residual": mp.nstr(exact, 70),
            "z_n": mp.nstr(z_remote_mp(n), 50),
            "truncations": [],
        }
        for K in range(MAX_K + 1):
            app = approx_row(n, sector, Ms, Zs, P, K)
            err = app-exact
            bound, rmax = geometric_remainder_bound(n, state, K)
            row["truncations"].append({
                "K": K,
                "approx": mp.nstr(app, 70),
                "error": mp.nstr(err, 60),
                "absolute_error": mp.nstr(abs(err), 60),
                "relative_error": mp.nstr(
                    abs(err)/max(abs(exact), mp.mpf("1e-300")), 40
                ),
                "geometric_abs_bound": mp.nstr(bound, 60),
                "error_over_bound": mp.nstr(
                    abs(err)/bound if bound else mp.mpf("0"), 40
                ),
                "max_m_over_n": mp.nstr(rmax, 30),
            })
        samples.append(row)
        print(
            sector,
            "n",
            n,
            "K0 rel",
            row["truncations"][0]["relative_error"],
            "K2 rel",
            row["truncations"][2]["relative_error"],
            "K4 rel",
            row["truncations"][4]["relative_error"],
        )

    return {
        "sector": sector,
        "N": N,
        "capacity": mp.nstr(state["C"], 70),
        "capacity_replay_relative_error": mp.nstr(
            state["capacity_replay_relative_error"], 30
        ),
        "complement_floor_midpoint": state["gamma_midpoint"],
        "refined_max_joint_residual": state["refined_max_joint_residual"],
        "moments_M": [mp.nstr(v, 70) for v in Ms],
        "moments_Z": [mp.nstr(v, 70) for v in Zs],
        "pole_moment": mp.nstr(P, 70),
        "samples": samples,
    }


def main():
    rows = [one_sector("even-v"), one_sector("odd-v")]
    out = {
        "N": N,
        "dps": DPS,
        "max_K": MAX_K,
        "sample_factors": SAMPLE_FACTORS,
        "rows": rows,
        "guardrail": (
            "Separated far-tail diagnostic for the frozen numerical N=4000 "
            "source solution. Geometric remainder formulas are algebraically "
            "exact for that frozen payload, but the source solution and scalar "
            "producer are not outward intervals here."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("\nwrote", OUT)
    print("GUARDRAIL:", out["guardrail"])


if __name__ == "__main__":
    main()
