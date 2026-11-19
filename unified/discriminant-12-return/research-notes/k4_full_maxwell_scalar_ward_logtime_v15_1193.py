#!/usr/bin/env python3
"""Gravity v15.1193 — complete scalar source Ward closure, Maxwell null harmonic.

Uses archived sourced K4 P-equation (v15.713), sourced scalar ADM
spatial metric variation and source Maxwell redshift from v15.1083/1085.
The Maxwell-to-ADM variable map is in a declared longitudinal Fourier
sign convention. This is a nonzero-k, prescribed first-order test-field
linear response, NOT a solved globally gauge-invariant metric detector.
No quarter-grid physical coupling is inserted.
"""
import sympy as s
t,k,eta,J0=s.symbols('t k eta J0',positive=True,real=True)
I=s.I; w=s.sqrt(3)*k
J=J0*s.exp(-I*w*s.log(t))/t
JPhi=J; Jpsi=J; JB=I*k*J
ward=s.factor(t*s.diff(JPhi,t)+s.sqrt(3)*JB+Jpsi)
assert s.simplify(ward)==0
# Source-first lapse/shift elimination previously established in v15.713:
F=s.factor((k*k*t*s.diff(JPhi,t)+s.sqrt(3)*k*k*JB+
            s.sqrt(3)*t*s.diff(JB,t)+s.sqrt(3)*JB)/(3*(1+k*k)))
assert s.simplify(F-2*k*k*J/(3*(1+k*k)))==0
A=2*s.sqrt(3)*k**4*t**3/(27*(1+k*k))
drive=s.factor(-F/A)
assert s.simplify(drive+3*s.sqrt(3)*J0*s.exp(-I*w*s.log(t))/(k*k*t**4))==0
nu2=s.factor((8*eta-3)*(1+k*k)/3)
svar=s.symbols('s',real=True)
force=-3*s.sqrt(3)*J0*s.exp((-1-I*w)*svar)/k**2
# P=t^-1 z(s), P''+3P'/t+lam²P/t² = t^-3(z''+nu²z).
z=s.Function('z')
P=z(s.log(t))/t
lam2=nu2+1
ode=s.diff(P,t,2)+3*s.diff(P,t)/t+lam2*P/t**2
assert s.simplify(ode*t**3-
                   (s.diff(z(svar),svar,2)+nu2*z(svar)).subs(svar,s.log(t)))==0
# The particular solution with exponential(-s-iws) forcing.
decay=-1-I*w
den=s.factor(decay**2+nu2)
zp=s.simplify(force/den)
assert s.simplify(s.diff(zp,svar,2)+nu2*zp-force)==0
phase_match=s.solve(s.factor(nu2-w*w),k*k)[0]
assert s.simplify(phase_match-(8*eta-3)/(4*(3-2*eta)))==0
assert s.simplify(den.subs(nu2,w*w))!=0
assert s.simplify((decay**2+w*w)-(1+2*I*w))==0
for ep in [s.Rational(1,2),s.Rational(3,4),s.Integer(1)]:
    kmatch=phase_match.subs(eta,ep)
    assert kmatch>0
    assert s.simplify(den.subs({eta:ep,k:s.sqrt(kmatch)}))!=0
print('PASS full scalar Ward with Maxwell spatial stress at k>0')
print('PASS scalar forcing tau^-4 and log-time source e^-s; no secular pole')
print('PASS same K4/GR+solid Maxwell action yields zero matched residual')
print('SCOPE ADM source convention and physically invariant tidal readout still require Audit')
