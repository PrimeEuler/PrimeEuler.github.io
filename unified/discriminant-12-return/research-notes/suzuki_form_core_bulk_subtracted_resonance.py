#!/usr/bin/env python3
"""Bulk-subtracted resonance diagnostic for Lane A at a=1, lambda=0.

This implements the divisor/hyperbola-inspired renormalization gate after
v13.800.  The smooth asymptotic bulk is the source-faithful same-parity cusp
principal part isolated in v13.301:

    B_sm = D_log - H,
    (D_log)_{nn} = log(n/4),
    H_{mn} = 1/(m+n).

The full corrected parity form is written

    A = B_sm + V,

where V contains the exact prime-shift contribution, the compact cusp
correction, the smooth archimedean remainder, and the parity-correct pole term

    even-v: +2 c c^T,
    odd-v : -2 d d^T.

After removing the first two basis modes in each parity sector, B_sm is
positive on every finite tail tested here.  The normalized tail interaction

    T = B_tt^{-1/2} V_tt B_tt^{-1/2}

turns small raw Ritz values into distances from the resonance value -1.
The script also tracks principal angles of the closest-to--1 resonance
subspaces and the source-resolvent Feshbach decomposition.

Outputs are finite-section diagnostics, not an infinite-cutoff theorem and
not a promotion of kappa1.
"""
from __future__ import annotations

import argparse

import mpmath as mp
import numpy as np

QS = (2, 3, 4, 5, 7)


def weights():
    return (
        mp.log(2) / mp.sqrt(2),
        mp.log(3) / mp.sqrt(3),
        mp.log(2) / 2,
        mp.log(5) / mp.sqrt(5),
        mp.log(7) / mp.sqrt(7),
    )


def h_arch(t):
    t = mp.mpf(t)
    if t == 0:
        return mp.mpf(1) / 4
    return mp.exp(-t / 2) / (1 - mp.exp(-2 * t)) - 1 / (2 * t)


def source_overlap(n):
    k = mp.mpf(n) * mp.pi / 2
    sign = -1 if n % 2 else 1
    return k * (mp.exp(-1) - sign * mp.e) / (1 + k * k)


def parity_components(max_mode, sector):
    if sector not in ("even-v", "odd-v"):
        raise ValueError("sector must be even-v or odd-v")

    ns = list(range(1 if sector == "even-v" else 2, max_mode + 1, 2))
    ws = weights()

    prime_sine = []
    arch_sine = []
    arch_diag = []
    sine_integral = []
    cusp_diag = []
    pole_vector = []

    for n in ns:
        k = mp.mpf(n) * mp.pi / 2
        si = mp.si(n * mp.pi)
        ci = mp.ci(n * mp.pi)

        sine_integral.append(si)
        cusp_diag.append(
            mp.log(mp.mpf(n) / 4) - ci - si / (n * mp.pi)
        )

        arch_sine.append(
            mp.quad(lambda t, k=k: h_arch(t) * mp.sin(k * t), [0, 2])
        )
        arch_diag.append(
            mp.quad(
                lambda t, k=k: -h_arch(t)
                * ((2 - t) * mp.cos(k * t) + mp.sin(k * t) / k),
                [0, 2],
            )
        )

        prime_sine.append(
            mp.fsum(
                w * mp.sin(n * mp.pi * mp.log(q) / 2)
                for q, w in zip(QS, ws)
            )
        )

        if sector == "even-v":
            pole_vector.append(
                2 * k * mp.cosh(mp.mpf("0.5"))
                / (k * k + mp.mpf("0.25"))
            )
        else:
            pole_vector.append(
                2 * k * mp.sinh(mp.mpf("0.5"))
                / (k * k + mp.mpf("0.25"))
            )

    size = len(ns)
    cusp = mp.matrix(size)
    prime = mp.matrix(size)
    arch = mp.matrix(size)
    pole = mp.matrix(size)
    pole_sign = 2 if sector == "even-v" else -2

    for i, m in enumerate(ns):
        for j, n in enumerate(ns):
            if i == j:
                cusp[i, j] = cusp_diag[i]
                k = mp.mpf(n) * mp.pi / 2
                prime[i, j] = -mp.fsum(
                    w
                    * (
                        (2 - mp.log(q))
                        * mp.cos(n * mp.pi * mp.log(q) / 2)
                        + mp.sin(n * mp.pi * mp.log(q) / 2) / k
                    )
                    for q, w in zip(QS, ws)
                )
                arch[i, j] = arch_diag[i]
            else:
                den = m * m - n * n
                cusp[i, j] = (
                    (2 / mp.pi)
                    * (n * sine_integral[i] - m * sine_integral[j])
                    / den
                )
                prime[i, j] = (
                    (4 / mp.pi)
                    * (n * prime_sine[i] - m * prime_sine[j])
                    / den
                )
                arch[i, j] = (
                    (4 / mp.pi)
                    * (n * arch_sine[i] - m * arch_sine[j])
                    / den
                )

            pole[i, j] = pole_sign * pole_vector[i] * pole_vector[j]

    full = cusp + prime + arch + pole
    return ns, cusp, prime, arch, pole, full


def prefix(matrix, size):
    return mp.matrix(
        [[matrix[i, j] for j in range(size)] for i in range(size)]
    )


def smooth_bulk(ns):
    out = mp.matrix(len(ns))
    for i, m in enumerate(ns):
        for j, n in enumerate(ns):
            out[i, j] = (
                (mp.log(mp.mpf(n) / 4) if i == j else 0)
                - mp.mpf(1) / (m + n)
            )
    return out


def resonance_data(data, cutoff, core_dim=2, count=6):
    ns, _, _, _, _, full = data
    size = sum(n <= cutoff for n in ns)
    ns = ns[:size]
    full = prefix(full, size)
    bulk = smooth_bulk(ns)
    residual = full - bulk

    bulk_tail = bulk[core_dim:, core_dim:]
    vals_bulk, q_bulk = mp.eigsy(bulk_tail)
    if vals_bulk[0] <= 0:
        raise RuntimeError("smooth bulk tail is not positive at this cutoff")

    invsqrt = mp.diag([1 / mp.sqrt(x) for x in vals_bulk])
    normalized = (
        invsqrt
        * (q_bulk.T * residual[core_dim:, core_dim:] * q_bulk)
        * invsqrt
    )
    mu, u = mp.eigsy((normalized + normalized.T) / 2)

    ids = sorted(
        range(len(mu)),
        key=lambda i: abs(1 + mu[i]),
    )[:count]

    full_vals, _ = mp.eigsy(full)

    return {
        "ns": ns,
        "full": full,
        "bulk": bulk,
        "bulk_tail_min": vals_bulk[0],
        "q_bulk": q_bulk,
        "invsqrt": invsqrt,
        "mu": mu,
        "u": u,
        "ids": ids,
        "distances": [abs(1 + mu[i]) for i in ids],
        "full_vals": full_vals,
    }


def resonance_basis(data, cutoff, howmany=4, core_dim=2):
    out = resonance_data(
        data,
        cutoff,
        core_dim=core_dim,
        count=max(6, howmany),
    )
    selected = mp.matrix(out["u"].rows, howmany)
    for j, idx in enumerate(out["ids"][:howmany]):
        for i in range(out["u"].rows):
            selected[i, j] = out["u"][i, idx]

    coeff = out["q_bulk"] * out["invsqrt"] * selected
    coeff = np.array(
        [
            [float(coeff[i, j]) for j in range(coeff.cols)]
            for i in range(coeff.rows)
        ]
    )
    q, _ = np.linalg.qr(coeff)
    return q


def max_principal_angle_deg(q_small, q_large):
    embedded = np.zeros((q_large.shape[0], q_small.shape[1]))
    embedded[: q_small.shape[0], :] = q_small
    singular = np.linalg.svd(embedded.T @ q_large, compute_uv=False)
    angles = np.arccos(np.clip(singular, -1, 1)) * 180 / np.pi
    return float(np.max(angles))


def source_feshbach(data, cutoff, core_dim=2):
    ns, _, _, _, _, full = data
    size = sum(n <= cutoff for n in ns)
    ns = ns[:size]
    full = prefix(full, size)
    bulk = smooth_bulk(ns)
    f = mp.matrix([source_overlap(n) for n in ns])

    energy_full = (f.T * mp.lu_solve(full, f))[0]
    energy_bulk = (f.T * mp.lu_solve(bulk, f))[0]

    residual = full - bulk
    bulk_tail = bulk[core_dim:, core_dim:]
    vals_bulk, q_bulk = mp.eigsy(bulk_tail)
    invsqrt = mp.diag([1 / mp.sqrt(x) for x in vals_bulk])

    normalized = (
        invsqrt
        * (q_bulk.T * residual[core_dim:, core_dim:] * q_bulk)
        * invsqrt
    )
    mu, u = mp.eigsy((normalized + normalized.T) / 2)

    tail_source = f[core_dim:, :]
    q_source = invsqrt * (q_bulk.T * tail_source)
    z = u.T * q_source
    tail_terms = [z[i] ** 2 / (1 + mu[i]) for i in range(len(mu))]
    tail_energy = mp.fsum(tail_terms)

    ids = sorted(range(len(mu)), key=lambda i: abs(1 + mu[i]))
    tail_energy_4 = mp.fsum(tail_terms[i] for i in ids[:4])

    att = full[core_dim:, core_dim:]
    act = full[:core_dim, core_dim:]
    acc = full[:core_dim, :core_dim]

    tail_solution = mp.lu_solve(att, tail_source)

    cross_solve = mp.matrix(att.rows, core_dim)
    for j in range(core_dim):
        rhs = mp.matrix([act[j, i] for i in range(act.cols)])
        sol = mp.lu_solve(att, rhs)
        for i in range(att.rows):
            cross_solve[i, j] = sol[i]

    schur = acc - act * cross_solve
    schur = (schur + schur.T) / 2

    core_source = f[:core_dim, :] - act * tail_solution
    schur_vals, schur_vecs = mp.eigsy(schur)
    core_coords = schur_vecs.T * core_source
    core_terms = [
        core_coords[i] ** 2 / schur_vals[i]
        for i in range(core_dim)
    ]
    core_energy = mp.fsum(core_terms)

    return {
        "energy_full": energy_full,
        "energy_bulk": energy_bulk,
        "tail_energy": tail_energy,
        "tail_energy_4_fraction": tail_energy_4 / tail_energy,
        "schur_vals": schur_vals,
        "core_energy": core_energy,
        "core_low_fraction": core_terms[0] / core_energy,
    }


def report(max_mode=64, dps=60):
    with mp.workdps(dps):
        data = {
            sector: parity_components(max_mode, sector)
            for sector in ("even-v", "odd-v")
        }

        cutoffs = [
            n for n in (16, 24, 32, 48, 64, 80, 96)
            if n <= max_mode
        ]

        print("Lane A bulk-subtracted resonance diagnostic")
        print("a=1 lambda=0 max_mode=", max_mode, "dps=", dps)

        for sector in ("even-v", "odd-v"):
            print("\\n" + sector)
            for cutoff in cutoffs:
                out = resonance_data(data[sector], cutoff)
                eig6 = (
                    mp.nstr(out["full_vals"][5], 12)
                    if len(out["full_vals"]) > 5
                    else "-"
                )
                eig7 = (
                    mp.nstr(out["full_vals"][6], 12)
                    if len(out["full_vals"]) > 6
                    else "-"
                )
                print(
                    cutoff,
                    "Btail_min=",
                    mp.nstr(out["bulk_tail_min"], 10),
                    "dist_to_-1=",
                    [mp.nstr(x, 9) for x in out["distances"]],
                    "eig6=",
                    eig6,
                    "eig7=",
                    eig7,
                )

            if max_mode >= 96:
                q64_4 = resonance_basis(data[sector], 64, howmany=4)
                q96_4 = resonance_basis(data[sector], 96, howmany=4)
                q64_5 = resonance_basis(data[sector], 64, howmany=5)
                q96_5 = resonance_basis(data[sector], 96, howmany=5)
                print(
                    "principal_angle_4D_64_to_96_deg=",
                    max_principal_angle_deg(q64_4, q96_4),
                )
                print(
                    "principal_angle_5D_64_to_96_deg=",
                    max_principal_angle_deg(q64_5, q96_5),
                )

            final = source_feshbach(data[sector], max_mode)
            print("source_E_full=", mp.nstr(final["energy_full"], 18))
            print("source_E_smooth_bulk=", mp.nstr(final["energy_bulk"], 18))
            print("tail_E=", mp.nstr(final["tail_energy"], 18))
            print(
                "tail_E_fraction_first4=",
                mp.nstr(final["tail_energy_4_fraction"], 16),
            )
            print(
                "core_Schur_eigs=",
                [
                    mp.nstr(final["schur_vals"][i], 14)
                    for i in range(len(final["schur_vals"]))
                ],
            )
            print(
                "core_low_direction_energy_fraction=",
                mp.nstr(final["core_low_fraction"], 16),
            )

        even_source = source_feshbach(data["even-v"], max_mode)
        odd_source = source_feshbach(data["odd-v"], max_mode)
        ee = even_source["energy_full"]
        eo = odd_source["energy_full"]
        print(
            "\\nkappa0_at_max_cutoff=",
            mp.nstr((ee - eo) / (ee + eo), 25),
        )
        print(
            "guardrail: finite-cutoff bulk/Feshbach diagnostic only; "
            "no infinite-cutoff theorem and no kappa1 promotion"
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-mode", type=int, default=64)
    parser.add_argument("--dps", type=int, default=60)
    args = parser.parse_args()
    report(max_mode=args.max_mode, dps=args.dps)


if __name__ == "__main__":
    main()
