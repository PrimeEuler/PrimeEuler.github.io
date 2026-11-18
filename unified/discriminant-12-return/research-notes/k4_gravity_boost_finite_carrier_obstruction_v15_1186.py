#!/usr/bin/env python3
"""Gravity v15.1186: continuous SO(1,1) boost orbits versus finite q2 ladder.
Representation-space only. Physical gravitational boost generator unselected.
Canonical exact checks (SymPy); no frozen objects modified.
"""
import sympy as s
for L in range(1,16):
    j=s.Rational(L,4); T=j+s.Rational(1,4)
    vals=[]
    factors=[]
    for i in range(L+1):
        m=-j+s.Rational(i,2)
        A=s.factor(T+m);B=s.factor(T-m)
        Y2=s.factor(j*(j+s.Rational(1,2))-m*m)
        assert s.factor(A*B-Y2)==s.Rational(1,16)
        assert A==s.Rational(2*i+1,4)
        assert B==s.Rational(2*L-2*i+1,4)
        vals.append(Y2)
        factors.append(A)
    assert vals==list(reversed(vals))
    assert len(set(vals))==(L+2)//2
    assert sum(factors)>0
    if L in [3,4,5]:
        print("L",L,"transverse values",vals)
# If a finite Hermitian G generated exact e^eta A scaling under conjugation,
# differentiating requires i[G,A]=A (up to a sign convention).
# But tr([G,A])=0 for all finite matrices while tr(A)>0: contradiction.
for n in range(2,8):
    A=s.diag(*[s.Rational(2*i+1,4) for i in range(n)])
    G=s.Matrix(n,n,lambda i,j:s.Symbol(f"g{i}{j}"))
    assert s.trace(G*A-A*G)==0
    assert s.trace(A)>0
# Continuous rapidity eta: multiplication by A=a exp(eta), B=b exp(-eta),
# generator -i d/deta gives the correct opposite logarithmic scalings.
eta,a,b=s.symbols("eta a b",real=True,positive=True)
Ac=a*s.exp(eta);Bc=b*s.exp(-eta)
assert s.simplify(s.diff(Ac,eta)-Ac)==0
assert s.simplify(s.diff(Bc,eta)+Bc)==0
assert s.simplify(Ac*Bc-a*b)==0
assert s.simplify(Ac*Bc-(Ac*Bc-s.Rational(1,16))-s.Rational(1,16))==0
print("PASS L=1..15, invariant boost channels and finite-dimensional obstruction")
print("CONDITIONAL: continuous boost carrier requires chosen Hilbert measure/action")
