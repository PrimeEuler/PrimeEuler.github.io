#!/usr/bin/env python3
"""Parity-separated and quadrature-refined audit of Suzuki v2 equation (8.7).

This file supersedes the numerical interpretation recorded in ledger v13.287.
The committed v13.287 implementation, when actually executed, does not reproduce
its recorded ~-1.3 Ritz table.  This audit therefore treats reproduction as the
first invariant and then studies parity, denominator conditioning, quadrature
refinement, and an independent off-grid generalized residual.

For a=1 the Hurwitz-Lerch contribution is accelerated with the convergent local
series used by Suzuki immediately before equation (2.2).  Since |x-y|<=2 and
2<pi, this stays inside the |t|<pi convergence window.  The accelerated values
are checked against the direct high-precision Lerch implementation at sample
points before use.

This is a numerical audit, not a proof of RH and not an admissibility
certificate for any lambda.
"""
from __future__ import annotations

from math import exp, factorial, floor, log, pi, sqrt
import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import Legendre, leggauss

from suzuki_riemann_screw_calibration import (
    archimedean_term,
    pole_term,
    riemann_prime_powers,
)

Array = np.ndarray


def neumann_kernel(a: float, x: float, y: float) -> float:
    return (x*x + y*y)/(4.0*a) - 0.5*abs(x-y) + a/6.0


def _arch_series_coefficients(nmax: int = 48, dps: int = 60):
    with mp.workdps(dps):
        q = mp.mpf('0.25')
        coeff = [0.0, 0.0]
        for n in range(2, nmax + 1):
            coeff.append(float(mp.zeta(2-n, q) * (-2)**n / mp.factorial(n)))
        return (
            coeff,
            float(mp.digamma(q)),
            float(mp.digamma(2)),
            float(mp.log(mp.pi)),
        )


_ARCH_COEFF, _PSI_Q, _PSI_2, _LOG_PI = _arch_series_coefficients()


def archimedean_series(t: float) -> float:
    """Suzuki's pre-(2.2) expansion, valid here for |t|<=2<pi."""
    T = abs(float(t))
    if T == 0.0:
        return 0.0
    poly = 0.0
    # Horner for sum_{n>=2} c_n T^n.
    for n in range(len(_ARCH_COEFF)-1, 1, -1):
        poly = (poly + _ARCH_COEFF[n]) * T
    poly *= T
    delta_F = 2*T*(log(2*T) + _PSI_Q - _PSI_2) + poly
    return -0.5*T*(_PSI_Q - _LOG_PI) + 0.25*delta_F


def series_calibration(ts=(1e-4, 1e-2, 0.1, 0.5, 1.0, 2.0), dps: int = 35):
    return [
        {
            't': t,
            'series': archimedean_series(t),
            'direct': archimedean_term(t, dps=dps),
            'abs_error': abs(archimedean_series(t) - archimedean_term(t, dps=dps)),
        }
        for t in ts
    ]


def g_fast(t: float, prime_data) -> float:
    T = abs(float(t))
    ramp = sum(c * max(T-log(n), 0.0) for n, c in prime_data)
    return pole_term(t) + ramp + archimedean_series(T)


def basis_values(degree: int, x: Array | float, a: float) -> Array:
    t = np.asarray(x, dtype=float)/a
    return np.asarray([Legendre.basis(n)(t) for n in range(1, degree+1)])


def row_breakpoints(x: float, a: float, prime_data) -> list[float]:
    pts = {-a, a, float(x)}
    for n, _ in prime_data:
        ell = log(n)
        for y in (x-ell, x+ell):
            if -a < y < a:
                pts.add(float(y))
    return sorted(pts)


def outer_breakpoints(a: float, prime_data) -> list[float]:
    pts = {-a, 0.0, a}
    for n, _ in prime_data:
        ell = log(n)
        for x in (-a+ell, a-ell):
            if -a < x < a:
                pts.add(float(x))
    return sorted(pts)


def galerkin_matrices(
    degree: int,
    a: float = 1.0,
    outer_order: int = 7,
    inner_order: int = 8,
) -> tuple[Array, Array]:
    if 2*a >= pi:
        raise ValueError('series-accelerated audit currently requires 2a < pi')
    prime_data = riemann_prime_powers(2.0*a)
    G = np.zeros((degree, degree), dtype=float)
    K = np.zeros((degree, degree), dtype=float)
    xo, wo = leggauss(outer_order)
    yi, wi = leggauss(inner_order)

    obp = outer_breakpoints(a, prime_data)
    for xl, xr in zip(obp[:-1], obp[1:]):
        xs = 0.5*(xr-xl)*xo + 0.5*(xr+xl)
        wx = 0.5*(xr-xl)*wo
        for x, w_x in zip(xs, wx):
            px = basis_values(degree, x, a)
            rg = np.zeros(degree)
            rk = np.zeros(degree)
            rbp = row_breakpoints(float(x), a, prime_data)
            for yl, yr in zip(rbp[:-1], rbp[1:]):
                ys = 0.5*(yr-yl)*yi + 0.5*(yr+yl)
                wy = 0.5*(yr-yl)*wi
                py = np.asarray([basis_values(degree, y, a) for y in ys])
                gv = np.asarray([g_fast(float(x-y), prime_data) for y in ys])
                kv = np.asarray([neumann_kernel(a, float(x), float(y)) for y in ys])
                rg += (wy*gv) @ py
                rk += (wy*kv) @ py
            G += w_x*np.outer(px, rg)
            K += w_x*np.outer(px, rk)

    return 0.5*(G+G.T), 0.5*(K+K.T)


def generalized_eigenpairs(G: Array, K: Array) -> tuple[Array, Array]:
    L = np.linalg.cholesky(K)
    X = np.linalg.solve(L, G)
    A = np.linalg.solve(L, X.T).T
    A = 0.5*(A+A.T)
    vals, y = np.linalg.eigh(A)
    vecs = np.linalg.solve(L.T, y)
    return vals, vecs


def sector_indices(degree: int, parity: str) -> list[int]:
    if parity == 'odd':
        return [j for j in range(degree) if (j+1) % 2 == 1]
    if parity == 'even':
        return [j for j in range(degree) if (j+1) % 2 == 0]
    raise ValueError("parity must be 'odd' or 'even'")


def sector_minimum(G: Array, K: Array, parity: str) -> float:
    idx = sector_indices(len(G), parity)
    vals, _ = generalized_eigenpairs(G[np.ix_(idx, idx)], K[np.ix_(idx, idx)])
    return float(vals[0])


def parity_leakage(G: Array, K: Array) -> tuple[float, float]:
    odd = sector_indices(len(G), 'odd')
    even = sector_indices(len(G), 'even')
    return (
        float(np.linalg.norm(G[np.ix_(odd, even)], ord=np.inf)),
        float(np.linalg.norm(K[np.ix_(odd, even)], ord=np.inf)),
    )


def refinement_audit(
    degree: int = 10,
    quadratures=((7,8),(11,12),(15,16),(19,20),(23,24),(27,28),(31,32),(39,40)),
    a: float = 1.0,
):
    rows = []
    for outer_order, inner_order in quadratures:
        G, K = galerkin_matrices(degree, a, outer_order, inner_order)
        odd_min = sector_minimum(G, K, 'odd')
        even_min = sector_minimum(G, K, 'even')
        leak_G, leak_K = parity_leakage(G, K)
        rows.append({
            'outer_order': outer_order,
            'inner_order': inner_order,
            'odd_min': odd_min,
            'even_min': even_min,
            'lowest': min(odd_min, even_min),
            'cond_K': float(np.linalg.cond(K)),
            'min_eig_K': float(np.linalg.eigvalsh(K)[0]),
            'parity_leak_G_inf': leak_G,
            'parity_leak_K_inf': leak_K,
        })
    return rows


def operator_action(c: Array, xs: Array, a: float = 1.0, inner_order: int = 50):
    degree = len(c)
    prime_data = riemann_prime_powers(2*a)
    yi, wi = leggauss(inner_order)
    Gu = np.zeros(len(xs))
    Ku = np.zeros(len(xs))
    for ix, x in enumerate(xs):
        for yl, yr in zip(row_breakpoints(float(x), a, prime_data)[:-1], row_breakpoints(float(x), a, prime_data)[1:]):
            ys = 0.5*(yr-yl)*yi + 0.5*(yr+yl)
            wy = 0.5*(yr-yl)*wi
            uy = np.asarray([basis_values(degree, y, a) @ c for y in ys])
            gv = np.asarray([g_fast(float(x-y), prime_data) for y in ys])
            kv = np.asarray([neumann_kernel(a, float(x), float(y)) for y in ys])
            Gu[ix] += np.sum(wy*gv*uy)
            Ku[ix] += np.sum(wy*kv*uy)
    return Gu, Ku


def offgrid_residual(
    degree: int = 10,
    a: float = 1.0,
    outer_order: int = 39,
    inner_order: int = 40,
    check_x_order: int = 61,
    check_inner_order: int = 50,
):
    G, K = galerkin_matrices(degree, a, outer_order, inner_order)
    vals, vecs = generalized_eigenpairs(G, K)
    lam = float(vals[0])
    c = vecs[:, 0]
    x, w = leggauss(check_x_order)
    x = a*x
    w = a*w
    Gu, Ku = operator_action(c, x, a=a, inner_order=check_inner_order)
    # Ga=P_a G P_a.  The trial vector is already mean-zero; project the output.
    mean_G = np.sum(w*Gu)/(2*a)
    Gap = Gu - mean_G
    r = Gap - lam*Ku
    nr = sqrt(float(np.sum(w*r*r)))
    nG = sqrt(float(np.sum(w*Gap*Gap)))
    nK = sqrt(float(np.sum(w*Ku*Ku)))
    denom = nG + abs(lam)*nK
    return {
        'lambda': lam,
        'residual_L2': nr,
        'relative_residual': nr/denom if denom else float('nan'),
        'norm_Gu': nG,
        'norm_Ku': nK,
        'mean_G_before_projection': float(mean_G),
    }


if __name__ == '__main__':
    print('Series calibration against direct Hurwitz-Lerch:')
    for row in series_calibration():
        print(row)
    print('\nDegree-10 parity/quadrature audit:')
    for row in refinement_audit():
        print(row)
    print('\nIndependent off-grid residual:')
    print(offgrid_residual())
