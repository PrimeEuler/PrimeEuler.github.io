#!/usr/bin/env python3
"""v15.947. The ORIGINAL Cone triangle T(n)=D(n)+A(n):
(a,b)>0, a+b<=n+1 map to a semicircular half-DISK
X=(a-b)/2, Y=sqrt(ab), R=(a+b)/2.
Parabola offsets modulo 1/2 produce fractional corrections to nH_n;
they are not themselves D(n) without adding nH_n.
All integer and exact rational verification, no physical field claim.
"""
from fractions import Fraction

def check(n):
    v=[Fraction(n-k*k,2*k) for k in range(1,n+1)]
    H=sum((Fraction(1,k) for k in range(1,n+1)),Fraction(0))
    B=sum((2*(w-(w//Fraction(1,2))*Fraction(1,2)) for w in v),Fraction(0))
    T=n*(n+1)//2
    D=sum(n//k for k in range(1,n+1))
    A=T-D
    # All rows k correspond to X_n(k)=(n-k^2)/(2k).
    assert 2*sum(v,Fraction(0))==n*H-T
    assert B==n*H-D
    assert n*H-B==D
    assert B-2*sum(v,Fraction(0))==A
    assert sum(k+(2*w)//1 for k,w in enumerate(v,1))==D
    tri=[(a,b) for a in range(1,n+1) for b in range(1,n+1-a+1)]
    assert len(tri)==T
    assert all(a+b<=n+1 for a,b in tri)
    hits=[(a,b) for a,b in tri if a*b<=n]
    misses=[(a,b) for a,b in tri if a*b>n]
    assert len(hits)==D and len(misses)==A
    outer=[(a,b) for a,b in tri if a+b==n+1]
    assert len(outer)==n
    assert len([1 for a,b in outer if a*b<=n])==(1 if n==1 else 2)
    # Since (a-1)(b-1)>=0, ab>=a+b-1.
    # If ab<=n, automatically a+b<=n+1: D hits are inside T halfdisk.
    for a,b in tri:
        X=Fraction(a-b,2)
        R=Fraction(a+b,2)
        assert X*X+a*b==R*R
        assert a*b>=a+b-1
    return T,D,A,B

for n in range(1,301):
    check(n)
for n in (1,2,3,4,6,12,30,100,300):
    T,D,A,B=check(n)
    print(f"n={n} T={T} D={D} A={A} offset_correction={B}")
print("PASS: n=1..300 exact T=D+A, parabola mod-1/2 formula, "
      "half-disk mapping, outer-boundary stations")
