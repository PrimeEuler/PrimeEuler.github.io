#!/usr/bin/env python3
"""Gravity v15.862: Muse/Sandbox force lever versus physical stress and TT.

MusE v15.859-860: light-cone energy labels U=E+p, V=E-p (c=1).
A classical dust stress at one event has T^{mu nu}=A w^mu w^nu,
w=(1,beta n_v). Contraction with null covectors (1,+/- n_v)
gives A(1+/-beta)^2. The null flux leverage is the *square*
of U/V, not U/V. The normalized stress asymmetry is tanh(2 psi),
whereas U/V's asymmetry is tanh psi.

The same beta/lever ratio does not select TT detector response:
a wavevector along z projects a dust spatial stress
S_ij=A beta_i beta_j onto TT. For a velocity in the xz-plane,
its tensor source norm depends on sin(theta)^2 and vanishes for
motion parallel to the wavevector. A is externally supplied.
This is a local kinematic stress-projection comparator, NOT a
globally conserved accelerated point-particle matter source and
NOT a source-to-optical K4 simulation.
"""
import sympy as s
beta,theta,A=s.symbols("beta theta A", positive=True, real=True)
gamma=1/s.sqrt(1-beta**2)
E=s.symbols("E",positive=True,real=True)
u=E*(1+beta)
v=E*(1-beta)
assert s.simplify((u-v)/(u+v)-beta)==0
lever=s.factor(u/v)
assert lever==(beta+1)/(1-beta)
# 1+1D snapshot: T=A [[1,beta],[beta,beta²]]
T=A*s.Matrix([[1,beta],[beta,beta**2]])
l_plus=s.Matrix([1,1]);l_minus=s.Matrix([1,-1])
plus=s.factor((l_plus.T*T*l_plus)[0])
minus=s.factor((l_minus.T*T*l_minus)[0])
assert s.simplify(plus-A*(1+beta)**2)==0
assert s.simplify(minus-A*(1-beta)**2)==0
assert s.simplify(plus/minus-lever**2)==0
stress_asym=s.factor((plus-minus)/(plus+minus))
assert s.simplify(stress_asym-2*beta/(1+beta**2))==0
assert s.simplify(stress_asym-beta)!=0
# Orientation of spatial dust stress relative to measurement wavevector
# n_k=z, velocity unit vector in xz plane, theta angle to z.
w=s.Matrix([beta*s.sin(theta),0,beta*s.cos(theta)])
P=s.diag(1,1,0)
S=A*w*w.T
S_TT=s.simplify(P*S*P-s.trace(P*S)*P/2)
expect=A*beta**2*s.sin(theta)**2*s.diag(s.Rational(1,2),
                                        -s.Rational(1,2),0)
assert (S_TT-expect).applyfunc(s.simplify)==s.zeros(3)
assert s.simplify(s.trace(S_TT*S_TT)
     -A**2*beta**4*s.sin(theta)**4/2)==0
assert S_TT.subs(theta,0)==s.zeros(3)
assert S_TT.subs(theta,s.pi/2)!=s.zeros(3)
# Angular mean of sin(theta)^4 over isotropic directions is 8/15.
mu=s.symbols("mu",real=True)
mean=s.integrate((1-mu**2)**2/2,(mu,-1,1))
assert mean==s.Rational(8,15)
for b in (s.Rational(1,4),s.Rational(1,2),s.Rational(4,5)):
    print("beta",b,"energy U/V",lever.subs(beta,b),
          "null stress plus/minus",(plus/minus).subs(beta,b),
          "stress asymmetry",stress_asym.subs(beta,b))
# Same beta=1/2 and source A give TT=0 for parallel and nonzero
# for transverse wavevector; lever is 3 for both orientations.
assert lever.subs(beta,s.Rational(1,2))==3
assert s.simplify(S_TT[0,0].subs({beta:s.Rational(1,2),
                theta:s.pi/2})-A/8)==0
print("PASS standard SR energy and null-stress asymmetries differ")
print("PASS identical leverage -> zero or nonzero TT depending on angle")
print("PASS isotropic angular average sin^4(theta)=8/15")
print("NEGATIVE no source-independent Cone gravitational selector identified")
