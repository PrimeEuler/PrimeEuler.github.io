#!/usr/bin/env python3
"""Canonical end-to-end assembler for the pole-free Suzuki a=1 even-v matrix A0.

Audit status
------------
External Audit Round 20 incorrectly replaced the source-faithful archimedean
off-diagonal formula by the expression obtained from pairing h=g'' with the
derivative-basis overlap.  v13.387 resolves the issue: after integration by
parts, h acts on the Dirichlet sine modes themselves.

Accordingly the canonical/default archimedean off-diagonal entry is

    Karch_mn = -(4/pi)(n H_m-m H_n)/(n^2-m^2),
    H_n = int_0^2 h(t) sin(n*pi*t/2) dt.

The derivative-overlap expression is retained only as an audit comparator:

    Karch_derivative_overlap
      = (2ab/(a^2-b^2))(b H_n-a H_m),
      a=m*pi/2, b=n*pi/2.

Direct evaluation of Suzuki's source screw function against psi'_m,psi'_n
agrees with the canonical formula and not with the derivative-overlap branch.
The pole-free off-diagonal matrix therefore retains the rank-two sequence

    Z_n = 2 A_n + Si(n*pi) + 2 H_n,
    (A0)_mn = -(2/pi)(n Z_m-m Z_n)/(n^2-m^2).

This script is numerical regression infrastructure, not an RH/GRH proof or an
exact-zero certificate.
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


def arch_off_source(m: int, n: int) -> float:
    """Source-faithful post-IBP arch term; restored by v13.387."""
    return -(4.0/pi)*(n*H(m)-m*H(n))/(n*n-m*m)


def arch_off_derivative_overlap(m: int, n: int) -> float:
    """Audit comparator only; NOT the post-IBP arch matrix element."""
    a, b = m*pi/2.0, n*pi/2.0
    return (2.0*a*b/(a*a-b*b))*(b*H(n)-a*H(m))

# Backward-compatible name used by older scripts.
arch_off_legacy = arch_off_source


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


def A0_entry(m: int, n: int, source_faithful: bool = True) -> float:
    if m == n:
        return cusp_diag(n)+prime_diag(n)+arch_diag(n)
    ka = (arch_off_source(m, n) if source_faithful
          else arch_off_derivative_overlap(m, n))
    return cusp_off(m, n)+prime_off(m, n)+ka


def assemble(start: int = 21, stop: int = 399, source_faithful: bool = True):
    modes = np.arange(start, stop+1, 2, dtype=int)
    A = np.empty((len(modes), len(modes)), dtype=float)
    for i, m in enumerate(modes):
        A[i, i] = A0_entry(int(m), int(m), source_faithful)
        for j in range(i+1, len(modes)):
            n = int(modes[j])
            z = A0_entry(int(m), n, source_faithful)
            A[i, j] = A[j, i] = z
    return modes, A


def report():
    _, Asrc = assemble(source_faithful=True)
    _, Awrong = assemble(source_faithful=False)
    lsrc = float(np.linalg.eigvalsh(Asrc)[0])
    lwrong = float(np.linalg.eigvalsh(Awrong)[0])
    print('source-faithful lambda_min A0_[21,399] =', repr(lsrc))
    print('derivative-overlap comparator           =', repr(lwrong))
    print('historical rank-two target              = 0.231953166244')
    print('expected source-faithful value          ~= 0.231953166254')
    print('guardrail: derivative-overlap branch is not Suzuki post-IBP A0')


if __name__ == '__main__':
    report()
