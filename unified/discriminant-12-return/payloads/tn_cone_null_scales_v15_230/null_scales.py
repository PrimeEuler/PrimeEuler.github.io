#!/usr/bin/env python3
"""
Null-scale bookkeeping: (A) the apex account (-1/2 seat, 0 apex,
+1/2 Sciama balance) with current cosmological numbers; (B) a
cross-ratio catalog of the null scales, with coincidence discipline.

Constants: CODATA c, hbar, G, kB exact-ish; g = 9.80665 (defined
standard gravity); H0 = 67.36 +/- 0.54 km/s/Mpc (Planck 2018) and
73.04 +/- 1.04 (SH0ES) where noted; Omega_K = 0.0007 +/- 0.0019
(Planck 2018); a0 = 1.20e-10 m/s^2 (MOND canonical, SPARC).
"""
import numpy as np

c = 299792458.0
hbar = 1.054571817e-34
G = 6.67430e-11
kB = 1.380649e-23
g = 9.80665
Mpc = 3.0856775814913673e22
yr = 365.25 * 86400.0
ly = c * yr
a0 = 1.20e-10
psi_D = 45.310004305  # v14.621 hierarchy target, for comparison

def H0_si(v):  # km/s/Mpc -> 1/s
    return v * 1e3 / Mpc

print("=" * 74)
print("A. APEX BOOKKEEPING:  -1/2 (seat) ... 0 (apex) ... +1/2 (Sciama)")
print("=" * 74)
print("Identity: for a sphere of radius R and mean density rho,")
print("  GM/(R c^2) = 4 pi G rho R^2 / (3 c^2).")
print("At R = R_H = c/H0 and rho = Omega * rho_c, rho_c = 3 H0^2/(8 pi G):")
print("  GM/(R_H c^2) = Omega/2   exactly -- H0 cancels.")
for name, Om, dOm in [("Planck 2018 (Omega_K = 0.0007 +/- 0.0019)", 0.9993, 0.0019)]:
    print(f"  {name}: Omega_tot = {Om:.4f} +/- {dOm:.4f} "
          f"-> B = Omega/2 = {Om/2:.4f} +/- {dOm/2:.4f}")
print("  The +1/2 entry is measured (cosmology), H0-independent: the")
print("  Hubble tension moves R_H and M_H but cannot move B.")
for tag, h in [("Planck", 67.36), ("SH0ES", 73.04)]:
    H = H0_si(h)
    RH = c / H
    rho_c = 3 * H**2 / (8 * np.pi * G)
    MH = rho_c * 4 * np.pi / 3 * RH**3
    rs = 2 * G * MH / c**2
    print(f"  {tag}: H0 = {h} -> R_H = {RH:.3e} m = {RH/ly/1e9:.2f} Gly, "
          f"M_H = {MH:.3e} kg, r_s(M_H) = {rs/RH:.4f} R_H")
print("  Geometric face: at Omega = 1 the Hubble sphere sits exactly at")
print("  its own Schwarzschild radius (r_s = Omega * R_H).")
print("  Entries: seat -1/2 [D, geometry]; apex 0 [the sum, no dynamics")
print("  on record]; cosmic +1/2 [empirical, = Omega/2]. Sciama's Machian")
print("  reading makes +1/2 an identity (G defined by the inventory);")
print("  LCDM makes it a measured initial condition. Nothing on record")
print("  identifies the two 1/2's or supplies the apex cancellation.")

print()
print("=" * 74)
print("B. CROSS-RATIO CATALOG OF THE NULL SCALES (the temptation, tagged)")
print("=" * 74)
H = H0_si(67.36)
RH = c / H
aH = c * H
lg = c**2 / g            # Rindler length at 1 g
tg = c / g               # time for 1 g to reach c
lP = np.sqrt(hbar * G / c**3)
aP = np.sqrt(c**7 / (hbar * G))
TU_g = hbar * g / (2 * np.pi * c * kB)
TGH = hbar * H / (2 * np.pi * kB)
print(f"scales: c^2/g = {lg:.3e} m = {lg/ly:.4f} ly | c/g = {tg/yr:.4f} yr | "
      f"c/H0 = {RH/ly/1e9:.2f} Gly")
print(f"        a_P = {aP:.3e} m/s^2 | cH0 = {aH:.3e} | a0 = {a0:.2e} | "
      f"T_U(g) = {TU_g:.2e} K | T_GH = {TGH:.2e} K")
rows = [
    ("c^2/g in light-years", lg / ly, "the '1 g = 1 ly' headline"),
    ("(c/g) in years", tg / yr, "SAME coincidence restated (x c)"),
    ("(c^2/g) / (c/H0) = cH0/g", lg / RH, "local g vs cosmic null scale"),
    ("a0 / (cH0)", a0 / aH, "raw MOND-cosmic ratio"),
    ("a0 / (cH0/2pi) [Planck H0]", a0 / (aH / (2*np.pi)), "THE MOND coincidence"),
    ("a0 / (cH0/2pi) [SH0ES H0]", a0 / (c*H0_si(73.04) / (2*np.pi)), "same, other H0"),
    ("g / a0", g / a0, "terrestrial vs galactic acceleration"),
    ("g / aP", g / aP, "terrestrial vs Planck acceleration"),
    ("a0 / aP", a0 / aP, "galactic vs Planck acceleration"),
    ("(c/H0) / lP", RH / lP, "Hubble radius in Planck lengths"),
    ("(c^2/g) / lP", lg / lP, "Rindler length in Planck lengths"),
    ("T_U(g) / T_CMB", TU_g / 2.725, "Unruh at 1 g vs the microwave sky"),
    ("T_U(g) / T_GH", TU_g / TGH, "= g/(cH0): pins ratio"),
]
for name, val, note in rows:
    print(f"  {name:<34} = {val:>12.5g}   ln = {np.log(val):>9.3f}   [{note}]")
print(f"\n  comparison depth: psi_D (v14.621) = {psi_D}; 2 psi_D = {2*psi_D:.2f};")
print(f"  ln(aP/g) = {np.log(aP/g):.2f}, ln(aP/a0) = {np.log(aP/a0):.2f} -- "
      "neither lands on psi_D")
print("  or 2 psi_D: the null-scale log-depths (~117, ~142, ~140) are NOT")
print("  the Dirac depth. Discipline: every row above is a catalog entry,")
print("  not a derivation; no mechanism on record connects any pair.")
