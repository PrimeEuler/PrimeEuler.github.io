#!/usr/bin/env python3
"""Evaluate the certified numerical grouped residue over |delta| <= 0.02.

The residual-certified numerical four-space Qhat is reconstructed by the
v13.824 algorithm (independently replayed by External Audit Round 108).

Because Qhat is B_T-orthonormal, with
    Y = B_T^{1/2} Qhat
and
    Phat4 = Y Y^*,
the numerical grouped residue is exactly

    Ghat(delta)
      = C(delta)^* Phat4 C(delta)
      = K(delta)^T K(delta),

where
    K(delta) = Qhat^T F_TC(delta)
             = K0 - delta K1.

Hence Ghat is a 2x2 quadratic matrix polynomial.  This script evaluates its
coefficients, endpoint matrices, exact scalar-entry quadratic extrema, and a
uniform Loewner cap.  No interval grid is used for certification.

The exact grouped residue G=C^*P4C is handled separately by the v13.826
projector-error enclosure.
"""
from __future__ import annotations

import math
import numpy as np

from suzuki_tail_P4_residual_basis_certificate import (
    first_stage_ritz,
    graph_extend,
    second_stage_ritz,
)
from suzuki_grouped_residue_error_certificate import (
    layout,
    coupling_rows,
)


DELTA0 = 0.02
CENTER_REPLAY_RESERVE = 1.0e-10

LOEWNER_CAP = {
    "even-v": 1.75e-4,
    "odd-v": 1.00e-4,
}

# Widened entrywise enclosures for the numerical center.
ENTRY_CAPS = {
    "even-v": {
        (0,0): (2.0e-11, 1.109e-4),
        (0,1): (-3.0e-12, 8.402e-5),
        (1,1): (1.6e-10, 6.375e-5),
    },
    "odd-v": {
        (0,0): (5.5e-8, 5.447e-5),
        (0,1): (3.8e-8, 4.905e-5),
        (1,1): (2.1e-7, 4.434e-5),
    },
}

EXACT_GROUPED_ERROR_CAP = {
    "even-v": 0.0086,
    "odd-v": 0.0152,
}


def build_basis(sector):
    m1, theta1, q1, _ = first_stage_ritz(sector)
    modes, x = graph_extend(sector, m1, theta1, q1)
    theta, qhat, _az, _bz, _gfinite, defect = second_stage_ritz(
        sector, modes, x
    )
    if defect >= 1.0e-12:
        raise RuntimeError(("B-orthogonality defect", sector, defect))
    return modes, theta, qhat, defect


def polynomial_data(sector):
    modes, theta, qhat, defect = build_basis(sector)
    core, _ = layout(sector)

    a_tc = coupling_rows(
        sector,
        core,
        modes,
        0.0,
    )

    rows = modes.astype(float)
    cc = core.astype(float)
    b_tc = -1.0 / (rows[:,None] + cc[None,:])

    k0 = qhat.T @ a_tc
    k1 = qhat.T @ b_tc

    g0 = k0.T @ k0
    g1 = k0.T @ k1 + k1.T @ k0
    g2 = k1.T @ k1

    return {
        "modes": modes,
        "theta": theta,
        "qhat": qhat,
        "defect": defect,
        "k0": k0,
        "k1": k1,
        "g0": g0,
        "g1": g1,
        "g2": g2,
    }


def g_of(data, delta):
    return (
        data["g0"]
        - delta * data["g1"]
        + delta * delta * data["g2"]
    )


def k_direct(data, delta):
    return data["k0"] - delta * data["k1"]


def scalar_quadratic_extrema(a, b, c):
    vals = [
        a + DELTA0*b + DELTA0*DELTA0*c,  # delta=-DELTA0
        a - DELTA0*b + DELTA0*DELTA0*c,  # delta=+DELTA0
    ]

    if c != 0.0:
        dstar = b/(2.0*c)
        if -DELTA0 <= dstar <= DELTA0:
            vals.append(a - dstar*b + dstar*dstar*c)

    return min(vals), max(vals)


def certify_sector(sector):
    data = polynomial_data(sector)

    endpoints = {}
    for delta in (-DELTA0, 0.0, +DELTA0):
        gp = g_of(data, delta)
        kd = k_direct(data, delta)
        gd = kd.T @ kd
        replay = np.linalg.norm(gp-gd, 2)
        if replay >= CENTER_REPLAY_RESERVE:
            raise RuntimeError(("polynomial/direct replay", sector, delta, replay))

        ev = np.linalg.eigvalsh((gp+gp.T)/2.0)
        if ev[0] < -CENTER_REPLAY_RESERVE:
            raise RuntimeError(("numerical grouped residue PSD failure", sector, delta, ev))

        endpoints[delta] = {
            "matrix": gp,
            "eigenvalues": ev,
            "operator_norm": float(ev[-1]),
            "replay_defect": float(replay),
        }

    # Convexity of ||K0-delta K1|| implies the maximum operator norm of
    # Ghat=K^T K occurs at an interval endpoint.
    endpoint_max = max(
        endpoints[-DELTA0]["operator_norm"],
        endpoints[+DELTA0]["operator_norm"],
    )
    if endpoint_max >= LOEWNER_CAP[sector]:
        raise RuntimeError(("uniform Loewner cap", sector, endpoint_max))

    entry_extrema = {}
    for i,j in ((0,0),(0,1),(1,1)):
        lo, hi = scalar_quadratic_extrema(
            data["g0"][i,j],
            data["g1"][i,j],
            data["g2"][i,j],
        )
        publo, pubhi = ENTRY_CAPS[sector][(i,j)]
        if not (lo > publo and hi < pubhi):
            raise RuntimeError(
                ("entry cap failed", sector, (i,j), lo, hi, publo, pubhi)
            )
        entry_extrema[(i,j)] = (lo,hi)

    # Combining the numerical-center Loewner cap with v13.826 gives a
    # simple exact-residue upper enclosure as a corollary.
    exact_upper = (
        LOEWNER_CAP[sector]
        + EXACT_GROUPED_ERROR_CAP[sector]
    )

    return {
        "sector": sector,
        "theta": data["theta"],
        "B_orthogonality_defect": data["defect"],
        "K0": data["k0"],
        "K1": data["k1"],
        "G0": data["g0"],
        "G1": data["g1"],
        "G2": data["g2"],
        "endpoints": endpoints,
        "entry_extrema": entry_extrema,
        "uniform_loewner_cap": LOEWNER_CAP[sector],
        "exact_grouped_upper_corollary": exact_upper,
    }


def main():
    rows = [
        certify_sector("even-v"),
        certify_sector("odd-v"),
    ]

    for row in rows:
        print("\nsector =", row["sector"])
        print("Ritz values =", row["theta"])
        print("B-orthogonality defect =", row["B_orthogonality_defect"])
        print("K0 =\n", row["K0"])
        print("K1 =\n", row["K1"])
        print("G0 =\n", row["G0"])
        print("G1 =\n", row["G1"])
        print("G2 =\n", row["G2"])

        for delta in (-DELTA0, 0.0, +DELTA0):
            ep = row["endpoints"][delta]
            print("\ndelta =", delta)
            print("Ghat =\n", ep["matrix"])
            print("eigenvalues =", ep["eigenvalues"])
            print("operator norm =", ep["operator_norm"])
            print("poly/direct defect =", ep["replay_defect"])

        print("\nentry extrema =", row["entry_extrema"])
        print("uniform Loewner cap =", row["uniform_loewner_cap"])
        print(
            "exact grouped upper corollary =",
            row["exact_grouped_upper_corollary"],
        )

    print("\nPASS numerical grouped-residue polynomial/enclosure")
    print(
        "For each sector, 0 <= Ghat(delta) <= M I_2 uniformly on "
        "|delta|<=0.02, with M equal to the reported public Loewner cap."
    )


if __name__ == "__main__":
    main()
