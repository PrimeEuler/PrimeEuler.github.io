#!/usr/bin/env python3
"""Breakpoint-aware Galerkin control for Suzuki v2 equation (8.7).

Computes Ritz values for

    G_a u = lambda K_a u,   u in L^2_0(-a,a),

where G_a has kernel g_zeta(x-y) and K_a=(-Delta_N)^(-1) has Suzuki's
continuous Neumann kernel.  The polynomial trial space is spanned by
P_1(x/a),...,P_d(x/a), so the mean-zero constraint is exact.  Inner and outer
quadrature are split at all analytically known prime-power/cusp transitions.

The lowest Ritz value is an UPPER bound on the true bottom lambda_a.  Therefore
this routine estimates lambda_a from above; it does NOT certify that a chosen
lambda is below lambda_a.  It is a numerical research control, not an RH proof.
"""
from __future__ import annotations

from math import log
import numpy as np
from numpy.polynomial.legendre import Legendre, leggauss

from suzuki_riemann_screw_calibration import (
    archimedean_term,
    pole_term,
    riemann_prime_powers,
)

Array = np.ndarray


def neumann_kernel(a: float, x: float, y: float) -> float:
    return (x*x + y*y)/(4.0*a) - 0.5*abs(x-y) + a/6.0


def g_with_data(t: float, prime_data, dps: int) -> float:
    T = abs(float(t))
    ramp = sum(c*max(T-log(n), 0.0) for n, c in prime_data)
    return pole_term(t) + ramp + archimedean_term(t, dps=dps)


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
    # Values of x where an inner prime breakpoint enters/leaves [-a,a].
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
    dps: int = 25,
) -> tuple[Array, Array]:
    """Return symmetric Galerkin matrices (G,K) on the exact mean-zero space."""
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
                gv = np.asarray([g_with_data(float(x-y), prime_data, dps) for y in ys])
                kv = np.asarray([neumann_kernel(a, float(x), float(y)) for y in ys])
                rg += (wy*gv) @ py
                rk += (wy*kv) @ py
            G += w_x*np.outer(px, rg)
            K += w_x*np.outer(px, rk)

    # Roundoff/product-integration asymmetry is not part of the self-adjoint problem.
    return 0.5*(G+G.T), 0.5*(K+K.T)


def generalized_eigenvalues(G: Array, K: Array) -> Array:
    """Solve symmetric G c=lambda K c using a Cholesky reduction."""
    L = np.linalg.cholesky(K)
    X = np.linalg.solve(L, G)
    A = np.linalg.solve(L, X.T).T  # L^{-1} G L^{-T}
    A = 0.5*(A+A.T)
    return np.linalg.eigvalsh(A)


def ritz_study(
    degrees=(4, 6, 8, 10),
    a: float = 1.0,
    outer_order: int = 7,
    inner_order: int = 8,
    dps: int = 25,
) -> list[dict]:
    rows = []
    for degree in degrees:
        G, K = galerkin_matrices(degree, a, outer_order, inner_order, dps)
        ev = generalized_eigenvalues(G, K)
        rows.append({
            "degree": degree,
            "lambda_ritz_min": float(ev[0]),
            "first_eigenvalues": [float(x) for x in ev[:min(5, len(ev))]],
            "cond_K": float(np.linalg.cond(K)),
            "sym_G_inf": float(np.linalg.norm(G-G.T, ord=np.inf)),
            "sym_K_inf": float(np.linalg.norm(K-K.T, ord=np.inf)),
        })
    return rows


if __name__ == "__main__":
    print("Suzuki v2 generalized-eigenvalue Ritz control, equation (8.7)")
    print("CAUTION: lambda_ritz_min is an upper bound on lambda_a, not a lower bound.")
    for row in ritz_study():
        print(row)
