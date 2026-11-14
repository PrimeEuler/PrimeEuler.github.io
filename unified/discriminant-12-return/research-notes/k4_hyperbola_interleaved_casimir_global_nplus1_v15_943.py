#!/usr/bin/env python3
"""Gravity v15.943: fixed-product hyperbola and two interleaved factor-row
parabola families; global n+1 reconstructible from local midpoint
displacement. Separate from fixed-diameter circle, quarter Casimir
operators and shifted-seat/divisor counts. Exact SymPy verification.
"""
import sympy as s
n,k,j,u=s.symbols('n k j u',positive=True)
h=s.Rational(1,2)
X=lambda t:(n-t*t)/(2*t)
R=lambda t:(n+t*t)/(2*t)
D=lambda t:t+n/t
DX=s.factor(X(k+h)-(X(k)+X(k+1))/2)
DR=s.factor(R(k+h)-(R(k)+R(k+1))/2)
assert s.simplify(DX+n/(4*k*(k+1)*(2*k+1)))==0
assert s.simplify(DR-DX)==0
assert s.simplify(1-4*k*(k+1)*(2*k+1)*DX-(n+1))==0
assert s.factor(D(k)-(n+1))==(k-1)*(k-n)/k
assert s.simplify(R(k)**2-X(k)**2-n)==0
assert s.simplify(X(n/k)+X(k))==0
assert s.simplify(R(n/k)-R(k))==0
C=lambda q:q*(q+1)
DC=s.factor(C(j+s.Rational(1,4))-(C(j)+C(j+h))/2)
assert DC==-s.Rational(1,16)
assert s.simplify(DX-4*n*DC/(k*(k+1)*(2*k+1)))==0
# Physical scale u: recover dimensionless n+1 using DX_phys/u.
assert s.simplify(1-4*k*(k+1)*(2*k+1)*(u*DX)/u-(n+1))==0
# Fixed D=n+1 is different from fixed product n; only at k=1,n
# does D(k)=n+1. The separately known fixed-D GM-square
# interpolation surplus is +1/4.
D0=n+1
Y2=lambda t:t*(D0-t)
assert s.simplify(Y2(k+h)-(Y2(k)+Y2(k+1))/2)==s.Rational(1,4)
assert s.simplify(s.diff(Y2(k),k))==n+1-2*k
for nn in range(2,101):
    for kk in range(1,nn+1):
        dd=s.simplify(DX.subs({k:kk,n:nn}))
        assert 1-4*kk*(kk+1)*(2*kk+1)*dd==nn+1
        if kk not in (1,nn):
            assert D(k).subs({k:kk,n:nn})!=nn+1
for kk in (1,2,3):
    nn=12
    print('n=12 k=',kk,'X_EM=',X(k).subs({k:kk,n:nn}),
          'X_interlay=',X(k+h).subs({k:kk,n:nn}),
          'DX=',DX.subs({k:kk,n:nn}),
          'recovered D=',
          1-4*kk*(kk+1)*(2*kk+1)*DX.subs({k:kk,n:nn}))
print('PASS: symbolic identities, Casimir midpoint -1/16, fixed-D +1/4, 5049 row checks')
