#!/usr/bin/env python3
"""Exact-rational q=3,5,7 physical-multiplier sup-norm no-go bound."""
from fractions import Fraction as F
from math import isqrt

BITS = 320


def mul(a, b):
    v = [x*y for x in a for y in b]
    return min(v), max(v)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(a, q):
    return mul(a, (F(q), F(q)))


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


# The q=3,5,7 physical multiplier has amplitudes 2 log(q)/sqrt(q).
# Rational independence of 1, log(3)/2, log(5)/2, log(7)/2 plus
# Kronecker density makes its supremum equal to the sum of amplitudes.
amplitude_sum = (F(0), F(0))
for q in (3, 5, 7):
    amplitude_sum = add(amplitude_sum,
                        scale(mul(log_interval(q), recip(sqrt_interval(F(q)))), 2))

assert F(4179, 1000) < amplitude_sum[0]
assert amplitude_sum[1] < F(4180, 1000)

print("q357_amplitude_sum_lower", dec(amplitude_sum[0]))
print("q357_amplitude_sum_upper", dec(amplitude_sum[1]))
print("certified", "4.179 < ||Z_357||_infinity < 4.180")
