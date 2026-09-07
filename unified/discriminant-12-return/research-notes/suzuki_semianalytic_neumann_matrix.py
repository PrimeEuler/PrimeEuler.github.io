#!/usr/bin/env python3
"""Semi-analytic Neumann/Dirichlet matrix elements for Suzuki's screw kernel.

The 2-D matrix element of a translation kernel h(x-y) against the normalized
Dirichlet derivative basis is reduced exactly to one dimension in t=x-y.  The
remaining universal Suzuki cusp

    g(t)=1/2 |t| log|t| + A |t| + O(t^2)

is subtracted before Gauss-Legendre integration.  Prime-power breakpoints then
become fixed one-dimensional points t=log(p^k).  This removes the dominant
quadrature error seen in v13.289.

This is a numerical control, not a proof of RH and not an admissibility
certificate for lambda.
"""
from __future__ import annotations

from math import log, pi, sqrt
import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import leggauss

from suzuki_generalized_eigenvalue_parity_audit import g_fast, riemann_prime_powers

Array = np.ndarray


def frequency(n: int, a: float = 1.0) -> float:
    return n*pi/(2.0*a)


def overlap_one(m: int, n: int, t: float, a: float = 1.0) -> float:
    """Integral of q_m(x)q_n(x-t) over the overlap, t>=0.

    q_n(x)=k_n a^{-1/2} cos(k_n(x+a)) is the derivative of the normalized
    Dirichlet sine mode.  The x-integral is evaluated analytically.
    """
    L = 2.0*a
    A = frequency(m, a)
    B = frequency(n, a)

    def int_cos(w: float, phase: float) -> float:
        if abs(w) < 1e-14:
            return (L-t)*np.cos(phase)
        return (np.sin(w*L+phase)-np.sin(w*t+phase))/w

    I = 0.5*(int_cos(A-B, B*t) + int_cos(A+B, -B*t))
    return (A*B/a)*I


def symmetric_overlap(m: int, n: int, t: float, a: float = 1.0) -> float:
    """Positive- and negative-t overlap contribution for an even kernel."""
    return overlap_one(m, n, t, a) + overlap_one(n, m, t, a)


def local_model(t: float) -> float:
    """Suzuki equation-(2.2) singular model near the origin."""
    T = abs(float(t))
    if T == 0.0:
        return 0.0
    A = 0.5*(log(2*pi) + float(mp.euler) - 1.0)
    return 0.5*T*log(T) + A*T


def breakpoints(a: float = 1.0) -> list[float]:
    L = 2.0*a
    pts = {0.0, L}
    for n, _ in riemann_prime_powers(L):
        ell = log(n)
        if 0.0 < ell < L:
            pts.add(float(ell))
    return sorted(pts)


def model_integral(m: int, n: int, a: float = 1.0, order: int = 160) -> float:
    """Integrate the t log t model after t=L u^2 regularization."""
    L = 2.0*a
    gx, gw = leggauss(order)
    u = 0.5*(gx+1.0)
    wu = 0.5*gw
    t = L*u*u
    jac = 2.0*L*u
    vals = np.asarray([
        local_model(float(tt))*symmetric_overlap(m, n, float(tt), a)
        for tt in t
    ])
    return float(np.sum(wu*jac*vals))


def remainder_integral(m: int, n: int, a: float = 1.0, order: int = 16) -> float:
    """Integrate g-local_model on exact prime-power segments."""
    prime_data = riemann_prime_powers(2.0*a)
    gx, gw = leggauss(order)
    total = 0.0
    for left, right in zip(breakpoints(a)[:-1], breakpoints(a)[1:]):
        t = 0.5*(right-left)*gx + 0.5*(right+left)
        w = 0.5*(right-left)*gw
        vals = np.asarray([
            (g_fast(float(tt), prime_data)-local_model(float(tt)))
            * symmetric_overlap(m, n, float(tt), a)
            for tt in t
        ])
        total += float(np.sum(w*vals))
    return total


def matrix(modes: int, a: float = 1.0, remainder_order: int = 16,
           model_order: int = 160) -> Array:
    A = np.zeros((modes, modes), dtype=float)
    for m in range(1, modes+1):
        for n in range(m, modes+1):
            value = model_integral(m, n, a, model_order)
            value += remainder_integral(m, n, a, remainder_order)
            A[m-1, n-1] = A[n-1, m-1] = value
    return A


def parity_indices(modes: int, parity: str) -> list[int]:
    if parity == 'odd':
        return [j for j in range(modes) if (j+1) % 2 == 1]
    if parity == 'even':
        return [j for j in range(modes) if (j+1) % 2 == 0]
    raise ValueError("parity must be 'odd' or 'even'")


def audit(modes: int = 14, orders=(8,10,12,16,20,24,32), a: float = 1.0):
    rows = []
    for order in orders:
        A = matrix(modes, a, remainder_order=order)
        odd = parity_indices(modes, 'odd')
        even = parity_indices(modes, 'even')
        eo = np.linalg.eigvalsh(A[np.ix_(odd, odd)])
        ee = np.linalg.eigvalsh(A[np.ix_(even, even)])
        ev = np.linalg.eigvalsh(A)
        rows.append({
            'remainder_order': order,
            'lowest': float(ev[0]),
            'odd_min': float(eo[0]),
            'even_min': float(ee[0]),
            'first_eigenvalues': [float(x) for x in ev[:min(6, len(ev))]],
        })
    return rows


if __name__ == '__main__':
    print('Suzuki semi-analytic 1D matrix audit with cusp subtraction')
    for row in audit():
        print(row)
