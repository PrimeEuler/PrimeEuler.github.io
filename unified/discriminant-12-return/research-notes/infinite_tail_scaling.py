#!/usr/bin/env python3
"""Scaling probe: K_{p,N}, diagonal coercivity, and paired structure vs N.

Computes for N in {8000, 16000, 32000, 64000, 128000}:
  - K_p^{(diag)}(N) = sum_{n>N,parity} 1/(n^2 d_n)  [diagonal approx to <u,S^{-1}u>]
  - d_min(N) = min_{n>N} d_n  [diagonal coercivity floor]
  - ||u||^2 = sum 1/n^2
  - the T2 scale A*C_S*K^2 with A=803, C_S=421.84 (N=4000 values, for scale)
All deterministic.
"""
from __future__ import annotations
import math
from infinite_tail_producer import diag_n

def K_diag(N, parity, M_factor=20):
    """Sum_{N<n<=M_factor*N, parity} 1/(n^2 d_n) + integral tail estimate."""
    M = M_factor * N
    s = 0.0
    n = N + (1 if parity == "odd" else 2)  # even sector: odd modes; odd sector: even
    # adjust: even sector modes are odd, odd sector modes are even
    if parity == "even":
        start = N + 1  # odd
    else:
        start = N + 2  # even
    n = start
    while n <= M:
        d = diag_n(n)
        s += 1.0 / (n * n * d)
        n += 2
    # tail integral: (1/2)*int_M^inf dx/(x^2 log(x/4)) ~ (1/2)/(M log(M/4))
    tail = 0.5 / (M * math.log(M / 4))
    return s, tail

def main():
    print(f"{'N':>8} {'K_e':>12} {'K_o':>12} {'d_min':>8} {'||u||^2':>12} {'T2scale':>12}")
    for N in [8000, 16000, 32000, 64000, 128000]:
        Ke, te = K_diag(N, "even")
        Ko, to = K_diag(N, "odd")
        Ke_tot, Ko_tot = Ke + te, Ko + to
        # d_min over the window
        dmin = min(diag_n(N + 1 + 2 * j) for j in range(200))
        u2 = 0.5 / N  # sum_{n>N,parity} 1/n^2 ~ 1/(2N)
        # T2 = A*C_S*K^2 with A=803, C_S=421.84
        T2 = 803 * 421.84 * Ke_tot * Ko_tot
        print(f"{N:>8} {Ke_tot:>12.4e} {Ko_tot:>12.4e} {dmin:>8.3f} {u2:>12.4e} {T2:>12.4e}")
    print()
    print("margin = 3.4556e-7")
    print("T2scale uses A=803, C_S=421.84 (N=4000 values) -- for ORDER only.")

if __name__ == "__main__":
    main()
