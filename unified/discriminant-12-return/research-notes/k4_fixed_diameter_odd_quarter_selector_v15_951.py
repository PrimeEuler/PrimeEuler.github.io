#!/usr/bin/env python3
"""Gravity v15.951: two different factor-grid units, one common n+1
outer diameter. Exact odd-quarter shell alignment and distinct
geometric-vs-formal Casimir differences. No sourced physical selector.
Tested locally with SymPy before GitHub deposit.
"""
import sympy as s
n,u,v,P=s.symbols("n u v P", positive=True)
C=lambda j:j*(j+1)
pair_em=(n,s.Integer(1))
pair_q=(n+s.Rational(1,2),s.Rational(1,2))
assert sum(pair_em)==sum(pair_q)==n+1
Lg=2*n+1
assert s.simplify(Lg/4-n/2-s.Rational(1,4))==0
assert s.simplify(C(Lg/4)-(C(n/2)+C((n+1)/2))/2+s.Rational(1,16))==0
assert s.simplify(s.prod(pair_em)-s.prod(pair_q)-n/2+s.Rational(1,4))==0
rc2=lambda unit,diam:s.factor((s.sympify(diam)**2-s.sympify(unit)**2)/4)
assert s.simplify(rc2(s.Rational(1,2),n+1)-rc2(1,n+1)-s.Rational(3,16))==0
assert s.simplify(rc2(s.Rational(1,2),n+1)-Lg*(Lg+2)/16)==0
assert s.simplify(C(Lg/4)-rc2(s.Rational(1,2),n+1)-Lg/8)==0
assert s.simplify((P/u+u)-(P/v+v)-(u-v)*(1-P/(u*v)))==0
assert s.solve(s.Eq(P/u+u,P/v+v),P)==[u*v]
for nn in range(1,201):
    assert (2*nn+1)%2==1
    assert rc2(s.Rational(1,2),nn+1)-rc2(1,nn+1)==s.Rational(3,16)
    assert C(s.Rational(2*nn+1,4))==(C(s.Rational(nn,2))+C(s.Rational(nn+1,2)))/2-s.Rational(1,16)
print("PASS: 200 shared diameters, odd-quarter shell, geometric gap 3/16, formal midpoint -1/16")
for nn in (1,2,3,6,12):
    print(nn, "odd quarter L",2*nn+1, "EM C",C(s.Rational(nn,2)),
          "quarter formal C",C(s.Rational(2*nn+1,4)),
          "quarter geometric R_C2",rc2(s.Rational(1,2),nn+1))
