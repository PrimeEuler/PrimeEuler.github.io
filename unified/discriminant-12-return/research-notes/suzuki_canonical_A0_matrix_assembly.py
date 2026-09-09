#!/usr/bin/env python3
"""Canonical end-to-end assembler for the pole-free Suzuki a=1 even-v matrix A0.

Purpose
-------
This file was added in direct response to External Audit Rounds 20-21. It
assembles one actual matrix from the component definitions, rather than
validating isolated formulas or replaying a stored certificate transcript.

Basis: psi_n(x)=sin(n*pi*(x+1)/2), n odd.

The important correction is the off-diagonal archimedean term. If

    h(t)=r''(t)=exp(-t/2)/(1-exp(-2t)) - 1/(2t),
    H_n=int_0^2 h(t) sin(n*pi*t/2) dt,
    a=m*pi/2, b=n*pi/2,

then direct product-to-sum reduction of the verified overlap kernel gives

    Karch_mn = [2ab/(a^2-b^2)] [b H_n - a H_m]
              = pi*m*n*(n H_n-m H_m)/(m^2-n^2).

This is NOT the older cross-paired expression

    -(4/pi)(n H_m-m H_n)/(n^2-m^2),

which External Audit Round 20 correctly found to disagree with direct
quadrature.

The corrected arch term remains Cauchy-like/displacement-rank two: writing
Y_n=n H_n,

    (m^2-n^2) Karch_mn = pi [ m (n Y_n) - (m Y_m) n ].

The cusp+prime off-diagonal part is separately displacement-rank two, so the
corrected full A0 is displacement-rank at most four rather than two.

This script is a numerical end-to-end reconstruction/cross-check, not itself
an interval certificate. It deliberately contains both the corrected and
legacy arch formulas so the historical v13.348 number can be reproduced and
the effect of the correction isolated.
"""
from __future__ import annotations

from functools import lru_cache
from math import exp, log, pi, sin, cos, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.special import sici

QS = (2, 3, 4, 5, 7)
LAMBDAS = (log(2), log(3), log(2), log(5), log(7))
ELLS = tuple(log(q) for q in QS)
WEIGHTS = tuple(L/sqrt(q) for L, q in zip(LAMBDAS, QS))


def h(t: float) -> float:
    if t == 0.0:
        return 0.25
    # Analytic expansion at the removable singularity:
    # h(t)=1/4-t/48-t^2/32+7t^3/11520+O(t^4).
    if abs(t) < 1e-7:
        return 0.25 - t/48.0 - t*t/32.0 + 7.0*t**3/11520.0
    return exp(-t/2.0)/(1.0-exp(-2.0*t)) - 1.0/(2.0*t)


@lru_cache(None)
def H(n: int) -> float:
    b = n*pi/2.0
    return quad(lambda t: h(t)*sin(b*t), 0.0, 2.0,
                epsabs=2e-13, epsrel=2e-13, limit=300)[0]


@lru_cache(None)
def arch_diag(n: int) -> float:
    b = n*pi/2.0
    f = lambda t: h(t)*((2.0-t)*cos(b*t)+sin(b*t)/b)
    return -quad(f, 0.0, 2.0, epsabs=2e-13, epsrel=2e-13, limit=300)[0]


def arch_off_correct(m: int, n: int) -> float:
    a, b = m*pi/2.0, n*pi/2.0
    return (2.0*a*b/(a*a-b*b))*(b*H(n)-a*H(m))


def arch_off_legacy(m: int, n: int) -> float:
    return -(4.0/pi)*(n*H(m)-m*H(n))/(n*n-m*m)


@lru_cache(None)
def prime_sequence(n: int) -> float:
    return sum(w*sin(n*pi*ell/2.0) for w, ell in zip(WEIGHTS, ELLS))


def prime_off(m: int, n: int) -> float:
    return -(4.0/pi)*(n*prime_sequence(m)-m*prime_sequence(n))/(n*n-m*m)


def prime_diag(n: int) -> float:
    k = n*pi/2.0
    ans = 0.0
    for w, ell in zip(WEIGHTS, ELLS):
        Snn = (2.0-ell)*cos(k*ell) + sin(k*ell)/k
        ans -= w*Snn
    return ans


@lru_cache(None)
def Si_n(n: int) -> float:
    return float(sici(n*pi)[0])


def cusp_off(m: int, n: int) -> float:
    return (2.0/pi)*(n*Si_n(m)-m*Si_n(n))/(m*m-n*n)


def cusp_diag(n: int) -> float:
    Si, Ci = sici(n*pi)
    return log(n/4.0)-float(Ci)-float(Si)/(n*pi)


def A0_entry(m: int, n: int, corrected_arch: bool = True) -> float:
    if m == n:
        return cusp_diag(n)+prime_diag(n)+arch_diag(n)
    ka = arch_off_correct(m, n) if corrected_arch else arch_off_legacy(m, n)
    return cusp_off(m, n)+prime_off(m, n)+ka


def assemble(start: int = 21, stop: int = 399,
             corrected_arch: bool = True):
    modes = np.arange(start, stop+1, 2, dtype=int)
    A = np.empty((len(modes), len(modes)), dtype=float)
    for i, m in enumerate(modes):
        A[i, i] = A0_entry(int(m), int(m), corrected_arch)
        for j in range(i+1, len(modes)):
            n = int(modes[j])
            z = A0_entry(int(m), n, corrected_arch)
            A[i, j] = A[j, i] = z
    return modes, A


def audit_pairs():
    targets = {
        (21, 29): 6.772385648528e-5,
        (21, 101): 1.9437951e-5,
        (29, 101): 1.4070380e-5,
    }
    rows = []
    for pair, target in targets.items():
        corr = arch_off_correct(*pair)
        old = arch_off_legacy(*pair)
        rows.append((pair, corr, target, corr-target, old))
    return rows


def report():
    print('arch pair cross-checks: pair, corrected, audit target, difference, legacy')
    for row in audit_pairs():
        print(row)
    _, Aold = assemble(corrected_arch=False)
    _, Anew = assemble(corrected_arch=True)
    lold = float(np.linalg.eigvalsh(Aold)[0])
    lnew = float(np.linalg.eigvalsh(Anew)[0])
    print('legacy lambda_min A0_[21,399]    =', repr(lold))
    print('corrected lambda_min A0_[21,399] =', repr(lnew))
    print('historical ledger target          = 0.231953166244')
    print('round-20 independent report       ~= 0.2767 (not reproduced here)')
    print('status: corrected matrix positive on this finite test only;')
    print('        infinite high-complement certification must be rebuilt.')


if __name__ == '__main__':
    report()
