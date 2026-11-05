#!/usr/bin/env python3
"""Exact-interval budget required for a cancellation-preserving cross-pair gate."""
from fractions import Fraction as F
from math import isqrt

BITS = 320


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


def log_interval(q):
    r = F(q - 1, q + 1)
    kmax = 2 * BITS + 32
    s = 2 * sum((r ** (2*k + 1) / (2*k + 1) for k in range(kmax)), F(0))
    e = 2 * r ** (2*kmax + 1) / ((2*kmax + 1) * (1-r*r))
    return I(s, s + e)


def sqrt_integer_interval(q):
    k = isqrt(q << (2*BITS))
    return I(F(k, 1 << BITS), F(k + 1, 1 << BITS))


L2, L3, L5, L7 = (log_interval(q) for q in (2, 3, 5, 7))
L4 = 2*L2
S2, S3, S5, S6, S7, S10, S14, S15, S21, S35 = (
    sqrt_integer_interval(q) for q in (2, 3, 5, 6, 7, 10, 14, 15, 21, 35)
)

# The exact diagonal contribution used in the audited v15.401 assembly.
diagonal = L2*L2/F(2) + L3*L3/F(3) + L4*L4/F(4) + L5*L5/F(5) + L7*L7/F(7)

# Reconstruct all ten independently audited closed forms exactly as v15.401.
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

target = F(2535946, 1000000)
target_square = target * target
allowed_cross = I(target_square) - diagonal
required_reduction = pair_sum - allowed_cross
fraction = required_reduction / pair_sum

# Rigorous, human-readable enclosures.
assert F(4249, 1000) < allowed_cross.lo
assert allowed_cross.hi < F(4250, 1000)
assert F(1932, 1000) < required_reduction.lo
assert required_reduction.hi < F(1933, 1000)
assert F(312, 1000) < fraction.lo
assert fraction.hi < F(313, 1000)

print("target", float(target))
print("target_square", float(target_square))
print("diagonal_square", float(diagonal.lo), float(diagonal.hi))
print("audited_pair_sum", float(pair_sum.lo), float(pair_sum.hi))
print("maximum_admissible_joint_cross", float(allowed_cross.lo), float(allowed_cross.hi))
print("minimum_required_cross_pair_reduction", float(required_reduction.lo), float(required_reduction.hi))
print("minimum_required_fraction", float(fraction.lo), float(fraction.hi))
print("certified", "4.249 < admissible joint-cross budget < 4.250")
print("certified", "1.932 < required reduction < 1.933")
print("certified", "31.2% < required fraction < 31.3%")
print("scope", "necessary budget for improving the audited Gram-triangle route to 2.535946; not a construction, lower bound, or complete-tail certificate")
