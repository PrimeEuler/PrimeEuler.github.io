#!/usr/bin/env python3
"""M3999/4000 midpoint test of the frozen P4 source-active six-plane.

This is the first theorem-scale cutoff diagnostic after v14.003/v14.005.

For each parity at a=1, lambda=0, rho=0:
  * build the source-faithful finite section through mode 3999/4000;
  * freeze P = {two low source-active coordinates} plus the already-frozen
    P4 carrier restricted to this cutoff;
  * do NOT regenerate a resonance basis;
  * define Q = I - P P^T;
  * solve only the stiff complement with the SPD deflated operator

        D_def = Q A Q + P P^T,

    whose restriction to Q is exactly the complement block and whose
    restriction to P is the identity;
  * solve the six protected coupling columns and source column jointly;
  * assemble the protected Schur/source data;
  * source-align the 6D protected problem and report the scalar crossing.

The capacity itself is not used as a carrier-quality metric; exact full
capacity is partition invariant.  The relevant diagnostics are:
  1. complement floor;
  2. joint complement residual;
  3. source-orthogonal 5-plane floor;
  4. source-aligned scalar s and alpha=s/||g||^2.

Midpoint diagnostic only.  No outward exact-vs-float operator enclosure,
no infinite tail, and no Xi theorem is asserted.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.sparse.linalg import LinearOperator, cg, eigsh

from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data,
    offdiag,
    pole_vector,
)
from suzuki_kkt_remote_residual_certificate import source_rows

HERE = Path(__file__).resolve().parent
P4ROOT = HERE / "p4_payload"
OUT = HERE / "M3999_frozen_p4_source_capacity_midpoint_result.json"


def frozen_protected_basis(sector: str, full_modes: np.ndarray):
    root = P4ROOT / sector
    modes_p4 = np.load(root / "modes.npy").astype(int)
    Z = np.load(root / "Z.npy")

    tail_modes = full_modes[2:]
    mask = modes_p4 <= int(full_modes[-1])
    modes_cut = modes_p4[mask]
    Zcut = Z[mask, :]

    if not np.array_equal(modes_cut, tail_modes):
        raise RuntimeError(
            (
                sector,
                "frozen-P4 mode mismatch",
                modes_cut[:6].tolist(),
                tail_modes[:6].tolist(),
                modes_cut[-6:].tolist(),
                tail_modes[-6:].tolist(),
            )
        )

    qtail, rtail = np.linalg.qr(Zcut, mode="reduced")
    if np.min(np.abs(np.diag(rtail))) < 1e-12:
        raise RuntimeError((sector, "restricted frozen P4 lost rank"))

    n = len(full_modes)
    P = np.zeros((n, 6), dtype=float)
    P[0, 0] = 1.0
    P[1, 1] = 1.0
    P[2:, 2:] = qtail

    orth = np.linalg.norm(P.T @ P - np.eye(6), ord=2)
    if orth > 1e-12:
        raise RuntimeError((sector, "protected basis not orthonormal", orth))
    return P, orth


def full_source_matrix(modes: np.ndarray, sector: str):
    z, diag = endpoint_data(modes, sign=-1, rho=0.0)
    A = offdiag(modes, modes, z, z)
    np.fill_diagonal(A, diag)
    p, alpha = pole_vector(modes, sector)
    A += alpha * np.outer(p, p)
    A = (A + A.T) / 2.0
    f = source_rows(modes, sector)
    return A, f


def projector(P: np.ndarray, x: np.ndarray):
    return x - P @ (P.T @ x)


def solve_joint(A: np.ndarray, P: np.ndarray, f: np.ndarray, rtol: float):
    n = A.shape[0]

    def mv(x):
        x = np.asarray(x, dtype=float)
        qx = projector(P, x)
        return projector(P, A @ qx) + P @ (P.T @ x)

    op = LinearOperator((n, n), matvec=mv, dtype=float)

    # Complement spectral floor of the deflated SPD operator.  Protected
    # directions have eigenvalue exactly 1, so the smallest eigenvalue is
    # the complement floor whenever that floor is < 1.
    evals = eigsh(op, k=4, which="SA", return_eigenvectors=False, tol=1e-11)
    evals = np.sort(evals)
    complement_floor = float(evals[0])

    AP = A @ P
    E = projector(P, AP)
    fQ = projector(P, f)

    rhs = np.column_stack([E, fQ])
    sol = np.empty_like(rhs)
    residuals = []
    infos = []
    iters = []

    for j in range(rhs.shape[1]):
        count = [0]

        def cb(_):
            count[0] += 1

        x, info = cg(
            op,
            rhs[:, j],
            rtol=rtol,
            atol=0.0,
            maxiter=20000,
            callback=cb,
        )
        sol[:, j] = x
        rr = rhs[:, j] - mv(x)
        residuals.append(float(np.linalg.norm(rr)))
        infos.append(int(info))
        iters.append(int(count[0]))

    if any(info != 0 for info in infos):
        raise RuntimeError(("CG did not converge", infos, residuals))

    # Project once more to suppress roundoff P components.
    sol = projector(P, sol)

    return {
        "op": op,
        "eigs": [float(x) for x in evals],
        "floor": complement_floor,
        "E": E,
        "fQ": fQ,
        "Y": sol[:, :6],
        "yf": sol[:, 6],
        "residuals": residuals,
        "iters": iters,
    }


def householder_source_mp(g):
    n = g.rows
    beta = mp.sqrt((g.T * g)[0])
    u = g / beta
    e1 = mp.matrix(n, 1)
    e1[0] = 1
    v = e1 - u
    vv = (v.T * v)[0]
    if abs(vv) < mp.eps * 100:
        H = mp.eye(n)
    else:
        H = mp.eye(n) - (2 / vv) * (v * v.T)
    return H, beta


def reduced_scalar(A, P, f, solved, dps):
    E = solved["E"]
    fQ = solved["fQ"]
    Y = solved["Y"]
    yf = solved["yf"]

    # Form the small matrices with longdouble accumulation.
    Pld = P.astype(np.longdouble)
    AldP = (A @ P).astype(np.longdouble)
    Eld = E.astype(np.longdouble)
    Yld = Y.astype(np.longdouble)
    fld = f.astype(np.longdouble)
    fQld = fQ.astype(np.longdouble)
    yfld = yf.astype(np.longdouble)

    App = Pld.T @ AldP
    S = App - Eld.T @ Yld
    S = (S + S.T) / np.longdouble(2.0)

    fp = Pld.T @ fld
    g = fp - Eld.T @ yfld
    h = fQld @ yfld

    # Convert only the reduced 6D data to arbitrary precision; this does not
    # repair finite-section assembly error, but prevents another loss of
    # precision in the final 6D cancellation.
    with mp.workdps(dps):
        Smp = mp.matrix(
            [[mp.mpf(str(S[i, j])) for j in range(6)] for i in range(6)]
        )
        gmp = mp.matrix([mp.mpf(str(g[i])) for i in range(6)])
        hmp = mp.mpf(str(h))

        H, beta = householder_source_mp(gmp)
        R = H.T * Smp * H
        R = (R + R.T) / 2

        a = R[0, 0]
        c = R[1:, 0]
        D5 = R[1:, 1:]
        vals5, _ = mp.eigsy(D5)

        if vals5[0] <= 0:
            return {
                "source_orthogonal_positive": False,
                "fiveplane_min": mp.nstr(vals5[0], 50),
            }

        z = mp.lu_solve(D5, c)
        correction = (c.T * z)[0]
        s = a - correction
        alpha = s / (beta * beta)
        capacity = alpha / (1 + alpha * hmp)

        valsS, _ = mp.eigsy(Smp)
        return {
            "source_orthogonal_positive": True,
            "beta": mp.nstr(beta, 50),
            "source_axis_a": mp.nstr(a, 50),
            "fiveplane_correction": mp.nstr(correction, 50),
            "scalar_s": mp.nstr(s, 50),
            "fiveplane_eigenvalues": [mp.nstr(vals5[j], 50) for j in range(5)],
            "fiveplane_min": mp.nstr(vals5[0], 50),
            "S6_eigenvalues": [mp.nstr(valsS[j], 50) for j in range(6)],
            "alpha_crossing": mp.nstr(alpha, 50),
            "h": mp.nstr(hmp, 50),
            "alpha_times_h": mp.nstr(alpha * hmp, 40),
            "capacity_midpoint": mp.nstr(capacity, 50),
            "fiveplane_to_scalar_abs_ratio": (
                mp.nstr(vals5[0] / abs(s), 40) if s != 0 else "inf"
            ),
        }


def one_sector(sector: str, rtol: float, dps: int):
    if sector == "even-v":
        modes = np.arange(1, 4000, 2, dtype=int)
    elif sector == "odd-v":
        modes = np.arange(2, 4001, 2, dtype=int)
    else:
        raise ValueError(sector)

    print("\nbuilding", sector, "dimension", len(modes))
    P, orth = frozen_protected_basis(sector, modes)
    A, f = full_source_matrix(modes, sector)
    print("matrix built", sector)

    solved = solve_joint(A, P, f, rtol=rtol)
    print(
        "joint solves",
        sector,
        "floor", solved["floor"],
        "max residual", max(solved["residuals"]),
        "iterations", solved["iters"],
    )

    scalar = reduced_scalar(A, P, f, solved, dps=dps)
    return {
        "sector": sector,
        "last_mode": int(modes[-1]),
        "dimension": int(len(modes)),
        "protected_orthogonality_defect": float(orth),
        "deflated_lowest_eigenvalues": solved["eigs"],
        "complement_floor_midpoint": solved["floor"],
        "joint_residual_norms": solved["residuals"],
        "joint_max_residual": float(max(solved["residuals"])),
        "cg_iterations": solved["iters"],
        "scalar": scalar,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rtol", type=float, default=2e-14)
    parser.add_argument("--dps", type=int, default=80)
    args = parser.parse_args()

    rows = [
        one_sector("even-v", args.rtol, args.dps),
        one_sector("odd-v", args.rtol, args.dps),
    ]

    out = {
        "rtol": args.rtol,
        "dps_reduced": args.dps,
        "rows": rows,
        "guardrail": (
            "M3999/4000 finite midpoint diagnostic only. Full operator entries "
            "are binary64 source-faithful formulas; no outward exact-vs-float "
            "enclosure or infinite-tail promotion is made."
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
