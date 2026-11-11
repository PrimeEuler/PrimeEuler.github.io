#!/usr/bin/env python3
"""v15.722: coasting K4 V/T sourced Euler modes with zero dynamical initial data.

Same v15.716 covariantly conserved Fourier-stress template. The source
is present on tau>=tau0 with sharp initial preparation; any discontinuous
shift contact at onset is an idealization, not a smooth physical pulse.
Electric Weyl vector/tensor formulas are the local conformal results of
v15.721. No full localized matter action or instrument is selected.
"""
import sympy as s
t,t0,k,eta=s.symbols("tau tau0 k eta",positive=True,real=True)
Q=s.symbols("Q",nonzero=True)
D=4+3*k*k
nu=s.symbols("nu",positive=True,real=True)
beta=1+nu*nu
f0=-3*s.I*Q/(eta*k*D)
L=s.log(t/t0)
f=s.simplify(f0*(1-t0/t*(s.cos(nu*L)+s.sin(nu*L)/nu)))
ODE=s.diff(f,t,2)+3*s.diff(f,t)/t+beta*f/t**2
assert s.simplify(ODE-beta*f0/t**2)==0
assert s.simplify(f.subs(t,t0))==0
assert s.simplify(s.diff(f,t).subs(t,t0))==0
assert s.simplify((beta*f0).subs(nu**2,2*eta*D/3-1)+2*s.I*Q/k)==0
b=4*t/(s.sqrt(3)*D)
Bpart=-s.I*s.sqrt(3)*k*Q/D
B=Bpart+b*s.diff(f,t)
assert s.simplify(B.subs(t,t0)-Bpart)==0
assert s.simplify(s.expand(s.diff(B,t).subs(t,t0)).subs(
    nu**2,2*eta*D/3-1)-b.subs(t,t0)*(-2*s.I*Q/(k*t0**2)))==0
a=t/s.sqrt(3)
E=-s.I*k*s.diff(B,t)/(4*a)
assert s.simplify(s.expand(E.subs(t,t0)).subs(
    nu**2,2*eta*D/3-1)+2*Q/(D*t0**2))==0
assert s.simplify(E.subs(Q,0))==0
mag=-k*k*B/(4*a*a)
assert s.simplify(mag.subs(t,t0)-(-k*k*Bpart/
    (4*(t0/s.sqrt(3))**2)))==0
for e in (s.Rational(3,8),s.Rational(3,4),s.Rational(3,2)):
    for kk in (s.Rational(1,2),s.Integer(1),s.Integer(3)):
        assert 2*e*(4+3*kk**2)/3-1>0
kappa,QT=s.symbols("kappa Q_T",positive=True,real=True)
nuT=s.symbols("nu_T",positive=True,real=True)
mcoef=3*k*k+s.Rational(8,3)*eta
gamma0=-2*kappa*QT/mcoef
gamma=s.factor(gamma0*(1-t0/t*(
    s.cos(nuT*L)+s.sin(nuT*L)/nuT)))
Lt=s.simplify(s.diff(gamma,t,2)+3*s.diff(gamma,t)/t+
    (1+nuT**2)*gamma/t**2)
assert s.simplify(Lt-(1+nuT**2)*gamma0/t**2)==0
assert s.simplify(gamma.subs(t,t0))==0
assert s.simplify(s.diff(gamma,t).subs(t,t0))==0
assert s.simplify(s.expand(Lt).subs(nuT**2,mcoef-1)+
    2*kappa*QT/t**2)==0
ET=(t*t*s.diff(gamma,t,2)+t*s.diff(gamma,t)-
    3*k*k*gamma)/(12*a*a)
assert s.simplify(s.expand(ET.subs(t,t0)).subs(
    nuT**2,mcoef-1)+kappa*QT/(6*a.subs(t,t0)**2))==0
print("PASS: vector retarded Euler and zero displacement/velocity data")
print("PASS: vector electric Weyl at tau0+ = -2Q/(D tau0^2), nonzero")
print("PASS: tensor retarded Euler and nonzero electric Weyl at tau0+")
