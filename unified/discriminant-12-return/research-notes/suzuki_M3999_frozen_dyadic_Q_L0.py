#!/usr/bin/env python3
"""Frozen exact-dyadic Q and L0 inputs for the M=3999 Suzuki verifier.

Every hexadecimal literal below is an exact representation of one IEEE-754
binary64 value. The verifier treats these dyadics as fixed mathematical inputs;
it must NOT regenerate eigenvectors or a Cholesky factor.

Q is 10x6. Its first six rows form a 6x6 dyadic minor whose determinant is
computed below with exact Fraction arithmetic and Bareiss elimination. The
result is nonzero, so rank(Q)=6 exactly.

L0 is 6x6 lower triangular with six nonzero dyadic diagonal entries, hence it is
invertible exactly.

These facts remove any eigenvector or moving-Cholesky validation requirement.
The proof target is simply to certify the exact operator inequalities in these
fixed coordinates.

Guardrail: frozen verifier data only; the outward operator replay remains open.
No exact-zero, final inertia, RH, or GRH conclusion follows.
"""

from fractions import Fraction

Q_HEX = [
['0x1.a9b0106ac01e8p-4','0x1.50e85227b79f2p-5','0x1.110e340c239ffp-7','-0x1.26a56146f4c61p-9','-0x1.c3bc320065106p-12','-0x1.3ddf24d66961ap-9'],
['0x1.31614dcd93fadp-2','0x1.f5ac98952c139p-4','0x1.a3f768a3f4820p-6','-0x1.d238dc60d4bc0p-8','-0x1.5b42f56f67900p-10','-0x1.f257751033980p-8'],
['0x1.ce789977291cdp-2','0x1.9b6445cd32180p-3','0x1.710376b61e89ep-5','-0x1.b443abef4fc9cp-7','-0x1.30a7867c4bda8p-9','-0x1.c82d01295d99ep-7'],
['0x1.12868d5f20568p-1','0x1.17dbd9766c281p-2','0x1.1a23c7dfb9336p-4','-0x1.75e2ce9fbf67cp-6','-0x1.c8458b60c3edep-9','-0x1.75967d178eb3ep-6'],
['0x1.fe7099bce9880p-12','-0x1.6029608f09120p-12','-0x1.0b6cac294ebf3p-4','0x1.e3081403468f4p-3','-0x1.de674a31d9b83p-1','-0x1.092202100922cp-2'],
['0x1.78ae806502bb8p-2','0x1.73a4763af9621p-2','0x1.3eb502e4eff0dp-3','-0x1.7fefb6818df0cp-4','-0x1.ecb9b14c73288p-7','-0x1.2bf87ac4484d6p-4'],
['-0x1.ae668ca1cd0f0p-3','0x1.596694f849d90p-4','0x1.5de702d2aa8f2p-2','-0x1.a2b41e5441d46p-1','-0x1.0cbaa50837aebp-3','-0x1.6e2e1c3e46549p-2'],
['-0x1.5706bcc587e32p-2','0x1.ab01142a9e1b8p-2','0x1.49a79c77f13f3p-1','0x1.ec9bd6cef6483p-2','0x1.09f8afc5c94a0p-3','-0x1.8c7426ec776aep-3'],
['-0x1.5886f59dbcaa3p-2','0x1.70067d3c53b3dp-1','-0x1.900a8aa8bfe82p-2','-0x1.36755ea389b2ep-3','-0x1.030b5f2af21c4p-3','0x1.a98d4a3cfb6f8p-2'],
['0x1.ffa22a56bf28ep-5','-0x1.93cc3126d01fep-3','0x1.0ef7cb0da9f59p-1','-0x1.ba679d6129a27p-4','-0x1.1b6a2e159d855p-2','0x1.88dcec0ac34b7p-1'],
]

L0_HEX = [
['0x1.9be6472ce844cp-13','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['0x1.1bc7b425ec472p-43','0x1.e1d13acd74362p-7','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.0334f3068864cp-42','-0x1.bebb714d496d0p-50','0x1.c1a4c3504ca1fp-1','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.8f493ba5ca6eep-42','0x1.1aa47eb676025p-48','0x1.86ea932041c6ap-52','0x1.4dfa151bb0094p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.d4b7b575bf7d5p-44','0x1.a231497eb8b46p-48','0x1.80e1a99ec70cfp-52','0x1.670073992bbbdp-56','0x1.6b6c07a0eec9ap+0','0x0.0p+0'],
['0x1.e1711cbdb3146p-42','0x1.d0b5ccbc83ab6p-50','-0x1.452798c7f5298p-50','0x1.6dad86e75f51ap-53','0x1.a00d12034cd1fp-54','0x1.883bd6fde0ad5p+0'],
]

Q_GRAM_ERROR_MIDPOINT_2NORM = 1.290470233512659e-15
L0_DIAG_HEX = [L0_HEX[i][i] for i in range(6)]


def dyadic(hex_literal: str) -> Fraction:
    """Convert an exact binary64 hex literal to its exact rational value."""
    x = float.fromhex(hex_literal)
    p, q = x.as_integer_ratio()
    return Fraction(p, q)


def bareiss_det(matrix):
    """Exact determinant via fraction-free Bareiss-style elimination."""
    A = [[Fraction(v) for v in row] for row in matrix]
    n = len(A)
    if n == 0:
        return Fraction(1)
    sign = 1
    prev = Fraction(1)
    for k in range(n - 1):
        if A[k][k] == 0:
            swap = next((r for r in range(k + 1, n) if A[r][k] != 0), None)
            if swap is None:
                return Fraction(0)
            A[k], A[swap] = A[swap], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pivot - A[i][k] * A[k][j]) / prev
        for i in range(k + 1, n):
            A[i][k] = Fraction(0)
        prev = pivot
    return sign * A[-1][-1]


def exact_first6_minor_det():
    minor = [[dyadic(Q_HEX[i][j]) for j in range(6)] for i in range(6)]
    return bareiss_det(minor)


if __name__ == '__main__':
    det = exact_first6_minor_det()
    print('Q shape =', len(Q_HEX), 'x', len(Q_HEX[0]))
    print('exact first-six minor determinant numerator =', det.numerator)
    print('exact first-six minor determinant denominator =', det.denominator)
    print('decimal determinant diagnostic =', float(det))
    print('Q midpoint Gram error 2-norm =', Q_GRAM_ERROR_MIDPOINT_2NORM)
    print('L0 diagonal exact hex =', L0_DIAG_HEX)
    assert det != 0
    assert all(dyadic(x) != 0 for x in L0_DIAG_HEX)
    print('PASS: rank(Q)=6 and invertibility(L0) verified exactly from frozen dyadics')