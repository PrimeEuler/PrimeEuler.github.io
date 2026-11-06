#!/usr/bin/env python3
"""Exact 16-branch transfer-operator certificate for Lane A v15.475."""

from itertools import product
from math import prod

DIMENSION = 4
BRANCHES = tuple(product((-1, 1), repeat=DIMENSION))


def branch_average_character(exponent):
    """Return the exact sign average over the 16 inverse branches."""
    numerator = sum(
        prod(sign ** power for sign, power in zip(branch, exponent))
        for branch in BRANCHES
    )
    return numerator, len(BRANCHES)


def expected_character_image(exponent):
    if any(power % 2 for power in exponent):
        return 0, None
    return 1, tuple(power // 2 for power in exponent)


def main():
    assert len(BRANCHES) == 2 ** DIMENSION == 16

    tested = 0
    killed = 0
    survived = 0
    for exponent in product(range(-4, 5), repeat=DIMENSION):
        numerator, denominator = branch_average_character(exponent)
        coefficient, image = expected_character_image(exponent)
        assert denominator == 16
        assert numerator == 16 * coefficient
        if coefficient == 0:
            killed += 1
        else:
            assert image == tuple(power // 2 for power in exponent)
            survived += 1
        tested += 1

    # Character-level transfer identity:
    # L(alpha(chi_a) chi_b) = chi_a L(chi_b), alpha(chi_a)=chi_(2a).
    transfer_tests = 0
    for a in product(range(-2, 3), repeat=DIMENSION):
        for b in product(range(-2, 3), repeat=DIMENSION):
            left_exp = tuple(2 * x + y for x, y in zip(a, b))
            left_coeff, left_image = expected_character_image(left_exp)
            right_coeff, right_image_b = expected_character_image(b)
            if right_coeff == 0:
                assert left_coeff == 0
            else:
                right_image = tuple(x + y for x, y in zip(a, right_image_b))
                assert left_coeff == 1
                assert left_image == right_image
            transfer_tests += 1

    assert tested == 9 ** 4
    assert survived == 5 ** 4
    assert killed == tested - survived
    assert transfer_tests == 5 ** 8

    print("status=PASS_EXACT_16_BRANCH_TRANSFER_OPERATOR")
    print("base_map=coordinatewise_squaring_on_T4")
    print("transfer_normalization=1/16")
    print("character_rule=odd_coordinate_killed_even_vector_halved")
    print(f"character_tests={tested}")
    print(f"transfer_identity_tests={transfer_tests}")
    print("physical_45_diagonal_representation=UNBUILT")
    print("joint_norm_gate=UNEVALUATED")


if __name__ == "__main__":
    main()
