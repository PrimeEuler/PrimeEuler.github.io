#!/usr/bin/env python3
"""Gravity v15.900: two Cone circles as conditional radial turning points of a
constant-inward-force, fixed-angular-momentum Newtonian rotor.
No Cone field force or physical radius mapping is assumed to be derived.
"""
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

n, l, u, M, L, r=sp.symbols("n ell u M L r",positive=True)
ri=l*u*sp.sqrt(n)
ro=l*u*(n+1)/2
G=sp.factor(ro/ri)
F0=sp.factor((L**2/(2*M))*(1/ri**2-1/ro**2)/(ro-ri))
expected=sp.factor(L**2*(ro+ri)/(2*M*ri**2*ro**2))
assert sp.simplify(F0-expected)==0
U=L**2/(2*M*r*r)+F0*r
assert sp.simplify(U.subs(r,ri)-U.subs(r,ro))==0
ai=sp.factor((L**2/(M*r**3)-F0).subs(r,ri)/M)
ao=sp.factor((L**2/(M*r**3)-F0).subs(r,ro)/M)
assert sp.simplify(ai-L**2*(G-1)*(2*G+1)/(2*M**2*G**2*ri**3))==0
assert sp.simplify(ao+L**2*(G-1)*(G+2)/(2*M**2*G**3*ri**3))==0
equil=sp.real_root(L**2/(M*F0),3)
assert sp.simplify(sp.diff(U,r,2)-3*L**2/(M*r**4))==0
p,C=sp.symbols("p C", positive=True)
V=C*r**p/p
Us=L**2/(2*M*r**2)+V
rs=sp.symbols("rs",positive=True)
curv=sp.diff(Us,r,2).subs(C,L**2/(M*rs**(p+2))).subs(r,rs)
assert sp.simplify((curv/M)/(L**2/(M**2*rs**4))-(p+2))==0
print("PASS turning-point force, inward/outward accelerations and power-law frequency ratio sqrt(p+2)")

# n=4, ell*u=1, M=L=1, r_i=1, r_o=5/4.
R_i,R_o,Mass,AngMom=1.,1.25,1.,1.
force=AngMom**2*(R_o+R_i)/(2*Mass*R_i**2*R_o**2)
def ode(t,y):
    rr,rd,theta=y
    return [rd, AngMom**2/(Mass**2*rr**3)-force/Mass,AngMom/(Mass*rr**2)]
def inner_turn(t,y): return y[1]
inner_turn.terminal=True
inner_turn.direction=1
res=solve_ivp(ode,(0,20),(R_o,0.,0.),events=inner_turn,rtol=1e-11,atol=1e-12,max_step=.005)
assert res.status==1 and abs(res.y[0,-1]-R_i)<1e-10
energy=.5*Mass*res.y[1]**2+AngMom**2/(2*Mass*res.y[0]**2)+force*res.y[0]
assert np.max(np.abs(energy-energy[0]))<1e-11
print("n=4 F0=",force,"half radial period=",res.t[-1],"inner turning radius=",res.y[0,-1],
      "angular sweep outer->inner=",res.y[2,-1],"max energy drift=",np.max(np.abs(energy-energy[0])))
print("PASS energy and two radial turning points; angular orbit generally precesses")
