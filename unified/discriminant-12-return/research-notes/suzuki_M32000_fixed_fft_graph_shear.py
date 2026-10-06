#!/usr/bin/env python3
"""M=32000 fixed-FFT graph/shear and protected-form headroom diagnostic.

Lane-A gate requested by v14.080/v14.083.

For the frozen six-plane P and calibrated fixed-FFT finite operator A_N,
solve on Q=P^perp

    (Q A_N Q) Y = Q A_N P.

If S is the protected Schur matrix and C=Q A_N Q, the exact Feshbach
factorization is a unit-triangular congruence. For tau=||Y||_2,

    sigma_min(T) >= (sqrt(tau^2+4)-tau)/2,

so

    lambda_min(A_N)
      >= min(lambda_min(S), lambda_min(C)) * sigma_min(T)^2.

This script also evaluates a positive pre-cancellation component majorant

    Qcomp = |W|^T H_component |W|,   W=P-Y,

in blocks, using the exact source-faithful midpoint structure.  Qcomp is the
load-bearing magnitude in the conservative LDDD rounding envelope.

Diagnostic only: no theorem promotion.  The protected pivot is consumed from
the completed arch-200/LDDD 32k replay rather than recomputed by the fast
stationary long-double contraction (which loses the ~1e-30 cancellation).
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
from suzuki_endpoint_M3999_midpoint_effective_core import endpoint_data, pole_vector

HERE = Path(__file__).resolve().parent
OUT = HERE / "M32000_fixed_fft_graph_shear_result.json"

CUTOFF = 32000
TARGET_MU = 1.2e-31
ULD = 2.0**-64
CDD_AUDIT_SAFE = 8192.0

PROTECTED_S_MID = {
    "even-v": 5.67126816594919256613793717097e-30,
    "odd-v": 1.42959091963877922082616902732e-26,
}
COMPLEMENT_GAMMA_MID = {
    "even-v": 0.15515504171681802,
    "odd-v": 0.5320538996387548,
}

# Through-16k arch-200 caps, except the even z cap is widened to cover the
# completed 16k<n<=32k incremental interval replay.
SCALAR = {
    "even-v": {
        "eps_z": 5.88e-39,
        "eps_d": 4.317700732362615e-37,
        "eps_p": 7.365230177656668e-40,
        "eps_c": 6.740593794183538e-42,
    },
    "odd-v": {
        "eps_z": 5.876097431412404e-39,
        "eps_d": 1.1754198692159515e-38,
        "eps_p": 4.987119893996533e-41,
        "eps_c": 6.740593794183538e-42,
    },
}


def pnorm_cap(sector: str) -> float:
    if sector == "even-v":
        return math.sqrt(2.0) * math.cosh(0.5)
    return 4.0 * math.sinh(0.5) / math.sqrt(24.0)


def source_operator_radius(sector: str, npts: int) -> float:
    e = SCALAR[sector]
    # H_{15999}<11. ZCAP=10.
    edisp = 11.0 * ((1.0 + e["eps_c"]) * e["eps_z"] + 10.0 * e["eps_c"])
    dp = math.sqrt(float(npts)) * e["eps_p"]
    epole = 2.0 * (2.0 * pnorm_cap(sector) * dp + dp * dp)
    return e["eps_d"] + edisp + epole


def component_qcomp(modes, sector: str, W, chunk: int = 256):
    """Positive component form |W|^T H_component |W|, blockwise."""
    modes = np.asarray(modes, dtype=float)
    W = np.asarray(W, dtype=float)
    aw = np.abs(W)

    z, diag = endpoint_data(modes.astype(int), sign=-1, rho=0.0)
    p, alpha = pole_vector(modes.astype(int), sector)
    az = np.abs(np.asarray(z, dtype=float))
    ap = np.abs(np.asarray(p, dtype=float))
    ad = np.abs(np.asarray(diag, dtype=float))
    aa = abs(float(alpha))
    c = 2.0 / math.pi

    n = len(modes)
    Q = np.zeros((6, 6), dtype=float)
    rowmax = 0.0
    mj = modes[None, :]
    azj = az[None, :]
    apj = ap[None, :]

    for i0 in range(0, n, chunk):
        i1 = min(i0 + chunk, n)
        mi = modes[i0:i1, None]
        den = np.abs(mi * mi - mj * mj)

        # Replace diagonal denominators before division, then overwrite the
        # diagonal entries by the true positive component diagonal.
        rr = np.arange(i1 - i0)
        gg = np.arange(i0, i1)
        den[rr, gg] = 1.0

        B = c * (az[i0:i1, None] * mj + azj * mi) / den
        B += aa * (ap[i0:i1, None] * apj)
        B[rr, gg] = ad[i0:i1] + aa * ap[i0:i1] * ap[i0:i1]

        rowmax = max(rowmax, float(np.max(np.sum(B, axis=1))))
        T = B @ aw
        Q += aw[i0:i1, :].T @ T

    return float(np.max(Q)), Q, rowmax


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

    W = P - Y
    svals = np.linalg.svd(Y, compute_uv=False)
    tau = float(svals[0])

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

    qmax, qmat, rowmax = component_qcomp(modes, sector, W)
    wfrob2 = float(np.sum(W * W))

    eop = source_operator_radius(sector, len(modes))
    esource = eop * wfrob2

    # How large may the public Qcomp cap be if every other protected charge
    # were ignored? This is a useful fail-fast ceiling.
    protected_needed = TARGET_MU / sigma2
    qcap_max_rounding_only = max(
        0.0,
        (smin - protected_needed) /
        (CDD_AUDIT_SAFE * len(modes) * ULD * ULD),
    )

    # Show a deliberately simple candidate cap.  It is not promoted here.
    qcap_candidate = 12.0
    eround_candidate = (
        CDD_AUDIT_SAFE * len(modes) * ULD * ULD * qcap_candidate
    )
    sout_candidate = smin - esource - eround_candidate
    mu_candidate = max(0.0, sout_candidate) * sigma2

    row = {
        "sector": sector,
        "cutoff": CUTOFF,
        "dimension": len(modes),
        "graph_shear_tau_2norm": tau,
        "graph_shear_singular_values": [float(x) for x in svals],
        "cg_iters": iters,
        "recomputed_graph_residual_max_binary": max(residuals),
        "protected_S_min_arch200_ldd_midpoint": smin,
        "complement_gamma_fixed_fft_midpoint": gamma,
        "P_gram_min": float(gevals[0]),
        "P_gram_max": float(gevals[-1]),
        "W_frobenius_squared": wfrob2,
        "shear_sigma_min_lower_formula": sigma_shear,
        "shear_sigma_min_squared": sigma2,
        "mu_midpoint_congruence_candidate": mu_mid,
        "target_mu": TARGET_MU,
        "headroom_mu_over_target": mu_mid / TARGET_MU,
        "tau_max_allowed_if_S_midpoint_exact": tau_max,
        "tau_headroom_factor": tau_max / tau if tau > 0 else None,
        "Q_component_max_midpoint": qmax,
        "Q_component_matrix_midpoint": qmat.tolist(),
        "component_row_sum_max_midpoint": rowmax,
        "CDD_audit_safe": CDD_AUDIT_SAFE,
        "Qcap_max_rounding_only_for_target": qcap_max_rounding_only,
        "Qcap_candidate": qcap_candidate,
        "source_operator_radius_from_32k_scalar_caps": eop,
        "source_form_radius_candidate": esource,
        "DD_rounding_radius_candidate": eround_candidate,
        "protected_lower_candidate_before_residual": sout_candidate,
        "mu_candidate_before_residual_and_outward_shear": mu_candidate,
        "candidate_headroom_over_target": mu_candidate / TARGET_MU,
        "guardrail": (
            "Diagnostic only. Qcomp is midpoint positive-component magnitude. "
            "Candidate Qcap=12 and C_DD=8192 are stress-test values, not yet theorem."
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
