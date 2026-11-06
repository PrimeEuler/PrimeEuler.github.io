#!/usr/bin/env python3
"""v15.435: outward-consistent Zbar hardening of the corrected tail bound."""

from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

physical_commutator_upper = D("2.534644890455112455357343436959794")
nonprime_commutator_upper = D("0.000003108")
wbar_upper = D("5.634544")
pi_over_two_upper = D("1.570797")
# Enforce Zbar = pi/2 + Wbar using outward upper endpoints.
zbar_upper = pi_over_two_upper + wbar_upper
inv_pi_upper = D("0.31831")
n0 = D(256001)
pole_upper = D("0.000008056")

diagonal_restoration_upper = zbar_upper * inv_pi_upper / n0
full_tail_upper = (
    physical_commutator_upper
    + nonprime_commutator_upper
    + wbar_upper
    + pi_over_two_upper
    + diagonal_restoration_upper
    + pole_upper
)

assert zbar_upper == D("7.205341")
assert diagonal_restoration_upper < D("0.000008961")
assert full_tail_upper < D("9.740007")

print("outward_zbar_upper", zbar_upper)
print("diagonal_restoration_upper", diagonal_restoration_upper)
print("hardened_full_tail_upper", full_tail_upper)
print("certified", "||Q B Q|| < 9.740007 on either physical parity tail n>=256001")
print("scope", "outward-rounding hardening only; chosen counting-measure ell2; no FULL_K_TRANSFER")
