#!/usr/bin/env python3
"""v15.729: traceful matter source -> full K4 scalar Bardeen/Weyl transfer.

The sourced scalar auxiliary Hessian H is derived from the original EH
and solid quadratic action in v15.711-712; the free P-to-metric transfer
is v15.720. The physical pressure source J_psi modifies the scalar Ward
and hence the Newtonian lapse. All expressions are in the original
v14.935 (+---), coasting a=tau/sqrt3, Fourier k>0 conventions.
"""
import sympy as s
k,t=s.symbols("k tau",positive=True,real=True)
p=s.Function("P")(t)
JP=s.Function("J_Phi")(t);JB=s.Function("J_B")(t);JS=s.Function("J_psi")(t)
a=t/s.sqrt(3)
H=s.Matrix([[-2*t/s.sqrt(3),2*t*k*k/3],
            [2*t*k*k/3,2*t*k*k/(3*s.sqrt(3))]])
assert s.simplify(H.det()+4*t*t*k*k*(1+k*k)/9)==0
delta=-H.inv()*s.Matrix([JP,JB])
sourcePhi=s.factor(delta[0]+s.diff(a*delta[1],t))
sourcePsi=s.factor(-delta[1]/s.sqrt(3))
ward={s.diff(JP,t):-(s.sqrt(3)*JB+JS)/t}
sourcePhi=s.factor(sourcePhi.subs(ward))
expectPhi=s.sqrt(3)*(JP+JS)/(2*t*(1+k*k))-3*s.diff(JB,t)/(2*k*k*(1+k*k))
expectPsi=s.sqrt(3)*JP/(2*t*(1+k*k))+3*JB/(2*k*k*t*(1+k*k))
assert s.simplify(sourcePhi-expectPhi)==0
assert s.simplify(sourcePsi-expectPsi)==0
Phi=s.factor((t*t*s.diff(p,t,2)+2*t*s.diff(p,t))/(3*(1+k*k))+expectPhi)
Psi=s.factor((k*k*p-t*s.diff(p,t))/(3*(1+k*k))+expectPsi)
assert s.simplify(Phi-Phi.subs(JS,0)-s.sqrt(3)*JS/(2*t*(1+k*k)))==0
assert s.simplify(Psi-Psi.subs(JS,0))==0
# Scalar Weyl tensor is first-order gauge invariant on FLRW since the
# background Weyl vanishes. W is its electric STF scalar amplitude.
W=s.factor(k*k*(Phi+Psi)/(2*a*a))
Q=s.diag(-s.Rational(1,3),-s.Rational(1,3),s.Rational(2,3))
E=W*Q
assert s.simplify(s.trace(E))==0
assert s.simplify(s.trace(E*E)-s.Rational(2,3)*W**2)==0
eta=s.symbols("eta",positive=True,real=True)
beta=(8*eta*(1+k*k)-3*k*k)/3
Pforce=3*s.sqrt(3)*JS/(2*k*k*t**3)-9*(t*s.diff(JB,t)+JB)/(2*k**4*t**3)
Pacc=Pforce-3*s.diff(p,t)/t-beta*p/t**2
W_on=s.factor(W.subs(s.diff(p,t,2),Pacc))
assert not W_on.has(s.diff(p,t,2))
assert s.simplify(W_on.subs(JS,0)-W.subs(JS,0).subs(s.diff(p,t,2),Pacc.subs(JS,0)))==0
print("PASS: exact pressure-corrected Bardeen metric potentials from K4 ADM")
print("PASS: gauge-invariant electric Weyl STF 2/3 norm and on-shell transfer")
print("PRESSURE_ADDITION_TO_PHI=",s.factor(Phi-Phi.subs(JS,0)))
print("PHI_NEWTON=",Phi)
print("PSI_NEWTON=",Psi)
print("WEYL_ON_SHELL=",W_on)
