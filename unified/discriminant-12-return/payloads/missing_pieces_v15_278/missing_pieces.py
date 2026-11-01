#!/usr/bin/env python3
"""
Shot 1 -- the missing denominator 8.
Scan the record's dyadic forms mod 1 over the quarter lattice and
collect exact denominators; then the parity reason: for j = a/4,
j(j+1) = a(a+4)/16, and v2(a(a+4)) is never 1 (a, a+4 share a parity
class), so the reduced denominator 16/2^v2 is in {16, 4, 1} -- 8 is
excluded for EVERY quadratic form of this type. Contrast: the cubic
j^3 hits 1/8 exactly (j = 1/2): 8 lives one degree up.
Shot 2 -- the quantum doublet (Kramers).
T = exp(-i pi J_y) K; verify T^2 = (-1)^{2j} for j = 1/2, 1, 3/2 and
that a T-invariant spin-3/2 Hamiltonian has forced doublets while
the same form at spin 1 does not: the doublet of v15.277 is a
THEOREM on the half-integer (odd-diagonal) side.
"""
from fractions import Fraction as Fr
import numpy as np

print("SHOT 1: denominators of the record's forms (j on the quarter lattice)")
forms = {
    "j(j+1) Casimir": lambda j: j * (j + 1),
    "(j+1/2)^2 ladder": lambda j: (j + Fr(1, 2))**2,
    "(k/4)^2 pair product (j=k/2)": lambda j: (2 * j / 4)**2,
    "seat ((2j-1)/4)^2-ish root sq": lambda j: ((2 * j - 1) / 4)**2,
}
for name, f in forms.items():
    dens = sorted({(f(Fr(a, 4)) % 1).denominator for a in range(0, 33)})
    print(f"  {name:30s} denominators mod 1: {dens}")
print("  cubic contrast j^3: denominators:",
      sorted({(Fr(a, 4)**3 % 1).denominator for a in range(0, 9)}),
      "-- j=1/2 gives exactly 1/8.")
print("\n  parity mechanism for j(j+1), j = a/4 -> a(a+4)/16:")
for a in range(0, 9):
    v = 0; x = a * (a + 4)
    while x % 2 == 0 and x > 0:
        x //= 2; v += 1
    print(f"    a={a}: v2(a(a+4)) = {v if a else 'inf(0)'} -> "
          f"denominator {(16 // 2**v) if v < 4 else 1}")
print("  v2 is never 1 (a and a+4 share a parity class), so the reduced")
print("  denominator is never 8: the 8 is missing BY PARITY in every")
print("  quadratic form on the dyadic lattice -- it exists only at odd")
print("  degree (cubic: 1/8 at j = 1/2).")

def spin_ops(j):
    dim = int(2 * j + 1)
    ms = np.array([j - i for i in range(dim)], float)
    Jp = np.zeros((dim, dim))  # (J+)_{m+1,m} = sqrt(j(j+1)-m(m+1))
    for col, m in enumerate(ms):
        for row, mp in enumerate(ms):
            if mp == m + 1:
                Jp[row, col] = np.sqrt(j * (j + 1) - m * (m + 1))
    Jm = Jp.T
    Jx = (Jp + Jm) / 2; Jy = (Jp - Jm) / (2j); Jz = np.diag(ms)
    return Jx, Jy, Jz

def T_unitary(Jy):
    w, V = np.linalg.eigh(Jy)
    return V @ np.diag(np.exp(-1j * np.pi * w)) @ V.conj().T

print("\nSHOT 2: Kramers -- T^2 and forced doublets")
for j in (0.5, 1.0, 1.5):
    Jx, Jy, Jz = spin_ops(j)
    U = T_unitary(Jy)
    T2 = U @ U.conj()
    sign = +1 if np.allclose(T2, np.eye(len(T2))) else \
           (-1 if np.allclose(T2, -np.eye(len(T2))) else 0)
    print(f"  j={j}: T^2 = {sign:+d} x I   (predicted (-1)^(2j) = "
          f"{int((-1)**(2*j)):+d})")
for j, D, E in ((1.5, 1.0, 0.3), (1.0, 1.0, 0.3)):
    Jx, Jy, Jz = spin_ops(j)
    dim = int(2 * j + 1)
    H = D * (Jz @ Jz - j * (j + 1) / 3 * np.eye(dim)) + E * (Jx @ Jx - Jy @ Jy)
    U = T_unitary(Jy)
    Tinv = np.allclose(U @ H.conj() @ U.conj().T, H)
    ev = np.sort(np.linalg.eigvalsh(H).real)
    print(f"  j={j}: H T-invariant: {Tinv}; spectrum {np.round(ev, 4)}")
print("  -> spin-3/2: two forced doublets (Kramers); spin 1: three")
print("     distinct levels. The v15.277 phase doublet is a theorem on")
print("     the half-integer side -- the cone's odd diagonals.")
