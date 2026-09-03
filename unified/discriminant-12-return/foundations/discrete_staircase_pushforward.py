#!/usr/bin/env python3
"""Exact-formula numerical audit for the AM--GM cone staircase push-forward.

This script evaluates the flat (X,Y)-area carried by the width-one column
staircases whose ordinary factor-plane areas are T_n, n H_n, D(n), and A_n.
It uses only the closed column formula derived from the exact Jacobian

    J(x,y) = (x+y)/(4 sqrt(xy)).

No numerical quadrature is used.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction


def W_column(k: int, h: float) -> float:
    """Flat (X,Y)-area of [k-1,k] x [0,h]."""
    if k < 1 or h < 0:
        raise ValueError("require k >= 1 and h >= 0")
    a = k - 1
    delta32 = k ** 1.5 - a ** 1.5
    delta12 = math.sqrt(k) - math.sqrt(a)
    return (math.sqrt(h) * delta32 + h ** 1.5 * delta12) / 3.0


def divisor_sum(n: int) -> int:
    return sum(n // k for k in range(1, n + 1))


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0, 1))


def pushforwards(n: int) -> dict[str, float | int | Fraction]:
    D = divisor_sum(n)
    T = n * (n + 1) // 2
    A = T - D
    H = harmonic(n)

    W_D = sum(W_column(k, n // k) for k in range(1, n + 1))
    W_H = sum(W_column(k, n / k) for k in range(1, n + 1))
    W_T = sum(W_column(k, n + 1 - k) for k in range(1, n + 1))
    W_A = W_T - W_D

    return {
        "n": n,
        "T_n": T,
        "D_n": D,
        "A_n": A,
        "H_n": H,
        "nH_n": float(n * H),
        "W_T": W_T,
        "W_H": W_H,
        "W_D": W_D,
        "W_A": W_A,
        "W_H_minus_W_D": W_H - W_D,
    }


def print_report(n: int) -> None:
    r = pushforwards(n)
    print(f"n = {n}")
    print(f"T_n = {r['T_n']}")
    print(f"D(n) = {r['D_n']}")
    print(f"A_n = {r['A_n']}")
    print(f"H_n = {r['H_n']} = {float(r['H_n']):.15f}")
    print(f"n H_n = {r['nH_n']:.15f}")
    print()
    print(f"W_T(n) = {r['W_T']:.15f}")
    print(f"W_H(n) = {r['W_H']:.15f}")
    print(f"W_D(n) = {r['W_D']:.15f}")
    print(f"W_A(n) = {r['W_A']:.15f}")
    print(f"W_H(n)-W_D(n) = {r['W_H_minus_W_D']:.15f}")
    print()
    print(f"W_T/T_n = {r['W_T']/r['T_n']:.15f}")
    print(f"W_H/(nH_n) = {r['W_H']/r['nH_n']:.15f}")
    print(f"W_D/D(n) = {r['W_D']/r['D_n']:.15f}")
    if r["A_n"]:
        print(f"W_A/A_n = {r['W_A']/r['A_n']:.15f}")
    print(f"pi/4 = {math.pi/4:.15f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="?", type=int, default=11)
    args = parser.parse_args()
    if args.n < 1:
        raise SystemExit("n must be positive")
    print_report(args.n)
