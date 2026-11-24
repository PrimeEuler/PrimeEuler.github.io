#!/usr/bin/env python3
"""v15.1398: canonical prefactor of Weyl-F-H2 quartic vertex.
Schematic 4-mode kappa excludes actual polarization overlap P5."""
import sympy as s
r,R,f,g,M,L,z,V=s.symbols("r R f g M Lambda zeta V",positive=True)
wA,wG,wU,wW=s.symbols("wA wG wU wV",positive=True)
F=f*r;area_g=g*r*r
vertex=s.simplify(s.sqrt(2)*area_g/(M*F*F))
assert s.simplify(vertex-s.sqrt(2)*g/(M*f*f))==0
radius_change=s.simplify(s.sqrt(2)*(g*r*r/R**2)*R**2/(M*(f*r/R*R)**2))
assert s.simplify(radius_change-vertex)==0
normalized=s.simplify(vertex.subs(g,z/L**2))
P5=s.symbols("P5",real=True)
kappa=s.simplify(normalized*P5/(4*V*s.sqrt(wA*wG*wU*wW)))
assert not kappa.has(r)
assert s.simplify(kappa.subs(z,0))==0
print("PASS canonically normalized vertex:",normalized)
print("PASS schematic finite-volume four-mode coupling:",kappa)
print("NEGATIVE free zeta/Lambda², f, M, and mode overlap remain, no quarter selector")
print("OPEN actual tensor overlap, full interacting Einstein-sigma-Maxwell dynamics")
