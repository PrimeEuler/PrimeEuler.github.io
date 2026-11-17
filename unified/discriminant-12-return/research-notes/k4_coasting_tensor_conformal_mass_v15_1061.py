#!/usr/bin/env python3
"""v15.1061 second reproducer: conformal-time K4 tensor effective mass."""
import sympy as s
eta,tau0,zeta,k=s.symbols("eta tau0 zeta k",positive=True,real=True)
a=tau0*s.exp(eta/s.sqrt(3))/s.sqrt(3)
tau=tau0*s.exp(eta/s.sqrt(3))
H=1/tau
mt2=s.Rational(8,3)*zeta*H**2
mass=s.simplify(a*a*mt2-s.diff(a,eta,2)/a)
assert s.simplify(mass-(8*zeta-3)/9)==0
assert mass.subs(zeta,s.Rational(3,8))==0
assert mass.subs(zeta,s.Rational(3,2))==1
assert s.simplify(mt2.subs(zeta,s.Rational(3,8))-H**2)==0
# friction removal h=psi/a in the h''+2a'/a h'+(k²+a² mt²)h equation
f=s.Function("psi")(eta)
h=f/a
eq=s.diff(h,eta,2)+2*s.diff(a,eta)/a*s.diff(h,eta)+(k*k+a*a*mt2)*h
assert s.simplify(a*eq-(s.diff(f,eta,2)+(k*k+mass)*f))==0
print("PASS: mu_eff²=(8*zeta-3)/9; zero at zeta=3/8, positive above; physical m_T²=H² at boundary")
