#!/usr/bin/env python3
"""
Nature's pushback, in two exact forms.
(1) Radiation reaction: F_react = m tau0 * jerk (the retarded-minus-
    advanced field difference, Dirac). Over one period of harmonic
    motion, the work against the reaction exactly pays the Larmor
    radiation: <F_react . v> + <P_Larmor> = 0 (symbolic).
(2) Fluctuation-dissipation: Langevin velocity with damping gamma
    and noise strength 2 gamma k_B T -- ONE coefficient in both
    opposed roles. Equilibrium <v^2> = k_B T / m (numeric OU process).
"""
import sympy as sp
import numpy as np

t, A, w, tau0, m = sp.symbols('t A omega tau_0 m', positive=True)
x = A * sp.cos(w * t)
v = sp.diff(x, t)
jerk = sp.diff(x, t, 3)
P_react = m * tau0 * jerk * v                    # power against reaction
P_larm = m * tau0 * sp.diff(x, t, 2)**2          # Larmor (m tau0 = e^2/6 pi eps0 c^3)
avg = lambda e: sp.simplify(sp.integrate(e, (t, 0, 2 * sp.pi / w)) * w / (2 * sp.pi))
print("radiation reaction over one period:")
print("  <F_react . v> =", avg(P_react))
print("  <P_Larmor>    =", avg(P_larm))
print("  sum =", sp.simplify(avg(P_react) + avg(P_larm)),
      " -- the pushback exactly collects the radiated energy.")

e, eps0, c, m_e = 1.602176634e-19, 8.8541878128e-12, 299792458.0, 9.10938370e-31
tau_e = e**2 / (6 * np.pi * eps0 * m_e * c**3)
print(f"  electron reaction time tau_0 = {tau_e:.3e} s "
      f"(nature's pushback delay on an accelerating electron).")

rng = np.random.default_rng(7)
gamma_, kBT, mm, dt = 1.0, 1.0, 1.0, 1e-3
a_ou = np.exp(-gamma_ / mm * dt)
s_ou = np.sqrt(kBT / mm * (1 - a_ou**2))
ens = np.zeros(200_000)
for _ in range(4000):  # t = 4 >> correlation time m/gamma = 1: equilibrated
    ens = a_ou * ens + s_ou * rng.standard_normal(ens.size)
meas = float(np.mean(ens**2))
err = float(np.sqrt(2.0 / ens.size))
print(f"\nfluctuation-dissipation: damping gamma={gamma_}, noise set BY gamma")
print(f"  (strength 2 gamma k_B T): measured <v^2> = {meas:.4f} +- {err:.4f}, "
      f"k_B T / m = {kBT/mm:.4f}")
print("  -> drive and pushback share one coefficient; their balance IS")
print("     the equilibrium (the diagonal): <v^2> = k_B T/m, no net drift.")
