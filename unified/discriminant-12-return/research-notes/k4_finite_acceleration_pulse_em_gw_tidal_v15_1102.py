#!/usr/bin/env python3
"""Gravity v15.1102: finite opposite-charge/internal-force dipole pulse.

Nonrelativistic, long-wavelength, far-zone leading EM electric dipole and
Einstein TT mass quadrupole comparator. Matter stress includes a toy strut
for momentum balance. This is not a fully sourced Einstein-K4/Maxwell
radiation-reaction solution; G is imported to display standard comparator.
"""
import sympy as s
z,T,x0,eps,m,q,G,c,D,eps0=s.symbols('z T x0 eps m q G c D eps0',positive=True,real=True)
g=(1-z*z)**4
x=x0+eps*g
v=s.diff(x,z)/T
acc=s.diff(x,z,2)/T**2
# Two masses at +/- x and charges +/- q; forces +/-m*a supplied by an
# internal strut. Full kinetic+strut xx integrated stress equals 1/2 Ixx''.
Ixx=2*m*x**2
stress_particles=2*m*v**2
stress_strut=2*x*m*acc
assert s.simplify(stress_particles+stress_strut-s.diff(Ixx,z,2)/(2*T*T))==0
# Electric dipole p_x=2q*x, mass tracefree quadrupole Qxx-Qyy=2m*x^2.
p=2*q*x
Qdiff=2*m*x*x
pdd=s.diff(p,z,2)/T**2
Qdd=s.diff(Qdiff,z,2)/T**2
assert s.simplify(pdd-2*q*acc)==0
assert s.simplify(Qdd-4*m*(v*v+x*acc))==0
# Observer on z axis: E_rad along x, h_plus = h_xx^TT = -h_yy^TT.
Efar=pdd/(4*s.pi*eps0*c*c*D)
hplus=G*Qdd/(c**4*D)
tidal_acc=s.diff(hplus,z,2)/(2*T**2)
assert s.simplify(hplus-4*G*m*(v*v+x*acc)/(c**4*D))==0
for n in (0,1,2,3):
 assert s.diff(g,z,n).subs(z,1)==0
 assert s.diff(g,z,n).subs(z,-1)==0
assert s.simplify(v.subs(z,0))==0
assert s.simplify(acc.subs(z,0)+8*eps/T**2)==0
assert s.simplify(pdd.subs(z,0)+16*q*eps/T**2)==0
assert s.simplify(hplus.subs(z,0)+32*G*m*eps*(x0+eps)/(c**4*D*T**2))==0
assert s.simplify(Efar.subs(z,0)+4*q*eps/(s.pi*eps0*c*c*D*T**2))==0
Iacc=s.integrate(s.diff(g,z,2)**2,(z,-1,1))
assert s.simplify(Iacc)>0
assert s.integrate(s.diff(g,z,2),(z,-1,1))==0
# Standard electric-dipole Larmor radiated energy, not included in
# the reduced instantaneous actuator energy budget.
Uem=s.simplify(s.integrate((pdd**2/(6*s.pi*eps0*c**3))*T,(z,-1,1)))
assert s.simplify(Uem-(4*q*q*eps*eps/(6*s.pi*eps0*c**3*T**3))*Iacc)==0
assert s.simplify(Qdd.subs(x0,0).subs(eps,-eps)-Qdd.subs(x0,0))==0
assert s.simplify(pdd.subs(eps,-eps)+pdd)==0
assert s.simplify(s.diff(hplus,eps).subs({eps:0,x0:0}))==0
print('PASS finite C3 pulse, Newtonian strut momentum stress, EM dipole and GR TT quadrupole')
print('pulse acceleration integral=',Iacc)
print('EM radiated energy=',Uem)
print('Efar(center)=',s.factor(Efar.subs(z,0)))
print('hplus(center)=',s.factor(hplus.subs(z,0)))
print('tidal(center)=',s.factor(tidal_acc.subs(z,0)))
