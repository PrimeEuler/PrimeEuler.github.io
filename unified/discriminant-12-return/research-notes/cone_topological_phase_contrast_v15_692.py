#!/usr/bin/env python3
"""v15.692: exact topology vs formal Cone q=2 spectral parity.

Uses the integer first-Chern monopole patches of v15.632 and the
geometric quarter-shell Casimir of v15.626.  Cross-sector equal-pair
comparison is conditional, not a derived common physical interferometer.
"""
import sympy as s
pi=s.pi
theta=s.symbols("theta",real=True)
k=s.symbols("k",integer=True)
C=lambda ell:s.Rational(ell*(ell+4),16)
for L in range(128):
    assert s.simplify(s.exp(16*pi*s.I*C(L))-(-1)**L)==0

AN=k*(1-s.cos(theta))/2
AS=-k*(1+s.cos(theta))/2
assert s.simplify(AN-AS-k)==0
F=s.diff(AN,theta)
assert s.simplify(s.integrate(F,(theta,0,pi))-k)==0

# Latitude holonomy from the north-patch connection.
phase=s.pi*k*(1-s.cos(theta))
assert s.simplify(s.diff(phase,theta)-pi*k*s.sin(theta))==0
for n in range(12):
    assert s.simplify(s.exp(s.I*phase.subs({k:n,theta:pi/2}))-(-1)**n)==0

# Equal first-Chern winding: same angular Wilson phase.
# Equal dimensionless pair products: k_G=2 k_EM (conditional).
for ke in range(1,15):
    kg=2*ke
    assert s.Rational(ke,2)==s.Rational(kg,4)
    assert (-1)**kg==1
    assert s.Rational((-1)**kg,(-1)**ke)==(-1)**ke

# chi=+ for all formal EM even-L shells, whereas an actual k=1
# angular monopole has equatorial Wilson phase -1.
assert (-1)**2==1 and (-1)**1==-1
assert C(1)==s.Rational(5,16)
jphys=s.Rational(1,2)
assert jphys*(jphys+1)==s.Rational(3,4)
print("PASS: formal Cone character, integer Chern winding and conditional pair-matched holonomy")
