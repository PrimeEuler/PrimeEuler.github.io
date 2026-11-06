#!/usr/bin/env python3
"""Exact-decimal certificate for the v15.431 full-tail bound update.

This inserts the independently audited v15.423/v15.424 commutator norm
into the exact v15.309 decomposition.  The remaining terms retain the
certified v15.309 outward bounds; no numerical probe is consumed.
"""

from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

# Audited outward upper endpoint from v15.426 / External Audit Round 486.
commutator_upper = D("2.534644890455112455357343436959794")

# Certified v15.309 outward bounds.
wbar_upper = D("5.634544")
zbar_upper = D("7.205332")
n0 = D(256001)
pole_upper = D("0.000008056")

# Simple rational outward constants: pi/2 < 1.570797 and 1/pi < 0.31831.
constant_hankel_upper = D("1.570797")
inv_pi_upper = D("0.31831")

diagonal_restoration_upper = zbar_upper * inv_pi_upper / n0
full_tail_upper = (
    commutator_upper
    + wbar_upper
    + constant_hankel_upper
    + diagonal_restoration_upper
    + pole_upper
)

assert diagonal_restoration_upper < D("0.000008960")
assert full_tail_upper < D("9.740003")
assert full_tail_upper < D("12.84")

print("commutator_upper", commutator_upper)
print("variable_hankel_anticommutator_upper", wbar_upper)
print("constant_hankel_upper", constant_hankel_upper)
print("diagonal_restoration_upper", diagonal_restoration_upper)
print("pole_upper", pole_upper)
print("full_tail_upper", full_tail_upper)
print("certified", "||Q B Q|| < 9.740003 on either physical parity tail n>=256001")
print("scope", "chosen counting-measure ell2 only; no FULL_K_TRANSFER or source-native Suzuki Phi")
