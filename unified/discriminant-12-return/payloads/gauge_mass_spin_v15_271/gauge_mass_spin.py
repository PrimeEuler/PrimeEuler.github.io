#!/usr/bin/env python3
"""
Gauge/labels check: (m, J) as orbit labels; J in atomic EM structure.

(a) Dirac hydrogen levels: E depends on j through |kappa| = j + 1/2 --
    the fine-structure splitting of the n=2 P states.
(b) Thomas bookkeeping: naive rest-frame spin-orbit coefficient g/2;
    Thomas precession subtracts 1/2; net (g-1)/2 (the observed).
(c) Linear Stark effect in parabolic states: dE = (3/2) n k F (a.u.),
    k = n1 - n2 = the mesh offset quantum number (2X).
"""
import numpy as np

alpha = 7.2973525693e-3
mc2 = 510998.95  # eV

def dirac_binding(n, j, Z=1):
    kap = j + 0.5
    nr = n - int(kap)
    denom = nr + np.sqrt(kap**2 - (Z * alpha)**2)
    E = mc2 / np.sqrt(1.0 + (Z * alpha / denom)**2)
    return mc2 - E  # binding energy, eV

print("Dirac hydrogen binding energies (eV):")
for (n, j, name) in [(1, 0.5, "1S1/2"), (2, 0.5, "2S1/2 / 2P1/2"),
                     (2, 1.5, "2P3/2"), (3, 0.5, "3S1/2 / 3P1/2"),
                     (3, 1.5, "3P3/2 / 3D3/2"), (3, 2.5, "3D5/2")]:
    print(f"  {name:16s} n={n} j={j}: {dirac_binding(n, j):.6f}")
dE = dirac_binding(2, 0.5) - dirac_binding(2, 1.5)
print(f"  2P3/2 - 2P1/2 splitting: {dE:.3e} eV = {dE * 2.417989e14 / 1e9:.2f} GHz")
print("  (measured: 4.53e-5 eV, 10.97 GHz -- the J-dependence of atomic levels)")

g = 2.00231930436
print(f"\nThomas bookkeeping: naive rest-frame coefficient g/2 = {g/2:.5f};")
print(f"  Thomas precession subtracts 1/2; net (g-1)/2 = {(g-1)/2:.5f}.")
print("  Without the transport correction the spin-orbit splitting is 2x")
print("  too large -- hydrogen's fine structure measures the spin-transport")
print("  holonomy (Wigner rotation along the orbit) directly.")

print("\nLinear Stark shifts dE = (3/2) n k F (atomic units), k = n1 - n2:")
for n in (2, 3):
    row = []
    for n1 in range(n):
        for n2 in range(n - n1):
            m_abs = n - 1 - n1 - n2
            k = n1 - n2
            row.append(f"(n1,n2)=({n1},{n2}) k={k:+d} dE/F={1.5*n*k:+.1f}")
    print(f"  n={n}: " + "; ".join(row))
print("-> the mesh offset (Stark number k = 2X) is an atomic EM observable;")
print("   the parabolic states |n1 n2 m> are the mesh crossings (Paper C).")
