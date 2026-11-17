#!/usr/bin/env python3
"""Gravity v15.1076: conserved Maxwell standing wave and conditional tensor response.

No wall source / 3+1 ADM solution claimed. Units c=epsilon0=mu0=1.
"""
import sympy as s
t,z,k,E=s.symbols('t z k E', positive=True, real=True)
Ex=-E*s.sin(k*z)*s.cos(k*t)
By=E*s.cos(k*z)*s.sin(k*t)
energy=(Ex**2+By**2)/2
flux=Ex*By
plus=(By**2-Ex**2)/2
assert s.trigsimp(s.diff(energy,t)+s.diff(flux,z))==0
assert s.trigsimp(s.diff(flux,t)+s.diff(energy,z))==0
assert s.trigsimp(plus-E**2*(s.cos(2*k*z)-s.cos(2*k*t))/4)==0
assert s.trigsimp(flux.subs(z,0))==0
assert s.trigsimp(flux.subs(z,s.pi/k))==0
assert s.trigsimp(s.diff(Ex,z)-s.diff(By,t))==0
assert s.trigsimp(s.diff(By,z)-s.diff(Ex,t))==0
# Static spatial k=2k linear tensor mode response for a prescribed normalized drive F.
mu,F=s.symbols('mu F',positive=True,real=True)
omega=s.sqrt(4*k*k+mu*mu)
h=F/omega**2*(1-s.cos(omega*t))
assert s.simplify(s.diff(h,t,2)+omega**2*h-F)==0
assert h.subs(t,0)==0
assert s.diff(h,t).subs(t,0)==0
# No sector or q2 ladder labels are introduced by these sourced field equations.
print('PASS: source-free cavity Maxwell equations, local stress conservation,')
print('      exact plus-stress harmonics, zero wall energy flux, conditional retarded drive')
print('Pi_plus = E^2/4 [cos(2 k z)-cos(2 k t)]')
