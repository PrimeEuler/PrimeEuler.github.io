#!/usr/bin/env python3
"""Directed-Decimal arithmetic for the v15.447 mixed-Gram barrier.

The mathematical implication is proved in the accompanying ledger.  This
script freezes the audited endpoints and evaluates the resulting thresholds;
it is not a certificate for the open full-commutator norm gate.
"""

from decimal import Decimal, getcontext


getcontext().prec = 90

JOINT_TARGET = Decimal("2.535928984925255331033863148972074")
PRIME_UPPER = Decimal("2.534644890455112455357343436959794")
CONSTANT_HANKEL_NORM = Decimal(
    "1.570796326794896619231321691639751442098584699687552910487"
)
NONPRIME_UPPER = Decimal("0.000003108")


def main() -> None:
    square_allowance = JOINT_TARGET**2 - PRIME_UPPER**2
    remainder_norm_lower = CONSTANT_HANKEL_NORM - NONPRIME_UPPER
    remainder_square_lower = remainder_norm_lower**2
    mixed_expectation_required = square_allowance - remainder_square_lower
    retained_fraction = square_allowance / remainder_square_lower

    assert square_allowance == Decimal(
        "0.006511095873826861093859237590420287629662490904514607857259339040"
    )
    assert remainder_norm_lower == Decimal(
        "1.570793218794896619231321691639751442098584699687552910487"
    )
    assert remainder_square_lower == Decimal(
        "2.46739133621203196163123760807340255113346076700770439877296199473557448029586573791719534"
    )
    assert mixed_expectation_required == Decimal(
        "-2.46088024033820510053737837048298226350379827610318979091570265569557448029586573791719534"
    )
    assert retained_fraction < Decimal("0.002639")

    print("status=PASS_MIXED_GRAM_BARRIER_ARITHMETIC")
    print(f"joint_target={JOINT_TARGET}")
    print(f"prime_upper={PRIME_UPPER}")
    print(f"square_allowance={square_allowance}")
    print(f"remainder_norm_lower={remainder_norm_lower}")
    print(f"remainder_square_lower={remainder_square_lower}")
    print(f"mixed_expectation_required_lt={mixed_expectation_required}")
    print(f"retained_fraction_lt={retained_fraction}")
    print("full_norm_gate=UNEVALUATED")


if __name__ == "__main__":
    main()
