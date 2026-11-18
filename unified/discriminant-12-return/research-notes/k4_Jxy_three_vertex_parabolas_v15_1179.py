#!/usr/bin/env python3
"""Gravity v15.1179 — Jxy as a nonconfocal translated row parabola.
Integer EM rows P_k and half-integer quarter-interlay P_(k+1/2) share
focus X=0. Fix state-row k and vary D=n+1, analytically continuing
Jxy²=f_D(k+1/2)-1/4. At physical Schwinger D>=k+1, its zero-height
vertex is generally OUTSIDE the sampled physical domain (k>0).
"""
import sympy as s
k,X,D=s.symbols("k X D",integer=True,nonnegative=True)
K=k+s.Rational(1,2)
P=lambda r:r*r+2*r*X
Jxy=s.expand(P(K)-s.Rational(1,4))
xv=s.factor(-K/2+s.Rational(1,8)/K)
tests={
"shifted row parabola":Jxy-(2*k+1)*X-k*(k+1),
"zero-height vertex":xv+k*(k+1)/(2*k+1),
"focus displacement":xv+K/2-1/(4*(2*k+1)),
"harmonic mean vertex":xv+k*(k+1)/(2*k+1),
"first EM vertex distance":xv+k/2+k/(2*(2*k+1)),
"second EM vertex distance":xv+(k+1)/2-(k+1)/(2*(2*k+1)),
"quarter interlay vertex offset":xv+K/2-1/(8*K),
"fixed-X average":Jxy-(P(k)+P(k+1))/2+s.Rational(1,2),
"fixed-D state":Jxy.subs(X,D/2-K)-(K*(D-K)-s.Rational(1,4)),
"first allowed physical state":Jxy.subs(X,(k+1)/2-K)-k/s.Integer(2),
"fixed D midpoint":K*(D-K)-(k*(D-k)+(k+1)*(D-k-1))/2-s.Rational(1,4)
}
for name,expr in tests.items():
    assert s.simplify(expr)==0,(name,expr)
for ki in range(9):
    x=s.simplify(xv.subs(k,ki))
    assert -s.Rational(ki+1,2)<=x<=-s.Rational(ki,2)
    if ki:assert x < -s.Rational(ki,2)
    print("k",ki,"P_k vertex",-s.Rational(ki,2),
          "Jxy vertex",x,"P_(k+1/2) vertex",-s.Rational(2*ki+1,4),
          "P_(k+1) vertex",-s.Rational(ki+1,2))
print("PASS: Jxy shifted parabola focus +1/[4(2k+1)]; others focus 0")
print("PASS: exact vertex bracketing; extrapolated vertex outside k>0 physical domain")
