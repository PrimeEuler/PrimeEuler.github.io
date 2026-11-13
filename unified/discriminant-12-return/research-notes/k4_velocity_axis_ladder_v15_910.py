#!/usr/bin/env python3
"""Gravity v15.910 — SI velocity-axis versus SU(2) transition dynamics.
u has m/s, H=hbar*g*Jx with g in s^-1. X as physical velocity is a
conditional operator identification, not automatically particle velocity.
"""
import sympy as s
n,k,u,g,t=s.symbols('n k u g t',positive=True)
X=lambda a,b:u*(a-b)/2
assert s.simplify(X(n+1,k-1)-X(n,k)-u)==0
assert s.simplify(n*k-(n-1)*(k+1)+(n-k-1))==0
V=u/2+u*(n-k-1)*s.cos(g*t)/2
assert s.simplify(V.subs(t,0)-X(n,k))==0
assert s.simplify(s.diff(V,t).subs(t,0))==0
assert s.simplify(s.diff(V,t,2).subs(t,0)+u*g*g*(n-k-1)/2)==0
for D in range(2,11):
    jp=s.zeros(D)
    for a in range(D-1):
        jp[a+1,a]=s.sqrt((a+1)*(D-a-1))
    jm=jp.T
    jx=(jp+jm)/2
    jy=(jp-jm)/(2*s.I)
    jz=s.diag(*[s.Rational(2*a-D+1,2) for a in range(D)])
    xop=u*(jz+s.eye(D)/2)
    assert s.simplify(jx*jy-jy*jx-s.I*jz)==s.zeros(D)
    assert s.simplify(s.I*g*(jx*xop-xop*jx)-g*u*jy)==s.zeros(D)
    assert s.simplify(-g*g*(jx*(jx*xop-xop*jx)-(jx*xop-xop*jx)*jx)+g*g*u*jz)==s.zeros(D)
    for a in range(D):
        npair,kpair=a+1,D-1-a
        assert s.simplify(xop[a,a]-X(npair,kpair))==0
        assert jy[a,a]==0
        if a<D-1:
            assert s.simplify(jp[a+1,a]**2-npair*kpair)==0
print('PASS: fixed-D shells 2..10; adjacent velocity nodes spaced u (m/s)')
print('PASS: initial <X> acceleration zero in Jz eigenstate under Jx drive')
print('PASS: time jerk d²<X>/dt² = -g²u<Jz> and arbitrary g survives')
for a,b in [(3,2),(4,1),(5,0)]:
    print((a,b),'X/u=',(a-b)/2,'jerk/(u*g²)=',-(a-b-1)/2)
