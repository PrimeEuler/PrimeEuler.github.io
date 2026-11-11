#!/usr/bin/env python3
"""v15.716: dimension-dependent STF 2/3 identity; do not equate physical sectors."""
import sympy as s
D=s.symbols('D',integer=True,positive=True)
assert s.simplify(1-2/D+D/D**2-(D-1)/D)==0
for d in range(2,11):
    n=s.Matrix([s.Integer(1)]+[s.Integer(0)]*(d-1))
    Q=n*n.T-s.eye(d)/d
    assert s.simplify(s.trace(Q*Q)-s.Rational(d-1,d))==0
    assert Q.trace()==0
x,y,z=s.symbols('x y z',real=True)
S=s.Matrix([[x*x,x*y,x*z],[x*y,y*y,y*z],[x*z,y*z,z*z]])
Q=s.expand(S-s.eye(3)*(x*x+y*y+z*z)/3)
norm=s.expand(s.trace(Q*Q))
assert s.simplify(norm-s.Rational(2,3)*(x*x+y*y+z*z)**2)==0
u=s.symbols('u',real=True)
assert s.integrate(1-u**2,(u,-1,1))/2==s.Rational(2,3)
print('PASS: STF dyad norm=(d-1)/d, d=3 is 2/3; angular moment 2/3 separate')
