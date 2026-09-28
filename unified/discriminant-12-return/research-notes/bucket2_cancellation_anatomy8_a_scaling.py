"""Angle 5h: A-scaling of the ker mechanism. Verify selection principle at
multiple A, track corr(w,Pker f) and l(A). Also test parity angle: does the
(-) channel give a consistent picture?"""
import sys
import numpy as np
import os as _os
sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from bucket2_cancellation_screw import D12Screw
from bucket2_cancellation_lsq85 import Lsq85

screw = D12Screw(tmax=12.0)
print("=== ker-selection vs Tikhonov across A (plus channel) ===")
for A in [2.0, 3.0, 4.0, 5.0]:
    L = Lsq85(screw, A=A, N=120, lam=0.0, dirichlet=False)
    r = L.solve(1.0, alpha=1e-10)
    K, xs = L.K, L.xs
    Mc, nd = K.shape
    U, sv, Vt = np.linalg.svd(K, full_matrices=False)
    Pker = np.eye(Mc) - U @ U.T
    f = np.exp(xs); X = np.column_stack([xs, np.ones_like(xs)])
    Mker = X.T @ Pker @ X; bker = X.T @ Pker @ f
    a_ker = np.linalg.solve(Mker, -bker)
    lker = A*a_ker[0]+a_ker[1]; ltrue = A*r['A']+r['B']
    # representer orthogonality
    eA = np.array([A,1.0]); s = np.linalg.solve(Mker, eA)
    w = Pker @ (X @ s); pf = Pker @ f
    corr = (w@pf)/np.linalg.norm(w)/np.linalg.norm(pf)
    print(f"A={A}: match={np.allclose(a_ker,[r['A'],r['B']],atol=1e-6)} l_ker={lker:+.4f} l_true={ltrue:+.4f} corr(w,Pkerf)={corr:+.2e} l/e^A={ltrue/np.exp(A):+.2e}")
