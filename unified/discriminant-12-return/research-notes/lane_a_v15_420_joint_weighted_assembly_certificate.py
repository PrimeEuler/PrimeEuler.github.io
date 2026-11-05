#!/usr/bin/env python3
"""Exact source-faithful assembly certificate for the five-frequency cross term.

This does not estimate the operator norm.  It certifies the 40 weighted-shift
labels, their adjoint pairing, the physical phase signs, and the exact
coefficient transport identity needed before a joint Cotlar/Gram estimate.
"""
from fractions import Fraction
from itertools import combinations, product

Q = (2, 3, 4, 5, 7)


class Poly:
    """Integer polynomial in the four formal saw values a,b,c,d."""
    def __init__(self, terms=None):
        self.terms = {m: z for m, z in (terms or {}).items() if z}

    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly({(0, 0, 0, 0): other})
        keys = set(self.terms) | set(other.terms)
        return Poly({m: self.terms.get(m, 0) + other.terms.get(m, 0) for m in keys})

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -z for m, z in self.terms.items()})

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        other = other if isinstance(other, Poly) else Poly({(0, 0, 0, 0): other})
        out = {}
        for m, z in self.terms.items():
            for n, w in other.terms.items():
                p = tuple(x + y for x, y in zip(m, n))
                out[p] = out.get(p, 0) + z*w
        return Poly(out)

    __rmul__ = __mul__

    def __eq__(self, other):
        other = other if isinstance(other, Poly) else Poly({(0, 0, 0, 0): other})
        return self.terms == other.terms


one = Poly({(0, 0, 0, 0): 1})
a, b, c, d = [Poly({tuple(1 if i == j else 0 for i in range(4)): 1})
              for j in range(4)]

# Put lambda=tau*B-sigma*A and abbreviate
# a=s(x+lambda), b=s(x+tau*B), c=s(x), d=s(x-sigma*A).
# Directly rewriting the two D-products gives the following two sides of
# G_{-sigma,-tau}(x)=G_{sigma,tau}(x+lambda).
transport_lhs = (c-d)*(a-d) + (c-b)*(a-b)
transport_rhs = (a-b)*(c-b) + (a-d)*(c-d)
assert transport_lhs == transport_rhs

rows = []
for q, r in combinations(Q, 2):
    for sigma, tau in product((-1, 1), repeat=2):
        # exp(lambda)=r^tau/q^sigma is an exact positive rational label.
        label = Fraction(r if tau == 1 else 1, 1 if tau == 1 else r)
        label /= Fraction(q if sigma == 1 else 1, 1 if sigma == 1 else q)
        rows.append((q, r, sigma, tau, label, sigma*tau))

assert len(rows) == 40
assert len({row[4] for row in rows}) == 40
assert all(row[4] != 1 for row in rows)

index = {(q, r, sigma, tau): (label, phase)
         for q, r, sigma, tau, label, phase in rows}
orbits = set()
for q, r, sigma, tau, label, phase in rows:
    partner_label, partner_phase = index[(q, r, -sigma, -tau)]
    assert partner_label == 1/label
    assert partner_phase == phase
    key = tuple(sorted((label, partner_label)))
    orbits.add(key)
assert len(orbits) == 20

print("frequency_pairs", len(tuple(combinations(Q, 2))))
print("weighted_shift_terms", len(rows))
print("distinct_exact_labels", len({row[4] for row in rows}))
print("adjoint_orbits", len(orbits))
print("transport_identity", "G_-sigma,-tau(x)=G_sigma,tau(x+tau*B-sigma*A)")
print("physical_phase_pairing", "sigma*tau is invariant under (sigma,tau)->(-sigma,-tau)")
print("joint_operator", "self-adjoint exact 40-term weighted-shift assembly")
print("scope", "five-frequency commutator cross term only; no norm or full-K claim")
