#!/usr/bin/env python3
"""Gravity v15.1317: exact sourced K4 scalar longitudinal and transverse-
averaged spatial Einstein equations. Requires original Maxwell Ward and
sourced scalar P equation; not full SVT/ADM closure or a physical detector.
"""
import sympy as s
t,k=s.symbols("t k",positive=True)
p=s.Function("P")(t);r=s.Function("r")(t)
f=s.Function("F")(t);T=s.Function("T")(t)
I=s.I; den=1+k*k
Pdd=-3*s.diff(p,t)/t-(2+k*k)*p/t**2+9*(3*T-r)/(2*k*k*t**4)
rdot=-I*s.sqrt(3)*k*f/t
fdot=-I*s.sqrt(3)*k*T/t
Jb=-I*s.sqrt(3)*k*f/t
Jbd=(-3*k*k*T+I*s.sqrt(3)*k*f)/t**2
phi=((t*t*Pdd+2*t*s.diff(p,t))/3-3*r/t**2-3*Jbd/(2*k*k))/den
psi=((k*k*p-t*s.diff(p,t))/3-3*r/(2*t*t)+3*Jb/(2*k*k*t))/den
Pddd=s.diff(Pdd,t).subs({s.diff(p,t,2):Pdd,s.diff(r,t):rdot,s.diff(f,t):fdot})
subs={s.diff(p,t,3):Pddd,s.diff(p,t,2):Pdd,
      s.diff(r,t,2):s.diff(rdot,t).subs({s.diff(f,t):fdot}),
      s.diff(f,t,2):s.diff(fdot,t),s.diff(r,t):rdot,s.diff(f,t):fdot}
def reduce(expr):
    for _ in range(3):expr=expr.subs(subs)
    return s.factor(expr)
psidot=reduce(s.diff(psi,t))
psiddot=reduce(s.diff(psi,t,2))
phidot=reduce(s.diff(phi,t))
Gz=2*(psiddot+(3*psidot+phidot)/t+phi/t**2)
Gx=Gz+3*k*k*(psi-phi)/t**2
Tz=9*T/t**4-2*psi/t**2-2*k*k*p/(3*t**2)
Tx=9*(r-T)/(2*t**4)-2*psi/t**2+4*k*k*p/(3*t**2)
assert s.factor(Gz-Tz)==0
assert s.factor(Gx-Tx)==0
print("PASS scalar longitudinal and transverse-averaged Einstein spatial equations")
# Separately derive the solid principal pressure terms from the unexpanded F.
eta,C,a,eps=s.symbols("eta C a eps",positive=True)
b1,b2,b3=s.symbols("b1 b2 b3",positive=True)
B=[b1,b2,b3]
solid=C*(b1*b2*b3)**s.Rational(1,3)*(1+eta*((b1*b1+b2*b2+b3*b3)/(b1+b2+b3)**2-s.Rational(1,3)))
pressure=[-solid+2*b*s.diff(solid,b) for b in B]
q=s.symbols("Psi",real=True)
bx=a**-2*(1+2*eps*q)
bz=a**-2*(1+2*eps*(q-k*k*p))
v={b1:bx,b2:bx,b3:bz}
px=s.factor(s.diff(pressure[0].subs(v),eps).subs(eps,0).subs({a:t/s.sqrt(3),eta:s.Rational(3,4),C:1}))
pz=s.factor(s.diff(pressure[2].subs(v),eps).subs(eps,0).subs({a:t/s.sqrt(3),eta:s.Rational(3,4),C:1}))
assert s.factor(px+2*q/t**2-4*k*k*p/(3*t**2))==0
assert s.factor(pz+2*q/t**2+2*k*k*p/(3*t**2))==0
print("PASS independently varied K4 scalar solid spatial pressures")
print("OPEN transverse vector and TT, full metric, causal optical detector")
