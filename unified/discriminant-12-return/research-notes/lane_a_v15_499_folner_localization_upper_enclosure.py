#!/usr/bin/env python3
"""Exact Følner-localization upper-enclosure certificate for Lane A v15.499."""

from fractions import Fraction
from itertools import combinations, product

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


def overlap(g, radius):
    length = 2 * radius + 1
    numerator = 1
    for coordinate in g:
        numerator *= max(0, length - abs(coordinate))
    return Fraction(numerator, length**4)


def indicator(point, center, radius):
    return all(abs(point[i] - center[i]) <= radius for i in range(4))


def translated_window_sum(h, g, radius):
    """Sum_k phi_k(h)phi_k(h-g), evaluated by exact finite enumeration."""
    length = 2 * radius + 1
    # A contributing center lies in both h+[-R,R]^4 and h-g+[-R,R]^4.
    ranges = [
        range(max(h[i] - radius, h[i] - g[i] - radius),
              min(h[i] + radius, h[i] - g[i] + radius) + 1)
        for i in range(4)
    ]
    count = 0
    shifted = tuple(h[i] - g[i] for i in range(4))
    for center in product(*ranges):
        assert indicator(h, center, radius)
        assert indicator(shifted, center, radius)
        count += 1
    return Fraction(count, length**4)


def tent_weight(n, radius):
    return max(0, radius + 1 - abs(n))


def tent_correlation_1d(shift, radius):
    norm_squared = sum(tent_weight(n, radius) ** 2
                       for n in range(-radius, radius + 1))
    correlation = sum(tent_weight(n, radius) * tent_weight(n - shift, radius)
                      for n in range(-2 * radius, 2 * radius + 1))
    return Fraction(correlation, norm_squared)


def tent_overlap(g, radius):
    value = Fraction(1)
    for coordinate in g:
        value *= tent_correlation_1d(coordinate, radius)
    return value


def main():
    radii = (2, 4, 8, 16, 32)
    support = []
    for q, r in combinations(FREQUENCIES, 2):
        for sigma, tau in product((-1, 1), repeat=2):
            support.append((q, r, sigma, tau, label(q, r, sigma, tau)))
    assert len(support) == 40
    assert len({entry[-1] for entry in support}) == 40

    localization_tests = 0
    test_points = ((0, 0, 0, 0), (2, -1, 3, -2), (-4, 2, 1, 5))
    for radius in radii[:3]:
        for *_, g in support:
            expected = overlap(g, radius)
            for h in test_points:
                assert translated_window_sum(h, g, radius) == expected
                localization_tests += 1

    # The sawtooth lies in [-1,1] up to endpoint convention.  Each D factor
    # has norm <=2, hence each of the two products in G has norm <=4 and
    # ||G||_infinity <=8.  With alpha_q=log(q)/(2sqrt(q)), the boundary
    # penalty is bounded by
    #   sum_(q<r) 2 log(q)log(r)/sqrt(qr) * pair_delta[q,r,R],
    # where pair_delta is the exact sum of 1-overlap over four sign branches.
    pair_delta = {}
    tent_pair_delta = {}
    for radius in radii:
        for q, r in combinations(FREQUENCIES, 2):
            value = sum(
                1 - overlap(label(q, r, sigma, tau), radius)
                for sigma, tau in product((-1, 1), repeat=2)
            )
            pair_delta[(radius, q, r)] = value
            assert 0 < value < 4
            tent_value = sum(
                1 - tent_overlap(label(q, r, sigma, tau), radius)
                for sigma, tau in product((-1, 1), repeat=2)
            )
            tent_pair_delta[(radius, q, r)] = tent_value
            assert 0 < tent_value
            if radius >= 8:
                assert tent_value < value

    # Exact decay and the elementary support-radius estimate.
    for q, r in combinations(FREQUENCIES, 2):
        values = [pair_delta[(radius, q, r)] for radius in radii]
        tent_values = [tent_pair_delta[(radius, q, r)] for radius in radii]
        assert all(values[i + 1] < values[i] for i in range(len(values) - 1))
        assert all(tent_values[i + 1] < tent_values[i]
                   for i in range(len(tent_values) - 1))
        for radius, value in zip(radii, values):
            assert value <= Fraction(12, 2 * radius + 1)

    print("status=PASS_EXACT_FOLNER_LOCALIZATION_UPPER_ENCLOSURE")
    print("identity=sum_k_phi_k_T_phi_k=sum_g_overlap_R(g)*A_g_lambda_g")
    print("upper_bound=norm(T)<=finite_cube_norm+sum_g_boundary_R(g)*norm(a_g)")
    print("coefficient_bound=norm(G_sigma_tau)_infinity<=8")
    print("finite_cube_norm=essential_supremum_of_finite_Hermitian_matrix_field")
    print(f"exact_localization_identity_tests={localization_tests}")
    for radius in radii:
        encoded = ",".join(
            f"{q}-{r}:{pair_delta[(radius,q,r)].numerator}/{pair_delta[(radius,q,r)].denominator}"
            for q, r in combinations(FREQUENCIES, 2)
        )
        print(f"radius_{radius}_pair_delta={encoded}")
        tent_encoded = ",".join(
            f"{q}-{r}:{tent_pair_delta[(radius,q,r)].numerator}/{tent_pair_delta[(radius,q,r)].denominator}"
            for q, r in combinations(FREQUENCIES, 2)
        )
        print(f"radius_{radius}_tent_pair_delta={tent_encoded}")
    print("finite_matrix_field_supremum=UNEVALUATED")
    print("signed_45_diagonal_norm=UNEVALUATED")


if __name__ == "__main__":
    main()
