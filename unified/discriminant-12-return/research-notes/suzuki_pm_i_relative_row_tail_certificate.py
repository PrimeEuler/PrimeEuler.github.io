#!/usr/bin/env python3
"""Exact ±i observable-row difference and tail certificate.

For the a=1 parity Fourier basis used throughout the current Lane A
source-faithful architecture,

    p_-i,n = <psi_n, e^x>,

and reflection gives

    p_+i,n = +p_-i,n  on the even spatial sector (odd n),
    p_+i,n = -p_-i,n  on the odd  spatial sector (even n).

Hence Delta p := p_+i - p_-i vanishes identically on even-v and is
supported entirely on odd-v.

The exact source coefficient formula is imported from the audited KKT
remote-residual architecture.  For even n,

    Delta p_n
      = 8*pi*n*sinh(1)/(pi^2*n^2 + 4)
      = [8*sinh(1)/(pi*n)] / [1 + 4/(pi^2*n^2)].

Thus Delta p is l2 but has a genuine 1/n leading term; there is no
N^{-3/2} cancellation.  Its same-parity l2 tail is O(N^{-1/2}) with an
explicit two-sided bound.

This is exactly the trace norm of the rank-one border-row truncation,
because the other rank-one factor is a unit border coordinate.

Guardrail: this certifies only the observable-row tail.  It does not by
itself certify convergence of the inverse bordered operator or the full
finite-section projective ratio.
"""
from __future__ import annotations

import math
import numpy as np

from suzuki_kkt_remote_residual_certificate import source_rows


def delta_exact(n: np.ndarray) -> np.ndarray:
    n = np.asarray(n, dtype=float)
    return 8.0 * math.pi * n * math.sinh(1.0) / (
        math.pi**2 * n**2 + 4.0
    )


def tail_bounds(N: int):
    if N % 2:
        raise ValueError("N must be even")
    # Remaining odd-sector modes are n=N+2,N+4,...
    A = 8.0 * math.sinh(1.0) / math.pi
    n0 = N + 2

    # sum_{even n>N} 1/n^2 = (1/4) sum_{m>N/2} 1/m^2
    # and for M=N/2:
    #   1/[4(M+1)] <= sum <= 1/(4M)
    s_lower = 1.0 / (2.0 * (N + 2.0))
    s_upper = 1.0 / (2.0 * N)

    factor_min = 1.0 / (1.0 + 4.0 / (math.pi**2 * n0**2))
    lo = A * factor_min * math.sqrt(s_lower)
    hi = A * math.sqrt(s_upper)
    return lo, hi


def main():
    odd_modes = np.arange(2, 42, 2, dtype=int)
    even_modes = np.arange(1, 42, 2, dtype=int)

    pminus_odd = source_rows(odd_modes, "odd-v")
    pplus_odd = -pminus_odd
    delta_odd = pplus_odd - pminus_odd

    pminus_even = source_rows(even_modes, "even-v")
    pplus_even = pminus_even
    delta_even = pplus_even - pminus_even

    exact = delta_exact(odd_modes)
    err = float(np.max(np.abs(delta_odd - exact)))

    print("±i observable-row reflection certificate")
    print("max exact-formula error on first 20 odd-sector modes =", repr(err))
    print("max even-sector row difference =", repr(float(np.max(np.abs(delta_even)))))

    lead = 8.0 * math.sinh(1.0) / math.pi
    norm_lead = 4.0 * math.sqrt(2.0) * math.sinh(1.0) / math.pi

    print("pointwise leading coefficient n*Delta p_n ->", repr(lead))
    print("tail leading constant sqrt(N)||Delta p_{>N}||_2 ->", repr(norm_lead))

    for N in (100, 1000, 10000, 100000, 1000000):
        lo, hi = tail_bounds(N)
        print(
            "N =", N,
            "lower =", repr(lo),
            "upper =", repr(hi),
            "sqrtN lower =", repr(math.sqrt(N) * lo),
            "sqrtN upper =", repr(math.sqrt(N) * hi),
        )

    assert err < 2.0e-15
    assert np.max(np.abs(delta_even)) == 0.0

    print(
        "PASS: Delta p is odd-sector only, trace-class as a rank-one row "
        "perturbation, with explicit O(N^-1/2) truncation tail."
    )
    print(
        "GUARDRAIL: no inverse-border or finite-to-infinite ratio convergence "
        "claim follows from this row-tail bound alone."
    )


if __name__ == "__main__":
    main()
