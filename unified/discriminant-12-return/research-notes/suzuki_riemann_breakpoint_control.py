#!/usr/bin/env python3
"""Breakpoint-aware Riemann control solve for Suzuki Section 8.

This is the source-faithful control experiment for the D12 Fredholm program.
It couples Suzuki's exact Riemann screw function from equation (1.3) to the
parity-reduced first-kind Fredholm system, but replaces the global Nyström rule
by row-wise product integration split at every analytically known kink:

  y = x,  y = x +/- log(p^k),  y = log(p^k) - x.

The unknown q_e and q_o are represented by their values at Legendre-Gauss-
Lobatto interpolation nodes on [0,a].  On each row-specific segment, Gauss-
Legendre quadrature integrates the kernel times the barycentric Lagrange basis.

This file is a numerical research control, not a proof of RH and not yet a D12
numerical computation.  The parameter lambda must satisfy lambda < lambda_a in
Suzuki's operator construction; exploratory runs that do not certify that
inequality must be labelled as formal Fredholm smoke tests only.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import cosh, log, pi, sinh
from typing import Sequence

import numpy as np
from numpy.polynomial.legendre import Legendre, leggauss

from suzuki_riemann_screw_calibration import (
    archimedean_term,
    pole_term,
    riemann_prime_powers,
)

Array = np.ndarray


def lobatto_nodes(degree: int, a: float) -> Array:
    if degree < 2:
        raise ValueError("degree must be >= 2")
    if a <= 0:
        raise ValueError("a must be positive")
    P = Legendre.basis(degree)
    t = np.concatenate(([-1.0], P.deriv().roots(), [1.0]))
    return 0.5 * a * (t + 1.0)


def barycentric_weights(nodes: Array) -> Array:
    """Direct barycentric weights; adequate for the low/moderate control degrees."""
    m = len(nodes)
    w = np.ones(m, dtype=float)
    for j in range(m):
        w[j] = 1.0 / np.prod(nodes[j] - np.delete(nodes, j))
    w /= np.max(np.abs(w))
    return w


def lagrange_values(nodes: Array, bary: Array, y: Array) -> Array:
    """Matrix L[r,j]=ell_j(y_r) for the nodal interpolation basis."""
    y = np.asarray(y, dtype=float)
    D = y[:, None] - nodes[None, :]
    L = np.empty_like(D)
    close = np.isclose(D, 0.0, rtol=0.0, atol=1e-14)
    for r in range(len(y)):
        if np.any(close[r]):
            L[r] = 0.0
            L[r, int(np.argmax(close[r]))] = 1.0
        else:
            tmp = bary / D[r]
            L[r] = tmp / np.sum(tmp)
    return L


def neumann_kernel(a: float, x: float, y: Array | float) -> Array:
    y = np.asarray(y, dtype=float)
    return (x * x + y * y) / (4.0 * a) - 0.5 * np.abs(x - y) + a / 6.0


def prime_ramp_with_data(t: float, prime_data: Sequence[tuple[int, float]]) -> float:
    T = abs(float(t))
    return sum(c * max(T - log(n), 0.0) for n, c in prime_data)


def g_with_data(t: float, prime_data: Sequence[tuple[int, float]], dps: int) -> float:
    """Suzuki (1.3), reusing one finite prime-power table for |t|<=2a."""
    return (
        pole_term(t)
        + prime_ramp_with_data(t, prime_data)
        + archimedean_term(t, dps=dps)
    )


def row_breakpoints(x: float, a: float, prime_data: Sequence[tuple[int, float]]) -> list[float]:
    """All kernel nonsmooth points in y for the parity-compressed row at x."""
    pts = {0.0, float(a)}
    if 0.0 < x < a:
        pts.add(float(x))  # |x-y|=0, including the |t| log |t| cusp
    for n, _ in prime_data:
        ell = log(n)
        # g(x-y): |x-y|=ell;  g(x+y): x+y=ell on x,y>=0.
        for y in (x - ell, x + ell, ell - x):
            if 1e-14 < y < a - 1e-14:
                pts.add(float(y))
    return sorted(pts)


def parity_row(
    x: float,
    parity: str,
    nodes: Array,
    bary: Array,
    a: float,
    lam: float,
    prime_data: Sequence[tuple[int, float]],
    quad_order: int,
    dps: int,
) -> Array:
    """Return coefficients of -integral K_{e/o}(x,y) q(y) dy in the nodal basis."""
    if parity not in ("even", "odd"):
        raise ValueError("parity must be 'even' or 'odd'")
    gx, gw = leggauss(quad_order)
    coeff = np.zeros(len(nodes), dtype=float)
    bp = row_breakpoints(x, a, prime_data)

    for left, right in zip(bp[:-1], bp[1:]):
        if right <= left:
            continue
        y = 0.5 * (right - left) * gx + 0.5 * (right + left)
        w = 0.5 * (right - left) * gw
        L = lagrange_values(nodes, bary, y)
        kval = np.empty_like(y)
        for r, yy in enumerate(y):
            kxy = g_with_data(x - yy, prime_data, dps) - lam * neumann_kernel(a, x, yy)
            kxmy = g_with_data(x + yy, prime_data, dps) - lam * neumann_kernel(a, x, -yy)
            kval[r] = kxy + kxmy if parity == "even" else kxy - kxmy
        coeff += -(w * kval) @ L
    return coeff


@dataclass
class ControlSolution:
    a: float
    lam: float
    degree: int
    quad_order: int
    nodes: Array
    q_even: Array
    q_odd: Array
    B: float
    A: float
    cond_even: float
    cond_odd: float
    residual_even_inf: float
    residual_odd_inf: float


def solve_control(
    a: float = 1.0,
    lam: float = -5.0,
    degree: int = 8,
    quad_order: int = 6,
    dps: int = 25,
    rcond: float | None = None,
) -> ControlSolution:
    """Solve the parity-reduced formal Fredholm equations with product integration."""
    nodes = lobatto_nodes(degree, a)
    bary = barycentric_weights(nodes)
    m = len(nodes)
    prime_data = riemann_prime_powers(2.0 * a)

    Me = np.zeros((m + 1, m + 1), dtype=float)
    be = np.zeros(m + 1, dtype=float)
    for i, x in enumerate(nodes):
        Me[i, :m] = parity_row(
            float(x), "even", nodes, bary, a, lam, prime_data, quad_order, dps
        )
        Me[i, m] = -1.0
        be[i] = cosh(float(x))
    Me[m, m - 1] = 1.0  # q_e(a)=0

    Mo = np.zeros((m + 1, m + 1), dtype=float)
    bo = np.zeros(m + 1, dtype=float)
    row = 0
    for i in range(1, m):
        x = float(nodes[i])
        Mo[row, :m] = parity_row(
            x, "odd", nodes, bary, a, lam, prime_data, quad_order, dps
        )
        Mo[row, m] = -x
        bo[row] = sinh(x)
        row += 1
    Mo[row, 0] = 1.0  # q_o(0)=0
    row += 1
    Mo[row, m - 1] = 1.0  # q_o(a)=0

    ue, *_ = np.linalg.lstsq(Me, be, rcond=rcond)
    uo, *_ = np.linalg.lstsq(Mo, bo, rcond=rcond)
    return ControlSolution(
        a=a,
        lam=lam,
        degree=degree,
        quad_order=quad_order,
        nodes=nodes,
        q_even=ue[:m],
        q_odd=uo[:m],
        B=float(ue[m]),
        A=float(uo[m]),
        cond_even=float(np.linalg.cond(Me)),
        cond_odd=float(np.linalg.cond(Mo)),
        residual_even_inf=float(np.linalg.norm(Me @ ue - be, ord=np.inf)),
        residual_odd_inf=float(np.linalg.norm(Mo @ uo - bo, ord=np.inf)),
    )


def interpolate(solution: ControlSolution, values: Array, y: Array) -> Array:
    bary = barycentric_weights(solution.nodes)
    return lagrange_values(solution.nodes, bary, np.asarray(y, dtype=float)) @ values


def characteristic_raw(
    solution: ControlSolution,
    z: complex,
    theta: float = pi,
    quad_order: int = 80,
) -> complex:
    """Compute W_raw from the interpolated parity solution on [0,a]."""
    gx, gw = leggauss(quad_order)
    y = 0.5 * solution.a * (gx + 1.0)
    w = 0.5 * solution.a * gw
    qe = interpolate(solution, solution.q_even, y)
    qo = interpolate(solution, solution.q_odd, y)
    Fp = 2.0 * np.sum(w * (qe * np.cos(z * y) + 1j * qo * np.sin(z * y)))
    Fm = 2.0 * np.sum(w * (qe * np.cos(z * y) - 1j * qo * np.sin(z * y)))
    return (z - 1j) * Fp + np.exp(1j * theta) * (z + 1j) * Fm


def characteristic_ratio(
    solution: ControlSolution,
    z: complex,
    z_ref: complex,
    theta: float = pi,
) -> complex:
    den = characteristic_raw(solution, z_ref, theta=theta)
    if den == 0:
        raise ZeroDivisionError("reference characteristic vanishes")
    return characteristic_raw(solution, z, theta=theta) / den


def convergence_study(
    degrees=(4, 6, 8, 10),
    a: float = 1.0,
    lam: float = -5.0,
    quad_order: int = 6,
    dps: int = 25,
    z: complex = 1.0,
    z_ref: complex = 0.5,
) -> list[dict]:
    """Low-degree smoke study; lambda<lambda_a is not certified by this routine."""
    rows = []
    for degree in degrees:
        sol = solve_control(a, lam, degree, quad_order, dps)
        ratio = characteristic_ratio(sol, z, z_ref)
        rows.append(
            {
                "degree": degree,
                "cond_even": sol.cond_even,
                "cond_odd": sol.cond_odd,
                "res_even_inf": sol.residual_even_inf,
                "res_odd_inf": sol.residual_odd_inf,
                "A": sol.A,
                "B": sol.B,
                "W_ratio": ratio,
            }
        )
    return rows


if __name__ == "__main__":
    print("Suzuki Riemann breakpoint-aware formal Fredholm control")
    print("WARNING: default lambda=-5 is an exploratory value; lambda<lambda_a is not certified here.")
    for row in convergence_study():
        print(row)
