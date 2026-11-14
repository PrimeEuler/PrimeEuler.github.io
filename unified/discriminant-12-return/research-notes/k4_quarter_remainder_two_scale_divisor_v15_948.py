#!/usr/bin/env python3
"""Cone Gravity v15.948: original half-grid parabolic remainders vs
quarter-grid refinement. Exact two-scale D(n),D(2n) identities.
This does NOT introduce additional integer-factor stations or a gravity force.
"""
from fractions import Fraction as F

def D(n):
    return sum(n//k for k in range(1,n+1))

def compute(n):
    rows=[F(n-k*k,2*k) for k in range(1,n+1)]
    rem=lambda x,cell: x-(x//cell)*cell
    Bhalf=2*sum((rem(v,F(1,2)) for v in rows),F())
    Bquarter=2*sum((rem(v,F(1,4)) for v in rows),F())
    H=sum((F(1,k) for k in range(1,n+1)),F())
    digit=sum(int(F(n,k)-n//k>=F(1,2)) for k in range(1,n+1))
    assert Bhalf==n*H-D(n)
    assert Bquarter==F(1,2)*sum((F(2*n,k)-(2*n//k) for k in range(1,n+1)),F())
    assert Bhalf-Bquarter==F(digit,2)
    assert digit==D(2*n)-2*D(n)-n
    assert digit==sum((2*n//k-2*(n//k) for k in range(1,n+1)))
    assert D(2*n)==2*n*H+n-2*Bquarter
    assert 0<=digit<=n
    T=n*(n+1)//2
    assert T-D(n)==sum((int(a*b>n)
         for a in range(1,n+1) for b in range(1,n+2-a)))
    return digit, Bhalf, Bquarter

for n in range(1,1001):
    compute(n)
for n in (1,2,3,4,5,6,8,9,12,20,30,60):
    e,half,quarter=compute(n)
    print('n=',n,'D(n)=',D(n),'D(2n)=',D(2*n),
          'upper-half digit=',e,'Bhalf=',half,'Bquarter=',quarter)
print('PASS 1000 exact rational levels, quarter D(2n), T(n) partition')
