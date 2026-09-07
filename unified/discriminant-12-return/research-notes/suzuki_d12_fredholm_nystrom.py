#!/usr/bin/env python3
"""Parity-reduced Nyström prototype for the D12 Suzuki Section-8 Fredholm system.

This module implements the exact half-interval reduction derived in ledger v13.283:

    -∫_0^a K_e(x,y) q_e(y) dy = cosh(x) + B,
    -∫_0^a K_o(x,y) q_o(y) dy = sinh(x) + A x,

where

    K_e(x,y) = k(x,y) + k(x,-y),
    K_o(x,y) = k(x,y) - k(x,-y).

The endpoint traces q_e(a)=0 and q_o(a)=0 are imposed explicitly.  In the odd
sector the x=0 collocation equation is identically 0=0, so it is replaced by
the parity condition q_o(0)=0.

The file deliberately keeps the archimedean reduced screw kernel as an injected
callable.  The Neumann kernel and the exact finite D12 prime-ramp contribution
are implemented here, so a later source-faithful archimedean kernel can be
plugged in without changing the discretization.

This is a research prototype, not a proof of the a→∞ Suzuki limit or GRH.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, log
from typing import Callable, Iterable, Sequence

import numpy as np
from numpy.polynomial.legendre import Legendre

Array = np.ndarray
Kernel = Callable[[Array, Array], Array]


def gauss_lobatto_legendre(n: int, a: float) -> tuple[Array, Array]:
    """Return n+1 Gauss-Lobatto-Legendre nodes/weights on [0,a].

    n is the polynomial degree, so there are n+1 nodes including both endpoints.
    """
    if n < 2:
        raise ValueError("n must be >= 2")
    if a <= 0:
        raise ValueError("a must be positive")

    Pn = Legendre.basis(n)
    interior = Pn.deriv().roots()
    x = np.concatenate(([-1.0], interior, [1.0]))
    px = Pn(x)
    w = 2.0 / (n * (n + 1) * px * px)

    # affine map [-1,1] -> [0,a]
    nodes = 0.5 * a * (x + 1.0)
    weights = 0.5 * a * w
    return nodes, weights


def neumann_kernel(a: float, x: Array, y: Array) -> Array:
    """Suzuki Section-8 kernel of (-Delta_N)^(-1) on the mean-zero subspace."""
    return (x * x + y * y) / (4.0 * a) - 0.5 * np.abs(x - y) + a / 6.0


def chi12(n: int) -> int:
    """Primitive real character modulo 12, extended by 0 off the unit classes."""
    r = n % 12
    if r in (1, 11):
        return 1
    if r in (5, 7):
        return -1
    return 0


def _primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    limit = int(n**0.5)
    for p in range(2, limit + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = False
    return np.flatnonzero(sieve).astype(int).tolist()


def d12_prime_powers(a: float, max_n: int = 2_000_000) -> list[tuple[int, float]]:
    """Return (n, b_K(n)/sqrt(n)) for prime powers n <= exp(2a).

    b_K(p^k) = log(p) * (1 + chi12(p)^k), with chi12(p)=0 at p=2,3.

    max_n is an explicit safety ceiling for exploratory numerics.  The exact
    finite prime horizon is floor(exp(2a)); if it exceeds max_n this function
    raises rather than silently truncating the arithmetic.
    """
    horizon = int(np.floor(exp(2.0 * a)))
    if horizon > max_n:
        raise ValueError(
            f"prime horizon exp(2a)={horizon} exceeds max_n={max_n}; "
            "raise max_n explicitly if the larger computation is intended"
        )

    data: list[tuple[int, float]] = []
    for p in _primes_up_to(horizon):
        cp = chi12(p)
        pk = p
        k = 1
        lp = log(p)
        while pk <= horizon:
            if cp == 0:
                b = lp
            else:
                b = lp * (1 + cp**k)
            if b != 0.0:
                data.append((pk, b / np.sqrt(pk)))
            if pk > horizon // p:
                break
            pk *= p
            k += 1
    data.sort(key=lambda item: item[0])
    return data


def prime_ramp_value(t: Array, prime_data: Sequence[tuple[int, float]]) -> Array:
    """Exact finite D12 prime-ramp screw contribution at difference t."""
    at = np.abs(t)
    out = np.zeros_like(at, dtype=float)
    for n, coeff in prime_data:
        out += coeff * np.maximum(at - log(n), 0.0)
    return out


def make_reduced_kernel(
    a: float,
    mu: float,
    arch_reduced: Callable[[Array], Array],
    prime_data: Sequence[tuple[int, float]],
) -> Kernel:
    """Build k_K(x,y)=g_red(x-y)-mu*N_a(x,y).

    arch_reduced(t) must contain the source-faithful reduced archimedean/pole
    screw contribution, excluding the conductor.  The conductor has already
    been absorbed into mu=lambda-log(12), as derived in v13.282.
    """

    def kernel(x: Array, y: Array) -> Array:
        t = x - y
        g = arch_reduced(t) + prime_ramp_value(t, prime_data)
        return g - mu * neumann_kernel(a, x, y)

    return kernel


def half_kernels(kernel: Kernel, x: Array, y: Array) -> tuple[Array, Array]:
    """Return parity-compressed kernels K_e and K_o on [0,a]."""
    kxy = kernel(x, y)
    kxmy = kernel(x, -y)
    return kxy + kxmy, kxy - kxmy


@dataclass
class ParitySolution:
    nodes: Array
    weights: Array
    q_even: Array
    q_odd: Array
    B: float
    A: float
    even_residual_inf: float
    odd_residual_inf: float
    even_condition: float
    odd_condition: float

    @property
    def q_plus(self) -> Array:
        return self.q_even + self.q_odd

    @property
    def q_minus_reflected_samples(self) -> Array:
        """Samples of q_-(x)=q_+(-x) on x>=0: q_e(x)-q_o(x)."""
        return self.q_even - self.q_odd


def solve_parity_nystrom(
    kernel: Kernel,
    a: float,
    degree: int = 48,
    rcond: float | None = None,
) -> ParitySolution:
    """Solve the two augmented parity systems using GLL Nyström collocation.

    Even unknowns: q_e at all GLL nodes plus B.
      Collocate at every node and append q_e(a)=0.

    Odd unknowns: q_o at all GLL nodes plus A.
      The x=0 integral equation is exactly 0=0, so collocate only at nodes i>=1,
      append q_o(0)=0 and q_o(a)=0.

    np.linalg.lstsq is used intentionally because first-kind Fredholm systems are
    often ill-conditioned.  Singular values/condition numbers should be tracked
    as part of every convergence study.
    """
    x, w = gauss_lobatto_legendre(degree, a)
    m = len(x)

    X = x[:, None]
    Y = x[None, :]
    Ke, Ko = half_kernels(kernel, X, Y)

    # Even: m collocation equations + one endpoint equation; m q-values + B.
    Me = np.zeros((m + 1, m + 1), dtype=float)
    be = np.zeros(m + 1, dtype=float)
    Me[:m, :m] = -Ke * w[None, :]
    Me[:m, m] = -1.0
    be[:m] = np.cosh(x)
    Me[m, m - 1] = 1.0  # q_e(a)=0

    se = np.linalg.svd(Me, compute_uv=False)
    cond_e = np.inf if se[-1] == 0 else float(se[0] / se[-1])
    ue, *_ = np.linalg.lstsq(Me, be, rcond=rcond)
    qe = ue[:m]
    B = float(ue[m])
    re = Me @ ue - be

    # Odd: (m-1) nontrivial collocation equations + q_o(0)=q_o(a)=0.
    # Unknowns: m q-values + A -> m+1 total equations/unknowns.
    Mo = np.zeros((m + 1, m + 1), dtype=float)
    bo = np.zeros(m + 1, dtype=float)
    Mo[: m - 1, :m] = -Ko[1:, :] * w[None, :]
    Mo[: m - 1, m] = -x[1:]
    bo[: m - 1] = np.sinh(x[1:])
    Mo[m - 1, 0] = 1.0  # q_o(0)=0
    Mo[m, m - 1] = 1.0  # q_o(a)=0

    so = np.linalg.svd(Mo, compute_uv=False)
    cond_o = np.inf if so[-1] == 0 else float(so[0] / so[-1])
    uo, *_ = np.linalg.lstsq(Mo, bo, rcond=rcond)
    qo = uo[:m]
    A = float(uo[m])
    ro = Mo @ uo - bo

    return ParitySolution(
        nodes=x,
        weights=w,
        q_even=qe,
        q_odd=qo,
        B=B,
        A=A,
        even_residual_inf=float(np.linalg.norm(re, ord=np.inf)),
        odd_residual_inf=float(np.linalg.norm(ro, ord=np.inf)),
        even_condition=cond_e,
        odd_condition=cond_o,
    )


def characteristic_raw(solution: ParitySolution, z: complex, theta: float = np.pi) -> complex:
    """Quadrature approximation to the raw finite Suzuki characteristic.

    Reconstruct the full-interval Fourier transforms from parity on [0,a]:

      F_+(z) = 2∫_0^a [q_e(x) cos(zx) + i q_o(x) sin(zx)] dx,
      F_-(z) = F_+(-z) for the canonical real reflected basis.
    """
    x = solution.nodes
    w = solution.weights
    qe = solution.q_even
    qo = solution.q_odd

    Fp = 2.0 * np.sum(w * (qe * np.cos(z * x) + 1j * qo * np.sin(z * x)))
    Fm = 2.0 * np.sum(w * (qe * np.cos(z * x) - 1j * qo * np.sin(z * x)))
    return (z - 1j) * Fp + np.exp(1j * theta) * (z + 1j) * Fm


def normalized_characteristic(
    solution: ParitySolution,
    z: complex,
    z_ref: complex,
    theta: float = np.pi,
) -> complex:
    """Normalization-free characteristic ratio W(z)/W(z_ref)."""
    den = characteristic_raw(solution, z_ref, theta=theta)
    if den == 0:
        raise ZeroDivisionError("reference characteristic is zero")
    return characteristic_raw(solution, z, theta=theta) / den


def zero_arch_reduced(t: Array) -> Array:
    """Structural-test placeholder; NOT the physical D12 archimedean kernel."""
    return np.zeros_like(t, dtype=float)


if __name__ == "__main__":
    # Structural smoke test only.  It checks assembly/parity numerics for a
    # prime+Neumann toy kernel; it is not a D12 spectral computation because the
    # reduced archimedean kernel is intentionally omitted here.
    a = 2.0
    mu = -4.0
    pdata = d12_prime_powers(a, max_n=100_000)
    k = make_reduced_kernel(a, mu, zero_arch_reduced, pdata)
    sol = solve_parity_nystrom(k, a, degree=24)

    print(f"prime powers used: {len(pdata)}")
    print(f"even residual inf: {sol.even_residual_inf:.3e}")
    print(f"odd residual inf:  {sol.odd_residual_inf:.3e}")
    print(f"even cond: {sol.even_condition:.3e}")
    print(f"odd cond:  {sol.odd_condition:.3e}")
    print(f"q_e(a): {sol.q_even[-1]:+.3e}")
    print(f"q_o(0), q_o(a): {sol.q_odd[0]:+.3e}, {sol.q_odd[-1]:+.3e}")
