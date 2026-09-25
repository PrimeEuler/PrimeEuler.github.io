#!/usr/bin/env python3
"""Outward interval certificate for the rho=0.10 endpoint remote-tail floors.

Targets
-------
even-v remote tail starts at n=4001,
odd-v remote tail starts at n=4002.

For F^-_rho = A - rho B_sm, rho=0.10, use the audited lower bound

  gamma_even(N)
    = (1-rho) [ log(N/4) - pi/2 ]
      - 2.05
      - beta_cusp(N)
      - beta_arch(N),

and in corrected odd-v subtract the adverse pole norm

  beta_pole(N)
    = 32 sinh(1/2)^2 / pi^2 * s2(N).

All arithmetic is performed with mpmath interval arithmetic at 80 decimal
digits.  Apéry's constant is enclosed independently by summing the first
20,000 positive terms and bounding the remainder by the monotone integral test:

  1/(2(M+1)^2)
    <= sum_{k>M} 1/k^3
    <= 1/(2 M^2).

The script also combines the certified tail floors with the frozen finite-side
normalized bounds from v13.809:

  C_even > 0.9999992082 I,
  C_odd  > 0.9999999425 I.

The products gamma*C_lower are the rigorous terminal budgets available before
subtracting the remote residual Gram H.
"""
from __future__ import annotations

import mpmath as mp


iv = mp.iv
iv.dps = 80

RHO = iv.mpf("0.10")
PRIME_BOUND = iv.mpf("2.05")

C_EVEN_LOWER = iv.mpf("0.9999992082")
C_ODD_LOWER = iv.mpf("0.9999999425")


def zeta3_interval(M: int = 20000):
    s = iv.mpf(0)
    for k in range(1, M + 1):
        x = iv.mpf(k)
        s += 1 / (x**3)

    tail_lo = 1 / (2 * iv.mpf(M + 1)**2)
    tail_hi = 1 / (2 * iv.mpf(M)**2)
    return iv.mpf([s.a + tail_lo.a, s.b + tail_hi.b])


ZETA3 = zeta3_interval()
PI = iv.pi
SINH_HALF = (
    iv.exp(iv.mpf("0.5"))
    - iv.exp(-iv.mpf("0.5"))
) / 2


def s2(N: int):
    n = iv.mpf(N)
    return n**-2 + 1 / (2 * n)


def cusp_tail_bound(N: int):
    n = iv.mpf(N)
    c = 2 / PI**3 + 6 / PI**4
    alpha = 2 * c / PI
    cdiag = (
        2 / PI**2
        + 2 / PI**3
        + 2 / PI**4
        + 6 / PI**5
    )

    rank1 = 2 / PI**2 * s2(N)
    off = (
        2 * alpha
        * iv.sqrt(
            PI**2 / 12
            * (
                n**-6
                + 1 / (10 * n**5)
            )
        )
    )
    diag = (
        cdiag
        * iv.sqrt(
            n**-4
            + 1 / (6 * n**3)
        )
    )
    return rank1 + off + diag


def arch_tail_bound(N: int):
    q = 2 / PI
    m4 = ZETA3 * q**3 / (4 * (1 - q)**3)
    cr = iv.mpf(19) / 12 + 4 * m4
    return 4 * cr / PI**2 * s2(N)


def odd_pole_tail_bound(N: int):
    return (
        32 * SINH_HALF**2 / PI**2
        * s2(N)
    )


def bulk_lower_term(N: int):
    n = iv.mpf(N)
    return (
        (1 - RHO)
        * (iv.log(n / 4) - PI / 2)
    )


def endpoint_tail_floor(N: int, odd: bool = False):
    out = (
        bulk_lower_term(N)
        - PRIME_BOUND
        - cusp_tail_bound(N)
        - arch_tail_bound(N)
    )
    if odd:
        out -= odd_pole_tail_bound(N)
    return out


def report():
    gamma_even = endpoint_tail_floor(4001, odd=False)
    gamma_odd = endpoint_tail_floor(4002, odd=True)

    terminal_even = gamma_even * C_EVEN_LOWER
    terminal_odd = gamma_odd * C_ODD_LOWER

    print("rho=0.10 endpoint tail-floor interval certificate")
    print("zeta(3) enclosure =", ZETA3)

    print("\neven-v N=4001")
    print("bulk =", bulk_lower_term(4001))
    print("cusp upper interval =", cusp_tail_bound(4001))
    print("arch upper interval =", arch_tail_bound(4001))
    print("gamma_even =", gamma_even)
    print("C_even lower =", C_EVEN_LOWER)
    print("gamma_even*C_even_lower =", terminal_even)

    print("\nodd-v N=4002")
    print("bulk =", bulk_lower_term(4002))
    print("cusp upper interval =", cusp_tail_bound(4002))
    print("arch upper interval =", arch_tail_bound(4002))
    print("odd-pole upper interval =", odd_pole_tail_bound(4002))
    print("gamma_odd =", gamma_odd)
    print("C_odd lower =", C_ODD_LOWER)
    print("gamma_odd*C_odd_lower =", terminal_odd)

    # Conservative decimal PASS thresholds, strictly below the interval lowers.
    assert gamma_even > iv.mpf("2.75305442655809082")
    assert gamma_odd > iv.mpf("2.75316939956044161")
    assert terminal_even > iv.mpf("2.7530522466895958")
    assert terminal_odd > iv.mpf("2.7531692412532011")

    print("\nPASS outward endpoint tail floors")
    print(
        "rigorous even terminal budget > 2.7530522466895958"
    )
    print(
        "rigorous odd terminal budget  > 2.7531692412532011"
    )
    print(
        "Guardrail: these terminal budgets precede subtraction of the "
        "remote residual Gram H; no infinite endpoint inertia theorem is "
        "promoted by this script alone."
    )


if __name__ == "__main__":
    report()
