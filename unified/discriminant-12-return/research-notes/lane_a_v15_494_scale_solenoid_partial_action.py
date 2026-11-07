#!/usr/bin/env python3
"""Exact scale-solenoid partial-action certificate for Lane A v15.494."""

from fractions import Fraction

INF = None
UNDEFINED = object()
MAX_SCALE = 9
MAX_SHIFT = 6
MAX_OFFSET = 22


def theta(scale_index, shift):
    """Partial Z-action on scale indices; INF denotes the boundary t=0."""
    if scale_index is INF:
        return INF
    target = scale_index + shift
    return target if target >= 0 else UNDEFINED


def scale_value(scale_index):
    return Fraction(0) if scale_index is INF else Fraction(1, 2**scale_index)


def dual_pullback(label, shift):
    """Pullback on the solenoid dual Z[1/2]^4 under S^shift."""
    factor = Fraction(2**shift, 1) if shift >= 0 else Fraction(1, 2 ** (-shift))
    return tuple(factor * coordinate for coordinate in label)


def kernel_squared(scale_index, offset, x, y):
    """Square of the v15.485 constant-Hankel rescaled coefficient."""
    t = scale_value(scale_index)
    denominator = x + (2**offset) * y - t
    return Fraction(2**offset, 4) / denominator**2


def main():
    domain_tests = 0
    inverse_tests = 0
    action_tests = 0
    dual_tests = 0
    covariance_tests = 0
    continuity_tests = 0

    scales = list(range(MAX_SCALE + 1)) + [INF]

    # theta_n has domain a+n>=0 and maps a to a+n; the boundary is fixed.
    for a in scales:
        for n in range(-MAX_SHIFT, MAX_SHIFT + 1):
            result = theta(a, n)
            if a is INF:
                assert result is INF
            elif a + n < 0:
                assert result is UNDEFINED
            else:
                assert result == a + n
                assert theta(result, -n) == a
                inverse_tests += 1
                expected_scale = (
                    Fraction(1, 2**n) * scale_value(a)
                    if n >= 0
                    else Fraction(2 ** (-n)) * scale_value(a)
                )
                assert scale_value(result) == expected_scale
                covariance_tests += 1
            domain_tests += 1

    # Partial-action composition on its exact natural domain.
    for a in scales:
        for n in range(-MAX_SHIFT, MAX_SHIFT + 1):
            first = theta(a, n)
            for m in range(-MAX_SHIFT, MAX_SHIFT + 1):
                if first is UNDEFINED:
                    continue
                second = theta(first, m)
                if second is UNDEFINED:
                    continue
                direct = theta(a, n + m)
                assert direct is not UNDEFINED
                assert second == direct
                action_tests += 1

    # The solenoid dual action is multiplication by 2^n and composes exactly.
    labels = [
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(-2), Fraction(3, 2), Fraction(-5, 4)),
        (Fraction(7, 8), Fraction(11, 4), Fraction(-13, 2), Fraction(17)),
    ]
    for label in labels:
        for n in range(-MAX_SHIFT, MAX_SHIFT + 1):
            for m in range(-MAX_SHIFT, MAX_SHIFT + 1):
                assert dual_pullback(dual_pullback(label, n), m) == dual_pullback(label, n + m)
                dual_tests += 1

    # Exact continuity at t=0 for the constant-Hankel coefficient family.
    samples = [(Fraction(1), Fraction(1)), (Fraction(5, 4), Fraction(7, 5)), (Fraction(2), Fraction(3, 2))]
    for d in range(MAX_OFFSET + 1):
        c = Fraction(2**d, 4)
        for x, y in samples:
            B = x + (2**d) * y
            boundary = kernel_squared(INF, d, x, y)
            assert boundary == c / B**2
            previous = None
            for a in range(MAX_SCALE + 1):
                t = scale_value(a)
                value = kernel_squared(a, d, x, y)
                exact_difference = c * t * (2 * B - t) / ((B - t) ** 2 * B**2)
                assert value - boundary == exact_difference
                assert value > boundary
                if previous is not None:
                    assert previous > value
                previous = value
                continuity_tests += 1

    print("status=PASS_EXACT_SCALE_SOLENOID_PARTIAL_ACTION")
    print("scale_compactum={0}_union_{2^-a:a>=0}")
    print("forward_map=(t,z)->(t/2,Sz)")
    print("forward_range=scale_compactum_without_{1}")
    print("boundary_action=(0,z)->(0,Sz)")
    print("physical_orbit=nonnegative_annuli_only")
    print("solenoid_dual_pullback=q->2^n*q")
    print("constant_kernel_field=continuous_at_t=0")
    print(f"domain_tests={domain_tests}")
    print(f"inverse_tests={inverse_tests}")
    print(f"partial_action_composition_tests={action_tests}")
    print(f"dual_composition_tests={dual_tests}")
    print(f"scale_covariance_tests={covariance_tests}")
    print(f"kernel_continuity_tests={continuity_tests}")
    print("full_signed_operator_groupoid_membership=UNPROVED")
    print("signed_45_diagonal_norm=UNEVALUATED")


if __name__ == "__main__":
    main()
