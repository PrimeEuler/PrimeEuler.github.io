#!/usr/bin/env python3
"""Exact signed shifted-sawtooth branch identities on R/(2Z)."""
from fractions import Fraction as F


def saw(x):
    x %= 2
    return F(1) - x


def dplus(x, L):
    return saw(x - L) - saw(x)


def dminus(x, L):
    return saw(x + L) - saw(x)


# Check both L<1 and L>1 regimes at exact rational sample points in every
# branch interval.  The ledger supplies the universal affine derivation.
for L in (F(2, 3), F(3, 2)):
    plus_points = (L / 2, (L + 2) / 2)
    minus_points = ((2 - L) / 2, 2 - L / 2)
    assert dplus(plus_points[0], L) == L - 2
    assert dplus(plus_points[1], L) == L
    assert dminus(minus_points[0], L) == -L
    assert dminus(minus_points[1], L) == 2 - L

print("D_plus(x)", "L-2 on [0,L); L on [L,2)")
print("D_minus(x)", "-L on [0,2-L); 2-L on [2-L,2)")
print("magnitudes", "2-L/L and L/2-L, matching v15.327")
print("certified", "exact signed sawtooth branches under s(x)=1-x convention")
