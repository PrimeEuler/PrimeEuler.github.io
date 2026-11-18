#!/usr/bin/env python3
"""Gravity v15.1185 VALIDATED — boosted quarter hyperboloid factor pairs.

Additive correction of exploratory k4_gravity_hyperboloid_boost_quarter_factors_v15_1185.py:
that preliminary script reversed one factor-ratio check. This validated
script checks BOTH coordinates of the mirror boost.
"""
import sympy as s
eta,A,B,Y,mu=s.symbols('eta A B Y mu',real=True)
z=s.exp(eta)
assert s.simplify((z*A)*(B/z)-A*B)==0
for L in range(1,16):
    j=s.Rational(L,4);h=s.Rational(1,2);T=j+h/2
    pts=[]
    for i in range(L+1):
        m=-j+s.Rational(i,2)
        a=s.factor(T+m);b=s.factor(T-m)
        y2=s.factor(j*(j+h)-m*m)
        assert a==s.Rational(2*i+1,4)
        assert b==s.Rational(2*L-2*i+1,4)
        assert a*b-y2==s.Rational(1,16)
        assert T*T-m*m-y2==s.Rational(1,16)
        pts.append((a,b,y2))
    for i in range(L+1):
        a,b,y2=pts[i];ar,br,y2r=pts[L-i]
        assert (ar,br,y2r)==(b,a,y2)
        boost_factor=s.factor(ar/a)
        assert s.simplify(boost_factor*a-ar)==0
        assert s.simplify(b/boost_factor-br)==0
        assert s.simplify((boost_factor*a)*(b/boost_factor)-a*b)==0
    assert min(pt[0] for pt in pts)==s.Rational(1,4)
    assert max(pt[0] for pt in pts)==s.Rational(2*L+1,4)
    if L in (1,3,5):
        print('L',L,'points',pts)
print('PASS L=1..15: Q=1/16, mirror boosts, no global nontrivial finite-ladder boost')
