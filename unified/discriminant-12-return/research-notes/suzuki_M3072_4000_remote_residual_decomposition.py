#!/usr/bin/env python3
"""Decompose the exact N=3072 -> M=4000 remote residual correction.

v14.011-prep diagnostic.

For the exact nested finite-section correction,

    H = G_M - G_N = r^* S^{-1} r,

where S = D - B A_N^{-1} B^* is the shell Schur complement and
r = f_Q - B A_N^{-1} f_N is the actual Galerkin residual on the new shell.

v14.010 showed

    r_n = L/n + subleading.

This script reconstructs the LDDD-refined N=3072 finite source solution,
evaluates the actual source-faithful remote residual on every shell mode
through 4000, writes

    r = L u + eps,  u_n=1/n,

and decomposes the standalone-tail quadratic form

    r^* D^{-1} r
      = L^2 u^*D^{-1}u
        + 2 L u^*D^{-1}eps
        + eps^*D^{-1}eps.

Since S <= D for the positive block problem,

    r^* D^{-1} r <= r^* S^{-1} r = H.

Thus the gap between the standalone-tail actual-residual form and the exact
capacity increment measures positive Schur feedback, while the cross term
quantifies the destructive subleading interference that makes the pure 1/n
model overpredict.

Guardrail: midpoint diagnostic only; no outward tail theorem is promoted.
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
from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data,
    ldl_solve,
    pole_vector,
    structured_ldl,
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
    dd_dot_to_mp,
    direct_remote_residual_mp,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "M3072_4000_remote_residual_decomposition_result.json"

N = 3072
M = 4000
CAP = {
    "even-v": {
        N: mp.mpf("7.60517660046981743730761773326432114842733975365269163351943e-30"),
        M: mp.mpf("7.5773007563692575306680936106689123586265630100827471120927e-30"),
    },
    "odd-v": {
        N: mp.mpf("2.19248446398439423563170694421551363762978394343163246988626e-25"),
        M: mp.mpf("2.1845239838296620020805542670090522874748063437543145074951e-25"),
    },
}


def refined_solution(sector: str, dps: int = 180):
    modes = np.arange(
        1 if sector == "even-v" else 2,
        N + 1,
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
        G = h + (g.T * w)[0]
        C = 1 / G
        C_target = CAP[sector][N]
        rel_capacity_replay_error = abs(C-C_target)/C_target
        if rel_capacity_replay_error > mp.mpf("1e-8"):
            raise RuntimeError((
                sector,
                "refined source capacity replay failed",
                mp.nstr(C, 50),
                mp.nstr(C_target, 50),
                mp.nstr(rel_capacity_replay_error, 20),
            ))

        coeffs = [w[j] for j in range(6)] + [mp.mpf(1)]
        xh, xl = dd_linear_combination(Uh, Ul, coeffs)

        zx = dd_dot_to_mp(data.z_hi, data.z_lo, xh, xl)
        px = dd_dot_to_mp(data.pole_hi, data.pole_lo, xh, xl)

        alpha = mp.mpf(2 if sector == "even-v" else -2)
        if sector == "even-v":
            f_lead = 4 * mp.cosh(1) / mp.pi
            g0 = mp.cosh(mp.mpf("0.5"))
        else:
            f_lead = -4 * mp.sinh(1) / mp.pi
            g0 = mp.sinh(mp.mpf("0.5"))

        L = f_lead + (2 / mp.pi) * zx - alpha * (4*g0/mp.pi) * px

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
        "C_refined": C,
        "capacity_replay_relative_error": rel_capacity_replay_error,
        "L": L,
        "gamma_midpoint": gamma,
        "initial_max_joint_residual": max(norms0),
        "refined_max_joint_residual": max(norms1),
    }


def parity_shell(sector: str):
    start = 1 if sector == "even-v" else 2
    modes = np.arange(start, M + 1, 2, dtype=int)
    return modes[modes > N]


def tail_solve(modes, sector, rhs):
    z, diag = endpoint_data(modes, sign=-1, rho=0.0)
    Ld, Dd = structured_ldl(modes, z, diag)
    y0 = ldl_solve(Ld, Dd, rhs)

    p, alpha = pole_vector(modes, sector)
    yp = ldl_solve(Ld, Dd, p)
    den = 1.0 + alpha * float(p @ yp)
    y = y0 - alpha * yp * float(p @ y0) / den
    return y, den


def one_sector(sector: str, dps: int = 180):
    state = refined_solution(sector, dps=dps)
    shell = parity_shell(sector)

    with mp.workdps(dps):
        residual_mp = []
        for j, n in enumerate(shell):
            rr = direct_remote_residual_mp(
                int(n),
                sector,
                state["modes"],
                state["xmp"],
                state["zmp"],
                state["pmp"],
            )
            residual_mp.append(rr)
            if (j + 1) % 100 == 0 or j + 1 == len(shell):
                print(sector, "remote rows", j + 1, "/", len(shell))

        Lmp = state["L"]
        ump = [1 / mp.mpf(int(n)) for n in shell]
        epsmp = [r - Lmp*u for r, u in zip(residual_mp, ump)]

        # Conversion to float is safe for this diagnostic quadratic form:
        # the remote residuals are ~1e12 and are already resolved to many
        # clean digits by the mp producer.
        r = np.array([float(v) for v in residual_mp], dtype=float)
        u = 1.0 / shell.astype(float)
        eps = np.array([float(v) for v in epsmp], dtype=float)
        Lf = float(Lmp)

    Du, den = tail_solve(shell, sector, u)
    Deps, den2 = tail_solve(shell, sector, eps)
    Dr, den3 = tail_solve(shell, sector, r)
    if max(abs(den-den2), abs(den-den3)) > 1e-12:
        raise RuntimeError("inconsistent Woodbury denominator")

    q_lead = Lf*Lf * float(u @ Du)
    q_cross = 2.0*Lf * float(u @ Deps)
    q_eps = float(eps @ Deps)
    q_actual = float(r @ Dr)
    q_sum = q_lead + q_cross + q_eps

    Cn = CAP[sector][N]
    Cm = CAP[sector][M]
    with mp.workdps(dps):
        eta_exact = Cn/Cm - 1
        H_exact = 1/Cm - 1/Cn

    eta_lead = float(Cn) * q_lead
    eta_cross = float(Cn) * q_cross
    eta_eps = float(Cn) * q_eps
    eta_D_actual = float(Cn) * q_actual

    return {
        "sector": sector,
        "N": N,
        "M": M,
        "shell_dimension": int(len(shell)),
        "first_shell_mode": int(shell[0]),
        "last_shell_mode": int(shell[-1]),
        "C_N": mp.nstr(Cn, 60),
        "C_M": mp.nstr(Cm, 60),
        "C_refined_reconstructed": mp.nstr(state["C_refined"], 60),
        "L": mp.nstr(state["L"], 60),
        "eta_exact": mp.nstr(eta_exact, 50),
        "H_exact": mp.nstr(H_exact, 50),
        "eta_lead_D": eta_lead,
        "eta_cross_D": eta_cross,
        "eta_eps_D": eta_eps,
        "eta_D_actual": eta_D_actual,
        "eta_D_sum_check": float(Cn) * q_sum,
        "lead_fraction_of_exact": eta_lead / float(eta_exact),
        "cross_fraction_of_lead": eta_cross / eta_lead,
        "eps_fraction_of_lead": eta_eps / eta_lead,
        "standalone_actual_fraction_of_exact": (
            eta_D_actual / float(eta_exact)
        ),
        "schur_feedback_eta": float(eta_exact) - eta_D_actual,
        "schur_feedback_fraction_of_exact": (
            (float(eta_exact)-eta_D_actual) / float(eta_exact)
        ),
        "woodbury_denominator": den,
        "initial_max_joint_residual": state["initial_max_joint_residual"],
        "refined_max_joint_residual": state["refined_max_joint_residual"],
        "max_abs_eps_over_abs_lead_pointwise": float(
            np.max(np.abs(eps) / np.maximum(np.abs(Lf*u), 1e-300))
        ),
        "rms_eps_over_lead": float(
            np.linalg.norm(eps) / np.linalg.norm(Lf*u)
        ),
        "inequality_D_le_exact": bool(
            eta_D_actual <= float(eta_exact) * (1 + 1e-10)
        ),
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
        "eta_exact_odd_minus_even": float(mp.mpf(o["eta_exact"]) - mp.mpf(e["eta_exact"])),
        "eta_lead_D_odd_minus_even": o["eta_lead_D"] - e["eta_lead_D"],
        "eta_cross_D_odd_minus_even": o["eta_cross_D"] - e["eta_cross_D"],
        "eta_eps_D_odd_minus_even": o["eta_eps_D"] - e["eta_eps_D"],
        "eta_D_actual_odd_minus_even": o["eta_D_actual"] - e["eta_D_actual"],
        "schur_feedback_eta_odd_minus_even": (
            o["schur_feedback_eta"] - e["schur_feedback_eta"]
        ),
    }

    out = {
        "rows": rows,
        "paired": paired,
        "guardrail": (
            "Midpoint finite-shell diagnostic only. The exact eta comes from "
            "nested LDDD capacities; D-inverse decomposition uses a standalone "
            "source-faithful shell and is not an outward Schur certificate."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("\nPAIRED")
    print(json.dumps(paired, indent=2))
    print("\nwrote", OUT)
    print("GUARDRAIL:", out["guardrail"])


if __name__ == "__main__":
    main()
