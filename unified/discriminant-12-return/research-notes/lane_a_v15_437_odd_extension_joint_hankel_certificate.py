#!/usr/bin/env python3
"""Exact arithmetic witness for Lane A v15.437.

The analytic certificate identifies the positive-half-line joint operator

    (1/pi)([W,Hminus] - {W,Hplus})

with the restriction of the normalized bilateral commutator to odd inputs,
where W is extended oddly.  This witness checks the coefficient identity
exactly over representative rational data and reconstructs the outward
full-tail arithmetic from the already-audited endpoints.

Scope: the chosen counting-measure ell2 model only.  This is not a
source-native Suzuki-Phi or FULL_K_TRANSFER certificate.
"""

from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 90


def joint_halfline(n, m, wn, wm):
    """Coefficient of [W,Hminus]-{W,Hplus}, without 1/pi."""
    return (
        wn * (Fraction(1, n - m) - Fraction(1, n + m))
        - wm * (Fraction(1, n - m) + Fraction(1, n + m))
    )


def canonical(n, m, wn, wm):
    return Fraction(2, 1) * (m * wn - n * wm) / (n * n - m * m)


for n, m, wn, wm in [
    (5, 3, Fraction(7, 11), Fraction(-2, 13)),
    (17, 9, Fraction(-5, 19), Fraction(23, 29)),
    (256003, 256001, Fraction(31, 37), Fraction(-41, 43)),
]:
    assert joint_halfline(n, m, wn, wm) == canonical(n, m, wn, wm)

# Outward endpoints already certified/audited in v15.423/v15.424,
# v15.309/v15.432/v15.433, and v15.435/v15.436.
prime_joint_upper = Decimal("2.534644890455112455357343436959794")
nonprime_joint_upper = Decimal("0.000003108")
constant_hankel_upper = Decimal("1.570797")
diagonal_restoration_upper = Decimal("0.000008959074744668966136851027926")
pole_upper = Decimal("0.000008056")

joint_variable_upper = prime_joint_upper + nonprime_joint_upper
full_tail_upper = (
    joint_variable_upper
    + constant_hankel_upper
    + diagonal_restoration_upper
    + pole_upper
)

assert joint_variable_upper == Decimal("2.534647998455112455357343436959794")
assert full_tail_upper == Decimal("4.105462013529857124323480287987720")
assert full_tail_upper < Decimal("4.105463")
assert full_tail_upper < Decimal("9.740007")
assert full_tail_upper > Decimal("2.535946")

print("prime_joint_upper", prime_joint_upper)
print("nonprime_joint_upper", nonprime_joint_upper)
print("joint_variable_upper", joint_variable_upper)
print("full_tail_upper", full_tail_upper)
print("certified_bound", "||Q B Q|| < 4.105463")
print("target_status", "OPEN: 4.105463 > 2.535946")
