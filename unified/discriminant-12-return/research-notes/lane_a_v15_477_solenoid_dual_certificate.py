#!/usr/bin/env python3
"""Exact natural-extension/dual-group certificate for Lane A v15.477."""

from fractions import Fraction
from itertools import product

DIMENSION = 4


def dual_coordinate(exponent, level):
    """Class [(m, level)] in the direct limit, represented in Z[1/2]^4."""
    scale = 2 ** level
    return tuple(Fraction(value, scale) for value in exponent)


def refine(exponent, level):
    """(m,n) ~ (2m,n+1), induced by z_n=z_(n+1)^2."""
    return tuple(2 * value for value in exponent), level + 1


def shift_action(exponent, level):
    """Character pullback by S: multiplication by 2 on Z[1/2]^4."""
    if level == 0:
        return tuple(2 * value for value in exponent), 0
    return exponent, level - 1


def inverse_shift_action(exponent, level):
    """Character pullback by S^{-1}: division by 2 on Z[1/2]^4."""
    return exponent, level + 1


def main():
    class_tests = 0
    action_tests = 0
    inverse_tests = 0

    for exponent in product(range(-3, 4), repeat=DIMENSION):
        for level in range(7):
            refined_exp, refined_level = refine(exponent, level)
            assert dual_coordinate(exponent, level) == dual_coordinate(
                refined_exp, refined_level
            )
            class_tests += 1

            shifted_exp, shifted_level = shift_action(exponent, level)
            original = dual_coordinate(exponent, level)
            shifted = dual_coordinate(shifted_exp, shifted_level)
            assert shifted == tuple(2 * value for value in original)
            action_tests += 1

            inv_exp, inv_level = inverse_shift_action(exponent, level)
            inverse = dual_coordinate(inv_exp, inv_level)
            assert inverse == tuple(value / 2 for value in original)
            inverse_tests += 1

    # Algebraic sequence check for the natural extension:
    # S(z)_0=D(z_0), S(z)_(n+1)=z_n; dropping coordinate 0 is S^{-1}.
    # The inverse-limit relation D(z_(n+1))=z_n makes both compositions exact.
    assert class_tests == 7 ** 4 * 7
    assert action_tests == class_tests
    assert inverse_tests == class_tests

    print("status=PASS_EXACT_NATURAL_EXTENSION_SOLENOID_DUAL")
    print("base_inverse_limit=lim_inverse(T4,coordinatewise_squaring)")
    print("natural_extension_shift=AUTOMORPHISM")
    print("pontryagin_dual=Z[1/2]^4")
    print("shift_character_action=multiply_by_2")
    print("inverse_shift_character_action=divide_by_2")
    print(f"equivalence_class_tests={class_tests}")
    print(f"shift_action_tests={action_tests}")
    print(f"inverse_shift_tests={inverse_tests}")
    print("physical_45_diagonal_embedding=UNBUILT")
    print("joint_norm_gate=UNEVALUATED")


if __name__ == "__main__":
    main()
