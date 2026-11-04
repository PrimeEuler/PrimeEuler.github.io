#!/usr/bin/env python3
"""Exact symbolic transported q=3,5 same-translation coefficient gate.

The fixed convention is the one frozen in v15.357:
  D_sigma(x;L) = s(x-sigma*L)-s(x), s(x)=1-(x mod 2).
For T_(q,sigma)=M_(alpha_q D_sigma) U_(sigma L_q), the two terms at
translation tau*L5-sigma*L3 have the (normalization-free) coefficient

 D_sigma(x+sigma*L3;L3) D_tau(x+sigma*L3;L5)
 + D_-tau(x-tau*L5;L5) D_-sigma(x-tau*L5;L3).

All symbolic identities below are in Q[A,B], A=log(3), B=log(5).
"""
from fractions import Fraction as F
from math import isqrt

BITS = 320


def log_interval(q):
    r = F(q - 1, q + 1)
    kmax = 2 * BITS + 32
    s = 2 * sum((r ** (2*k + 1) / (2*k + 1) for k in range(kmax)), F(0))
    e = 2 * r ** (2*kmax + 1) / ((2*kmax + 1) * (1-r*r))
    return s, s + e


def sqrt_interval(q):
    k = isqrt(q << (2*BITS))
    return F(k, 1 << BITS), F(k + 1, 1 << BITS)


A_I, B_I = log_interval(3), log_interval(5)


class P:
    """Sparse polynomial in A,B with rational coefficients."""
    def __init__(self, terms=()):
        self.t = {ij: F(c) for ij, c in dict(terms).items() if c}

    def __add__(self, other):
        other = other if isinstance(other, P) else P({(0, 0): other})
        keys = set(self.t) | set(other.t)
        return P({k: self.t.get(k, 0) + other.t.get(k, 0) for k in keys})

    __radd__ = __add__

    def __neg__(self):
        return P({k: -v for k, v in self.t.items()})

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return P({(0, 0): other}) - self

    def __mul__(self, other):
        other = other if isinstance(other, P) else P({(0, 0): other})
        out = {}
        for (i, j), c in self.t.items():
            for (k, l), d in other.t.items():
                out[(i+k, j+l)] = out.get((i+k, j+l), 0) + c*d
        return P(out)

    __rmul__ = __mul__

    def interval(self):
        out = (F(0), F(0))
        for (i, j), c in self.t.items():
            ai = (A_I[0]**i, A_I[1]**i)
            bj = (B_I[0]**j, B_I[1]**j)
            vals = [c*x*y for x in ai for y in bj]
            term = (min(vals), max(vals))
            out = (out[0] + term[0], out[1] + term[1])
        return out

    def __eq__(self, other):
        other = other if isinstance(other, P) else P({(0, 0): other})
        return self.t == other.t

    def __repr__(self):
        return repr(self.t)


ONE, A, B = P({(0, 0): 1}), P({(1, 0): 1}), P({(0, 1): 1})


def certified_wrap(x):
    lo, hi = x.interval()
    for k in range(-4, 5):
        if 2*k < lo and hi < 2*(k+1):
            return k
    raise AssertionError((lo, hi))


def saw(x):
    k = certified_wrap(x)
    return ONE + 2*k - x


def D(sig, x, L):
    return saw(x - sig*L) - saw(x)


def G(sig, tau, x):
    y, z = x + sig*A, x - tau*B
    return D(sig, y, A)*D(tau, y, B) + D(-tau, z, B)*D(-sig, z, A)


group_cuts = {
    (+1, +1): [0, B-A, 2-A, B, 2],
    (+1, -1): [0, 2-B, 2-A, 4-A-B, 2],
    (-1, +1): [0, A+B-2, A, B, 2],
    (-1, -1): [0, 2-B, A, A+2-B, 2],
}
expected = {
    (+1, +1): [2*A*B-4*A, 4-2*A-2*B+2*A*B,
                8-4*A-4*B+2*A*B, 4-2*A-2*B+2*A*B],
    (+1, -1): [2*A+2*B-2*A*B, 4*A-2*A*B,
                2*A+2*B-2*A*B, -8+4*A+4*B-2*A*B],
    (-1, +1): [-8+4*A+4*B-2*A*B, 2*A+2*B-2*A*B,
                4*A-2*A*B, 2*A+2*B-2*A*B],
    (-1, -1): [4-2*A-2*B+2*A*B, 8-4*A-4*B+2*A*B,
                4-2*A-2*B+2*A*B, 2*A*B-4*A],
}

for key, cuts in group_cuts.items():
    for i, (left, right) in enumerate(zip(cuts, cuts[1:])):
        left = left if isinstance(left, P) else P({(0, 0): left})
        right = right if isinstance(right, P) else P({(0, 0): right})
        assert (right-left).interval()[0] > 0
        assert G(*key, (left+right)*F(1, 2)) == expected[key][i]

# Common partition for the row sum of the four distinct translations.
cuts = [0, 2-B, B-A, A+B-2, 2-A, A, 4-A-B, A+2-B, B, 2]
rows = []
for left, right in zip(cuts, cuts[1:]):
    left = left if isinstance(left, P) else P({(0, 0): left})
    right = right if isinstance(right, P) else P({(0, 0): right})
    assert (right-left).interval()[0] > 0
    x = (left+right)*F(1, 2)
    row = P()
    for sig in (+1, -1):
        for tau in (+1, -1):
            value = G(sig, tau, x)
            lo, hi = value.interval()
            assert hi < 0 or lo > 0
            row += -value if hi < 0 else value
    rows.append(row)

row_max = 12 - 4*B
assert row_max in rows
for row in rows:
    assert (row_max-row).interval()[0] >= 0

# Restoring alpha_3 alpha_5 = A*B/(4*sqrt(15)) gives
# B_35 = A*B*(3-B)/sqrt(15).  The block is self-adjoint, so the column
# Schur sum equals the row sum after the opposite-translation relabeling.
numer = A*B*(3-B)
nlo, nhi = numer.interval()
slo, shi = sqrt_interval(15)
bound = (nlo/shi, nhi/slo)
assert F(634, 1000) < bound[0]
assert bound[1] < F(635, 1000)

print("group_piece_counts", {k: len(v) for k, v in expected.items()})
print("row_sum_max_symbolic", row_max)
print("q35_cross_block_lower", float(bound[0]))
print("q35_cross_block_upper", float(bound[1]))
print("certified", "0.634 < B_35 = log(3)log(5)(3-log(5))/sqrt(15) < 0.635")
print("scope", "q=3,5 self-adjoint commutator cross block only")
