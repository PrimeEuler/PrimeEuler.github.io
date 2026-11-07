#!/usr/bin/env python3
"""Exact annulus-scale obstruction certificate for Lane A v15.485."""

from fractions import Fraction

N = 5
MAX_SCALE = 5
MAX_OFFSET = 22


def sample_indices(length):
    return sorted({0, length // 2, length - 1})


def main():
    identity_tests = 0
    nonstationary_tests = 0
    limit_tests = 0

    for a in range(MAX_SCALE + 1):
        n_a = (2 ** a) * N
        for d in range(MAX_OFFSET + 1):
            b = a + d
            n_b = (2 ** b) * N
            for r in sample_indices(n_a):
                for s in sample_indices(n_b):
                    j = (2 ** a - 1) * N + r
                    k = (2 ** b - 1) * N + s
                    x = Fraction(N + j, n_a)
                    y = Fraction(N + k, n_b)

                    # Square of the block kernel after unitary step-function
                    # rescaling: n_a*n_b/[4(N+j+k)^2].
                    physical_squared = Fraction(n_a * n_b, 4 * (N + j + k) ** 2)
                    formula_squared = Fraction(2 ** d, 4) / (
                        x + (2 ** d) * y - Fraction(1, 2 ** a)
                    ) ** 2
                    assert physical_squared == formula_squared
                    identity_tests += 1

            # Remove the a-independent factor 2^(d/2). At x=y=1 the
            # remaining rational coefficient changes strictly with a.
            A = Fraction(1 + 2 ** d, 1)
            t = Fraction(1, 2 ** a)
            h_a = Fraction(1, 2) / (A - t)
            h_limit = Fraction(1, 2) / A
            assert h_a > h_limit
            assert h_a - h_limit == t / (2 * (A - t) * A)
            limit_tests += 1
            if a < MAX_SCALE:
                t_next = Fraction(1, 2 ** (a + 1))
                h_next = Fraction(1, 2) / (A - t_next)
                assert h_a != h_next
                assert h_a > h_next > h_limit
                nonstationary_tests += 1

    assert identity_tests == (MAX_SCALE + 1) * (MAX_OFFSET + 1) * 9
    assert nonstationary_tests == MAX_SCALE * (MAX_OFFSET + 1)
    assert limit_tests == (MAX_SCALE + 1) * (MAX_OFFSET + 1)

    print("status=PASS_EXACT_SCALE_COORDINATE_OBSTRUCTION")
    print("rescaled_block_squared=2^d/[4(x+2^d*y-2^-a)^2]")
    print("absolute_scale_coordinate=t_a=2^-a")
    print("stationary_solenoid_coefficient=IMPOSSIBLE_FOR_CONSTANT_BLOCK")
    print("required_extension=scale_coordinate_plus_refining_grid_fibers")
    print(f"exact_identity_tests={identity_tests}")
    print(f"nonstationarity_tests={nonstationary_tests}")
    print(f"limit_identity_tests={limit_tests}")
    print("physical_45_diagonal_embedding=UNBUILT")
    print("joint_norm_gate=UNEVALUATED")


if __name__ == "__main__":
    main()
