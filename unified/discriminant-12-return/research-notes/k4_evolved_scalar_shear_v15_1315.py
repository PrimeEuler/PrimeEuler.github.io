#!/usr/bin/env python3
"""v15.1315: independently vary K4 solid anisotropic spatial pressure;
check evolved scalar spatial-shear Einstein identity. No spatial trace,
vector/tensor Einstein equations, full ADM or measured detector.
"""
import sympy as s
t,k,eta,C,a,eps,P,Pd,r,F,T=s.symbols("tau k eta C a eps P Pd r F T",positive=True)
ps=s.symbols("Psi",real=True)
bx=a**-2*(1+2*eps*ps)
bz=a**-2*(1+2*eps*(ps-k*k*P))
b1,b2,b3=s.symbols("b1 b2 b3",positive=True)
B=[b1,b2,b3]
Fsolid=C*(b1*b2*b3)**s.Rational(1,3)*(1+eta*((b1*b1+b2*b2+b3*b3)/(b1+b2+b3)**2-s.Rational(1,3)))
pressure=[-Fsolid+2*b*s.diff(Fsolid,b) for b in B]
variation=[s.factor(s.diff(p.subs({b1:bx,b2:bx,b3:bz}),eps).subs(eps,0)) for p in pressure]
solid=s.factor(variation[0]-variation[2])
expected=8*eta*C*k*k*P/(9*a*a)
assert s.simplify(solid-expected)==0
beta=(8*eta*(1+k*k)-3*k*k)/3
Pdd=-3*Pd/t-beta*P/t**2+9*(3*T-r)/(2*k*k*t**4)
Jbd=(-3*k*k*T+s.I*s.sqrt(3)*k*F)/t**2
Jb=-s.I*s.sqrt(3)*k*F/t
den=1+k*k
phi=s.factor(((t*t*Pdd+2*t*Pd)/3-3*r/t**2-3*Jbd/(2*k*k))/den)
psi=s.factor(((k*k*P-t*Pd)/3-3*r/(2*t*t)+3*Jb/(2*k*k*t))/den)
geom=3*k*k*(psi-phi)/t**2
Maxwell=9*(r-3*T)/(2*t**4)
solid_source=s.factor(expected.subs({a:t/s.sqrt(3),eta:s.Rational(3,4),C:1}))
assert s.simplify((geom-Maxwell-solid_source).subs(eta,s.Rational(3,4)))==0
print("K4 solid spatial x-z shear:",solid)
print("Maxwell spatial shear:",Maxwell)
print("K4 shear at eta=3/4, C=1:",solid_source)
print("PASS exact evolved scalar spatial-shear Einstein equation")
print("OPEN spatial trace, vector/tensor, complete metric and optical apparatus")
