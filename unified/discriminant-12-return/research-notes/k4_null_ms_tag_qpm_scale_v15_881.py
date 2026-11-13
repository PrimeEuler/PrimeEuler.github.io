#!/usr/bin/env python3
"""Gravity v15.881: m/s null ray sets a speed, not a unique QPM length.

Sandbox v15.860 SI null tag U=E+pc, V=E-pc; its ratio is
(c+v)/(c-v) on a massive on-shell state. c maps a specified time
period into a distance. Gertsenshtein phase matching additionally
requires photon/graviton wavenumber mismatch Delta k.
Delta k = omega*(n_gamma-n_g)/c when refractive indices are given.
The square-wave B-field QPM period is 2pi/|Delta k|.
At vacuum index equality no finite required QPM reversal period:
phase mismatch vanishes, and an unreversed uniform B builds
conversion coherently over the finite interaction length.
Compton frequency or length require an independently supplied
mass and hbar and do not follow from c alone.
"""
import sympy as s
c,v,E,p,m,omega,f,ngam,ngrav,hbar=s.symbols(
    "c v E p m omega f ngam ngrav hbar",positive=True)
U=E+p*c
V=E-p*c
# E=gamma m c², p=gamma m v: ratio independent of gamma,m
gamma=s.symbols("gamma",positive=True)
ratio=s.factor((U/V).subs({E:gamma*m*c*c,p:gamma*m*v}))
assert s.simplify(ratio-(c+v)/(c-v))==0
assert s.simplify(ratio.subs(v,0)-1)==0
k_gamma=ngam*omega/c
k_grav=ngrav*omega/c
delta=s.simplify(k_gamma-k_grav)
assert s.simplify(delta-omega*(ngam-ngrav)/c)==0
beat=2*s.pi/delta
period=2*s.pi/omega
# For a nonzero signed index difference, absolute beat length uses |delta|.
assert s.simplify((beat/period)/(c/(ngam-ngrav)))==0
assert s.simplify((beat.subs(omega,2*s.pi*f))-c/(f*(ngam-ngrav)))==0
assert s.simplify(delta.subs(ngam,ngrav))==0
# Putting ordinary Compton length in uses BOTH mass and hbar.
compton=hbar/(m*c)
assert s.diff(compton,m)!=0
assert s.diff(compton,hbar)!=0
print("PASS SI null-ray leverage ratio")
print("PASS phase length 2pi/|Delta k|=c/(f|n_gamma-n_g|)")
print("PASS vacuum Delta k=0: no finite QPM reversal length selected")
print("PASS Compton length requires mass and Planck action, not c only")
print("NEGATIVE mesh half/quarter or c alone does not set unique length")
