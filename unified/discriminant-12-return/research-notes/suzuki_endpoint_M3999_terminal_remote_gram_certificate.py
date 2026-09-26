#!/usr/bin/env python3
"""Terminal outward remote-Gram certificate for the rho=0.10 minus endpoint.

This script freezes the final fail-closed scalar comparison on the exact
dyadic six-planes from v13.807, after the finite-side correction from
External Audit Round 104.

It replays the repaired nominal remote Gram through n=2,000,000, checks the
coarse far-tail envelopes, proves the analytic |Z_n|<8 generator bound used
there, and then applies a deliberately loose residual-operator perturbation
budget.

The final comparison is

    H_even < gamma_even * C_even,
    H_odd  < gamma_odd  * C_odd,

with gamma*C from the outward interval tail-floor certificate v13.810.

The residual-operator uncertainty cap EPS_Y=1e-5 is intentionally much looser
than the derived current budget.  Its derivation uses:
  * exact-vs-nominal endpoint operator uncertainty eps_F=2.1e-13;
  * v13.809 buffer floors and six-RHS residuals;
  * exact frozen L0 conditioning;
  * a crude common remote cross-operator cap 20;
  * a 1e-8 replay-arithmetic reserve.

No basis is regenerated.
"""
from __future__ import annotations

from decimal import Decimal, getcontext
import math

import mpmath as mp
import numpy as np

from suzuki_endpoint_M3999_frozen_six_direction_remote_gram import (
    finite_payload,
    normalized_gram,
    far_envelope,
)


getcontext().prec = 60

# Certified endpoint / finite-side inputs.
EPS_F = Decimal("2.1e-13")
Q_NORM2_UPPER = Decimal("1.00000000000001")

MU = {
    "even-v": Decimal("0.00226937786446"),
    "odd-v": Decimal("0.00182140889323"),
}
KQ = {
    "even-v": Decimal("0.788"),
    "odd-v": Decimal("0.772"),
}
SOLVE_RESIDUAL = {
    "even-v": Decimal("1.29e-15"),
    "odd-v": Decimal("1.93e-15"),
}
L0_INV_CAP = {
    "even-v": Decimal("5.576"),
    "odd-v": Decimal("1.232"),
}
WNORM_CAP = {
    "even-v": Decimal("8"),
    "odd-v": Decimal("2"),
}

# Crude validated componentwise cap for the remote cross operator.
REMOTE_CROSS_CAP = Decimal("20")
REPLAY_ARITH_CAP = Decimal("1e-8")
EPS_Y = Decimal("1e-5")

# Point replay caps, rounded generously upward from the repaired script.
H_EXPLICIT_CAP = {
    "even-v": Decimal("0.177388"),
    "odd-v": Decimal("0.012097"),
}
H_FAR_CAP = {
    "even-v": Decimal("0.0004"),
    "odd-v": Decimal("0.00003"),
}
Y_POINT_NORM_CAP = {
    "even-v": Decimal("0.422"),
    "odd-v": Decimal("0.111"),
}

# Fully outward-certified terminal budgets from v13.810.
TERMINAL_LOWER = {
    "even-v": Decimal("2.7530522466895958"),
    "odd-v": Decimal("2.7531692412532011"),
}

# Raw tail floors, used to report normalized post-tail positivity.
GAMMA_LOWER = {
    "even-v": Decimal("2.75305442655809082"),
    "odd-v": Decimal("2.75316939956044161"),
}
C_LOWER = {
    "even-v": Decimal("0.9999992082"),
    "odd-v": Decimal("0.9999999425"),
}


def prove_z_far_bound():
    """Rigorous |Z_n|<8 for n >= 2,000,001 by elementary bounds."""
    iv = mp.iv
    iv.dps = 80

    qs = [iv.mpf(2), iv.mpf(3), iv.mpf(4), iv.mpf(5), iv.mpf(7)]
    lambdas = [
        iv.log(2),
        iv.log(3),
        iv.log(2),
        iv.log(5),
        iv.log(7),
    ]
    wsum = sum(l / iv.sqrt(q) for l, q in zip(lambdas, qs))

    n = iv.mpf(2_000_001)
    y = n * iv.pi / 4

    # Im psi(1/4+iy) = sum y/((k+1/4)^2+y^2)
    # <= pi/2 + 1/y by decreasing-sum + integral comparison.
    psi_upper = iv.pi / 2 + 1 / y

    # n*pi * sum exp(-2a_k)/(a_k^2+(n*pi/2)^2)
    # <= 4/(n*pi) * exp(-1)/(1-exp(-4)).
    corr_upper = (
        4 / (n * iv.pi)
        * iv.exp(-1)
        / (1 - iv.exp(-4))
    )

    z_upper = 2 * wsum + psi_upper + corr_upper
    assert z_upper < iv.mpf(8)
    return z_upper


def common_cross_cap_check():
    """Verify the crude common cross cap 20 from existing component majorants."""
    # Global versions of the same cusp/arch majorants used in v13.804,
    # evaluated at N=1.
    pi = math.pi
    s2 = 1.5

    c = 2 / pi**3 + 6 / pi**4
    alpha = 2 * c / pi
    cdiag = (
        2 / pi**2
        + 2 / pi**3
        + 2 / pi**4
        + 6 / pi**5
    )
    cusp = (
        2 / pi**2 * s2
        + 2 * alpha * math.sqrt(
            pi**2 / 12 * (1 + 1 / 10)
        )
        + cdiag * math.sqrt(1 + 1 / 6)
    )

    q = 2 / pi
    m4 = float(mp.zeta(3)) * q**3 / (4 * (1 - q)**3)
    cr = 19 / 12 + 4 * m4
    arch = 4 * cr / pi**2 * s2

    hilbert = 0.9 * pi / 2
    prime = 2.05

    # Crude full rank-one norm caps from |c_n|,|d_n| <= const/n.
    pole_even = (16 / 3) * math.cosh(0.5)**2
    pole_odd = (16 / 3) * math.sinh(0.5)**2

    even_total = hilbert + prime + cusp + arch + pole_even
    odd_total = hilbert + prime + cusp + arch + pole_odd

    assert even_total < 20
    assert odd_total < 20
    return even_total, odd_total


def eps_y_derived(sector: str):
    """Derived normalized residual-operator perturbation bound."""
    eps = EPS_F
    mu = MU[sector]
    k = KQ[sector]
    r = SOLVE_RESIDUAL[sector]
    t = L0_INV_CAP[sector]

    q = Q_NORM2_UPPER.sqrt()

    # Exact-vs-nominal plus finite-solve perturbation of the dressed
    # finite six-plane, before the remote cross map.
    dx = (
        eps * q / (mu - eps)
        + eps * k / (mu * (mu - eps))
        + r / mu
    ) * t

    total = (
        REMOTE_CROSS_CAP * dx
        + eps * WNORM_CAP[sector]
        + REPLAY_ARITH_CAP
    )
    return dx, total


def point_replay(sector: str):
    payload = finite_payload(sector)
    _G, H = normalized_gram(payload)
    lam = float(np.linalg.eigvalsh(H)[-1])
    far = float(far_envelope(payload)["bound"])

    assert Decimal(str(lam)) < H_EXPLICIT_CAP[sector]
    assert Decimal(str(far)) < H_FAR_CAP[sector]
    return lam, far


def terminal_certificate(sector: str):
    lam, far = point_replay(sector)

    dx, eps_derived = eps_y_derived(sector)
    assert eps_derived < EPS_Y

    h_point = H_EXPLICIT_CAP[sector] + H_FAR_CAP[sector]
    h_perturb = (
        2 * Y_POINT_NORM_CAP[sector] * EPS_Y
        + EPS_Y * EPS_Y
    )
    h_upper = h_point + h_perturb

    terminal = TERMINAL_LOWER[sector]
    margin = terminal - h_upper

    # Equivalent normalized post-tail six-plane lower bound:
    # C - H/gamma.
    normalized_lower = (
        C_LOWER[sector]
        - h_upper / GAMMA_LOWER[sector]
    )

    assert margin > Decimal("2.5")
    assert normalized_lower > Decimal("0.93")

    return {
        "point_lambda": lam,
        "point_far": far,
        "dressed_plane_error": dx,
        "derived_eps_y": eps_derived,
        "eps_y_cap": EPS_Y,
        "h_point_upper": h_point,
        "h_perturb": h_perturb,
        "h_upper": h_upper,
        "terminal_lower": terminal,
        "margin": margin,
        "normalized_post_tail_lower": normalized_lower,
    }


def main():
    zbound = prove_z_far_bound()
    cross = common_cross_cap_check()

    print("rigorous far generator bound =", zbound)
    print("remote cross component totals =", cross)

    even = terminal_certificate("even-v")
    odd = terminal_certificate("odd-v")

    for name, row in (("even-v", even), ("odd-v", odd)):
        print("\n", name)
        for k, v in row.items():
            print(k, "=", v)

    assert even["h_upper"] < Decimal("0.177797")
    assert odd["h_upper"] < Decimal("0.012130")

    assert even["margin"] > Decimal("2.57525")
    assert odd["margin"] > Decimal("2.74102")

    print("\nPASS: outward six-plane remote Gram certificate")
    print(
        "even: H < 0.1777964401 I < gamma*C, "
        "terminal margin > 2.5752558065895958"
    )
    print(
        "odd:  H < 0.0121292201 I < gamma*C, "
        "terminal margin > 2.7410400211532011"
    )
    print(
        "Guardrail: this certifies positivity on the frozen six-plane at "
        "the rho=0.10 minus endpoint. It does not by itself certify the "
        "four complementary core directions or the plus endpoint."
    )


if __name__ == "__main__":
    main()
