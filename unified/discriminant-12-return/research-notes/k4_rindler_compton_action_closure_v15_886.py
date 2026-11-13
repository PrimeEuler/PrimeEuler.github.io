#!/usr/bin/env python3
"""v15.886: test conditional Rindler/Compton length weld.

Hypothesis L_R=c²/a = lambda_Cbar=hbar/(mc) fixes
 a_*=mc³/hbar, c/a_*=hbar/(mc²), omega_C=mc²/hbar.
This is a consistent conditional identification, NOT a consequence
of tangency or quantization. A dimensionless arbitrary ratio rho
of the two lengths survives every previous action/tangency identity:
 a=mc³/(rho*hbar). Therefore continuous frequency ambiguity remains.
"""
import sympy as s
m,hbar,c,a,rho,beta=s.symbols('m hbar c a rho beta',positive=True)
LR=c*c/a
LC=hbar/(m*c)
a_star=s.solve(s.Eq(LR,LC),a)[0]
assert s.simplify(a_star-m*c**3/hbar)==0
omegaC=m*c*c/hbar
assert s.simplify(c/a_star-1/omegaC)==0
assert s.simplify((LR.subs(a,a_star))/LC-1)==0
# General arbitrary weld LR=rho LC
arho=s.solve(s.Eq(LR,rho*LC),a)[0]
assert s.simplify(arho-m*c**3/(rho*hbar))==0
assert s.simplify((LR.subs(a,arho))/LC-rho)==0
v1=s.Rational(1,4);v2=s.Rational(1,2)
fn=s.simplify(beta/s.sqrt(1-beta**2))
tgap=s.simplify((c/a)*(fn.subs(beta,v2)-fn.subs(beta,v1)))
gap_coeff=s.simplify(tgap*a/c)
assert s.simplify(tgap.subs(a,arho)-rho*gap_coeff/omegaC)==0
assert s.simplify(tgap.subs(a,a_star)-gap_coeff/omegaC)==0
assert s.simplify((tgap.subs(a,2*a_star))/(tgap.subs(a,a_star))-s.Rational(1,2))==0
# Circle action J_phase=E/omega; Compton energy is supplied E=mc².
E=m*c*c
assert s.simplify(E/omegaC-hbar)==0
assert s.simplify((E/(2*omegaC))*2-hbar)==0
# No derivation of rho=1: rho is an unconstrained dimensionless input.
assert s.simplify(s.diff(arho,rho))!=0
print('PASS conditional LR=LC gives a=mc^3/hbar, omega=mc^2/hbar')
print('PASS node gap coefficient',gap_coeff)
print('PASS arbitrary LR/LC=rho survives, with node time multiplied by rho')
print('NEGATIVE equality LR=LC is an additional postulate and uses mass')
