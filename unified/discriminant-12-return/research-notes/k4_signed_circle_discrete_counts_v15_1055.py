#!/usr/bin/env python3
"""Gravity v15.1055: exact rational finite-sample check of two-sheet circle arithmetic."""
from fractions import Fraction
for n in range(1,201):
    A=Fraction(n+1,2)
    entries=[]
    for k in range(1,n+1):
        x=A*Fraction(k*k-n,k*k+n)
        assert n*(A+x)/(A-x)==k*k
        h_tri=n+1-k
        h_div=n//k
        assert h_div<=h_tri
        entries.append((x,h_tri,h_div))
    assert all(entries[i][0]<entries[i+1][0] for i in range(n-1))
    tri=n*(n+1)//2
    D=sum(n//k for k in range(1,n+1))
    d=sum(n%k==0 for k in range(1,n+1))
    assert sum(e[1] for e in entries)==tri
    assert sum(e[2] for e in entries)==D
    assert sum(e[1]-e[2] for e in entries)==tri-D
    # Floor of the *wrongly oriented* signed null coordinate
    assert sum((-n)//k for k in range(1,n+1))==-D-(n-d)
print("PASS exact Fraction test, n=1..200")
print("n=11: T=66, D=29, d=2, complement=37")
