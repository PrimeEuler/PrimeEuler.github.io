"""Angle 5d: dissect the optimality condition for l_A = A*Acoef+Bcoef.

Parametrize affine as s*(x-A) + l_A. Then (s*, l_A*) = argmin ||K^d(e^x + s(x-A) + l_A)||^2.
Optimality: <K^d phi_*, p2> = 0 and <K^d phi_*, K^d(x-A)> = 0, where phi_* = e^x + s*(x-A)+l_A*.
Since K^d phi_* = -v_*, this is <v_*, p2>=0, <v_*, q1>=0 with q1=K^d(x-A).

=> l_A* = -[<p0,p2> + s_*<q1,p2>] / ||p2||^2.
Check this identity and examine the two terms.
"""
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
K, xs, nodes = L.K, L.xs, L.nodes
v, Ac, Bc = r['v'], r['A'], r['B']
d = np.exp(xs)
s_star = Ac
l_A_star = A * Ac + Bc
print(f"s*={s_star:.4f} l_A*={l_A_star:.6f}")

p1, *_ = np.linalg.lstsq(K, xs, rcond=None)
p2, *_ = np.linalg.lstsq(K, np.ones_like(xs), rcond=None)
p0, *_ = np.linalg.lstsq(K, d, rcond=None)
q1 = p1 - A * p2   # K^d (x - A)

t1 = p0 @ p2
t2 = s_star * (q1 @ p2)
den = p2 @ p2
print(f"<p0,p2> = {t1:.4f}")
print(f"s_*<q1,p2> = {t2:.4f}")
print(f"||p2||^2 = {den:.4f}")
print(f"l_A* via formula = {-(t1+t2)/den:.6f}  (direct {l_A_star:.6f})")

# orthogonality checks
print(f"\n<v_*,p2>/(||v|| ||p2||) = {(v@p2)/np.linalg.norm(v)/np.linalg.norm(p2):.2e}")
print(f"<v_*,q1>/(||v|| ||q1||) = {(v@q1)/np.linalg.norm(v)/np.linalg.norm(q1):.2e}")

# Now the key: WHY is <p0,p2> + s_*<q1,p2> ~ 0 ?
# Look at it as: <K^d e^x, K^d 1> + s_* <K^d(x-A), K^d 1>.
# Consider the "K-inner product" <a,b>_K := <K^d a, K^d b>.
# Then <p0,p2> = <e^x, 1>_K and <q1,p2> = <x-A, 1>_K.
# So l_A* = -[<e^x,1>_K + s_*<x-A,1>_K]/<1,1>_K.
# i.e. l_A* is (minus) the K-orthogonal projection coefficient of e^x + s_*(x-A) onto constants!
print(f"\n<e^x,1>_K = {t1:.4f}, <x-A,1>_K = {q1@p2:.4f}, <1,1>_K = {den:.4f}")

# What does <.,.>_K look like? Compare <x,1>_K vs <x,1>_{L2} etc.
# If K^d ~ c*L (differential), then <a,b>_K ~ c^2 <La, Lb>.
# For a differential L killing affines: <1,1>_K ~ 0?? But den=||p2||^2=311, not small.
print(f"||p2||^2 = {den:.2f} (K-inner product of 1 with itself)")

# Decompose p0, p1, p2 in SVD basis to see which singular components dominate
U, sv, Vt = np.linalg.svd(K, full_matrices=False)
V = Vt.T
c0 = V.T @ p0   # coefficients of p0 in right-singular basis: p0 = V c0, and K^d e^x coeffs
# K^d e^x = V (U^T e^x / sv)
u0 = U.T @ d
print(f"\nTop 5 singular values: {sv[:5]}")
print(f"p0 coeffs (V-basis) largest indices: {np.argsort(np.abs(c0))[::-1][:5]}")
print(f"  with |c|: {np.sort(np.abs(c0))[::-1][:5]}")
# which left-singular components of e^x dominate p0? (u0/sv)
w0 = u0 / sv
print(f"e^x left-coeffs/sv largest indices: {np.argsort(np.abs(w0))[::-1][:5]}")
print(f"  smallest sv among top contributors: {sv[np.argsort(np.abs(w0))[::-1][:5]].min():.2e}")
