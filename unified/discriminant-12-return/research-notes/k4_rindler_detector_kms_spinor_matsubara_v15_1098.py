#!/usr/bin/env python3
"""Gravity v15.1098: accelerated detector KMS rate ratio and Dirac thermal modes.

Long-time stationary ideal Unruh-DeWitt scalar detector with prescribed gap
Delta E=m c^2; this is a comparator, not a self-consistent Dirac electron.
"""
import sympy as s
rho,c,a,m,hbar,kB=s.symbols('rho c a m hbar kB',positive=True,real=True)
Omega=m*c*c/hbar
alpha=a/c
TU=hbar*a/(2*s.pi*c*kB)
R=c*c/a
lam=hbar/(m*c)
assert s.simplify((R/lam) - Omega/alpha)==0
r=s.exp(-2*s.pi*Omega/alpha)
assert s.simplify(r.subs(a,m*c**3/(rho*hbar))-s.exp(-2*s.pi*rho))==0
assert s.simplify(s.exp(-m*c*c/(kB*TU))-r)==0
# Standard massless 3+1 scalar eternally and uniformly accelerated detector.
up=s.factor(Omega/(2*s.pi)/(s.exp(2*s.pi*Omega/alpha)-1))
down=s.factor(Omega/(2*s.pi)/(1-s.exp(-2*s.pi*Omega/alpha)))
assert s.simplify(up/down-r)==0
assert s.simplify(down-up-Omega/(2*s.pi))==0
n=s.symbols('n',integer=True,nonnegative=True)
beta_time=2*s.pi/alpha
matsubara=s.simplify((2*n+1)*s.pi/beta_time)
assert s.simplify(matsubara-(n+s.Rational(1,2))*alpha)==0
assert s.simplify((matsubara/Omega).subs(a,m*c**3/(rho*hbar))-(n+s.Rational(1,2))/rho)==0
# Equating a Euclidean Matsubara frequency to the rest-energy gap would
# be an ADDITIONAL chosen condition, and different n choose different rho.
assert s.simplify((Omega-matsubara).subs(a,m*c**3/(rho*hbar)).subs(rho,n+s.Rational(1,2)))==0
for rv in (s.Rational(1,4),s.Rational(1,2),s.S.One,s.Rational(2,1)):
    assert s.exp(-2*s.pi*rv)>0
assert s.simplify(s.diff(s.exp(-2*s.pi*rho),rho)+2*s.pi*s.exp(-2*s.pi*rho))==0
print('PASS accelerated scalar detector detailed balance and Dirac Matsubara frequencies')
print('rate ratio=',s.simplify(r.subs(a,m*c**3/(rho*hbar))))
print('fermionic thermal Matsubara omega_n / omega_C=',s.simplify((matsubara/Omega).subs(a,m*c**3/(rho*hbar))))
print('rho=1 rate ratio numeric=',s.N(s.exp(-2*s.pi),12))
