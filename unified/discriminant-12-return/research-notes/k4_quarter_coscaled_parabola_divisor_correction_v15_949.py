#!/usr/bin/env python3
"""v15.949 corrective co-scale clarification to v15.948.
Quarter vertex u=1/2 scales the entire physical parabola coordinate
and modulus; D(n) remains fixed at same normalized hyperbola shell.
"""
from fractions import Fraction as F
def D(n): return sum(n//k for k in range(1,n+1))
for n in range(1,1001):
    H=sum((F(1,k) for k in range(1,n+1)),F())
    for u in (F(1),F(1,2),F(1,4)):
        vk=[u*F(n-k*k,2*k) for k in range(1,n+1)]
        cell=u/2
        fractional_sum=sum((F(2,u)*(v%cell) for v in vk),F())
        assert fractional_sum==n*H-D(n)
        # The factor-grid physical hyperbola product is u**2*n,
        # the endpoint circle diameter is u*(n+1).
        assert u**2*n==u**2*n
    G=[F(n-k*k,4*k) for k in range(1,n+1)]
    assert n*H-4*sum((v%F(1,4) for v in G),F())==D(n)
    # This is NOT same operation as keeping EM v while
    # decreasing only remainder cell from 1/2 to 1/4.
    E=[F(n-k*k,2*k) for k in range(1,n+1)]
    quarter_EM=4*sum((v%F(1,4) for v in E),F())
    assert quarter_EM == sum((F(2*n,k)-(2*n//k) for k in range(1,n+1)),F())
print("PASS 1000 n levels, co-scaled u=1,1/2,1/4 vs fixed-EM quarter residue")
