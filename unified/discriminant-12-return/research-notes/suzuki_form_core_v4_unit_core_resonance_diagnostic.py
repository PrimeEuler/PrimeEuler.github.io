#!/usr/bin/env python3
"""V4 / unit-core diagnostic for the Lane A compact resonance problem.

This asks a deliberately narrow question after v13.801:

    Do the four numerically stable tail resonances realize the four U(12)
    characters, or can the U(12) unit-core classes still help only as a
    finite rank-4 Schur organization?

The script imports the corrected source-faithful parity matrices and
bulk-subtracted resonance basis from
suzuki_form_core_bulk_subtracted_resonance.py.

It tests:
  1. invariance of the four-resonance subspace under the three nontrivial
     diagonal character-sign operators on the unit-core label
         u(n)=n/(2^v2(n) 3^v3(n)) mod 12 in {1,5,7,11};
  2. overlap of the resonance subspace with the four normalized unit-core
     class-average directions;
  3. generalized class-average eigenvalues of (A,B_sm);
  4. commutators of A and B_sm with the character-sign operators;
  5. the Hadamard-character form of the finite class-average relative
     compression.

These are finite-section diagnostics.  They do not assert an exact V4
symmetry, an infinite-dimensional class-average projector, or a relation
between the cone U(24) double cover and the Suzuki even strata.
"""
from __future__ import annotations

import argparse
import numpy as np
from scipy.linalg import eigh

from suzuki_form_core_bulk_subtracted_resonance import (
    parity_components,
    resonance_basis,
    smooth_bulk,
)


H4 = np.array(
    [
        [1, 1, 1, 1],
        [1, 1, -1, -1],
        [1, -1, 1, -1],
        [1, -1, -1, 1],
    ],
    dtype=float,
) / 2.0

CHARACTERS = {
    "chi_-4": {1: 1, 5: 1, 7: -1, 11: -1},
    "chi_-3": {1: 1, 5: -1, 7: 1, 11: -1},
    "chi_12": {1: 1, 5: -1, 7: -1, 11: 1},
}


def unit_core_mod12(n: int) -> int:
    n = int(n)
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    r = n % 12
    if r not in (1, 5, 7, 11):
        raise ValueError((n, r))
    return r


def np_matrix(M):
    return np.array(
        [[float(M[i, j]) for j in range(M.cols)] for i in range(M.rows)],
        dtype=float,
    )


def class_average_basis(labels):
    classes = (1, 5, 7, 11)
    U = np.zeros((len(labels), 4), dtype=float)
    for j, r in enumerate(classes):
        idx = np.where(labels == r)[0]
        U[idx, j] = 1.0 / np.sqrt(len(idx))
    return U


def sector_report(sector: str, cutoff: int, dps: int, core_dim: int = 2):
    data = parity_components(cutoff, sector)
    ns_full, _, _, _, _, A_mp = data

    size = sum(n <= cutoff for n in ns_full)
    ns = ns_full[:size]
    tail_ns = ns[core_dim:]

    A = np_matrix(A_mp[:size, :size])[core_dim:, core_dim:]
    B = np_matrix(smooth_bulk(ns))[core_dim:, core_dim:]

    # resonance_basis returns a Euclidean-orthonormal basis for the coefficient-
    # space span of the four closest relative resonances.
    Q4 = resonance_basis(
        data,
        cutoff,
        howmany=4,
        core_dim=core_dim,
    )

    labels = np.array([unit_core_mod12(n) for n in tail_ns], dtype=int)
    U = class_average_basis(labels)

    overlap = U.T @ Q4
    svals = np.linalg.svd(overlap, compute_uv=False)
    trace_projection = float(np.sum(svals * svals))
    per_vector_projection = np.sum(overlap * overlap, axis=0)

    Ac = U.T @ A @ U
    Bc = U.T @ B @ U
    gen_eigs = eigh(Ac, Bc, eigvals_only=True)

    bvals, bvecs = eigh(Bc)
    Binvsqrt = bvecs @ np.diag(1.0 / np.sqrt(bvals)) @ bvecs.T
    Jc = Binvsqrt @ Ac @ Binvsqrt
    Jhat = H4 @ Jc @ H4.T
    off = Jhat - np.diag(np.diag(Jhat))

    char_rows = {}
    for name, table in CHARACTERS.items():
        d = np.array([table[int(r)] for r in labels], dtype=float)
        DQ = d[:, None] * Q4
        restricted = Q4.T @ DQ
        leakage = DQ - Q4 @ restricted

        comm_A = d[:, None] * A - A * d[None, :]
        comm_B = d[:, None] * B - B * d[None, :]

        char_rows[name] = {
            "resonance_leakage_norm": float(
                np.linalg.svd(leakage, compute_uv=False)[0]
            ),
            "comm_A_relative": float(
                np.linalg.norm(comm_A, 2) / np.linalg.norm(A, 2)
            ),
            "comm_B_relative": float(
                np.linalg.norm(comm_B, 2) / np.linalg.norm(B, 2)
            ),
        }

    return {
        "sector": sector,
        "cutoff": cutoff,
        "tail_modes": len(tail_ns),
        "class_counts": {
            r: int(np.sum(labels == r))
            for r in (1, 5, 7, 11)
        },
        "class_overlap_singular_values": svals,
        "class_projection_trace": trace_projection,
        "class_projection_fraction_of_4D": trace_projection / 4.0,
        "per_resonance_class_projection": per_vector_projection,
        "class_generalized_eigenvalues": gen_eigs,
        "class_B_min": float(np.min(bvals)),
        "hadamard_relative_offdiag_fro": float(
            np.linalg.norm(off, "fro") / np.linalg.norm(Jhat, "fro")
        ),
        "hadamard_max_offdiag": float(np.max(np.abs(off))),
        "character_tests": char_rows,
    }


def report(cutoff: int = 96, dps: int = 55):
    print("Lane A V4/unit-core resonance diagnostic")
    print("cutoff=", cutoff, "dps=", dps)
    for sector in ("even-v", "odd-v"):
        row = sector_report(sector, cutoff, dps)
        print("\n", sector)
        print("class_counts=", row["class_counts"])
        print(
            "class_overlap_singular_values=",
            [f"{x:.9g}" for x in row["class_overlap_singular_values"]],
        )
        print(
            "class_projection_fraction_of_4D=",
            f"{row['class_projection_fraction_of_4D']:.9g}",
        )
        print(
            "per_resonance_class_projection=",
            [f"{x:.9g}" for x in row["per_resonance_class_projection"]],
        )
        print(
            "class_generalized_eigenvalues=",
            [f"{x:.9g}" for x in row["class_generalized_eigenvalues"]],
        )
        print("class_B_min=", f"{row['class_B_min']:.9g}")
        print(
            "hadamard_relative_offdiag_fro=",
            f"{row['hadamard_relative_offdiag_fro']:.9g}",
        )
        print(
            "hadamard_max_offdiag=",
            f"{row['hadamard_max_offdiag']:.9g}",
        )
        for name, vals in row["character_tests"].items():
            print(
                name,
                "leak=",
                f"{vals['resonance_leakage_norm']:.9g}",
                "commArel=",
                f"{vals['comm_A_relative']:.9g}",
                "commBrel=",
                f"{vals['comm_B_relative']:.9g}",
            )

    print(
        "\nguardrail: character labels are a finite diagnostic/certificate "
        "organization here, not an exact symmetry theorem"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoff", type=int, default=96)
    parser.add_argument("--dps", type=int, default=55)
    args = parser.parse_args()
    report(cutoff=args.cutoff, dps=args.dps)


if __name__ == "__main__":
    main()
