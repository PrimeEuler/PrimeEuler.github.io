"""Angle 5e: singular vector anatomy. Look at small-sigma right/left singular
vectors of K. Are they boundary layers? How do e^x, x, 1 project onto them?"""
import sys
import numpy as np
import os as _os
sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from bucket2_cancellation_screw import D12Screw
from bucket2_cancellation_lsq85 import Lsq85

screw = D12Screw(tmax=12.0)
A = 5.0
L = Lsq85(screw, A=A, N=120, lam=0.0, dirichlet=False)
K, xs, nodes = L.K, L.xs, L.nodes
U, sv, Vt = np.linalg.svd(K, full_matrices=False)
V = Vt.T
n = len(sv)
print(f"ndof={V.shape[0]}, ncoll={U.shape[0]}")
print(f"sv[0]={sv[0]:.3f}, sv[60]={sv[60]:.3e}, sv[100]={sv[100]:.3e}, sv[-1]={sv[-1]:.3e}")

# right singular vectors v_i (in P1 coefficient space) for small sigma: boundary layers?
print("\nRight singular vectors (P1 nodal values), small-sigma:")
for i in [n-1, n-2, n-3, n-5, n-10]:
    vi = V[:, i]
    # concentration: fraction of ||vi||^2 in outer 10% near each endpoint
    m = len(vi); e = m//10
    print(f"  i={i} sv={sv[i]:.2e} |v|^2 left10%={np.sum(vi[:e]**2)/np.sum(vi**2):.2f} right10%={np.sum(vi[-e:]**2)/np.sum(vi**2):.2f} mid80%={np.sum(vi[e:-e]**2)/np.sum(vi**2):.2f}")
print("\nRight singular vectors, large-sigma (for contrast):")
for i in [0, 1, 2]:
    vi = V[:, i]
    m = len(vi); e = m//10
    print(f"  i={i} sv={sv[i]:.2e} left10%={np.sum(vi[:e]**2)/np.sum(vi**2):.2f} right10%={np.sum(vi[-e:]**2)/np.sum(vi**2):.2f}")

# left singular vectors u_i (on collocation grid): projections of e^x, x, 1
d = np.exp(xs); xx = xs; oo = np.ones_like(xs)
print("\n<u_i, e^x>, <u_i, x>, <u_i, 1> for small-sigma i:")
for i in [n-1, n-2, n-3, n-5, n-10]:
    ui = U[:, i]
    print(f"  i={i} sv={sv[i]:.2e} <u,e^x>={ui@d:+.4e} <u,x>={ui@xx:+.4e} <u,1>={ui@oo:+.4e}")
print("\nfor large-sigma i:")
for i in [0, 1, 2]:
    ui = U[:, i]
    print(f"  i={i} sv={sv[i]:.2f} <u,e^x>={ui@d:+.4e} <u,x>={ui@xx:+.4e} <u,1>={ui@oo:+.4e}")

# The K^dagger-amplified coefficients: <u_i,f>/sv_i for f=e^x. Which i dominate p0?
w = (U.T @ d) / sv
idx = np.argsort(np.abs(w))[::-1][:8]
print(f"\nTop contributors to p0=K^d e^x (index, sv, |<u,e^x>|/sv):")
for i in idx:
    print(f"  i={i} sv={sv[i]:.2e} coeff={w[i]:+.4e}")
