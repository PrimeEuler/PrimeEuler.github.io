#!/usr/bin/env python3
"""Exact-rational NO-GO for generic adjoint pairing of the q=3,5 block."""
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
overlap_triangle = mul(mul(b3, b5), L5)
generic_adjoint_pair = (2 * overlap_triangle[0], 2 * overlap_triangle[1])

# The universal estimate
#   ||sum_j s_j(A_j+A_j^*)|| <= 2 sum_j ||A_j||
# is sharp even for the audited sign pattern (+,-,-,+): on C, choose
# A_j=s_j*a_j*I.  The exact scalar example below checks this forcing.
signs = (+1, -1, -1, +1)
magnitudes = (F(1, 7), F(2, 7), F(3, 7), F(4, 7))
lhs_sharp_example = sum(
    F(s) * (F(s) * a + F(s) * a) for s, a in zip(signs, magnitudes)
)
rhs_generic = 2 * sum(magnitudes)
assert lhs_sharp_example == rhs_generic

assert F(1468, 1000) < generic_adjoint_pair[0]
assert generic_adjoint_pair[1] < F(1470, 1000)

print("q35_generic_adjoint_pair_lower", dec(generic_adjoint_pair[0]))
print("q35_generic_adjoint_pair_upper", dec(generic_adjoint_pair[1]))
print("sharp_scalar_example", lhs_sharp_example, rhs_generic)
print("certified", "1.468 < 2*C_q35 < 1.470; generic A+A* pairing is sharp")
