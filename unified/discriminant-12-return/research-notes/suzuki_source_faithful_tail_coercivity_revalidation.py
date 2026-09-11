#!/usr/bin/env python3
"""Independent source-faithful revalidation of the raw Suzuki odd tail gap.

This file isolates the part of the old high-complement architecture that does
not depend on the audited v13.365 six-plane cross certificate.

For odd modes n >= N, use

    A0_tail >= log(N/4) I
              - ||H_odd|| I
              - ||B_prime|| I
              - beta_cusp(N) I
              - beta_arch(N) I,

with

    ||H_odd|| = pi/2,
    ||B_prime|| < 2.05

(the robust validated-computational prime target), and the explicit cusp and
archimedean localization bounds inherited from the source-faithful rank-two
matrix.

At N=16003 this gives a raw tail lower bound above 4.6733.  No finite-high /
remote-tail coupling estimate is used here.

Guardrail: this revalidates only the raw tail compression lower bound.  It does
not restore v13.365, prove positivity of the whole high complement, or imply an
inertia/RH/GRH conclusion.
"""

from __future__ import annotations

import math
import mpmath as mp

PRIME_BOUND = 2.05
N_TARGET = 16003


def odd_sum2_tail_bound(N: int) -> float:
    return 1.0 / N**2 + 1.0 / (2.0 * N)


def odd_sum4_tail_bound(N: int) -> float:
    return 1.0 / N**4 + 1.0 / (6.0 * N**3)


def odd_sum6_tail_bound(N: int) -> float:
    return 1.0 / N**6 + 1.0 / (10.0 * N**5)


def cusp_tail_bound(N: int) -> float:
    rank_one = (2.0 / math.pi**2) * odd_sum2_tail_bound(N)
    c = 2.0 / math.pi**3 + 6.0 / math.pi**4
    alpha = 2.0 * c / math.pi
    offdiag = 2.0 * alpha * math.sqrt(
        (math.pi**2 / 12.0) * odd_sum6_tail_bound(N)
    )
    c_diag = (
        2.0 / math.pi**2
        + 2.0 / math.pi**3
        + 2.0 / math.pi**4
        + 6.0 / math.pi**5
    )
    diagonal = c_diag * math.sqrt(odd_sum4_tail_bound(N))
    return rank_one + offdiag + diagonal


def r4_majorant() -> float:
    q = 2.0 / math.pi
    return float(mp.zeta(3)) * q**3 / (4.0 * (1.0 - q) ** 3)


def arch_entry_constant() -> float:
    return 19.0 / 12.0 + 4.0 * r4_majorant()


def arch_tail_bound(N: int) -> float:
    return arch_entry_constant() * (4.0 / math.pi**2) * odd_sum2_tail_bound(N)


def tail_margin(N: int) -> float:
    return (
        math.log(N / 4.0)
        - math.pi / 2.0
        - PRIME_BOUND
        - cusp_tail_bound(N)
        - arch_tail_bound(N)
    )


if __name__ == "__main__":
    cusp = cusp_tail_bound(N_TARGET)
    arch = arch_tail_bound(N_TARGET)
    margin = tail_margin(N_TARGET)
    print("N =", N_TARGET)
    print("robust prime bound =", PRIME_BOUND)
    print("cusp tail <=", cusp)
    print("arch tail <=", arch)
    print("raw tail lower bound >=", margin)
    assert margin > 4.6732
    print("PASS: independent raw tail coercivity target > 4.6732")
    print("guardrail: no cross/high-complement/inertia/RH/GRH conclusion")
