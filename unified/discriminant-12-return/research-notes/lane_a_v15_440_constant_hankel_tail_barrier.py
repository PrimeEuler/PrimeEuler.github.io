#!/usr/bin/env python3
"""Arithmetic witness for Lane A v15.440's constant-Hankel tail barrier.

Analytic input recorded in the ledger:
  * the generalized Hilbert matrices G_a[j,k]=1/(j+k+a) differ
    Hilbert--Schmidtly for positive a;
  * the classical Hilbert matrix has norm and essential norm pi.
Thus every same-parity Hplus tail has norm exactly pi/2.

This witness checks the compact-difference majorant and the exact remaining
allowance arithmetic.  It makes no source-native Suzuki or full-K claim.
"""

from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 90


def grouped_hs_term(r: int, a: int, b: int) -> Fraction:
    """Sum of squared entry differences on j+k=r."""
    delta = a - b
    return Fraction((r + 1) * delta * delta, (r + a) ** 2 * (r + b) ** 2)


# For a,b>=1, every grouped term is bounded by
# (a-b)^2/(r+1)^3, whose series converges.
for a, b in [(1, 2), (1, 128001), (17, 256003)]:
    for r in range(200):
        assert grouped_hs_term(r, a, b) <= Fraction((a - b) ** 2, (r + 1) ** 3)

pi = Decimal(
    "3.141592653589793238462643383279502884197169399375105820974944592307816406286"
)
sharp_constant_hankel_norm = pi / Decimal(2)
published_outward_upper = Decimal("1.570797")

joint_variable_upper = Decimal("2.534647998455112455357343436959794")
diagonal_restoration_upper = Decimal("0.000008959074744668966136851027926")
pole_upper = Decimal("0.000008056")
target = Decimal("2.535946")

nonconstant_total = (
    joint_variable_upper + diagonal_restoration_upper + pole_upper
)
remaining_triangle_allowance = target - nonconstant_total

assert sharp_constant_hankel_norm < published_outward_upper
assert remaining_triangle_allowance == Decimal(
    "0.001280986470142875676519712012280"
)
assert sharp_constant_hankel_norm > remaining_triangle_allowance

print("sharp_constant_hankel_norm", sharp_constant_hankel_norm)
print("published_outward_upper", published_outward_upper)
print("nonconstant_total", nonconstant_total)
print("remaining_triangle_allowance", remaining_triangle_allowance)
print("barrier", "constant Hankel cannot be closed by an independent tail norm bound")
