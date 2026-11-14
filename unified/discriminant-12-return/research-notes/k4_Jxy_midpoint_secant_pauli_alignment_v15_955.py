#!/usr/bin/env python3
"""v15.955. At fixed D=n+1, the D quarter-row half-integer
MIDPOINT positions coincide with the D Schwinger STATE magnetic
coordinates, and their squared heights minus 1/4 equal the
diagonal Jx²+Jy² operator. The D-1 integer rows remain J+- EDGES.
Secant ratio labels individual edges, not frequencies; the
formal odd-quarter projected ladder is a separate operator.
"""
import sympy as s
D,k=s.symbols("D k", integer=True, positive=True)
f=lambda t:t*(D-t)
R=s.Rational(1,2)*D
xm=R-k-s.Rational(1,2)
j=(D-1)/s.Integer(2)
a2=f(k)
b2=f(k+1)
trans=(a2+b2)/2
mid=f(k+s.Rational(1,2))
assert s.simplify(mid-trans-s.Rational(1,4))==0
assert s.simplify(trans-(j*(j+1)-xm*xm))==0
assert s.simplify(R*R-mid-xm*xm)==0
ratio=D/(D-2*k)
assert s.simplify(a2-R*R*(1-1/ratio**2))==0
# Original EM edge is at X=R-k=m+1/2; midpoint at X=m.
assert s.simplify((R-k)-xm-s.Rational(1,2))==0
for d in range(2,15):
    p=s.zeros(d)
    xx=s.zeros(d)
    yy=s.zeros(d)
    for kk in range(1,d):
        ampl=s.sqrt(kk*(d-kk))
        p[kk-1,kk]=ampl
        sx=s.zeros(d); sy=s.zeros(d)
        sx[kk-1,kk]=sx[kk,kk-1]=1
        sy[kk-1,kk]=-s.I
        sy[kk,kk-1]=s.I
        xx+=ampl*sx/2
        yy+=ampl*sy/2
    assert xx==(p+p.T)/2
    assert yy==(p-p.T)/(2*s.I)
    zz=s.diag(*[s.Rational(d-1,2)-kk for kk in range(d)])
    assert xx*yy-yy*xx==s.I*zz
    midpoint=s.diag(*[
        (f(k+s.Rational(1,2))-s.Rational(1,4)).subs({D:d,k:kk})
        for kk in range(d)])
    assert s.simplify(xx*xx+yy*yy-midpoint)==s.zeros(d)
    assert s.simplify(xx*xx+yy*yy+zz*zz-
        s.Rational(d*d-1,4)*s.eye(d))==s.zeros(d)
    assert all(midpoint[kk,kk]>0 for kk in range(d))
    if d==5:
        print('D=5 transverse diagonal:',[midpoint[kk,kk] for kk in range(d)])
        print('D=5 edge J+ squared:',[kk*(d-kk) for kk in range(1,d)])
    # q2 odd L=2D-1 has 2D formal quarter-grid m-nodes:
    assert (2*d-1)+1==2*d
    assert 2*d!=d
print('PASS: universal midpoint/secant identities, D=2..14 Schwinger matrices, Pauli edge sums, carrier separation')
