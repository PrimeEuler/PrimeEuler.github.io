#!/usr/bin/env python3
"""M=32000 fixed-FFT graph-shear diagnostic for the finite-section floor.

This is the first Lane-A gate requested by v14.080/v14.083.

For the frozen six-plane P and the calibrated fixed-FFT finite operator A_N,
solve on Q=P^perp

    (Q A_N Q) Y = Q A_N P.

For the exact Feshbach graph factorization, if
  * S is the protected Schur matrix,
  * C=Q A_N Q is the complement block,
  * tau=||Y||_2 with Y=C^{-1}Q A_N P,
then the unit-triangular congruence has

    sigma_min(T) >= (sqrt(tau^2+4)-tau)/2,

and therefore

    lambda_min(A_N)
      >= min(lambda_min(S), lambda_min(C)) * sigma_min(T)^2.

This diagnostic computes tau and combines it with the already-completed
arch-200/LDDD 32k protected pivot and fixed-FFT complement midpoint.  It is
NOT an outward certificate: the purpose is only to decide whether the graph
route has enough headroom before outwardizing the scalar/operator, complement,
and shear errors.

Important: do not recompute the ~1e-30 protected pivot by the fast stationary
long-double contraction here.  At 32k that subtraction is below the accuracy
of the accelerated contraction.  The load-bearing midpoint values below come
from the completed full arch-200/LDDD fixed-FFT replay.
"""
from __future__ import annotations

import argparse, json, math
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import cg

from suzuki_fixed_fft_stationary_feshbach import base_payload
from suzuki_full_fft_fixed_capacity_replay import fixed_operator
from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import (
    embedded_P, modes_for,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "M32000_fixed_fft_graph_shear_result.json"

CUTOFF = 32000
TARGET_MU = 1.2e-31

# Completed arch-200/LDDD 32k capacity replay values.
PROTECTED_S_MID = {
    "even-v": 5.67126816594919256613793717097e-30,
    "odd-v": 1.42959091963877922082616902732e-26,
}
COMPLEMENT_GAMMA_MID = {
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

    svals = np.linalg.svd(Y, compute_uv=False)
    tau = float(svals[0])

    # Report actual frozen-P Gram spectrum as a coordinate sanity check.
    G = P.T @ P
    gevals = np.linalg.eigvalsh((G + G.T) / 2)

    sigma_shear = (math.sqrt(tau * tau + 4.0) - tau) / 2.0
    sigma2 = sigma_shear * sigma_shear

    smin = PROTECTED_S_MID[sector]
    gamma = COMPLEMENT_GAMMA_MID[sector]
    mu_mid = min(smin, gamma) * sigma2

    ratio = TARGET_MU / smin
    if 0.0 < ratio < 1.0:
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
        "protected_S_min_arch200_ldd_midpoint": smin,
        "complement_gamma_fixed_fft_midpoint": gamma,
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
            "Diagnostic only. Protected pivot comes from the completed arch-200/LDDD "
            "32k replay; no outward certification of the 32k finite-section floor."
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
