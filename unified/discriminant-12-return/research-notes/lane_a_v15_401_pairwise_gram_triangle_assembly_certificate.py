#!/usr/bin/env python3
"""Exact-interval assembly of all ten transported pair certificates."""
from fractions import Fraction as F
from math import isqrt

BITS = 320


def log_interval(q):
    r = F(q - 1, q + 1)
    kmax = 2 * BITS + 32
    s = 2 * sum((r ** (2*k + 1) / (2*k + 1) for k in range(kmax)), F(0))
    e = 2 * r ** (2*kmax + 1) / ((2*kmax + 1) * (1-r*r))
    return I(s, s + e)


def sqrt_integer_interval(q):
    k = isqrt(q << (2*BITS))
    return I(F(k, 1 << BITS), F(k + 1, 1 << BITS))


def sqrt_fraction_interval(x):
    assert x > 0
    scaled = (x.numerator << (2*BITS)) // x.denominator
    k = isqrt(scaled)
    return F(k, 1 << BITS), F(k + 1, 1 << BITS)


class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other if isinstance(other, I) else -I(other))

    def __rsub__(self, other):
        return I(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        vals = (self.lo*other.lo, self.lo*other.hi,
                self.hi*other.lo, self.hi*other.hi)
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        assert 0 < other.lo
        return self * I(1/other.hi, 1/other.lo)

    def __repr__(self):
        return f"I({float(self.lo):.16g}, {float(self.hi):.16g})"


L2, L3, L5, L7 = (log_interval(q) for q in (2, 3, 5, 7))
L4 = 2*L2
S2, S3, S5, S6, S7, S10, S14, S15, S21, S35 = (
    sqrt_integer_interval(q) for q in (2, 3, 5, 6, 7, 10, 14, 15, 21, 35)
)

# Exact diagonal block contributions b_q^2, b_q=log(q)/sqrt(q).
diagonal = L2*L2/F(2) + L3*L3/F(3) + L4*L4/F(4) + L5*L5/F(5) + L7*L7/F(7)

# The ten independently audited self-adjoint cross-block constants.
pairs = {
    "23": 2*L2*L3/S6,
    "24": L2*L2*(2 + 5*L2 - 4*L2*L2)/(2*S2),
    "25": L2*L5*(4 + 6*L2 + 2*L5 - 4*L2*L5)/(4*S10),
    "27": L2*L7*(3 - L7)/S14,
    "34": 2*L3*L2/S3,
    "35": L3*L5*(3 - L5)/S15,
    "37": L3*L7*(3 - L7)/S21,
    "45": L5*L2*(16 - 12*L2 + 8*L5*L2 - 6*L5)/(4*S5),
    "47": L7*L2*(3 - L7)/S7,
    "57": L5*L7*(3 - L7)/S35,
}
pair_sum = sum(pairs.values(), I(0))
gram_square = diagonal + pair_sum

root_lo = sqrt_fraction_interval(gram_square.lo)[0]
root_hi = sqrt_fraction_interval(gram_square.hi)[1]

assert F(2892, 1000) < root_lo
assert root_hi < F(2893, 1000)
assert F(2535946, 1000000) < root_lo

print("diagonal_square_contribution", float(diagonal.lo), float(diagonal.hi))
for key in sorted(pairs):
    print("pair", key, float(pairs[key].lo), float(pairs[key].hi))
print("pair_sum", float(pair_sum.lo), float(pair_sum.hi))
print("gram_square", float(gram_square.lo), float(gram_square.hi))
print("gram_triangle_bound", float(root_lo), float(root_hi))
print("certified", "2.892 < B_GramTriangle < 2.893")
print("target_comparison", "B_GramTriangle > 2.535946; this assembly route does not close")
print("scope", "valid full five-frequency commutator bound from diagonal squares plus ten self-adjoint pair bounds; triangle assembly only")
