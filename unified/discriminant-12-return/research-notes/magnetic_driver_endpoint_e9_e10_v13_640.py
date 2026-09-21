#!/usr/bin/env python3
"""Analytic endpoint reduction using exact v13.639 a8,z9 coefficients."""
import sympy as s
e,j=s.symbols('e j'); pi=s.pi
A=1-e**2/s.Integer(64)-3*e**4/s.Integer(2048)-341*e**6/s.Integer(3145728)-21745*e**8/s.Integer(3623878656)
Z=e/s.Integer(8)+e**3/s.Integer(128)+61*e**5/s.Integer(196608)+937*e**7/s.Integer(452984832)-5033593*e**9/s.Integer(5218385264640)
# Exact endpoint maps; staged series evaluation is recommended to avoid expression swell.
F=s.sqrt(A*A+Z*Z)
phase=s.atan((Z/F)*s.tan(pi*F/4))
p12=(A*A/F**2)*s.sin(pi*F/2)**2
print("c_phi_9 =",s.factor(2*j*s.diff(phase,e,9).subs(e,0)/s.factorial(9)))
# fixed-j symmetric-power inversion
Pinv=1-p12**(2*j)
print("c_P_10 =",s.factor(s.diff(Pinv,e,10).subs(e,0)/s.factorial(10)))
