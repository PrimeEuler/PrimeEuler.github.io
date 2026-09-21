#!/usr/bin/env python3
"""Symbolic reduction for the next magnetic-driver endpoint coefficients.

The fifth/sixth endpoint coefficients depend on the still-required next
stroboscopic Floquet coefficients a4,z5. This derives that dependence exactly
and deliberately does not guess a4,z5 from floating-point residuals.
"""
import sympy as s
e,j,a4,z5=s.symbols('e j a4 z5', real=True)
pi=s.pi
A=1-e**2/s.Integer(64)+a4*e**4
Z=e/s.Integer(8)+e**3/s.Integer(128)+z5*e**5
F=s.sqrt(A*A+Z*Z)
def ser(x,n): return s.series(x,e,0,n).removeO().expand()
ph=ser(s.atan(ser((Z/F)*s.tan(pi*F/4),7)),7)
p=ser((A*A/F**2)*s.sin(pi*F/2)**2,8)
infj=ser(1-p**(2*j),8)
print("c5(j;a4,z5) =",s.factor(2*j*ph.coeff(e,5)))
print("c6(j;a4,z5) =",s.factor(infj.coeff(e,6)))
print("Guardrail: derive a4,z5 from fifth-order Floquet recursion before promotion.")
