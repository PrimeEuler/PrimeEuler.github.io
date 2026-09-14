#!/usr/bin/env python3
"""Pole-free midpoint replay for the odd M=4000 Suzuki finite-high block.

This isolates the source-faithful pole-free block

    A_FF^(0),  F={22,24,...,4000},

from the positive odd sinh-pole contribution 2 d d^T.  Since 2 d d^T >= 0,
a proof of A_FF^(0) >= 0.53 I is sufficient for the full odd finite-high block.

This file is a midpoint/regression diagnostic only.  It intentionally uses the
same scipy quadrature/special-function path as the independently reconstructed
v13.407 replay.  It does NOT by itself outward-certify the exact matrix.

Current regression values are approximately

    lambda_min(A_FF^(0))            = 0.532842383786
    lambda_min(A_FF^(0)-0.53 I)     = 0.002842383786
    ||B-L L^T||_F                   = 3.9e-14
    ||B-L L^T||_2                   = 2.8e-15
    1/sqrt(lambda_min(B))            = 18.75679541

The upstream analytic source-enclosure route is the v13.357 dimension-free
operator budget, based on the certified polynomial approximation to h(t).
That enclosure is logically separate from the nominal floating-point factor
residual computed here.
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


def assemble(start: int = 22, stop: int = 4000):
    modes = np.arange(start, stop+1, 2, dtype=float)
    k = modes*pi/2.0
    H, H_err = quad_vec(
        lambda t: h(float(t))*np.sin(k*t),
        0.0, 2.0, epsabs=1e-11, epsrel=1e-11,
    )
    arch_diag, arch_err = quad_vec(
        lambda t: -h(float(t))*((2.0-t)*np.cos(k*t)+np.sin(k*t)/k),
        0.0, 2.0, epsabs=1e-11, epsrel=1e-11,
    )

    prime_seq = np.zeros_like(modes)
    prime_diag = np.zeros_like(modes)
    for w, ell in zip(WEIGHTS, ELLS):
        prime_seq += w*np.sin(modes*pi*ell/2.0)
        Snn = (2.0-ell)*np.cos(k*ell) + np.sin(k*ell)/k
        prime_diag -= w*Snn

    Si, Ci = sici(modes*pi)
    cusp_diag = np.log(modes/4.0) - Ci - Si/(modes*pi)
    Z = 2.0*prime_seq + Si + 2.0*H

    m = modes[:, None]
    n = modes[None, :]
    den = n*n-m*m
    num = n*Z[:, None]-m*Z[None, :]
    np.fill_diagonal(den, 1.0)
    A0 = -(2.0/pi)*num/den
    np.fill_diagonal(A0, cusp_diag+prime_diag+arch_diag)
    A0 = 0.5*(A0+A0.T)

    d = 2.0*k*sinh(0.5)/(k*k+0.25)
    Ap = A0 + 2.0*np.outer(d, d)
    return modes.astype(int), A0, Ap, float(H_err), float(arch_err)


def report():
    modes, A0, Ap, H_err, arch_err = assemble()
    lam0 = float(eigsh(A0, k=1, which='SA', return_eigenvectors=False,
                       tol=1e-12)[0])
    lamp = float(eigsh(Ap, k=1, which='SA', return_eigenvectors=False,
                       tol=1e-12)[0])

    shift = 0.53
    B = A0-shift*np.eye(len(A0))
    shifted_min = float(eigsh(B, k=1, which='SA', return_eigenvectors=False,
                              tol=1e-12)[0])
    L = np.linalg.cholesky(B)
    R = B-L@L.T
    residual_fro = float(np.linalg.norm(R, ord='fro'))
    residual_2 = float(np.linalg.norm(R, ord=2))
    inverse_scale = 1.0/sqrt(shifted_min)

    print('dimension =', len(modes))
    print('modes =', modes[0], '..', modes[-1], 'step 2')
    print('quad_vec H reported error =', H_err)
    print('quad_vec arch-diag reported error =', arch_err)
    print('lambda_min(pole-free A_FF^(0)) =', repr(lam0))
    print('lambda_min(full A_FF) =', repr(lamp))
    print('lambda_min(A_FF^(0)-0.53 I) =', repr(shifted_min))
    print('shifted Cholesky Frobenius residual =', repr(residual_fro))
    print('shifted Cholesky spectral residual =', repr(residual_2))
    print('1/sqrt(shifted minimum) =', repr(inverse_scale))
    print('guardrail: midpoint only; outward source + arithmetic enclosure still required')

    assert 0.5328 < lam0 < 0.5329
    assert lamp > lam0
    assert shifted_min > 0.0028
    assert residual_fro < 1e-12


if __name__ == '__main__':
    report()
