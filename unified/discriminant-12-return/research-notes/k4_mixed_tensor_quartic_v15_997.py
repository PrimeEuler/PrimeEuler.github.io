#!/usr/bin/env python3
"""v15.997: frozen K4 solid mixed plus/cross tensor quartic source.
Two transverse TT polarizations in the unimodular one-dimensional ansatz;
NOT the full gauge/constraint-reduced nonlinear K4 action.
"""
import sympy as s
b,c,db,dc,t=s.symbols('b c db dc t',real=True)
S=s.Matrix([[b,c],[c,-b]])
V=s.Matrix([[db,dc],[dc,-db]])
A1=2*V
A2=2*(V*S-S*V)
assert s.expand(s.trace(A1*A2+A2*A1))==0
assert s.simplify(S*S-(b*b+c*c)*s.eye(2))==s.zeros(2)
r=s.symbols('r',real=True)
J=(2*s.cosh(4*r)+1)/(2*s.cosh(2*r)+1)**2-s.Rational(1,3)
ser=s.series(J,r,0,7).removeO().expand()
assert s.simplify(ser-(s.Rational(8,9)*r*r-s.Rational(8,9)*r**4+s.Rational(112,135)*r**6))==0
J4=s.expand(s.Rational(8,9)*(b*b+c*c)-s.Rational(8,9)*(b*b+c*c)**2)
assert J4.coeff(b,2).coeff(c,2)==-s.Rational(16,9)
z=s.symbols('z',real=True)
e0=1/s.sqrt(s.pi);e4=s.sqrt(2/s.pi)*s.cos(4*z)
I04=s.integrate(e0*e4*s.cos(2*z)**2,(z,0,s.pi))
assert s.simplify(I04-s.sqrt(2)/4)==0
# In the frozen local solid constitutive term L_solid=-C eta J,
# background b=B cos(2z) and cross fluctuation c=c0 e0+c4 e4,
# the b²c² correction is +16/9 C eta B² cos²(2z) c².
# Its c0 c4 LAGRANGIAN coefficient is twice the overlap.
C,eta,B=s.symbols('C eta B',real=True)
mixed=s.simplify(2*s.Rational(16,9)*C*eta*B**2*I04)
assert s.simplify(mixed-8*s.sqrt(2)*C*eta*B**2/9)==0
print('PASS: one-dimensional mixed-plus/cross cubic kinetic trace zero')
print('K4 solid J expansion=',ser)
print('Cross-pol spatial k0-k4 overlap=',I04)
print('Selected solid Lagrangian cross coefficient=',mixed)
