"""Angle 5c: shapes of p0=K^d e^x, p1=K^d x, p2=K^d 1.
Understand the projection P(p0) onto span{p1,p2} and why the
associated affine vanishes at x=A."""
import sys
import numpy as np
import os as _os
sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from bucket2_cancellation_screw import D12Screw
from bucket2_cancellation_lsq85 import Lsq85

screw = D12Screw(tmax=12.0)
for A in [3.0, 5.0]:
    L = Lsq85(screw, A=A, N=120, lam=0.0, dirichlet=False)
    r = L.solve(1.0, alpha=1e-10)
    K, xs, nodes = L.K, L.xs, L.nodes
    v, Ac, Bc = r['v'], r['A'], r['B']
    d = np.exp(xs)
    p1, *_ = np.linalg.lstsq(K, xs, rcond=None)
    p2, *_ = np.linalg.lstsq(K, np.ones_like(xs), rcond=None)
    p0, *_ = np.linalg.lstsq(K, d, rcond=None)
    print(f"\n===== A={A} =====")
    print(f"Acoef={Ac:.3f} Bcoef={Bc:.3f} ell(A)={A*Ac+Bc:.4f}")
    # projection of p0 onto span{p1,p2} (Euclidean)
    G = np.array([[p1@p1, p1@p2],[p2@p1, p2@p2]])
    c = np.array([p0@p1, p0@p2])
    ab = np.linalg.solve(G, c)   # Pp0 = ab[0]*p1 + ab[1]*p2
    print(f"P(p0) coords: {ab[0]:.3f}*p1 + {ab[1]:.3f}*p2  (expect {-Ac:.3f}, {-Bc:.3f})")
    resid = p0 - (ab[0]*p1 + ab[1]*p2)
    print(f"||p0||={np.linalg.norm(p0):.1f} ||Pp0||={np.linalg.norm(ab[0]*p1+ab[1]*p2):.1f} ||resid||={np.linalg.norm(resid):.1f}")
    print(f"v vs -resid: {np.linalg.norm(v+resid)/np.linalg.norm(v):.2e}")
    # shapes: print p0, p1, p2 at nodes
    print("   x      |  p0=K^d e^x  |  p1=K^d x    |  p2=K^d 1")
    for i in range(0, len(nodes), 20):
        print(f"  {nodes[i]:+.2f}  | {p0[i]:+.4e} | {p1[i]:+.4e} | {p2[i]:+.4e}")
    # correlation: is p0 ~ alpha*p1 + beta*p2 pointwise?
    # check ratio p0/(ab0*p1+ab1*p2) in the interior
    approx = ab[0]*p1 + ab[1]*p2
    print(f"  max|p0-approx|/max|p0| = {np.max(np.abs(p0-approx))/np.max(np.abs(p0)):.3f}")
