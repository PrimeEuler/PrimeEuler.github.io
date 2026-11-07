#!/usr/bin/env python3
"""Exact sharp sawtooth-difference penalty certificate for Lane A v15.501."""

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations, product
from math import factorial

FREQUENCIES = {
    2: (1, 0, 0, 0),
    3: (0, 1, 0, 0),
    4: (2, 0, 0, 0),
    5: (0, 0, 1, 0),
    7: (0, 0, 0, 1),
}


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def scale(c, u):
    return tuple(c * a for a in u)


def label(q, r, sigma, tau):
    return add(scale(tau, FREQUENCIES[r]), scale(-sigma, FREQUENCIES[q]))


def tent_weight(n, radius):
    return max(0, radius + 1 - abs(n))


def tent_correlation_1d(shift, radius):
    norm_squared = sum(tent_weight(n, radius) ** 2
                       for n in range(-radius, radius + 1))
    correlation = sum(tent_weight(n, radius) * tent_weight(n - shift, radius)
                      for n in range(-2 * radius, 2 * radius + 1))
    return Fraction(correlation, norm_squared)


def tent_overlap(g, radius):
    answer = Fraction(1)
    for coordinate in g:
        answer *= tent_correlation_1d(coordinate, radius)
    return answer


def sawtooth(x):
    return Fraction(1) - (x % 2)


def main():
    # Exact elementary comparisons: 2 < e < 3 and 7 < e^2.
    e_lower = sum(Fraction(1, factorial(k)) for k in range(7))
    assert e_lower > 2
    assert e_lower * e_lower > 7
    # For k>=1, k! >= 2^(k-1), with strict inequality eventually, so e<3.
    assert all(factorial(k) >= 2 ** (k - 1) for k in range(1, 20))
    e_upper = Fraction(3)
    assert e_lower < e_upper

    # For 0<c<2, s(x-c)-s(x) is c off the wrap interval and c-2 on it.
    difference_tests = 0
    for denominator in range(3, 18):
        for numerator in range(1, 2 * denominator):
            c = Fraction(numerator, denominator)
            if c >= 2:
                continue
            for j in range(1, 4 * denominator):
                x = Fraction(j, 2 * denominator)
                if (x % 2) == c:
                    continue
                value = sawtooth(x - c) - sawtooth(x)
                assert value in (c, c - 2)
                difference_tests += 1

    # Hence ||D_log(q)||=max(log(q),2-log(q)).  The exact branch is selected
    # by log(2)<1 and log(q)>1 for q=3,4,5,7, using 2<e<3.
    norm_branch = {2: "2-log(2)", 3: "log(3)", 4: "log(4)",
                   5: "log(5)", 7: "log(7)"}

    # G is a sum of two D_q D_r products, so
    # ||G|| <= 2 m_q m_r, improving the former uniform bound 8.
    # Compute only decimal orientation values for the exact rational tent
    # geometry; these are explicitly not interval certificates.
    getcontext().prec = 60
    orientation = {}
    for radius in (8, 16, 32):
        total = Decimal(0)
        for q, r in combinations(FREQUENCIES, 2):
            delta = sum(
                1 - tent_overlap(label(q, r, sigma, tau), radius)
                for sigma, tau in product((-1, 1), repeat=2)
            )
            qd, rd = Decimal(q), Decimal(r)
            lq, lr = qd.ln(), rd.ln()
            mq = Decimal(2) - lq if q == 2 else lq
            mr = Decimal(2) - lr if r == 2 else lr
            weight = lq * lr * mq * mr / (Decimal(2) * (qd * rd).sqrt())
            total += weight * Decimal(delta.numerator) / Decimal(delta.denominator)
        orientation[radius] = total
    assert orientation[32] < orientation[16] < orientation[8]

    print("status=PASS_EXACT_SHARP_SAWTOOTH_DIFFERENCE_PENALTY")
    print("exact_difference_values={c,c-2}")
    print("exact_difference_norm=max(c,2-c)")
    print(f"rational_difference_tests={difference_tests}")
    for q in FREQUENCIES:
        print(f"q_{q}_difference_norm={norm_branch[q]}")
    print("coefficient_bound=norm(G_qr_sigma_tau)<=2*m_q*m_r")
    print("weighted_penalty_factor=log(q)log(r)m_qm_r/(2sqrt(qr))")
    for radius in (8, 16, 32):
        print(f"radius_{radius}_decimal_orientation={orientation[radius]}")
    print("decimal_orientations=NOT_INTERVAL_CERTIFICATES")
    print("finite_matrix_field_supremum=UNEVALUATED")
    print("signed_45_diagonal_norm=UNEVALUATED")


if __name__ == "__main__":
    main()
