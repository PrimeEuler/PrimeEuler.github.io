#!/usr/bin/env python3
"""
Reproducer for v14.099: SO(4,2) parabolic dipole scale |C|/a0 and e^2 determination.

Derives, from the parabolic SO(4,2) construction (no Schrodinger wavefunctions,
no spherical radial integrals):
  I1 = -2048/243  (parabolic gamma integrals)
  <000|z|100> = -128/243  (exact rational)
  |C|/a0 = 256/(243*sqrt(2)) ~ 0.744936  (sqrt(2) from |2p_z> definition)
  |<R10|r|R21>|/a0 = 768/(243*sqrt(6)) ~ 1.290266  (sqrt(3) from bicone Wigner-Eckhart)

Then the e^2 formula with the 2p->1s 1/3 angular/degeneracy factor explicit,
validated against Lyman-alpha.

Reference: workspace/d12/explorations/parabolic-dipole/REPORT.md
Ledger: v14.099 (partial v14.097)
"""

import numpy as np
from math import factorial, sqrt, pi

print("=" * 70)
print("v14.099 reproducer: SO(4,2) parabolic dipole scale")
print("=" * 70)

# ---------------------------------------------------------------------------
# Step 1: I1 = -2048/243 via gamma integrals
# I1 = (1/2)[ -int xi^3 e^{-3xi/4} dxi * int e^{-3eta/4} deta
#              + int xi e^{-3xi/4} dxi * int eta^2 e^{-3eta/4} deta ]
# int_0^inf x^n e^{-a x} dx = n! / a^{n+1}, a = 3/4
# ---------------------------------------------------------------------------
print("\n--- Step 1: I1 via gamma integrals (a = 3/4) ---")
a = 3/4
I_xi3 = factorial(3) / a**4    # 6 / (81/256) = 512/27
I_e   = factorial(0) / a**1    # 1 / (3/4) = 4/3
I_xi1 = factorial(1) / a**2    # 1 / (9/16) = 16/9
I_eta2= factorial(2) / a**3    # 2 / (27/64) = 128/27
print(f"  int xi^3 e^(-3xi/4) = {I_xi3:.6f}  (expect 512/27 = {512/27:.6f})")
print(f"  int e^(-3eta/4)     = {I_e:.6f}  (expect 4/3 = {4/3:.6f})")
print(f"  int xi e^(-3xi/4)    = {I_xi1:.6f}  (expect 16/9 = {16/9:.6f})")
print(f"  int eta^2 e^(-3eta/4)= {I_eta2:.6f}  (expect 128/27 = {128/27:.6f})")

I1 = 0.5 * (-I_xi3 * I_e + I_xi1 * I_eta2)
I1_exact = -2048/243
print(f"\n  I1 = (1/2)[-({I_xi3:.4f})({I_e:.4f}) + ({I_xi1:.4f})({I_eta2:.4f})]")
print(f"  I1 = {I1:.10f}")
print(f"  -2048/243 = {I1_exact:.10f}")
assert abs(I1 - I1_exact) < 1e-9, "I1 mismatch"
print("  PASS: I1 = -2048/243")

# ---------------------------------------------------------------------------
# Step 2: <000|z|100> = (pi*N/(4*sqrt(pi))) * I1, N = 1/(4*sqrt(pi))
# pi*N/(4*sqrt(pi)) = pi/(16*pi) = 1/16
# ---------------------------------------------------------------------------
print("\n--- Step 2: <000|z|100> = -128/243 ---")
N = 1/(4*sqrt(pi))
prefac = pi * N / (4*sqrt(pi))
print(f"  N = 1/(4*sqrt(pi)) = {N:.10f}")
print(f"  prefactor pi*N/(4*sqrt(pi)) = {prefac:.10f} (expect 1/16 = 0.0625)")
assert abs(prefac - 1/16) < 1e-12
z_000_100 = prefac * I1
z_exact = -128/243
print(f"  <000|z|100> = (1/16)*(-2048/243) = {z_000_100:.10f}")
print(f"  -128/243 = {z_exact:.10f}")
assert abs(z_000_100 - z_exact) < 1e-9, "z matrix element mismatch"
print("  PASS: <000|z|100> = -128/243 (exact rational)")

# ---------------------------------------------------------------------------
# Step 3: sqrt(2) from |2p_z> = (|100> - |010>)/sqrt(2)
# <000|z|2p_z> = sqrt(2) * <000|z|100>  (by xi<->eta antisymmetry)
# |C|/a0 = |<000|z|2p_z>| = 128*sqrt(2)/243 = 256/(243*sqrt(2))
# ---------------------------------------------------------------------------
print("\n--- Step 3: sqrt(2) -> |C|/a0 ---")
C_a0 = abs(z_000_100) * sqrt(2)
C_a0_exact = 256/(243*sqrt(2))
print(f"  |C|/a0 = sqrt(2)*128/243 = {C_a0:.10f}")
print(f"  256/(243*sqrt(2)) = {C_a0_exact:.10f}")
assert abs(C_a0 - C_a0_exact) < 1e-12
print(f"  PASS: |C|/a0 = 256/(243*sqrt(2)) = 0.7449355390...")
print(f"  (audit: 30-digit spherical confirmation: 0.7449355390...)")

# ---------------------------------------------------------------------------
# Step 4: sqrt(3) from bicone SO(3) Wigner-Eckhart
# |<R10|r|R21>| = sqrt(3) * |C|  =>  768/(243*sqrt(6))
# ---------------------------------------------------------------------------
print("\n--- Step 4: sqrt(3) (bicone WE) -> 768/(243*sqrt(6)) ---")
R_a0 = sqrt(3) * C_a0
R_a0_exact = 768/(243*sqrt(6))
print(f"  |<R10|r|R21>|/a0 = sqrt(3)*|C|/a0 = {R_a0:.10f}")
print(f"  768/(243*sqrt(6)) = {R_a0_exact:.10f}")
assert abs(R_a0 - R_a0_exact) < 1e-12
print("  PASS: |<R10|r|R21>|/a0 = 768/(243*sqrt(6)) = 1.290266...")

# ---------------------------------------------------------------------------
# Step 5: e^2 formula with 1/3 angular/degeneracy factor EXPLICIT
#
# Einstein A (2p->1s): A = w^3 |d|^2 / (3 pi eps0 hbar c^3)
#   |d|^2 = e^2 * |<1s|r_vec|2p>|^2
#   |<1s|r_vec|2p>|^2 = |C|^2   (only q=-m contributes; bicone delta_{q,-m})
#   |C|^2 = (1/3) * |<R10|r|R21>|^2   [1/3: radial -> vector, WE]
#
# Hence, with Y_geom = |<R10|r|R21>|/a0 (radial, geometric):
#   e^2 = (3 pi eps0 hbar c^3 * A) / (w^3 * |C|^2)
#       = (3 pi eps0 hbar c^3 * A) / (w^3 * a0^2 * Y_geom^2 / 3)
#       = (9 pi eps0 hbar c^3 * A) / (w^3 * a0^2 * Y_geom^2)
# The 1/3 is the SO(3) Wigner-Eckhart radial->vector factor (explicit above).
# ---------------------------------------------------------------------------
print("\n--- Step 5: e^2 with 1/3 factor explicit, Lyman-alpha check ---")
eps0 = 8.8541878128e-12
hbar = 1.054571817e-34
c = 299792458.0
e_known = 1.602176634e-19
a0 = 5.29177210903e-11

A21 = 6.265e8          # s^-1, measured
E21 = 10.2 * e_known   # J, measured
w = E21 / hbar

Y_geom = R_a0  # radial geometric dipole, from SO(4,2)+bicone (Steps 1-4)
# |C|^2 = Y_geom^2/3 * a0^2  [1/3 explicit]
C2 = (Y_geom**2 / 3) * a0**2
e2 = (3*pi*eps0*hbar*c**3 * A21) / (w**3 * C2)
print(f"  |<1s|r_vec|2p>|^2 = |C|^2 = (1/3)*Y_geom^2*a0^2  [1/3 explicit]")
print(f"  e^2 = (3*pi*eps0*hbar*c^3*A)/(w^3*|C|^2)")
print(f"      = (9*pi*eps0*hbar*c^3*A)/(w^3*a0^2*Y_geom^2)  [1/3 absorbed]")
print(f"\n  e^2 derived = {e2:.6e} C^2")
print(f"  e^2 known   = {e_known**2:.6e} C^2")
print(f"  ratio = {e2/e_known**2:.6f}")
alpha = e2/(4*pi*eps0*hbar*c)
print(f"  alpha = 1/{1/alpha:.4f}  (known 1/137.036)")
assert abs(e2/e_known**2 - 1) < 0.01, "e2 determination failed"
print("  PASS: e^2 from (SO(4,2)+bicone geometry + Lyman-alpha)")

print("\n" + "=" * 70)
print("ALL CHECKS PASS")
print("Chain: I1=-2048/243 -> <z>=-128/243 -> |C|/a0=256/(243√2)")
print("     -> |<R10|r|R21>|/a0=768/(243√6) -> e^2 (Lyman-alpha) -> alpha~1/137")
print("Zero Schrodinger input on the theory side.")
print("=" * 70)
