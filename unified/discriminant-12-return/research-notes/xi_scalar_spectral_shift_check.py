#!/usr/bin/env python3
"""Xi scalar from the centered spectral-shift / sign-phase formula.

This is a numerical reproducer for ledger v13.965.

For the source-fixed infinite Xi target, define
    Xi(t) = xi(1/2 + i t)
and locate:
    gamma_j  : positive zeros of Xi,
    alpha_j  : zeros of Xi' between gamma_j and gamma_{j+1}.

The scalar first Schur parameter admits the sign-phase representation
    kappa_Xi = 2 * int_0^inf sgn(m_Xi(t)) t/(1+t^2)^2 dt,
with m_Xi(t) proportional to -Xi'(t)/Xi(t).

Assuming the numerically observed simple/interlacing pattern over the
computed window, this becomes the finite partial sum
    kappa_M = 1 - 2 sum_{j<=M}
                  [1/(1+gamma_j^2) - 1/(1+alpha_j^2)].

The remainder after a completed sign interval ending at alpha_M is bounded by
    1/(1+alpha_M^2)
from |sgn(m)| <= 1.

This script is a numerical check, not a proof of RH or simplicity.
"""
from __future__ import annotations

import mpmath as mp


def xi(s):
    return (
        mp.mpf("0.5")
        * s
        * (s - 1)
        * mp.pi ** (-s / 2)
        * mp.gamma(s / 2)
        * mp.zeta(s)
    )


def Xi(t):
    return mp.re(xi(mp.mpf("0.5") + 1j * t))


def Xi_prime(t):
    return mp.diff(Xi, t)


def derivative_zero_between(a, b, scan=80):
    xs = [a + (b - a) * mp.mpf(k) / scan for k in range(scan + 1)]
    y0 = Xi_prime(xs[0])
    for k in range(scan):
        y1 = Xi_prime(xs[k + 1])
        if y0 == 0:
            return xs[k]
        if y0 * y1 < 0:
            return mp.findroot(Xi_prime, (xs[k], xs[k + 1]))
        y0 = y1
    raise RuntimeError(f"no Xi' sign change found in ({a}, {b})")


def kappa_target():
    s0 = mp.mpf("1.5")
    x0 = xi(s0)
    x1 = mp.diff(xi, s0)
    x2 = mp.diff(xi, s0, 2)
    return x2 / x1 - x1 / x0


def run(num_intervals=19, dps=50):
    mp.mp.dps = dps
    gammas = [mp.im(mp.zetazero(j)) for j in range(1, num_intervals + 2)]
    alphas = [
        derivative_zero_between(
            gammas[j] + mp.mpf("1e-20"),
            gammas[j + 1] - mp.mpf("1e-20"),
        )
        for j in range(num_intervals)
    ]

    partial = mp.mpf(1)
    rows = []
    for j, (g, a) in enumerate(zip(gammas, alphas), start=1):
        decrement = 2 * (
            1 / (1 + g * g)
            - 1 / (1 + a * a)
        )
        partial -= decrement
        tail = 1 / (1 + a * a)
        rows.append((j, g, a, decrement, partial, tail))

    target = kappa_target()
    print("Xi scalar centered spectral-shift check")
    print("dps =", dps)
    print("target kappa =", mp.nstr(target, 30))
    print("j gamma_j alpha_j decrement partial tail_bound contains_target")
    for j, g, a, dec, p, tail in rows:
        contains = abs(p - target) <= tail
        print(
            j,
            mp.nstr(g, 16),
            mp.nstr(a, 16),
            mp.nstr(dec, 14),
            mp.nstr(p, 18),
            mp.nstr(tail, 12),
            contains,
        )


if __name__ == "__main__":
    run()
