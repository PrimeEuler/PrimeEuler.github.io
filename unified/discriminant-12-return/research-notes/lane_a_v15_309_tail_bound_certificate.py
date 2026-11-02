#!/usr/bin/env python3
"""Exact-rational certificate for the sharpened all-offset K_full tail bound.

No machine transcendental values enter the asserted inequalities.  Logs, pi,
e^-1 and square roots are enclosed by rational intervals.
"""
from fractions import Fraction as F
from math import factorial, isqrt

BITS = 320
N0 = 256001


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b):
    v = [x * y for x in a for y in b]
    return min(v), max(v)


def scale(a, q):
    return mul(a, (F(q), F(q)))


def recip(a):
    assert a[0] > 0
    return 1 / a[1], 1 / a[0]


def sqrt_interval(q, bits=BITS):
    assert q > 0
    k = isqrt((q.numerator << (2 * bits)) // q.denominator)
    lo, hi = F(k, 1 << bits), F(k + 1, 1 << bits)
    assert lo * lo <= q <= hi * hi
    return lo, hi


def log_interval(q, bits=BITS):
    # log(q) = 2 sum_{k>=0} r^(2k+1)/(2k+1), r=(q-1)/(q+1).
    r = F(q - 1, q + 1)
    K = 2 * bits + 32
    total = 2 * sum((r ** (2 * k + 1) / (2 * k + 1) for k in range(K)), F(0))
    tail = 2 * r ** (2 * K + 1) / ((2 * K + 1) * (1 - r * r))
    return total, total + tail


def atan_recip(q, bits=BITS):
    K = bits // 3 + 32
    total = sum((F((-1) ** k, (2 * k + 1) * q ** (2 * k + 1)) for k in range(K)), F(0))
    nxt = F((-1) ** K, (2 * K + 1) * q ** (2 * K + 1))
    return min(total, total + nxt), max(total, total + nxt)


def exp_minus_one(bits=BITS):
    K = 1
    while F(1, factorial(K + 1)) > F(1, 1 << (bits + 24)):
        K += 1
    total = sum((F((-1) ** j, factorial(j)) for j in range(K + 1)), F(0))
    nxt = F((-1) ** (K + 1), factorial(K + 1))
    return min(total, total + nxt), max(total, total + nxt)


def dec(q, digits=18):
    return f"{q.numerator / q.denominator:.{digits}f}"


# Certified constants.
a5, a239 = atan_recip(5), atan_recip(239)
pi = (16 * a5[0] - 4 * a239[1], 16 * a5[1] - 4 * a239[0])
logs = {q: log_interval(q) for q in (2, 3, 5, 7, 10)}
roots = {q: sqrt_interval(F(q)) for q in (2, 3, 5, 7, 17)}

# q=2,4 share one phase: 2 log(2) sin(t) (1/sqrt(2)+cos(t)).
# Its positive maximizing cosine is x=(sqrt(17)-1)/(4sqrt(2)).
x = scale(mul(add(roots[17], (F(-1), F(-1))), recip(roots[2])), F(1, 4))
one_minus_x2 = add((F(1), F(1)), scale(mul(x, x), -1))
pair = scale(mul(mul(logs[2], sqrt_interval(one_minus_x2[1])), add(recip(roots[2]), x)), 2)

# The remaining q=3,5,7 amplitudes are bounded independently.
rest = (F(0), F(0))
for q in (3, 5, 7):
    rest = add(rest, scale(mul(logs[q], recip(roots[q])), 2))

# Physical nonprime displacement from pi/2 for n>=N0, directly from
# suzuki_certified_remote_z.py's standard-precision enclosure.
em1 = exp_minus_one()
s0 = mul(em1, recip(add((F(1), F(1)), scale(mul(mul(em1, em1), mul(em1, em1)), -1))))
nonprime_rem = F(4, 9 * 256000**2) + F(55, 81 * 256000**3)
eps_np = F(1 + 4 * s0[1], N0) / pi[0] + nonprime_rem

W = add(add(pair, rest), (F(0), eps_np))
Z = add(scale(pi, F(1, 2)), W)

# With H_- and H_+ norms <= pi/2 and c=2/pi, splitting Z=(pi/2)I+W gives
# ||B0|| <= 2 Wbar + pi/2 + Zbar/(pi*N0).
B0 = 2 * W[1] + pi[1] / 2 + Z[1] / (pi[0] * N0)

# For either step-two parity lattice, p_n <= L/n, L<1.436, and
# sum_{j>=0}(N0+2j)^-2 <= N0^-2 + (2N0)^-1.
Lbar = F(359, 250)
pole = 2 * Lbar * Lbar * (F(1, N0 * N0) + F(1, 2 * N0))
Mtail = B0 + pole

assert pair[1] < F(145547, 100000)
assert rest[1] < F(4179064, 1000000)
assert W[1] < F(5634544, 1000000)
assert Mtail < F(1284, 100)

# A simple certified finite stopping point for C=2, b<=10.45, Mtail<12.84.
Nstop = 400_000_000_000
log_stop = scale(logs[10], 11)  # log(10^11) < log((Nstop+2)/4)
margin = log_stop[0] - F(2) - F(1045, 100) - F(1284, 100)
assert margin > 0

print("pair_upper", dec(pair[1], 30))
print("rest_upper", dec(rest[1], 30))
print("nonprime_upper", dec(eps_np, 30))
print("W_upper", dec(W[1], 30))
print("Z_upper", dec(Z[1], 30))
print("B0_upper", dec(B0, 30))
print("pole_upper", dec(pole, 30))
print("Mtail_upper", dec(Mtail, 30))
print("certified_Mtail_lt", "12.84")
print("certified_stopping_N", Nstop)
print("stopping_margin_lower", dec(margin, 30))
