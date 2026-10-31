#!/usr/bin/env python3
"""
The 1 g acceleration parabola vs the Dirac depth, and its crossings.

Scaled (edge-pinned) coordinates for acceleration g:
    u  = g t / c        (dimensionless time)
    xi = g x / c^2      (dimensionless position; xi = u is the null edge)
Curves:  parabola (Galilean const accel)  xi_p = u^2 / 2
         Rindler hyperbola (relativistic const proper accel, same g)
                                          xi_h = sqrt(1 + u^2) - 1
         interval hyperbolas (shells)     u^2 - xi^2 = sigma^2
Depths: log-depth of an acceleration a below Planck acceleration a_P,
compared with the Dirac depth psi_D = 45.310004305 (v14.621).
"""
import numpy as np
import sympy as sp

c = 299792458.0
hbar = 1.054571817e-34
G = 6.67430e-11
g = 9.80665
yr = 365.25 * 86400.0
aP = np.sqrt(c**7 / (hbar * G))
psi = 45.310004305

print("DEPTH COMPARISON (log-depth below the Planck acceleration)")
d_g = np.log(aP / g)
print(f"  a_P = {aP:.4e} m/s^2;  depth of g: ln(a_P/g) = {d_g:.3f}")
print(f"  Dirac depth psi_D = {psi};  ratio = {d_g/psi:.4f};  "
      f"excess = {d_g - psi:.3f} (factor e^{d_g-psi:.2f} = {np.exp(d_g-psi):.3e})")
a_psi = aP * np.exp(-psi)
l_psi = c**2 / a_psi
lP = np.sqrt(hbar * G / c**3)
print(f"  acceleration AT the Dirac depth: a_P e^-psi = {a_psi:.4e} m/s^2")
print(f"  its Rindler length c^2/a = {l_psi:.3e} m "
      f"(= l_P e^psi = {lP*np.exp(psi):.3e} m)")
print(f"  references: proton charge radius 8.41e-16 m (ratio {l_psi/8.41e-16:.3f}),")
print(f"  proton reduced Compton 2.103e-16 m (ratio {l_psi/2.103e-16:.3f}) --")
print("  fermi neighbourhood, NOT an identity: psi was built from p/e data.")

print("\nCROSSINGS (scaled coordinates; exact algebra + numeric check)")
u = sp.symbols('u', positive=True)
xi_p = u**2 / 2
xi_h = sp.sqrt(1 + u**2) - 1
print("  parabola x edge (xi = u): u =", sp.solve(sp.Eq(xi_p, u), u),
      " -> t = 2c/g =", 2 * c / g / yr, "yr, x = 2c^2/g =", 2 * c**2 / g / (c * yr), "ly")
diff = sp.series(xi_p - xi_h, u, 0, 8)
print("  parabola - Rindler hyperbola =", diff, " (tangent at 0, > 0 after:")
us = np.linspace(0.01, 20, 2000)
d = us**2 / 2 - (np.sqrt(1 + us**2) - 1)
print(f"    numeric min over u in (0, 20]: {d.min():.4f} at u = {us[np.argmin(d)]:.2f}"
      " -> parabola strictly outside, NEVER crosses its own hyperbola")
print("  parabola x interval hyperbola u^2 - xi^2 = sigma^2:")
print("    u^2 - u^4/4 = sigma^2  ->  u^2 = 2 +/- 2 sqrt(1 - sigma^2):")
for sig in [0.5, 0.9, 1.0, 1.1]:
    if sig < 1:
        a_, b_ = 2 - 2*np.sqrt(1 - sig**2), 2 + 2*np.sqrt(1 - sig**2)
        print(f"    sigma = {sig}: TWO crossings, u = {np.sqrt(a_):.4f} and {np.sqrt(b_):.4f}")
    elif sig == 1:
        print(f"    sigma = 1: ONE grazing crossing, u = sqrt(2) = {np.sqrt(2):.4f}"
              " (xi = 1, inside the edge)")
    else:
        print(f"    sigma = {sig}: NO crossing (discriminant < 0)")
print("  -> the parabola crosses exactly the hyperbolas inside its own")
print("     Rindler scale (sigma < 1), grazes sigma = 1, and never reaches")
print("     the ones beyond it. Its own Rindler hyperbola it only touches")
print("     at birth: the hyperbola bends toward the edge and stays inside;")
print("     the parabola crosses the edge itself at u = 2 and leaves.")
