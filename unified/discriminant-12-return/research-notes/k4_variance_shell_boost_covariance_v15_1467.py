#!/usr/bin/env python3
"""Gravity v15.1467 — compare Sandbox v15.1465 two-point variance shell
to Lorentz-invariant pair-product hyperbola; 1/16 variance is
boost-dependent; interpretation may specify a distinguished frame.
"""
import sympy as s
n,k,e=s.symbols('n k e',positive=True,real=True)
T=(n+k)/2; X=(n-k)/2
nb=n*s.exp(e);kb=k*s.exp(-e)
Tb=(nb+kb)/2;Xb=(nb-kb)/2
assert s.simplify(T**2-X**2-n*k)==0
assert s.simplify(s.expand((Tb-(T*s.cosh(e)+X*s.sinh(e))).rewrite(s.exp)))==0
assert s.simplify(s.expand((Xb-(X*s.cosh(e)+T*s.sinh(e))).rewrite(s.exp)))==0
assert s.simplify(Tb**2-Xb**2-n*k)==0
assert s.simplify(Xb.subs({n:1,k:1})**2-s.sinh(e)**2)==0
assert s.simplify(X**2).subs({n:2,k:1})==s.Rational(1,4)
assert s.simplify(X**2).subs({n:1,k:s.Rational(1,2)})==s.Rational(1,16)
for x in [0,.5,1.]:
 print('rapidity=',x,'balanced pair variance=',float(s.sinh(x)**2),'invariant nk=',1.)
print('PASS pair variance changes under boost; nk invariant; 1/16 variance is not physical rest-mass invariant')
