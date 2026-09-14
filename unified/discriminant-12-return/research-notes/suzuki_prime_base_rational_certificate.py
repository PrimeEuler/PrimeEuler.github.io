#!/usr/bin/env python3
"""Elementary rational certificate for the five Suzuki prime base angles.

The odd-sector finite-high modes are n=2r.  Prime phases are therefore

    r*pi*log(q), q in {2,3,4,5,7}.

This helper encloses pi and log(q) using exact Fraction arithmetic only:

  pi = 16 atan(1/5) - 4 atan(1/239),

with alternating arctan remainders, and

  log(q) = 2 atanh((q-1)/(q+1))
         = 2 sum x^(2k+1)/(2k+1),

with a positive geometric tail bound.

It intentionally stops at the base-angle stage.  A following checker can turn
these intervals into sin/cos intervals by exact Taylor bounds and then use the
matrix-power telescoping estimate for r<=2000.
"""
from __future__ import annotations

from fractions import Fraction

QS = (2, 3, 4, 5, 7)
LOG_K = {2: 12, 3: 19, 4: 26, 5: 32, 7: 46}


def atan_interval(x: Fraction, K: int):
    """Alternating interval for atan(x), summing k=0..K inclusive."""
    s = Fraction(0)
    for k in range(K + 1):
        t = x ** (2*k + 1) / (2*k + 1)
        s += t if (k % 2 == 0) else -t
    r = x ** (2*K + 3) / (2*K + 3)
    # next term has sign (-1)^(K+1)
    if (K + 1) % 2 == 0:
        return s, s + r
    return s - r, s


def pi_interval():
    a5_lo, a5_hi = atan_interval(Fraction(1, 5), 12)
    a239_lo, a239_hi = atan_interval(Fraction(1, 239), 3)
    return 16*a5_lo - 4*a239_hi, 16*a5_hi - 4*a239_lo


def log_interval(q: int, K: int):
    x = Fraction(q - 1, q + 1)
    s = Fraction(0)
    for k in range(K + 1):
        s += 2 * x ** (2*k + 1) / (2*k + 1)
    # For positive x, bound the remaining odd-denominator series by replacing
    # every later denominator with the first omitted denominator.
    rem = (
        2 * x ** (2*K + 3)
        / (2*K + 3)
        / (1 - x*x)
    )
    return s, s + rem


def mul_positive_intervals(a, b):
    assert a[0] > 0 and b[0] > 0
    return a[0]*b[0], a[1]*b[1]


def report():
    p = pi_interval()
    print('pi width =', float(p[1] - p[0]))
    print('pi midpoint =', float((p[0] + p[1])/2))
    assert float(p[1] - p[0]) < 1e-18

    worst_alpha_width = 0.0
    for q in QS:
        L = log_interval(q, LOG_K[q])
        alpha = mul_positive_intervals(p, L)
        lw = float(L[1] - L[0])
        aw = float(alpha[1] - alpha[0])
        worst_alpha_width = max(worst_alpha_width, aw)
        print('q =', q,
              'log width =', lw,
              'alpha width =', aw,
              'alpha midpoint =', float((alpha[0] + alpha[1])/2))
        assert lw < 1e-13
        assert aw < 4e-13

    # The exact rotation map is 1-Lipschitz in its angle in operator norm.
    # Using half the alpha width as base-angle radius, telescoping r<=2000
    # keeps pure base-interval propagation far below the micro-scale target.
    propagated = 2000.0 * worst_alpha_width/2.0
    print('worst r<=2000 base-angle propagation scale =', propagated)
    assert propagated < 4e-10


if __name__ == '__main__':
    report()
