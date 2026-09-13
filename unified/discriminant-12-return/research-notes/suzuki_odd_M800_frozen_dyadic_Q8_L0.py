#!/usr/bin/env python3
"""Frozen exact-dyadic odd-sector Q8 and L0 verifier inputs.

Source-faithful odd-v/even-index sector, low core C={2,4,...,20}, finite high
block through mode 800.  The frozen basis is the midpoint Schur eigenspace
corresponding to directions 3,...,10.

Every hexadecimal literal is the exact IEEE-754 binary64 dyadic value.  The
verifier must treat these as fixed mathematical inputs and must not regenerate
an eigenspace or Cholesky factor.

The first eight rows of Q8 form an 8x8 dyadic minor with exact nonzero
rational determinant, so rank(Q8)=8 exactly.  L0 is lower triangular with
nonzero dyadic diagonal and is exactly invertible.

Guardrail: exact frozen verifier inputs only; odd-sector outward replay remains
open. No exact-zero, RH, GRH, or final odd inertia conclusion follows here.
"""
from fractions import Fraction

Q8_HEX = [
['%s'],
]

L0_HEX = [
['%s'],
]

def fhex(s):
    x=float.fromhex(s)
    n,d=x.as_integer_ratio()
    return Fraction(n,d)

def bareiss_det(A):
    A=[row[:] for row in A]
    n=len(A)
    sign=1
    prev=Fraction(1,1)
    for k in range(n-1):
        if A[k][k] == 0:
            swap=next(i for i in range(k+1,n) if A[i][k] != 0)
            A[k],A[swap]=A[swap],A[k]
            sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*piv-A[i][k]*A[k][j])/prev
        prev=piv
        for i in range(k+1,n):
            A[i][k]=Fraction(0,1)
    return sign*A[-1][-1]

if __name__ == '__main__':
    Q=[[fhex(x) for x in row] for row in Q8_HEX]
    minor=[row[:] for row in Q[:8]]
    det=bareiss_det(minor)
    print('exact first-8-row minor determinant =', det)
    print('decimal diagnostic =', float(det))
    assert det != 0
    assert all(float.fromhex(L0_HEX[i][i]) != 0.0 for i in range(8))
    print('PASS: rank(Q8)=8 exactly; L0 invertible exactly')
