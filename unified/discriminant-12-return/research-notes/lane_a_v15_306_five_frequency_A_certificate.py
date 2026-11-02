#!/usr/bin/env python3
"""Exact-rational certificate for the v15.305 five-frequency constant A.

Only Decimal.ln/sqrt are used as primitive transcendental evaluations.  Python's
Decimal specification makes those correctly rounded in ROUND_HALF_EVEN; the
results are widened by 1e-110 at precision 120 before conversion to Fractions.
Pi is enclosed independently by exact Machin-series rational bounds, and sine
is enclosed by exact alternating Taylor bounds after reduction to [0, pi/2].
"""

from decimal import Decimal, localcontext, ROUND_HALF_EVEN
from fractions import Fraction


PREC = 120
RAD = Decimal("1e-110")
QS = (2, 3, 4, 5, 7)


def frac_decimal(x: Decimal) -> Fraction:
    return Fraction(x)


def rounded_decimal_bounds(x: Decimal) -> tuple[Fraction, Fraction]:
    return frac_decimal(x - RAD), frac_decimal(x + RAD)


def atan_inv_bounds(m: int, even_last: int = 100) -> tuple[Fraction, Fraction]:
    """Bounds atan(1/m) by consecutive alternating partial sums."""
    assert even_last % 2 == 0
    upper = sum(
        ((-1) ** k) * Fraction(1, (2 * k + 1) * m ** (2 * k + 1))
        for k in range(even_last + 1)
    )
    lower = upper - Fraction(1, (2 * even_last + 3) * m ** (2 * even_last + 3))
    return lower, upper


def pi_bounds() -> tuple[Fraction, Fraction]:
    a5_lo, a5_hi = atan_inv_bounds(5)
    a239_lo, a239_hi = atan_inv_bounds(239)
    return 16 * a5_lo - 4 * a239_hi, 16 * a5_hi - 4 * a239_lo


def sin_bounds_0_halfpi(y_lo: Fraction, y_hi: Fraction, odd_last: int = 19):
    """Enclose sin([y_lo,y_hi]) for 0 <= y <= pi/2 exactly."""
    assert odd_last % 2 == 1
    # sin is increasing here.  Odd final k gives a lower partial sum;
    # the preceding even final k gives an upper partial sum.
    lower = sum(
        ((-1) ** k) * y_lo ** (2 * k + 1) / factorial(2 * k + 1)
        for k in range(odd_last + 1)
    )
    upper = sum(
        ((-1) ** k) * y_hi ** (2 * k + 1) / factorial(2 * k + 1)
        for k in range(odd_last)
    )
    return lower, upper


def factorial(n: int) -> int:
    out = 1
    for k in range(2, n + 1):
        out *= k
    return out


def dec(x: Fraction, digits: int = 60) -> str:
    with localcontext() as ctx:
        ctx.prec = digits
        return str(Decimal(x.numerator) / Decimal(x.denominator))


def main() -> None:
    pi_lo, pi_hi = pi_bounds()
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = ROUND_HALF_EVEN
        log_bounds = {q: rounded_decimal_bounds(Decimal(q).ln()) for q in QS}
        sqrt_bounds = {q: rounded_decimal_bounds(Decimal(q).sqrt()) for q in QS}

    A_lo = Fraction(0)
    A_hi = Fraction(0)
    for q in QS:
        l_lo, l_hi = log_bounds[q]
        if q == 4:
            w_lo, w_hi = log_bounds[2][0] / 2, log_bounds[2][1] / 2
        else:
            s_lo, s_hi = sqrt_bounds[q]
            w_lo, w_hi = l_lo / s_hi, l_hi / s_lo

        th_lo, th_hi = pi_lo * l_lo / 2, pi_hi * l_hi / 2
        if th_hi <= pi_lo / 2:
            y_lo, y_hi = th_lo, th_hi
        else:
            assert th_lo >= pi_hi / 2 and th_hi < pi_lo
            y_lo, y_hi = pi_lo - th_hi, pi_hi - th_lo
        sin_lo, sin_hi = sin_bounds_0_halfpi(y_lo, y_hi)
        term_lo = 8 * w_lo * w_lo * sin_lo * sin_lo
        term_hi = 8 * w_hi * w_hi * sin_hi * sin_hi
        A_lo += term_lo
        A_hi += term_hi
        print(f"q={q}: [{dec(term_lo)}, {dec(term_hi)}]")

    A_claim = Fraction(838, 125)       # 6.704
    sqrt_claim = Fraction(2589, 1000)  # 2.589
    L_claim = Fraction(103, 250)       # 0.412
    assert A_lo > A_claim
    assert A_lo > sqrt_claim * sqrt_claim
    assert A_lo > (2 * pi_hi * L_claim) ** 2

    print(f"A interval: [{dec(A_lo)}, {dec(A_hi)}]")
    print("CERTIFIED: A > 838/125 = 6.704")
    print("CERTIFIED: sqrt(A) > 2589/1000 = 2.589")
    print("CERTIFIED: sqrt(A)/(2*pi) > 103/250 = 0.412")


if __name__ == "__main__":
    main()
