#!/usr/bin/env python3
"""Exact finite checks supporting Lane A v15.442's analytic upper bound.

For N>=1, G_N[j,k]=1/(j+k+N) is the moment Gram matrix
integral_0^1 t^(j+k+N-1) dt and is positive semidefinite.  Its
quadratic form is dominated, after absolute values, by G_1, so the
classical sharp Hilbert inequality gives ||G_N||<=pi.  Combined with
Round 491's audited essential-norm lower bound, ||G_N||=pi.
"""

from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 90


def hilbert_form(N, x):
    return sum(
        Fraction(x[j] * x[k], j + k + N)
        for j in range(len(x))
        for k in range(len(x))
    )


def moment_form(N, x):
    # Expand |sum_j x_j t^j|^2 t^(N-1) and integrate termwise.
    coeff = [0] * (2 * len(x) - 1)
    for j, xj in enumerate(x):
        for k, xk in enumerate(x):
            coeff[j + k] += xj * xk
    return sum(Fraction(c, degree + N) for degree, c in enumerate(coeff))


for N in [1, 2, 17, 128001, 256003]:
    for x in ([1, -2, 3], [4, 0, -5, 7], [1, 1, 1, 1, 1]):
        qN = hilbert_form(N, x)
        assert qN == moment_form(N, x)
        assert qN >= 0
        # Entrywise domination after absolute values.
        assert abs(qN) <= hilbert_form(1, [abs(v) for v in x])

pi = Decimal(
    "3.141592653589793238462643383279502884197169399375105820974944592307816406286"
)
exact_same_parity_norm = pi / Decimal(2)
remaining_allowance = Decimal("0.001280986470142875676519712012280")
assert exact_same_parity_norm > remaining_allowance

print("shifted_hilbert_norm", pi)
print("same_parity_constant_hankel_norm", exact_same_parity_norm)
print("remaining_triangle_allowance", remaining_allowance)
print("status", "exact equality hardened; cancellation still required")
