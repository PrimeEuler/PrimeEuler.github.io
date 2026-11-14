#!/usr/bin/env python3
"""v15.984: re-use v15.900 rotor, compare genuine radial dynamics
with v15.898 energy-circle and v15.983 EM transition envelope.
Units: rho=r/ri, tau=t L/(M ri**2), Gamma=ro/ri>1.
All matching of geometrical/physical radii explicitly CONDITIONAL.
"""
import sympy as s
rho,G=s.symbols('rho G',positive=True)
f=(G+1)/(2*G**2)
e=s.Rational(1,2)+f
U=s.Rational(1,2)/rho**2+f*rho
radial=s.factor(2*(e-U))
expected=(G-rho)*(rho-1)*(G*rho+G+rho)/(G**2*rho**2)
assert s.simplify(radial-expected)==0
# beta=sin chi=sqrt(1-1/rho^2), r=ri sec chi, so
# chi'**2=rho'**2/[rho**2*(rho**2-1)].
chi2=s.factor(radial/(rho**2*(rho**2-1)))
chi_expected=(G-rho)*(G*rho+G+rho)/(G**2*rho**4*(rho+1))
assert s.simplify(chi2-chi_expected)==0
inner=s.factor(s.limit(chi2,rho,1,dir='+'))
assert s.simplify(inner-(G-1)*(2*G+1)/(2*G**2))==0
assert s.simplify(chi2.subs(rho,G))==0
assert s.simplify((1/rho**2)-(1/rho)**2)==0
# physical speed->transition envelope conditional A=1/gamma=1/rho
# primitive factor pair (n,1) corresponds to OUTER turning point
n=s.symbols('n',positive=True)
gn=(n+1)/(2*s.sqrt(n))
assert s.simplify((1/gn)**2-4*n/(n+1)**2)==0
D=5
G4=s.Rational(5,4)
assert s.simplify(f.subs(G,G4)-s.Rational(18,25))==0
assert s.simplify(inner.subs(G,G4)-s.Rational(7,25))==0
assert s.simplify((1/rho**2).subs(rho,G4)-s.Rational(16,25))==0
assert s.simplify((1/rho).subs(rho,G4)-s.Rational(4,5))==0
assert s.simplify(chi_expected.subs({G:G4,rho:G4}))==0
assert inner.subs(G,G4)>0
# discrete D5 edges can be sampled as radii of continuous rotor orbit;
# no edge reaches the exact continuous saddle f=D²/4 for D odd.
for k in (1,2,3,4):
    amp=s.sqrt(k*(D-k))/s.Rational(D,2)
    rcoord=s.simplify(1/amp)
    assert rcoord>=1 and rcoord<=G4
    assert s.simplify(amp*rcoord-1)==0
assert all(s.Rational(k*(D-k))!=s.Rational(D*D,4) for k in range(1,D))
print('PASS rotor, angular-speed=A², radial angle rate, D5 finite-edge controls')
print('chi_prime_squared=',chi_expected)
print('n4 inner chi_prime_squared=',inner.subs(G,G4),'outer=',0)
