#!/usr/bin/env python3
"""Gravity v15.982 — X-axis velocity dictionary at fixed null diameter.
Distinguish intrinsic X/T from a CHOSEN outward-edge/(2T) map.
All velocity interpretations conditional; no physical time/force.
"""
import sympy as s

D=s.symbols("D",integer=True,positive=True)
m=s.symbols("m",real=True)
T=D/s.Integer(2)
X=m
Y2=T*T-X*X
assert s.simplify(T*T-X*X-Y2)==0
beta_center=s.factor(X/T)
beta_edge=s.factor((m+s.Rational(1,2))/T)
beta_half=s.factor((m+s.Rational(1,2))/D)
assert s.simplify(beta_edge-2*beta_half)==0
assert s.simplify(beta_center-2*m/D)==0

cayley=lambda beta:(1+beta)/(1-beta)
inner=s.Rational(1,2)
outer=s.Rational(3,2)
profile={
"center":(beta_center.subs({D:4,m:inner}),beta_center.subs({D:4,m:outer})),
"edge":(beta_edge.subs({D:4,m:inner}),beta_edge.subs({D:4,m:outer})),
"half_edge":(beta_half.subs({D:4,m:inner}),beta_half.subs({D:4,m:outer}))
}
assert profile["center"]==(s.Rational(1,4),s.Rational(3,4))
assert profile["edge"]==(s.Rational(1,2),s.Integer(1))
assert profile["half_edge"]==(s.Rational(1,4),s.Rational(1,2))
assert s.factor(cayley(profile["center"][1])/cayley(profile["center"][0]))==s.Rational(21,5)
assert s.factor(cayley(profile["half_edge"][1])/cayley(profile["half_edge"][0]))==s.Rational(9,5)
assert cayley(profile["edge"][1])==s.zoo

lam=s.symbols("lam",positive=True)
for scale in (s.Rational(1,2),s.Rational(2,3),s.Rational(3,4),s.Integer(1)):
    bi=scale*s.Rational(1,4)
    bo=scale*s.Rational(3,4)
    ratio=s.factor(cayley(bo)/cayley(bi))
    assert 0<bi<bo<1
    print("lambda",scale,"beta_i",bi,"beta_o",bo,"Cayley ratio",ratio)

# Fixed-D level has a circle Y^2=T^2-X^2, not a Lorentzian
# time variable selected by dynamics. Relativistic speed needs c-tag.
for d in range(2,25):
    j=s.Rational(d-1,2)
    assert s.simplify((j+s.Rational(1,2))/(d/s.Integer(2))-1)==0
    assert s.simplify((j+s.Rational(1,2))/d-s.Rational(1,2))==0

print("PASS: exact null-cone center/edge normalization D=2..24;")
print("D=4 ratios 21/5, divergent, 9/5; free speed scaling.")
