#!/usr/bin/env python3
"""Exact local fiber-charge and bundle-overlap diagnostic for Taub–NUT v15.647.
This symbolic algebra does not assert a physical global raising operator exists.
"""
import sympy as s
psi,phi=s.symbols('psi phi',real=True)
k=s.symbols('k',integer=True)
f=s.Function('f')(psi)
P=lambda h:-s.I*s.diff(h,psi)
W=s.exp(s.I*psi)
assert s.simplify(P(W*f)-W*P(f)-W*f)==0
a=s.Function('a')(phi)
F=s.Function('F')(psi,phi)
Dphi=lambda h:s.diff(h,phi)-a*s.diff(h,psi)
assert s.simplify(P(Dphi(F))-Dphi(P(F)))==0
assert s.simplify(s.exp(s.I*(k+1)*phi)/s.exp(s.I*k*phi)-s.exp(s.I*phi))==0
L,c,hbar=s.symbols('L c hbar',positive=True)
E=lambda q:hbar*c*q/(4*L)
assert s.simplify(E(k+1)-E(k)-hbar*c/(4*L))==0
print('PASS: invariant derivative, local raise, bundle winding, fixed-l energy shift')
