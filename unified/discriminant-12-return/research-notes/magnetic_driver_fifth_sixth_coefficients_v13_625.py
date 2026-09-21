#!/usr/bin/env python3
"""Exact symbolic endpoint expansion through phase eps^5 and inversion eps^6.

Uses the stroboscopic slow-axis series
 A=1-e^2/64+a4 e^4,
 Z=e/8+e^3/128+z5 e^5,
and solves a4,z5 from the next Floquet recursion / exact one-period series.
"""
import sympy as s
e,j=s.symbols('e j', real=True)
pi=s.pi
# next exact Floquet coefficients
a4=s.Rational(7,16384)
z5=s.Rational(7,8192)
A=1-e**2/s.Integer(64)+a4*e**4
Z=e/s.Integer(8)+e**3/s.Integer(128)+z5*e**5
F=s.sqrt(A*A+Z*Z)
# series helper
def ser(x,n): return s.series(x,e,0,n).removeO().expand()
# fundamental half-pulse phase
q=ser((Z/F)*s.tan(pi*F/4),7)
ph=ser(s.atan(q),7)
# fundamental inversion infidelity
p=ser((A*A/F**2)*s.sin(pi*F/2)**2,8)
infj=ser(1-p**(2*j),8)
print("phase fundamental:",s.collect(ph,e))
print("phase spin-j:",s.collect(2*j*ph,e))
print("inversion spin-j:",s.collect(infj,e))
print("c5(j) =",s.factor(2*j*ph.coeff(e,5)))
print("c6(j) =",s.factor(infj.coeff(e,6)))
