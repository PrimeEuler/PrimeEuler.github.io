#!/usr/bin/env python3
"""Exact label census for the translation-unitary Cotlar barrier."""
from fractions import Fraction as F
from itertools import combinations, product

Q = (2, 3, 4, 5, 7)
labels = {}
for q, r in combinations(Q, 2):
    for sigma, tau in product((-1, 1), repeat=2):
        value = F(q if sigma == 1 else 1, q if sigma == -1 else 1)
        value *= F(r if tau == 1 else 1, r if tau == -1 else 1)
        labels[(q, r, sigma, tau)] = value

assert len(labels) == 40
assert len(set(labels.values())) == 40

# For lambda_a=log(a), translations U_lambda on L2(R/2Z) satisfy
# U_lambda^* U_mu = U_(mu-lambda).  Every U is unitary, hence every
# off-diagonal Cotlar product has norm exactly one.  The exact rational
# ratios below certify that all 780 products are nonidentity shifts; their
# nonidentity does not make their operator norm smaller.
ratios = []
for (_, a), (_, b) in combinations(labels.items(), 2):
    ratio = b / a
    assert ratio != 1
    ratios.append(ratio)

assert len(ratios) == 780

print("signed_translation_labels", len(labels))
print("unordered_off_diagonal_products", len(ratios))
print("exact_nonidentity_products", len(ratios))
print("translation_identity", "U_lambda^* U_mu = U_(mu-lambda)")
print("certified_norm", "||U_lambda^* U_mu|| = 1 for all 780 off-diagonal pairs")
print("common_mode", "the constant function 1 is fixed by all 40 translations")
print("conclusion", "translation-label distinctness alone supplies no Cotlar decay or orthogonality")
print("next_data", "must use signed multiplication coefficients and their translated overlaps")
print("scope", "operator-representation structural barrier only; not a lower bound on the weighted physical cross sum or complete-tail closure")
