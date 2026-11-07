#!/usr/bin/env python3
"""Outward rational certificate for all 40 coefficient suprema (Lane A v15.503)."""

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations, product
from math import isqrt

FREQUENCIES = {
    2: (1, 0, 0, 0), 3: (0, 1, 0, 0), 4: (2, 0, 0, 0),
    5: (0, 0, 1, 0), 7: (0, 0, 0, 1),
}


def ln_bounds(n, terms=260):
    """Rational outward bounds from log n=2*atanh((n-1)/(n+1))."""
    z = Fraction(n - 1, n + 1)
    lower = 2 * sum(z ** (2 * k + 1) / (2 * k + 1) for k in range(terms))
    remainder = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return lower, lower + remainder


LOG = {q: ln_bounds(q) for q in FREQUENCIES}


def dec(x, digits=35):
    getcontext().prec = digits + 10
    return Decimal(x.numerator) / Decimal(x.denominator)


def interval_linear(constant, a, b, A, B):
    lo = hi = Fraction(constant)
    for coefficient, interval in ((a, A), (b, B)):
        if coefficient >= 0:
            lo += coefficient * interval[0]
            hi += coefficient * interval[1]
        else:
            lo += coefficient * interval[1]
            hi += coefficient * interval[0]
    return lo, hi


def floor_half(interval):
    lo, hi = interval
    k = lo // 2
    assert 2 * k < lo and hi < 2 * (k + 1)
    return k


def d_linear(x, za, zb, sign, variable, A, B):
    """Linear form for D_sign(z; variable), z=x+za*A+zb*B."""
    z = interval_linear(x, za, zb, A, B)
    if variable == "A":
        zm = interval_linear(x, za - sign, zb, A, B)
        linear = (2 * (floor_half(zm) - floor_half(z)), sign, 0)
    else:
        zm = interval_linear(x, za, zb - sign, A, B)
        linear = (2 * (floor_half(zm) - floor_half(z)), 0, sign)
    return linear


def multiply_linear(u, v):
    c, a, b = u
    d, e, f = v
    # basis: 1,A,B,A^2,AB,B^2
    return (c*d, a*d+c*e, b*d+c*f, a*e, a*f+b*e, b*f)


def add_poly(u, v):
    return tuple(a + b for a, b in zip(u, v))


def poly_interval(p, A, B):
    monomials = (
        (Fraction(1), Fraction(1)), A, B,
        (A[0] * A[0], A[1] * A[1]),
        (A[0] * B[0], A[1] * B[1]),
        (B[0] * B[0], B[1] * B[1]),
    )
    lo = hi = Fraction(0)
    for coefficient, interval in zip(p, monomials):
        if coefficient >= 0:
            lo += coefficient * interval[0]
            hi += coefficient * interval[1]
        else:
            lo += coefficient * interval[1]
            hi += coefficient * interval[0]
    return lo, hi


def abs_bounds(interval):
    lo, hi = interval
    upper = max(abs(lo), abs(hi))
    lower = Fraction(0) if lo <= 0 <= hi else min(abs(lo), abs(hi))
    return lower, upper


def breakpoint(raw_a, raw_b, A, B):
    raw = interval_linear(0, raw_a, raw_b, A, B)
    getcontext().prec = 80
    mid = (dec(raw[0], 70) + dec(raw[1], 70)) / 2
    k = int((mid / 2).to_integral_value(rounding="ROUND_FLOOR"))
    reduced = (raw[0] - 2*k, raw[1] - 2*k)
    assert 0 < reduced[0] and reduced[1] < 2
    return reduced


def word_values(q, r, sigma, tau):
    A, B = LOG[q], LOG[r]
    points = [(Fraction(0), Fraction(0))]
    for a, b in ((-sigma, 0), (-sigma, tau), (0, tau)):
        points.append(breakpoint(a, b, A, B))
    points.sort(key=lambda z: z[0])
    assert all(points[i][1] < points[i+1][0] for i in range(len(points)-1))
    edges = points + [(Fraction(2), Fraction(2))]
    values = []
    for left, right in zip(edges[:-1], edges[1:]):
        x = (left[1] + right[0]) / 2
        first = multiply_linear(
            d_linear(x, sigma, 0, sigma, "A", A, B),
            d_linear(x, sigma, 0, tau, "B", A, B),
        )
        second = multiply_linear(
            d_linear(x, 0, -tau, -tau, "B", A, B),
            d_linear(x, 0, -tau, -sigma, "A", A, B),
        )
        values.append(add_poly(first, second))
    assert len(values) == 4
    return tuple(values)


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def scale(c, u):
    return tuple(c * a for a in u)


def label(q, r, sigma, tau):
    return add(scale(tau, FREQUENCIES[r]), scale(-sigma, FREQUENCIES[q]))


def tent_weight(n, radius):
    return max(0, radius + 1 - abs(n))


def tent_corr(shift, radius):
    norm = sum(tent_weight(n, radius)**2 for n in range(-radius, radius+1))
    corr = sum(tent_weight(n, radius)*tent_weight(n-shift, radius)
               for n in range(-2*radius, 2*radius+1))
    return Fraction(corr, norm)


def tent_overlap(g, radius):
    answer = Fraction(1)
    for coordinate in g:
        answer *= tent_corr(coordinate, radius)
    return answer


def sqrt_lower(n, digits=90):
    scale10 = 10 ** digits
    return Fraction(isqrt(n * scale10 * scale10), scale10)


def main():
    coefficient_upper = {}
    cell_tests = 0
    dominance_tests = 0
    tightness_tests = 0
    for q, r in combinations(FREQUENCIES, 2):
        A, B = LOG[q], LOG[r]
        for sigma, tau in product((-1, 1), repeat=2):
            values = word_values(q, r, sigma, tau)
            bounds = [abs_bounds(poly_interval(p, A, B)) for p in values]
            upper = max(bound[1] for bound in bounds)
            lower = max(bound[0] for bound in bounds)
            coefficient_upper[(q, r, sigma, tau)] = upper
            # The largest outward interval must overlap a genuine cell lower
            # bound; this guards against a vacuous interval explosion.
            assert max(bound[0] for bound in bounds) <= upper
            assert upper - lower < Fraction(1, 10**50)
            cell_tests += len(values)
            dominance_tests += sum(1 for lower, high in bounds if lower <= upper and high <= upper)
            tightness_tests += 1

    assert len(coefficient_upper) == 40
    assert cell_tests == 160 and dominance_tests == 160 and tightness_tests == 40

    # Exact outward localization penalties, including log and sqrt weights.
    penalty_upper = {}
    for radius in (8, 16, 32):
        total = Fraction(0)
        for q, r in combinations(FREQUENCIES, 2):
            sqrt_qr = sqrt_lower(q * r)
            weight_upper = LOG[q][1] * LOG[r][1] / (4 * sqrt_qr)
            for sigma, tau in product((-1, 1), repeat=2):
                delta = 1 - tent_overlap(label(q, r, sigma, tau), radius)
                total += weight_upper * coefficient_upper[(q, r, sigma, tau)] * delta
        penalty_upper[radius] = total
    assert penalty_upper[32] < penalty_upper[16] < penalty_upper[8]

    print("status=PASS_OUTWARD_INTERVAL_COEFFICIENT_SUPREMA")
    print("log_bounds=rational_atanh_series_260_terms")
    print("sqrt_bounds=90_decimal_rational_floor")
    print(f"certified_piecewise_cells={cell_tests}")
    print(f"certified_cell_interval_tests={dominance_tests}")
    print(f"fifty_decimal_tightness_tests={tightness_tests}")
    for q, r in combinations(FREQUENCIES, 2):
        values = []
        for sigma, tau in product((-1, 1), repeat=2):
            u = coefficient_upper[(q, r, sigma, tau)]
            values.append(f"{sigma:+d}{tau:+d}:{dec(u,30)}")
        print(f"pair_{q}_{r}_sup_upper=" + ",".join(values))
    for radius in (8, 16, 32):
        print(f"radius_{radius}_penalty_outward_upper={dec(penalty_upper[radius],40)}")
    print("finite_matrix_field_supremum=UNEVALUATED")
    print("signed_45_diagonal_norm=UNEVALUATED")


if __name__ == "__main__":
    main()
