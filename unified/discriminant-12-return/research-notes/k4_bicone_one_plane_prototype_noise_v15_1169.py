#!/usr/bin/env python3
"""Gravity v15.1169: hypothetical one-plane bicone torsion/Zeeman device.
All apparatus values are chosen illustrations, not measured performance;
same standard GR+solid and source-free Maxwell controls as v15.1155.
"""
import numpy as np
from scipy.constants import Boltzmann,hbar,pi
m=1e-3 # kg at each of two endpoints
d=.10 # meters between endpoints
I=m*d*d/2 # two point masses at +/-d/2
DeltaQ=m*d*d/2 # symmetric mass quadrupole anisotropy
f0=1.0 # Hz
omega0=2*pi*f0
Q=10_000.
kappa=I*omega0**2
Gamma=I*omega0/Q
temperature=300. # kelvin
G=.01 # tesla/m
B0=.01 # tesla along spin quantization w
gamma_e=1.76085963e11 # rad/(s*tesla), illustrative electron spin
assert B0>G*d/2 and np.isclose(I,DeltaQ)
# theta=0 oriented u,v plane gives normalized torque s=-E_uv and
# Larmor derivative d(DeltaOmega)/dtheta=gamma_e*G*d.
tau=.01 # Ramsey seconds, assumed prepared singlet/triplet protocol
N=1_000_000 # ideal independent pairs counted over 1 second
Tobs=1. # second of rectangular averaging
# Classical equilibrium viscous one-sided torque power spectrum per Hz
S_tau=4*Boltzmann*temperature*Gamma
S_g=S_tau/DeltaQ**2
equivalent_noise_bandwidth=1/(2*Tobs)
g_thermal=np.sqrt(S_g*equivalent_noise_bandwidth)
# shot-only delta(phi)=1/sqrt(N) at exact quadrature bias
# delta(phi)/delta(g)=gamma*G*d*tau*DeltaQ/kappa
g_spin=kappa/(abs(gamma_e*G*d)*DeltaQ*tau*np.sqrt(N))
# magnitude of spin-conditioned torque branch, not a white-noise PSD
spin_torque_branch=hbar*abs(gamma_e*G*d)/2
assert np.isclose(kappa,1.973920880217872e-4)
assert 1.4e-9 < np.sqrt(S_g) < 1.5e-9
assert 2.2e-8 < g_spin < 2.3e-8
assert g_spin/g_thermal>20
print('I=DeltaQ',I,'kappa',kappa,'Gamma',Gamma)
print('magnetic field at endpoints T',B0-G*d/2,B0+G*d/2)
print('one-sided thermal equiv tidal ASD s^-2/sqrtHz',np.sqrt(S_g))
print('ideal 1-second white thermal rms s^-2',g_thermal)
print('ideal 1-second N-pair projection rms s^-2',g_spin)
print('ratio spin noise/thermal',g_spin/g_thermal)
print('conditional spin torque (N*m, NOT PSD)',spin_torque_branch)
print('PASS illustrative one-plane thermal/spin noise budget')
print('NO real coil, suspension, state rate or quantum coherence engineering certified')
