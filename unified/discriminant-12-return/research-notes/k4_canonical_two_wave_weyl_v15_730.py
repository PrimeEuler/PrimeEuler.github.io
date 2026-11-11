#!/usr/bin/env python3
"""v15.730: explicit on-shell canonical scalar source yields nonzero K4 Weyl.
Two real KG waves on coasting FLRW produce a quadratic cross-stress
Fourier component K=p+q with nonzero scalar, vector and tensor stress
projectors. Use pressure-corrected v15.728/729 K4 scalar equations and
initial P=Pdot=0 at tau=1. Nonlocalized plane-wave benchmark, NOT a
finite spatial packet or a complete T/V detector response.
"""
import sympy as s
t=s.symbols("tau",positive=True,real=True)
x,z=s.symbols("x z",real=True)
a=t/s.sqrt(3)
p2=s.Integer(4);q2=s.Integer(1);K2=p2+q2
A=s.cos(s.sqrt(3*p2-1)*s.log(t))/t
B=s.cos(s.sqrt(3*q2-1)*s.log(t))/t
chi=A*s.cos(2*x)+B*s.cos(z)
KG=s.simplify(s.diff(chi,t,2)+3*s.diff(chi,t)/t
 -(s.diff(chi,x,2)+s.diff(chi,z,2))/a**2)
assert KG==0
p=s.Matrix([2,0,0]);q=s.Matrix([0,0,1]);K=p+q
# Mode amplitude exp(iK.x): each real cosine contributes 1/2.
# T0i=(-i/4a^2)(A'B q_i + AB' p_i), K=p+q.
JP=a**3*s.diff(A,t)*s.diff(B,t)/4
JB=a*a*(q2*s.diff(A,t)*B+p2*A*s.diff(B,t))/4
JS=3*JP # p.q=0, pressure-trace cross mode is purely kinetic.
assert s.simplify(t*s.diff(JP,t)+s.sqrt(3)*JB+JS)==0
assert s.simplify(JP.subs(t,1)-1/(12*s.sqrt(3)))==0
assert s.simplify(JB.subs(t,1)+s.Rational(5,12))==0
assert s.simplify(JS.subs(t,1)-1/(4*s.sqrt(3)))==0
assert s.simplify(s.diff(JB,t).subs(t,1)+s.Rational(7,6))==0
eta=s.Rational(3,4)
beta=(8*eta*(1+K2)-3*K2)/3
assert beta==7
forcing=3*s.sqrt(3)*JS/(2*K2*t**3)-9*(t*s.diff(JB,t)+JB)/(2*K2**2*t**3)
Pacc=s.simplify(forcing.subs(t,1))
assert Pacc==s.Rational(9,25)
# Constraint-compatible initial P(1)=Pdot(1)=0; the metric lapse and
# shift are fixed by the source constraints, not set to zero arbitrarily.
PhiN=s.simplify(Pacc/(3*(1+K2))
 +s.sqrt(3)*(JP+JS).subs(t,1)/(2*(1+K2))
 -3*s.diff(JB,t).subs(t,1)/(2*K2*(1+K2)))
PsiN=s.simplify(s.sqrt(3)*JP.subs(t,1)/(2*(1+K2))
 +3*JB.subs(t,1)/(2*K2*(1+K2)))
W=s.simplify(K2*(PhiN+PsiN)/(2*a.subs(t,1)**2))
assert PhiN==s.Rational(191,1800)
assert PsiN==-s.Rational(1,72)
assert W==s.Rational(83,120)
Q=s.diag(-s.Rational(1,3),-s.Rational(1,3),s.Rational(2,3))
assert s.trace(Q*Q)==s.Rational(2,3)
S=p*q.T+q*p.T;nh=K/s.sqrt(K2);Perp=s.eye(3)-nh*nh.T
TT=s.simplify(Perp*S*Perp-Perp*s.trace(Perp*S)/2)
V=s.simplify(Perp*S*nh*nh.T+nh*(nh.T*S*Perp))
SC=s.simplify(S-TT-V)
norm=lambda X:s.simplify(s.trace(X*X))
assert (norm(TT),norm(V),norm(SC))==(
 s.Rational(32,25),s.Rational(72,25),s.Rational(96,25))
print("PASS: on-shell canonical scalar two-wave source, corrected energy Ward")
print("PASS: source has nonzero scalar, vector, tensor stress projectors")
print("PASS: K4 scalar curvature W(1)=83/120 for epsilon^2 Fourier amplitude")
print("PhiN=",PhiN,"PsiN=",PsiN,"W=",W)
