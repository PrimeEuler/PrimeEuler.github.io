#!/usr/bin/env python3
"""Gravity v15.983: fixed D=N+1 transition-circle spectrum and
conditional physical light-speed dictionary. Exact SU(2) Schwinger
amplitudes, Cayley factor ratios, state/edge interleaving, and a
constant-mass obstruction for a fixed-energy relativistic reading.
"""
import sympy as s
D, k = s.symbols('D k', integer=True, positive=True)
T = D/s.Integer(2)
X = T-k
f = k*(D-k)
beta = s.factor(X/T)
assert s.simplify(T*T-X*X-f) == 0
assert s.simplify(f-T*T*(1-beta**2)) == 0
assert s.simplify((1+beta)/(1-beta)-(D-k)/k) == 0
assert s.simplify((T/X)-D/(D-2*k)) == 0
assert s.simplify((1-beta**2)-4*k*(D-k)/D**2) == 0
assert s.simplify(f/s.factor((k+1)*(D-k-1)) -
                  (1-beta**2)/(1-(1-2*(k+1)/D)**2)) == 0
j=(D-1)/s.Integer(2)
r=s.symbols('r', integer=True, nonnegative=True)
m=j-r
assert s.simplify(m-(T-(r+s.Rational(1,2))))==0
assert s.simplify(f.subs(k,r+s.Rational(1,2))-
                  ((f.subs(k,r)+f.subs(k,r+1))/2+s.Rational(1,4)))==0
assert [s.simplify((j-r)/T).subs(D,4) for r in range(4)] == [s.Rational(3,4),s.Rational(1,4),-s.Rational(1,4),-s.Rational(3,4)]
assert [beta.subs({D:4,k:z}) for z in range(1,4)] == [s.Rational(1,2),0,-s.Rational(1,2)]
for d in range(3,30):
    fs=[z*(d-z) for z in range(1,d)]
    for z in range(1,d):
        b=s.Rational(d-2*z,d)
        assert abs(b)<1
        assert s.simplify(s.Rational(d*d,4)*(1-b*b)-fs[z-1])==0
    if d>=4:
        assert len(set(fs))>1
print('PASS: exact transition/null identities, ratio and half-step identities; D=3..29 controls')
