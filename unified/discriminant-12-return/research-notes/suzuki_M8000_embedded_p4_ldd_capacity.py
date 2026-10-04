#!/usr/bin/env python3
"""M=8000 LDDD capacity gate with the N=4000 six-plane embedded unchanged.

Purpose
-------
Implement the v14.011 near/far split numerically.

The validated theorem-scale finite section ends at:
  * even-v: mode 3999;
  * odd-v:  mode 4000.

For the target section through:
  * even-v: mode 7999;
  * odd-v:  mode 8000,

freeze exactly the same six-dimensional protected plane used at N=4000,
embed it by zeros on the newly added shell, and treat every new mode as part
of the complement.  Do NOT re-Ritz or regenerate a carrier.

Then:
  * build the source-faithful M=8000 finite operator;
  * certify numerically that the embedded-plane complement is positive;
  * solve the six coupling columns plus source column in binary64;
  * evaluate/refine their residuals in the validated LDDD operator arithmetic;
  * form the 7x7 variational augmented reduction;
  * use the quadratic residual-Gram Loewner correction;
  * report finite-section capacities and the exact nested normalized shell
    increments eta = C_4000/C_8000 - 1.

This remains a midpoint diagnostic because the M=8000 complement floor is
not yet outward-certified.  It is designed to make n >= 2N the subsequent
far-tail region, where m/n <= 1/2 for all retained m <= N.
"""
from __future__ import annotations

import gc
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
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement,
    capacity_from_K,
    dd_matrix_to_mp,
    dd_project,
    form_Ktilde,
    form_trial,
    mp_inverse_split,
    refine_once,
    residual_gram_mp,
    residuals_dd,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "M8000_embedded_p4_ldd_capacity_result.json"

BASE_MAX = 4000
TARGET_MAX = 8000
DPS = 180

BASE_CAP = {
    "even-v": mp.mpf(
        "7.5773007563692575306680936106689123586265630100827471120927e-30"
    ),
    "odd-v": mp.mpf(
        "2.1845239838296620020805542670090522874748063437543145074951e-25"
    ),
}


def parity_modes(sector: str, max_mode: int) -> np.ndarray:
    start = 1 if sector == "even-v" else 2
    return np.arange(start, max_mode + 1, 2, dtype=int)


def embedded_protected_basis(sector: str):
    base_modes = parity_modes(sector, BASE_MAX)
    target_modes = parity_modes(sector, TARGET_MAX)

    if not np.array_equal(target_modes[: len(base_modes)], base_modes):
        raise RuntimeError((sector, "target prefix is not the frozen base"))

    Pbase, base_orth = frozen_protected_basis(sector, base_modes)
    P = np.zeros((len(target_modes), Pbase.shape[1]), dtype=float)
    P[: len(base_modes), :] = Pbase

    orth = float(np.linalg.norm(P.T @ P - np.eye(6), ord=2))
    if orth > 1e-12:
        raise RuntimeError((sector, "embedded protected basis lost orthogonality", orth))

    if np.linalg.norm(P[len(base_modes):, :]) != 0.0:
        raise RuntimeError((sector, "new shell must carry zero protected entries"))

    return base_modes, target_modes, P, float(base_orth), orth


def one_sector(sector: str):
    base_modes, modes, P, base_orth, embedded_orth = embedded_protected_basis(
        sector
    )

    print("\n", sector, "dimension", len(modes))
    print("base last mode =", int(base_modes[-1]))
    print("target last mode =", int(modes[-1]))

    # Exact DD Gram of the frozen binary64 protected vectors.
    Gh, Gl = dd_dot_columns(P, None, P, None)
    Gih, Gil, Gi_mp = mp_inverse_split(Gh, Gl, DPS)
    Gi = np.array(
        [[float(Gi_mp[i, j]) for j in range(6)] for i in range(6)]
    )

    # Binary64 finite operator is ONLY the correction solver / midpoint
    # complement-floor producer.  The final residual evaluation is LDDD.
    A, f = full_source_matrix(modes, sector)
    print(sector, "built binary64 A", A.shape)

    op, proj, gamma, evals, Y0, yf0, initial_double_res = (
        build_double_complement(A, P, Gi, f, rtol=2e-14)
    )
    print(sector, "embedded complement low eigs =", evals)
    print(sector, "embedded complement floor =", gamma)

    if not np.isfinite(gamma) or gamma <= 0.0:
        raise RuntimeError((sector, "embedded M8000 complement not positive", gamma))

    # The closures op/proj retain A.  Build LDDD source data after the
    # complement gate succeeds.
    data = hp_parity_data(
        modes,
        sector,
        dps=DPS,
        arch_terms=160,
        correction_terms=50,
    )
    print(sector, "built LDDD source operator data")

    Yh = Y0.astype(LD)
    Yl = np.zeros_like(Yh, dtype=LD)
    yfh = yf0.astype(LD)
    yfl = np.zeros_like(yfh, dtype=LD)

    Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)
    yfh, yfl = dd_project(P, Gih, Gil, yfh, yfl)

    history = []
    for step in range(2):
        Uh, Ul = form_trial(P, Yh, Yl, yfh, yfl)
        AUh, AUl, Rh, Rl, norms = residuals_dd(
            data, P, Gih, Gil, Uh, Ul
        )
        history.append([float(x) for x in norms])
        print(
            sector,
            "refinement",
            step,
            "max LDDD residual",
            max(norms),
        )

        if step == 0:
            Yh, Yl, yfh, yfl = refine_once(
                op, proj, Yh, Yl, yfh, yfl, Rh, Rl
            )
            Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)
            yfh, yfl = dd_project(P, Gih, Gil, yfh, yfl)

    Kt = form_Ktilde(data, Uh, Ul, AUh, AUl, DPS)
    RR = residual_gram_mp(Rh, Rl, DPS)

    with mp.workdps(DPS):
        gamma_mp = mp.mpf(str(gamma))
        M = RR / gamma_mp
        KL = Kt - M
        KU = Kt

        CL, valsL = capacity_from_K(KL)
        CM, valsM = capacity_from_K(Kt)
        CU, valsU = capacity_from_K(KU)

        if CM is None or CL is None or CU is None:
            raise RuntimeError(
                (
                    sector,
                    "M8000 augmented crossing did not stay in the positive regime",
                    mp.nstr(valsL[0], 30),
                    mp.nstr(valsM[0], 30),
                    mp.nstr(valsU[0], 30),
                )
            )

        Cbase = BASE_CAP[sector]
        eta_mid = Cbase / CM - 1
        eta_lo = Cbase / CU - 1
        eta_hi = Cbase / CL - 1

        rr_eigs, _ = mp.eigsy((RR + RR.T) / 2)
        m_eigs, _ = mp.eigsy((M + M.T) / 2)

        row = {
            "sector": sector,
            "base_max_requested": BASE_MAX,
            "base_last_mode": int(base_modes[-1]),
            "target_max_requested": TARGET_MAX,
            "target_last_mode": int(modes[-1]),
            "dimension": int(len(modes)),
            "base_protected_orthogonality_defect": base_orth,
            "embedded_protected_orthogonality_defect": embedded_orth,
            "new_shell_protected_norm": float(
                np.linalg.norm(P[len(base_modes):, :])
            ),
            "embedded_complement_lowest_eigenvalues": [
                float(x) for x in evals
            ],
            "embedded_complement_floor_midpoint": gamma,
            "initial_double_residuals": initial_double_res,
            "ldd_residual_history": history,
            "final_max_ldd_residual": max(history[-1]),
            "capacity_lower_diagnostic": mp.nstr(CL, 70),
            "capacity_midpoint_variational": mp.nstr(CM, 70),
            "capacity_upper_diagnostic": mp.nstr(CU, 70),
            "base_capacity_midpoint": mp.nstr(Cbase, 70),
            "eta_4000_to_8000_lower_diagnostic": mp.nstr(eta_lo, 60),
            "eta_4000_to_8000_midpoint": mp.nstr(eta_mid, 60),
            "eta_4000_to_8000_upper_diagnostic": mp.nstr(eta_hi, 60),
            "K_lower_S_min": mp.nstr(valsL[0], 50),
            "K_mid_S_min": mp.nstr(valsM[0], 50),
            "K_upper_S_min": mp.nstr(valsU[0], 50),
            "residual_gram_norm": mp.nstr(max(rr_eigs), 50),
            "loewner_error_norm_bound": mp.nstr(max(m_eigs), 50),
        }

    # Release large arrays before the next parity.
    del A, f, data, Y0, yf0, Yh, Yl, yfh, yfl
    gc.collect()

    return row


def main():
    rows = [
        one_sector("even-v"),
        one_sector("odd-v"),
    ]

    with mp.workdps(DPS):
        Ce = mp.mpf(rows[0]["capacity_midpoint_variational"])
        Co = mp.mpf(rows[1]["capacity_midpoint_variational"])
        q = Ce / Co
        kappa = (Co - Ce) / (Co + Ce)

        eta_e = mp.mpf(rows[0]["eta_4000_to_8000_midpoint"])
        eta_o = mp.mpf(rows[1]["eta_4000_to_8000_midpoint"])

        summary = {
            "Ce_target": mp.nstr(Ce, 70),
            "Co_target": mp.nstr(Co, 70),
            "q_target": mp.nstr(q, 60),
            "kappa_target": mp.nstr(kappa, 60),
            "eta_even_base_to_target": mp.nstr(eta_e, 60),
            "eta_odd_base_to_target": mp.nstr(eta_o, 60),
            "eta_odd_minus_even": mp.nstr(eta_o - eta_e, 60),
            "q_ratio_target_over_base_from_eta": mp.nstr(
                (1 + eta_o) / (1 + eta_e),
                60,
            ),
        }

    out = {
        "base_max": BASE_MAX,
        "target_max": TARGET_MAX,
        "dps": DPS,
        "rows": rows,
        "summary": summary,
        "guardrail": (
            "Finite-section midpoint diagnostic at target cutoff " + str(TARGET_MAX) + ". The N=4000 protected "
            "six-plane is embedded unchanged. LDDD residuals and quadratic "
            "Loewner corrections are evaluated, but the target complement "
            "floor and all-mode arithmetic are not yet outward interval-certified."
        ),
    }

    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print("\nSUMMARY")
    print(json.dumps(summary, indent=2))
    print("\nwrote", OUT)
    print("GUARDRAIL:", out["guardrail"])


if __name__ == "__main__":
    main()
