#!/usr/bin/env python3
"""Neumann-eigenbasis preconditioning audit for Suzuki v2 equation (8.7).

This is the v13.289 follow-up to the parity/quadrature audit.  It removes the
numerically assembled compact denominator K_a=(-Delta_N)^(-1) by working in its
exact eigenbasis on L^2_0(-a,a).  In that basis

    K_a phi_n = mu_n^{-1} phi_n,
    mu_n = (n*pi/(2a))^2,  n>=1,

and the generalized problem G c = lambda K c is converted exactly to

    A y = lambda y,   A = K^{-1/2} G K^{-1/2}.

The same matrix is also assembled independently as Suzuki's direct quadratic
form <G_a Dv,Dv> on the normalized Dirichlet sine basis.  Agreement of those
two constructions is an implementation invariant.

For a=1 the fast screw-kernel evaluator and exact breakpoint geometry are
imported from the v13.288 audit.  This remains a numerical audit, not a proof of
RH and not a certification of lambda<lambda_a.
"""
from __future__ import annotations

from math import pi, sqrt
import numpy as np
from numpy.polynomial.legendre import leggauss

from suzuki_generalized_eigenvalue_parity_audit import (
    g_fast,
    outer_breakpoints,
    riemann_prime_powers,
    row_breakpoints,
)

Array = np.ndarray


def frequencies(modes: int, a: float = 1.0) -> Array:
    n = np.arange(1, modes + 1, dtype=float)
    return n*pi/(2.0*a)


def neumann_basis_values(modes: int, x: Array | float, a: float = 1.0) -> Array:
    """Normalized nonconstant Neumann eigenfunctions on [-a,a]."""
    x = np.asarray(x, dtype=float)
    k = frequencies(modes, a)
    if x.ndim == 0:
        return np.cos(k*(float(x)+a))/sqrt(a)
    return np.cos(np.outer(x+a, k))/sqrt(a)


def dirichlet_derivative_values(modes: int, x: Array | float, a: float = 1.0) -> Array:
    """Derivatives of normalized Dirichlet sine modes.

    psi_n(x)=a^{-1/2} sin(k_n(x+a)), so psi'_n=k_n phi_n.
    The factor i in D=i d/dx cancels in the Hermitian quadratic form.
    """
    vals = neumann_basis_values(modes, x, a)
    k = frequencies(modes, a)
    return vals*k if vals.ndim == 1 else vals*k[None, :]


def assemble_g_matrix(
    modes: int,
    a: float = 1.0,
    outer_order: int = 23,
    inner_order: int = 24,
    derivative_basis: bool = False,
) -> Array:
    """Assemble <basis_m,G basis_n> with exact row-wise breakpoints."""
    prime_data = riemann_prime_powers(2.0*a)
    G = np.zeros((modes, modes), dtype=float)
    xo, wo = leggauss(outer_order)
    yi, wi = leggauss(inner_order)
    basis = dirichlet_derivative_values if derivative_basis else neumann_basis_values

    obp = outer_breakpoints(a, prime_data)
    for xl, xr in zip(obp[:-1], obp[1:]):
        xs = 0.5*(xr-xl)*xo + 0.5*(xr+xl)
        wx = 0.5*(xr-xl)*wo
        for x, w_x in zip(xs, wx):
            px = basis(modes, float(x), a)
            row = np.zeros(modes, dtype=float)
            rbp = row_breakpoints(float(x), a, prime_data)
            for yl, yr in zip(rbp[:-1], rbp[1:]):
                ys = 0.5*(yr-yl)*yi + 0.5*(yr+yl)
                wy = 0.5*(yr-yl)*wi
                py = basis(modes, ys, a)
                gv = np.asarray([g_fast(float(x-y), prime_data) for y in ys])
                row += (wy*gv) @ py
            G += w_x*np.outer(px, row)
    return 0.5*(G+G.T)


def preconditioned_matrix(G_neumann: Array, a: float = 1.0) -> Array:
    k = frequencies(len(G_neumann), a)
    A = k[:, None]*G_neumann*k[None, :]
    return 0.5*(A+A.T)


def parity_indices(modes: int, parity: str) -> list[int]:
    # n odd -> odd function; n even -> even function under x -> -x.
    if parity == 'odd':
        return [j for j in range(modes) if (j+1) % 2 == 1]
    if parity == 'even':
        return [j for j in range(modes) if (j+1) % 2 == 0]
    raise ValueError("parity must be 'odd' or 'even'")


def sector_minimum(A: Array, parity: str) -> float:
    idx = parity_indices(len(A), parity)
    return float(np.linalg.eigvalsh(A[np.ix_(idx, idx)])[0])


def direct_form_crosscheck(
    modes: int = 10,
    a: float = 1.0,
    outer_order: int = 23,
    inner_order: int = 24,
) -> dict:
    G = assemble_g_matrix(modes, a, outer_order, inner_order, derivative_basis=False)
    A_pre = preconditioned_matrix(G, a)
    A_direct = assemble_g_matrix(modes, a, outer_order, inner_order, derivative_basis=True)
    diff = A_pre-A_direct
    scale = max(np.linalg.norm(A_direct, ord=np.inf), 1.0)
    return {
        'modes': modes,
        'outer_order': outer_order,
        'inner_order': inner_order,
        'abs_inf_difference': float(np.linalg.norm(diff, ord=np.inf)),
        'relative_inf_difference': float(np.linalg.norm(diff, ord=np.inf)/scale),
    }


def quadrature_audit(
    modes: int = 10,
    a: float = 1.0,
    quadratures=((7,8),(11,12),(15,16),(23,24),(31,32),(39,40),(47,48)),
) -> list[dict]:
    rows = []
    for outer_order, inner_order in quadratures:
        G = assemble_g_matrix(modes, a, outer_order, inner_order, derivative_basis=False)
        A = preconditioned_matrix(G, a)
        ev = np.linalg.eigvalsh(A)
        rows.append({
            'outer_order': outer_order,
            'inner_order': inner_order,
            'lowest': float(ev[0]),
            'odd_min': sector_minimum(A, 'odd'),
            'even_min': sector_minimum(A, 'even'),
            'first_eigenvalues': [float(x) for x in ev[:min(5, len(ev))]],
        })
    return rows


def mode_audit(
    max_modes: int = 14,
    a: float = 1.0,
    outer_order: int = 47,
    inner_order: int = 48,
    mode_counts=(4,6,8,10,12,14),
) -> list[dict]:
    G = assemble_g_matrix(max_modes, a, outer_order, inner_order, derivative_basis=False)
    rows = []
    for modes in mode_counts:
        A = preconditioned_matrix(G[:modes, :modes], a)
        ev = np.linalg.eigvalsh(A)
        rows.append({
            'modes': modes,
            'lowest': float(ev[0]),
            'odd_min': sector_minimum(A, 'odd'),
            'even_min': sector_minimum(A, 'even'),
            'first_eigenvalues': [float(x) for x in ev[:min(4, len(ev))]],
        })
    return rows


if __name__ == '__main__':
    print('Neumann-basis preconditioning / direct-form cross-check')
    print(direct_form_crosscheck())
    print('\nQuadrature refinement at 10 modes:')
    for row in quadrature_audit():
        print(row)
    print('\nMode-count refinement at 47x48 quadrature:')
    for row in mode_audit():
        print(row)
