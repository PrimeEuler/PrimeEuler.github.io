#!/usr/bin/env python3
"""Fixed-a Xi scalar phase-window diagnostic for the source-faithful form core.

This reproduces the numerical checks recorded in ledger v13.967.

Scope:
  * a = 1, absolute Suzuki shift lambda = 0.
  * Uses the corrected source-faithful parity matrices from v13.800.
  * Solves the two parity source problems once.
  * Reconstructs the truncated one-source transform F_N(t).
  * Forms the two fixed boundary characteristics
        W_0  = (t-i)F(t) + (t+i)F(-t),
        W_pi = (t-i)F(t) - (t+i)F(-t).
  * Scans their real roots and evaluates the sign-phase moment.

This is a finite-section diagnostic.  A truncated Fourier transform need not
itself generate an exact Herglotz Weyl function, so the numerical sign-phase
integral is NOT a rigorous spectral-shift certificate for the exact operator.
The exact certification theorem and its uncertain-window budget are proved in
the ledger entry.
"""
from __future__ import annotations

import argparse
import math

import mpmath as mp
import numpy as np

from suzuki_form_core_corrected_fast_cutoff import even_v_block, odd_v_block
from suzuki_form_core_schur_parameter_diagnostic import source_overlap


def solve_coefficients(max_mode: int, dps: int):
    with mp.workdps(dps):
        ns_e, A_e = even_v_block(max_mode)
        ns_o, A_o = odd_v_block(max_mode)

        f_e = mp.matrix([source_overlap(n, mp.mpf(1), mp.mpf(1)) for n in ns_e])
        f_o = mp.matrix([source_overlap(n, mp.mpf(1), mp.mpf(1)) for n in ns_o])

        c_e = mp.lu_solve(A_e, f_e)
        c_o = mp.lu_solve(A_o, f_o)

        E_e = (f_e.T * c_e)[0]
        E_o = (f_o.T * c_o)[0]
        kappa = (E_e - E_o) / (E_e + E_o)

        coeff = {n: c_e[j] for j, n in enumerate(ns_e)}
        coeff.update({n: c_o[j] for j, n in enumerate(ns_o)})
        return coeff, E_e, E_o, kappa


def sinc(x):
    x = np.asarray(x, dtype=float)
    return np.sinc(x / np.pi)


def fourier_overlap(n: int, t):
    """Integral_{-1}^1 psi_n(x) exp(i t x) dx, vectorized in t."""
    t = np.asarray(t, dtype=float)
    k = n * np.pi / 2.0
    if n % 2:
        s = (-1) ** ((n - 1) // 2)
        return s * (sinc(t + k) + sinc(t - k))
    s = (-1) ** (n // 2)
    return (s / 1j) * (sinc(t + k) - sinc(t - k))


def characteristic_arrays(coeff, t):
    t = np.asarray(t, dtype=float)
    F = np.zeros(t.shape, dtype=np.complex128)
    for n in sorted(coeff):
        F += float(coeff[n]) * fourier_overlap(n, t)
    Z = (t - 1j) * F
    # W_0 = 2 Re Z; W_pi = 2 i Im Z.  We return the real root carriers.
    return 2.0 * Z.real, 2.0 * Z.imag


def bisect_scalar(coeff, which: int, a: float, b: float, iterations: int = 60):
    fa = characteristic_arrays(coeff, np.array([a]))[which][0]
    fb = characteristic_arrays(coeff, np.array([b]))[which][0]
    if fa == 0:
        return a
    if fb == 0:
        return b
    if fa * fb > 0:
        raise ValueError("root is not bracketed")
    for _ in range(iterations):
        m = 0.5 * (a + b)
        fm = characteristic_arrays(coeff, np.array([m]))[which][0]
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5 * (a + b)


def root_scan(coeff, T: float, step: float):
    grid = np.arange(1e-5, T + step, step)
    w0, wpi = characteristic_arrays(coeff, grid)
    roots = [[], []]
    for which, vals in enumerate((w0, wpi)):
        for j in range(len(grid) - 1):
            if vals[j] * vals[j + 1] < 0:
                roots[which].append(
                    bisect_scalar(coeff, which, float(grid[j]), float(grid[j + 1]))
                )
    return roots[0], roots[1]


def phase_moment(coeff, T: float, samples: int):
    t = np.linspace(1e-7, T, samples)
    w0, wpi = characteristic_arrays(coeff, t)
    ratio = -w0 / wpi
    sigma = np.sign(ratio)
    sigma[~np.isfinite(sigma)] = 0.0
    weight = 2.0 * t / (1.0 + t * t) ** 2
    return float(np.trapezoid(sigma * weight, t))


def pair_common(r0, rpi, tolerance: float):
    used = [False] * len(rpi)
    common, only0 = [], []
    for x in r0:
        hits = [(abs(x - y), j) for j, y in enumerate(rpi) if not used[j]]
        if not hits:
            only0.append(x)
            continue
        d, j = min(hits)
        if d <= tolerance:
            used[j] = True
            common.append((x, rpi[j], d))
        else:
            only0.append(x)
    onlypi = [y for j, y in enumerate(rpi) if not used[j]]
    return common, only0, onlypi


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--max-mode", type=int, default=48)
    p.add_argument("--dps", type=int, default=80)
    p.add_argument("--T", type=float, default=100.0)
    p.add_argument("--root-step", type=float, default=0.05)
    p.add_argument("--phase-samples", type=int, default=100000)
    p.add_argument("--pair-tol", type=float, default=1e-7)
    args = p.parse_args()

    coeff, E_e, E_o, kappa = solve_coefficients(args.max_mode, args.dps)
    r0, rpi = root_scan(coeff, args.T, args.root_step)
    common, only0, onlypi = pair_common(r0, rpi, args.pair_tol)
    phase = phase_moment(coeff, args.T, args.phase_samples)
    tail = 1.0 / (1.0 + args.T * args.T)

    print("a=1 lambda=0 finite-section Xi scalar phase diagnostic")
    print("max_mode =", args.max_mode, "dps =", args.dps)
    print("E_even =", mp.nstr(E_e, 18))
    print("E_odd  =", mp.nstr(E_o, 18))
    print("kappa_direct =", mp.nstr(kappa, 25))
    print("q=E_odd/E_even =", mp.nstr(E_o / E_e, 18))
    print("W0 roots:", [f"{x:.12f}" for x in r0])
    print("Wpi roots:", [f"{x:.12f}" for x in rpi])
    print("paired common roots:", [(f"{x:.12f}", f"{d:.3e}") for x, _, d in common])
    print("unpaired W0 roots:", [f"{x:.12f}" for x in only0])
    print("unpaired Wpi roots:", [f"{x:.12f}" for x in onlypi])
    print("phase moment through T =", phase)
    print("universal exact-operator tail scale 1/(1+T^2) =", tail)
    print("difference phase - direct finite-section kappa =", phase - float(kappa))
    print("GUARDRAIL: phase moment is diagnostic for this truncated characteristic only.")


if __name__ == "__main__":
    main()
