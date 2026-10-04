#!/usr/bin/env python3
"""Double-double evaluator for the source-faithful a=1, lambda=0 parity matrix.

Motivation
----------
The v14.005 frozen-P4 carrier survives at M3999/4000 with an O(1) complement
floor and 1e-15-class double complement solves, but binary64 assembly of the
protected reduction bottoms out at 1e-17--1e-16.  The physical capacity scalar
is much smaller.

This module evaluates the source-faithful operator with a two-float expansion
(roughly 30 decimal digits) while retaining the O(n^2) displacement-rank
matrix action.  It is intended for:
  * high-precision residual evaluation of only a handful of trial columns;
  * iterative refinement with the existing double complement solve;
  * high-precision 7x7 augmented-Schur formation.

The exact scalar sequences z_n and d_n are generated with mpmath.  The
archimedean diagonal is evaluated from the convergent Taylor series

  h_arch(t)
    = e^{-t/2}/(1-e^{-2t}) - 1/(2t)
    = sum_{r>=0} B_{r+1}(3/4) 2^r t^r/(r+1)!,

combined with exact endpoint recurrences for integrals of t^r sin(k t) and
t^r cos(k t), k=n*pi/2.  Modes 1 and 2 use direct high-precision quadrature.

The double-double arithmetic treats the frozen binary64 carrier/iterate
coefficients as exact dyadics.  This module does not by itself supply outward
rounding intervals; it is a high-precision midpoint/residual engine.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import mpmath as mp
import numpy as np


SPLIT = 134217729.0  # 2^27+1, Dekker split constant for binary64.
QS = (2, 3, 4, 5, 7)


def two_sum(a, b):
    s = a + b
    bb = s - a
    e = (a - (s - bb)) + (b - bb)
    return s, e


def two_prod(a, b):
    p = a * b
    ca = SPLIT * a
    ah = ca - (ca - a)
    al = a - ah
    cb = SPLIT * b
    bh = cb - (cb - b)
    bl = b - bh
    e = ((ah * bh - p) + ah * bl + al * bh) + al * bl
    return p, e


def dd_add(ah, al, bh, bl):
    s, e = two_sum(ah, bh)
    t = al + bl + e
    return two_sum(s, t)


def dd_sub(ah, al, bh, bl):
    return dd_add(ah, al, -bh, -bl)


def dd_mul_d(ah, al, b):
    p, e = two_prod(ah, b)
    e = e + al * b
    return two_sum(p, e)


def dd_mul(ah, al, bh, bl):
    p, e = two_prod(ah, bh)
    e = e + ah * bl + al * bh + al * bl
    return two_sum(p, e)


def dd_div_d(ah, al, b):
    q1 = ah / b
    ph, pl = two_prod(q1, b)
    rh, rl = dd_sub(ah, al, ph, pl)
    q2 = (rh + rl) / b
    return dd_add(q1, 0.0, q2, 0.0)


def split_mpf(x):
    hi = float(x)
    lo = float(x - mp.mpf(hi))
    return hi, lo


def dd_to_mpf(hi, lo):
    return mp.mpf(float(hi)) + mp.mpf(float(lo))


@dataclass
class DDParityData:
    modes: np.ndarray
    z_hi: np.ndarray
    z_lo: np.ndarray
    diag_hi: np.ndarray
    diag_lo: np.ndarray
    pole_hi: np.ndarray
    pole_lo: np.ndarray
    source_hi: np.ndarray
    source_lo: np.ndarray
    c_hi: float
    c_lo: float
    alpha: float


def arch_coefficients(rmax: int):
    x = mp.mpf(3) / 4
    return [
        mp.bernpoly(r + 1, x) * (mp.mpf(2) ** r) / mp.factorial(r + 1)
        for r in range(rmax + 1)
    ]


def arch_diag_series(n: int, coeffs):
    k = mp.mpf(n) * mp.pi / 2

    # Direct quadrature for the two lowest frequencies avoids recurrence
    # cancellation.  Only one such mode occurs in each parity sector.
    if n <= 2:
        def h(t):
            t = mp.mpf(t)
            if t == 0:
                return mp.mpf(1) / 4
            return mp.e**(-t / 2) / (1 - mp.e**(-2 * t)) - 1 / (2 * t)

        return mp.quad(
            lambda t: -h(t)
            * ((2 - t) * mp.cos(k * t) + mp.sin(k * t) / k),
            [0, 2],
        )

    rmax = len(coeffs) - 1
    eps = mp.mpf(-1 if n % 2 else 1)

    C = [mp.mpf(0)] * (rmax + 2)
    S = [mp.mpf(0)] * (rmax + 2)
    C[0] = 0
    S[0] = (1 - eps) / k

    for r in range(1, rmax + 2):
        C[r] = -mp.mpf(r) * S[r - 1] / k
        S[r] = -(mp.mpf(2) ** r) * eps / k + mp.mpf(r) * C[r - 1] / k

    return -mp.fsum(
        coeffs[r] * (2 * C[r] - C[r + 1] + S[r] / k)
        for r in range(rmax + 1)
    )


def hp_parity_data(
    modes,
    sector: str,
    dps: int = 120,
    arch_terms: int = 140,
    correction_terms: int = 40,
):
    modes = np.asarray(modes, dtype=int)

    with mp.workdps(dps):
        weights = (
            mp.log(2) / mp.sqrt(2),
            mp.log(3) / mp.sqrt(3),
            mp.log(2) / 2,
            mp.log(5) / mp.sqrt(5),
            mp.log(7) / mp.sqrt(7),
        )
        coeffs = arch_coefficients(arch_terms)
        c = 2 / mp.pi
        c_hi, c_lo = split_mpf(c)

        z_hi = np.empty(len(modes))
        z_lo = np.empty(len(modes))
        d_hi = np.empty(len(modes))
        d_lo = np.empty(len(modes))
        p_hi = np.empty(len(modes))
        p_lo = np.empty(len(modes))
        f_hi = np.empty(len(modes))
        f_lo = np.empty(len(modes))

        for i, nn in enumerate(modes):
            n = mp.mpf(int(nn))
            k = n * mp.pi / 2
            parity = mp.mpf(1 if int(nn) % 2 == 0 else -1)

            prime_sine = mp.fsum(
                w * mp.sin(n * mp.pi * mp.log(q) / 2)
                for q, w in zip(QS, weights)
            )

            corr = mp.fsum(
                mp.e**(-2 * (2 * j + mp.mpf("0.5")))
                / ((2 * j + mp.mpf("0.5")) ** 2 + k * k)
                for j in range(correction_terms)
            )

            z = (
                2 * prime_sine
                + mp.im(mp.digamma(mp.mpf("0.25") + 1j * n * mp.pi / 4))
                - parity * n * mp.pi * corr
            )

            cusp = (
                mp.log(n / 4)
                - mp.ci(n * mp.pi)
                - mp.si(n * mp.pi) / (n * mp.pi)
            )

            prime_diag = -mp.fsum(
                w
                * (
                    (2 - mp.log(q))
                    * mp.cos(n * mp.pi * mp.log(q) / 2)
                    + mp.sin(n * mp.pi * mp.log(q) / 2) / k
                )
                for q, w in zip(QS, weights)
            )

            arch = arch_diag_series(int(nn), coeffs)
            diag = cusp + prime_diag + arch

            if sector == "even-v":
                pole = 2 * k * mp.cosh(mp.mpf("0.5")) / (k * k + mp.mpf("0.25"))
                alpha = 2.0
            elif sector == "odd-v":
                pole = 2 * k * mp.sinh(mp.mpf("0.5")) / (k * k + mp.mpf("0.25"))
                alpha = -2.0
            else:
                raise ValueError(sector)

            sign = mp.mpf(-1 if int(nn) % 2 else 1)
            source = k * (mp.e**(-1) - sign * mp.e) / (1 + k * k)

            z_hi[i], z_lo[i] = split_mpf(z)
            d_hi[i], d_lo[i] = split_mpf(diag)
            p_hi[i], p_lo[i] = split_mpf(pole)
            f_hi[i], f_lo[i] = split_mpf(source)

        return DDParityData(
            modes=modes.copy(),
            z_hi=z_hi,
            z_lo=z_lo,
            diag_hi=d_hi,
            diag_lo=d_lo,
            pole_hi=p_hi,
            pole_lo=p_lo,
            source_hi=f_hi,
            source_lo=f_lo,
            c_hi=c_hi,
            c_lo=c_lo,
            alpha=alpha,
        )


def dd_column(data: DDParityData, j: int):
    modes = data.modes.astype(float)
    n = float(data.modes[j])

    t1h, t1l = dd_mul_d(data.z_hi, data.z_lo, n)
    t2h, t2l = dd_mul_d(data.z_hi[j], data.z_lo[j], modes)
    nh, nl = dd_sub(t1h, t1l, t2h, t2l)

    den = modes * modes - n * n
    safe_den = den.copy()
    safe_den[j] = 1.0

    qh, ql = dd_div_d(nh, nl, safe_den)
    ah, al = dd_mul(data.c_hi, data.c_lo, qh, ql)

    ph, pl = dd_mul(
        data.pole_hi,
        data.pole_lo,
        data.pole_hi[j],
        data.pole_lo[j],
    )
    ph, pl = dd_mul_d(ph, pl, data.alpha)
    ah, al = dd_add(ah, al, ph, pl)

    # Exact diagonal formula replaces the removable 0/0 off-diagonal form.
    p2h, p2l = dd_mul(
        data.pole_hi[j],
        data.pole_lo[j],
        data.pole_hi[j],
        data.pole_lo[j],
    )
    p2h, p2l = dd_mul_d(p2h, p2l, data.alpha)
    dh, dl = dd_add(
        data.diag_hi[j],
        data.diag_lo[j],
        p2h,
        p2l,
    )
    ah[j] = dh
    al[j] = dl
    return ah, al


def dd_matvec(data: DDParityData, X_hi, X_lo=None):
    X_hi = np.asarray(X_hi, dtype=float)
    one = X_hi.ndim == 1
    if one:
        X_hi = X_hi[:, None]

    if X_lo is None:
        X_lo = np.zeros_like(X_hi)
    else:
        X_lo = np.asarray(X_lo, dtype=float)
        if X_lo.ndim == 1:
            X_lo = X_lo[:, None]

    n, r = X_hi.shape
    if n != len(data.modes):
        raise ValueError("dimension mismatch")

    Yh = np.zeros((n, r), dtype=float)
    Yl = np.zeros((n, r), dtype=float)

    for j in range(n):
        ah, al = dd_column(data, j)

        # A[:,j] * X[j,:], including the low component of X.
        ph, pl = dd_mul(
            ah[:, None],
            al[:, None],
            X_hi[j, :][None, :],
            X_lo[j, :][None, :],
        )
        Yh, Yl = dd_add(Yh, Yl, ph, pl)

    return (Yh[:, 0], Yl[:, 0]) if one else (Yh, Yl)


def dd_dot_columns(X_hi, X_lo, Y_hi, Y_lo):
    X_hi = np.asarray(X_hi, dtype=float)
    Y_hi = np.asarray(Y_hi, dtype=float)
    if X_hi.ndim == 1:
        X_hi = X_hi[:, None]
    if Y_hi.ndim == 1:
        Y_hi = Y_hi[:, None]

    if X_lo is None:
        X_lo = np.zeros_like(X_hi)
    if Y_lo is None:
        Y_lo = np.zeros_like(Y_hi)

    rx = X_hi.shape[1]
    ry = Y_hi.shape[1]
    H = np.zeros((rx, ry), dtype=float)
    L = np.zeros((rx, ry), dtype=float)

    for i in range(X_hi.shape[0]):
        for a in range(rx):
            ph, pl = dd_mul(
                X_hi[i, a],
                X_lo[i, a],
                Y_hi[i, :],
                Y_lo[i, :],
            )
            H[a, :], L[a, :] = dd_add(H[a, :], L[a, :], ph, pl)
    return H, L


def dd_norm2(hi, lo):
    hi = np.asarray(hi, dtype=float).ravel()
    lo = np.asarray(lo, dtype=float).ravel()
    sh = 0.0
    sl = 0.0
    for i in range(len(hi)):
        ph, pl = dd_mul(hi[i], lo[i], hi[i], lo[i])
        sh, sl = dd_add(sh, sl, ph, pl)
    return math.sqrt(max(sh + sl, 0.0))


if __name__ == "__main__":
    print(
        "Library module: use suzuki_doubledouble_source_operator_validation.py "
        "for the fail-closed small-section validation."
    )
