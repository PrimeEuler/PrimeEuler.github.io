"""
Divisor-split sign test, addendum (2026-11-07, sandbox).
Jeremy, after the v15.527 delivery: "everything is square
mode content because of the geometric mean."

The precise form: every Voronoi mode's phase is
4 pi sqrt(k x) - pi/4, and sqrt(k x) IS the geometric
mean GM(k, x) of the mode index and the argument -- the
cone's own label. A mode family phase-locks at argument
x exactly when GM(k, x) is an integer for all its members
at once, which happens iff k and x share a squarefree
kernel: at x = s m^2 the locking modes are k = s j^2
(GM = s j m). The seat shells of the main test are the
kernel-1 case (x = m^2, modes j^2, GM = j m).

Prediction, frozen before the run: shells with kernel
s > 1 carry the same one-sided bias, weaker, of size
  P_s = (1/(2 pi)) s^{-3/4} sum_j d(s j^2) j^{-3/2}
(the locking modes' coherent contribution in normalized
units), and the fraction of positive Delta(s m^2) should
fall with s accordingly. If the kernel shells show no
bias, Jeremy's GM reading fails outside the seats.
"""
import numpy as np
from math import pi

N = 2_000_000
GAMMA = 0.5772156649015329

try:
    d = np.load("d_cache.npy")
    assert len(d) == N + 1
except Exception:
    d = np.zeros(N + 1, dtype=np.int32)
    for k in range(1, N + 1):
        d[k::k] += 1
    np.save("d_cache.npy", d)
D = np.cumsum(d, dtype=np.int64)
n_arr = np.arange(N + 1, dtype=np.float64)
M = np.where(n_arr > 0, n_arr * np.log(np.maximum(n_arr, 1)) + (2 * GAMMA - 1) * n_arr, 0.0)
Delta = D - M

print("kernel s | shells s*m^2<=2e6 | mean Delta/x^(1/4) | frac positive | predicted P_s")
for s in (1, 2, 3, 5, 6, 7, 10, 30):
    mmax = int((N // s) ** 0.5)
    ms = np.arange(2, mmax + 1)
    shells = s * ms ** 2
    vals = Delta[shells] / shells ** 0.25
    jmax = int((N // s) ** 0.5)
    jj = np.arange(1, jmax + 1, dtype=np.float64)
    S_s = float(np.sum(d[s * (np.arange(1, jmax + 1) ** 2)].astype(np.float64)
                       * jj ** (-1.5)))
    P_s = (s ** (-0.75)) * S_s / (2 * pi)
    print(f"  s={s:2d} | {len(shells):5d} | {vals.mean():+.4f} | "
          f"{(vals > 0).mean():.3f} | {P_s:+.4f}")

# control: same shells shifted by +1 (off the kernel lattice)
print("\ncontrol, shells s*m^2 + 1:")
for s in (1, 2, 3, 5):
    mmax = int((N // s) ** 0.5)
    ms = np.arange(2, mmax + 1)
    shells = s * ms ** 2 + 1
    vals = Delta[shells] / shells ** 0.25
    print(f"  s={s:2d} | mean {vals.mean():+.4f} | frac positive {(vals > 0).mean():.3f}")
