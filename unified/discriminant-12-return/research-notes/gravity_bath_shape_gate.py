#!/usr/bin/env python3
"""Cone gravity: bath and phase eccentricity mapping, exact G-free gate."""
import sympy as s
q=s.symbols("q",positive=True)
e=s.sqrt(1-q*q)
rho2=s.simplify((1-e)/(1+e))
overlap=s.simplify(s.Rational(2,3)*(1-rho2))
qstar=1/s.sqrt(3)
assert s.simplify(rho2.subs(q,qstar)-(5-2*s.sqrt(6)))==0
assert s.simplify(overlap.subs(q,qstar)-(-s.Rational(8,3)+4*s.sqrt(6)/3))==0
x=s.symbols("x",real=True)
assert s.integrate(1-x*x,(x,-1,1))/2==s.Rational(2,3)
print("bath q* =",qstar,"bath eccentricity =",s.simplify(e.subs(q,qstar)))
print("physical phase rho² =",s.simplify(rho2.subs(q,qstar)))
print("Gram witness =",s.simplify(overlap.subs(q,qstar)),float(overlap.subs(q,qstar)))
print("invalid rho=q shortcut =",s.Rational(4,9))
print("spherical mean sin² theta =",s.Rational(2,3))
for a,b in [(3,1),(4,1),(3,s.Rational(6,5))]:
    print("bath drift a,b:",a,b,"equilibrium q²:",s.Rational(b,a),"e²:",1-s.Rational(b,a))
