#!/usr/bin/env python3
"""Double-double residual refinement and 7x7 capacity bracket.

This implements the precision mechanism prepared in v14.003/v14.005.

For a frozen six-dimensional protected span P:
  * solve the stiff complement in binary64;
  * evaluate the seven joint residual columns with the validated ~30-digit
    double-double source operator;
  * correct those residuals using the same cheap binary64 complement solve;
  * retain corrections as two-float expansions;
  * form the variational 7x7 augmented reduction

        Ktilde = V^* K_full V;

  * use the exact identity

        Ktilde - K = R^* D^{-1} R >= 0

    and the complement floor gamma to obtain the diagnostic Loewner bracket

        Ktilde - (R^*R)/gamma <= K <= Ktilde.

The capacity is the scalar C at which

    K + diag(0,...,0,1/C)

is singular.  Therefore capacities computed from the lower and upper Loewner
matrices give a diagnostic bracket for the exact finite-section crossing.

The default N=192 run validates the machinery against the independent
80-digit v14.003 capacities.  A theorem-scale M3999/4000 run uses the same
code path but still requires outward certification of gamma and arithmetic
tails before promotion.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.sparse.linalg import LinearOperator, cg, eigsh

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis,
    full_source_matrix,
)
from suzuki_doubledouble_source_operator import (
    dd_add,
    dd_dot_columns,
    dd_matvec,
    dd_norm2,
    dd_sub,
    dd_to_mpf,
    hp_parity_data,
    split_mpf,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "dd_refined_capacity_bracket_result.json"


def dd_matrix_to_mp(H, L):
    return mp.matrix(
        [
            [dd_to_mpf(H[i, j], L[i, j]) for j in range(H.shape[1])]
            for i in range(H.shape[0])
        ]
    )


def mp_inverse_split(Gh, Gl, dps):
    with mp.workdps(dps):
        G = dd_matrix_to_mp(Gh, Gl)
        Gi = G**-1
        H = np.empty((G.rows, G.cols))
        L = np.empty((G.rows, G.cols))
        for i in range(G.rows):
            for j in range(G.cols):
                H[i, j], L[i, j] = split_mpf(Gi[i, j])
        return H, L, Gi


def dd_small_matmul(Ah, Al, Bh, Bl):
    m, k = Ah.shape
    k2, n = Bh.shape
    if k != k2:
        raise ValueError("small matmul dimension mismatch")
    H = np.zeros((m, n))
    L = np.zeros((m, n))
    from suzuki_doubledouble_source_operator import dd_mul

    for i in range(m):
        for j in range(n):
            sh = 0.0
            sl = 0.0
            for q in range(k):
                ph, pl = dd_mul(Ah[i, q], Al[i, q], Bh[q, j], Bl[q, j])
                sh, sl = dd_add(sh, sl, ph, pl)
            H[i, j] = sh
            L[i, j] = sl
    return H, L


def dd_project(P, Gih, Gil, Xh, Xl):
    one = Xh.ndim == 1
    if one:
        Xh = Xh[:, None]
        Xl = Xl[:, None]

    ch, cl = dd_dot_columns(P, None, Xh, Xl)
    dh, dl = dd_small_matmul(Gih, Gil, ch, cl)

    Ph = np.zeros_like(Xh)
    Pl = np.zeros_like(Xl)
    from suzuki_doubledouble_source_operator import dd_mul_d

    for a in range(P.shape[1]):
        th, tl = dd_mul_d(
            dh[a, :][None, :],
            dl[a, :][None, :],
            P[:, a][:, None],
        )
        Ph, Pl = dd_add(Ph, Pl, th, tl)

    Qh, Ql = dd_sub(Xh, Xl, Ph, Pl)
    return (Qh[:, 0], Ql[:, 0]) if one else (Qh, Ql)


def double_projector(P, Gi):
    def proj(X):
        X = np.asarray(X, dtype=float)
        return X - P @ (Gi @ (P.T @ X))
    return proj


def build_double_complement(A, P, Gi, f, rtol):
    n = A.shape[0]
    proj = double_projector(P, Gi)

    def mv(x):
        qx = proj(x)
        return proj(A @ qx) + P @ (Gi @ (P.T @ x))

    op = LinearOperator((n, n), matvec=mv, dtype=float)
    evals = np.sort(
        eigsh(op, k=4, which="SA", return_eigenvectors=False, tol=1e-11)
    )
    gamma = float(evals[0])

    E = proj(A @ P)
    fQ = proj(f)
    rhs = np.column_stack([E, fQ])

    sol = np.empty_like(rhs)
    residuals = []
    for j in range(7):
        x, info = cg(op, rhs[:, j], rtol=rtol, atol=0.0, maxiter=20000)
        if info != 0:
            raise RuntimeError(("initial CG failed", j, info))
        sol[:, j] = proj(x)
        residuals.append(float(np.linalg.norm(rhs[:, j] - mv(sol[:, j]))))

    return op, proj, gamma, evals, sol[:, :6], sol[:, 6], residuals


def solve_correction(op, proj, rhs, rtol=2e-14):
    x, info = cg(op, rhs, rtol=rtol, atol=0.0, maxiter=20000)
    if info != 0:
        raise RuntimeError(("correction CG failed", info))
    return proj(x)


def dd_source_column(data):
    return (
        data.source_hi[:, None].copy(),
        data.source_lo[:, None].copy(),
    )


def form_trial(P, Yh, Yl, yfh, yfl):
    Wh, Wl = dd_sub(P, np.zeros_like(P), Yh, Yl)
    Uh = np.column_stack([Wh, yfh])
    Ul = np.column_stack([Wl, yfl])
    return Uh, Ul


def residuals_dd(data, P, Gih, Gil, Uh, Ul):
    AUh, AUl = dd_matvec(data, Uh, Ul)

    Rh = AUh.copy()
    Rl = AUl.copy()

    # Source residual: Q(A*yf - f).
    Rh[:, 6], Rl[:, 6] = dd_sub(
        Rh[:, 6],
        Rl[:, 6],
        data.source_hi,
        data.source_lo,
    )

    Rh, Rl = dd_project(P, Gih, Gil, Rh, Rl)
    norms = [dd_norm2(Rh[:, j], Rl[:, j]) for j in range(7)]
    return AUh, AUl, Rh, Rl, norms


def refine_once(op, proj, Yh, Yl, yfh, yfl, Rh, Rl):
    for j in range(6):
        rhs = Rh[:, j] + Rl[:, j]
        delta = solve_correction(op, proj, rhs)
        Yh[:, j], Yl[:, j] = dd_add(
            Yh[:, j], Yl[:, j], delta, np.zeros_like(delta)
        )

    # Source residual is Q(A*yf-f), so correction has the opposite sign.
    rhs = -(Rh[:, 6] + Rl[:, 6])
    delta = solve_correction(op, proj, rhs)
    yfh, yfl = dd_add(yfh, yfl, delta, np.zeros_like(delta))
    return Yh, Yl, yfh, yfl


def form_Ktilde(data, Uh, Ul, AUh, AUl, dps):
    Gh, Gl = dd_dot_columns(Uh, Ul, AUh, AUl)
    fh = data.source_hi[:, None]
    fl = data.source_lo[:, None]
    qh, ql = dd_dot_columns(Uh, Ul, fh, fl)

    with mp.workdps(dps):
        G = dd_matrix_to_mp(Gh, Gl)
        q = dd_matrix_to_mp(qh, ql)
        K = mp.matrix(7)
        for i in range(6):
            for j in range(6):
                K[i, j] = G[i, j]
            K[i, 6] = G[i, 6] - q[i]
            K[6, i] = K[i, 6]
        K[6, 6] = G[6, 6] - 2 * q[6]
        K = (K + K.T) / 2
        return K


def residual_gram_mp(Rh, Rl, dps):
    H, L = dd_dot_columns(Rh, Rl, Rh, Rl)
    with mp.workdps(dps):
        M = dd_matrix_to_mp(H, L)
        return (M + M.T) / 2


def capacity_from_K(K):
    S = K[:6, :6]
    g = -K[:6, 6]
    h = -K[6, 6]
    vals, _ = mp.eigsy((S + S.T) / 2)
    if vals[0] <= 0:
        return None, vals
    w = mp.lu_solve(S, g)
    G = h + (g.T * w)[0]
    if G <= 0:
        return None, vals
    return 1 / G, vals


def one_sector(max_mode, sector, dps, refinements):
    modes = np.arange(
        1 if sector == "even-v" else 2,
        max_mode + 1,
        2,
        dtype=int,
    )
    P, _ = frozen_protected_basis(sector, modes)

    # Exact Gram of the frozen binary64 protected basis in DD.
    Gh, Gl = dd_dot_columns(P, None, P, None)
    Gih, Gil, Gi_mp = mp_inverse_split(Gh, Gl, dps)
    Gi = np.array(
        [[float(Gi_mp[i, j]) for j in range(6)] for i in range(6)]
    )

    # Binary64 complement operator is used only as the correction solver.
    A, f = full_source_matrix(modes, sector)
    op, proj, gamma, evals, Y0, yf0, initial_res = build_double_complement(
        A, P, Gi, f, rtol=2e-14
    )

    data = hp_parity_data(
        modes,
        sector,
        dps=dps,
        arch_terms=140,
        correction_terms=40,
    )

    Yh = Y0.copy()
    Yl = np.zeros_like(Yh)
    yfh = yf0.copy()
    yfl = np.zeros_like(yfh)

    # The binary64 correction solver only enforces complement membership to
    # machine precision.  At a 1e-30 protected scalar that leakage is far too
    # large.  Re-project the hi/lo expansions with the DD Gram projector before
    # every residual/variational evaluation.
    Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)
    yfh, yfl = dd_project(P, Gih, Gil, yfh, yfl)

    history = []
    for step in range(refinements + 1):
        Uh, Ul = form_trial(P, Yh, Yl, yfh, yfl)
        AUh, AUl, Rh, Rl, norms = residuals_dd(
            data, P, Gih, Gil, Uh, Ul
        )
        history.append(norms)
        print(sector, "refinement", step, "max DD residual", max(norms))
        if step < refinements:
            Yh, Yl, yfh, yfl = refine_once(
                op, proj, Yh, Yl, yfh, yfl, Rh, Rl
            )
            Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)
            yfh, yfl = dd_project(P, Gih, Gil, yfh, yfl)

    Kt = form_Ktilde(data, Uh, Ul, AUh, AUl, dps)
    RR = residual_gram_mp(Rh, Rl, dps)

    with mp.workdps(dps):
        M = RR / mp.mpf(str(gamma))
        KL = Kt - M
        KU = Kt

        CL, valsL = capacity_from_K(KL)
        CU, valsU = capacity_from_K(KU)
        CM, valsM = capacity_from_K(Kt)

        out = {
            "sector": sector,
            "max_mode": int(max_mode),
            "dimension": int(len(modes)),
            "complement_floor_midpoint": gamma,
            "deflated_lowest_eigenvalues": [float(x) for x in evals],
            "initial_double_residuals": initial_res,
            "dd_residual_history": history,
            "final_max_dd_residual": max(history[-1]),
            "capacity_lower_diagnostic": (
                mp.nstr(CL, 60) if CL is not None else None
            ),
            "capacity_midpoint_variational": (
                mp.nstr(CM, 60) if CM is not None else None
            ),
            "capacity_upper_diagnostic": (
                mp.nstr(CU, 60) if CU is not None else None
            ),
            "K_lower_S_min": mp.nstr(valsL[0], 50),
            "K_mid_S_min": mp.nstr(valsM[0], 50),
            "K_upper_S_min": mp.nstr(valsU[0], 50),
            "residual_gram_norm": mp.nstr(
                max(mp.eigsy(RR)[0]), 50
            ),
            "loewner_error_norm_bound": mp.nstr(
                max(mp.eigsy(M)[0]), 50
            ),
        }
        return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-mode", type=int, default=192)
    parser.add_argument("--dps", type=int, default=120)
    parser.add_argument("--refinements", type=int, default=1)
    args = parser.parse_args()

    rows = [
        one_sector(args.max_mode, "even-v", args.dps, args.refinements),
        one_sector(args.max_mode, "odd-v", args.dps, args.refinements),
    ]

    out = {
        "max_mode": args.max_mode,
        "dps": args.dps,
        "refinements": args.refinements,
        "rows": rows,
        "guardrail": (
            "Finite-section midpoint/refinement diagnostic. The complement "
            "floor and DD arithmetic are not yet outward interval-certified."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    for row in rows:
        print("\nsector =", row["sector"])
        for k, v in row.items():
            if k != "sector":
                print(k, "=", v)

    print("\nwrote", OUT)
    print("GUARDRAIL:", out["guardrail"])


if __name__ == "__main__":
    main()
