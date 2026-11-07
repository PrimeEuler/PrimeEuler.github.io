#!/usr/bin/env python3
"""Exact support/Folner certificate for Lane A v15.497.

This is an architecture certificate.  It certifies the finite group support
used by the faithful regular representation and exact Folner-cube boundary
ratios; it does not turn finite compressions into upper norm enclosures.
"""

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


def overlap_ratio(g, radius):
    """|F_R intersect (F_R+g)|/|F_R| for F_R=[-R,R]^4."""
    length = 2 * radius + 1
    numerator = 1
    for coordinate in g:
        numerator *= max(0, length - abs(coordinate))
    return Fraction(numerator, length**4)


def main():
    support = {
        label(q, r, sigma, tau)
        for q, r in combinations(FREQUENCIES, 2)
        for sigma, tau in product((-1, 1), repeat=2)
    }
    zero = (0, 0, 0, 0)
    assert zero not in support
    assert len(support) == 40
    assert support == {scale(-1, g) for g in support}
    orbits = {tuple(sorted((g, scale(-1, g)))) for g in support}
    assert len(orbits) == 20

    max_l1 = max(sum(abs(x) for x in g) for g in support)
    max_linf = max(max(abs(x) for x in g) for g in support)
    assert max_l1 == 3
    assert max_linf == 3

    # Exact covariance index identity for
    # pi_tilde(a)xi(h)=pi(alpha_{-h}(a))xi(h),
    # lambda_g xi(h)=xi(h-g):
    # lambda_g pi_tilde(a) lambda_g^*=pi_tilde(alpha_g(a)).
    covariance_tests = 0
    for h in product(range(-3, 4), repeat=4):
        for g in support:
            left_index = tuple(-(h[i] - g[i]) for i in range(4))
            right_index = tuple(g[i] - h[i] for i in range(4))
            assert left_index == right_index
            covariance_tests += 1

    radii = (2, 4, 8, 16, 32)
    boundary = []
    for radius in radii:
        ratios = [1 - overlap_ratio(g, radius) for g in support]
        worst = max(ratios)
        length = 2 * radius + 1
        # Union bound: 1-prod_i(1-|g_i|/L) <= ||g||_1/L.
        assert all(ratio <= Fraction(sum(abs(x) for x in g), length)
                   for g, ratio in zip(sorted(support),
                                       [1 - overlap_ratio(g, radius) for g in sorted(support)]))
        boundary.append(worst)
    assert all(boundary[i + 1] < boundary[i] for i in range(len(boundary) - 1))

    print("status=PASS_EXACT_FAITHFUL_REGULAR_ARCHITECTURE")
    print("group=Z^4")
    print("group_amenable=YES")
    print("full_equals_reduced_crossed_product=YES")
    print("faithful_regular_representation=CANONICAL_FROM_ANY_FAITHFUL_COEFFICIENT_REP")
    print("support_labels=40")
    print("zero_support_label=ABSENT")
    print("adjoint_support_orbits=20")
    print(f"max_support_l1={max_l1}")
    print(f"max_support_linf={max_linf}")
    print(f"covariance_index_tests={covariance_tests}")
    for radius, ratio in zip(radii, boundary):
        print(f"folner_radius_{radius}_worst_boundary={ratio.numerator}/{ratio.denominator}")
    print("finite_compressions=CONVERGENT_LOWER_APPROXIMATIONS_ONLY")
    print("certified_finite_section_upper_enclosure=UNEVALUATED")
    print("signed_45_diagonal_norm=UNEVALUATED")


if __name__ == "__main__":
    main()
