#!/usr/bin/env python3
"""
Where does the electron's rest-mass hyperbola sit in the light-year
(null-scale) structure? The mass shell uv = s^2 is a level hyperbola
whose length scale, via the hbar pin, is the reduced Compton length
L_e = hbar/(m_e c). Place L_e on the v15.230 log-depth ladder and
test the marked rungs (psi_D, 2 psi_D) honestly.
"""
import numpy as np

hbar, c, G = 1.054571817e-34, 299792458.0, 6.67430e-11
m_e, m_p = 9.10938370e-31, 1.67262192e-27
ly = 9.4607304725808e15
lP = np.sqrt(hbar * G / c**3)
Le = hbar / (m_e * c)
g = 9.80665
Rind = c**2 / g
psi = 45.310004305  # v14.621 Dirac depth
Lpsi = lP * np.exp(psi)

print(f"electron reduced Compton length L_e = {Le:.4e} m = {Le/ly:.4e} ly")
print(f"electron rest energy m_e c^2 = {m_e*c**2/1.602176634e-13:.4f} MeV")
print(f"\nlog-depths of L_e (ln of ratio):")
for name, L in [("Planck length l_P", lP),
                ("depth-psi length l_P e^psi", Lpsi),
                ("Rindler length c^2/g (0.9687 ly)", Rind),
                ("one light-year", ly)]:
    print(f"  ln(L_e / {name:34s}) = {np.log(Le/L):+.3f}")
for H0, tag in [(67.4, "Planck"), (73.0, "SH0ES")]:
    RH = c / (H0 * 1e3 / 3.085677581e22)
    print(f"  ln(R_H / L_e) [{tag} H0={H0}] = {np.log(RH/Le):.3f}   "
          f"(total ln(R_H/l_P) = {np.log(RH/lP):.2f})")

print(f"\nmarked-rung tests:")
print(f"  depth above Planck: ln(L_e/l_P) = {np.log(Le/lP):.3f}")
print(f"    vs psi_D = {psi:.3f}: excess {np.log(Le/lP)-psi:+.3f} "
      f"(factor {np.exp(np.log(Le/lP)-psi):.1f}) -- NOT the Dirac rung")
print(f"    vs psi_D + ln(m_p/m_e) built-in check: "
      f"{psi + np.log(3.66):.3f} (the 3.66 of v15.233) -- arithmetic, not a lock")
d = np.log((c / (67.4e3 / 3.085677581e22)) / Le)
print(f"  depth below horizon: {d:.3f} vs 2 psi_D = {2*psi:.3f}: "
      f"off by {d-2*psi:+.2f} (factor {np.exp(abs(d-2*psi)):.1f}) -- NOT 2 psi")
print(f"\nposition summary: on a cone drawn at light-year scale, the")
print(f"electron hyperbola is a level curve at Y ~ {Le/ly:.1e} ly --")
print(f"indistinguishable from the apex axis; atomic physics lives in")
print(f"the apex's immediate neighborhood of the cosmic ladder, at log")
print(f"depth {np.log(Le/lP):.1f} of {np.log((c/(67.4e3/3.085677581e22))/lP):.1f} "
      f"from Planck to horizon.")
