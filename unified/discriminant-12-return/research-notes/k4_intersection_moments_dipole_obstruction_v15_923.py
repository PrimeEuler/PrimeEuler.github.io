#!/usr/bin/env python3
"""Gravity v15.923: signed/weighted AM-GM hyperbola intersections and cross-shell
operator obstruction. Uses integer-product slice ab=N at t=1; for legacy
division t, physical N maps to integer product Nt².
"""
import sympy as s
N=s.symbols("N",integer=True,positive=True)
for n in range(1,90):
    pairs=[(n//k,k) for k in s.divisors(n)]
    xs=[s.Rational(a-b,2) for a,b in pairs]
    ts=[s.Rational(a+b,2) for a,b in pairs]
    ys2=[s.Integer(n) for a,b in pairs]
    d=s.divisor_count(n)
    sig1=s.divisor_sigma(n,1)
    sig2=s.divisor_sigma(n,2)
    assert len(xs)==d
    assert sum(xs)==0
    assert sum(xs[i]**2 for i in range(len(xs)))==s.Rational(sig2-n*d,2)
    assert sum(ys2)==n*d
    assert sum(ts)==sig1
    assert sum(t*t for t in ts)==s.Rational(sig2+n*d,2)
    assert sum(xs[i]**2+ys2[i]-ts[i]**2 for i in range(len(xs)))==0
    # Every unweighted odd X moment cancels by involution (a,b) ↔ (b,a).
    for power in [1,3,5]:
        assert sum(x**power for x in xs)==0
print("PASS exact divisor moments and mirror parity, N=1..89")
pairs=[(12//k,k) for k in s.divisors(12)]
print("N=12:",pairs)
print("N=12: sum X²",sum(s.Rational(a-b,2)**2 for a,b in pairs))
print("N=12: sum Y²",12*len(pairs))
print("N=12: sum T²",sum(s.Rational(a+b,2)**2 for a,b in pairs))
# A diagonal fixed-shell f(X,T,Y²) cannot change the shell D.
# Compare two Hilbert spaces D=2,3 (2+3 states); all measured diagonals
# identical while an arbitrary cross-shell dipole block can be 0 or nonzero.
u=s.symbols("u",positive=True)
shells=[2,3]
vel=[]
labels=[]
for D in shells:
    for a in range(D):
        b=D-1-a
        vel.append(u*s.Rational((a+1)-b,2))
        labels.append((D,a))
Xop=s.diag(*vel)
Top=s.diag(*[u*s.Rational(D,2) for D,a in labels])
P2=s.diag(*[int(D==2) for D,a in labels])
P3=s.eye(len(labels))-P2
assert P2*Xop*P3==s.zeros(len(labels))
assert P2*Top*P3==s.zeros(len(labels))
for power in [0,1,2,3]:
    assert P2*(Xop**power)*P3==s.zeros(len(labels))
dipole=s.zeros(len(labels))
dipole[0,2]=dipole[2,0]=1
assert P2*dipole*P3!=s.zeros(len(labels))
assert all(dipole[i,i]==0 for i in range(len(labels)))
print("PASS same shell diagonal geometry admits both zero and independent nonzero cross-shell dipole (unselected)")
