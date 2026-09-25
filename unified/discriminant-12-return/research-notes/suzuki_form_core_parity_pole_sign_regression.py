#!/usr/bin/env python3
"""Parity sign regression for the pole part of Suzuki's a=1 form.

This audit exists because the older odd-v certificate lineage (v13.403 onward)
used +2 d d^T for the sinh pole channel.  The source-faithful direct form used
by the current Lane A Galerkin code instead gives the parity-signed identity

    A_pole = 2 c c^T - 2 d d^T,

where
    c_n = <psi_n, cosh(x/2)>,
    d_n = <psi_n, sinh(x/2)>.

Hence odd Dirichlet indices (even-v functions) see +2 c c^T, while even
Dirichlet indices (odd-v functions) see -2 d d^T.

The identity follows directly from
    g_pole(x-y) = -8(cosh((x-y)/2)-1)
and integration by parts on H_0^1.  This script numerically regresses the
closed identity against the independently assembled source component from
suzuki_componentwise_high_precision_audit.py.

No spectral, RH, or zero-mode conclusion follows from this file.
"""
from __future__ import annotations

import mpmath as mp

from suzuki_componentwise_high_precision_audit import component_matrices_mp


def psi(n: int, x: mp.mpf, a: mp.mpf = mp.mpf(1)) -> mp.mpf:
    return mp.sin(mp.mpf(n) * mp.pi * (x + a) / (2 * a)) / mp.sqrt(a)


def cosh_overlap(n: int, a: mp.mpf = mp.mpf(1)) -> mp.mpf:
    return mp.quad(lambda x: psi(n, x, a) * mp.cosh(x / 2), [-a, a])


def sinh_overlap(n: int, a: mp.mpf = mp.mpf(1)) -> mp.mpf:
    return mp.quad(lambda x: psi(n, x, a) * mp.sinh(x / 2), [-a, a])


def analytic_even_mode_d(n: int) -> mp.mpf:
    """Magnitude of <psi_n,sinh(x/2)> at a=1 for even n."""
    if n % 2:
        raise ValueError("n must be even")
    k = mp.mpf(n) * mp.pi / 2
    return 2 * k * mp.sinh(mp.mpf("0.5")) / (k * k + mp.mpf("0.25"))


def report(modes: int = 8, dps: int = 60) -> None:
    with mp.workdps(dps):
        P, _, _ = component_matrices_mp(modes, a=1, dps=dps)
        c = mp.matrix([cosh_overlap(n) for n in range(1, modes + 1)])
        d = mp.matrix([sinh_overlap(n) for n in range(1, modes + 1)])
        closed = 2 * c * c.T - 2 * d * d.T

        err = max(
            abs(P[i, j] - closed[i, j])
            for i in range(modes)
            for j in range(modes)
        )

        print("max |direct pole - (2cc^T-2dd^T)| =", mp.nstr(err, 20))
        print("parity samples")
        for n in range(1, modes + 1):
            diag = P[n - 1, n - 1]
            if n % 2:
                predicted = 2 * c[n - 1] ** 2
                label = "even-v / cosh / positive"
            else:
                predicted = -2 * d[n - 1] ** 2
                label = "odd-v / sinh / negative"
                dan = analytic_even_mode_d(n)
                # Basis convention can flip d_n; compare magnitudes.
                assert abs(abs(d[n - 1]) - dan) < mp.mpf("1e-50")
            print(n, label, mp.nstr(diag, 20), mp.nstr(predicted, 20))
            assert abs(diag - predicted) < mp.mpf("1e-50")

        # The old odd-v convention +2dd^T differs from the correct -2dd^T
        # by exactly 4dd^T.
        n = 2
        dn = analytic_even_mode_d(n)
        old_minus_correct_diag = 4 * dn * dn
        print(
            "n=2 old(+2dd)-correct(-2dd) diagonal =",
            mp.nstr(old_minus_correct_diag, 20),
        )

        assert err < mp.mpf("1e-50")
        print("PASS: pole parity sign identity verified")


if __name__ == "__main__":
    report()
