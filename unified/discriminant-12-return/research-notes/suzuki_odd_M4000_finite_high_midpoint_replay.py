#!/usr/bin/env python3
"""Independent source-faithful midpoint replay of the odd M=4000 finite-high block.

Purpose
-------
Rebuild

    F = {22,24,...,4000}

from the canonical source-faithful scalar formulas rather than importing the
stored v13.404/v13.405 odd-sector transcript constants.  The full odd sinh-pole
rank-one term is included.

This is a reproducible midpoint/regression artifact.  Adaptive quadrature and
binary64 linear algebra are used, so this file alone is NOT an outward interval
certificate for A_FF >= 0.53 I.

Expected regression values on the audited branch are approximately

    lambda_min(A_FF)              = 0.533744999027
    lambda_min(A_FF-0.53 I)       = 0.003744999028
    ||A_FF-0.53 I - L L^T||_F     = 4.1e-14
    1/sqrt(lambda_min(shifted))    = 16.34083126

No exact-zero, RH, or GRH conclusion follows.
"""
from __future__ import annotations

from math import exp, log, pi, sin, sqrt, sinh
import numpy as np
from scipy.integrate import quad_vec
from scipy.special import sici
from scipy.sparse.linalg import eigsh

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


def scalar_sequences(modes: np.ndarray):
    """Return H_n and source-faithful arch diagonal for all requested modes."""
    k = modes*pi/2.0
    H, H_err = quad_vec(
        lambda t: h(float(t))*np.sin(k*t),
        0.0, 2.0, epsabs=1e-11, epsrel=1e-11,
    )
    arch_diag, arch_err = quad_vec(
        lambda t: -h(float(t))*((2.0-t)*np.cos(k*t)+np.sin(k*t)/k),
        0.0, 2.0, epsabs=1e-11, epsrel=1e-11,
    )
    return H, arch_diag, float(H_err), float(arch_err)


def assemble_odd_finite_high(start: int = 22, stop: int = 4000):
    modes = np.arange(start, stop+1, 2, dtype=float)
    H, arch_diag, H_err, arch_err = scalar_sequences(modes)

    prime_seq = np.zeros_like(modes)
    prime_diag = np.zeros_like(modes)
    k = modes*pi/2.0
    for w, ell in zip(WEIGHTS, ELLS):
        prime_seq += w*np.sin(modes*pi*ell/2.0)
        Snn = (2.0-ell)*np.cos(k*ell) + np.sin(k*ell)/k
        prime_diag -= w*Snn

    Si, Ci = sici(modes*pi)
    cusp_diag = np.log(modes/4.0) - Ci - Si/(modes*pi)

    # Combined source-faithful displacement sequence
    # Z_n = 2 A_n + Si(n pi) + 2 H_n.
    Z = 2.0*prime_seq + Si + 2.0*H

    m = modes[:, None]
    n = modes[None, :]
    den = n*n-m*m
    num = n*Z[:, None]-m*Z[None, :]
    # Avoid the removable diagonal 0/0; overwrite it immediately below.
    np.fill_diagonal(den, 1.0)
    A = -(2.0/pi)*num/den
    np.fill_diagonal(A, cusp_diag+prime_diag+arch_diag)

    # Odd-v/even-index sinh pole channel.  A diagonal basis-sign conjugation
    # may be used to make these coefficients positive without changing spectra.
    d = 2.0*k*sinh(0.5)/(k*k+0.25)
    A += 2.0*np.outer(d, d)
    A = 0.5*(A+A.T)
    return modes.astype(int), A, H_err, arch_err


def report():
    modes, A, H_err, arch_err = assemble_odd_finite_high()
    lam = float(eigsh(A, k=1, which='SA', return_eigenvectors=False,
                      tol=1e-12)[0])
    shift = 0.53
    B = A-shift*np.eye(len(A))
    L = np.linalg.cholesky(B)
    residual = float(np.linalg.norm(B-L@L.T, ord='fro'))
    shifted_min = float(eigsh(B, k=1, which='SA', return_eigenvectors=False,
                              tol=1e-12)[0])
    inverse_scale = 1.0/sqrt(shifted_min)

    print('dimension =', len(modes))
    print('modes =', modes[0], '..', modes[-1], 'step 2')
    print('quad_vec H reported error =', H_err)
    print('quad_vec arch-diag reported error =', arch_err)
    print('lambda_min(A_FF) =', repr(lam))
    print('lambda_min(A_FF-0.53 I) =', repr(shifted_min))
    print('shifted Cholesky Frobenius residual =', repr(residual))
    print('1/sqrt(shifted minimum) =', repr(inverse_scale))
    print('guardrail: midpoint regression only; outward source/arithmetic enclosure remains required')

    # Broad regression guards only; these are not proof inequalities.
    assert 0.5337 < lam < 0.5338
    assert shifted_min > 0.0037
    assert residual < 1e-12


if __name__ == '__main__':
    report()
