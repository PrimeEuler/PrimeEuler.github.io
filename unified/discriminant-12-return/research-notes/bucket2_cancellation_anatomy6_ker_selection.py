"""Angle 5f: is a_* driven by ker(K^T) projection?
Compute a_ker = argmin_a ||P_ker (Xa+f)||^2 and compare its l(A) to the true one.
Also decompose the W_alpha objective across sigma to see which components pick (A,B)."""
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
    K, xs = L.K, L.xs
    M_coll, ndof = K.shape
    U, sv, Vt = np.linalg.svd(K, full_matrices=False)
    f = np.exp(xs); X = np.column_stack([xs, np.ones_like(xs)])
    Pker = np.eye(M_coll) - U @ U.T
    # a_ker = argmin ||Pker(Xa+f)||^2
    PX = Pker @ X; Pf = Pker @ f
    a_ker, *_ = np.linalg.lstsq(PX, -Pf, rcond=None)
    l_ker = A * a_ker[0] + a_ker[1]
    l_true = A * r['A'] + r['B']
    print(f"A={A}: a_ker=({a_ker[0]:.4f},{a_ker[1]:.4f}) l_ker(A)={l_ker:.4f} | true l(A)={l_true:.4f} | e^A={np.exp(A):.1f}")
    # How much of f, X is in ker?
    print(f"   ||Pker f||/||f||={np.linalg.norm(Pf)/np.linalg.norm(f):.4f}, ||Pker X||_F/||X||_F={np.linalg.norm(PX)/np.linalg.norm(X):.4f}")
