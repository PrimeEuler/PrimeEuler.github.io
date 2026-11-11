#!/usr/bin/env python3
"""v15.713: exact coasting K4 sourced scalar Ward-like constraint and P equation.

Runs v15.712 reconstruction of the REAL archived v14.935 scalar quadratic
action, adds formal J_Phi Phi+J_B B before lapse/shift elimination, retains
a(t)=t/sqrt(3) in EL differentiation. Formal J are not yet physically
covariant conserved stress coefficients. For every k>0:
  E_psi = -tau J_Phi_dot-sqrt(3)J_B =0;
  Pddot+3/tau Pdot +[8 eta(1+k^2)-3k^2]/(3tau^2)P
      = -9(tau J_B_dot+J_B)/(2 k^4 tau^3).
The archived v14.935 source-free scalar_statespace.py alpha=-C01/C00
attempts 0/0 since its exact source-free psi EL equation is identically 0.
This does NOT change the correctly reproduced P-mode dispersion.
"""
import runpy
from pathlib import Path
import sympy as s

src=runpy.run_path(str(Path(__file__).with_name("k4_full_scalar_sourced_mixed_v15_712.py")))
L,H,d=[src[name] for name in ("L","H","d")]
a,adot,C,kappa,eta,k=[src[name] for name in ("a","adot","C","kappa","eta","k")]
Phi,B,psi,P,psi_t,P_t=[src[name] for name in ("Phi","B","psi","P","psi_t","P_t")]
JP,JB=s.symbols("J_Phi J_B")
J=s.Matrix([JP,JB])
Lred=L.subs({Phi:0,B:0})-s.Rational(1,2)*((d+J).T*H.inv()*(d+J))[0]
t=s.symbols("tau",positive=True)
ps=s.Function("psi")(t);p=s.Function("P")(t)
jp=s.Function("J_Phi")(t);jb=s.Function("J_B")(t)
Lcoast=s.cancel(Lred.subs({a:t/s.sqrt(3),adot:1/s.sqrt(3),C:1,kappa:1}))
Lf=s.expand(Lcoast.subs({psi:ps,P:p,psi_t:s.diff(ps,t),P_t:s.diff(p,t),
                           JP:jp,JB:jb},simultaneous=True))
def EL(q):
    return s.diff(s.diff(Lf,s.diff(q,t)),t)-s.diff(Lf,q)
Epsi=EL(ps);EP=EL(p)
ward=-t*s.diff(jp,t)-s.sqrt(3)*jb
assert s.simplify(Epsi-ward)==0
assert s.simplify(Epsi.subs({jp:0,jb:0}).doit())==0
A=s.factor(s.diff(EP,s.diff(p,t,2)))
Bcoef=s.factor(s.diff(EP,s.diff(p,t)))
Ccoef=s.factor(s.diff(EP,p))
assert s.simplify(A-2*s.sqrt(3)*k**4*t**3/(27*(k*k+1)))==0
assert s.simplify(Bcoef/A-3/t)==0
assert s.simplify(Ccoef/A-(8*eta*(k*k+1)-3*k*k)/(3*t*t))==0
F=s.factor(EP-A*s.diff(p,t,2)-Bcoef*s.diff(p,t)-Ccoef*p)
expectedF=(k*k*t*s.diff(jp,t)+s.sqrt(3)*k*k*jb
          +s.sqrt(3)*t*s.diff(jb,t)+s.sqrt(3)*jb)/(3*(k*k+1))
assert s.simplify(F-expectedF)==0
forced=s.factor((F/A).subs(s.diff(jp,t),-s.sqrt(3)*jb/t))
assert s.simplify(forced-9*(t*s.diff(jb,t)+jb)/(2*k**4*t**3))==0
assert s.simplify(s.diff(Epsi.subs({jp:0,jb:0}),ps))==0
assert s.simplify(s.diff(Epsi.subs({jp:0,jb:0}),p))==0
print("PASS: exact sourced scalar psi constraint / source consistency")
print("PASS: time-dependent coasting scalar P forced ODE and v14.935 dispersion")
print("E_psi=",s.factor(Epsi))
print("P forcing after Ward:",s.factor(forced))
print("AUDIT ALERT: v14.935 scalar_statespace.py psi=alpha P attempts 0/0")
