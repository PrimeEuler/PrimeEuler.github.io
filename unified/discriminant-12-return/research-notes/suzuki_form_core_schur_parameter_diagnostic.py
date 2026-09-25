#!/usr/bin/env python3
"""Source-faithful form-core Galerkin diagnostics for Suzuki's finite Schur data.

This script implements the numerical gate opened in ledger v13.794.

It reuses the audited direct Dirichlet form matrix from
suzuki_componentwise_high_precision_audit.py and solves

    (A_N - lambda I)c_N = f_N,

where f_N is the exact L2 projection of exp(x) onto the orthonormal Dirichlet
basis

    psi_n(x) = a^{-1/2} sin(n*pi*(x+a)/(2a)).

No endpoint condition is imposed on the limiting deficiency vector.  Endpoint
traces occur only on the form-core trial functions, as is appropriate for a
Friedrichs/form Galerkin approximation.

For lambda=0 the outputs are diagnostics for the Section-7 xi target only when
the unshifted finite section is positive/invertible.  They are NOT a proof that
A_a>0, RH, or finite-to-infinite convergence.

The first two scalar Schur diagnostics are

    kappa0 = h(i) = m'(i),

and

    kappa1 = h_1(i),

with h(z)=F(z)/F(-z).  In the exact finite theory both lie in the closed unit
disk.  A Galerkin value outside the disk is therefore a useful truncation /
conditioning warning, not a contradiction of the exact operator theory.
"""
from __future__ import annotations

import mpmath as mp

from suzuki_componentwise_high_precision_audit import (
    component_matrices_mp,
    parity_indices_v,
)


def frequency(n: int, a: mp.mpf) -> mp.mpf:
    return mp.mpf(n) * mp.pi / (2 * a)


def source_overlap(n: int, a: mp.mpf, alpha: mp.mpf) -> mp.mpf:
    """Exact <psi_n, exp(alpha*x)> on [-a,a]."""
    k = frequency(n, a)
    s = -1 if n % 2 else 1  # (-1)^n
    u = mp.e ** (-alpha * a) - s * mp.e ** (alpha * a)
    return (k / mp.sqrt(a)) * u / (alpha * alpha + k * k)


def moment_overlap(n: int, a: mp.mpf, alpha: mp.mpf) -> mp.mpf:
    """Exact <psi_n, x exp(alpha*x)> = d/dalpha source_overlap."""
    k = frequency(n, a)
    s = -1 if n % 2 else 1
    em = mp.e ** (-alpha * a)
    ep = mp.e ** (alpha * a)
    u = em - s * ep
    up = -a * (em + s * ep)
    den = alpha * alpha + k * k
    return (k / mp.sqrt(a)) * (up / den - 2 * alpha * u / (den * den))


def _submatrix(A: mp.matrix, idx: list[int]) -> mp.matrix:
    return mp.matrix([[A[i, j] for j in idx] for i in idx])


def _subvector(v: mp.matrix, idx: list[int]) -> mp.matrix:
    return mp.matrix([v[i] for i in idx])


def schur_diagnostic_from_matrix(
    A: mp.matrix,
    modes: int,
    a: float | mp.mpf = 1,
    lam: float | mp.mpf = 0,
) -> dict:
    """Compute kappa0,kappa1 and conditioning data for one prefix."""
    aa = mp.mpf(str(a))
    ll = mp.mpf(str(lam))

    even = parity_indices_v(modes, "even")
    odd = parity_indices_v(modes, "odd")

    Ae = _submatrix(A, even)
    Ao = _submatrix(A, odd)
    for j in range(len(even)):
        Ae[j, j] -= ll
    for j in range(len(odd)):
        Ao[j, j] -= ll

    fplus = mp.matrix([
        source_overlap(n, aa, mp.mpf(1)) for n in range(1, modes + 1)
    ])
    fminus = mp.matrix([
        source_overlap(n, aa, mp.mpf(-1)) for n in range(1, modes + 1)
    ])
    mxplus = mp.matrix([
        moment_overlap(n, aa, mp.mpf(1)) for n in range(1, modes + 1)
    ])
    mxminus = mp.matrix([
        moment_overlap(n, aa, mp.mpf(-1)) for n in range(1, modes + 1)
    ])

    fe = _subvector(fplus, even)
    fo = _subvector(fplus, odd)

    ce = mp.lu_solve(Ae, fe)
    co = mp.lu_solve(Ao, fo)

    Ee = (fe.T * ce)[0]
    Eo = (fo.T * co)[0]
    H = Ee + Eo
    kappa0 = (Ee - Eo) / H

    c = mp.matrix(modes, 1)
    for j, idx in enumerate(even):
        c[idx] = ce[j]
    for j, idx in enumerate(odd):
        c[idx] = co[j]

    Mplus = (mxplus.T * c)[0]
    Mminus = (mxminus.T * c)[0]

    kappa1 = -2 * (Mminus / H + kappa0 * Mplus / H) / (1 - kappa0**2)

    ve, _ = mp.eigsy(Ae)
    vo, _ = mp.eigsy(Ao)

    re = Ae * ce - fe
    ro = Ao * co - fo
    residual_inf = max(
        [abs(re[j]) for j in range(len(re))]
        + [abs(ro[j]) for j in range(len(ro))]
    )

    return {
        "modes": modes,
        "a": aa,
        "lambda": ll,
        "min_even": ve[0],
        "min_odd": vo[0],
        "cond_even": abs(ve[-1] / ve[0]),
        "cond_odd": abs(vo[-1] / vo[0]),
        "energy_even": Ee,
        "energy_odd": Eo,
        "odd_even_energy_ratio": Eo / Ee,
        "kappa0": kappa0,
        "kappa1": kappa1,
        "residual_inf": residual_inf,
    }


def run_sequence(
    mode_counts=(4, 6, 8, 10, 12),
    a: float = 1.0,
    lam: float = 0.0,
    dps: int = 60,
) -> list[dict]:
    """Assemble the largest form matrix once and return nested-prefix diagnostics."""
    max_modes = max(mode_counts)
    with mp.workdps(dps):
        P, R, H = component_matrices_mp(max_modes, a=a, dps=dps)
        A = P + R + H
        return [
            schur_diagnostic_from_matrix(A, N, a=a, lam=lam)
            for N in mode_counts
        ]


def print_sequence(**kwargs) -> None:
    rows = run_sequence(**kwargs)
    print("Suzuki source-faithful form-core Schur diagnostic")
    for row in rows:
        print(
            "N=", row["modes"],
            "a=", mp.nstr(row["a"], 6),
            "lambda=", mp.nstr(row["lambda"], 6),
            "min_even=", mp.nstr(row["min_even"], 10),
            "min_odd=", mp.nstr(row["min_odd"], 10),
            "kappa0=", mp.nstr(row["kappa0"], 18),
            "kappa1=", mp.nstr(row["kappa1"], 18),
            "Eo/Ee=", mp.nstr(row["odd_even_energy_ratio"], 12),
            "resinf=", mp.nstr(row["residual_inf"], 6),
        )


if __name__ == "__main__":
    print_sequence()
