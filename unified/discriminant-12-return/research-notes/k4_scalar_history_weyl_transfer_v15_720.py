#!/usr/bin/env python3
"""v15.720: source-history -> gauge-invariant K4 scalar Weyl transfer.

Exact coasting background, original K4 scalar ADM quadratic action
regenerated via v15.712. J_Phi,J_B satisfy tau J_Phi' +sqrt3 J_B=0.
The physical scalar P obeys the forced ODE of v15.713, whose retarded
Green function was derived in v15.714. This reproducer verifies
the source-to-metric transfer before imposing an initial condition and
tests its reduction to the v15.719 conserved tilted-source solution.
"""
import runpy
from pathlib import Path
import sympy as s
src=runpy.run_path(str(Path(__file__).with_name(
    "k4_full_scalar_sourced_mixed_v15_712.py")))
H,d=[src[n] for n in ("H","d")]
a,adot,C,kappa,eta,k=[src[n] for n in
    ("a","adot","C","kappa","eta","k")]
P,psi,P_t,psi_t=[src[n] for n in ("P","psi","P_t","psi_t")]
t=s.symbols("tau",positive=True)
p=s.Function("P")(t)
ps=s.Function("psi")(t)
jp=s.Function("J_Phi")(t)
jb=s.Function("J_B")(t)
at=t/s.sqrt(3)
subs={a:at,adot:1/s.sqrt(3),C:1,kappa:1,
      P:p,P_t:s.diff(p,t),psi:ps,psi_t:s.diff(ps,t)}
q=(-H.subs(subs).inv()*(d.subs(subs)+s.Matrix([jp,jb])))
q=q.applyfunc(s.factor)
PhiB=s.factor(q[0]+s.diff(at*q[1],t))
PsiB=s.factor(ps-q[1]/s.sqrt(3))
assert s.diff(PhiB,ps)==0 and s.diff(PsiB,ps)==0
ward={s.diff(jp,t):-s.sqrt(3)*jb/t}
F=s.factor(PhiB.subs(ward))
S=s.factor(PsiB)
Fexpected=(t*t*s.diff(p,t,2)+2*t*s.diff(p,t))/(3*(1+k*k)) + s.sqrt(3)*jp/(2*t*(1+k*k)) -3*s.diff(jb,t)/(2*k*k*(1+k*k))
Sexpected=(k*k*p-t*s.diff(p,t))/(3*(1+k*k)) + s.sqrt(3)*jp/(2*t*(1+k*k)) +3*jb/(2*k*k*t*(1+k*k))
assert s.simplify(F-Fexpected)==0
assert s.simplify(S-Sexpected)==0
Q=s.diag(-s.Rational(1,3),-s.Rational(1,3),s.Rational(2,3))
amplitude=s.factor(k*k*(F+S)/(2*at**2))
W=amplitude*Q
assert s.simplify(s.trace(W))==0
assert s.simplify(s.trace(W*W)-s.Rational(2,3)*amplitude**2)==0
sigma,rho0=s.symbols("sigma rho0",real=True)
beta=1+(8*eta-3)*(1+k*k)/3
D=8*eta*(1+k*k)-3*k*k
p0=sigma/(4*k*k*beta)
steady={p:p0,s.diff(p,t):0,s.diff(p,t,2):0,
        jp:s.sqrt(3)*(k*k*sigma*t+4*rho0)/36,
        jb:-k*k*sigma*t/36,s.diff(jb,t):-k*k*sigma/36}
assert s.simplify(Fexpected.subs(steady)-
    (sigma/24+rho0/(6*t*(1+k*k))))==0
assert s.simplify(Sexpected.subs(steady)-
    (sigma/24+rho0/(6*t*(1+k*k))-sigma*(8*eta-3)/(12*D)))==0
print("PASS: exact general-history sourced Bardeen and Weyl transfer")
print("PASS: arbitrary scalar gauge cancels; steady source reproduces v15.719")
print("PHI_TRANSFER=",Fexpected)
print("PSI_TRANSFER=",Sexpected)
print("WEYL_STF_AMP=",amplitude)
