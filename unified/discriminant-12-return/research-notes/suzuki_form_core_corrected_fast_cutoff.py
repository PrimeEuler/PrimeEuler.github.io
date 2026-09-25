#!/usr/bin/env python3
"""Corrected fast-cutoff diagnostic for Lane A at a=1, lambda=0.

This extends the source-resolvent cutoff study beyond N=16 while preserving
the source-faithful parity pole sign

    A_pole^(even-v) = +2 c c^T,
    A_pole^(odd-v)  = -2 d d^T.

The even-v block uses the archived source-faithful same-parity formulas with
high-precision archimedean quadrature.  The odd-v block uses the archived
even-index Cauchy formulas with the corrected negative sinh-pole channel.

Outputs are high-precision finite-section diagnostics, not convergence or
spectral theorems.
"""
from __future__ import annotations

import mpmath as mp

from suzuki_form_core_schur_parameter_diagnostic import source_overlap

QS = (2, 3, 4, 5, 7)


def _weights():
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


def even_v_block(max_mode: int):
    """Odd Dirichlet indices: even-v sector, positive cosh pole channel."""
    ns = list(range(1, max_mode + 1, 2))
    ws = _weights()

    def amp(j):
        return sum(
            w * mp.sin(j * mp.pi * mp.log(q) / 2)
            for q, w in zip(QS, ws)
        )

    def cusp(m, n):
        if m == n:
            return (
                mp.log(mp.mpf(n) / 4)
                - mp.ci(n * mp.pi)
                - mp.si(n * mp.pi) / (n * mp.pi)
            )
        return (
            (2 / mp.pi)
            * (n * mp.si(m * mp.pi) - m * mp.si(n * mp.pi))
            / (m * m - n * n)
        )

    def shift(m, n, t):
        if m == n:
            k = n * mp.pi / 2
            return (2 - t) * mp.cos(k * t) + mp.sin(k * t) / k
        th = mp.pi * t / 2
        return (
            (4 / mp.pi)
            * (n * mp.sin(m * th) - m * mp.sin(n * th))
            / (n * n - m * m)
        )

    def prime(m, n):
        if m == n:
            return -sum(
                w * shift(n, n, mp.log(q))
                for q, w in zip(QS, ws)
            )
        return (
            -(4 / mp.pi)
            * (n * amp(m) - m * amp(n))
            / (n * n - m * m)
        )

    c = [
        mp.quad(
            lambda x, n=n:
                mp.sin(n * mp.pi * (x + 1) / 2) * mp.cosh(x / 2),
            [-1, 1],
        )
        for n in ns
    ]

    A = mp.matrix(len(ns))
    for i, m in enumerate(ns):
        for j, n in enumerate(ns):
            arch = mp.quad(
                lambda t, m=m, n=n: -h_arch(t) * shift(m, n, t),
                [0, 2],
            )
            A[i, j] = cusp(m, n) + prime(m, n) + arch + 2 * c[i] * c[j]
    return ns, A


def odd_v_block(max_mode: int):
    """Even Dirichlet indices: odd-v sector, corrected negative sinh pole."""
    ns = list(range(2, max_mode + 1, 2))
    ws = _weights()

    H = []
    D = []
    P = []
    Pd = []
    Si = []
    cusp = []
    d = []

    for n in ns:
        k = mp.mpf(n) * mp.pi / 2
        H.append(mp.quad(lambda t, k=k: h_arch(t) * mp.sin(k * t), [0, 2]))
        D.append(
            mp.quad(
                lambda t, k=k:
                    -h_arch(t)
                    * ((2 - t) * mp.cos(k * t) + mp.sin(k * t) / k),
                [0, 2],
            )
        )

        ps = mp.mpf(0)
        pd = mp.mpf(0)
        for q, w in zip(QS, ws):
            ell = mp.log(q)
            ang = n * mp.pi * ell / 2
            ps += w * mp.sin(ang)
            pd -= w * (
                (2 - ell) * mp.cos(ang)
                + mp.sin(ang) / k
            )
        P.append(ps)
        Pd.append(pd)

        x = n * mp.pi
        si = mp.si(x)
        ci = mp.ci(x)
        Si.append(si)
        cusp.append(mp.log(mp.mpf(n) / 4) - ci - si / x)
        d.append(2 * k * mp.sinh(mp.mpf("0.5")) / (k * k + mp.mpf("0.25")))

    Z = [2 * P[i] + Si[i] + 2 * H[i] for i in range(len(ns))]
    A = mp.matrix(len(ns))

    for i, m in enumerate(ns):
        for j, n in enumerate(ns):
            if i == j:
                val = cusp[i] + Pd[i] + D[i]
            else:
                val = (
                    -(2 / mp.pi)
                    * (n * Z[i] - m * Z[j])
                    / (n * n - m * m)
                )
            A[i, j] = val - 2 * d[i] * d[j]
    return ns, A


def _prefix(A, k):
    return mp.matrix([[A[i, j] for j in range(k)] for i in range(k)])


def spectral_energy(A, ns):
    vals, Q = mp.eigsy(A)
    f = mp.matrix([source_overlap(n, mp.mpf(1), mp.mpf(1)) for n in ns])
    y = Q.T * f
    terms = [y[j] ** 2 / vals[j] for j in range(len(ns))]
    E = sum(terms)
    return vals, E, terms[0] / E


def schur_low_core(A, core_dim=10):
    if A.rows <= core_dim:
        return A
    Acc = A[:core_dim, :core_dim]
    Acb = A[:core_dim, core_dim:]
    Abb = A[core_dim:, core_dim:]
    X = mp.matrix(Abb.rows, core_dim)
    for j in range(core_dim):
        rhs = mp.matrix([Acb[j, i] for i in range(Acb.cols)])
        sol = mp.lu_solve(Abb, rhs)
        for i in range(Abb.rows):
            X[i, j] = sol[i]
    S = Acc - Acb * X
    return (S + S.T) / 2


def report(max_mode=32, dps=90):
    with mp.workdps(dps):
        ns_e, A_e = even_v_block(max_mode)
        ns_o, A_o = odd_v_block(max_mode)

        print("Lane A corrected fast-cutoff diagnostic")
        print("a=1 lambda=0 max_mode=", max_mode, "dps=", dps)
        print("N kappa0 lambda_e lambda_o")
        for N in range(18, max_mode + 1, 2):
            ke = len([n for n in ns_e if n <= N])
            ko = len([n for n in ns_o if n <= N])
            ve, Ee, _ = spectral_energy(_prefix(A_e, ke), ns_e[:ke])
            vo, Eo, _ = spectral_energy(_prefix(A_o, ko), ns_o[:ko])
            kappa0 = (Ee - Eo) / (Ee + Eo)
            print(
                N,
                mp.nstr(kappa0, 22),
                mp.nstr(ve[0], 10),
                mp.nstr(vo[0], 10),
            )

        Se = schur_low_core(A_e)
        So = schur_low_core(A_o)
        ee, _ = mp.eigsy(Se)
        eo, _ = mp.eigsy(So)

        print("max-cutoff effective 10-core Schur spectrum")
        print("even-v:", [mp.nstr(ee[i], 12) for i in range(min(10, len(ee)))])
        print("odd-v :", [mp.nstr(eo[i], 12) for i in range(min(10, len(eo)))])
        print("guardrail: finite-cutoff diagnostic only; no kappa1 promotion")


if __name__ == "__main__":
    report()
