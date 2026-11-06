#!/usr/bin/env python3
"""Exact dyadic-annulus tail arithmetic for Lane A v15.453.

The ledger proves the block-Schur estimate.  This witness freezes a rational
upper approximation to 1/sqrt(2), certifies the first admissible bandwidth,
and computes the remaining joint allowance.  It does not evaluate the near
joint operator.
"""

from decimal import Decimal, getcontext
from fractions import Fraction


getcontext().prec = 90

R_UPPER = Fraction(707107, 1_000_000)  # > 1/sqrt(2)
JOINT_TARGET = Fraction("2.535928984925255331033863148972074")
PRIME_UPPER = Fraction("2.534644890455112455357343436959794")
NONPRIME_UPPER = Fraction("0.000003108")


def far_annulus_tail(bandwidth: int) -> Fraction:
    """Two-sided block-row tail beyond |a-b| <= bandwidth."""
    return R_UPPER ** (bandwidth + 1) / (1 - R_UPPER)


def dec(q: Fraction) -> Decimal:
    return Decimal(q.numerator) / Decimal(q.denominator)


def main() -> None:
    allowance = JOINT_TARGET - PRIME_UPPER
    tail_21 = far_annulus_tail(21)
    tail_22 = far_annulus_tail(22)

    assert R_UPPER * R_UPPER > Fraction(1, 2)
    assert tail_21 + NONPRIME_UPPER > allowance
    assert tail_22 + NONPRIME_UPPER < allowance

    near_joint_margin = allowance - tail_22 - NONPRIME_UPPER
    assert near_joint_margin > 0

    print("status=PASS_EXACT_DYADIC_TAIL_REDUCTION")
    print(f"r_upper={dec(R_UPPER)}")
    print(f"tail_band_21_upper={dec(tail_21)}")
    print(f"tail_band_22_upper={dec(tail_22)}")
    print(f"prime_to_joint_allowance={dec(allowance)}")
    print(f"nonprime_upper={dec(NONPRIME_UPPER)}")
    print(f"near_joint_margin={dec(near_joint_margin)}")
    print("required_dyadic_bandwidth=22")
    print("near_joint_operator_gate=UNEVALUATED")


if __name__ == "__main__":
    main()
