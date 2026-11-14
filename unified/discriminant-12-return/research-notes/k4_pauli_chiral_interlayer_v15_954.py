#!/usr/bin/env python3
"""Gravity v15.954: Pauli-type chiral extension on the *transition-edge*
half-grid, not on the D-dimensional Schwinger state shell. The even
edge sector has D-1 points; the odd interlayer has D points.
Unit nearest-neighbor incidence is a choice, not a physical source.
"""
import sympy as s
x=s.symbols("x")
for D in range(2,13):
    e,o=D-1,D
    B=s.zeros(o,e)
    for k in range(1,D):
        B[k-1,k-1]=1
        B[k,k-1]=1
    L=B.T*B
    assert L.det()!=0
    assert s.expand(L.charpoly(x).as_expr()-
                    s.chebyshevu(e,(x-2)/2))==0
    z=s.Matrix([(-1)**r for r in range(o)])
    assert B.T*z==s.zeros(e,1)
    Qx=s.BlockMatrix([[s.zeros(e,e),B.T],
                       [B,s.zeros(o,o)]]).as_explicit()
    Qy=s.BlockMatrix([[s.zeros(e,e),-s.I*B.T],
                       [s.I*B,s.zeros(o,o)]]).as_explicit()
    Z=s.diag(*([1]*e+[-1]*o))
    assert Qx.rank()==2*e
    assert Z*Qx+Qx*Z==s.zeros(e+o)
    assert Z*Qy+Qy*Z==s.zeros(e+o)
    assert Qx**2==Qy**2
    assert Qx*Qy+Qy*Qx==s.zeros(e+o)
    assert Qx*Qy-Qy*Qx==2*s.I*Z*(Qx**2)
    assert Qx*s.Matrix.vstack(s.zeros(e,1),z)==s.zeros(e+o,1)
    # The squared eigenvalues are 2+2 cos(pi*m/D) for
    # m=1,..,D-1, plus one unpaired zero in the odd sector.
    if D<=8:
        predicted=s.prod(x-2-2*s.cos(s.pi*m/D) for m in range(1,D))
        assert s.simplify(s.expand(L.charpoly(x).as_expr()-predicted))==0
    # Distinct positive row heights can weight an incidence choice,
    # without changing sector count. Nothing fixes an overall g.
    heights=s.diag(*[s.sqrt((s.Rational(r,1)+s.Rational(1,2))*
                              (D-s.Rational(r,1)-s.Rational(1,2)))
                      for r in range(o)])
    Bw=heights*B
    assert (Bw.T*Bw).det()!=0
    assert Bw.T*heights.inv()*z==s.zeros(e,1)
print("PASS: D=2..12, chiral Pauli identities, Chebyshev spectrum,")
print("one odd-sector zero mode, optional geometric row weights")
