#!/usr/bin/env python3
"""Gravity v15.1122: an accelerated pair of events produces a null-cone
causal diamond whose intersection is an EXACT boosted/rest action-shaped circle.

Worldline and secant labels from audited Gravity v15.1100:
T(u)=R sinh(u), X(u)=R(cosh(u)-1), k(u)=R exp(u).
Two events u1=m-d, u2=m+d, d>0. Spatial light-front pair
inside 2+1 Minkowski: (T-T1)^2=(X-X1)^2+Y², (T-T2)^2=(X-X2)^2+Y².
Their invariant apex separation is 2R sinh(d).
"""
import sympy as s
R,m,d=s.symbols("R m d",positive=True,real=True)
u1=m-d;u2=m+d
T=lambda u:R*s.sinh(u)
X=lambda u:R*(s.cosh(u)-1)
DT=s.trigsimp(T(u2)-T(u1))
DX=s.trigsimp(X(u2)-X(u1))
assert s.simplify(DT-2*R*s.cosh(m)*s.sinh(d))==0
assert s.simplify(DX-2*R*s.sinh(m)*s.sinh(d))==0
tau2=s.simplify(DT*DT-DX*DX)
assert s.simplify(tau2-4*R*R*s.sinh(d)**2)==0
v=s.simplify(DX/DT)
assert s.simplify(v-s.tanh(m))==0
radius=R*s.sinh(d)
Ccut=s.simplify(tau2/(2*DT))
assert s.simplify(Ccut-radius*s.sech(m))==0
A=DT/2; B=radius; focal=DX/2
assert s.simplify(A**2-B**2-focal**2)==0
assert s.simplify(A-radius*s.cosh(m))==0
assert s.simplify(focal-radius*s.sinh(m))==0
# The center of the causal ellipse is the midpoint of both events.
assert s.simplify((X(u1)+X(u2))/2-X(m)-R*s.cosh(m)*(s.cosh(d)-1))==0
# Physical rapidity difference (source proper time) =2d c/a; chord
# radius R sinh(d) is NOT a period or prescribed quantum action.
k1,k2=s.symbols("k1 k2",positive=True,real=True)
mm=s.log(s.sqrt(k1*k2)/R)
dd=s.log(k2/k1)/2
assert s.simplify(s.tanh(mm).rewrite(s.exp)-
                  (k1*k2-R**2)/(k1*k2+R**2))==0
assert s.simplify(R*s.sinh(dd).rewrite(s.exp)-
                  R*(k2-k1)/(2*s.sqrt(k1*k2)))==0
assert s.diff(radius,m)==0
assert s.simplify(radius.subs(d,0))==0
assert s.simplify(v.subs(m,0))==0
print("PASS accelerated pair, invariant chord interval, boosted ellipse and sech cut")
print("v=tanh(midpoint rapidity) =",v)
print("rest circle radius =",radius)
print("cut plane intercept =",Ccut)
print("secant-label eccentricity=abs((k1*k2-R²)/(k1*k2+R²))")
print("secant-label radius=R*(k2-k1)/(2*sqrt(k1*k2)) (k2>k1)")
