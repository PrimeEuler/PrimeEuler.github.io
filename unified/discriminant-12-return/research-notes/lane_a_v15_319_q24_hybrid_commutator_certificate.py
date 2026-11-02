#!/usr/bin/env python3
"""Exact-rational q=2,4 paired / q=3,5,7 commutator hybrid bound."""
from fractions import Fraction as F
from math import isqrt

BITS = 320


def add(a, b): return a[0] + b[0], a[1] + b[1]
def mul(a, b):
    v = [x*y for x in a for y in b]
    return min(v), max(v)
def scale(a, q): return mul(a, (F(q), F(q)))
def recip(a): return 1/a[1], 1/a[0]


def log_interval(q):
    r = F(q - 1, q + 1)
    K = 2 * BITS + 32
    s = 2 * sum((r ** (2*k + 1) / (2*k + 1) for k in range(K)), F(0))
    e = 2 * r ** (2*K + 1) / ((2*K + 1) * (1-r*r))
    return s, s + e


def sqrt_interval(q):
    k = isqrt((q.numerator << (2*BITS)) // q.denominator)
    return F(k, 1 << BITS), F(k + 1, 1 << BITS)


def dec(x): return f"{x.numerator/x.denominator:.30f}"


logs = {q: log_interval(q) for q in (2, 3, 5, 7)}
roots = {q: sqrt_interval(F(q)) for q in (2, 3, 5, 7, 17)}

# q=2,4 physical signal: 2 log(2) sin(t)(1/sqrt(2)+cos(t)).
x = scale(mul(add(roots[17], (F(-1), F(-1))), recip(roots[2])), F(1, 4))
one_minus_x2 = add((F(1), F(1)), scale(mul(x, x), -1))
pair = scale(mul(mul(logs[2], sqrt_interval(one_minus_x2[1])),
                 add(recip(roots[2]), x)), 2)

# Generic commutator bound after c=2/pi:
# ||(c/2)[Z_pair,Hminus]|| <= ||Z_pair||, hence pair[1].
# Retain exact single-frequency sawtooth norms for q=3,5,7.
rest = (F(0), F(0))
for q in (3, 5, 7):
    weight = mul(logs[q], recip(roots[q]))
    term = mul(weight, logs[q])
    rest = add(rest, term)

hybrid = add(pair, rest)
assert F(4741, 1000) < hybrid[0]
assert hybrid[1] < F(4742, 1000)

print("q24_pair_upper", dec(pair[1]))
print("q357_lower", dec(rest[0]))
print("q357_upper", dec(rest[1]))
print("hybrid_lower", dec(hybrid[0]))
print("hybrid_upper", dec(hybrid[1]))
print("certified", "4.741 < q24-paired hybrid bound < 4.742")
