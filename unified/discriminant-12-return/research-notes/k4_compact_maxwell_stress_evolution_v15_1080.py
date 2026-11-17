#!/usr/bin/env python3
"""v15.1080: Maxwell evolution of compact-source integrated plus stress.

At t=0 E=(partial_y Psi,-partial_x Psi,0), B=0, where
Psi=A f(x/a) f(y/b) f(z/c), f(s)=(1-s²)^3 inside |s|<1 and 0 outside.
Free Maxwell: E_dot=0, E_ddot=Laplace E, B_dot=-curl E.
Not a solved K4 gravity/ADM observable.
"""
import sympy as s
q=s.symbols("q",real=True)
f=(1-q*q)**3
I0=s.integrate(f**2,(q,-1,1))
I1=s.integrate(s.diff(f,q)**2,(q,-1,1))
I2=s.integrate(s.diff(f,q,2)**2,(q,-1,1))
assert (I0,I1,I2)==(s.Rational(2048,3003),s.Rational(1024,385),s.Rational(1024,35))
a,b,c,A=s.symbols("a b c A",positive=True)
X=A*A*a*c/b*I0**2*I1
Y=A*A*b*c/a*I0**2*I1
energy=(X+Y)/2
P0=(Y-X)/2
# Pdd=int[Ey Delta Ey-Ex Delta Ex +(curl E)_y^2-(curl E)_x^2].
# All six gradient norms are independent products of three one-dimensional integrals.
ex_dx=A*A*c/(a*b)*I1**2*I0
ex_dy=A*A*a*c/b**3*I0**2*I2
ex_dz=A*A*a/(b*c)*I0*I1**2
ey_dx=A*A*b*c/a**3*I0**2*I2
ey_dy=A*A*c/(a*b)*I1**2*I0
ey_dz=A*A*b/(a*c)*I0*I1**2
Pdd=s.factor((ex_dx+ex_dy+ex_dz)-(ey_dx+ey_dy+ey_dz)+ex_dz-ey_dz)
expected=A*A*c*I0**2*I2*(a/b**3-b/a**3)+2*A*A*I0*I1**2/c*(a/b-b/a)
assert s.simplify(Pdd-expected)==0
ratio=s.factor(Pdd/energy)
assert s.simplify(ratio-22*(a*a-b*b)/(a*a*b*b)-s.Rational(78,5)*(a*a-b*b)/(c*c*(a*a+b*b)))==0
assert s.simplify(P0/energy-(b*b-a*a)/(b*b+a*a))==0
ell=s.symbols("ell",positive=True)
assert s.simplify(ratio.subs({a:ell,b:2*ell,c:ell})+s.Rational(1293,50)/ell**2)==0
assert s.simplify(Pdd.subs({b:a}))==0
print("PASS exact compact Maxwell source initial stress curvature and longitudinal B generation")
print("I0=",I0,"I1=",I1,"I2=",I2)
print("P0/energy=",s.factor(P0/energy),"Pdd/energy=",ratio)
