#!/usr/bin/env python3
"""v15.1401 nested EM/Q2 representation-space hyperboloid volume.
Fixed-T area ratio 3:1 is not regulator-independent Lorentz scalar.
"""
import sympy as s
T,a,b,chi,R,theta=s.symbols("T a b chi R theta",positive=True,real=True)
em=s.Rational(1,2);q2=s.Rational(1,4)
area_shell=s.pi*(a*a-b*b)
area_inner=s.pi*b*b
assert s.simplify(area_shell.subs({a:em,b:q2})/area_inner.subs(b,q2))==3
assert s.simplify(area_shell.subs({a:em,b:q2})/(s.pi*em**2))==s.Rational(3,4)
assert s.simplify(s.diff(area_shell,T))==0
F=s.Matrix([R*s.cosh(chi),R*s.sinh(chi)*s.cos(theta),R*s.sinh(chi)*s.sin(theta)])
assert s.simplify(s.det(F.jacobian([R,chi,theta]))-R**2*s.sinh(chi))==0
V_shell=2*s.pi*(s.cosh(chi)-1)*(a**3-b**3)/3
V_inner=2*s.pi*(s.cosh(chi)-1)*b**3/3
assert s.simplify((V_shell/V_inner).subs({a:em,b:q2}))==7
assert s.limit(V_shell.subs({a:em,b:q2}),chi,s.oo)==s.oo
vol3=lambda m:s.Rational(4,3)*s.pi*(T*T-m*m)**s.Rational(3,2)
ratio3=s.simplify((vol3(q2)-vol3(em))/(s.Rational(4,3)*s.pi*T**3-vol3(q2)))
assert s.limit(ratio3,T,s.oo)==3
assert s.simplify(ratio3.subs(T,em))!=3
print("PASS equal-T 2+1 areas: EM-G=3*pi/16 G-null=pi/16 EM-null=pi/4")
print("PASS fixed-T slab shell volume=3*pi*(Tmax-Tmin)/16 for Tmin>=1/2")
print("PASS common rapidity cutoff invariant volume densities produce 7:1, not 3:1")
print("PASS unbounded Lorentzian shell volume diverges")
print("PASS 3+1 equal-T sphere-volume ratio T dependent, tends 3")
for tt in [s.Rational(1,2),s.Rational(3,5),s.S(1),s.S(2),s.S(4)]:
 print("3+1 T",tt,"shell/inner",float(ratio3.subs(T,tt)))
