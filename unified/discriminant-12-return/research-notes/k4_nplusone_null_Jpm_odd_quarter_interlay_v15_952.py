#!/usr/bin/env python3
"""v15.952: Schwinger J+- transitions live on fixed D=n+1 null section;
at common D, half-unit factor rows split into EM even and new odd
interleaves. The ordinary SU2 operator cannot create odd-row amplitude.
No spacetime-frequency/physical intersector law is asserted.
"""
import sympy as s
D=s.symbols('D',integer=True,positive=True)
r=s.symbols('r',integer=True,nonnegative=True)
Y2=lambda x:x*(D-x)
X=lambda x:D/s.Integer(2)-x
assert s.simplify(s.Rational(1,4)*(2*r)*(2*D-2*r)-Y2(r))==0
assert s.simplify(Y2(r+s.Rational(1,2))-
                  (Y2(r)+Y2(r+1))/2-s.Rational(1,4))==0
assert s.simplify((D/s.Integer(2))**2-X(r)**2-Y2(r))==0
assert s.simplify((D/s.Integer(2))**2-
                  X(r+s.Rational(1,2))**2-Y2(r+s.Rational(1,2)))==0
for dd in range(2,16):
    N=dd-1
    plus=s.zeros(dd)
    for k in range(1,dd):
        plus[k-1,k]=s.sqrt(k*(dd-k))
    minus=plus.T
    Nz=(dd-1)*s.eye(dd)
    z=s.diag(*[s.Rational(dd-1,2)-k for k in range(dd)])
    assert Nz*plus-plus*Nz==s.zeros(dd)
    assert plus*minus-minus*plus==2*z
    assert s.simplify((plus*minus+minus*plus)/2+z*z-
                      s.Rational(N*(N+2),4)*s.eye(dd))==s.zeros(dd)
    em=[]; half=[]
    for l in range(1,2*dd):
        kk=s.Rational(l,2)
        yy=kk*(dd-kk)
        if l%2==0:
            em.append(yy)
        else:
            half.append(yy)
        assert (s.Rational(dd,2)-kk)**2+yy==s.Rational(dd*dd,4)
        assert l%2==(2*dd-l)%2
    assert em==[k*(dd-k) for k in range(1,dd)]
    assert len(em)==dd-1 and len(half)==dd
    # The odd-row projected step-1 ladder misses a nonzero edge at k=1/2.
    assert Y2(s.Rational(1,2)).subs(D,dd)>0
print('PASS: null geometry, Schwinger J algebra, even/odd incidence,')
print('midpoint 1/4, nonclosing half-row boundary D=2..15')
