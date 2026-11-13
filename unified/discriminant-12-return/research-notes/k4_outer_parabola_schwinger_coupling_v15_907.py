#!/usr/bin/env python3
"""Gravity v15.907: exact fixed-diameter Schwinger chord and drive obstruction.

No physical force law or drive coefficient is inferred from geometry alone.
"""
import sympy as S

n,k,u=S.symbols('n k u', integer=True, positive=True)
assert S.simplify((n+k)**2-(n-k)**2-4*n*k)==0
assert S.simplify(((n+k)/2)**2-((n-k)/2)**2-n*k)==0

for D in range(2,10):
    # Paper C Fock dictionary: (x,y)=(a+1,b), a+b=D-1.
    jp=S.zeros(D)
    jz=S.zeros(D)
    for a in range(D):
        b=D-1-a
        jz[a,a]=S.Rational(a-b,2)
        if a<D-1:
            jp[a+1,a]=S.sqrt((a+1)*b)
    jm=jp.T
    x=u*(jz+S.eye(D)/2)
    y2=u**2*jm*jp
    T=S.Rational(D,2)*u
    assert y2.is_diagonal()
    assert S.simplify(x*x+y2-T*T*S.eye(D))==S.zeros(D)
    assert S.simplify(jz*y2-y2*jz)==S.zeros(D)
    assert S.simplify(jz*jp-jp*jz-jp)==S.zeros(D)
    for a in range(D-1):
        npair=a+1
        kpair=D-1-a
        assert S.simplify(jp[a+1,a]**2-npair*kpair)==0
    if D==5:
        # Pair (4,1) is a=3. Jx couples in BOTH directions.
        a=3
        assert jp[a+1,a]==2
        assert jm[a-1,a]==S.sqrt(6)
        # H_int / hbar = g Jx; short-time total leakage:
        # (g*t)^2 (4+6)/4 + O((g*t)^4).
        assert S.simplify((jp[a+1,a]**2+jm[a-1,a]**2)/4-S.Rational(5,2))==0

print('PASS: outer circle chord-square operator, diagonal geometry obstruction, and two-sided Jx coupling D=2..9')
