#!/usr/bin/env python3
"""Diagnostic for the v13.991 projective bordered matrices on v13.988 data.

This uses the already-landed corrected six-dimensional arbitrary-carrier
payload.  It does *not* claim that the nominal source energies are certified;
v13.987 explicitly showed they are not.  The purpose is only to test whether
augmenting the nearly singular reduced matrices by the source/observable rows
removes the tiny singular directions.

For each parity:
    M = [[H_C, K_eff^T],
         [K_eff, J_eff]]
and
    f = [f_C, s_eff].

The parity source energy has nominal bordered matrix
    B_p = [[M_p, f_p],
           [-f_p^T, h_reg,p]].

For the combined deficiency-overlap observables,
    F(-i)=G_e+G_o,
    F(+i)=G_e-G_o,
so with M=diag(M_e,M_o), rhs=(f_e,f_o),
the 13x13 borders use rows
    g_-=(f_e,f_o), d_-=h_e+h_o,
    g_+=(f_e,-f_o), d_+=h_e-h_o.

If their smallest singular values remain at machine-epsilon scale, the direct
v13.991 "whole-border sigma_min" criterion does not close.  That would mean
the determinant ratio still contains several common near-null factors that
must be factored projectively rather than certified separately.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
KKT = HERE / "p4_payload_kkt"
CROSS = HERE / "p4_payload_kkt_residual_cross"
OUT = HERE / "projective_border_diagnostic_result.json"


def sector_data(sector: str):
    manifest = json.loads((KKT / sector / "manifest.json").read_text())
    H = np.load(KKT / sector / "HChat.npy")
    f0 = np.load(KKT / sector / "f6_hat.npy")
    K = np.load(CROSS / sector / "K_eff.npy")
    J = np.load(CROSS / sector / "J_eff.npy")
    s = np.load(CROSS / sector / "s_eff.npy")

    J = (J + J.T) / 2.0
    H = (H + H.T) / 2.0
    M = np.block([[H, K.T], [K, J]])
    f = np.concatenate([f0[:2], s])
    h = float(manifest["h_reg_hat"])

    Benergy = np.block(
        [[M, f[:, None]], [-f[None, :], np.array([[h]])]]
    )

    return {
        "M": M,
        "f": f,
        "h": h,
        "M_singular_values": np.linalg.svd(M, compute_uv=False),
        "energy_border_singular_values": np.linalg.svd(
            Benergy, compute_uv=False
        ),
    }


def mp_matrix(A):
    return mp.matrix(
        [[mp.mpf(repr(float(x))) for x in row] for row in np.asarray(A)]
    )


def main():
    even = sector_data("even-v")
    odd = sector_data("odd-v")

    M = np.block(
        [
            [even["M"], np.zeros((6, 6))],
            [np.zeros((6, 6)), odd["M"]],
        ]
    )
    rhs = np.concatenate([even["f"], odd["f"]])

    g_minus = np.concatenate([even["f"], odd["f"]])
    g_plus = np.concatenate([even["f"], -odd["f"]])
    d_minus = even["h"] + odd["h"]
    d_plus = even["h"] - odd["h"]

    def border(g, d):
        return np.block(
            [[M, rhs[:, None]], [-g[None, :], np.array([[d]])]]
        )

    Bminus = border(g_minus, d_minus)
    Bplus = border(g_plus, d_plus)

    # Shared top block of both borders.
    C = np.column_stack([M, rhs])

    sv_minus = np.linalg.svd(Bminus, compute_uv=False)
    sv_plus = np.linalg.svd(Bplus, compute_uv=False)
    sv_C = np.linalg.svd(C, compute_uv=False)

    mp.mp.dps = 100
    det_minus = mp.det(mp_matrix(Bminus))
    det_plus = mp.det(mp_matrix(Bplus))
    nominal_ratio = det_plus / det_minus

    result = {
        "even": {
            "M_singular_values": [
                float(x) for x in even["M_singular_values"]
            ],
            "energy_border_singular_values": [
                float(x) for x in even["energy_border_singular_values"]
            ],
        },
        "odd": {
            "M_singular_values": [
                float(x) for x in odd["M_singular_values"]
            ],
            "energy_border_singular_values": [
                float(x) for x in odd["energy_border_singular_values"]
            ],
        },
        "combined": {
            "B_minus_singular_values": [float(x) for x in sv_minus],
            "B_plus_singular_values": [float(x) for x in sv_plus],
            "shared_source_matrix_singular_values": [float(x) for x in sv_C],
            "B_minus_sigma_min": float(sv_minus[-1]),
            "B_plus_sigma_min": float(sv_plus[-1]),
            "shared_source_sigma_min_nonzero": float(sv_C[-1]),
            "nominal_det_ratio_Fplus_over_Fminus": mp.nstr(
                nominal_ratio, 50
            ),
            "guardrail": (
                "Nominal ratio is diagnostic only and may be nonphysical; "
                "v13.987 forbids promotion of these source energies."
            ),
        },
    }

    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    print("v13.991 projective border diagnostic on v13.988 payload")
    for label, row in (("even", even), ("odd", odd)):
        print("\n", label)
        print("M singular values =", row["M_singular_values"])
        print(
            "energy border singular values =",
            row["energy_border_singular_values"],
        )

    print("\ncombined")
    print("B(-i) sigma_min =", sv_minus[-1])
    print("B(+i) sigma_min =", sv_plus[-1])
    print("shared [M f] singular values =", sv_C)
    print("nominal det ratio F(+i)/F(-i) =", mp.nstr(nominal_ratio, 50))
    print("\nwrote", OUT)
    print(
        "GUARDRAIL: conditioning diagnostic only. No kappa, Xi, RH/GRH, "
        "source-energy, or finite-to-infinite claim."
    )


if __name__ == "__main__":
    main()
