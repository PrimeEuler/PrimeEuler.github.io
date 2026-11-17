#!/usr/bin/env python3
"""Gravity v15.1090: stationary electric probe detects EM duality phase; gravity source does not.
Ideal source-free Maxwell field and negligible test charge: no charged-probe backreaction.
"""
import sympy as s
A,a,b,c,Q,V=s.symbols('A a b c Q V',positive=True,real=True)
x,y,z=s.symbols('x y z',real=True)
f=lambda u:(1-u*u)**3
psi=A*f(x/a)*f(y/b)*f(z/c)
E=s.Matrix([s.diff(psi,y),-s.diff(psi,x),0])
Ev=s.simplify(E.subs({x:0,y:b/2,z:0}))
assert Ev==s.Matrix([-s.Rational(27,16)*A/b,0,0])
def stress(e,B):
 rho=(e.dot(e)+B.dot(B))/2
 return rho,s.eye(3)*rho-e*e.T-B*B.T,e.cross(B)
reference=stress(Ev,s.zeros(3,1))
for C,S in [(1,0),(0,1),(s.sqrt(2)/2,s.sqrt(2)/2),(s.Rational(3,5),s.Rational(4,5))]:
 e=C*Ev; B=-S*Ev
 r,T,momentum=stress(e,B)
 assert s.simplify(r-reference[0])==0
 assert (T-reference[1]).applyfunc(s.simplify)==s.zeros(3)
 assert (momentum-reference[2]).applyfunc(s.simplify)==s.zeros(3,1)
 force=Q*(e+s.Matrix([0,0,V]).cross(B))
 assert (force-Q*(C*Ev-S*s.Matrix([0,0,V]).cross(Ev))).applyfunc(s.simplify)==s.zeros(3,1)
 if C==0: assert s.simplify(force.subs(V,0))==s.zeros(3,1)
 if S==0: assert s.simplify(force.subs(V,0)-Q*Ev)==s.zeros(3,1)
e=Ev/s.sqrt(2); B=-Ev/s.sqrt(2)
assert s.simplify(e.dot(e)-B.dot(B))==0
assert s.simplify(e.dot(B)+Ev.dot(Ev)/2)==0
assert s.simplify(e.cross(B))==s.zeros(3,1)
print('PASS: exact compact field at point, full source duality equality and charge force discrimination')
