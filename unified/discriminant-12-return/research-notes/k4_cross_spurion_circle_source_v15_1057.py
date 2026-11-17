#!/usr/bin/env python3
"""v15.1057 conditional K4 mixed tensor Hessian, not a sourced coupling."""
import sympy as s
b,c,B,C,z=s.symbols('b c B C z',real=True)
J2=s.Rational(8,9)*(b*b+c*c)
J4=-s.Rational(8,9)*(b*b+c*c)**2
M=s.expand(s.diff(J2+J4,b,c))
assert M==-s.Rational(64,9)*b*c
e0=1/s.sqrt(s.pi)
e4=s.sqrt(2/s.pi)*s.cos(4*z)
I=s.simplify(s.integrate(e0*e4*s.cos(2*z)**2,(z,0,s.pi)))
assert s.simplify(I-s.sqrt(2)/4)==0
kernel=M.subs({b:B*s.cos(2*z),c:C*s.cos(2*z)})
V=s.simplify(s.integrate(e0*e4*kernel,(z,0,s.pi)))
assert s.simplify(V+s.Rational(16,9)*s.sqrt(2)*B*C)==0
assert V.subs(C,0)==0
assert s.simplify(V.subs(C,-C)+V)==0
P=s.diag(1,-1)
even=s.diag(s.Symbol('a'),s.Symbol('d'))
odd=s.Matrix([[0,s.Symbol('g')],[s.Symbol('g'),0]])
assert P*even*P==even
assert P*odd*P==-odd
print("PASS: K4 quartic odd susceptibility, normalized 0/4 overlap, parity control")
print("mixed Hessian:",M,"overlap:",I,"conditional projection:",V)
