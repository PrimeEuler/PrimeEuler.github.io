#!/usr/bin/env python3
"""Exact arithmetic for the Lane A v15.456 annulus-truncation barrier.

This certifies a uniform lower bound for every dyadic diagonal block of the
constant-Hankel operator C(j,k)=1/[2(N+j+k)].  It does not evaluate the signed
joint operator P+C_near(22).
"""

from fractions import Fraction


NEAR_JOINT_MARGIN = Fraction(
    "0.000102161983428448238386143268860611667901091380097629678822426476751658630579456575507632181"
)


def diagonal_block_lower(a: int) -> Fraction:
    """Constant-vector Rayleigh lower bound on the a-th diagonal annulus."""
    assert a >= 0
    return Fraction(2**a, 2 * (2 ** (a + 2) - 1))


def main() -> None:
    one_eighth = Fraction(1, 8)
    samples = [diagonal_block_lower(a) for a in range(8)]

    # Exact identity: lower(a)-1/8 = 1/[8(2^(a+2)-1)] > 0.
    for a, lower in enumerate(samples):
        assert lower - one_eighth == Fraction(1, 8 * (2 ** (a + 2) - 1))
        assert lower > one_eighth

    assert one_eighth > NEAR_JOINT_MARGIN

    print("status=PASS_EXACT_ANNULUS_TRUNCATION_BARRIER")
    print("uniform_diagonal_block_lower_strict=1/8")
    print(f"near_joint_margin={NEAR_JOINT_MARGIN.numerator}/{NEAR_JOINT_MARGIN.denominator}")
    print(f"barrier_to_margin_ratio_lower={float(one_eighth / NEAR_JOINT_MARGIN):.12f}")
    print("finite_annulus_constant_tail_status=NOT_NORM_SMALL")
    print("signed_joint_gate_status=UNEVALUATED")


if __name__ == "__main__":
    main()
