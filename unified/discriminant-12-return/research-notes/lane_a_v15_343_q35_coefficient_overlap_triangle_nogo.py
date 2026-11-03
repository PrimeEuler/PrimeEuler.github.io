#!/usr/bin/env python3
"""Exact-rational q=3,5 signed coefficient-overlap triangle NO-GO."""
from fractions import Fraction as F
from math import isqrt

BITS = 320


def mul(a, b):
    v = [x * y for x in a for y in b]
    return min(v), max(v)


def recip(a):
    return 1 / a[1], 1 / a[0]


def log_interval(q):
    r = F(q - 1, q + 1)
    kmax = 2 * BITS + 32
    s = 2 * sum((r ** (2 * k + 1) / (2 * k + 1) for k in range(kmax)), F(0))
    e = 2 * r ** (2 * kmax + 1) / ((2 * kmax + 1) * (1 - r * r))
    return s, s + e


def sqrt_interval(q):
    k = isqrt((q.numerator << (2 * BITS)) // q.denominator)
    return F(k, 1 << BITS), F(k + 1, 1 << BITS)


def dec(x):
    return f"{x.numerator / x.denominator:.30f}"


L3, L5 = log_interval(3), log_interval(5)
b3 = mul(L3, recip(sqrt_interval(F(3))))
b5 = mul(L5, recip(sqrt_interval(F(5))))
generic_product = mul(b3, b5)

# Exact branch geometry for both T_3^*T_5 and T_3T_5^* gives two HH
# maxima and two LH maxima among the four signed products.  Factoring
# k_q=L_q/(2 sqrt(q)) yields
# 2*k3*k5*(L3*L5 + (2-L3)*L5) = b3*b5*L5.
overlap_triangle = mul(generic_product, L5)

assert F(456, 1000) < generic_product[0]
assert generic_product[1] < F(457, 1000)
assert F(734, 1000) < overlap_triangle[0]
assert overlap_triangle[1] < F(735, 1000)
assert generic_product[1] < overlap_triangle[0]

print("generic_q35_product_upper", dec(generic_product[1]))
print("q35_overlap_triangle_lower", dec(overlap_triangle[0]))
print("q35_overlap_triangle_upper", dec(overlap_triangle[1]))
print("certified", "0.734 < C_q35 < 0.735 and b3*b5 < C_q35 = b3*b5*log(5)")
