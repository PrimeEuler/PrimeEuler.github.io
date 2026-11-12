#!/usr/bin/env python3
"""v15.794: local Minkowski TT light-time benchmark, first-order null rays.
Outgoing plus returning photon path in a Fourier TT wave, h_ij =
H_ij exp[-i*omega*t+i*k dot x]. Fixed TT-coordinate freely falling mirrors
in local Minkowski; ignores cosmological expansion, arms moving under
scalar/vector K4 forces, Ricci contribution, instrument noise. This
benchmark is conventional GR and is NOT a full Cone K4 detector response.
"""
import sympy as s
x,y=s.symbols('x y',real=True)
F=lambda z:s.exp(s.I*z/2)*s.sin(z/2)/(z/2)
# x=omega*L; y=k*L*dot(n,u).
# One-way outgoing: (L/2)*Huu exp(-i omega te)*F(y-x)
# Return:           (L/2)*Huu exp(-i omega te)*exp(i(y-x))*F(-y-x)
Transfer=F(y-x)+s.exp(s.I*(y-x))*F(-y-x)
assert s.simplify(s.limit(s.limit(Transfer,x,0),y,0)-2)==0
assert s.simplify(Transfer.subs(x,0)-2*F(y))==0
assert s.simplify(Transfer.subs(y,0)-F(-x)*(1+s.exp(-s.I*x)))==0
m=s.symbols('m',integer=True,positive=True)
assert s.simplify(Transfer.subs({y:0,x:2*s.pi*m}))==0
for xx,yy in ((.1,0.),(1.,.6),(2.,1.)):
    z=complex(Transfer.subs({x:xx,y:yy}).evalf())
    assert abs(z)<2.001
    print('omegaL',xx,'mu*kL',yy,'complex transfer',z)
print('PASS: conventional TT outgoing/return null-geodesic time transfer')
print('PASS: low-frequency limit, stationary spatial-averaging limit, TT temporal null')
print('CAUTION: no K4-specific operator; cosmological detector and scalar/vector photon transfer OPEN')
