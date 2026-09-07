#!/usr/bin/env python3
"""Source-faithful calibration kernel for Suzuki arXiv:2606.09096v2, eq. (1.3).

This is the Riemann control experiment for the D12 Fredholm solver.  It implements
Suzuki's exact continuous screw function before any D12 transfer is attempted.
The formula is kept visibly decomposed into pole, prime-ramp, and archimedean
pieces so each contribution can be audited independently.

Requires numpy and mpmath.  This file is a research calibration, not an RH proof.
"""
from __future__ import annotations

from math import exp, floor, log, pi, sqrt
from typing import Iterable
import numpy as np
import mpmath as mp


def _primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(sqrt(n)) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = False
    return np.flatnonzero(sieve).astype(int).tolist()


def riemann_prime_powers(T: float) -> list[tuple[int, float]]:
    """(p^k, Lambda(p^k)/sqrt(p^k)) for log(p^k)<=T."""
    horizon = int(floor(exp(T)))
    out: list[tuple[int, float]] = []
    for p in _primes_up_to(horizon):
        lp = log(p)
        pk = p
        while pk <= horizon:
            out.append((pk, lp / sqrt(pk)))
            if pk > horizon // p:
                break
            pk *= p
    out.sort()
    return out


def prime_ramp(t: float, data: Iterable[tuple[int, float]] | None = None) -> float:
    """Suzuki's prime term sum Lambda(n)/sqrt(n) (|t|-log n)_+."""
    T = abs(float(t))
    if data is None:
        data = riemann_prime_powers(T)
    return sum(c * max(T - log(n), 0.0) for n, c in data)


def pole_term(t: float) -> float:
    """The s(s-1) contribution in Suzuki (1.3)."""
    T = abs(float(t))
    return -4.0 * (exp(T/2.0) + exp(-T/2.0) - 2.0)


def archimedean_term(t: float, dps: int = 50) -> float:
    """Exact non-prime, non-pole gamma term in Suzuki (1.3).

    A direct Hurwitz-Lerch evaluation is used away from t=0.  At t=0 the
    continuous value is exactly zero.  High precision is intentional because
    the two Lerch terms cancel strongly near the origin.
    """
    T = abs(float(t))
    if T == 0.0:
        return 0.0
    with mp.workdps(dps):
        q = mp.mpf('0.25')
        TT = mp.mpf(T)
        psi = mp.digamma(q)
        linear = -(TT/2) * (psi - mp.log(mp.pi))
        phi1 = mp.zeta(2, q)  # Phi(1,2,1/4)
        z = mp.e ** (-2*TT)
        phiz = mp.lerchphi(z, 2, q)
        lerch = -mp.mpf('0.25') * (phi1 - mp.e**(-TT/2) * phiz)
        return float(linear + lerch)


def g_suzuki(t: float, dps: int = 50) -> float:
    """Suzuki v2 equation (1.3), exactly decomposed."""
    return pole_term(t) + prime_ramp(t) + archimedean_term(t, dps=dps)


def local_model(t: float) -> float:
    """Leading no-prime expansion from Suzuki eq. (2.2), valid near zero."""
    T = abs(float(t))
    if T == 0.0:
        return 0.0
    A = 0.5 * (log(2*pi) + float(mp.euler) - 1.0)
    return 0.5*T*log(T) + A*T


def calibration_report(ts=(1e-4, 1e-3, 1e-2, 0.1, 0.5, 1.0)) -> dict:
    """Return source-level invariants used before coupling to Nyström."""
    rows = []
    for t in ts:
        gp = g_suzuki(t)
        gm = g_suzuki(-t)
        rows.append({
            't': t,
            'g(t)': gp,
            'even_error': abs(gp-gm),
            'local_remainder': gp-local_model(t) if t < 0.3 else None,
        })
    return {
        'g(0)': g_suzuki(0.0),
        'rows': rows,
        'source_equation': 'Suzuki arXiv:2606.09096v2 eq. (1.3)',
    }


if __name__ == '__main__':
    report = calibration_report()
    print('source:', report['source_equation'])
    print('g(0):', report['g(0)'])
    for row in report['rows']:
        print(row)
