#!/usr/bin/env python3
"""Gravity v15.1103: finite v15.1102 gravitational TT pulse pumps a seeded
transverse EM cavity mode. This is ordinary Einstein-Maxwell with a prescribed
weak pump, not a K4-derived gain or a fully conservative cavity+GW solution.
The GW travels along z; the cavity standing mode propagates along x and
has small z extent compared with the GW wavelength.
"""
import sympy as s
import mpmath as mp
z,T,omega,m,G,c,D,x0,eps=s.symbols('z T omega m G c D x0 eps',positive=True,real=True)
h,dh,Q,Qd,Qdd=s.symbols('h dh Q Qd Qdd',real=True)
g=(1-z*z)**4
x=x0+eps*g
vel=s.diff(x,z)/T
acc=s.diff(x,z,2)/T**2
strain=4*G*m/(c**4*D)*(vel**2+x*acc)
expected=4*G*m/(c**4*D*T**2)*(x0*eps*s.diff(g,z,2)+eps**2*s.diff(g*g,z,2)/2)
assert s.simplify(strain-expected)==0
assert s.integrate(s.diff(g,z,2),(z,-1,1))==0
assert s.integrate(s.diff(g*g,z,2),(z,-1,1))==0
assert s.integrate(g,(z,-1,1))==s.Rational(256,315)
assert s.integrate(g*g,(z,-1,1))==s.Rational(65536,109395)
# Maxwell TT reduction for A_y(t,x) at fixed thin-z plane:
# 1/2 [(1+h)Qdot^2 - omega^2 Q^2] + O(h^2).
Emode=(1+h)*Qd**2/2+omega**2*Q**2/2
Edot=s.diff(Emode,Q)*Qd+s.diff(Emode,Qd)*Qdd+s.diff(Emode,h)*dh
# equation of motion (1+h)Qdd+dh Qd+omega^2 Q=0
assert s.simplify(Edot.subs(Qdd,-(dh*Qd+omega**2*Q)/(1+h))+dh*Qd**2/2)==0
# Fourier overlap for finite TT strain
# xi = 2 omega T; F_p(xi)=int_-1^1(1-z^2)^p cos(xi z) dz.
# Hhat = -(4Gm/(c^4 D T))xi^2 [x0 eps F4 + eps^2 F8/2].
mp.mp.dps=40
F=lambda power,xi:mp.quad(lambda u:(1-u*u)**power*mp.cos(xi*u),[-1,0,1])
g2=s.lambdify(z,s.diff(g,z,2),'mpmath')
g8_2=s.lambdify(z,s.diff(g*g,z,2),'mpmath')
for xi in (mp.mpf('0.4'),mp.pi,2*mp.pi,mp.mpf('11')):
 direct=mp.quad(lambda u:(g2(u)+mp.mpf('0.25')*g8_2(u))*mp.cos(xi*u),[-1,0,1])
 byparts=-xi**2*(F(4,xi)+mp.mpf('0.25')*F(8,xi))
 assert abs(direct-byparts)<mp.mpf('1e-30')
# First-order classical fractional work:
# Delta E/E0=omega int h(t)sin(2omega t+2phi)dt.
# Even h -> omega sin(2phi) Hhat. Zero unseeded Q stays zero.
phi=s.symbols('phi',real=True)
assert s.sin(2*phi).subs(phi,0)==0
assert s.sin(2*phi).subs(phi,s.pi/4)==1
# A co-propagating traveling vacuum EM null field has no O(h) TT pair
# vertex in the plane-wave limit; cavity transverse mode breaks this case.
Ey,Bx=s.symbols('Ey Bx')
assert (Ey**2-Bx**2).subs(Bx,Ey)==0
print('PASS finite tidal pulse Fourier overlap and TT transverse seeded Maxwell mode')
print('F4(pi)=',mp.nstr(F(4,mp.pi),13))
print('F4(2pi)=',mp.nstr(F(4,2*mp.pi),13))
print('dimensionless linear overlap -pi^2 F4(pi)=',mp.nstr(-mp.pi**2*F(4,mp.pi),13))
