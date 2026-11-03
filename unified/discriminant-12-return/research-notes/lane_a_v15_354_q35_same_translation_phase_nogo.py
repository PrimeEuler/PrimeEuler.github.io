#!/usr/bin/env python3
"""Exact formal q=3,5 same-translation phase-collection certificate."""
from collections import defaultdict
from fractions import Fraction as F


groups = defaultdict(list)
for sigma in (+1, -1):
    for tau in (+1, -1):
        scalar = F(sigma * tau, 4)
        shift = (tau, -sigma)  # tau*L5 - sigma*L3
        groups[shift].append(("A", sigma, tau, scalar))
        groups[tuple(-v for v in shift)].append(("A*", sigma, tau, scalar))

expected = {
    (+1, -1): F(+1, 2),  # +(L5-L3)
    (-1, +1): F(+1, 2),  # -(L5-L3)
    (+1, +1): F(-1, 2),  # +(L5+L3)
    (-1, -1): F(-1, 2),  # -(L5+L3)
}

assert set(groups) == set(expected)
for shift, terms in groups.items():
    assert len(terms) == 2
    scalars = [term[3] for term in terms]
    # Same-translation physical sine phases reinforce, rather than cancel.
    assert scalars[0] == scalars[1]
    assert sum(scalars, F(0)) == expected[shift]

for shift in sorted(groups):
    print("shift", shift, "terms", groups[shift], "phase_sum", expected[shift])
print("certified", "same-translation phase factors reinforce: +1/2,+1/2,-1/2,-1/2")
print("scope", "sawtooth coefficient multipliers remain distinct and unevaluated")
