"""Completing the last step: the inventory must be COUNTED (exact integer
+ closure), not weighed (density). Criterion + candidate closures."""
import numpy as np
psi = 45.310004305; D = np.exp(2*psi)
N_pairs = 8.94e79                      # eta-based census (this evening)
N_gamma = 1.47e89

print('=== The drift check: is sqrt(N_pairs) = D with MODERN numbers? ===')
print(f'  sqrt(N_pairs) = {np.sqrt(N_pairs):.3e}   D = {D:.3e}')
print(f'  ratio sqrt(N)/D = {np.sqrt(N_pairs)/D:.2f}   (Dirac 1937: ~1 with his H0)')
print(f'  half-log gap = {0.5*np.log(N_pairs) - 2*psi:.3f}  -> the coincidence has')
print(f'  DRIFTED off 1: any completion must predict the ratio (~4.2), not 1.')

print()
print('=== Candidate A: phase closure on the one worldline ===')
mec2_hbar = 7.763e20                   # m_e c^2 / hbar, s^-1
T_age = 4.35e17                        # s
Phi = mec2_hbar * N_pairs * T_age      # total phase, all strands parallel
print(f'  total phase Phi ~ {Phi:.2e} rad; closure solutions spaced')
print(f'  dN/N ~ 2pi/Phi ~ {2*np.pi/Phi:.1e} -> integers are dense: selects NOTHING.')

print()
print('=== Candidate B: the tangency closure (Sciama balance) ===')
print('  B = G M_u/(R_u c^2) = Omega/2 for R = Hubble radius.')
print('  Closure B = 1/2 exactly  <=>  Omega = 1 exactly: the Hubble volume')
print('  sits exactly at its own Schwarzschild tangency. Inflation drives')
print('  Omega -> 1 but runs with G given: promotes the balance to exact,')
print('  fixes RATIOS -- the count magnitude stays a free integer.')

print()
print('=== Candidate C: what maps exist from small integers to ~1e80? ===')
acc, j = 0.0, 0
while acc < np.log(N_pairs):
    j += 1; acc += np.log(2*j+1)
print(f'  ladder product prod(2j+1) reaches ln N_pairs at J = {j} shells')
acc2, j2 = 0.0, 0
while acc2 < 2*psi:
    j2 += 1; acc2 += np.log(2*j2+1)
print(f'  ladder product reaches 2psi (ln D) at J = {j2}')
print(f'  shell-state census (J+1)^2 = N_pairs needs J+1 = {np.sqrt(N_pairs):.2e} (no small J)')
