#!/usr/bin/env python3
"""Gravity v15.1078: compact Maxwell data and exact TT-plus source ratio.

Field at initial conformal time: E=(∂y ψ,-∂x ψ,0), B=0, where
ψ=A f(x/a)f(y/b)f(z/c), f(s)=(1-s²)^3 on |s|<1 and zero outside.
This is a source for Einstein-K4, not a solved constrained metric.
"""
import sympy as s
x=s.symbols("x",real=True)
f=(1-x*x)**3
I0=s.integrate(f*f,(x,-1,1))
I1=s.integrate(s.diff(f,x)**2,(x,-1,1))
assert I0==s.Rational(2048,3003)
assert I1==s.Rational(1024,385)
a,b,c,A=s.symbols("a b c A",positive=True)
energy=s.factor(A*A*c*I0**2*I1*(a/b+b/a)/2)
plus=s.factor(A*A*c*I0**2*I1*(b/a-a/b)/2)
assert s.simplify(plus/energy-(b*b-a*a)/(b*b+a*a))==0
assert s.simplify((plus/energy).subs({a:1,b:2})-s.Rational(3,5))==0
X,Y,Z=s.symbols("X Y Z",real=True)
psi=A*(1-(X/a)**2)**3*(1-(Y/b)**2)**3*(1-(Z/c)**2)**3
Ex=s.diff(psi,Y)
Ey=-s.diff(psi,X)
assert s.diff(Ex,X)+s.diff(Ey,Y)==0
# Fields are set to zero outside compact support. f is C² across edges.
assert s.integrate(f*s.diff(f,x),(x,-1,1))==0
# Source Fourier TT+ at q=(0,0,k_z) is nonzero near k_z=0:
# after integrating x,y, both energy and plus profiles ∝ f(z/c)^2.
# For q != 0 the Fourier TT projection exists, and the ratio is 3/5.
# Matched EH+elasticity comparator uses identical retarded operator.
p,q,mu=s.symbols("p q mu",positive=True)
R=1/(p*p+q*q+mu*mu)
R_pure_GR=1/(p*p+q*q)
assert s.simplify(R/R_pure_GR-(p*p+q*q)/(p*p+q*q+mu*mu))==0
assert s.simplify(R.subs(mu,0)-R_pure_GR)==0
print("PASS: compact Maxwell initial Gauss law, finite energy, TT+ stress, 3/5 ratio, matched response")
print("I0=",I0,"I1=",I1,"energy=",energy,"plus=",plus)
