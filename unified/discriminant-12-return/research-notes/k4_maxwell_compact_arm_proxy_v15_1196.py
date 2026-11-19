#!/usr/bin/env python3
"""Gravity v15.1196: compact Maxwell initial-slice exact arm-sampling proxy.

Inherited as established (not rederived): initial longitudinal Maxwell
constraint completion v15.1159 (standard GR initial slice) and spatial
line-average proxy v15.793. The source's z envelope is
f(z/c)^2=(1-(z/c)^2)^6, |z|<=c, zero beyond.
Here c is packet width, NOT the speed of light.

Caution: v15.1159 assumes homogeneous-solid metric data fixed in the
specified initial-slice gauge; full K4 constraint completion/dynamics
and a causal finite-arm detector are not provided here.
"""
import sympy as s
u,r=s.symbols('u r',real=True,nonnegative=True)
g=(1-u**2)**6
B=s.simplify(s.integrate(g,(u,0,r))/r)
assert s.simplify(s.diff(r*B,r)-g.subs(u,r))==0
assert s.limit(B,r,0)==1
for v,exact in [(s.Rational(1,4),s.Rational(44640757639,50381979648)),
                (s.Rational(1,2),s.Rational(7981087,12300288)),
                (s.Integer(1),s.Rational(1024,3003))]:
    assert s.simplify(B.subs(r,v)-exact)==0
    print('L/c =',v,'arm-average G =',exact,'decimal',s.N(exact,12))
# From v15.1159 initial nonzero-q standard-GR scalar constraints:
kap,R,a,q=s.symbols('kappa R a q',positive=True)
Psi=-kap*R/(2*a*a*q*q);Phi=3*Psi
S=s.factor(-q*q*Phi/(a*a))
W=s.factor(q*q*(Phi+Psi)/(2*a*a))
assert s.simplify(S-3*kap*R/(2*a**4))==0
assert s.simplify(W+kap*R/a**4)==0
assert s.simplify(S/W+s.Rational(3,2))==0
# Local scalar full electric curvature Eij=A(z)deltaij+S(z)Qij.
# Spatial sampling proxy, arm along z versus arm along x, anchored at z=0:
S0,A0=s.symbols('S0 A0',real=True)
arm_z=(A0+2*S0/s.Integer(3))*B
arm_x=A0-S0/s.Integer(3)
diff=s.expand(arm_z-arm_x)
assert s.simplify(diff-((2*B+1)*S0/3+(B-1)*A0))==0
assert s.limit(diff,r,0)==S0
for v in (s.Rational(1,2),s.Integer(1)):
    gamma=s.factor((2*B.subs(r,v)+1)/3)
    leak=s.factor(B.subs(r,v)-1)
    print('L/c',v,'STF gain',gamma,'isotropic leakage /A0',leak)
    assert gamma>0 and gamma<1 and leak<0
print('PASS compact envelope exact spatial average; initial GR S/W=-3/2; isotropic leakage')
print('OPEN K4 constraint and physical isotropic tide; causal light/mirror transfer')
