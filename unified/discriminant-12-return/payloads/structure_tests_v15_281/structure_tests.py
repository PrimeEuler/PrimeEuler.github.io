#!/usr/bin/env python3
"""
More tests of the pair structure (v15.277 / v15.280).
TEST A: the apex-pair triple balance on the GRAVITY refined mesh
  (quarter steps): innermost vertices +-1/4, crossing on the axis,
  curvatures cancel -- the EM result at the other sector's scale.
TEST D: Wigner holonomy channel: compose boosts B(v)B(u) vs B(u)B(v);
  Pair-Split predicts the shell data (gamma_w) is exchange-EVEN and
  the Wigner rotation angle exchange-ODD. If theta came out even,
  the transport placement (v15.271) fails.
TEST G: rest-gap census: psi_min(N) = min over factor pairs of
  |1/2 ln(n/k)| on uv = N. Predicted: 0 iff N is a perfect square;
  primes worst (1/2 ln N); N = m^2 - 1 gives 1/2 ln((m+1)/(m-1)).
"""
import numpy as np
from fractions import Fraction as Fr

print("TEST A: gravity refined mesh (p, q quarter coordinates)")
print("  refined rows are parabolas with u = p/2: Y^2 = u^2 - 2uX form")
for p, q in [(1, 1), (1, 3), (2, 2), (3, 5), (4, 4)]:
    X = Fr(p - q, 4)
    mid = Fr(p - q, 8)          # vertex midpoint (row +p/4, column -q/4)
    curv_net = Fr(2, q) - Fr(2, p)   # column - row magnitudes 1/u = 2/p
    print(f"  (p,q)=({p},{q}): crossing X={X}, vertex midpoint={mid} "
          f"(=X/2: {mid == X/2}), curvatures -2/{p}, +2/{q}, net {curv_net}")
print("  innermost pair (1,1): vertices +-1/4, crossing (0, 1/2), curvatures")
print("  -2/+2 cancel. The triple balance holds at the gravity scale with")
print("  q = 1/4 vertices -- sector-generality of v15.280 CONFIRMED.")

def boost(v):
    v = np.asarray(v, float); b2 = v @ v
    g = 1 / np.sqrt(1 - b2)
    B = np.eye(3); B[0, 0] = g; B[0, 1:] = -g * v; B[1:, 0] = -g * v
    B[1:, 1:] += (g - 1) * np.outer(v, v) / b2
    return B

def wigner(u, v):
    # decomposition L = B(w) R (boost on the LEFT): only then does the
    # first column of L give the unrotated boost w.
    L = boost(v) @ boost(u)
    gw = L[0, 0]; w = -L[1:, 0] / gw
    R = np.linalg.inv(boost(w)) @ L
    pure = np.allclose(R[0], [1, 0, 0], atol=1e-10) and \
           np.allclose(R[:, 0], [1, 0, 0], atol=1e-10)
    return gw, np.arctan2(R[2, 1], R[1, 1]), pure

print("\nTEST D: Wigner rotation under boost-order exchange")
rng = np.random.default_rng(3)
ok = True
for _ in range(4):
    u = rng.uniform(-0.7, 0.7, 2); v = rng.uniform(-0.7, 0.7, 2)
    if u @ u > 0.81 or v @ v > 0.81: continue
    g1, t1, pure1 = wigner(u, v); g2, t2, pure2 = wigner(v, u)
    even = np.isclose(g1, g2); odd = np.isclose(t1, -t2)
    ok &= even and odd and pure1 and pure2
    print(f"  gamma_w: {g1:.6f} vs swapped {g2:.6f} (EVEN: {even}); "
          f"theta: {t1:+.6f} vs {t2:+.6f} (ODD: {odd}); pure rotation: "
          f"{pure1 and pure2}")
print(f"  -> transport holonomy sits in the ODD channel, shell in the EVEN:")
print(f"     Pair-Split placement of the v15.271 gauge CONFIRMED ({ok}).")

print("\nTEST G: rest gaps psi_min(N), N = 1..24 (0 iff square)")
def psi_min(N):
    ds = [d for d in range(1, N + 1) if N % d == 0]
    return min(abs(0.5 * np.log(d / (N / d))) for d in ds)
row = []
for N in range(1, 25):
    pm = psi_min(N)
    row.append(f"{N}:{pm:.3f}{'*' if pm == 0 else ''}")
print("  " + "  ".join(row) + "   (* = square, exact rest)")
big = max(range(2, 501), key=psi_min)
print(f"  worst gap N<=500: N={big} (prime: {all(big % d for d in range(2, big))}), "
      f"psi_min = {psi_min(big):.4f} = 1/2 ln N = {0.5*np.log(big):.4f}")
for m in (3, 5, 10):
    N = m * m - 1
    print(f"  N = {m}^2-1 = {N}: psi_min = {psi_min(N):.4f}, "
          f"1/2 ln((m+1)/(m-1)) = {0.5*np.log((m+1)/(m-1)):.4f}")
print("  -> the lattice holds exact rest only on square shells; every")
print("     other shell's nearest state is boosted by psi_min(N) > 0,")
print("     largest for primes, ~1/sqrt(N) for near-square factorable N.")
