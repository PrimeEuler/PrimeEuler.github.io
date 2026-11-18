#!/usr/bin/env python3
"""Gravity v15.1182: 'cone of observability' is the future quadratic
hyperboloid Q=1/4, not a global T-translated null cone.
At fixed U=T-X=K>0, it IS the null parabolic section translated
along the complementary null coordinate V=T+X by mu/K.
That exactly reproduces the Jxy focal offset mu/(2K).
No physical mass-shell or gravitational coupling is inferred.
"""
import sympy as s
T,X,Y,K,mu,a=s.symbols('T X Y K mu a',real=True,nonzero=True)
U=T-X;V=T+X
Q=T*T-X*X-Y*Y
assert s.expand(Q-(U*V-Y*Y))==0
d=mu/(2*K)
shifted=s.expand(Q.subs({T:T+d,X:X+d},simultaneous=True))
assert s.simplify(shifted-Q-mu*U/K)==0
assert s.simplify((shifted-mu).subs(T,X+K)-Q.subs(T,X+K))==0
assert s.simplify((T+d)-(X+d)-U)==0
assert s.simplify((T+d)+(X+d)-V-mu/K)==0
xvertex=(mu-K*K)/(2*K)
focus=s.simplify(xvertex+K/2)
assert s.simplify(focus-mu/(2*K))==0
k=s.symbols('k',integer=True,nonnegative=True)
assert s.simplify(focus.subs({mu:s.Rational(1,4),K:k+s.Rational(1,2)})-1/(4*(2*k+1)))==0
assert s.expand(((T-a)**2-X*X-Y*Y)-Q+2*a*T-a*a)==0
for spin in [s.Integer(0),s.Rational(1,2),s.Integer(1),s.Rational(3,2),s.Integer(2)]:
    t=spin+s.Rational(1,2)
    R=s.sqrt(spin*(spin+1))
    assert s.simplify(t*t-R*R-s.Rational(1,4))==0
    assert s.simplify((t-R)*(t+R)-s.Rational(1,4))==0
print("PASS global Q=1/4 hyperboloid and fixed-U null-direction translate")
print("PASS focus shift 1/[4(2k+1)], no global fixed-T translation")
print("SCOPE representation-space geometry; not physical gravity mass shell")
