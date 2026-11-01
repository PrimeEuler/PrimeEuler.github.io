#!/usr/bin/env python3
"""
Position on the mass hyperbola = intersection of two opposite-sign
parabolas. Crossing (n, k): AM = (n+k)/2, offset = (n-k)/2, GM =
sqrt(nk). Read E = AM, p = offset, m = GM: then E^2 - p^2 = nk = m^2
identically -- the crossing lies on the hyperbola labelled by its
own GM, at rapidity psi = (1/2) ln(n/k) from the seat (n = k).
Boost = product-preserving split (u, v) -> (lambda u, v/lambda).
Electron worked example (continuous labels u = E + pc, v = E - pc).
"""
import numpy as np
from fractions import Fraction as Fr

print("lattice check: for every factor pair of N, AM^2 - offset^2 = N")
for N in (12, 36, 60):
    pairs = [(d, N // d) for d in range(1, N + 1) if N % d == 0]
    ok = all(Fr(n + k, 2)**2 - Fr(n - k, 2)**2 == N for n, k in pairs)
    psis = [0.5 * np.log(n / k) for n, k in pairs]
    print(f"  N={N}: {len(pairs)} crossings, identity exact: {ok}, "
          f"psi range [{min(psis):+.3f}, {max(psis):+.3f}], seat at psi=0 "
          f"{'present (sqrt(N) integer)' if int(np.sqrt(N))**2 == N else 'absent'}")
    print(f"    all crossings carry GM = sqrt(N) = {np.sqrt(N):.3f} = the "
          f"hyperbola label; position along it = ratio n/k.")

m = 0.51099895  # MeV
print(f"\nelectron (continuous labels, c=1): u = E + pc, v = E - pc, uv = m^2")
for E in (m, 1.0, 5.0):
    pc = np.sqrt(E**2 - m**2)
    u, v = E + pc, E - pc
    psi = 0.5 * np.log(u / v)
    print(f"  E={E:7.4f} MeV: u={u:.5f}, v={v:.5f}, uv={u*v:.6f} "
          f"(m^2={m**2:.6f}), psi={psi:.4f} = arccosh(E/m)={np.arccosh(E/m):.4f}")
print("-> at rest the two parabola labels are EQUAL (u = v = m c^2): the")
print("   electron at rest is the diagonal crossing -- seat -- of its own")
print("   hyperbola, the opposed pair in exact balance. Motion is the")
print("   pair splitting asymmetrically at fixed product uv = m^2.")
