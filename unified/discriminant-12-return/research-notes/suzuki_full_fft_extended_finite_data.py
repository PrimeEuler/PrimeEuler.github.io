#!/usr/bin/env python3
"""Extended fixed-full-lattice finite data for the correlated infinite-tail bound.

This is the Lane-A finite-data producer requested by v14.069/v14.070.
It reuses the calibrated fixed full-lattice FFT operator from
suzuki_full_fft_fixed_capacity_replay.py and NEVER uses the old transported
remote-Schur front response.

For one parity and cutoff N it computes, from one shared fixed operator:
  * the refined source capacity C_N;
  * the remote leading coefficient L_N;
  * A_N = C_N L_N^2 and sign(L_N);
  * the direct leading-coupling quadratic form
        M_{p,11} = w1_p^T A_{p,N}^{-1} w1_p,
    with w1_p = -(2/pi)z + alpha_p(4 g_p/pi)p_p;
  * binary64-CG and LDDD residual diagnostics.

The theorem-level remote coercivity input is NOT recomputed here:
v14.044/v14.046 promote S_{p,4000} >= I.  For N>=4000, the later remote
operator is the exact Schur complement obtained by eliminating the finite
slice 4000<n<=N, and therefore S_{p,N} >= I by the variational
characterization of the Schur complement.

Diagnostic finite midpoints only until outward source/capacity radii are added.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.sparse.linalg import cg

from suzuki_full_fft_fixed_capacity_replay import fixed_operator, DPS, ARCH
from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import embedded_P, modes_for
from suzuki_ldd_refined_capacity_bracket import (
    dd_project,
    form_Ktilde,
    form_trial,
    mp_inverse_split,
    refine_once,
    residuals_dd,
)
from suzuki_ldd_source_operator import (
    LD,
    add as dd_add,
    dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,
    ldd_to_mpf,
)
from suzuki_ldd_remote_source_lead_diagnostic import (
    dd_linear_combination,
    dd_dot_to_mp,
)
from suzuki_ldd_M11_direct_difference import (
    w1_dd,
    generic_residuals,
    generic_Ktilde,
    energy_from_K,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "full_fft_extended_finite_data_result.json"


def solve_one(sector: str, cutoff: int):
    modes = modes_for(sector, cutoff)
    P = embedded_P(sector, modes)

    Gh, Gl = dd_dot_columns(P, None, P, None)
    Gih, Gil, Gi_mp = mp_inverse_split(Gh, Gl, DPS)
    Gi = np.array([[float(Gi_mp[i, j]) for j in range(6)] for i in range(6)])

    raw_mv, proj, op, f = fixed_operator(modes, sector, P, Gi)
    data = hp_parity_data(
        modes, sector, dps=DPS, arch_terms=ARCH, correction_terms=50
    )

    # Direct leading remote-coupling RHS w1_p.
    bh, bl = w1_dd(data, sector, DPS)
    bfloat = np.array(
        [float(ldd_to_mpf(bh[i], bl[i])) for i in range(len(modes))],
        dtype=float,
    )

    # Shared fixed-operator solves: six protected-coupling columns + source + w1.
    E = proj(raw_mv(P))
    rhs = np.column_stack([E, proj(f), proj(bfloat)])
    sol = np.empty_like(rhs)
    init_res = []
    iters = []
    for j in range(rhs.shape[1]):
        cnt = [0]
        x, info = cg(
            op, rhs[:, j], rtol=2e-14, atol=0.0, maxiter=30000,
            callback=lambda _: cnt.__setitem__(0, cnt[0] + 1),
        )
        if info != 0:
            raise RuntimeError(("fixed FFT CG failed", sector, cutoff, j, info))
        sol[:, j] = proj(x)
        init_res.append(float(np.linalg.norm(rhs[:, j] - op @ sol[:, j])))
        iters.append(cnt[0])

    Yh = sol[:, :6].astype(LD)
    Yl = np.zeros_like(Yh, dtype=LD)
    yfh = sol[:, 6].astype(LD)
    yfl = np.zeros_like(yfh, dtype=LD)
    ybh = sol[:, 7].astype(LD)
    ybl = np.zeros_like(ybh, dtype=LD)

    Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)
    yfh, yfl = dd_project(P, Gih, Gil, yfh, yfl)
    ybh, ybl = dd_project(P, Gih, Gil, ybh, ybl)

    # Refine common protected columns and source using the accepted LDDD path.
    Us_h, Us_l = form_trial(P, Yh, Yl, yfh, yfl)
    AUs_h, AUs_l, Rh, Rl, source_r0 = residuals_dd(
        data, P, Gih, Gil, Us_h, Us_l
    )
    Yh, Yl, yfh, yfl = refine_once(
        op, proj, Yh, Yl, yfh, yfl, Rh, Rl
    )
    Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)
    yfh, yfl = dd_project(P, Gih, Gil, yfh, yfl)

    Us_h, Us_l = form_trial(P, Yh, Yl, yfh, yfl)
    AUs_h, AUs_l, Rh, Rl, source_r1 = residuals_dd(
        data, P, Gih, Gil, Us_h, Us_l
    )

    # Refine the w1 RHS against the same now-refined protected columns.
    Ub_h, Ub_l = form_trial(P, Yh, Yl, ybh, ybl)
    AUb_h, AUb_l, Rbh, Rbl, m11_r0 = generic_residuals(
        data, P, Gih, Gil, Ub_h, Ub_l, bh, bl
    )
    rhs_b = -(Rbh[:, 6] + Rbl[:, 6])
    db, info = cg(op, rhs_b, rtol=2e-14, atol=0.0, maxiter=30000)
    if info != 0:
        raise RuntimeError(("w1 refinement CG failed", sector, cutoff, info))
    db = proj(db)
    ybh, ybl = dd_add(ybh, ybl, db, np.zeros_like(db))
    ybh, ybl = dd_project(P, Gih, Gil, ybh, ybl)

    Ub_h, Ub_l = form_trial(P, Yh, Yl, ybh, ybl)
    AUb_h, AUb_l, Rbh, Rbl, m11_r1 = generic_residuals(
        data, P, Gih, Gil, Ub_h, Ub_l, bh, bl
    )

    Ks = form_Ktilde(data, Us_h, Us_l, AUs_h, AUs_l, DPS)
    Kb = generic_Ktilde(Ub_h, Ub_l, AUb_h, AUb_l, bh, bl, DPS)

    with mp.workdps(DPS):
        S = Ks[:6, :6]
        g = -Ks[:6, 6]
        h = -Ks[6, 6]
        w = mp.lu_solve(S, g)
        G = h + (g.T * w)[0]
        C = 1 / G

        coeff = [w[j] for j in range(6)] + [mp.mpf(1)]
        xh, xl = dd_linear_combination(Us_h, Us_l, coeff)

        zx = dd_dot_to_mp(data.z_hi, data.z_lo, xh, xl)
        px = dd_dot_to_mp(data.pole_hi, data.pole_lo, xh, xl)

        alpha = mp.mpf(2 if sector == "even-v" else -2)
        if sector == "even-v":
            f_lead = 4 * mp.cosh(1) / mp.pi
            g0 = mp.cosh(mp.mpf("0.5"))
        else:
            f_lead = -4 * mp.sinh(1) / mp.pi
            g0 = mp.sinh(mp.mpf("0.5"))

        L = f_lead + (2 / mp.pi) * zx - alpha * (4 * g0 / mp.pi) * px
        Aamp = C * L * L
        M11 = energy_from_K(Kb)

    row = {
        "sector": sector,
        "cutoff": cutoff,
        "dimension": len(modes),
        "capacity_C": mp.nstr(C, 60),
        "remote_leading_L": mp.nstr(L, 60),
        "sign_L": 1 if L > 0 else -1 if L < 0 else 0,
        "A_C_times_L_squared": mp.nstr(Aamp, 60),
        "M11_direct": mp.nstr(M11, 60),
        "z_dot_source": mp.nstr(zx, 60),
        "pole_dot_source": mp.nstr(px, 60),
        "initial_cg_iters": iters,
        "initial_recomputed_residual_max": max(init_res),
        "source_ldd_residual_before_refine_max": max(source_r0),
        "source_ldd_residual_after_refine_max": max(source_r1),
        "M11_ldd_residual_before_refine_max": max(m11_r0),
        "M11_ldd_residual_after_refine_max": max(m11_r1),
        "remote_coercivity_gamma_inherited": 1.0,
        "gamma_provenance": (
            "v14.044/v14.046: S_{p,4000}>=I; exact later remote Schur "
            "complements inherit >=I variationally for cutoff>=4000."
        ),
        "guardrail": (
            "Fixed-full-lattice finite midpoint data only. No infinite-tail "
            "sign claim; outward finite-source/capacity radii still required."
        ),
    }
    print(json.dumps(row, indent=2), flush=True)
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sector", choices=["even-v", "odd-v"], required=True)
    ap.add_argument("--cutoff", type=int, choices=[32000, 64000], required=True)
    args = ap.parse_args()
    row = solve_one(args.sector, args.cutoff)
    OUT.write_text(json.dumps(row, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
