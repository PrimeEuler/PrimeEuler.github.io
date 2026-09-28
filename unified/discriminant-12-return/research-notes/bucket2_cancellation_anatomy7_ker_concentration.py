"""Angle 5g: where does P_ker concentrate? Examine P_ker f, P_ker x, P_ker 1
spatially, and dissect the 2x2 ker system M_ker a + b_ker = 0."""
import sys
import numpy as np
import os as _os
sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from bucket2_cancellation_screw import D12Screw
from bucket2_cancellation_lsq85 import Lsq85

screw = D12Screw(tmax=12.0)
A = 5.0
L = Lsq85(screw, A=A, N=120, lam=0.0, dirichlet=False)
K, xs = L.K, L.xs
M_coll, ndof = K.shape
U, sv, Vt = np.linalg.svd(K, full_matrices=False)
Pker = np.eye(M_coll) - U @ U.T
f = np.exp(xs); xx = xs; oo = np.ones_like(xs)
Pkerf, Pkerx, Pkero = Pker @ f, Pker @ xx, Pker @ oo
mid = M_coll // 2
for name, v in [("f", Pkerf), ("x", Pkerx), ("1", Pkero)]:
    lh = np.sum(v[:mid]**2)/np.sum(v**2); rh = np.sum(v[mid:]**2)/np.sum(v**2)
    print(f"Pker {name}: left-half E={lh:.3f} right-half E={rh:.3f} max|x| at x={xs[np.argmax(np.abs(v))]:+.2f}")
# 2x2 system
X = np.column_stack([xx, oo])
Mker = X.T @ Pker @ X
bker = X.T @ Pker @ f
print(f"\nM_ker=\n{Mker}\nb_ker={bker}")
a_ker = np.linalg.solve(Mker, -bker)
print(f"a_ker=({a_ker[0]:.4f},{a_ker[1]:.4f}) l(A)={A*a_ker[0]+a_ker[1]:.6f}")
# Representer: s = Mker^{-1} e_A, l_s = X s, then l(A) = -<Pker l_s, Pker f>
eA = np.array([A, 1.0])
s = np.linalg.solve(Mker, eA)
ls_aff = X @ s
Pker_ls = Pker @ ls_aff
print(f"\ns=Mker^-1 e_A=({s[0]:.6f},{s[1]:.6f})")
print(f"l(A) via -<Pker l_s,Pker f> = {-(Pker_ls @ Pkerf):.6f}")
print(f"||Pker l_s||={np.linalg.norm(Pker_ls):.4e} ||Pker f||={np.linalg.norm(Pkerf):.4e}")
# correlation
print(f"corr(Pker l_s, Pker f) = {(Pker_ls@Pkerf)/np.linalg.norm(Pker_ls)/np.linalg.norm(Pkerf):+.4f}")
