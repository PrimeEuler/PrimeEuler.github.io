#!/usr/bin/env python3
"""v15.1403 observed Dirac rapidity lifts onto nested observability sheets.
45.31 is 1/2 log observed EM/G force ratio, NOT acceleration in g.
The representation-space boost preserves Q and gives no G derivation.
"""
import mpmath as mp
import sympy as s
mp.mp.dps=70
D=mp.mpf('2.26866143917643529e39')
psi=mp.log(D)/2
assert abs(psi-mp.mpf('45.310004304981584842871084331617193'))<mp.mpf('1e-31')
for name,r in [('quarter',mp.mpf('0.25')),('EM',mp.mpf('0.5'))]:
 U=r*mp.exp(psi);V=r*mp.exp(-psi)
 T=r*mp.cosh(psi);X=r*mp.sinh(psi)
 assert mp.almosteq(U*V,r*r,rel_eps=mp.mpf('1e-60'))
 assert mp.almosteq(T+X,U,rel_eps=mp.mpf('1e-48'))
 assert mp.almosteq(T-X,V,rel_eps=mp.mpf('1e-48'))
 print(name,'Q',r*r,'T',mp.nstr(T,24),'X',mp.nstr(X,24),'U',mp.nstr(U,24),'V',mp.nstr(V,24))
print('boost',mp.nstr(psi,29),'1-beta',mp.nstr(1-mp.tanh(psi),26),'Dirac input',mp.nstr(D,25))
U,V,Y,eta=s.symbols('U V Y eta',real=True)
Q=U*V-Y**2
assert s.simplify(Q.subs({U:U*s.exp(eta),V:V*s.exp(-eta)},simultaneous=True)-Q)==0
r,chi,theta,C,H=s.symbols('r chi theta C H',positive=True)
coordinates=s.Matrix([r*s.cosh(chi),r*s.sinh(chi)*s.cos(theta),r*s.sinh(chi)*s.sin(theta)])
jac=s.simplify(coordinates.jacobian([r,chi,theta]).det())
assert s.simplify(jac-r**2*s.sinh(chi))==0
Jr=C/r**2
assert s.simplify(s.diff(jac*Jr,r)/jac)==0
flux=s.simplify(s.integrate(jac*Jr,(theta,0,2*s.pi),(chi,0,H)))
assert s.simplify(flux-2*s.pi*C*(s.cosh(H)-1))==0
print('radial conserved flux',flux)
print('PASS boost preserves all Q sheets, common radial flux constant')
print('NEGATIVE observed EM/G ratio inserted to define psi; flux normalization free')
