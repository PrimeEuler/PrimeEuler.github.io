#!/usr/bin/env python3
"""180-digit protected Feshbach gate for a Euclidean shell-Schur floor.

For N=4000 and M=8000, write the finite operator as

    A_M = [[A_N, B^T],
           [B,   D ]].

For the Euclidean shell projector Pi_Q onto modes N<n<=M,

    A_M(mu) := A_M - mu Pi_Q.

Since A_N is unchanged, positivity of A_M(mu) is equivalent to

    S_{N->M} - mu I > 0,

where S_{N->M}=D-B A_N^{-1}B^T is the finite-shell Schur complement.

Binary64 cannot resolve the six protected eigenvalues of A_M(mu), so this
script uses the frozen N=4000 six-plane and the v14.008 LDDD residual
refinement:
  * binary64 only solves the stiff complement;
  * source-faithful operator actions are recomputed in LDDD;
  * the 6x6 protected Schur matrix is accumulated in LDDD/mpmath;
  * R^*D^{-1}R gives a one-sided midpoint Loewner correction.

Targets:
  even-v: mu = 0.10
  odd-v:  mu = 0.40

If the lower Loewner 6x6 matrix is positive and the shifted stiff complement
is positive, the finite M=8000 shell has the corresponding midpoint Euclidean
Schur floor.

Guardrail: finite M=8000 midpoint/LDDD gate only.  The complement floor used
in the residual correction is still a midpoint eigsh value; no infinite-tail
attachment or final outward exact-source interval is asserted here.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from suzuki_M8000_embedded_p4_ldd_capacity import (
    DPS,
    embedded_protected_basis,
)
from suzuki_M3999_frozen_p4_source_capacity_midpoint import full_source_matrix
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement,
    dd_matrix_to_mp,
    dd_project,
    mp_inverse_split,
    residual_gram_mp,
    solve_correction,
)
from suzuki_ldd_source_operator import (
    LD,
    add as dd_add,
    dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,
    matvec as dd_matvec,
    mul_d as dd_mul_d,
    norm2 as dd_norm2,
    sub as dd_sub,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "M8000_shifted_shell_feshbach_ldd_result.json"

TARGET_MU = {
    "even-v": 0.10,
    "odd-v": 0.40,
}


def shifted_binary_matrix(A, shell_start, mu):
    B = A.copy()
    idx = np.arange(shell_start, A.shape[0])
    B[idx, idx] -= mu
    return B


def shifted_dd_matvec(data, Xh, Xl, shell_start, mu):
    Yh, Yl = dd_matvec(data, Xh, Xl)
    shift = np.zeros(Xh.shape[0], dtype=LD)
    shift[shell_start:] = LD(mu)
    Sh, Sl = dd_mul_d(Xh, Xl, shift[:, None])
    return dd_sub(Yh, Yl, Sh, Sl)


def coupling_residuals(data, P, Gih, Gil, Wh, Wl, shell_start, mu):
    AWh, AWl = shifted_dd_matvec(data, Wh, Wl, shell_start, mu)
    Rh, Rl = dd_project(P, Gih, Gil, AWh, AWl)
    norms = [dd_norm2(Rh[:, j], Rl[:, j]) for j in range(P.shape[1])]
    return AWh, AWl, Rh, Rl, norms


def form_variational(Wh, Wl, AWh, AWl, dps):
    H, L = dd_dot_columns(Wh, Wl, AWh, AWl)
    with mp.workdps(dps):
        S = dd_matrix_to_mp(H, L)
        return (S + S.T) / 2


def one_gate(sector, mu):
    base_modes, modes, P, base_orth, embedded_orth = embedded_protected_basis(
        sector
    )
    shell_start = len(base_modes)

    Gh, Gl = dd_dot_columns(P, None, P, None)
    Gih, Gil, Gi_mp = mp_inverse_split(Gh, Gl, DPS)
    Gi = np.array(
        [[float(Gi_mp[i, j]) for j in range(6)] for i in range(6)]
    )

    A, _ = full_source_matrix(modes, sector)
    Ashift = shifted_binary_matrix(A, shell_start, mu)

    # Zero seventh RHS: build_double_complement still supplies the six
    # coupling solves and the midpoint stiff-complement floor.
    zrhs = np.zeros(len(modes), dtype=float)
    op, proj, gamma, evals, Y0, _, initial_res = build_double_complement(
        Ashift, P, Gi, zrhs, rtol=2e-14
    )
    initial_res = initial_res[:6]

    if gamma <= 0:
        raise RuntimeError((sector, mu, "shifted complement not positive", gamma))

    data = hp_parity_data(
        modes,
        sector,
        dps=DPS,
        arch_terms=160,
        correction_terms=50,
    )

    Yh = Y0.astype(LD)
    Yl = np.zeros_like(Yh, dtype=LD)
    Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)

    history = []
    for step in range(2):
        Wh, Wl = dd_sub(P, np.zeros_like(P, dtype=LD), Yh, Yl)
        AWh, AWl, Rh, Rl, norms = coupling_residuals(
            data, P, Gih, Gil, Wh, Wl, shell_start, mu
        )
        history.append([float(x) for x in norms])
        print(sector, "mu", mu, "refinement", step,
              "max residual", max(norms))
        if step == 0:
            for j in range(6):
                rhs = Rh[:, j] + Rl[:, j]
                delta = solve_correction(op, proj, rhs, rtol=2e-14)
                Yh[:, j], Yl[:, j] = dd_add(
                    Yh[:, j], Yl[:, j],
                    delta, np.zeros_like(delta, dtype=LD)
                )
            Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)

    St = form_variational(Wh, Wl, AWh, AWl, DPS)
    RR = residual_gram_mp(Rh, Rl, DPS)

    with mp.workdps(DPS):
        M = RR / mp.mpf(str(gamma))
        SL = (St - M + (St - M).T) / 2
        SU = St
        valsL, _ = mp.eigsy(SL)
        valsU, _ = mp.eigsy(SU)
        rrvals, _ = mp.eigsy((RR + RR.T) / 2)
        mvals, _ = mp.eigsy((M + M.T) / 2)

        return {
            "sector": sector,
            "mu": mu,
            "base_last_mode": int(base_modes[-1]),
            "target_last_mode": int(modes[-1]),
            "dimension": len(modes),
            "shell_dimension": len(modes)-len(base_modes),
            "base_orthogonality_defect": base_orth,
            "embedded_orthogonality_defect": embedded_orth,
            "shifted_complement_floor_midpoint": gamma,
            "shifted_complement_low_eigenvalues": [float(x) for x in evals],
            "initial_double_residuals": initial_res,
            "ldd_residual_history": history,
            "protected_upper_eigenvalues": [
                mp.nstr(valsU[j], 60) for j in range(6)
            ],
            "protected_lower_eigenvalues": [
                mp.nstr(valsL[j], 60) for j in range(6)
            ],
            "protected_lower_min": mp.nstr(valsL[0], 60),
            "residual_gram_norm": mp.nstr(rrvals[-1], 50),
            "loewner_error_norm_midpoint": mp.nstr(mvals[-1], 50),
            "finite_shift_positive_midpoint_ldd": bool(valsL[0] > 0),
        }


def main():
    rows = []
    for sector in ("even-v", "odd-v"):
        row = one_gate(sector, TARGET_MU[sector])
        rows.append(row)
        print("\n", sector)
        print("mu =", row["mu"])
        print("complement floor =", row["shifted_complement_floor_midpoint"])
        print("protected lower eigs =", row["protected_lower_eigenvalues"])
        print("positive =", row["finite_shift_positive_midpoint_ldd"])

    out = {
        "rows": rows,
        "guardrail": (
            "Finite M8000 LDDD/midpoint shell-Schur floor gate only. "
            "The six-dimensional reduced arithmetic is high precision, but "
            "the stiff-complement floor in the Loewner correction is not yet "
            "an outward interval and the infinite tail is not attached."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("\nwrote", OUT)


if __name__ == "__main__":
    main()
