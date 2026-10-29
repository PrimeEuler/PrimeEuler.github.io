#!/usr/bin/env python3
"""v15.111 handoff, part 1: verify the longitudinal-shift Fourier Hessian
identity <theta^2 - S_ij S^ij> = 0 on flat periodic T^3, for beta^i = d^i b,
theta = div beta = Laplacian b, S_ij = d_i d_j b.

[D] symbolic per-mode: theta_hat(K) = -|K|^2 b_hat(K),
    S_ij_hat(K) = -K_i K_j b_hat(K), hence
    sum_ij |S_ij_hat|^2 = (sum_i K_i^2)^2 |b_hat|^2 = |theta_hat|^2,
    and Parseval turns the per-mode equality into the spatial-average one.
[N] discrete Parseval check: random band-limited b on a 16^3 periodic
    grid; theta and S_ij by exact FFT differentiation; compare means.
"""
import sympy as sp
import numpy as np

K1, K2, K3, bh = sp.symbols("K1 K2 K3 bh")
K = [K1, K2, K3]
theta_hat = -(K1**2 + K2**2 + K3**2) * bh
S_hat = [[-K[i] * K[j] * bh for j in range(3)] for i in range(3)]
lhs = sum(sp.expand(S_hat[i][j]) ** 2 for i in range(3) for j in range(3))
rhs = sp.expand(theta_hat**2)
# |.|^2 for real K and complex bh: use bh*bh_conj as a symbol product
bb = sp.symbols("bb", positive=True)  # stands for |bh|^2
lhs_f = sp.expand(lhs / bh**2)   # coefficient of bh^2 (real-K representative)
rhs_f = sp.expand(rhs / bh**2)
assert sp.simplify(lhs_f - rhs_f) == 0
print("[D] per-mode: sum_ij (K_i K_j)^2 =", sp.factor(lhs_f),
      " == |K|^4 =", sp.factor(rhs_f), "-> identity exact for every K.")

rng = np.random.default_rng(20261029)
n = 16
# random band-limited real b on T^3 (modes |K| <= 3 in index units)
bhat = np.zeros((n, n, n), dtype=complex)
idx = np.fft.fftfreq(n, d=1.0 / n).astype(int)
for i, kx in enumerate(idx):
    for j, ky in enumerate(idx):
        for l, kz in enumerate(idx):
            if 0 < kx * kx + ky * ky + kz * kz <= 9:
                bhat[i, j, l] = rng.normal() + 1j * rng.normal()
b = np.fft.ifftn(bhat).real
Bh = np.fft.fftn(b)
KX, KY, KZ = np.meshgrid(idx, idx, idx, indexing="ij")
Kv = [KX, KY, KZ]
theta = np.fft.ifftn(-(KX**2 + KY**2 + KZ**2) * Bh).real
S = [[np.fft.ifftn(-Kv[i] * Kv[j] * Bh).real for j in range(3)] for i in range(3)]
lhs_v = np.mean(theta**2)
rhs_v = sum(np.mean(S[i][j] ** 2) for i in range(3) for j in range(3))
print(f"[N] grid check: <theta^2> = {lhs_v:.15f}, <S_ij S^ij> = {rhs_v:.15f}, "
      f"diff = {abs(lhs_v - rhs_v):.3e}")
assert abs(lhs_v - rhs_v) < 1e-10 * max(1.0, lhs_v)
print("FOURIER HESSIAN IDENTITY VERIFIED (symbolic [D] + discrete Parseval [N])")
