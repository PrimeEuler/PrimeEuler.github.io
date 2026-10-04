#!/usr/bin/env python3
"""Residual-weighted variational source-energy gate on the corrected v13.988 payload.

For a positive source operator T and any trial vector x,

    G = <f,T^{-1}f>,
    J(x) = 2<f,x> - <x,Tx>,
    G - J(x) = <r,T^{-1}r>,  r=f-Tx.

If r lies in the certified complement and ||T_Q^{-1}|| <= M, then

    0 <= G-J(x) <= M ||r||^2.

This looks attractive because it avoids a global inverse perturbation theorem.
However, the corrected arbitrary-carrier trial is a linear combination of
seven approximate complement inverse actions.  Its residual is therefore
weighted by the reduced coefficients w.  Near singularity can amplify those
weights enormously.

This script forms the corrected nominal v13.988 6D system and reports the
conservative transformed residual combination

    e_trial <= e_f
               + |w_C1| e_C1 + |w_C2| e_C2
               + sum_j |w_Pj| e_Rj,

using the certified transformed residual totals from v13.987.

Diagnostic only: the nominal 6D solve is not certified and no source-energy
value is promoted.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
KKT = HERE / "p4_payload_kkt"
CROSS = HERE / "p4_payload_kkt_residual_cross"

M_CAP = {
    "even-v": 10.152566,
    "odd-v": 10.302509,
}

RESIDUALS = {
    "even-v": {
        "core": np.array([0.001143113659867295, 0.0033761214961490877]),
        "source": 6.345257042022136,
        "ritz": np.array([
            2.5579689820242703e-7,
            3.7638835995739965e-6,
            6.606183055064243e-4,
            4.068540511882385e-2,
        ]),
    },
    "odd-v": {
        "core": np.array([0.001978370588356106, 0.004014001687863045]),
        "source": 0.2651336618285081,
        "ritz": np.array([
            8.92664679238643e-8,
            7.96450660691399e-6,
            1.0027124437315032e-3,
            4.209243464768428e-2,
        ]),
    },
}


def one(sector: str):
    manifest = json.loads((KKT / sector / "manifest.json").read_text())
    H = np.load(KKT / sector / "HChat.npy")
    f0 = np.load(KKT / sector / "f6_hat.npy")
    K = np.load(CROSS / sector / "K_eff.npy")
    J = np.load(CROSS / sector / "J_eff.npy")
    s = np.load(CROSS / sector / "s_eff.npy")

    H = (H + H.T) / 2.0
    J = (J + J.T) / 2.0
    M6 = np.block([[H, K.T], [K, J]])
    f6 = np.concatenate([f0[:2], s])
    h = float(manifest["h_reg_hat"])

    sv = np.linalg.svd(M6, compute_uv=False)
    w = np.linalg.solve(M6, f6)
    nominal_energy = h + float(f6 @ w)

    rr = RESIDUALS[sector]
    pieces = {
        "source": float(rr["source"]),
        "core1": float(abs(w[0]) * rr["core"][0]),
        "core2": float(abs(w[1]) * rr["core"][1]),
    }
    for j in range(4):
        pieces[f"ritz{j+1}"] = float(abs(w[2+j]) * rr["ritz"][j])

    e_trial = float(sum(pieces.values()))
    energy_error_cap = float(M_CAP[sector] * e_trial * e_trial)

    return {
        "sector": sector,
        "singular_values": [float(x) for x in sv],
        "w": [float(x) for x in w],
        "max_abs_w": float(np.max(np.abs(w))),
        "nominal_energy_diagnostic": nominal_energy,
        "residual_contributions": pieces,
        "transformed_trial_residual_upper": e_trial,
        "complement_energy_error_upper_if_residual_is_complement": energy_error_cap,
        "error_over_abs_nominal_energy": (
            energy_error_cap / abs(nominal_energy)
            if nominal_energy != 0.0 else None
        ),
        "guardrail": (
            "Nominal solve/energy not certified. Error cap is conditional on "
            "the assembled trial residual lying in the certified complement."
        ),
    }


def main():
    rows = [one("even-v"), one("odd-v")]
    print("Residual-weighted variational source-energy diagnostic")
    for row in rows:
        print("\nsector =", row["sector"])
        print("sigma_min =", row["singular_values"][-1])
        print("max |w| =", row["max_abs_w"])
        print("w =", row["w"])
        print("nominal energy diagnostic =", row["nominal_energy_diagnostic"])
        print("residual contributions =", row["residual_contributions"])
        print("trial residual upper =", row["transformed_trial_residual_upper"])
        print(
            "conditional complement energy-error upper =",
            row["complement_energy_error_upper_if_residual_is_complement"],
        )
        print(
            "error / |nominal energy| =",
            row["error_over_abs_nominal_energy"],
        )

    print(
        "\nGUARDRAIL: this gate tests whether residual variational certification "
        "can survive coefficient amplification; it promotes no nominal energy."
    )


if __name__ == "__main__":
    main()
