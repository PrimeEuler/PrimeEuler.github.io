#!/usr/bin/env python3
"""Direct LDDD shell Schur kernel K_p=<u,S_p^{-1}u> for 4000->8000.

Let the M=8000 finite operator be split at the frozen N=4000 boundary:

    A_M = [[A_N, B^T],
           [B,   D ]].

For a right-hand side b=(0,u) with u_n=1/n on the new shell,

    b^T A_M^{-1} b = u^T S^{-1}u,
    S = D - B A_N^{-1}B^T.

Thus the desired v14.016 kernel can be evaluated directly with the same
embedded frozen-P4 LDDD protected/complement solver, without forming S.

The script reports K_e, K_o and the effective rank-one coefficient

    C_eff = -(K_o-K_e)/(K_o K_e),

which would equal C_S if S_o-S_e were exactly C_S u u^T.

Diagnostic only: the complement floor is still the midpoint finite M=8000
floor, so this is a normalization/structure check rather than an outward
certificate.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from suzuki_M8000_embedded_p4_ldd_capacity import (
    DPS,
    TARGET_MAX,
    embedded_protected_basis,
)
from suzuki_M3999_frozen_p4_source_capacity_midpoint import full_source_matrix
from suzuki_ldd_M11_direct_difference import (
    energy_from_K,
    generic_Ktilde,
    generic_residuals,
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement,
    dd_project,
    form_trial,
    mp_inverse_split,
    refine_once,
)
from suzuki_ldd_source_operator import (
    LD,
    add as dd_add,
    dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,
    split_mpf_ld,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "M8000_shell_u_kernel_ldd_result.json"


def shell_rhs_dd(base_modes, modes):
    bh = np.zeros(len(modes), dtype=LD)
    bl = np.zeros(len(modes), dtype=LD)
    nb = len(base_modes)
    with mp.workdps(DPS):
        for i in range(nb, len(modes)):
            bh[i], bl[i] = split_mpf_ld(1 / mp.mpf(int(modes[i])))
    return bh, bl


def one_sector(sector: str):
    base_modes, modes, P, base_orth, embedded_orth = embedded_protected_basis(
        sector
    )
    Gh, Gl = dd_dot_columns(P, None, P, None)
    Gih, Gil, Gi_mp = mp_inverse_split(Gh, Gl, DPS)
    Gi = np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A, _ = full_source_matrix(modes, sector)
    bh, bl = shell_rhs_dd(base_modes, modes)
    bfloat = (bh + bl).astype(float)

    op, proj, gamma, evals, Y0, yb0, initial_res = build_double_complement(
        A, P, Gi, bfloat, rtol=2e-14
    )
    data = hp_parity_data(
        modes, sector, dps=DPS, arch_terms=160, correction_terms=50
    )

    Yh = Y0.astype(LD)
    Yl = np.zeros_like(Yh, dtype=LD)
    ybh = yb0.astype(LD)
    ybl = np.zeros_like(ybh, dtype=LD)
    Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)
    ybh, ybl = dd_project(P, Gih, Gil, ybh, ybl)

    history = []
    for step in range(2):
        Uh, Ul = form_trial(P, Yh, Yl, ybh, ybl)
        AUh, AUl, Rh, Rl, norms = generic_residuals(
            data, P, Gih, Gil, Uh, Ul, bh, bl
        )
        history.append(norms)
        print(sector, "refinement", step, "max residual", max(norms))
        if step == 0:
            # Reuse the standard refinement logic.  Its source-column sign
            # convention matches the generic K construction here.
            Yh, Yl, ybh, ybl = refine_once(
                op, proj, Yh, Yl, ybh, ybl, Rh, Rl
            )
            Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)
            ybh, ybl = dd_project(P, Gih, Gil, ybh, ybl)

    Kt = generic_Ktilde(Uh, Ul, AUh, AUl, bh, bl, DPS)
    with mp.workdps(DPS):
        energy = energy_from_K(Kt)
        return {
            "sector": sector,
            "base_last_mode": int(base_modes[-1]),
            "target_last_mode": int(modes[-1]),
            "dimension": len(modes),
            "K_shell_midpoint": mp.nstr(energy, 80),
            "embedded_complement_floor_midpoint": gamma,
            "initial_double_residuals": initial_res,
            "ldd_residual_history": history,
        }


def main():
    e = one_sector("even-v")
    o = one_sector("odd-v")

    with mp.workdps(DPS):
        Ke = mp.mpf(e["K_shell_midpoint"])
        Ko = mp.mpf(o["K_shell_midpoint"])
        dK = Ko - Ke
        Ceff = -dK/(Ko*Ke)

    out = {
        "even": e,
        "odd": o,
        "paired": {
            "K_odd_minus_even": mp.nstr(dK, 70),
            "C_eff_from_Riccati_rank1": mp.nstr(Ceff, 70),
            "C_S_direct_M11_target": "421.8402156103752305874726998102954",
            "C_eff_minus_direct_target": mp.nstr(
                Ceff-mp.mpf("421.8402156103752305874726998102954"), 60
            ),
        },
        "guardrail": (
            "Finite M8000 shell-kernel midpoint diagnostic. C_eff is an "
            "effective coefficient including all parity-difference structure "
            "seen by u on this finite shell; it need not equal the asymptotic "
            "leading C_S before residual operator terms are separated."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True)+"\n")

    print("\nPAIRED")
    print(json.dumps(out["paired"], indent=2))
    print("\nwrote", OUT)


if __name__ == "__main__":
    main()
