#!/usr/bin/env python3
"""Exact source equation and curvature trace decomposition of audited rotor Xi."""
import sympy as s
r,A,Lam,c,G,rho=s.symbols('r A Lambda c G rho',positive=True)
Phi=s.Function('Phi')(r)
g=s.diff(Phi,r); h=s.diff(Phi,r,2); t=g/r
xi=(1-r*h/g)/3; lap=h+2*t
assert s.simplify(xi-(1-lap/(3*t)))==0
assert s.simplify((t-h)/(3*t)-xi)==0
assert s.simplify((1-(4*s.pi*G*rho-Lam*c**2)/(3*t))-xi.subs(h,4*s.pi*G*rho-Lam*c**2-2*t))==0
sds=-A/r-Lam*c**2*r**2/6
grad=s.diff(sds,r); rad=s.diff(sds,r,2); tang=grad/r
assert s.simplify(rad+2*tang+Lam*c**2)==0
assert s.simplify(rad-tang+3*A/r**3)==0
assert s.simplify((1-r*rad/grad)/3-1/(1-Lam*c**2*r**3/(3*A)))==0
point=-A/r
assert s.simplify((1-r*s.diff(point,r,2)/s.diff(point,r))/3-1)==0
assert s.simplify(s.diff(point,r).subs(r,r/2)/s.diff(point,r)-4)==0
assert s.simplify(s.diff(point,r,2).subs(r,r/2)/s.diff(point,r,2)-8)==0
B=s.symbols('B',real=True); alt=-A/r-B/r**3
x_alt=s.factor((1-r*s.diff(alt,r,2)/s.diff(alt,r))/3)
assert s.simplify(x_alt-(A*r**2+5*B)/(A*r**2+3*B))==0
assert s.simplify(s.diff(alt,r,2)+2*s.diff(alt,r)/r+6*B/r**5)==0
print("PASS v15.673: Xi Poisson, trace/tidal anisotropy, Lambda cancellation, point-source similarity, sourced completion")
