#!/usr/bin/env python3
"""Suzuki R=4 outward all-arc B^4 certificate attempt.

Promotes the independently audited v15.664 R=3 method to every v15.650
R=4 arc.  It uses exact-rational log/sqrt/cut/word-state enclosures and
conservative IEEE-754 sparse-product/row-sum error envelopes.

The result, whether pass or fail, concerns R=4 only.  It is not a radius-16
certificate and is not a full Suzuki conclusion.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import time
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
from math import isqrt
from multiprocessing import Pool

import numpy as np

PTH = (
    "unified/discriminant-12-return/research-notes/"
    "lane_a_v15_657_suzuki_positive_polynomial_small_radius_probe.py"
)
sp = spec_from_file_location("producer", PTH)
producer = module_from_spec(sp)
sp.loader.exec_module(producer)

# Exact rational intervals, unchanged from audited v15.664 except R=4.
P = 10**45
N = 220
QS = (2, 3, 4, 5, 7)
R = 4


def add(a, b): return a[0] + b[0], a[1] + b[1]
def sub(a, b): return a[0] - b[1], a[1] - b[0]


def mul(a, b):
    values = [x * y for x in a for y in b]
    return min(values), max(values)


def scale(a, s): return mul(a, (F(s), F(s)))


def div(a, b):
    assert b[0] > 0
    return mul(a, (1 / b[1], 1 / b[0]))


def logbound(q):
    x = F(q - 1, q + 1)
    total = sum((2 * x ** (2 * k + 1) / F(2 * k + 1) for k in range(N)), F())
    error = 2 * x ** (2 * N + 1) / ((2 * N + 1) * (1 - x * x))
    return total, total + error


def sqrtbound(q):
    k = isqrt(q * P * P)
    return F(k, P), F(k + 1, P)


LS = {q: logbound(q) for q in QS}
ALPHA = {q: div(LS[q], scale(sqrtbound(q), 2)) for q in QS}


def mod2(a):
    assert a[0] // 2 == a[1] // 2, (float(a[0]), float(a[1]))
    return sub(a, scale((F(2), F(2)), a[0] // 2))


def saw(a): return sub((F(1), F(1)), mod2(a))
def D(x, s, length): return sub(saw(sub(x, scale(length, s))), saw(x))


def G(x, s, t, a, b):
    y = add(x, scale(a, s))
    z = sub(x, scale(b, t))
    return add(mul(D(y, s, a), D(y, t, b)),
               mul(D(z, -t, b), D(z, -s, a)))


TOL = F(1, 10**12)
INPUT_TOL = F(1, 10**15)
STATE_TOL = F(1, 10**15)
for q in QS:
    log_float = F.from_float(float(producer.L[q]))
    assert LS[q][0] - INPUT_TOL < log_float < LS[q][1] + INPUT_TOL
    sqrt_float = F.from_float(float(np.sqrt(q)))
    sqrt_interval = sqrtbound(q)
    assert sqrt_interval[0] - INPUT_TOL < sqrt_float < sqrt_interval[1] + INPUT_TOL

# Certify every finite word-state coefficient lies within 1e-15 of its float replay.
max_state_error = F()
for q, r in combinations(QS, 2):
    for s, t in product((-1, 1), repeat=2):
        a, b = LS[q], LS[r]
        cuts = [(F(), F()), (F(2), F(2)), mod2(scale(a, -s)),
                mod2(scale(b, t)), mod2(sub(scale(b, t), scale(a, s)))]
        cuts = sorted(cuts, key=lambda z: z[0])
        for left, right in zip(cuts, cuts[1:]):
            assert left[1] < right[0]
            x = (left[1] + right[0]) / 2
            xi = (x, x)
            exact = mul((F(s * t), F(s * t)),
                        mul(ALPHA[q], mul(ALPHA[r], G(xi, s, t, a, b))))
            xf = float(x)
            vf = (s * t * producer.ALPHA[q] * producer.ALPHA[r]
                  * producer.G(xf, s, t, producer.L[q], producer.L[r]))
            value = F.from_float(float(vf))
            error = max(abs(value - exact[0]), abs(value - exact[1]))
            max_state_error = max(max_state_error, error)
            assert error < STATE_TOL, (q, r, s, t, float(error))


def cut_interval(k):
    value = (F(), F())
    for ki, q in zip(k, (2, 3, 5, 7)):
        value = add(value, scale(LS[q], -ki))
    return mod2(value)


EXACT = []
for k0 in range(-R - 1, R + 2):
    for k1, k2, k3 in product(range(-R, R + 1), repeat=3):
        EXACT.append(cut_interval((k0, k1, k2, k3)))
EXACT.sort(key=lambda z: z[0])
for a, b in zip(EXACT, EXACT[1:]):
    assert a[1] < b[0]

FCUTS = producer.cuts(R)
assert len(EXACT) == len(FCUTS) == 8019
for interval, cut in zip(EXACT, FCUTS):
    cut_fraction = F.from_float(float(cut))
    assert interval[0] - TOL < cut_fraction < interval[1] + TOL

MARGIN = F(1, 10**6)
MID = []
for i, cut in enumerate(FCUTS):
    wrap = i + 1 == len(FCUTS)
    right = float(FCUTS[(i + 1) % len(FCUTS)]) + (2 if wrap else 0)
    unwrapped_midpoint = (float(cut) + right) / 2
    midpoint = unwrapped_midpoint % 2
    midpoint_fraction = F.from_float(unwrapped_midpoint)
    left_interval = EXACT[i]
    right_interval = EXACT[(i + 1) % len(EXACT)]
    right_low = right_interval[0] + (2 if wrap else 0)
    assert midpoint_fraction > left_interval[1] + MARGIN
    assert midpoint_fraction < right_low - MARGIN
    MID.append(midpoint)

U = F(1, 2**53)


def gamma(k):
    value = F(k) * U
    assert value < 1
    return value / (1 - value)


def rowstats(matrix):
    counts = np.diff(matrix.indptr)
    k = int(counts.max())
    observed = float(np.asarray(abs(matrix).sum(axis=1)).ravel().max())
    observed_fraction = F.from_float(observed)
    return observed_fraction / (1 - gamma(k)), k


# The coefficient and floating-point reserve is unchanged from audited v15.664.
E = F(1, 10**9)
TARGET = F(41, 10)**4


def work(x):
    b = producer.assemble(R, x)
    b2 = b @ b
    b4 = b2 @ b2
    m, k1 = rowstats(b)
    c2, k2 = rowstats(b2)
    c4, k4 = rowstats(b4)
    r2 = gamma(2 * k1) * m * m
    r4 = r2 * (m * m + c2) + gamma(2 * k2) * c2 * c2
    perturb = (m + E)**4 - m**4
    total = c4 + r4 + perturb
    return total, x, k1, k2, k4


if __name__ == "__main__":
    print("max_exact_word_state_error", float(max_state_error),
          "cuts", len(MID), flush=True)
    start = time.time()
    best = (F(), None, None, None, None)
    with Pool(6) as pool:
        for count, result in enumerate(pool.imap_unordered(work, MID, chunksize=1), 1):
            if result[0] > best[0]:
                best = result
            if count % 250 == 0:
                print("progress", count, "root_bound", float(best[0])**0.25,
                      "seconds", time.time() - start, flush=True)
    print("CERTIFIED_R4_B4", len(MID), float(best[0]),
          float(best[0])**0.25, best[1:], time.time() - start)
    print("TARGET4", float(TARGET), "PASS", best[0] < TARGET)
