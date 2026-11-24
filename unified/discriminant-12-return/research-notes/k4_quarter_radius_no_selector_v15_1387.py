#!/usr/bin/env python3
"""Gravity v15.1387: quarter hyperboloid radius is degenerate with free
sigma and effective Weyl/Maxwell coupling normalizations, unless a
separate physical scale/coupling selector is derived."""
import sympy as s
r,rp,f,g,u,v=s.symbols("r rp f g u v",positive=True)
fp=f*r/rp
gp=g*r*r/(rp*rp)
G=lambda rr,ff:rr*rr*ff*ff
mix=lambda rr,gg:rr*rr*gg
assert s.simplify(G(r,f)-G(rp,fp))==0
assert s.simplify(mix(r,g)-mix(rp,gp))==0
q=s.Matrix([u,v]);D=1+u*u+v*v
G0=s.eye(2)-q*q.T/D
Omega=1/s.sqrt(D)
assert s.simplify(G(r,f)*G0-G(rp,fp)*G0)==s.zeros(2)
assert s.simplify(mix(r,g)*Omega-mix(rp,gp)*Omega)==0
assert s.simplify(-2/(f*r)**2+2/(fp*rp)**2)==0
print("PASS kinetic and unnormalized area interactions invariant under r->rp with f'=fr/rp, g'=g*r²/rp²")
print("PASS canonically normalized H2 curvature -2/(fr)^2 is unchanged")
print("PASS normalized area interaction has no explicit radius at all")
print("NEGATIVE radius 1/4 alone predicts no interaction size")
