#!/usr/bin/env python3
"""Exact symbolic transported q=2,4 same-translation coefficient gate."""
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


A_I = log_interval(2)


class P:
    """Sparse polynomial in A=log(2); the q=4 shift is exactly 2A."""
    def __init__(self, terms=()):
        self.t = {i: F(c) for i, c in dict(terms).items() if c}

    def __add__(self, other):
        other = other if isinstance(other, P) else P({0: other})
        keys = set(self.t) | set(other.t)
        return P({k: self.t.get(k, 0)+other.t.get(k, 0) for k in keys})

    __radd__ = __add__

    def __neg__(self):
        return P({k: -v for k, v in self.t.items()})

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return P({0: other}) - self

    def __mul__(self, other):
        other = other if isinstance(other, P) else P({0: other})
        out = {}
        for i, c in self.t.items():
            for j, d in other.t.items():
                out[i+j] = out.get(i+j, 0)+c*d
        return P(out)

    __rmul__ = __mul__

    def interval(self):
        out = (F(0), F(0))
        for i, c in self.t.items():
            vals = [c*x**i for x in A_I]
            out = (out[0]+min(vals), out[1]+max(vals))
        return out

    def __eq__(self, other):
        other = other if isinstance(other, P) else P({0: other})
        return self.t == other.t

    def __hash__(self):
        return hash(tuple(sorted(self.t.items())))

    def __repr__(self):
        return repr(self.t)


ONE, A = P({0: 1}), P({1: 1})
B = 2*A


def certified_wrap(x):
    if not x.t:
        return 0
    lo, hi = x.interval()
    for k in range(-4, 5):
        if 2*k < lo and hi < 2*(k+1):
            return k
    raise AssertionError((lo, hi))


def mod2_cut(x):
    if not x.t:
        return x
    return x - 2*certified_wrap(x)


def saw(x):
    return ONE + 2*certified_wrap(x) - x


def D(sig, x, L):
    return saw(x-sig*L)-saw(x)


def G(sig, tau, x):
    y, z = x+sig*A, x-tau*B
    return D(sig, y, A)*D(tau, y, B) + D(-tau, z, B)*D(-sig, z, A)


def ordered(values):
    values = list(set(values))
    values.sort(key=lambda p: float(sum(p.interval())/2))
    for left, right in zip(values, values[1:]):
        assert (right-left).interval()[0] > 0
    return values


group_cuts = {}
group_values = {}
for sig in (+1, -1):
    for tau in (+1, -1):
        cuts = ordered({P(), mod2_cut(-sig*A), mod2_cut(tau*B),
                        mod2_cut(tau*B-sig*A), 2*ONE})
        assert cuts[0] == 0 and cuts[-1] == 2
        group_cuts[(sig, tau)] = cuts
        group_values[(sig, tau)] = [G(sig, tau, (l+r)*F(1, 2))
                                    for l, r in zip(cuts, cuts[1:])]

cuts = ordered(set().union(*group_cuts.values()))
rows = []
for left, right in zip(cuts, cuts[1:]):
    x = (left+right)*F(1, 2)
    row = P()
    for sig in (+1, -1):
        for tau in (+1, -1):
            value = G(sig, tau, x)
            lo, hi = value.interval()
            assert hi < 0 or lo > 0
            row += -value if hi < 0 else value
    rows.append(row)

row_max = 4*ONE + 10*A - 8*A*A
assert row_max in rows
for row in rows:
    assert (row_max-row).interval()[0] >= 0

# The established q=4 weight is w_4=log(2)/2, exactly equal to
# alpha_4=log(4)/(2sqrt(4)).  With alpha_2=A/(2sqrt(2)), the product is
# A^2/(4sqrt(2)); hence B_24=A^2(4+10A-8A^2)/(4sqrt(2)).
numer = A*A*row_max
nlo, nhi = numer.interval()
slo, shi = sqrt_interval(2)
bound = (nlo/(4*shi), nhi/(4*slo))
assert F(601, 1000) < bound[0]
assert bound[1] < F(602, 1000)

print("group_piece_counts", {k: len(v) for k, v in group_values.items()})
print("common_partition_cells", len(rows))
print("row_sum_max_symbolic", row_max)
print("q24_cross_block_lower", float(bound[0]))
print("q24_cross_block_upper", float(bound[1]))
print("certified", "0.601 < B_24 = log(2)^2(2+5log(2)-4log(2)^2)/(2sqrt(2)) < 0.602")
print("normalization", "w_4=log(2)/2=log(4)/(2sqrt(4))")
print("scope", "q=2,4 self-adjoint commutator cross block only")
