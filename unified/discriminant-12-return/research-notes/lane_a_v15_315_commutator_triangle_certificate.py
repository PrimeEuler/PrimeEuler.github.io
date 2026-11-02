#!/usr/bin/env python3
"""Exact-rational enclosure of the frequencywise Hminus commutator bound."""
from fractions import Fraction as F
from math import isqrt

BITS = 320


def log_interval(q):
    r = F(q - 1, q + 1)
    K = 2 * BITS + 32
    s = 2 * sum((r ** (2*k + 1) / (2*k + 1) for k in range(K)), F(0))
    e = 2 * r ** (2*K + 1) / ((2*K + 1) * (1 - r*r))
    return s, s + e


def sqrt_interval(q):
    k = isqrt(q << (2 * BITS))
    return F(k, 1 << BITS), F(k + 1, 1 << BITS)


def mul(a, b):
    v = [x*y for x in a for y in b]
    return min(v), max(v)


def recip(a):
    return 1/a[1], 1/a[0]


def dec(x):
    return f"{x.numerator/x.denominator:.30f}"


total = (F(0), F(0))
rows = []
for q in (2, 3, 4, 5, 7):
    lq = log_interval(q)
    root = sqrt_interval(q)
    weight = mul(lq, recip(root))
    # phi_q=pi*log(q) lies in (0,2*pi).  The exact bilateral
    # commutator norm factor after c=2/pi is max(log(q),2-log(q)).
    factor = (F(2)-lq[1], F(2)-lq[0]) if q == 2 else lq
    term = mul(weight, factor)
    total = total[0] + term[0], total[1] + term[1]
    rows.append((q, term))

assert F(4887, 1000) < total[0]
assert total[1] < F(4888, 1000)

for q, term in rows:
    print(q, dec(term[0]), dec(term[1]))
print("sum_lower", dec(total[0]))
print("sum_upper", dec(total[1]))
print("certified", "4.887 < frequencywise_triangle_sum < 4.888")
