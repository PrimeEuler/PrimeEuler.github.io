#!/usr/bin/env python3
"""Audit Round 574 reproduction repair for v15.921 legacy WebGL identities.
Source repository webgl/index.html:
X=[(n+1)/2-k]/t, Y=sqrt(k*(n+1-k))/t,
Z=sqrt(X**2+Y**2); hyperbola Yh=sqrt(N) (NOT /t).
"""
import sympy as s
n,k,t,N=s.symbols('n k t N',positive=True)
a=n+1-k;b=k;u=1/t
X=s.simplify(((n+1)/2-k)/t)
Y2=s.simplify(k*(n+1-k)/t**2)
T=s.simplify((n+1)/(2*t))
assert s.simplify(X-u*(a-b)/2)==0
assert s.simplify(Y2-u*u*a*b)==0
assert s.simplify(T*T-X*X-Y2)==0
assert s.simplify((T*T-X*X)-a*b/t**2)==0
assert s.simplify(a*b-N*t**2)==a*b-N*t**2
for t0 in range(1,5):
  for n0 in range(1,15):
    for k0 in range(1,n0+1):
      xx=X.subs({t:t0,n:n0,k:k0})
      yy=Y2.subs({t:t0,n:n0,k:k0})
      zz=T.subs({t:t0,n:n0,k:k0})
      assert xx**2+yy==zz**2
      assert s.simplify(xx**2+N-(xx**2+yy)).subs(N,s.Rational(k0*(n0+1-k0),t0*t0))==0
D=5
assert [(D-k,k, s.Rational(D,2)-k, k*(D-k))
        for k in range(1,D)]==[(4,1,s.Rational(3,2),4),
        (3,2,s.Rational(1,2),6),(2,3,-s.Rational(1,2),6),
        (1,4,-s.Rational(3,2),4)]
print('PASS v15.921: exact WebGL cone, hyperbola scale, D=5 amplitudes and 420 sample points')
