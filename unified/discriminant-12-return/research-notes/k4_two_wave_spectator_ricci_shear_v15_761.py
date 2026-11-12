#!/usr/bin/env python3
"""v15.761 canonical KG two-wave source: exact spectator Ricci tidal shear.

The positive spatial Fourier coefficient at p+q of a real scalar gradient
cross-stress is computed from the on-shell cos modes at tau=1.
Tracefree arm differencing removes isotropic stress but not anisotropic
Ricci. This is only the spectator field's contribution, NOT the total
K4 elastic-solid Ricci or a calibrated detector signal.
"""
import sympy as s
t=s.symbols('tau',positive=True)
a=t/s.sqrt(3)
p=s.Matrix([2,0,0]);q=s.Matrix([0,0,1]);k=p+q
n=k/s.sqrt((k.T*k)[0]);e=s.Matrix([1,0,-2])/s.sqrt(5)
b=s.Matrix([0,1,0])
u=(n+e)/s.sqrt(2);v=(n-e)/s.sqrt(2)
Ds=[n*n.T-e*e.T,e*e.T-b*b.T,u*u.T-v*v.T]
A=s.cos(s.sqrt(11)*s.log(t))/t
B=s.cos(s.sqrt(2)*s.log(t))/t
# For chi=A cos(p.x)+B cos(q.x), each positive mode has 1/2.
# The positive sum-frequency cross-stress is -AB(pq^T+qp^T)/4a^2.
S=p*q.T+q*p.T
Pi=-A*B*S/(4*a*a)
P1=Pi.subs(t,1)
projs=s.Matrix([s.simplify(s.trace(D*P1)) for D in Ds])
assert projs==s.Matrix([-s.Rational(12,5),s.Rational(6,5),s.Rational(9,5)])
kappa=s.symbols('kappa',real=True)
ricci=-kappa*projs/2
assert ricci==s.Matrix([s.Rational(6,5)*kappa,-s.Rational(3,5)*kappa,
                       -s.Rational(9,10)*kappa])
assert (Pi+A*B*S/(4*a*a)).applyfunc(s.simplify)==s.zeros(3)
print('PASS: on-shell canonical two-wave spectator anisotropic Ricci shear')
print('D:T_spectator at tau=1',list(projs))
print('full-Riemann minus Weyl spectator correction',list(ricci))
print('CAUTION: requires total K4 solid stress and metric perturbations')
