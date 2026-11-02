#!/usr/bin/env python3
"""
Spinors can only live in the doublet channel.
A full 2pi rotation acts on a spin-j state as (-1)^{2j}: integer j
(tensors) return to +1 -- they live in the scalar (even/odd)
channels; half-integer j (spinors) return to -1 -- they live on the
double cover, i.e. IN the exchanged doublet itself, and cannot be
placed in a scalar channel. Same -1 as T^2 (Kramers, v15.278).
On the cone: shell lock ties half-integer j to the ODD diagonals,
integer j to the EVEN -- so spinors reside only on odd diagonals;
the even/odd channels see only spinor BILINEARS (density even,
current = the odd generators).
"""
import numpy as np

print("rotation sign R(2pi) = exp(-2 pi i J_z) = (-1)^{2j} I:")
for j in (0, 0.5, 1, 1.5, 2, 2.5, 3):
    dim = int(2 * j + 1)
    ms = np.array([j - i for i in range(dim)])
    R = np.diag(np.exp(-2j * np.pi * ms))
    sign = int(round(R[0, 0].real))
    kind = "SPINOR (doublet channel)" if sign < 0 else "tensor (scalar channels)"
    diag = "odd diagonal " if (2 * j) % 2 == 1 else "even diagonal"
    print(f"  j={j:3.1f}: R(2pi) = {sign:+d} I   {kind:26s} shell: {diag}")

print("\nspinor bilinears from an explicit 2-spinor psi = (a, b):")
a, b = 0.6 + 0.3j, -0.5 + 0.55j
psi = np.array([a, b])
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
dens = np.vdot(psi, psi).real
cur = [np.vdot(psi, s @ psi).real for s in (sx, sy, sz)]
print(f"  density psi+ psi = {dens:.4f} (scalar -- EVEN channel)")
print(f"  current psi+ sigma psi = {np.round(cur, 4)} (vector -- the ODD")
print("  generators). The spinor itself is in NEITHER scalar channel:")
print("  under the doublet's phase exchange it is the pair (psi, T psi),")
print("  and its own sign under 2pi / T^2 is -1. Only its bilinears")
print("  descend to the channels of v15.277.")
print("\n-> spinors live only in the doublet channel = on the odd")
print("   diagonals; even diagonals (integer j) cannot host them,")
print("   because their exchange sign is +1 by the same computation.")
