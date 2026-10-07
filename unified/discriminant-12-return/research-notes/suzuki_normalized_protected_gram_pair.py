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
    """One R->2R step in normalized coordinates, never forming S-D."""
    L = state["L"]
    b = state["b"]
    h = state["h"]
    a = state["a"]

    D, c, d = reduced_payload(sector, R)
    D = (D + D.T) / 2
    dvals, _ = mp.eigsy(D)

    # G = L^{-1} D L^{-T}, formed by column-wise solves only.
    X = solve_matrix(L, D)
    G = right_solve_transpose(L, X)
    G = (G + G.T) / 2
    gvals, _ = mp.eigsy(G)

    I = mp.eye(G.rows)
    if gvals[0] < 0 or gvals[-1] >= 1:
        raise RuntimeError((
            "normalized contraction unresolved by midpoint payload",
            sector, R, gvals[0], gvals[-1]
        ))

    # Pseudoinverse-free normalized increment identity:
    # delta K = sigma + tau^T (I-G)^{-1} tau,
    # tau=L^{-1}(c-Da).  This is exact and does not require D^+.
    t = c - D * a
    tau = mp.lu_solve(L, t)
    sigma = d - 2 * (a.T * c)[0] + (a.T * D * a)[0]
    resolv_tau = mp.lu_solve(I - G, tau)
    delta_normalized = sigma + (tau.T * resolv_tau)[0]

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
    increment_identity_abs = abs(delta - delta_normalized)

    # v14.130/v14.132 protected split is optional at midpoint.  The exact D
    # is PSD, but binary64 Gram assembly can show tiny negative eigenvalues in
    # nearly-null channels.  Do not invent a pseudoinverse cutoff: only expose
    # Lambda_parallel/u when this midpoint D is strictly SPD.
    protected = None
    if dvals[0] > 0:
        v = mp.lu_solve(D, c)
        Dv_res = norm2(D * v - c)
        u = L.T * (v - a)
        resolv_u = mp.lu_solve(I - G, u)
        lam = (u.T * G * resolv_u)[0]
        sigma_perp = d - (c.T * v)[0]
        split_res = abs(delta - (sigma_perp + lam))
        protected = {
            "u": u,
            "resolv_u": resolv_u,
            "Lambda_parallel": lam,
            "sigma_perp_mid": sigma_perp,
            "Dv_residual": Dv_res,
            "split_identity_abs": split_res,
        }

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
        "G": G,
        "G_min": gvals[0],
        "G_max": gvals[-1],
        "tau": tau,
        "resolv_tau": resolv_tau,
        "sigma": sigma,
        "delta_K_normalized": delta_normalized,
        "delta_K_mid": delta,
        "increment_identity_abs": increment_identity_abs,
        "protected": protected,
        "L2_factor_residual_fro": fro_norm(
            L2 * L2.T - L * (I - G) * L.T
        ),
    }


def paired_increment_metrics(even, odd):
    """Common-mode-preserving bound for the entire octave increment."""
    Ge, Go = even["G"], odd["G"]
    te, to = even["tau"], odd["tau"]
    se, so = even["sigma"], odd["sigma"]
    Ie = mp.eye(Ge.rows)
    Io = mp.eye(Go.rows)

    deltaG = Go - Ge
    deltat = to - te
    deltas = so - se

    Re_to = mp.lu_solve(Ie - Ge, to)
    Re_te = mp.lu_solve(Ie - Ge, te)
    Ro_to = mp.lu_solve(Io - Go, to)
    Ro_te = mp.lu_solve(Io - Go, te)
    dg = spectral_norm_sym(deltaG)
    dt = norm2(deltat)

    # Two exact resolvent decompositions, differing only in reference parity.
    # Taking their minimum is valid and often sharper.
    bound_e_ref = (
        abs(deltas)
        + dg * norm2(Ro_to) * norm2(Re_to)
        + dt * (norm2(Re_to) + norm2(Re_te))
    )
    bound_o_ref = (
        abs(deltas)
        + dg * norm2(Ro_te) * norm2(Re_te)
        + dt * (norm2(Ro_to) + norm2(Ro_te))
    )
    actual = odd["delta_K_normalized"] - even["delta_K_normalized"]

    return {
        "Delta_octave_increment": actual,
        "delta_sigma_abs": abs(deltas),
        "deltaG_spectral": dg,
        "deltatau_l2": dt,
        "paired_bound_even_reference": bound_e_ref,
        "paired_bound_odd_reference": bound_o_ref,
        "paired_bound_min": min(bound_e_ref, bound_o_ref),
    }

def paired_metrics(even, odd):
    if even["protected"] is None or odd["protected"] is None:
        return None
    Ge, Go = even["G"], odd["G"]
    ue, uo = even["protected"]["u"], odd["protected"]["u"]
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
    actual = odd["protected"]["Lambda_parallel"] - even["protected"]["Lambda_parallel"]

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
    out = {
        "R": r["R"],
        "R2": r["R2"],
        "D_min": nstr(r["D_min"]),
        "D_max": nstr(r["D_max"]),
        "G_min": nstr(r["G_min"]),
        "G_max": nstr(r["G_max"]),
        "tau_l2": nstr(norm2(r["tau"])),
        "resolv_tau_l2": nstr(norm2(r["resolv_tau"])),
        "sigma": nstr(r["sigma"]),
        "delta_K_normalized": nstr(r["delta_K_normalized"]),
        "delta_K_mid": nstr(r["delta_K_mid"]),
        "increment_identity_abs": nstr(r["increment_identity_abs"], 30),
        "L2_factor_residual_fro": nstr(r["L2_factor_residual_fro"], 30),
        "protected_split_available": r["protected"] is not None,
    }
    if r["protected"] is not None:
        p = r["protected"]
        out.update({
            "Dv_residual": nstr(p["Dv_residual"], 30),
            "u_l2": nstr(norm2(p["u"])),
            "resolv_u_l2": nstr(norm2(p["resolv_u"])),
            "Lambda_parallel": nstr(p["Lambda_parallel"]),
            "sigma_perp_mid": nstr(p["sigma_perp_mid"]),
            "protected_split_identity_abs": nstr(p["split_identity_abs"], 30),
        })
    return out

def pair_json(p):
    if p is None:
        return {"available": False}
    return {"available": True, **{k: nstr(v) for k, v in p.items()}}


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
        i1 = paired_increment_metrics(e1, o1)
        p1 = paired_metrics(e1, o1)

        e2 = normalized_step(e1["state"], "even-v", 128000)
        o2 = normalized_step(o1["state"], "odd-v", 128000)
        i2 = paired_increment_metrics(e2, o2)
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
                "paired_increment": pair_json(i1),
                "paired_protected_v14132": pair_json(p1),
            },
            "128k_256k": {
                "even": step_json(e2),
                "odd": step_json(o2),
                "paired_increment": pair_json(i2),
                "paired_protected_v14132": pair_json(p2),
            },
            "guardrail": (
                "normalized midpoint diagnostic; corrected explicit M64000 anchors required; "
                "no S-D formed. Pseudoinverse-free whole-increment pairing is always attempted "
                "when 0<=G<I; v14.132 protected split is emitted only if midpoint D is SPD. "
                "Binary64 reduced Gram payload still requires outward-radius propagation before theorem use"
            ),
        }
        print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
