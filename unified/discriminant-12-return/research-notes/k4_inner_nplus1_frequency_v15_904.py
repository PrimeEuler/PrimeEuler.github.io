#!/usr/bin/env python3
"""Gravity v15.904: inner sqrt(n) temporal frequency hypothesis omega_i=(n+1)omega_*.
Separate angular frequency in time from angular winding around circumference.
"""
import sympy as s
n,u,ell,M,L,omega=s.symbols("n u ell M L omega",positive=True)
ri=ell*u*s.sqrt(n)
ro=ell*u*(n+1)/2
gamma=s.factor(ro/ri)
wi=(n+1)*omega
wo=s.factor(wi/gamma**2)
Lreq=s.factor(M*ri**2*wi)
assert s.simplify(wo-4*n*omega/(n+1))==0
assert s.simplify(Lreq-M*ell**2*u**2*n*(n+1)*omega)==0
assert s.simplify((L/(M*ri**2))/omega-L/(M*ell**2*u**2*n*omega))==0
thalf=s.pi/wi
arc=s.pi*u*s.sqrt(n)
assert s.simplify(arc/thalf-u*s.sqrt(n)*(n+1)*omega)==0
assert s.simplify(s.pi*u*s.sqrt(n)/(n+1)-arc/(n+1))==0
vt=ri*wi
assert s.simplify(vt-ell*u*omega*(n+1)*s.sqrt(n))==0
print("PASS temporal frequency / spatial winding distinction and angular-momentum compatibility")
for N in (1,2,4,9,16):
    print(N, "inner omega/omega_*",N+1,"outer omega/omega_*",
          float(wo.subs({n:N,omega:1})), "inner half-time*omega_*",
          float(thalf.subs({n:N,omega:1})))
