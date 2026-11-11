#!/usr/bin/env python3
"""Exact WKB propagating K4 shear/photon phase matching and static-field Maxwell source.
Full exploratory reproducer also available in cone_propagating_k4_gates_202_205.zip.
"""
import sympy as s
K,m,v,H,eta,omega=s.symbols("K m v H eta omega",positive=True)
Om=s.sqrt(K*K+m*m)
q2=s.factor((Om**2/v**2-K*K)/4)
assert s.simplify(q2-(m*m+K*K*(1-v*v))/(4*v*v))==0
assert s.simplify(q2.subs(v,1)-m*m/4)==0
assert s.simplify(q2.subs(m,0)-K*K*(1-v*v)/(4*v*v))==0
ep=s.symbols("ep",positive=True)
pair=-ep*omega**2+K*K/4 # O(shear) photon pair cross-coefficient for y polarization
assert s.simplify(pair.subs({ep:1/v**2,omega:Om/2})+q2)==0
assert s.simplify(pair.subs({ep:1/v**2,omega:Om/2}).subs({v:1,m:0}))==0
mt2=s.Rational(8,3)*eta*H**2
assert s.simplify(q2.subs({v:1,m:s.sqrt(mt2)})-s.Rational(2,3)*eta*H**2)==0
for ratio in (100,1000):
 for e in (s.Rational(3,8),s.Rational(3,4),s.Rational(3,2)):
  val=(s.Rational(2,3)*e)/ratio**2
  print("K/H",ratio,"eta",e,"q_perp/K",float(s.sqrt(val)),"vertex/K²",float(val))
t,z,E0,small=s.symbols("t z E0 small",real=True)
amp=s.Function("a")(t,z); shear=s.Function("b")(t,z)
ay=-E0*t+small*amp
metric_factor=s.exp(2*small*shear)
eq=s.diff(metric_factor*s.diff(ay,t),t)-s.diff(metric_factor*s.diff(ay,z),z)
linear=s.diff(eq,small).subs(small,0)
assert s.simplify(linear-(s.diff(amp,t,2)-s.diff(amp,z,2)-2*E0*s.diff(shear,t)))==0
print("PASS: full exact phase matching, TT vertex, K4 suppressed channel, static E seed source.")
