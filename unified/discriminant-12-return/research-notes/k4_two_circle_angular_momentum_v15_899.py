#!/usr/bin/env python3
"""Cone gravity v15.899: test thin-ring angular-momentum contraction on two geometric radii.
No implied physical radius or spontaneous torque/force selector.
"""
import sympy as s
n,ell,m,L,t=s.symbols("n ell m L t", positive=True)
ro=ell*(n+1)/2
ri=ell*s.sqrt(n)
gamma=s.simplify(ro/ri)
Io=m*ro**2
Ii=m*ri**2
wo=L/Io
wi=L/Ii
Ko=L**2/(2*Io)
Ki=L**2/(2*Ii)
assert s.simplify(wi/wo-gamma**2)==0
assert s.simplify(Ki/Ko-gamma**2)==0
assert s.simplify((Ki-Ko)/Ko-(n-1)**2/(4*n))==0
assert s.simplify((ri*wi)/(ro*wo)-gamma)==0
assert s.simplify((ri*wi**2)/(ro*wo**2)-gamma**3)==0
r=s.Function("r")(t)
w=L/(m*r**2)
assert s.simplify(s.diff(w,t)+2*w*s.diff(r,t)/r)==0
# Energy balance under radial constraint / contraction:
Kr=L**2/(2*m*r**2)
assert s.simplify(s.diff(Kr,t)+L**2*s.diff(r,t)/(m*r**3))==0
print("PASS: angular-velocity ratio=gamma^2; kinetic-energy ratio=gamma^2; tangential speed ratio=gamma")
print("PASS: spin-up omega_dot=-2 omega r_dot/r; extra work required for inward contraction")
for N in (1,2,4,9,16):
    print("n",N,"gamma",float(gamma.subs(n,N)),"rotational KE ratio",float((gamma**2).subs(n,N)))
