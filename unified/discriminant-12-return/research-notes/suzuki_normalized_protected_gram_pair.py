#!/usr/bin/env python3
"""Paired Cholesky-normalized protected-Gram consumer for v14.130/v14.132.

Consumes the corrected explicit M64000 anchors for even-v and odd-v, regenerates
the reduced octave midpoint Gram payloads D,c,d, and evaluates the protected
term without ever forming S-D:

    G = L^{-1} D L^{-T},
    u = L^T (D^{-1} c - a),
    Lambda_parallel = u^T G (I-G)^{-1} u.

The next anchor factor is transported as

    S-D = L (I-G) L^T = (L C)(L C)^T,  C=chol(I-G),

so no near-singular protected-matrix subtraction is used.  The script also
evaluates the common-mode-preserving paired bound from ledger v14.132.

This is a midpoint diagnostic consumer.  It does not promote the binary64
Gram payload to an outward theorem; v14.128/v14.129 radii remain load-bearing.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np

import suzuki_M128000_M256000_reduced_feshbach_transport as red

DPS = 160
ANCHOR_K_TOL = mp.mpf("1e-60")
ANCHOR_SMIN_TOL = mp.mpf("1e-45")


def mp_mat(rows):
    return mp.matrix([[mp.mpf(str(x)) for x in row] for row in rows])


def mp_vec(xs):
    return mp.matrix([[mp.mpf(str(x))] for x in xs])


def norm2(x):
    return mp.sqrt(mp.fsum(abs(x[i]) ** 2 for i in range(x.rows)))


def fro_norm(A):
    return mp.sqrt(mp.fsum(abs(A[i, j]) ** 2 for i in range(A.rows) for j in range(A.cols)))


def spectral_norm_sym(A):
    vals, _ = mp.eigsy((A + A.T) / 2)
    return max(abs(vals[0]), abs(vals[-1]))


def solve_matrix(A, B):
    """Solve A X = B column-by-column; mpmath.lu_solve accepts vector RHS only."""
    if B.cols == 1:
        return mp.lu_solve(A, B)
    X = mp.matrix(A.cols, B.cols)
    for j in range(B.cols):
        xj = mp.lu_solve(A, B[:, j])
        for i in range(A.cols):
            X[i, j] = xj[i]
    return X


def right_solve_transpose(L, X):
    """Return X L^{-T} using column-wise left solves."""
    return solve_matrix(L, X.T).T


def reduced_payload(sector, R):
    """Validated midpoint reduced payload used by the existing transport producer."""
    R2 = 2 * R
    a = red.setup(sector, R)
    b2 = red.setup(sector, R2)
    n1 = len(a["modes"])

    Wpad = np.zeros((len(b2["modes"]), 6), dtype=float)
    Wpad[:n1, :] = a["W"]
    qpad = np.zeros(len(b2["modes"]), dtype=float)
    qpad[:n1] = a["q"]

    F = b2["raw"](Wpad)[n1:, :]
    r = b2["g"][n1:] - b2["raw"](qpad)[n1:]
    X = b2["Y"][n1:, :]
    y = b2["q"][n1:]

    D = F.T @ X
    D = (D + D.T) / 2
    c = F.T @ y
    d = float(r @ y)
    return mp_mat(D.tolist()), mp_vec(c.tolist()), mp.mpf(str(d))


def load_anchor(path, expected_sector):
    data = json.loads(Path(path).read_text())
    if data.get("sector") != expected_sector:
        raise RuntimeError(("sector mismatch", path, data.get("sector"), expected_sector))

    required = [
        "S", "b", "h", "Sinv_b", "K_total",
        "K_reconstructed", "protected_S_min",
        "protected_S_min_reconstructed", "K_consistency_abs",
        "Smin_consistency_abs",
    ]
    missing = [k for k in required if k not in data]
    if missing:
        raise RuntimeError(("corrected explicit anchor fields missing", path, missing))

    kerr = mp.mpf(data["K_consistency_abs"])
    merr = mp.mpf(data["Smin_consistency_abs"])
    if kerr > ANCHOR_K_TOL or merr > ANCHOR_SMIN_TOL:
        raise RuntimeError(("anchor fail-closed self-check", expected_sector, kerr, merr))

    S = mp_mat(data["S"])
    S = (S + S.T) / 2
    b = mp_vec(data["b"])
    h = mp.mpf(data["h"])
    a = mp_vec(data["Sinv_b"])

    vals, _ = mp.eigsy(S)
    if vals[0] <= 0:
        raise RuntimeError(("anchor S is not SPD", expected_sector, vals[0]))

    L = mp.cholesky(S)
    solve_res = norm2(S * a - b)
    K = h + (b.T * a)[0]
    K_total = mp.mpf(data["K_total"])
    if abs(K - K_total) > ANCHOR_K_TOL:
        raise RuntimeError(("independent anchor K reconstruction failed", expected_sector, K, K_total))

    return {
        "sector": expected_sector,
        "L": L,
        "b": b,
        "h": h,
        "a": a,
        "K": K,
        "S_min": vals[0],
        "Sinv_b_residual": solve_res,
    }


def normalized_step(state, sector, R):
    """One R->2R step, never forming S-D."""
    L = state["L"]
    b = state["b"]
    h = state["h"]
    a = state["a"]

    D, c, d = reduced_payload(sector, R)
    D = (D + D.T) / 2

    # v=D^+c.  For the current midpoint payload D is expected full rank; if it
    # is singular/indefinite at this precision, fail closed rather than invent
    # a rank cutoff.  The outward-radii theorem must decide that case.
    dvals, _ = mp.eigsy(D)
    if dvals[0] <= 0:
        raise RuntimeError(("midpoint D not SPD; outward rank treatment required", sector, R, dvals[0]))
    v = mp.lu_solve(D, c)
    Dv_res = norm2(D * v - c)

    # G = L^{-1} D L^{-T}, formed by triangular/linear solves only.
    X = solve_matrix(L, D)
    G = right_solve_transpose(L, X)
    G = (G + G.T) / 2
    gvals, _ = mp.eigsy(G)

    I = mp.eye(G.rows)
    if gvals[0] < 0 or gvals[-1] >= 1:
        raise RuntimeError(("normalized contraction failed", sector, R, gvals[0], gvals[-1]))

    u = L.T * (v - a)
    resolv_u = mp.lu_solve(I - G, u)
    lam = (u.T * G * resolv_u)[0]

    # Equivalent orthogonal midpoint split for cross-check only.
    sigma_perp = d - (c.T * v)[0]

    # Factor-preserving anchor transport:
    # S2 = L(I-G)L^T = (L C)(L C)^T.
    C = mp.cholesky(I - G)
    L2 = L * C
    b2 = b - c
    h2 = h + d
    y2 = mp.lu_solve(L2, b2)
    a2 = mp.lu_solve(L2.T, y2)
    K2 = h2 + (b2.T * a2)[0]

    delta = K2 - state["K"]
    split_res = abs(delta - (sigma_perp + lam))

    return {
        "state": {
            "sector": sector,
            "L": L2,
            "b": b2,
            "h": h2,
            "a": a2,
            "K": K2,
        },
        "R": R,
        "R2": 2 * R,
        "D_min": dvals[0],
        "D_max": dvals[-1],
        "Dv_residual": Dv_res,
        "G": G,
        "u": u,
        "G_min": gvals[0],
        "G_max": gvals[-1],
        "resolv_u": resolv_u,
        "Lambda_parallel": lam,
        "sigma_perp_mid": sigma_perp,
        "delta_K_mid": delta,
        "split_identity_abs": split_res,
        "L2_factor_residual_fro": fro_norm(
            L2 * L2.T - L * (I - G) * L.T
        ),
    }


def paired_metrics(even, odd):
    Ge, Go = even["G"], odd["G"]
    ue, uo = even["u"], odd["u"]
    Ie = mp.eye(Ge.rows)
    Io = mp.eye(Go.rows)

    deltaG = Go - Ge
    deltau = uo - ue

    Roe_uo = mp.lu_solve(Ie - Ge, uo)
    Roe_ue = mp.lu_solve(Ie - Ge, ue)
    Roo_uo = mp.lu_solve(Io - Go, uo)

    bound_G = spectral_norm_sym(deltaG) * norm2(Roo_uo) * norm2(Roe_uo)
    bound_u = norm2(deltau) * (
        norm2(Roe_uo) + norm2(Roe_ue) + norm2(uo) + norm2(ue)
    )
    paired_bound = bound_G + bound_u
    actual = odd["Lambda_parallel"] - even["Lambda_parallel"]

    return {
        "Delta_Lambda_parallel": actual,
        "deltaG_spectral": spectral_norm_sym(deltaG),
        "deltau_l2": norm2(deltau),
        "bound_G_term": bound_G,
        "bound_u_term": bound_u,
        "paired_bound_v14132": paired_bound,
        "headroom_if_nonzero": (paired_bound / abs(actual)) if actual != 0 else mp.inf,
    }


def nstr(x, n=70):
    return mp.nstr(x, n)


def step_json(r):
    return {
        "R": r["R"],
        "R2": r["R2"],
        "D_min": nstr(r["D_min"]),
        "D_max": nstr(r["D_max"]),
        "Dv_residual": nstr(r["Dv_residual"], 30),
        "G_min": nstr(r["G_min"]),
        "G_max": nstr(r["G_max"]),
        "u_l2": nstr(norm2(r["u"])),
        "resolv_u_l2": nstr(norm2(r["resolv_u"])),
        "Lambda_parallel": nstr(r["Lambda_parallel"]),
        "sigma_perp_mid": nstr(r["sigma_perp_mid"]),
        "delta_K_mid": nstr(r["delta_K_mid"]),
        "split_identity_abs": nstr(r["split_identity_abs"], 30),
        "L2_factor_residual_fro": nstr(r["L2_factor_residual_fro"], 30),
    }


def pair_json(p):
    return {k: nstr(v) for k, v in p.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--even-anchor", required=True)
    ap.add_argument("--odd-anchor", required=True)
    args = ap.parse_args()

    with mp.workdps(DPS):
        se = load_anchor(args.even_anchor, "even-v")
        so = load_anchor(args.odd_anchor, "odd-v")

        e1 = normalized_step(se, "even-v", 64000)
        o1 = normalized_step(so, "odd-v", 64000)
        p1 = paired_metrics(e1, o1)

        e2 = normalized_step(e1["state"], "even-v", 128000)
        o2 = normalized_step(o1["state"], "odd-v", 128000)
        p2 = paired_metrics(e2, o2)

        out = {
            "anchor": {
                "even_K": nstr(se["K"]),
                "odd_K": nstr(so["K"]),
                "even_S_min": nstr(se["S_min"]),
                "odd_S_min": nstr(so["S_min"]),
                "even_Sinv_b_residual": nstr(se["Sinv_b_residual"], 30),
                "odd_Sinv_b_residual": nstr(so["Sinv_b_residual"], 30),
            },
            "64k_128k": {
                "even": step_json(e1),
                "odd": step_json(o1),
                "paired": pair_json(p1),
            },
            "128k_256k": {
                "even": step_json(e2),
                "odd": step_json(o2),
                "paired": pair_json(p2),
            },
            "guardrail": (
                "v14.130/v14.132 midpoint diagnostic; corrected explicit M64000 "
                "anchors required; no S-D formed; binary64 reduced Gram payload "
                "still requires v14.128/v14.129 outward-radius propagation before theorem use"
            ),
        }
        print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
