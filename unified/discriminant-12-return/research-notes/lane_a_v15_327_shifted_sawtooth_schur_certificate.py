#!/usr/bin/env python3
"""Exact-rational all-frequency shifted-sawtooth Schur upper bound."""
from fractions import Fraction as F
from math import isqrt

BITS = 320


def mul(a, b):
    v = [x*y for x in a for y in b]
    return min(v), max(v)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def recip(a):
    return 1/a[1], 1/a[0]


def log_interval(q):
    r = F(q - 1, q + 1)
    kmax = 2 * BITS + 32
    s = 2 * sum((r ** (2*k + 1) / (2*k + 1) for k in range(kmax)), F(0))
    e = 2 * r ** (2*kmax + 1) / ((2*kmax + 1) * (1-r*r))
    return s, s + e


def sqrt_interval(q):
    k = isqrt((q.numerator << (2*BITS)) // q.denominator)
    return F(k, 1 << BITS), F(k + 1, 1 << BITS)


def dec(x):
    return f"{x.numerator/x.denominator:.30f}"


# For each q, pairing the +phi_q and -phi_q shifts pointwise gives a
# row/column absolute sum at most log(q)/sqrt(q). Summing all five q's
# is therefore a Schur bound for the normalized bilateral commutator.
schur = (F(0), F(0))
for q in (2, 3, 4, 5, 7):
    schur = add(schur, mul(log_interval(q), recip(sqrt_interval(F(q)))))

assert F(3272, 1000) < schur[0]
assert schur[1] < F(3273, 1000)

print("shifted_sawtooth_schur_lower", dec(schur[0]))
print("shifted_sawtooth_schur_upper", dec(schur[1]))
print("certified", "3.272 < B_comm_schur < 3.273")
