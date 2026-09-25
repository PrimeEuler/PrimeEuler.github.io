#!/usr/bin/env python3
"""Anisotropic finite-to-next-band test for Lane A endpoint pencils.

This diagnostic decides whether a compact remote interface can plausibly close
the endpoint inertia certificate using the analytic scalar tail floor.

For a finite block F and later band R, let S_F be the endpoint finite block
(after optional four-class unit-core Schur elimination).  Let W_+ span the
positive eigenspace of S_F.  If G is the coupling to R, define

    delta_crit_band
      = || Lambda_+^{-1/2} W_+^T G ||_2^2.

This is the normalized residual-Gram cost from this band alone.  Additional
orthogonal remote bands add positive semidefinite Gram contributions.

Hence, if delta_crit_band already exceeds the available analytic scalar tail
floor gamma, the corresponding scalar-floor Feshbach architecture cannot close
at that interface without stronger matrix-valued tail information.

The script is a midpoint diagnostic, not an interval certificate.
"""
from __future__ import annotations

import argparse

import mpmath as mp
import numpy as np

from suzuki_endpoint_v4_inertia_certificate_diagnostic import (
    endpoint_tail_floor,
    class_average_basis,
    orthogonal_complement,
    np_matrix,
)
from suzuki_form_core_bulk_subtracted_resonance import (
    parity_components,
    smooth_bulk,
)


def positive_residual_threshold(S, G, tol=1e-10):
    vals, Q = np.linalg.eigh((S+S.T)/2)
    mask = vals > tol
    if not np.any(mask):
        return 0.0, float("nan"), np.array([])
    lam = vals[mask]
    W = Q[:, mask]
    M = (W.T@G)/np.sqrt(lam)[:, None]
    sv = np.linalg.svd(M, compute_uv=False)
    return float(sv[0]**2), float(lam[0]), sv


def class_eliminate(FF, G, RR, finite_ns):
    U, _ = class_average_basis(finite_ns)
    Q = orthogonal_complement(U)

    C = U.T@FF@U
    Kq = Q.T@FF@U
    Kr = G.T@U

    S = Q.T@FF@Q - Kq@np.linalg.solve(C, Kq.T)
    Geff = Q.T@G - Kq@np.linalg.solve(C, Kr.T)
    Reff = RR - Kr@np.linalg.solve(C, Kr.T)

    return (S+S.T)/2, Geff, (Reff+Reff.T)/2


def one_case(
    sector,
    finite_cutoff,
    max_mode,
    rho=0.10,
    dps=35,
    core_dim=2,
):
    with mp.workdps(dps):
        ns, _cusp, _prime, _arch, _pole, A_mp = parity_components(max_mode, sector)
        B_mp = smooth_bulk(ns)

    A = np_matrix(A_mp)
    B = np_matrix(B_mp)

    tail_ns = ns[core_dim:]
    nf = sum(n <= finite_cutoff for n in tail_ns)
    if nf <= 4 or nf >= len(tail_ns):
        raise ValueError("max_mode must extend beyond finite_cutoff")

    F = A[core_dim:, core_dim:] - rho*B[core_dim:, core_dim:]
    FF = F[:nf, :nf]
    G = F[:nf, nf:]
    RR = F[nf:, nf:]

    raw_crit, raw_pos_min, raw_sv = positive_residual_threshold(FF, G)

    S, Geff, Reff = class_eliminate(
        FF,
        G,
        RR,
        tail_ns[:nf],
    )
    v4_crit, v4_pos_min, v4_sv = positive_residual_threshold(S, Geff)

    remote_start = finite_cutoff + 1
    gamma = endpoint_tail_floor(remote_start, rho, sector)

    return {
        "sector": sector,
        "finite_cutoff": finite_cutoff,
        "max_mode": max_mode,
        "finite_dim": nf,
        "band_dim": len(tail_ns)-nf,
        "analytic_tail_floor": gamma,
        "raw_delta_crit_band": raw_crit,
        "v4_delta_crit_band": v4_crit,
        "raw_ratio_to_floor": raw_crit/gamma,
        "v4_ratio_to_floor": v4_crit/gamma,
        "raw_positive_min": raw_pos_min,
        "v4_positive_min": v4_pos_min,
        "raw_sv": raw_sv[:6],
        "v4_sv": v4_sv[:6],
        "band_min": float(np.linalg.eigvalsh((RR+RR.T)/2)[0]),
        "band_min_after_v4": float(np.linalg.eigvalsh(Reff)[0]),
    }


def report(dps=35):
    cases = [
        ("even-v", 256, 384, 0.10),
        ("odd-v", 256, 384, 0.10),
        ("even-v", 400, 1024, 0.10),
    ]

    print("Lane A anisotropic endpoint-interface diagnostic")
    for sector, cutoff, max_mode, rho in cases:
        row = one_case(
            sector,
            cutoff,
            max_mode,
            rho=rho,
            dps=dps,
        )
        print("\n", sector, "finite<=", cutoff, "band<=", max_mode)
        print("analytic tail floor =", row["analytic_tail_floor"])
        print("raw delta_crit_band =", row["raw_delta_crit_band"])
        print("V4 delta_crit_band =", row["v4_delta_crit_band"])
        print("raw ratio/floor =", row["raw_ratio_to_floor"])
        print("V4 ratio/floor =", row["v4_ratio_to_floor"])
        print("raw positive min =", row["raw_positive_min"])
        print("V4 positive min =", row["v4_positive_min"])
        print("V4 leading singular values =", row["v4_sv"])
        print("band min =", row["band_min"])
        print("band min after V4 =", row["band_min_after_v4"])

    print(
        "\nGuardrail: this is a finite-band midpoint obstruction/viability "
        "diagnostic. A ratio below one does not certify the full infinite tail; "
        "a ratio above one shows that this scalar-floor architecture is already "
        "insufficient on the tested band."
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=35)
    parser.add_argument("--sector", choices=("even-v","odd-v"))
    parser.add_argument("--finite-cutoff", type=int)
    parser.add_argument("--max-mode", type=int)
    parser.add_argument("--rho", type=float, default=0.10)
    args = parser.parse_args()

    if args.sector:
        if args.finite_cutoff is None or args.max_mode is None:
            raise SystemExit(
                "--sector requires --finite-cutoff and --max-mode"
            )
        print(
            one_case(
                args.sector,
                args.finite_cutoff,
                args.max_mode,
                rho=args.rho,
                dps=args.dps,
            )
        )
    else:
        report(dps=args.dps)


if __name__ == "__main__":
    main()
