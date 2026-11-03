#!/usr/bin/env python3
"""Exact-rational NO-GO for product-norm-only Cotlar across q blocks."""
from fractions import Fraction as F
from math import isqrt

BITS = 320


def mul(a, b):
    v = [x * y for x in a for y in b]
    return min(v), max(v)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def recip(a):
    return 1 / a[1], 1 / a[0]


def log_interval(q):
    r = F(q - 1, q + 1)
    kmax = 2 * BITS + 32
    s = 2 * sum((r ** (2 * k + 1) / (2 * k + 1) for k in range(kmax)), F(0))
    e = 2 * r ** (2 * kmax + 1) / ((2 * kmax + 1) * (1 - r * r))
    return s, s + e


def sqrt_fraction_down(x):
    n = (x.numerator << (2 * BITS)) // x.denominator
    return F(isqrt(n), 1 << BITS)


def sqrt_interval(a):
    lo = sqrt_fraction_down(a[0])
    hi0 = sqrt_fraction_down(a[1])
    hi = hi0 if hi0 * hi0 == a[1] else hi0 + F(1, 1 << BITS)
    return lo, hi


def dec(x):
    return f"{x.numerator / x.denominator:.30f}"


qs = (2, 3, 4, 5, 7)
b = {}
triangle = (F(0), F(0))
for q in qs:
    sqrt_q = sqrt_interval((F(q), F(q)))
    b[q] = mul(log_interval(q), recip(sqrt_q))
    triangle = add(triangle, b[q])

# q=7 is the largest individual certified block bound.
for q in qs[:-1]:
    assert b[q][1] < b[7][0]

# Generic submultiplicativity gives both cross-product norms <= b_q b_r.
# Cotlar with a_qr=sqrt(b_q b_r) therefore returns
# sqrt(max_q b_q) * sum_r sqrt(b_r).
cotlar = (F(0), F(0))
sum_sqrt_b = (F(0), F(0))
for q in qs:
    sum_sqrt_b = add(sum_sqrt_b, sqrt_interval(b[q]))
cotlar = mul(sqrt_interval(b[7]), sum_sqrt_b)

assert F(3460, 1000) < cotlar[0]
assert cotlar[1] < F(3461, 1000)
assert triangle[1] < cotlar[0]

print("triangle_upper", dec(triangle[1]))
print("generic_cotlar_lower", dec(cotlar[0]))
print("generic_cotlar_upper", dec(cotlar[1]))
print("certified", "3.460 < B_generic_cotlar < 3.461 and B_triangle < B_generic_cotlar")
