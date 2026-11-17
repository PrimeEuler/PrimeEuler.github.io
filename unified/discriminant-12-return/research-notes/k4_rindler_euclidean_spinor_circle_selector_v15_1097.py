#!/usr/bin/env python3
"""Gravity v15.1097: Euclidean Rindler circle, parabola focus, spinor sign and free scale.

Conventional flat-space Rindler + Dirac spin structure; the Compton/Rindler
scale matching is a conditional identification, not a Cone dynamics selector.
"""
import sympy as s
c,a,m,hbar,kB,rho=s.symbols('c a m hbar k_B rho',positive=True,real=True)
R=c*c/a
lam=hbar/(m*c)
wC=m*c*c/hbar
wZ=2*wC
focus=R/2
rZ=lam/2
arho=m*c**3/(rho*hbar)
assert s.simplify((focus/rZ).subs(a,arho)-rho)==0
assert s.simplify((R/lam).subs(a,arho)-rho)==0
period=2*s.pi*c/a
wR=a/c
assert s.simplify(period*wR-2*s.pi)==0
assert s.simplify((wZ/wR).subs(a,arho)-2*rho)==0
TU=hbar*a/(2*s.pi*c*kB)
assert s.simplify((kB*TU/(m*c*c)).subs(a,arho)-1/(2*s.pi*rho))==0
boltz=s.exp(-m*c*c/(kB*TU))
assert s.simplify(boltz.subs(a,arho)-s.exp(-2*s.pi*rho))==0
r,theta=s.symbols('r theta',real=True)
X=r*s.cos(theta)
Y=r*s.sin(theta)
assert s.simplify(s.diff(X,r)**2+s.diff(Y,r)**2-1)==0
assert s.simplify(s.diff(X,theta)**2+s.diff(Y,theta)**2-r*r)==0
assert s.simplify(s.diff(X,r)*s.diff(X,theta)+s.diff(Y,r)*s.diff(Y,theta))==0
spin_half=s.diag(s.exp(s.I*theta/2),s.exp(-s.I*theta/2))
assert (spin_half.subs(theta,theta+2*s.pi)+spin_half).applyfunc(s.simplify)==s.zeros(2)
for n in (s.Rational(1,2),1,2,3):
 assert s.simplify((focus/rZ).subs(a,arho).subs(rho,n)-n)==0
print('PASS: Rindler Euclidean regular circle, no rho selection, spinor -1, Unruh gap ratio')
print('f/r_ZB=rho, omega_ZB/omega_R=2rho, kB TU/(mc^2)=1/(2pi rho)')
