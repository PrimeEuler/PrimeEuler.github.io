#!/usr/bin/env python3
"""Gravity v15.1196 validated general isotropic-curvature profile correction.

Maxwell source v15.1085 and standard-GR initial longitudinal constraints
v15.1159 only fix STF scalar S(q) proportional to source R(q) for q!=0.
The isotropic full electric Riemann A(z) is not thereby proved to share
the packet envelope g(z/c). Finite-arm response must retain Abar-A(0).
"""
import sympy as s
u,r=s.symbols('u r',nonnegative=True)
g=(1-u**2)**6
G=s.integrate(g,(u,0,r))/r
S0,Acenter,Abar=s.symbols('S0 Acenter Abar')
Ezbar=Abar+s.Rational(2,3)*S0*G
Ex=Acenter-s.Rational(1,3)*S0
D=s.factor(Ezbar-Ex)
assert s.simplify(D-(2*G+1)*S0/3-(Abar-Acenter))==0
assert s.limit((2*G+1)/3,r,0)==1
assert s.simplify(D.subs(Abar,Acenter*G)-
   ((2*G+1)*S0/3+(G-1)*Acenter))==0
assert s.simplify(G.subs(r,1)-s.Rational(1024,3003))==0
assert s.simplify(((2*G+1)/3).subs(r,1)-s.Rational(5051,9009))==0
print('PASS unrestricted isotropic profile: differential proxy=',D)
print('PASS conditional matched isotropic envelope recovers original exploratory formula')
print('IMPORTANT actual Abar must be determined from full physical constraints/dynamics')
