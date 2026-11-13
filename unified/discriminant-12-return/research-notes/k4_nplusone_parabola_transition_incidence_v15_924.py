#!/usr/bin/env python3
"""Gravity v15.924: the legacy row-parabola intersections ARE the
fixed D=n+1 Schwinger ladder entries (geometric incidence, not radiative E1).
D=n+1; k=1,...,D-1; X=D/2-k; Y=sqrt(k*(D-k)).
Hyperbola product is P=k*(D-k); same point is X=(P-k*k)/(2*k).
"""
import sympy as s
D,k,P,t=s.symbols('D k P t', positive=True)
X=D/s.Integer(2)-k
Y2=k*(D-k)
assert s.simplify(Y2-(k*k+2*k*X))==0
assert s.simplify(X*X+Y2-(D/s.Integer(2))**2)==0
assert s.simplify(((P-k*k)/(2*k)-X).subs(P,Y2))==0
# The parabola/circle equation has one other root X=-D/2-k,
# associated with a=-D-k <0, outside the positive-pair cone.
roots=s.solve(s.Eq(X*X+k*k+2*k*X,D**2/4),X)
assert all(s.simplify(root-(-k+D/2))==0 or s.simplify(root-(-k-D/2))==0 for root in roots)
# Explicit geometry-to-matrix construction, no post-hoc fitting.
for d in range(2,19):
    M=s.zeros(d)
    for b in range(1,d):
        x=s.Rational(d,2)-b
        y2=s.Rational(b*b)+2*b*x
        product=b*(d-b)
        assert y2==product
        assert x*x+y2==s.Rational(d*d,4)
        assert s.Rational(product-b*b,2*b)==x
        # State |a-1,b> with a=d-b. Under J+ its destination
        # |a,b-1>, indexed (a) in ascending first-mode occupation.
        a=d-b
        M[a,a-1]=s.sqrt(product)
    Jminus=M.T
    Jz=s.diag(*[s.Rational(2*a-(d-1),2) for a in range(d)])
    assert M*Jminus-Jminus*M==2*Jz
    if d==5:
        expected=s.zeros(5)
        for a in range(1,5):
            expected[a,a-1]=s.sqrt(a*(5-a))
        assert M==expected
        print('D=5 amplitudes for k=1..4:',[s.sqrt(b*(5-b)) for b in range(1,5)])
print('PASS exact parabola=hyperbola=circle incidence, D=2..18, SU2 ladder commutator')
