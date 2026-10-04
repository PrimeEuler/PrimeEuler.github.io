#!/usr/bin/env python3
"""Direct LDDD diagnostic for the v14.016 finite datum (M_o-M_e)_{11}.

For a parity sector p and finite cutoff N, the leading remote coupling vector
from the finite block into a remote mode n is

    B_p(n,.) = w1_p^T / n + O(z_n/n^2),

with

    w1_p = -(2/pi) z + alpha_p (4 g_p/pi) pole_p,

alpha_e=+2, g_e=cosh(1/2),
alpha_o=-2, g_o=sinh(1/2).

The v14.016 Schur coefficient uses

    M_{p,11} = w1_p^T A_{p,N}^{-1} w1_p.

This script evaluates M_{p,11} with the same frozen-P4 protected/complement
LDDD residual-refinement architecture used by v14.008, then forms the direct
parity difference in mp arithmetic.

Diagnostic only: the individual forms are potentially ~1e30 and their
difference ~1e3.  This script establishes scale/cancellation and residual
quality; it does not by itself supply a rigorous correlated exact-source
interval for the difference.
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
from suzuki_ldd_source_operator import (
    LD,
    dd_matvec,
    ldd_to_mpf,
    split_mpf_ld,
)
from suzuki_doubledouble_source_operator import (
    add as dd_add,
    sub as dd_sub,
    dot_columns as dd_dot_columns,
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement,
    dd_matrix_to_mp,
    dd_project,
    form_trial,
    mp_inverse_split,
    refine_once,
    residual_gram_mp,
)
from suzuki_ldd_source_operator import hp_parity_data_ld as hp_parity_data

HERE = Path(__file__).resolve().parent
OUT = HERE / "ldd_M11_direct_difference_result.json"


def w1_dd(data, sector: str, dps: int):
    with mp.workdps(dps):
        alpha = mp.mpf(2 if sector == "even-v" else -2)
        gp = mp.cosh(mp.mpf("0.5")) if sector == "even-v" else mp.sinh(mp.mpf("0.5"))
        cz = -mp.mpf(2) / mp.pi
        cp = alpha * (mp.mpf(4) * gp / mp.pi)

        bh = np.empty_like(data.z_hi, dtype=LD)
        bl = np.empty_like(data.z_lo, dtype=LD)
        for i in range(len(bh)):
            zi = ldd_to_mpf(data.z_hi[i], data.z_lo[i])
            pi = ldd_to_mpf(data.pole_hi[i], data.pole_lo[i])
            v = cz * zi + cp * pi
            bh[i], bl[i] = split_mpf_ld(v)
    return bh, bl


def generic_residuals(data, P, Gih, Gil, Uh, Ul, bh, bl):
    AUh, AUl = dd_matvec(data, Uh, Ul)
    Rh = AUh.copy()
    Rl = AUl.copy()
    Rh[:, 6], Rl[:, 6] = dd_sub(
        Rh[:, 6], Rl[:, 6], bh, bl
    )
    Rh, Rl = dd_project(P, Gih, Gil, Rh, Rl)
    norms = []
    for j in range(7):
        H, L = dd_dot_columns(
            Rh[:, j:j+1], Rl[:, j:j+1],
            Rh[:, j:j+1], Rl[:, j:j+1],
        )
        norms.append(float(mp.sqrt(dd_matrix_to_mp(H, L)[0, 0])))
    return AUh, AUl, Rh, Rl, norms


def generic_Ktilde(Uh, Ul, AUh, AUl, bh, bl, dps):
    Gh, Gl = dd_dot_columns(Uh, Ul, AUh, AUl)
    qh, ql = dd_dot_columns(Uh, Ul, bh[:, None], bl[:, None])
    with mp.workdps(dps):
        G = dd_matrix_to_mp(Gh, Gl)
        q = dd_matrix_to_mp(qh, ql)
        K = mp.matrix(7)
        for i in range(6):
            for j in range(6):
                K[i, j] = G[i, j]
            K[i, 6] = G[i, 6] - q[i]
            K[6, i] = K[i, 6]
        K[6, 6] = G[6, 6] - 2*q[6]
        return (K + K.T) / 2


def energy_from_K(K):
    S = K[:6, :6]
    g = -K[:6, 6]
    h = -K[6, 6]
    w = mp.lu_solve(S, g)
    return h + (g.T*w)[0]


def one_sector(max_mode: int, sector: str, dps: int, refinements: int):
    modes = np.arange(
        1 if sector == "even-v" else 2,
        max_mode + 1,
        2,
        dtype=int,
    )
    P, _ = frozen_protected_basis(sector, modes)

    Gh, Gl = dd_dot_columns(P, None, P, None)
    Gih, Gil, Gi_mp = mp_inverse_split(Gh, Gl, dps)
    Gi = np.array([[float(Gi_mp[i, j]) for j in range(6)] for i in range(6)])

    A, _ = full_source_matrix(modes, sector)
    data = hp_parity_data(
        modes, sector, dps=dps, arch_terms=160, correction_terms=50
    )
    bh, bl = w1_dd(data, sector, dps)
    bfloat = np.array([float(ldd_to_mpf(bh[i], bl[i])) for i in range(len(modes))])

    op, proj, gamma, evals, Y0, yb0, initial_res = build_double_complement(
        A, P, Gi, bfloat, rtol=2e-14
    )

    Yh = Y0.astype(LD)
    Yl = np.zeros_like(Yh, dtype=LD)
    ybh = yb0.astype(LD)
    ybl = np.zeros_like(ybh, dtype=LD)

    Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)
    ybh, ybl = dd_project(P, Gih, Gil, ybh, ybl)

    history = []
    for step in range(refinements + 1):
        Uh, Ul = form_trial(P, Yh, Yl, ybh, ybl)
        AUh, AUl, Rh, Rl, norms = generic_residuals(
            data, P, Gih, Gil, Uh, Ul, bh, bl
        )
        history.append(norms)
        print(sector, max_mode, "refinement", step, "max residual", max(norms))
        if step < refinements:
            # Protected coupling columns: same sign convention as standard.
            for j in range(6):
                rhs = Rh[:, j] + Rl[:, j]
                delta, info = __import__("scipy.sparse.linalg", fromlist=["cg"]).cg(
                    op, rhs, rtol=2e-14, atol=0.0, maxiter=20000
                )
                if info != 0:
                    raise RuntimeError(("coupling correction failed", j, info))
                delta = proj(delta)
                Yh[:, j], Yl[:, j] = dd_add(
                    Yh[:, j], Yl[:, j], delta, np.zeros_like(delta)
                )
            # RHS solve residual is Q(A*y-b), so opposite sign correction.
            rhs = -(Rh[:, 6] + Rl[:, 6])
            delta, info = __import__("scipy.sparse.linalg", fromlist=["cg"]).cg(
                op, rhs, rtol=2e-14, atol=0.0, maxiter=20000
            )
            if info != 0:
                raise RuntimeError(("rhs correction failed", info))
            delta = proj(delta)
            ybh, ybl = dd_add(
                ybh, ybl, delta, np.zeros_like(delta)
            )
            Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)
            ybh, ybl = dd_project(P, Gih, Gil, ybh, ybl)

    Kt = generic_Ktilde(Uh, Ul, AUh, AUl, bh, bl, dps)
    RR = residual_gram_mp(Rh, Rl, dps)

    with mp.workdps(dps):
        E = energy_from_K(Kt)
        rrmax = max(mp.eigsy(RR)[0])
        # Midpoint gamma only: diagnostic residual-quadratic scale.
        err_mid = rrmax / mp.mpf(str(gamma))
        return {
            "sector": sector,
            "max_mode": max_mode,
            "dimension": len(modes),
            "M11_midpoint": mp.nstr(E, 80),
            "complement_floor_midpoint": gamma,
            "initial_double_residuals": initial_res,
            "residual_history": history,
            "final_residual_gram_norm": mp.nstr(rrmax, 50),
            "midpoint_quadratic_error_scale": mp.nstr(err_mid, 50),
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cuts", default="768,1536,3072,4000")
    ap.add_argument("--dps", type=int, default=180)
    ap.add_argument("--refinements", type=int, default=1)
    args = ap.parse_args()

    cuts = [int(x) for x in args.cuts.split(",") if x.strip()]
    rows = []
    paired = []

    for N in cuts:
        e = one_sector(N, "even-v", args.dps, args.refinements)
        o = one_sector(N, "odd-v", args.dps, args.refinements)
        rows.extend([e, o])
        with mp.workdps(args.dps):
            Me = mp.mpf(e["M11_midpoint"])
            Mo = mp.mpf(o["M11_midpoint"])
            diff = Mo - Me
            rel = diff / max(abs(Me), abs(Mo))
        pair = {
            "cutoff": N,
            "M_even": e["M11_midpoint"],
            "M_odd": o["M11_midpoint"],
            "M_odd_minus_even": mp.nstr(diff, 80),
            "difference_over_max_abs_M": mp.nstr(rel, 40),
        }
        paired.append(pair)
        print("\nPAIR", N)
        print(json.dumps(pair, indent=2))

    out = {
        "cuts": cuts,
        "dps": args.dps,
        "refinements": args.refinements,
        "rows": rows,
        "paired": paired,
        "guardrail": (
            "Diagnostic correlated-difference scale only. The residual-quadratic "
            "error uses a midpoint complement floor and does not include a final "
            "outward exact-source correlation enclosure."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("\nwrote", OUT)
    print("GUARDRAIL:", out["guardrail"])


if __name__ == "__main__":
    main()
