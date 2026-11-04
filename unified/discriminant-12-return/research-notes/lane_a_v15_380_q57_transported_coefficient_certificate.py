#!/usr/bin/env python3
"""Exact symbolic transported q=5,7 same-translation coefficient gate."""
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


A_I, B_I = log_interval(5), log_interval(7)


class P:
    """Sparse polynomial in A=log(5), B=log(7)."""
    def __init__(self, terms=()):
        self.t = {ij: F(c) for ij, c in dict(terms).items() if c}

    def __add__(self, other):
        other = other if isinstance(other, P) else P({(0, 0): other})
        keys = set(self.t) | set(other.t)
        return P({k: self.t.get(k, 0)+other.t.get(k, 0) for k in keys})

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
                out[(i+k, j+l)] = out.get((i+k, j+l), 0)+c*d
        return P(out)

    __rmul__ = __mul__

    def interval(self):
        out = (F(0), F(0))
        for (i, j), c in self.t.items():
            vals = [c*x*y for x in (A_I[0]**i, A_I[1]**i)
                          for y in (B_I[0]**j, B_I[1]**j)]
            out = (out[0]+min(vals), out[1]+max(vals))
        return out

    def __eq__(self, other):
        other = other if isinstance(other, P) else P({(0, 0): other})
        return self.t == other.t

    def __hash__(self):
        return hash(tuple(sorted(self.t.items())))

    def __repr__(self):
        return repr(self.t)


ONE, A, B = P({(0, 0): 1}), P({(1, 0): 1}), P({(0, 1): 1})


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


# These are exactly all discontinuities of G_(sigma,tau): each D factor
# jumps only at zero or at its signed shift.
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
        assert len(group_values[(sig, tau)]) == 4

# Combine identical translations before absolute values on the common
# partition.  Certify every sign and the exact global maximum.
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

row_max = 12*ONE - 4*B
assert row_max in rows
for row in rows:
    assert (row_max-row).interval()[0] >= 0

# alpha_5 alpha_7=A*B/(4sqrt(35)); hence B_57=AB(3-B)/sqrt(35).
numer = A*B*(3-B)
nlo, nhi = numer.interval()
slo, shi = sqrt_interval(35)
bound = (nlo/shi, nhi/slo)
assert F(558, 1000) < bound[0]
assert bound[1] < F(559, 1000)

print("group_piece_counts", {k: len(v) for k, v in group_values.items()})
print("common_partition_cells", len(rows))
print("row_sum_max_symbolic", row_max)
print("q57_cross_block_lower", float(bound[0]))
print("q57_cross_block_upper", float(bound[1]))
print("certified", "0.558 < B_57 = log(5)log(7)(3-log(7))/sqrt(35) < 0.559")
print("scope", "q=5,7 self-adjoint commutator cross block only")


