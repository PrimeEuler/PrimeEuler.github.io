#!/usr/bin/env python3
"""Gravity v15.1185 — boost orbits on putative quarter observability hyperboloid.

Mathematical model: closed refined q=2 spin chain j=L/4, h=1/2,
m_i=-j+i/2, T=j+1/4, Y_i²=j(j+h)-m_i².
Q=T²-X²-Y²=1/16 and A=T+X=(2i+1)/4,
B=T-X=(2L-2i+1)/4. SO+(1,1) boosts A->exp(eta)A,
B->exp(-eta)B. They preserve Q,Y² and AB, NOT T nor finite grid.
Mirrors i<->L-i are equal Y² and pairwise boost-related.
They are not a single boost symmetry or physical gravity operator.
"""
import sympy as s
eta,A,B,Y,mu=s.symbols('eta A B Y mu',real=True,positive=True)
ep=s.exp(eta)
assert s.simplify((ep*A)*(B/ep)-A*B)==0
assert s.simplify((ep*A)*(B/ep)-Y**2-mu-(A*B-Y**2-mu))==0
for L in range(1,16):
    j=s.Rational(L,4);h=s.Rational(1,2);T=j+h/2
    pts=[]
    for i in range(L+1):
        m=-j+s.Rational(i,2)
        a=s.simplify(T+m);b=s.simplify(T-m)
        y2=s.simplify(j*(j+h)-m*m)
        assert a==s.Rational(2*i+1,4)
        assert b==s.Rational(2*L-2*i+1,4)
        assert a*b-y2==s.Rational(1,16)
        assert T*T-m*m-y2==s.Rational(1,16)
        pts.append((a,b,y2))
    for i in range(L+1):
        a,b,y2=pts[i];ar,br,y2r=pts[L-i]
        assert (ar,br,y2r)==(b,a,y2)
        z=s.simplify(ar/a)
        assert s.simplify((z*a)*(b/z)-a*b)==0
        assert s.simplify(z*b/a-1)==0
    # A common nonzero boost mapping the ENTIRE finite set onto itself
    # would scale its strictly positive minimum & maximum by same z;
    # equality of finite sets forces z=1, hence eta=0.
    assert min(pt[0] for pt in pts)==s.Rational(1,4)
    assert max(pt[0] for pt in pts)==s.Rational(2*L+1,4)
    if L in [1,3,5]:
        print('L=',L,'quarter factors and Y²:',pts)
print('PASS L=1..15, Q=1/16, mirror boost, finite-grid noninvariance')
print('OPEN physical momentum map and gravitation-selected dynamics')
