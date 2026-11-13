#!/usr/bin/env python3
"""v15.841: ordinary Poisson-constraint comparator, not full K4 ADM.

A spherical, compact, positive-energy physical canonical scalar Cauchy
datum has a nonzero *pre-existing* exterior Newtonian tidal field.
The Poisson normalization lambda is symbolic; measured G is not inserted.
This is an exact comparator/negative control, not a K4 gravity solution.
"""
import sympy as s
r,R,d,lam=s.symbols('r R d lambda',positive=True,real=True)
chi=(1-(r/R)**2)**8
dchi=s.diff(chi,r)
rho=s.factor((chi**2+3*dchi**2)/2)
M=s.factor(4*s.pi*s.integrate(rho*r*r,(r,0,R)))
Mbeta=s.pi*R**3*(s.beta(s.Rational(3,2),17)+768*s.beta(s.Rational(5,2),15)/R**2)
assert s.simplify(s.expand_func(M-Mbeta))==0
# In the infinite-space standard elliptic constraint comparator,
# Laplacian(Phi)=lambda*rho and Phi -> 0 at infinity.
A=lam*M/(4*s.pi)
phi=-A/d
radial=s.diff(phi,d,2)
transverse=s.diff(phi,d)/d
assert s.simplify(radial+2*transverse)==0
assert s.simplify(radial+2*A/d**3)==0
assert s.simplify(transverse-A/d**3)==0
T=s.diag(transverse,transverse,radial)
assert s.simplify(s.trace(T*T)-6*(A/d**3)**2)==0
assert s.simplify(radial/transverse+2)==0
R0=s.Rational(5,2);d0=s.Integer(6)
print('PASS analytic positive canonical compact mass, arbitrary normalization')
print('total mass',s.N(M.subs(R,R0),16))
print('lambda^-1 exterior potential',s.N((phi/lam).subs({R:R0,d:d0}),16))
print('lambda^-1 transverse tidal',s.N((transverse/lam).subs({R:R0,d:d0}),16))
print('lambda^-1 radial tidal',s.N((radial/lam).subs({R:R0,d:d0}),16))
print('PASS exterior tidal eigenvalue ratio -2; NOT a K4 retarded signal')
