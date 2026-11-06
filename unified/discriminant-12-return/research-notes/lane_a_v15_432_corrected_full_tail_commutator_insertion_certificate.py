#!/usr/bin/env python3
"""Corrected v15.432 certificate; additive correction to v15.431."""

from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

physical_five_frequency_commutator_upper = D("2.534644890455112455357343436959794")
# v15.309's separately certified remote-z/nonprime amplitude enclosure.
# The scaled commutator norm is at most the same sup bound because
# (1/pi)*2*||E||*||Hminus|| <= ||E|| and ||Hminus||<=pi/2.
nonprime_commutator_upper = D("0.000003108")

wbar_upper = D("5.634544")
zbar_upper = D("7.205332")
n0 = D(256001)
pole_upper = D("0.000008056")
constant_hankel_upper = D("1.570797")
inv_pi_upper = D("0.31831")

diagonal_restoration_upper = zbar_upper * inv_pi_upper / n0
full_tail_upper = (
    physical_five_frequency_commutator_upper
    + nonprime_commutator_upper
    + wbar_upper
    + constant_hankel_upper
    + diagonal_restoration_upper
    + pole_upper
)

assert diagonal_restoration_upper < D("0.000008960")
assert full_tail_upper < D("9.740007")
assert full_tail_upper < D("12.84")

print("physical_five_frequency_commutator_upper", physical_five_frequency_commutator_upper)
print("nonprime_commutator_upper", nonprime_commutator_upper)
print("variable_hankel_anticommutator_upper", wbar_upper)
print("constant_hankel_upper", constant_hankel_upper)
print("diagonal_restoration_upper", diagonal_restoration_upper)
print("pole_upper", pole_upper)
print("corrected_full_tail_upper", full_tail_upper)
print("certified", "||Q B Q|| < 9.740007 on either physical parity tail n>=256001")
print("scope", "chosen counting-measure ell2 only; v15.431 omitted the nonprime commutator and is superseded")
