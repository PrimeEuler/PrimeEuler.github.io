#!/usr/bin/env python3
"""Cone Gravity v15.898: two-circle relativistic energy-kinetic dictionary.
Normalized Cone geometry exact; physical energy map is CONDITIONAL.
"""
import sympy as s
n,u,m,c=s.symbols("n u m c",positive=True)
inner=u*s.sqrt(n)
outer=u*(n+1)/2
offset=u*(n-1)/2
gamma=s.simplify(outer/inner)
beta=s.simplify(offset/outer)
momentum=s.simplify(offset/inner)
kinetic=s.simplify(gamma-1)
assert s.simplify(gamma**2-momentum**2-1)==0
assert s.simplify(gamma**2*(1-beta**2)-1)==0
assert s.simplify(kinetic-(s.sqrt(n)-1)**2/(2*s.sqrt(n)))==0
assert s.simplify((outer**2-inner**2)/inner**2-momentum**2)==0
assert s.simplify((outer/inner)**2-gamma**2)==0
E=m*c**2*gamma
P=m*c*momentum
assert s.simplify(E**2-P**2*c**2-m**2*c**4)==0
assert s.simplify((E-m*c**2)/(m*c**2)-kinetic)==0
# A formal shell traversal clock remains free.
z=s.symbols("z",real=True)
assert s.simplify(s.cosh(z)**2-s.sinh(z)**2-1)==0
print("PASS exact normalized Lorentz energy-momentum and kinetic/rest-energy excess")
for N in (1,2,4,9,16):
    print(N, "gamma",float(gamma.subs(n,N)),"beta",float(beta.subs(n,N)),
          "K/Erest",float(kinetic.subs(n,N)))
print("No dynamics or energy normalization derived; gamma physical interpretation conditional")
