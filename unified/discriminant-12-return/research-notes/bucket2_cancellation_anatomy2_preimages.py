"""Angle 5b: where does v live? Examine v_*(x), Kv+e^x, and the affine.
Also compute the preimages p1=K^dagger x, p2=K^dagger 1, p0=K^dagger e^x
and verify the min-norm characterization."""
import sys
import numpy as np
import os as _os
sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from bucket2_cancellation_screw import D12Screw
from bucket2_cancellation_lsq85 import Lsq85

screw = D12Screw(tmax=12.0)
A = 5.0
L = Lsq85(screw, A=A, N=120, lam=0.0, dirichlet=False)
r = L.solve(1.0, alpha=1e-10)
K, X, Mm, xs = L.K, L.X, L.Mm, L.xs
v, Ac, Bc = r['v'], r['A'], r['B']
nodes = L.nodes

print(f"A={A}, Acoef={Ac:.4f}, Bcoef={Bc:.4f}, ell(A)={A*Ac+Bc:.4f}")
print("\nv(x) at nodes (every 12th):")
for i in range(0, len(nodes), 12):
    print(f"  x={nodes[i]:+.2f}  v={v[i]:+.4e}")
print("  ...")
print(f"  x={nodes[-1]:+.2f}  v={v[-1]:+.4e}")

# Kv + e^x on collocation grid vs affine
Kv = K @ v
d = np.exp(xs)
aff = Ac * xs + Bc
lhs = Kv + d  # should equal -aff + residual
print(f"\nmax|Kv+e^x+aff| (residual) = {np.max(np.abs(Kv+d+aff)):.2e}")
print(f"||Kv+e^x|| = {np.linalg.norm(Kv+d):.4e}, ||aff|| = {np.linalg.norm(aff):.4e}")

# where is |v| concentrated? cumulative mass from the right
mass = np.abs(v)
cum = np.cumsum(mass[::-1])[::-1]
tot = cum[0]
for frac in [0.5, 0.8, 0.95]:
    idx = np.searchsorted(cum[::-1], frac*tot)
    xr = nodes[::-1][idx]
    print(f"  rightmost {100*frac:.0f}% of |v|-mass lives at x >= {xr:.2f}")

# preimages of affine basis and e^x under K (lstsq = min-norm)
p1, *_ = np.linalg.lstsq(K, xs, rcond=None)     # K p1 = x
p2, *_ = np.linalg.lstsq(K, np.ones_like(xs), rcond=None)  # K p2 = 1
p0, *_ = np.linalg.lstsq(K, d, rcond=None)      # K p0 = e^x
print(f"\n||p1|| (K^d x) = {np.linalg.norm(p1):.4e}, ||p2|| (K^d 1) = {np.linalg.norm(p2):.4e}, ||p0|| (K^d e^x) = {np.linalg.norm(p0):.4e}")

# verify: v + (p0 + Ac*p1 + Bc*p2) should be ~0 (min-norm v = -(p0+A p1+B p2))
print(f"||v + (p0+Ac p1+Bc p2)||/||v|| = {np.linalg.norm(v + (p0+Ac*p1+Bc*p2))/np.linalg.norm(v):.2e}")

# M-orthogonality: <v, p1>_M = 0, <v, p2>_M = 0 ?
o1 = v @ (Mm @ p1); o2 = v @ (Mm @ p2)
print(f"<v,p1>_M = {o1:.4e}  (<v,v>_M = {v@Mm@v:.4e})")
print(f"<v,p2>_M = {o2:.4e}")

# the representer q of ell(A): q in span{p1,p2} with <q,p1>=A, <q,p2>=1
G = np.array([[p1@Mm@p1, p1@Mm@p2],[p2@Mm@p1, p2@Mm@p2]])
c = np.array([p0@Mm@p1, p0@Mm@p2])
coef = np.linalg.solve(G, np.array([A, 1.0]))
q = coef[0]*p1 + coef[1]*p2
print(f"\nrepresenter check: <q,p1>_M={q@Mm@p1:.4f} (want {A}), <q,p2>_M={q@Mm@p2:.4f} (want 1)")
print(f"ell(A) = -<q,p0>_M = {-(q@Mm@p0):.4f}  (direct: {A*Ac+Bc:.4f})")
# where does q live?
print("q at nodes (every 12th):")
for i in range(0, len(nodes), 12):
    print(f"  x={nodes[i]:+.2f}  q={q[i]:+.4e}")
