#!/usr/bin/env python3
"""v15.688: weld/power-map physical-length and temporal-selector audit.

The v14.904 weld fixes dimensionless member scales h=2q from dimensionless
pair quanta q.  This script shows exactly what extra data are required before
h_G/h_EM=1/2 can become a physical wavelength ratio and hence a 2:1 clock.

Let ell_s be the physical length represented by one normalized coordinate unit
in sector s and v_s its propagation speed.  Then
    lambda_s = ell_s h_s
and frequency is proportional to v_s/lambda_s.
"""
import sympy as s

ellG,ellE,vG,vE,hbar,pG,pE=s.symbols(
    "ell_G ell_EM v_G v_EM hbar p_G p_EM", positive=True, real=True
)

qE=s.Rational(1,2)
qG=s.Rational(1,4)
hE=2*qE
hG=2*qG
assert hE==1 and hG==s.Rational(1,2)

lambdaE=s.simplify(ellE*hE)
lambdaG=s.simplify(ellG*hG)
freq_ratio=s.simplify((vG/lambdaG)/(vE/lambdaE))
assert freq_ratio==2*(vG/vE)*(ellE/ellG)

# Desired primary parametric ratio 2 occurs iff the missing physical embedding
# satisfies (vG/vE)*(ellE/ellG)=1.  The dimensionless weld does not fix it.
constraint=s.simplify(freq_ratio/2)
assert constraint==(vG/vE)*(ellE/ellG)

# If a common physical coordinate unit and common speed are separately imposed,
# the desired factor two follows.
assert s.simplify(freq_ratio.subs({ellG:ellE,vG:vE})-2)==0

# v14.774 conditional action-length calibration ell=hbar/p introduces a
# momentum scale rather than eliminating it.
action_ratio=s.simplify(freq_ratio.subs({ellG:hbar/pG,ellE:hbar/pE}))
assert action_ratio==2*(vG/vE)*(pG/pE)

# The radial weld shift is dimensionless and independent of ell_s.
n=s.symbols("n", positive=True)
rE=s.log(hE**2*n)
rG=s.log(hG**2*n)
assert s.simplify(s.expand_log(rG-rE,force=True)+s.log(4))==0

print("weld scales: h_EM =",hE,", h_G =",hG)
print("physical frequency ratio =",freq_ratio)
print("2:1 requires (v_G/v_EM)*(ell_EM/ell_G)=1")
print("action-length ell=hbar/p gives ratio =",action_ratio)
print("radial coordinate shift r_G-r_EM = -log(4)")
print("PASS: weld fixes dimensionless counting scale, not a physical wavelength clock")
