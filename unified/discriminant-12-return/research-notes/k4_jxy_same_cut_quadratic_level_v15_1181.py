#!/usr/bin/env python3
"""Gravity v15.1181. Same 45-degree cut of Q=0 and Q=1/4."""
import sympy as s
T,X,Y,K,mu,j,m=s.symbols("T X Y K mu j m",real=True)
k=s.symbols("k",integer=True,nonnegative=True)
gamma,c=s.symbols("gamma c",real=True)
Q=T*T-X*X-Y*Y
assert s.expand(Q.subs(T,X+K)-(K*K+2*K*X-Y*Y))==0
assert s.simplify(Q.subs(T,X+K).subs(Y*Y,K*K+2*K*X-mu)-mu)==0
vertex=s.simplify((mu-K*K)/(2*K))
focus=s.simplify(vertex+K/2)
assert s.simplify(focus-mu/(2*K))==0
assert s.simplify(vertex.subs({mu:s.Rational(1,4),K:k+s.Rational(1,2)})+k*(k+1)/(2*k+1))==0
assert s.simplify(focus.subs({mu:s.Rational(1,4),K:k+s.Rational(1,2)})-1/(4*(2*k+1)))==0
assert s.simplify((K*K+2*K*X-mu).subs(mu,s.Rational(1,4)).subs(K,k+s.Rational(1,2)) - ((2*k+1)*X+k*(k+1)))==0
assert s.expand((j+s.Rational(1,2))**2-m*m-(j*(j+1)-m*m)-s.Rational(1,4))==0
# Sandbox tilt T*cos(gamma)+Y*sin(gamma)=c.  At gamma=45deg the
# conic is parabolic for ALL constant levels mu of the quadratic form.
section=s.expand(Q.subs(T,(c-s.sin(gamma)*Y)/s.cos(gamma))-mu)
assert s.simplify(section.subs(gamma,0)-(c*c-X*X-Y*Y-mu))==0
at45=s.trigsimp(section.subs(gamma,s.pi/4))
assert s.simplify(s.diff(at45,Y,2))==0
assert s.simplify(s.diff(at45,X,2)+2)==0
assert s.simplify(s.diff(section,Y,2).diff(mu))==0
assert s.simplify(s.diff(section,X,2).diff(mu))==0
assert s.simplify(s.diff(section.subs(gamma,s.pi/6),Y,2))!=0
print("PASS fixed 45-degree plane, Q=0 and Q=1/4, parabolas and focal shift")
print("PASS Sandbox gamma=45-degree parabolic limit unaffected by level mu")
print("NO new gravitational tilt, source, force or Casimir implied")
