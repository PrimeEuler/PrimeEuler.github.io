#!/usr/bin/env python3
"""v15.717: conserved FLRW source maps to K4 ADM scalar Ward and forced P.

Source Fourier amplitude exp(+ikz) pairs with scalar metric Fourier
amplitude exp(-ikz). The v14.935 scalar shift potential B obeys
delta g_0z=-a partial_z B=+ik a B on this metric mode. Consequently
J_Phi=a^3 T^{00}, J_B=ik a^4 T^{0z}.
This is a conserved stress template, not a derived localized matter action.
"""
import sympy as s
t,k,sigma,rho0=s.symbols('tau k sigma rho0',positive=True,real=True)
a=t/s.sqrt(3);H=1/t
nz2=s.Rational(1,6)
qzz=sigma*(nz2-s.Rational(1,3))
rho=-3*k*k*qzz/(2*t*t)+rho0/t**3
uz=-s.I*k*qzz/(2*t)
T0z=uz/a**2
assert s.simplify(s.diff(rho,t)+3*H*rho+s.I*k*T0z)==0
JP=s.simplify(a**3*rho)
JB=s.simplify(s.I*k*a**4*T0z)
ward=s.simplify(t*s.diff(JP,t)+s.sqrt(3)*JB)
assert ward==0
assert s.simplify(ward-t*a**3*(s.diff(rho,t)+3*H*rho+s.I*k*T0z))==0
Q0=sigma*s.diag(-s.Rational(1,3),-s.Rational(1,3),s.Rational(2,3))
assert Q0.trace()==0
assert s.simplify(a**3*T0z*(s.I*k*a)-JB)==0
assert s.simplify(a**3*rho-JP)==0
eta=s.symbols('eta',positive=True,real=True)
beta=1+(8*eta-3)*(1+k*k)/3
forcing=s.simplify(-9*(t*s.diff(JB,t)+JB)/(2*k**4*t**3))
assert s.simplify(forcing-sigma/(4*k*k*t*t))==0
part=sigma/(4*k*k*beta)
assert s.simplify(s.diff(part,t,2)+3*s.diff(part,t)/t+beta*part/t**2-forcing)==0
print('PASS: covariant source induces exact scalar forcing sigma/(4 k^2 tau^2)')
print('PASS: P_part=sigma/(4 k^2 beta), physical source matter action remains open')
print('PASS: ADM scalar Ward equals FLRW energy conservation for tracefree source')
print('J_Phi=',JP,'J_B=',JB)
