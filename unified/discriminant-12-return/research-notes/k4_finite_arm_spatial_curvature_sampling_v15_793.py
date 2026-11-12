#!/usr/bin/env python3
"""v15.793: exact finite-arm SPATIAL sampling of local Fermi curvature.
This is deliberately NOT a true null-ray or long-baseline geodesic
deviation detector; it tests a defined line-average proxy for plane
Fourier curvature, and exactly shows isotropic Ricci leakage when unequal
arms have different spatial phases.
"""
import sympy as s
q=s.symbols("q",positive=True,real=True)
I=s.I
F=lambda v:s.exp(I*v/2)*s.sin(v/2)/(v/2)
f=F(q);h=F(q/s.sqrt(2))
# At k along n, choose arms (n,e), (e,b), and (n+-e)/sqrt2
# and curvature tensor R=(trace/3)I+S(nn-I/3)+V(ne+en)+T(ee-bb).
# Define spatial arm average 1/L int_0^L R_ij(tu)u^iu^j dt.
M=s.Matrix([[(2*f+1)/3,0,-1],[0,0,2],[0,2*h,0]])
assert s.simplify(M.det()+s.Rational(4,3)*(2*f+1)*h)==0
M0=M.applyfunc(lambda a:s.limit(a,q,0))
assert M0==s.Matrix([[1,0,-1],[0,0,2],[0,2,0]])
# A1 also receives (F(q)-1)*tr(R)/3, even though its local
# difference-of-arms tensor is tracefree when both have F=1.
Rtr,S,V,T=s.symbols("Rtrace S V T",real=True)
data=M*s.Matrix([S,V,T])+s.Matrix([(f-1)*Rtr/3,0,0])
assert s.simplify(s.limit(data[0],q,0)-(S-T))==0
assert s.simplify(s.limit(data[1],q,0)-2*T)==0
assert s.simplify(s.limit(data[2],q,0)-2*V)==0
assert s.simplify(data[0].diff(Rtr)-(f-1)/3)==0
# F(q/sqrt2) = 0 when q=2*pi*sqrt2*m, so vector readout loses
# rank for this simplified choice of baseline.
m=s.symbols('m',integer=True,positive=True)
assert s.trigsimp(h.subs(q,2*s.pi*s.sqrt(2)*m))==0
for val in (s.Rational(1,10),s.Integer(1),s.Integer(3)):
    mat=M.subs(q,val).evalf()
    assert abs(complex(mat.det()))>0.01
print("PASS: finite-arm spatial average exact, local 3-channel inverse recovered")
print("PASS: isotropic full-Riemann leakage (F-1)*trace(R)/3")
print("PASS: vector spatial-average null at kL=2*pi*sqrt(2)*m")
print("SCOPE: proxy tests spatial averaging only, not photon travel timing")
