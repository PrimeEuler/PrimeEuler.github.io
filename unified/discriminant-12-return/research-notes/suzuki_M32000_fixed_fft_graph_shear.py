#!/usr/bin/env python3
"""M=32000 fixed-FFT graph-shear diagnostic for the finite-section floor.

This is the first Lane-A gate requested by v14.080/v14.083.

For the frozen six-plane P and the exact fixed-FFT finite operator A_N,
solve on Q=P^perp

    (Q A_N Q) Y = Q A_N P.

Then the exact block graph/Feshbach factorization is

    A_N = T^* diag(S, C) T,

with C=Q A_N Q, S=P^*A_NP-(Q A_NP)^*C^{-1}(Q A_NP), and a unit
triangular shear whose off-diagonal block is Y (up to the harmless frozen
P Gram normalization already used throughout the project).

For tau=||Y||_2, the exact 2x2 shear singular-value formula gives

    sigma_min(T)^2 >= ((sqrt(tau^2+4)-tau)/2)^2,

hence a midpoint diagnostic floor

    mu_mid >= min(lambda_min(S), gamma_Q) * sigma_min(T)^2.

This script is diagnostic only: it does NOT outward-certify gamma_Q,
lambda_min(S), or tau.  Its purpose is to decide whether the graph route
has enough numerical headroom to pursue the outward certificate.

The protected Schur matrix uses the same stationary-Feshbach contraction
as suzuki_fixed_fft_stationary_feshbach.py, including DD replacement of
the base P^T A P / A P payload.
"""
from __future__ import annotations

import argparse, json, math
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.sparse.linalg import cg

from suzuki_fixed_fft_stationary_feshbach import (
    base_payload, ld_dot_cols, mp_from_ld,
)
from suzuki_full_fft_fixed_capacity_replay import fixed_operator, DPS
from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import (
    embedded_P, modes_for,
)
from suzuki_ldd_source_operator import LD

HERE = Path(__file__).resolve().parent
OUT = HERE / "M32000_fixed_fft_graph_shear_result.json"

CUTOFF = 32000
TARGET_MU = 1.2e-31
GAMMA_MID = {
    "even-v": 0.15515504171681802,
    "odd-v": 0.5320538996387548,
}


def one(sector: str):
    base = base_payload(sector)
    modes = modes_for(sector, CUTOFF)
    P = embedded_P(sector, modes)

    raw_mv, proj, op, _ = fixed_operator(modes, sector, P, base["Gi"])

    AP = np.asarray(raw_mv(P), dtype=float)
    E = proj(AP)

    Y = np.empty_like(E)
    iters = []
    residuals = []
    for j in range(6):
        cnt = [0]
        y, info = cg(
            op, E[:, j], rtol=2e-14, atol=0.0, maxiter=30000,
            callback=lambda _: cnt.__setitem__(0, cnt[0] + 1),
        )
        if info != 0:
            raise RuntimeError(("graph CG failed", sector, j, info))
        y = proj(y)
        Y[:, j] = y
        iters.append(cnt[0])
        residuals.append(float(np.linalg.norm(E[:, j] - op @ y)))

    # Stationary protected Schur contraction.
    nb = len(base["modes"])
    APld = np.asarray(AP, dtype=LD)
    APld[:nb, :] = base["AP_ld"]
    APY = ld_dot_cols(APld, np.asarray(Y, dtype=LD))

    with mp.workdps(DPS):
        S = mp.matrix(base["K0"])
        for i in range(6):
            for j in range(6):
                S[i, j] -= mp_from_ld(APY[i, j])
        S = (S + S.T) / 2
        seigs, _ = mp.eigsy(S)
        smin = seigs[0]

    svals = np.linalg.svd(Y, compute_uv=False)
    tau = float(svals[0])

    # Frozen P is extremely close to orthonormal; report the actual Gram spectrum.
    G = P.T @ P
    gevals = np.linalg.eigvalsh((G + G.T) / 2)

    sigma_shear = (math.sqrt(tau * tau + 4.0) - tau) / 2.0
    sigma2 = sigma_shear * sigma_shear
    gamma = GAMMA_MID[sector]
    smin_f = float(smin)
    mu_mid = min(smin_f, gamma) * sigma2

    ratio = TARGET_MU / smin_f
    if ratio < 1.0:
        sig_req = math.sqrt(ratio)
        tau_max = 1.0 / sig_req - sig_req
    else:
        tau_max = 0.0

    row = {
        "sector": sector,
        "cutoff": CUTOFF,
        "dimension": len(modes),
        "graph_shear_tau_2norm": tau,
        "graph_shear_singular_values": [float(x) for x in svals],
        "cg_iters": iters,
        "recomputed_graph_residual_max": max(residuals),
        "protected_S_min_midpoint": mp.nstr(smin, 50),
        "complement_gamma_midpoint_external": gamma,
        "P_gram_min": float(gevals[0]),
        "P_gram_max": float(gevals[-1]),
        "shear_sigma_min_lower_formula": sigma_shear,
        "shear_sigma_min_squared": sigma2,
        "mu_midpoint_congruence_candidate": mu_mid,
        "target_mu": TARGET_MU,
        "headroom_mu_over_target": mu_mid / TARGET_MU,
        "tau_max_allowed_if_S_midpoint_exact": tau_max,
        "tau_headroom_factor": tau_max / tau if tau > 0 else None,
        "guardrail": (
            "Diagnostic only. No outward certification of the 32k finite-section "
            "floor. Uses the calibrated fixed-FFT operator and stationary-Feshbach "
            "protected contraction to test graph-shear headroom."
        ),
    }
    print(json.dumps(row, indent=2), flush=True)
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sector", choices=["even-v", "odd-v"], required=True)
    args = ap.parse_args()
    row = one(args.sector)
    OUT.write_text(json.dumps(row, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
