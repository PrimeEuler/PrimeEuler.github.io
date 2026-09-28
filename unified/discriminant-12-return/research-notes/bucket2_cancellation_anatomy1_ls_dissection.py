"""Angle 5: numerical anatomy of the cancellation L0+L1=0.

Goal: understand WHY the Tikhonov-selected affine ell(x)=A*x+B satisfies
ell(A) = o(e^A). Dissect the discrete (8.5)-LS problem.

Setup (code convention, verified against lsq85.py):
  solve  min_{v,A,B} ||K v + X[A;B] + d||^2 + alpha * v'Mm v,  d_j = e^{x_j}
  i.e. K v = -e^x - A x - B  (+ small residual)
  cancellation: ell(A) := A*Acoef + Bcoef = o(e^A)
"""
import sys, time
import numpy as np
import os as _os
sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from bucket2_cancellation_screw import D12Screw
from bucket2_cancellation_lsq85 import Lsq85

t0 = time.time()
screw = D12Screw(tmax=12.0)
print(f"screw built in {time.time()-t0:.1f}s", flush=True)

out = {}
for A in [3.0, 4.0, 5.0]:
    L = Lsq85(screw, A=A, N=120, lam=0.0, dirichlet=False)
    r = L.solve(1.0, alpha=1e-10)
    K, X, Mm = L.K, L.X, L.Mm
    xs = L.xs
    n, ndof = K.shape
    v, Ac, Bc = r['v'], r['A'], r['B']
    ellA = A * Ac + Bc
    print(f"\n===== A={A} =====")
    print(f"gate={r['gate']:.2e}  Acoef={Ac:.6f}  Bcoef={Bc:.6f}")
    print(f"ell(A) = A*Acoef+Bcoef = {ellA:.6f}   e^A={np.exp(A):.3f}   ratio={ellA/np.exp(A):.2e}")
    print(f"I1=A+1={Ac+1:.4f}  I0=B+1={Bc+1:.4f}")

    # --- SVD of K (rectangular: n_coll x ndof) ---
    U, svals, Vt = np.linalg.svd(K, full_matrices=False)
    print(f"K shape {K.shape}, top sv={svals[0]:.4e}, min sv={svals[-1]:.4e}, cond={svals[0]/svals[-1]:.2e}")
    # how many singular values are below sqrt(alpha)?
    print(f"sv < 1e-5: {(svals<1e-5).sum()}, sv < 1e-3: {(svals<1e-3).sum()}")

    # --- affine in Ran(K)? solve K w = X[:,0], X[:,1] (least squares) ---
    for j, nm in enumerate(['x', '1']):
        w, res, *_ = np.linalg.lstsq(K, X[:, j], rcond=None)
        rel = np.linalg.norm(K@w - X[:, j]) / np.linalg.norm(X[:, j])
        print(f"  affine '{nm}' in Ran(K): rel res = {rel:.2e}, ||w||={np.linalg.norm(w):.4e}")

    # --- e^x in Ran(K)? ---
    d = np.exp(xs)
    w, res, *_ = np.linalg.lstsq(K, d, rcond=None)
    rel = np.linalg.norm(K@w - d) / np.linalg.norm(d)
    print(f"  e^x in Ran(K): rel res = {rel:.2e}, ||w||={np.linalg.norm(w):.4e}")

    out[A] = dict(Ac=Ac, Bc=Bc, ellA=ellA, svals=svals)

import json
json.dump({str(k): {kk: (vv.tolist() if isinstance(vv, np.ndarray) else vv)
                    for kk, vv in v.items() if kk != 'svals'}
           for k, v in out.items()},
          open('/home/hatch/workspace/d12/lane_b/sandbox/runs/20260928-200000-bucket2-cancellation-mechanism/anatomy1.json', 'w'))
print("\nsaved.")
