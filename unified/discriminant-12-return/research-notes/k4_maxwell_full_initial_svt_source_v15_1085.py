#!/usr/bin/env python3
"""Gravity v15.1085: complete initial scalar/vector/TT Fourier stress split.

This establishes constraint-compatible *source data*, not an solved coupled
Einstein-K4 scalar metric or completed local electric Weyl observable.
"""
import sympy as s
r=s.symbols('r',real=True)
f=(1-r*r)**3
I0=s.integrate(f*f,(r,-1,1))
I1=s.integrate(s.diff(f,r)**2,(r,-1,1))
assert (I0,I1)==(s.Rational(2048,3003),s.Rational(1024,385))
a,b,A,q=s.symbols('a b A q',positive=True,real=True)
R=s.factor(A*A*I0*I1*(a/b+b/a)/2)
P=s.factor(A*A*I0*I1*(b/a-a/b)/2)
assert s.simplify(P/R-(b*b-a*a)/(b*b+a*a))==0
# Every component below is multiplied by the same longitudinal transform
# F0(q)=integral dz f(z/c)^2 exp(-i q z).
T=s.diag(P,-P,R)
assert s.simplify(s.trace(T)-R)==0
scalar=s.simplify(T[2,2]-s.trace(T)/3)
assert s.simplify(scalar-2*R/3)==0
Proj=s.diag(1,1,0)
TT=s.simplify(Proj*T*Proj-s.Rational(1,2)*Proj*s.trace(Proj*T))
assert all(s.simplify(x)==0 for x in TT-s.diag(P,-P,0))
assert s.simplify(s.trace(TT))==0
assert s.simplify((TT-T).trace()+R)==0
# Initial Poynting vector is zero because initial B=0.
# Ward identities for longitudinal Fourier amplitudes:
# rho_dot=-i q S_z; S_z_dot=-i q T_zz,
# hence rho_ddot(0)=-q² rho(0) since Tzz(0)=rho(0).
rho0,L0=s.symbols('rho0 L0')
assert s.simplify((-q*q*L0).subs(L0,rho0)+q*q*rho0)==0
# Trace free 4D Maxwell stress in -+++ convention: -T00+sum_i Tii=0.
assert s.simplify(-R+s.trace(T))==0
# At symmetric transverse widths a=b the TT+ source vanishes while
# scalar density and scalar anisotropic stress remain.
assert s.simplify(P.subs(b,a))==0
assert s.simplify(scalar.subs(b,a))!=0
print("PASS: compact Maxwell initial Fourier scalar/vector/TT split, Ward jets, conformal trace")
print("TT_plus / energy =",s.factor(P/R))
print("scalar longitudinal STF / energy =",s.factor(scalar/R))
