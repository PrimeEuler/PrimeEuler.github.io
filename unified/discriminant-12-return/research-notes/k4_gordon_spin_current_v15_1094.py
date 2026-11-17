#!/usr/bin/env python3
"""Cone Gravity v15.1094: localized Gordon spin magnetization current.

Standard Pauli/Dirac nonrelativistic current, not a novel Cone interaction.
A spin-up, real wavepacket with no external vector potential has zero
convection current but a nonzero magnetization current and full g=2 moment.
"""
import sympy as s
x,y,z,L,m,hbar,q=s.symbols('x y z L m hbar q', real=True)
rho=s.exp(-(x*x+y*y+z*z)/L**2)/(s.pi**s.Rational(3,2)*L**3)
spin_coeff=q*hbar/(2*m)
J=s.Matrix([spin_coeff*s.diff(rho,y),-spin_coeff*s.diff(rho,x),s.S.Zero])
assert s.simplify(s.diff(J[0],x)+s.diff(J[1],y)+s.diff(J[2],z))==0
normal=s.integrate(rho,(x,-s.oo,s.oo),(y,-s.oo,s.oo),(z,-s.oo,s.oo),conds='none')
assert s.simplify(normal-1)==0
x2=s.integrate(x*x*rho,(x,-s.oo,s.oo),(y,-s.oo,s.oo),(z,-s.oo,s.oo),conds='none')
y2=s.integrate(y*y*rho,(x,-s.oo,s.oo),(y,-s.oo,s.oo),(z,-s.oo,s.oo),conds='none')
assert s.simplify(x2-L*L/2)==0
assert s.simplify(y2-L*L/2)==0
mu_z=s.simplify(spin_coeff*(x2+y2)/L**2)
assert s.simplify(mu_z-q*hbar/(2*m))==0
c=s.symbols('c',positive=True)
rloop=hbar/(2*m*c)
mu_loop=s.simplify(q*c*rloop/2)
assert s.simplify(mu_loop-q*hbar/(4*m))==0
assert s.simplify(mu_z/mu_loop-2)==0
assert s.simplify(mu_z-mu_loop-mu_loop)==0
print('PASS Gaussian Gordon spin current is divergence-free and has full Dirac mu without convection')
print('mu_spin=',mu_z,'mu_loop=',mu_loop,'ratio=',s.simplify(mu_z/mu_loop))
