#!/usr/bin/env python3
"""v15.706: exact K4 full-SVT three-sector dispersion gap ratio.

The result is an identity of frozen-background local squared frequencies,
NOT a prediction of source amplitudes or full cosmological arrival times.
Its 3 arises from conventional isotropic elasticity at dp/drho=-1/3
(Carter 1973), hence is not a unique Cone signature.
"""
import sympy as s
eta,H,k,eps,cv2,w=s.symbols("eta H k eps c_V_sq w",real=True)
mass2=s.Rational(8,3)*eta*H**2
T=mass2+k**2
V=mass2+s.Rational(2,3)*eta*k**2
S=mass2+(s.Rational(8,9)*eta-s.Rational(1,3))*k**2
assert s.simplify((T-V)-3*(V-S))==0
assert s.simplify((T-V)/(V-S)-3)==0
assert s.simplify(s.Rational(8,9)*eta-s.Rational(1,3)
   -(s.Rational(4,3)*(s.Rational(2,3)*eta)-s.Rational(1,3)))==0
for e in (s.Rational(3,8),s.Rational(3,4),s.Integer(1),s.Rational(4,3)):
    assert s.simplify(((T-V)/(V-S)).subs(eta,e)-3)==0
for e in (s.Rational(3,8),s.Rational(3,4),s.Integer(1),s.Rational(3,2)):
    cs=s.Rational(8,9)*e-s.Rational(1,3)
    vv=s.Rational(2,3)*e
    assert 0<=cs<=1 and 0<vv<=1
assert s.simplify((T-V).subs(eta,s.Rational(3,2)))==0
assert s.simplify((V-S).subs(eta,s.Rational(3,2)))==0

# Isotropic relativistic elasticity: c_L^2 = dp/drho + 4 c_V^2/3.
R=s.simplify((1-cv2)/(cv2-(w+s.Rational(4,3)*cv2)))
assert s.simplify(R.subs(w,-s.Rational(1,3))-3)==0
assert s.simplify(R.subs(w,-s.Rational(1,3)+eps)
  -(1-cv2)/((1-cv2)/3-eps))==0
assert s.simplify(s.diff(R,w).subs(w,-s.Rational(1,3)))!=0
dT,dV,dS=s.symbols("dT dV dS")
Rshift=s.simplify(((T+dT)-(V+dV))/((V+dV)-(S+dS)))
assert s.simplify((Rshift-3).subs({dT:0,dV:0,dS:0}))==0
print("PASS: K4 local squared-frequency gap ratio = 3 for 3/8<eta<3/2")
print("PASS: Carter isotropic-elastic comparator; common gap and coasting required")
