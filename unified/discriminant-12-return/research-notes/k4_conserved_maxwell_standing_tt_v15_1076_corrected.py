#!/usr/bin/env python3
"""Gravity v15.1076 corrected, authoritative Maxwell standing-wave source reproducer.

Supersedes the two sign-incorrect Maxwell assertions in k4_conserved_maxwell_standing_tt_v15_1076.py
(commit 28437f135...). Conserved source and stress formulas were already correct.
"""
import sympy as s
t,z,k,E=s.symbols('t z k E', positive=True, real=True)
Ex=-E*s.sin(k*z)*s.cos(k*t)
By=E*s.cos(k*z)*s.sin(k*t)
energy=(Ex**2+By**2)/2
flux=Ex*By
plus=(By**2-Ex**2)/2
# Faraday: ∂t B_y = -∂z E_x.
# Ampere: ∂t E_x = -∂z B_y.
assert s.trigsimp(s.diff(By,t)+s.diff(Ex,z))==0
assert s.trigsimp(s.diff(Ex,t)+s.diff(By,z))==0
assert s.trigsimp(s.diff(energy,t)+s.diff(flux,z))==0
assert s.trigsimp(s.diff(flux,t)+s.diff(energy,z))==0
assert s.trigsimp(plus-E**2*(s.cos(2*k*z)-s.cos(2*k*t))/4)==0
assert s.trigsimp(flux.subs(z,0))==0
assert s.trigsimp(flux.subs(z,s.pi/k))==0
mu,F=s.symbols('mu F',positive=True,real=True)
omega=s.sqrt(4*k*k+mu*mu)
h=F/omega**2*(1-s.cos(omega*t))
assert s.simplify(s.diff(h,t,2)+omega**2*h-F)==0
assert h.subs(t,0)==0
assert s.diff(h,t).subs(t,0)==0
print('PASS source-free Maxwell equations; conserved stress; plus harmonics; wall energy flux; conditional retarded mode.')
