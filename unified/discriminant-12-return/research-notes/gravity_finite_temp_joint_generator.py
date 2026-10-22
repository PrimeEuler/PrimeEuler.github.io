#!/usr/bin/env python3
"""Finite-temperature Maxwellian bath joint generator: symbolic local coefficients.
No collision numerical fitting; uses EFT v3.4 half-covariance convention."""
import sympy as s
h,L,mu,r,v,A,P,Q=s.symbols('h L mu r v A P Q',positive=True)
T=-mu/(2*h)
z=1+2*h*L**2/mu**2
bh=-v*A+P+2*Q
bL=-A*L/v+Q*r**2/L
chh=2*P*v**2
chL=2*P*L
cLL=2*(Q*r**2+(P-Q)*L**2/v**2)
vars=s.Matrix([h,L])
b=s.Matrix([bh,bL]); cov=s.Matrix([[chh,chL],[chL,cLL]])
def drift(f):
 g=s.Matrix([s.diff(f,h),s.diff(f,L)])
 H=s.hessian(f,vars)
 return s.factor((g.dot(b)+s.trace(cov*H)/2))
def covar(f,g):
 return s.factor((s.Matrix([s.diff(f,h),s.diff(f,L)]).T*cov*s.Matrix([s.diff(g,h),s.diff(g,L)]))[0])
for k,x in [('bT',drift(T)),('bz',drift(z)),('aTT',covar(T,T)),('aTz',covar(T,z)),('azz',covar(z,z))]:
 print(k,'=',s.factor(x))
print('aTz simplified=',s.factor(covar(T,z)))
