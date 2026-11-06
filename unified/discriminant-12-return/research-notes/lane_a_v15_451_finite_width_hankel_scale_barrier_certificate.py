#!/usr/bin/env python3
"""Exact arithmetic for the v15.451 finite-width Hankel scale barrier.

The proof uses the Schur row bound stated in the ledger.  All checks here use
integers/Fractions; this is not a full joint-operator norm certificate.
"""

from fractions import Fraction


PHYSICAL_N = 256001


def crude_schur_bound(n0: int, width: int) -> Fraction:
    """M/(2N) for a step-two constant-Hankel block."""
    return Fraction(width, 2 * n0)


def exact_max_row_sum(n0: int, width: int) -> Fraction:
    """Maximum absolute row sum, attained at the first row."""
    return sum((Fraction(1, 2 * n0 + 2 * k) for k in range(width)), Fraction())


def main() -> None:
    for width in (128, 256, 512, 1024):
        exact = exact_max_row_sum(PHYSICAL_N, width)
        crude = crude_schur_bound(PHYSICAL_N, width)
        assert exact <= crude
        print(
            f"width={width} exact_row_upper={float(exact):.18f} "
            f"crude_upper={float(crude):.18f}"
        )

    assert crude_schur_bound(PHYSICAL_N, 1024) < Fraction(1, 500)
    assert crude_schur_bound(PHYSICAL_N, PHYSICAL_N - 1) < Fraction(1, 2)
    assert crude_schur_bound(PHYSICAL_N, PHYSICAL_N) == Fraction(1, 2)

    print("status=PASS_EXACT_FINITE_WIDTH_BARRIER")
    print(f"physical_tail_origin={PHYSICAL_N}")
    print("necessary_width_for_norm_at_least_half>=256001")
    print("full_joint_norm_gate=UNEVALUATED")


if __name__ == "__main__":
    main()
