#!/usr/bin/env python3
"""Exact fifth-order phase and sixth-order inversion coefficients."""
import sympy as s
e,j=s.symbols('e j', real=True); pi=s.pi
# Exact coefficients from magnetic_driver_exact_dyson_log_v13_626.py
a4=-s.Rational(3,2048); z5=s.Rational(61,196608)
A=1-e**2/s.Integer(64)+a4*e**4
Z=e/s.Integer(8)+e**3/s.Integer(128)+z5*e**5
F=s.sqrt(A*A+Z*Z)
ph=s.series(s.atan((Z/F)*s.tan(pi*F/4)),e,0,7).removeO().expand()
p=s.series((A*A/F**2)*s.sin(pi*F/2)**2,e,0,8).removeO().expand()
x=s.series(1-p,e,0,8).removeO().expand()
inf=s.series(2*j*x-s.binomial(2*j,2)*x**2+s.binomial(2*j,3)*x**3,e,0,8).removeO().expand()
print("c5 =",s.factor(2*j*ph.coeff(e,5)))
print("c6 =",s.factor(s.expand_func(inf.coeff(e,6))))
