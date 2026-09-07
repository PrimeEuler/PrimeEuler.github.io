#!/usr/bin/env python3
"""Near-null Ritz-vector convergence audit for Suzuki's a=1 quadratic form.

This v13.292 follow-up asks whether the very small positive Ritz values found in
v13.291 come from vectors converging toward a genuine element of ker(G_a), or
from escape into increasingly oscillatory / boundary-localized directions.

The finite matrix is assembled at arbitrary precision through the componentwise
1-D representation from v13.291.  The lowest Ritz vector v_M is then tracked
across nested Dirichlet spaces.  Diagnostics include embedded overlaps, the
corresponding u_M=Dv_M coefficients, spectral centroid/tail mass, boundary and
central L2 mass, and an independent breakpoint-aware off-grid evaluation of
P_a G_a u_M.

This remains a numerical audit.  Convergence of these diagnostics is evidence
for a kernel candidate, not a proof that ker(G_a) is nontrivial and not an RH
or GRH result.
"""
from __future__ import annotations

from math import pi, sqrt
import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss

from suzuki_componentwise_high_precision_audit import component_matrices_mp
from suzuki_generalized_eigenvalue_parity_audit import (
    g_fast,
    riemann_prime_powers,
    row_breakpoints,
)


def lowest_vector_mp(modes: int, a: float = 1.0, dps: int = 40):
    """Return lowest eigenvalue and L2-normalized Dirichlet coefficient vector."""
    with mp.workdps(dps):
        P, R, H = component_matrices_mp(modes, a, dps)
        A = P + R + H
        vals, Q = mp.eigsy(A)
        c = np.asarray([float(Q[j, 0]) for j in range(modes)], dtype=float)
        c /= np.linalg.norm(c)
        # Deterministic sign convention.
        if c[np.argmax(np.abs(c))] < 0:
            c = -c
        return mp.nstr(vals[0], 20), c


def k_values(modes: int, a: float = 1.0) -> np.ndarray:
    n = np.arange(1, modes + 1, dtype=float)
    return n*pi/(2*a)


def u_coefficients(c: np.ndarray, a: float = 1.0) -> np.ndarray:
    """Neumann coefficients of u=Dv, ignoring the harmless phase i."""
    return k_values(len(c), a) * c


def embedded_overlap(c_small: np.ndarray, c_large: np.ndarray) -> float:
    emb = np.zeros_like(c_large)
    emb[:len(c_small)] = c_small
    return float(abs(np.dot(emb, c_large)))


def normalized_u_overlap(c_small: np.ndarray, c_large: np.ndarray, a: float = 1.0) -> float:
    u1 = u_coefficients(c_small, a)
    u2 = u_coefficients(c_large, a)
    u1 /= np.linalg.norm(u1)
    u2 /= np.linalg.norm(u2)
    emb = np.zeros_like(u2)
    emb[:len(u1)] = u1
    return float(abs(np.dot(emb, u2)))


def spatial_metrics(c: np.ndarray, a: float = 1.0, grid: int = 20001) -> dict:
    """L2 mass and frequency diagnostics for normalized v."""
    modes = len(c)
    n = np.arange(1, modes + 1, dtype=float)
    k = k_values(modes, a)
    x = np.linspace(-a, a, grid)
    psi = np.sin(np.outer(x + a, k)) / sqrt(a)
    v = psi @ c
    norm = float(np.trapezoid(v*v, x))

    left = x <= -0.8*a
    right = x >= 0.8*a
    boundary = float(np.trapezoid(v[left]**2, x[left]) + np.trapezoid(v[right]**2, x[right])) / norm
    center_mask = np.abs(x) <= 0.2*a
    center = float(np.trapezoid(v[center_mask]**2, x[center_mask])) / norm

    tail2 = float(np.sum(c[max(0, modes-2):]**2))
    tail4 = float(np.sum(c[max(0, modes-4):]**2))
    centroid = float(np.sum(n*c*c))
    u_norm = float(np.linalg.norm(u_coefficients(c, a)))
    return {
        'spectral_centroid_n': centroid,
        'top2_mode_mass': tail2,
        'top4_mode_mass': tail4,
        'boundary_mass_absx_gt_0.8a': boundary,
        'central_mass_absx_lt_0.2a': center,
        'u_L2_norm': u_norm,
    }


def offgrid_kernel_residual(c: np.ndarray, a: float = 1.0,
                            x_order: int = 64, inner_order: int = 64) -> dict:
    """Independent L2 norm of P_a G_a u on Gauss x nodes.

    The y integration uses the original source kernel g_fast and row-dependent
    prime-power breakpoints, not the 1-D Ritz matrix.  The reported normalized
    residual is ||P_a G_a u||_2 / ||u||_2.  If v approaches a genuine lambda=0
    state, this quantity should tend to zero.
    """
    modes = len(c)
    prime_data = riemann_prime_powers(2*a)
    xi, wi = leggauss(x_order)
    yi, wy0 = leggauss(inner_order)
    xs = a*xi
    wx = a*wi
    k = k_values(modes, a)
    uc = k*c

    Gu = np.zeros_like(xs)
    for ix, x in enumerate(xs):
        total = 0.0
        rbp = row_breakpoints(float(x), a, prime_data)
        for yl, yr in zip(rbp[:-1], rbp[1:]):
            ys = 0.5*(yr-yl)*yi + 0.5*(yr+yl)
            wy = 0.5*(yr-yl)*wy0
            phi = np.cos(np.outer(ys+a, k))/sqrt(a)
            uvals = phi @ uc
            gv = np.asarray([g_fast(float(x-y), prime_data) for y in ys])
            total += float(np.sum(wy*gv*uvals))
        Gu[ix] = total

    mean_G = float(np.sum(wx*Gu)/(2*a))
    Gap = Gu - mean_G
    gnorm = sqrt(float(np.sum(wx*Gap*Gap)))
    unorm = float(np.linalg.norm(uc))
    return {
        'PGau_L2': gnorm,
        'u_L2': unorm,
        'normalized_PGau': gnorm/unorm,
        'mean_G_before_projection': mean_G,
    }


def sequence(mode_counts=(6,8,10,12), a: float = 1.0, dps: int = 40):
    rows = []
    vectors = {}
    for modes in mode_counts:
        lam, c = lowest_vector_mp(modes, a=a, dps=dps)
        vectors[modes] = c
        row = {'modes': modes, 'ritz_value': lam}
        row.update(spatial_metrics(c, a))
        row.update(offgrid_kernel_residual(c, a))
        rows.append(row)

    overlaps = []
    for m0, m1 in zip(mode_counts[:-1], mode_counts[1:]):
        overlaps.append({
            'from_modes': m0,
            'to_modes': m1,
            'v_embedded_overlap': embedded_overlap(vectors[m0], vectors[m1]),
            'u_embedded_overlap': normalized_u_overlap(vectors[m0], vectors[m1], a),
            'new_v_tail_norm': float(np.linalg.norm(vectors[m1][m0:])),
        })
    return rows, overlaps


if __name__ == '__main__':
    print('Suzuki v13.292 near-null Ritz-vector audit')
    rows, overlaps = sequence()
    for row in rows:
        print(row)
    print('nested-space overlaps:')
    for row in overlaps:
        print(row)
