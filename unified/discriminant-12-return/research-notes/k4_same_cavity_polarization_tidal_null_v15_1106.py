#!/usr/bin/env python3
"""Gravity v15.1106: same ideal slab cavity, equal-phase dual polarization
normalization of finite tidal-pulse work. Standard Einstein-Maxwell null,
not a new Cone tidal observable. A_y and A_z are transverse to x cavity
mode with plus TT GW propagating in z; walls and dispersion assumed ideal.
"""
import sympy as s
w,A,phi,Hcos=s.symbols('w A phi Hcos',positive=True,real=True)
delta_y=w*s.sin(2*phi)*Hcos
delta_z=-w*s.sin(2*phi)*Hcos
assert s.simplify(delta_y+delta_z)==0
assert s.simplify(delta_y-delta_z-2*w*s.sin(2*phi)*Hcos)==0
assert s.simplify(delta_y/delta_z+1)==0
# The common pulse can be the finite symmetric two-mass source of v15.1102.
t,T,m,G,c,D,x0,eps=s.symbols('t T m G c D x0 eps',positive=True,real=True)
u=t/T
g=(1-u*u)**4
x=x0+eps*g
h=2*G*m/(c**4*D)*s.diff(x*x,t,2)
assert s.simplify(h-4*G*m/(c**4*D)*(s.diff(x,t)**2+x*s.diff(x,t,2)))==0
assert delta_y.subs(phi,0)==0
assert s.simplify(delta_y.subs(phi,s.pi/4)-w*Hcos)==0
# If the seeds are differently phased, cancellation generally fails.
phiy,phiz=s.symbols('phiy phiz',real=True)
dy=w*s.sin(2*phiy)*Hcos
dz=-w*s.sin(2*phiz)*Hcos
assert s.simplify((dy+dz).subs(phiz,phiy))==0
assert s.simplify(dy+dz)!=0
print('PASS: same-cavity equal-seed polarization sum null and differential tidal transfer')
print('normalized dy=',delta_y,'normalized dz=',delta_z)
