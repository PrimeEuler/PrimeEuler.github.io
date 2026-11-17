#!/usr/bin/env python3
"""Gravity v15.1110: compact solenoidal Maxwell curl whose level sets are
the XY-projected ellipse of Cone PaperA, including the focal rest offset.

Wave axis x, ellipse axes y,z. A_x=psi0 f(x) (1-q)^4 for q<1,
q=((y-d)/A)^2+(z/B)^2; A=C/(1-e²), B=C/sqrt(1-e²),
d=-Ce/(1-e²). The compact axial f has unit L2 norm.
All calculations conventional Maxwell field/stress with prescribed currents.
"""
import sympy as s
e,C,p0,mu0,L=s.symbols("e C psi0 mu0 L",positive=True,real=True)
D=1-e**2
A=C/D; B=C/s.sqrt(D); d=-C*e/D
assert s.simplify(A**2-B**2-d**2)==0
r,p=s.symbols("r p",positive=True,real=True)
fp=-4*(1-r**2)**3
# B=curl(Psi xhat); y=d+A*r*cos(p), z=B*r*sin(p).
By=p0*fp*2*r*s.sin(p)/B
Bz=-p0*fp*2*r*s.cos(p)/A
rad=s.integrate(r**3*fp**2,(r,0,1))
assert rad==s.Rational(1,7)
# The compact x profile is normalized so that int f(x)^2 dx=1.
# Angular integrals of cos² and sin² are pi.
plus=s.simplify(4*s.pi*p0**2*A*B*(1/A**2-1/B**2)*rad/mu0)
total=s.simplify(4*s.pi*p0**2*A*B*(1/A**2+1/B**2)*rad/mu0)
assert s.simplify(plus+4*s.pi*p0**2*e**2/(7*mu0*s.sqrt(D)))==0
assert s.simplify(total-4*s.pi*p0**2*(2-e**2)/(7*mu0*s.sqrt(D)))==0
assert s.simplify(plus/(total/2)+2*e**2/(2-e**2))==0
v=s.symbols("v",real=True)
F8=s.integrate((1-v**2)**8,(v,-1,1))
assert F8==s.Rational(65536,109395)
# For a time-dependent shape, A=(Psi(x,y,z,t),0,0),
# E=-d_t A, B=curl A, rho=div E,
# J=curl B-d_t E in mu0=epsilon0=c_light=1.
x,y,z,t=s.symbols("x y z t",real=True)
psi=s.Function("Psi")(x,y,z,t)
Bx=s.S.Zero; Byg=s.diff(psi,z); Bzg=-s.diff(psi,y)
Ex=-s.diff(psi,t)
rho=-s.diff(psi,x,t)
Jx=-s.diff(psi,y,2)-s.diff(psi,z,2)+s.diff(psi,t,2)
Jy=s.diff(psi,x,y); Jz=s.diff(psi,x,z)
assert s.simplify(s.diff(Byg,y)+s.diff(Bzg,z))==0
assert s.simplify(s.diff(Ex,x)-rho)==0
assert s.simplify(s.diff(rho,t)+s.diff(Jx,x)+s.diff(Jy,y)+s.diff(Jz,z))==0
assert s.simplify(s.diff(Byg,t)+s.diff(Ex,z))==0
assert s.simplify(s.diff(Bzg,t)-s.diff(Ex,y))==0
# The cone's dimensionless rest offset d/C=-e/(1-e²)
# changes with sign(e), while the integrated TT stress is even.
assert s.simplify(plus.subs(e,s.Rational(1,2))/(total.subs(e,s.Rational(1,2))/2)+s.Rational(2,7))==0
assert s.simplify(plus.subs(e,s.Rational(1,4))/(total.subs(e,s.Rational(1,4))/2)+s.Rational(2,31))==0
print("PASS compact cone-ellipse Maxwell curl, current continuity, stress and energy")
print("U_B=",s.simplify(total/2))
print("TT stress=",plus)
print("TT stress/U_B=",s.simplify(plus/(total/2)))
