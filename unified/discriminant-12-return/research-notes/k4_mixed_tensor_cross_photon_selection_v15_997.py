#!/usr/bin/env python3
"""v15.997 control: cross-polarized gravity mixing is not by itself
a source for single-y photon mode. Same local 1D Maxwell model as v15.995.
"""
import sympy as s
b,c=s.symbols("b c",real=True)
S=s.Matrix([[b,c],[c,-b]])
Q=b*b+c*c
# g_transverse^{-1}=exp(-2S). Through cubic:
inv3=s.eye(2)-2*S+2*Q*s.eye(2)-s.Rational(4,3)*Q*S
assert s.simplify(inv3[1,1]-(1+2*b+2*Q+s.Rational(4,3)*b*Q))==0
assert s.diff(inv3[1,1],c).subs(c,0)==0
assert s.diff(inv3[0,1],c).subs({c:0,b:0})==-2
# The all-y electromagnetic field strength has no x component, so only
# inverse metric yy multiplies F_{ty}² and F_{zy}²; gxy requires F_{mu x}.
# The inverse determinant det exp(2S)=1 (exact traceless matrix).
assert s.trace(S)==0
print("PASS: y-only Maxwell vertex linear in cross polarization vanishes;")
print("a second physical photon polarization would be needed for linear h_xy coupling.")
