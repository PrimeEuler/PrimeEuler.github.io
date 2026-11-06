#!/usr/bin/env python3
"""Exact certificate for the Lane A v15.444 odd-extension reduction.

This certifies algebra and target arithmetic only.  It does not certify the
required full commutator norm bound.
"""

from decimal import Decimal, getcontext
from fractions import Fraction


getcontext().prec = 80

FULL_TARGET = Decimal("2.535946")
DIAGONAL_UPPER = Decimal("0.000008959074744668966136851027926")
POLE_UPPER = Decimal("0.000008056")
PRIME_COMMUTATOR_BOUND = Decimal("2.534644890455112455357343436959794")


def half_line_coefficient(n: int, m: int, zn: Fraction, zm: Fraction) -> Fraction:
    """Coefficient of f_m in [Z,H_-]-{Z,H_+}, without 1/pi."""
    return (
        zn * (Fraction(1, n - m) - Fraction(1, n + m))
        - zm * (Fraction(1, n - m) + Fraction(1, n + m))
    )


def canonical_coefficient(n: int, m: int, zn: Fraction, zm: Fraction) -> Fraction:
    return Fraction(2) * (m * zn - n * zm) / (n * n - m * m)


def mirror_coefficient(n: int, zn: Fraction) -> Fraction:
    """k=-n contribution to [M_{Zodd},H]Of on the positive half-line."""
    z_minus_n = -zn
    odd_input_factor = Fraction(-1)
    return (zn - z_minus_n) * Fraction(1, n - (-n)) * odd_input_factor


def main() -> None:
    samples = (
        (2, 1, Fraction(7, 13), Fraction(-5, 11)),
        (5, 3, Fraction(-17, 19), Fraction(23, 29)),
        (11, 4, Fraction(31, 37), Fraction(41, 43)),
        (19, 7, Fraction(-47, 53), Fraction(-59, 61)),
    )
    for n, m, zn, zm in samples:
        assert n != m
        assert half_line_coefficient(n, m, zn, zm) == canonical_coefficient(n, m, zn, zm)
        assert mirror_coefficient(n, zn) == -zn / n

    commutator_target = FULL_TARGET - DIAGONAL_UPPER - POLE_UPPER
    remaining_beyond_prime = commutator_target - PRIME_COMMUTATOR_BOUND

    assert commutator_target == Decimal("2.535928984925255331033863148972074")
    assert remaining_beyond_prime == Decimal("0.001284094470142875676519712012280")

    print("status=PASS_EXACT_REDUCTION_ONLY")
    print(f"full_target={FULL_TARGET}")
    print(f"diagonal_upper={DIAGONAL_UPPER}")
    print(f"pole_upper={POLE_UPPER}")
    print(f"commutator_target={commutator_target}")
    print(f"prime_commutator_bound={PRIME_COMMUTATOR_BOUND}")
    print(f"remaining_beyond_prime={remaining_beyond_prime}")
    print("norm_gate_status=UNEVALUATED")


if __name__ == "__main__":
    main()
