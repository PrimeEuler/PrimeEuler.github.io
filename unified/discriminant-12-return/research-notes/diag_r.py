"""Diagnostics: N-convergence of each moment; small eigenspace of K. Sandbox only."""
import numpy as np
import r_gate as rg
from scipy.linalg import eigvalsh

A = 2.0
print("=== moments vs N (A=2) ===")
for N in [400, 800, 1600, 3200]:
    o = rg.solve_moments(A, N, lam=-1.0, want_cond=(N <= 1600))
    print(f"N={N:5d}  M00={o['M00']:+.6e}  M1x={o['M1x']:+.6e}  "
          f"M0e={o['M0e']:+.6e}  M1e={o['M1e']:+.6e}  "
          f"d0={o['d0']:.4f} d1={o['d1']:.4f} r0={o['r0']:+.5e} r1={o['r1']:+.5e} "
          f"res={o['res']:.1e}", flush=True)

print("\n=== small eigenspace of K (A=2, N=800) ===")
K, k0, kx0, b, info = rg.assemble(2.0, 800, -1.0)
w, V = eigvalsh(K, eigvals=(0, 5))
xs = info['xs']
for i in range(6):
    v = V[:, i]
    # parity: evenness measure
    ev = np.max(np.abs(v - v[::-1])) / np.max(np.abs(v))
    od = np.max(np.abs(v + v[::-1])) / np.max(np.abs(v))
    # overlap with x-source load vector
    ov = abs(v @ b['x']) / (np.linalg.norm(v) * np.linalg.norm(b['x']))
    print(f"eig[{i}]={w[i]:+.6e}  even_resid={ev:.2e} odd_resid={od:.2e} overlap_xsrc={ov:.2e}",
          flush=True)

print("\n=== lambda dependence of d1, r1 (A=2, N=800) ===")
for lam in [-2.0, -1.0, -0.5, -0.2]:
    o = rg.solve_moments(2.0, 800, lam=lam, want_cond=False)
    print(f"lam={lam:+.1f}  d1={o['d1']:.4e} r1={o['r1']:+.6e} r0={o['r0']:+.6e} "
          f"res={o['res']:.1e}", flush=True)
