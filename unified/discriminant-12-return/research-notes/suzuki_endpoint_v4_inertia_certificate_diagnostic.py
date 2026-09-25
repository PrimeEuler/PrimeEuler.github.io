#!/usr/bin/env python3
"""Endpoint-pencil / V4 class-average certification diagnostic for Lane A.

For the bulk-subtracted resonance problem define

    B = B_sm = D_log - H,
    F_s(rho) = A + s*rho*B,       s in {-1,+1}.

The resonance count in |1+mu(K)|<rho is obtained from the inertia difference
of F_-(rho) and F_+(rho), once infinite-tail truncation is certified.

This script checks three pieces needed by that certificate:

1. analytic remote-tail lower bounds for F_-(rho), including the corrected
   negative odd-v pole rank-one cost;
2. finite endpoint inertias with and without eliminating the four U(12)
   unit-core class-average directions;
3. whether that four-class elimination reduces coupling to a later finite
   band (it need not).

It also records the exact off-diagonal identity showing that endpoint shifts
preserve the source-faithful rank-two Cauchy form:

    Z_n -> Z_n + s*rho*pi/2.

Finite-section outputs are diagnostics; analytic tail formulas use the
validated full prime bound ||B_prime||<2.05 and the audited cusp/arch
localization majorants.
"""
from __future__ import annotations

import argparse
import math

import mpmath as mp
import numpy as np

from suzuki_form_core_bulk_subtracted_resonance import (
    parity_components,
    smooth_bulk,
)
from suzuki_form_core_v4_unit_core_resonance_diagnostic import unit_core_mod12


PRIME_BOUND = 2.05


def s2(N):
    N = float(N)
    return N**-2 + 1.0/(2.0*N)


def cusp_tail_bound(N):
    pi = math.pi
    c = 2/pi**3 + 6/pi**4
    alpha = 2*c/pi
    Cdiag = 2/pi**2 + 2/pi**3 + 2/pi**4 + 6/pi**5

    rank1 = 2/pi**2 * s2(N)
    off = 2*alpha*math.sqrt(
        pi**2/12 * (N**-6 + 1.0/(10*N**5))
    )
    diag = Cdiag*math.sqrt(N**-4 + 1.0/(6*N**3))
    return rank1 + off + diag


def arch_tail_bound(N):
    pi = math.pi
    q = 2/pi
    M4 = float(mp.zeta(3))*q**3/(4*(1-q)**3)
    Cr = 19/12 + 4*M4
    return 4*Cr/pi**2 * s2(N)


def odd_pole_tail_bound(N):
    """Norm bound for the corrected odd-v term -2 d d^T on n>=N."""
    return (
        32*math.sinh(0.5)**2/math.pi**2
        * s2(N)
    )


def endpoint_tail_floor(N, rho, sector):
    """Analytic lower bound for A-rho*B_sm on a parity tail n>=N."""
    base = (
        (1-rho)*(math.log(N/4)-math.pi/2)
        - PRIME_BOUND
        - cusp_tail_bound(N)
        - arch_tail_bound(N)
    )
    if sector == "odd-v":
        base -= odd_pole_tail_bound(N)
    return base


def first_positive_tail_start(rho, sector, start=5, stop=100000):
    for N in range(start, stop+1):
        if endpoint_tail_floor(N, rho, sector) > 0:
            return N
    raise RuntimeError("no positive tail start found")


def np_matrix(M):
    return np.array(
        [[float(M[i, j]) for j in range(M.cols)] for i in range(M.rows)],
        dtype=float,
    )


def class_average_basis(ns):
    labels = np.array([unit_core_mod12(n) for n in ns], dtype=int)
    U = np.zeros((len(ns), 4), dtype=float)
    for j, r in enumerate((1, 5, 7, 11)):
        idx = np.where(labels == r)[0]
        U[idx, j] = 1.0/np.sqrt(len(idx))
    return U, labels


def orthogonal_complement(U):
    Q, _ = np.linalg.qr(U, mode="complete")
    return Q[:, U.shape[1]:]


def inertia(vals, tol=1e-10):
    vals = np.asarray(vals)
    return (
        int(np.sum(vals < -tol)),
        int(np.sum(np.abs(vals) <= tol)),
        int(np.sum(vals > tol)),
    )


def endpoint_class_schur(ns, A, B, rho, sign, core_dim=2):
    ns_tail = ns[core_dim:]
    F = A[core_dim:, core_dim:] + sign*rho*B[core_dim:, core_dim:]

    U, labels = class_average_basis(ns_tail)
    Q = orthogonal_complement(U)

    C = U.T@F@U
    K = Q.T@F@U
    D = Q.T@F@Q
    S = D - K@np.linalg.solve(C, K.T)
    S = (S + S.T)/2

    wF = np.linalg.eigvalsh((F+F.T)/2)
    wC = np.linalg.eigvalsh((C+C.T)/2)
    wS = np.linalg.eigvalsh(S)

    return {
        "class_counts": [int(np.sum(labels == r)) for r in (1,5,7,11)],
        "full_inertia": inertia(wF),
        "schur_inertia": inertia(wS),
        "class_min": float(wC[0]),
        "class_max": float(wC[-1]),
        "class_cross_norm": float(np.linalg.norm(K, 2)),
        "class_solve_amplification": float(np.linalg.norm(K,2)/wC[0]),
        "full_minabs": float(np.min(np.abs(wF))),
        "schur_minabs": float(np.min(np.abs(wS))),
        "gap_improvement": float(np.min(np.abs(wS))/np.min(np.abs(wF))),
    }


def next_band_cross_test(ns, A, B, finite_cutoff, rho, sign, core_dim=2):
    """Compare Q-to-next-band cross before/after class-average elimination."""
    ns_tail = ns[core_dim:]
    F = A[core_dim:, core_dim:] + sign*rho*B[core_dim:, core_dim:]

    nf = sum(n <= finite_cutoff for n in ns_tail)
    if nf <= 4 or nf >= len(ns_tail):
        raise ValueError("finite cutoff must leave both a class block and next band")

    ns_f = ns_tail[:nf]
    U, _ = class_average_basis(ns_f)
    Q = orthogonal_complement(U)

    FF = F[:nf, :nf]
    FR = F[:nf, nf:]
    RR = F[nf:, nf:]

    C = U.T@FF@U
    Kq = Q.T@FF@U
    Kr = FR.T@U
    QR = Q.T@FR

    QR_eff = QR - Kq@np.linalg.solve(C, Kr.T)
    RR_eff = RR - Kr@np.linalg.solve(C, Kr.T)
    RR_eff = (RR_eff + RR_eff.T)/2

    before = float(np.linalg.norm(QR, 2))
    after = float(np.linalg.norm(QR_eff, 2))

    return {
        "finite_dim": nf,
        "band_dim": len(ns_tail)-nf,
        "cross_before": before,
        "cross_after": after,
        "cross_ratio": after/before,
        "class_to_band_norm": float(np.linalg.norm(Kr,2)),
        "band_min_before": float(np.linalg.eigvalsh((RR+RR.T)/2)[0]),
        "band_min_after": float(np.linalg.eigvalsh(RR_eff)[0]),
    }


def cauchy_endpoint_shift_identity(rho, sign):
    """Constant added to source-faithful Z_n in F_s=A+s*rho*B_sm."""
    return sign*rho*math.pi/2


def report(max_mode=256, finite_cross_cutoff=192, dps=45):
    print("Lane A endpoint-pencil / V4 class-average diagnostic")
    print("max_mode=", max_mode, "finite_cross_cutoff=", finite_cross_cutoff)
    print("dps=", dps)

    print("\nAnalytic endpoint-tail starts")
    for rho in (0.02, 0.10):
        for sector in ("even-v", "odd-v"):
            N0 = first_positive_tail_start(rho, sector)
            print(
                "rho=", rho,
                sector,
                "first_positive_N=", N0,
                "floor=", endpoint_tail_floor(N0, rho, sector),
            )

    for N in (193, 257, 301, 401):
        print(
            "rho=.10 tail floor N=", N,
            "even=", endpoint_tail_floor(N, 0.10, "even-v"),
            "odd=", endpoint_tail_floor(N, 0.10, "odd-v"),
        )

    print("\nExact Cauchy generator shifts")
    for rho in (0.02, 0.10):
        print(
            "rho=", rho,
            "A-rho B: delta_Z=", cauchy_endpoint_shift_identity(rho, -1),
            "A+rho B: delta_Z=", cauchy_endpoint_shift_identity(rho, +1),
        )

    with mp.workdps(dps):
        for sector in ("even-v", "odd-v"):
            ns, A_mp = parity_components(max_mode, sector)
            B_mp = smooth_bulk(ns)
            A = np_matrix(A_mp)
            B = np_matrix(B_mp)

            print("\nSECTOR", sector)
            for rho in (0.02, 0.10):
                for sign, name in ((-1, "minus"), (+1, "plus")):
                    row = endpoint_class_schur(ns, A, B, rho, sign)
                    print(
                        "rho=", rho, name,
                        "full_inertia=", row["full_inertia"],
                        "schur_inertia=", row["schur_inertia"],
                        "Cmin=", row["class_min"],
                        "K/Cmin=", row["class_solve_amplification"],
                        "full_minabs=", row["full_minabs"],
                        "schur_minabs=", row["schur_minabs"],
                        "gap_ratio=", row["gap_improvement"],
                    )

                    if finite_cross_cutoff < max_mode:
                        cross = next_band_cross_test(
                            ns, A, B, finite_cross_cutoff, rho, sign
                        )
                        print(
                            "  band cross:",
                            "before=", cross["cross_before"],
                            "after=", cross["cross_after"],
                            "ratio=", cross["cross_ratio"],
                            "band_min_before=", cross["band_min_before"],
                            "band_min_after=", cross["band_min_after"],
                        )

    print(
        "\nGuardrail: class-average elimination is a finite conditioning/"
        "low-rank device. It is not an exact V4 symmetry and, if the band "
        "cross ratio is not <1 by a meaningful margin, it is not a "
        "remote-tail decoupling mechanism."
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-mode", type=int, default=256)
    parser.add_argument("--finite-cross-cutoff", type=int, default=192)
    parser.add_argument("--dps", type=int, default=45)
    args = parser.parse_args()
    report(
        max_mode=args.max_mode,
        finite_cross_cutoff=args.finite_cross_cutoff,
        dps=args.dps,
    )


if __name__ == "__main__":
    main()
