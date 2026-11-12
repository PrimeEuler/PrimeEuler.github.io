#!/usr/bin/env python3
"""R3 rigorous adjacent-arc test of norm-only B^4 telescoping transport.

This is a small-radius prerequisite for the all-arc R16 problem.  It certifies
the exact cut ordering around x=1, constructs the one-update positive weight,
and tests

  ||B_1^4||_w <= ||B_0^4||_w + 4 beta^3 delta,

where beta bounds both adjacent weighted B norms and delta bounds the weighted
norm of the exact matrix update.  Failure is only an obstruction to this
norm-only transport inequality, not a spectral lower bound.
"""
import hashlib
import json
from fractions import Fraction as F
from itertools import combinations, product
from math import isqrt

import numpy as np
from scipy.sparse import coo_matrix

Q = (2, 3, 4, 5, 7)
V = {2: (1, 0, 0, 0), 3: (0, 1, 0, 0), 4: (2, 0, 0, 0),
     5: (0, 0, 1, 0), 7: (0, 0, 0, 1)}
L = {q: np.log(q) for q in Q}
ALPHA_FLOAT = {q: L[q] / (2 * np.sqrt(q)) for q in Q}
L4 = np.array([L[2], L[3], L[5], L[7]])

P = 10**45
N = 220
R = 3
TARGET = F(41, 10) ** 4
U = F(1, 2**53)
E = F(1, 10**9)
MARGIN = F(1, 10**6)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[1], a[1] - b[0]


def mul(a, b):
    values = [x * y for x in a for y in b]
    return min(values), max(values)


def scale(a, s):
    return mul(a, (F(s), F(s)))


def div(a, b):
    assert b[0] > 0
    return mul(a, (1 / b[1], 1 / b[0]))


def logbound(q):
    x = F(q - 1, q + 1)
    value = sum((2 * x ** (2 * k + 1) / F(2 * k + 1)
                 for k in range(N)), F())
    error = 2 * x ** (2 * N + 1) / ((2 * N + 1) * (1 - x * x))
    return value, value + error


def sqrtbound(q):
    k = isqrt(q * P * P)
    return F(k, P), F(k + 1, P)


LS = {q: logbound(q) for q in Q}
ALPHA = {q: div(LS[q], scale(sqrtbound(q), 2)) for q in Q}


def mod2(a):
    assert a[0] // 2 == a[1] // 2
    return sub(a, scale((F(2), F(2)), a[0] // 2))


def saw_interval(a):
    return sub((F(1), F(1)), mod2(a))


def d_interval(x, sign, ell):
    return sub(saw_interval(sub(x, scale(ell, sign))), saw_interval(x))


def g_interval(x, sigma, tau, a, b):
    y = add(x, scale(a, sigma))
    z = sub(x, scale(b, tau))
    return add(mul(d_interval(y, sigma, a), d_interval(y, tau, b)),
               mul(d_interval(z, -tau, b), d_interval(z, -sigma, a)))


def saw(x):
    return 1 - np.mod(x, 2)


def d_float(x, sign, ell):
    return saw(x - sign * ell) - saw(x)


def g_float(x, sigma, tau, a, b):
    y = x + sigma * a
    z = x - tau * b
    return (d_float(y, sigma, a) * d_float(y, tau, b)
            + d_float(z, -tau, b) * d_float(z, -sigma, a))


def assemble(radius, x):
    width = 2 * radius + 1
    sites = np.indices((width,) * 4, dtype=np.int16).reshape(4, -1).T
    h = sites.astype(np.int32) - radius
    field = x + h @ L4
    rows, cols, data = [], [], []
    for q, r in combinations(Q, 2):
        for sigma, tau in product((-1, 1), repeat=2):
            jump = np.array([tau * V[r][i] - sigma * V[q][i]
                             for i in range(4)])
            source = sites - jump
            mask = np.all((source >= 0) & (source < width), axis=1)
            rr = np.flatnonzero(mask)
            cc = np.ravel_multi_index(source[mask].T, (width,) * 4)
            values = (sigma * tau * ALPHA_FLOAT[q] * ALPHA_FLOAT[r]
                      * g_float(field[mask], sigma, tau, L[q], L[r]))
            rows.append(rr)
            cols.append(cc)
            data.append(values)
    return coo_matrix((np.concatenate(data),
                      (np.concatenate(rows), np.concatenate(cols))),
                      shape=(len(sites), len(sites))).tocsr()


def gamma(k):
    value = F(k) * U
    assert value < 1
    return value / (1 - value)


def unweighted_row_upper(matrix):
    k = int(np.diff(matrix.indptr).max())
    observed = float(np.asarray(abs(matrix).sum(axis=1)).ravel().max())
    return F.from_float(observed) / (1 - gamma(k)), k


def weighted_row_upper(matrix, weight):
    k = int(np.diff(matrix.indptr).max())
    ratios = np.asarray(abs(matrix) @ weight).ravel() / weight
    observed = float(ratios.max())
    return F.from_float(observed) / (1 - gamma(2 * k + 1)), k


def cut_interval(k):
    value = (F(), F())
    for ki, q in zip(k, (2, 3, 5, 7)):
        value = add(value, scale(LS[q], -ki))
    return mod2(value)


def exact_cuts():
    cuts = []
    for k0 in range(-R - 1, R + 2):
        for k1, k2, k3 in product(range(-R, R + 1), repeat=3):
            cuts.append(cut_interval((k0, k1, k2, k3)))
    cuts.sort(key=lambda z: z[0])
    assert len(cuts) == 3087
    for left, right in zip(cuts, cuts[1:]):
        assert left[1] < right[0]
    return cuts


def midpoint(cuts, index):
    left = cuts[index]
    wrap = index + 1 == len(cuts)
    right = cuts[(index + 1) % len(cuts)]
    right_low = right[0] + (2 if wrap else 0)
    xq = (left[1] + right_low) / 2
    x = float(xq % 2)
    xf = F.from_float(x) + (2 if wrap and x < 1 else 0)
    assert xf > left[1] + MARGIN
    assert xf < right_low - MARGIN
    return x


def certify_word_state_tolerance():
    maximum = F()
    for q, r in combinations(Q, 2):
        for sigma, tau in product((-1, 1), repeat=2):
            a, b = LS[q], LS[r]
            cuts = [(F(), F()), (F(2), F(2)), mod2(scale(a, -sigma)),
                    mod2(scale(b, tau)),
                    mod2(sub(scale(b, tau), scale(a, sigma)))]
            cuts.sort(key=lambda z: z[0])
            for left, right in zip(cuts, cuts[1:]):
                assert left[1] < right[0]
                x = (left[1] + right[0]) / 2
                exact = mul((F(sigma * tau), F(sigma * tau)),
                            mul(ALPHA[q], mul(ALPHA[r],
                                g_interval((x, x), sigma, tau, a, b))))
                value = F.from_float(float(
                    sigma * tau * ALPHA_FLOAT[q] * ALPHA_FLOAT[r]
                    * g_float(float(x), sigma, tau, L[q], L[r])))
                error = max(abs(value - exact[0]), abs(value - exact[1]))
                maximum = max(maximum, error)
    assert maximum < F(1, 10**15)
    return maximum


def evaluate_neighbor(b0, b04, weight, condition, m, anchor_upper,
                      neighbor_index, x):
    b1 = assemble(R, x)
    b12 = b1 @ b1
    b14 = b12 @ b12
    b0w_stored, _ = weighted_row_upper(b0, weight)
    b1w_stored, _ = weighted_row_upper(b1, weight)
    b0w = b0w_stored + condition * E
    b1w = b1w_stored + condition * E
    beta = max(b0w, b1w)

    delta_stored_matrix = b1 - b0
    delta_stored, delta_k = weighted_row_upper(delta_stored_matrix, weight)
    subtraction = gamma(1) * (b0w_stored + b1w_stored)
    delta = delta_stored + subtraction + 2 * condition * E
    transported = anchor_upper + 4 * beta**3 * delta

    m1, k1 = unweighted_row_upper(b1)
    c12, k2 = unweighted_row_upper(b12)
    stored_b14w, _ = weighted_row_upper(b14, weight)
    r2 = gamma(2 * k1) * m1 * m1
    r4 = r2 * (m1 * m1 + c12) + gamma(2 * k2) * c12 * c12
    perturb1 = (m1 + E)**4 - m1**4
    direct_upper = stored_b14w + condition * (r4 + perturb1)

    return {
        "neighbor_arc": neighbor_index,
        "x": x,
        "delta_nnz": int(delta_stored_matrix.nnz),
        "delta_max_row_length": delta_k,
        "beta": float(beta),
        "delta": float(delta),
        "anchor_outward_b4": float(anchor_upper),
        "transport_increment": float(4 * beta**3 * delta),
        "transported_b4": float(transported),
        "transported_fourth_root": float(transported) ** 0.25,
        "direct_outward_b4": float(direct_upper),
        "direct_outward_fourth_root": float(direct_upper) ** 0.25,
        "direct_pass": direct_upper < TARGET,
        "target4": float(TARGET),
        "pass": transported < TARGET,
    }


if __name__ == "__main__":
    max_state_error = certify_word_state_tolerance()
    cuts = exact_cuts()
    candidates = [i for i, (left, right) in
                  enumerate(zip(cuts, cuts[1:]))
                  if left[1] < 1 < right[0]]
    assert len(candidates) == 1
    anchor_index = candidates[0]
    assert anchor_index == 1543

    b0 = assemble(R, 1.0)
    b02 = b0 @ b0
    b04 = b02 @ b02
    weight = np.asarray(abs(b04) @ np.ones(b0.shape[0])).ravel()
    assert np.all(np.isfinite(weight)) and np.all(weight > 0)
    weight /= weight.max()
    weight_sha = hashlib.sha256(weight.tobytes(order="C")).hexdigest()
    condition = (F.from_float(float(weight.max()))
                 / F.from_float(float(weight.min())))

    m, k1 = unweighted_row_upper(b0)
    c2, k2 = unweighted_row_upper(b02)
    stored_b4w, k4 = weighted_row_upper(b04, weight)
    r2 = gamma(2 * k1) * m * m
    r4 = r2 * (m * m + c2) + gamma(2 * k2) * c2 * c2
    perturb = (m + E)**4 - m**4
    anchor_upper = stored_b4w + condition * (r4 + perturb)

    results = []
    for neighbor in (anchor_index - 1, anchor_index + 1):
        results.append(evaluate_neighbor(
            b0, b04, weight, condition, m, anchor_upper,
            neighbor, midpoint(cuts, neighbor)))

    summary = {
        "radius": R,
        "cut_count": len(cuts),
        "anchor_arc": anchor_index,
        "dimension": int(b0.shape[0]),
        "b_nnz": int(b0.nnz),
        "weight_sha256": weight_sha,
        "weight_condition": float(condition),
        "max_exact_word_state_error": float(max_state_error),
        "anchor_outward_b4": float(anchor_upper),
        "anchor_outward_fourth_root": float(anchor_upper) ** 0.25,
        "neighbors": results,
        "method": "norm_only_telescoping_mu_plus_4_beta_cubed_delta",
        "scope": "R3_two_adjacent_arcs_only_no_C3_no_C16",
    }
    print("SUMMARY", json.dumps(summary, sort_keys=True))
    print("STATUS=NORM_ONLY_TRANSPORT_PASS" if all(r["pass"] for r in results)
          else "STATUS=NORM_ONLY_TRANSPORT_FAIL_NOT_SPECTRAL_LOWER_BOUND")
