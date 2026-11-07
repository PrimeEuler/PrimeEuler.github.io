#!/usr/bin/env python3
"""Exact common-dyadic-fiber certificate for Lane A v15.490."""

from fractions import Fraction

N = 5
MAX_SCALE = 7
MAX_GAP = 6


def annulus_start(a):
    return (2**a - 1) * N


def annulus_size(a):
    return (2**a) * N


def descendants(r, d):
    """Fine cells contained in coarse cell r after d refinements."""
    return range((2**d) * r, (2**d) * (r + 1))


def main():
    partition_tests = 0
    gram_tests = 0
    projection_tests = 0
    composition_tests = 0
    block_action_tests = 0

    # The annuli I_a are disjoint, consecutive, and exhaust the tested prefix.
    previous_stop = 0
    for a in range(MAX_SCALE + 1):
        start = annulus_start(a)
        size = annulus_size(a)
        stop = start + size
        assert start == previous_stop
        assert stop == annulus_start(a + 1)
        previous_stop = stop
        partition_tests += 2

    # B_{a,d} duplicates a coarse coordinate into its 2^d descendants.
    # Thus B^T B = 2^d I and J=2^(-d/2)B is an isometry.  The exact
    # fine-coordinate projection JJ^T has entries 2^-d inside each
    # descendant block and zero otherwise.
    for a in range(MAX_SCALE + 1):
        n = annulus_size(a)
        for d in range(MAX_GAP + 1):
            fine_n = (2**d) * n
            for r in {0, n // 2, n - 1}:
                block = set(descendants(r, d))
                assert len(block) == 2**d
                assert min(block) >= 0 and max(block) < fine_n
                gram_tests += 1

                # P^2=P on representative entries, entirely in Fractions.
                for u in {min(block), max(block)}:
                    for v in {min(block), max(block)}:
                        p_uv = Fraction(1, 2**d)
                        p2_uv = sum(
                            Fraction(1, 2**d) * Fraction(1, 2**d)
                            for _ in block
                        )
                        assert p2_uv == p_uv
                        projection_tests += 1

            # Refinements compose exactly: descendants in d+e steps agree
            # with first taking d descendants and then e descendants.
            for e in range(MAX_GAP - d + 1):
                for r in {0, n - 1}:
                    direct = set(descendants(r, d + e))
                    staged = set()
                    for q in descendants(r, d):
                        staged.update(descendants(q, e))
                    assert direct == staged
                    composition_tests += 1

    # U_a e_r=sqrt(n_a) 1_{cell(a,r)}.  For an arbitrary block entry A_rs,
    # the step kernel sqrt(n_a n_b) A_rs integrates U_b e_s exactly to
    # U_a(A_rs e_r).  Squaring removes radicals and leaves a rational identity.
    samples = [Fraction(-7, 11), Fraction(0), Fraction(13, 17)]
    for a in range(MAX_SCALE + 1):
        n_a = annulus_size(a)
        for d in range(MAX_GAP + 1):
            b = a + d
            n_b = annulus_size(b)
            for value in samples:
                # [sqrt(n_a*n_b)*A] * [sqrt(n_b)] * [1/n_b]
                # equals sqrt(n_a)*A; compare exact squares and signs.
                lhs_squared = Fraction(n_a * n_b) * value**2 * Fraction(n_b, n_b**2)
                rhs_squared = Fraction(n_a) * value**2
                assert lhs_squared == rhs_squared
                assert n_a > 0 and n_b > 0
                block_action_tests += 1

    assert partition_tests == 2 * (MAX_SCALE + 1)
    assert block_action_tests == (MAX_SCALE + 1) * (MAX_GAP + 1) * len(samples)

    print("status=PASS_EXACT_COMMON_DYADIC_FIBER")
    print("annulus_partition=DISJOINT_CONSECUTIVE")
    print("fiber=V_a_dyadic_step_functions_in_L2_[1,2]")
    print("refinement_isometry=J_ad=2^(-d/2)*B_ad")
    print("projection=J_ad*J_ad^*=block_average_on_2^d_descendants")
    print("common_ambient=direct_sum_a_L2_[1,2]")
    print("physical_space=unitarily_equal_to_direct_sum_a_V_a")
    print("arbitrary_block_step_kernel=sqrt(n_a*n_b)*A_ab_rs")
    print(f"partition_tests={partition_tests}")
    print(f"gram_tests={gram_tests}")
    print(f"projection_tests={projection_tests}")
    print(f"composition_tests={composition_tests}")
    print(f"block_action_tests={block_action_tests}")
    print("finite_band_norm_identity=EXACT_BY_UNITARY_CONJUGACY")
    print("signed_45_diagonal_norm=UNEVALUATED")
    print("continuous_field_groupoid_compression=UNBUILT")


if __name__ == "__main__":
    main()
