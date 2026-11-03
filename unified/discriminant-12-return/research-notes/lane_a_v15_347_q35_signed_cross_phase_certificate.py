#!/usr/bin/env python3
"""Exact formal certificate for the q=3,5 sine cross-term phases.

Only the group-algebra bookkeeping is certified here.  The sawtooth
difference multipliers remain attached to their corresponding shifts.
"""
from fractions import Fraction as F


def kappa_sign(sigma):
    """Return the coefficient of i in sigma/(2i) = (-sigma/2)i."""
    return F(-sigma, 2)


rows = []
for sigma in (+1, -1):
    for tau in (+1, -1):
        # conj(kappa_3,sigma) * kappa_5,tau is real with sign sigma*tau.
        signed_scalar = kappa_sign(sigma) * kappa_sign(tau)
        assert signed_scalar == F(sigma * tau, 4)
        # A_(sigma,tau)=T_(3,sigma)^* T_(5,tau) has this formal shift.
        shift = (tau, -sigma)  # tau*L5 - sigma*L3
        # Its adjoint is T_(5,tau)^* T_(3,sigma), with opposite shift and
        # the same real scalar.  This is the cross term paired in T^*T.
        adjoint_shift = (-tau, sigma)
        assert adjoint_shift == tuple(-v for v in shift)
        rows.append((sigma, tau, signed_scalar, shift, adjoint_shift))

expected = {
    (+1, +1): (F(1, 4), (+1, -1)),   # +(L5-L3)
    (+1, -1): (F(-1, 4), (-1, -1)),  # -(L5+L3)
    (-1, +1): (F(-1, 4), (+1, +1)),  # +(L5+L3)
    (-1, -1): (F(1, 4), (-1, +1)),   # -(L5-L3)
}
for sigma, tau, scalar, shift, _ in rows:
    assert (scalar, shift) == expected[(sigma, tau)]

print("sigma tau scalar shift=tau*L5-sigma*L3 adjoint_shift")
for row in rows:
    print(*row)
print("certified", "+,-,-,+ physical sine cross-phase pattern")
print("certified", "four T3^*T5 terms pair with four adjoints in T^*T")
