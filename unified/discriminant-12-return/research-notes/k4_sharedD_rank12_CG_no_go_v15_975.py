#!/usr/bin/env python3
"""Gravity v15.975 -- SU2 tensor rank 1 and 2 selection on the
*closed* matched-D EM spin (D-1)/2 and q2 spin (2D-1)/2.
For ordinary integer-spin tensors, triangle and parity give rank 1
only D=2, rank 2 D=2 or D=4. These rules apply to a single common SU2
action; if a cross-sector map is not SU2 covariant, no such inference.
"""
from fractions import Fraction
for D in range(2,101):
    je=Fraction(D-1,2)
    jq=Fraction(2*D-1,2)
    gap=jq-je
    assert gap==Fraction(D,2)
    for k in (1,2):
        allowed=(abs(jq-je)<=k<=jq+je
                 and (jq-je).denominator==1)
        assert allowed==((D==2) if k==1 else (D in (2,4)))
    if D%2:
        assert gap.denominator==2
    else:
        assert gap.denominator==1
print("PASS: rank 1 only D=2; rank 2 only D=2,4; D>4 both forbidden")
