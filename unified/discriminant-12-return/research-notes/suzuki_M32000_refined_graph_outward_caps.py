#!/usr/bin/env python3
"""Outward-cap closure replay for the M=32000 finite-section floor.

Purpose
-------
Close the three cap-tightness items left by v14.084-v14.087:

  1. recompute the six graph columns, perform the accepted one-step LDDD
     refinement, and bound the exact graph shear from the refined trial;
  2. recompute the positive pre-cancellation Qcomp on the refined graph and
     inflate it to the exact graph using the theorem complement floor;
  3. publish the transparent LDDD primitive-chain constant
         C_DD = 16 * 64 * 8 = 8192.

No finite-floor theorem is promoted by this producer alone.  It fails closed
unless the outward shear caps tau_e<=0.04, tau_o<=0.11 and Qcomp<=12 survive.

The graph correction uses only theorem inputs:
  * v14.029/v14.031 shifted M8000 complement floors delta_p;
  * v14.071 nested remote coercivity S_{p,8000} >= I;
  * v14.085 analytic cross-block cap ||B||<=40;
  * public per-column exact residual cap 2e-25.

For the refined represented graph W~, if C is the exact frozen-P complement,
the exact graph differs by DeltaY=C^{-1}R.  Hence
  ||DeltaY||_F <= sqrt(6) r_col / gamma_32.
This controls both the exact shear and the change in Qcomp.

For Hcomp, the positive component matrix, the same scalar-to-operator radius
used in v14.084 bounds the exact-source perturbation because
| |x|-|y| | <= |x-y| entrywise.  Since Hcomp is symmetric and entrywise
nonnegative, ||Hcomp||_2 <= max row sum.

The numerical pads below are deliberately huge relative to ordinary
binary64 positive-summation error (all Qcomp contractions are positive):
1e-8 on norms and 1e-8 absolute on Qcomp.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import cg

from suzuki_fixed_fft_stationary_feshbach import base_payload
from suzuki_full_fft_fixed_capacity_replay import fixed_operator, DPS, ARCH
from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import (
    embedded_P, modes_for,
)
from suzuki_ldd_refined_capacity_bracket import (
    dd_project, mp_inverse_split, solve_correction,
)
from suzuki_ldd_source_operator import (
    LD,
    add as dd_add,
    dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,
    matvec as dd_matvec,
    norm2 as dd_norm2,
    sub as dd_sub,
)
from suzuki_M32000_fixed_fft_graph_shear import (
    component_qcomp, source_operator_radius,
)

HERE = Path(__file__).resolve().parent
OUT = HERE / "M32000_refined_graph_outward_caps_result.json"

CUTOFF = 32000
NCOLS = 6
RCOL_CAP = 2.0e-25
B_CROSS_CAP = 40.0
TAU_CAP = {"even-v": 0.04, "odd-v": 0.11}
QCOMP_CAP = 12.0
NORM_NUMERIC_PAD = 1.0e-8
QCOMP_NUMERIC_PAD = 1.0e-8

DELTA8 = {
    "even-v": 7.795385618610192746e-6,
    "odd-v": 3.262507025086259604e-5,
}

# Transparent primitive-chain count:
# off-diagonal protected-form path uses fewer than 16 LDDD primitives from
# source entry construction through matvec and final protected dot.
PRIMITIVE_STAGE_CAP = 16
WORST_PRIMITIVE_U2 = 64
SAFETY_FACTOR = 8
CDD = PRIMITIVE_STAGE_CAP * WORST_PRIMITIVE_U2 * SAFETY_FACTOR


def shear_sigma2(tau: float) -> float:
    return (2.0 / (math.sqrt(tau * tau + 4.0) + tau)) ** 2


def complement_floor(sector: str) -> float:
    d = DELTA8[sector]
    tau_q = B_CROSS_CAP / d
    return d * shear_sigma2(tau_q)


def graph_residual(data, P, Gih, Gil, Yh, Yl):
    Wh, Wl = dd_sub(P, np.zeros_like(P, dtype=LD), Yh, Yl)
    AWh, AWl = dd_matvec(data, Wh, Wl)
    Rh, Rl = dd_project(P, Gih, Gil, AWh, AWl)
    norms = [dd_norm2(Rh[:, j], Rl[:, j]) for j in range(NCOLS)]
    return Wh, Wl, Rh, Rl, norms


def one(sector: str):
    modes = modes_for(sector, CUTOFF)
    P = embedded_P(sector, modes)
    base = base_payload(sector)

    Gh, Gl = dd_dot_columns(P, None, P, None)
    Gih, Gil, Gi_mp = mp_inverse_split(Gh, Gl, DPS)
    Gi = np.array([[float(Gi_mp[i, j]) for j in range(6)] for i in range(6)])

    raw_mv, proj, op, _ = fixed_operator(modes, sector, P, Gi)
    AP = np.asarray(raw_mv(P), dtype=float)
    E = proj(AP)

    Y0 = np.empty_like(E)
    initial_res = []
    iters = []
    for j in range(NCOLS):
        cnt = [0]
        y, info = cg(
            op, E[:, j], rtol=2e-14, atol=0.0, maxiter=30000,
            callback=lambda _: cnt.__setitem__(0, cnt[0] + 1),
        )
        if info != 0:
            raise RuntimeError(("graph CG failed", sector, j, info))
        y = proj(y)
        Y0[:, j] = y
        initial_res.append(float(np.linalg.norm(E[:, j] - op @ y)))
        iters.append(cnt[0])

    data = hp_parity_data(
        modes, sector, dps=DPS, arch_terms=ARCH, correction_terms=50
    )
    Yh = Y0.astype(LD)
    Yl = np.zeros_like(Yh, dtype=LD)
    Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)

    Wh, Wl, Rh, Rl, r0 = graph_residual(data, P, Gih, Gil, Yh, Yl)

    # One accepted LDDD residual refinement, exactly as in the fixed-FFT
    # finite-data producer.
    for j in range(NCOLS):
        delta = solve_correction(op, proj, Rh[:, j] + Rl[:, j], rtol=2e-14)
        Yh[:, j], Yl[:, j] = dd_add(
            Yh[:, j], Yl[:, j], delta, np.zeros_like(delta, dtype=LD)
        )
    Yh, Yl = dd_project(P, Gih, Gil, Yh, Yl)

    Wh, Wl, Rh, Rl, r1 = graph_residual(data, P, Gih, Gil, Yh, Yl)

    Y = np.asarray(Yh + Yl, dtype=float)
    W = np.asarray(Wh + Wl, dtype=float)

    # Spectral shear is bounded by Frobenius norm.  Use a positive sum and
    # add a very loose public numerical pad.
    y_frob = float(np.sqrt(np.sum(Y * Y, dtype=np.longdouble)))
    w_frob = float(np.sqrt(np.sum(W * W, dtype=np.longdouble)))

    qmid, _, rowmax = component_qcomp(modes, sector, W)
    eop = source_operator_radius(sector, len(modes))
    gamma = complement_floor(sector)

    # Exact graph correction from six per-column residual caps.
    dY_frob = math.sqrt(NCOLS) * RCOL_CAP / gamma

    tau_out = y_frob + dY_frob + NORM_NUMERIC_PAD

    # Exact-source Hcomp perturbation uses the same source/operator radius.
    # For each 6x6 form entry:
    # |w_i^T H w_j - wt_i^T Hmid wt_j|
    # <= ||Hmid|| (2||Wt||_F||dW||_F + ||dW||_F^2)
    #    + ||dH|| (||Wt||_F+||dW||_F)^2.
    graph_infl = rowmax * (2.0 * w_frob * dY_frob + dY_frob * dY_frob)
    source_infl = eop * (w_frob + dY_frob) ** 2
    qout = qmid + graph_infl + source_infl + QCOMP_NUMERIC_PAD

    row = {
        "sector": sector,
        "cutoff": CUTOFF,
        "dimension": len(modes),
        "initial_cg_iters": iters,
        "initial_binary_residual_max": max(initial_res),
        "ldd_graph_residual_before_refine_max": max(r0),
        "ldd_graph_residual_after_refine_max": max(r1),
        "public_exact_residual_cap_per_column": RCOL_CAP,
        "complement_floor_theorem": gamma,
        "exact_graph_correction_frobenius_cap": dY_frob,
        "refined_Y_frobenius_mid": y_frob,
        "refined_W_frobenius_mid": w_frob,
        "numeric_norm_pad": NORM_NUMERIC_PAD,
        "graph_shear_tau_outward": tau_out,
        "graph_shear_public_cap": TAU_CAP[sector],
        "graph_shear_passes": tau_out < TAU_CAP[sector],
        "Qcomp_refined_mid": qmid,
        "Hcomp_mid_row_sum_max": rowmax,
        "source_operator_radius": eop,
        "Qcomp_graph_inflation": graph_infl,
        "Qcomp_source_inflation": source_infl,
        "Qcomp_numeric_pad": QCOMP_NUMERIC_PAD,
        "Qcomp_outward": qout,
        "Qcomp_public_cap": QCOMP_CAP,
        "Qcomp_passes": qout < QCOMP_CAP,
        "primitive_stage_cap": PRIMITIVE_STAGE_CAP,
        "worst_primitive_u2_constant": WORST_PRIMITIVE_U2,
        "explicit_safety_factor": SAFETY_FACTOR,
        "C_DD_transparent": CDD,
    }

    if max(r1) >= RCOL_CAP:
        raise RuntimeError(("refined represented residual exceeds public cap", row))
    if not row["graph_shear_passes"]:
        raise RuntimeError(("outward graph shear cap failed", row))
    if not row["Qcomp_passes"]:
        raise RuntimeError(("outward Qcomp cap failed", row))
    if CDD != 8192:
        raise RuntimeError(("C_DD arithmetic mismatch", CDD))

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
