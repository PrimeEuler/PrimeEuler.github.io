#!/usr/bin/env python3
"""Gravity v15.1222 — compact Maxwell Cauchy jets expose incomplete E-fixed scalar ADM source.
The pressure-corrected source-to-P and Bardeen equations are those from archived
v15.728/v15.729. This reproducer does NOT certify their physical applicability
to anisotropically stressed Maxwell data without the longitudinal E-shear equation.
"""
import sympy as s
t=s.symbols('tau',positive=True)
k,eta,J=s.symbols('k eta J',positive=True,real=True)
p=s.Function('p')(t); jp=s.Function('jp')(t)
js=s.Function('js')(t); jb=s.Function('jb')(t)
beta=(8*eta*(1+k*k)-3*k*k)/3
force=3*s.sqrt(3)*js/(2*k*k*t**3)-9*(t*s.diff(jb,t)+jb)/(2*k**4*t**3)
pdd=-3*s.diff(p,t)/t-beta*p/t**2+force
pddd=s.diff(pdd,t).subs(s.diff(p,t,2),pdd)
Phi=(t*t*s.diff(p,t,2)+2*t*s.diff(p,t))/(3*(1+k*k))+s.sqrt(3)*(jp+js)/(2*t*(1+k*k))-3*s.diff(jb,t)/(2*k*k*(1+k*k))
Psi=(k*k*p-t*s.diff(p,t))/(3*(1+k*k))+s.sqrt(3)*jp/(2*t*(1+k*k))+3*jb/(2*k*k*t*(1+k*k))
R=-3*k*k*Phi/t**2
Araw=s.diff(Psi,t,2)+2*s.diff(Psi,t)/t+s.diff(Phi,t)/t
Aiso=Araw+R/3
# Initial compact Maxwell B=0: conformal R'=0, Tii'=0;
# R''=-k²R; a=tau/sqrt3. Differentiated source Ward then gives
# JB'(1)=sqrt3*k² J, while Jphi=Jpsi=J, J_B=0, Jphi'=Jpsi'=-J.
jet={t:1,p:0,s.diff(p,t):0,jp:J,js:J,jb:0,
     s.diff(jp,t):-J,s.diff(js,t):-J,
     s.diff(jb,t):s.sqrt(3)*k*k*J}
def initial(expr):
    return s.factor(s.simplify(expr.subs(s.diff(p,t,3),pddd)
                                     .subs(s.diff(p,t,2),pdd)
                                     .subs(jet)))
acc=initial(pdd); phi=initial(Phi); psi=initial(Psi)
stf=initial(R); iso=initial(Aiso)
assert s.simplify(acc+3*s.sqrt(3)*J/k**2)==0
assert s.simplify(phi+s.sqrt(3)*J*(k*k+2)/(2*k*k*(1+k*k)))==0
assert s.simplify(psi-s.sqrt(3)*J/(2*(1+k*k)))==0
assert s.simplify(stf-3*s.sqrt(3)*J*(k*k+2)/(2*(1+k*k)))==0
assert s.simplify(iso-s.sqrt(3)*J*(k*k-4)/(2*(1+k*k)))==0
ratio=s.factor(iso/(s.sqrt(3)*J))
assert s.simplify(ratio.subs(k,2))==0
assert s.simplify(s.diff(ratio,k)-5*k/(1+k*k)**2)==0
# Einstein R00 trace: homogeneous-degree-one K4 solid has rho+sum p=0;
# Maxwell has zero stress trace. So its physical normalized R00/3
# must be proportional to rho, without a k-dependent multiplier.
assert s.simplify(iso-s.sqrt(3)*J)!=0
assert s.simplify(iso+s.sqrt(3)*J)!=0
rho,a=s.symbols('rho a',positive=True)
Tij=s.diag(0,0,rho)
pi_scalar=s.simplify(Tij[2,2]-s.trace(Tij)/3)
assert pi_scalar==2*rho/3
# Gauge-fixed-away longitudinal Ezz mode would receive stress source
# of magnitude k² a³ Tzz: cannot be set to zero for k>0.
JE=-k*k*a**3*rho
assert s.simplify(JE)!=0
print('PASS initial Maxwell conservation jet and truncated ADM calculation')
print('pdd=',acc,'Phi_N=',phi,'Psi_N=',psi)
print('tracefree coefficient=',stf)
print('isotropic coefficient=',iso)
print('ratio to proposed positive-energy Einstein trace=',ratio)
print('OBSTRUCTION at k=2: isotropic coefficient zero with rho>0')
print('OPEN full scalar spatial-shear source and physical K4 tidal response')
