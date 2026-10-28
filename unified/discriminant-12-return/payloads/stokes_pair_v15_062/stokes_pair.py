"""Stokes pair of a polarized tensor wave on the k4 background.
Mode eq (v14.996 fingerprint): Q'' + 3H Q' + (3k^2+4)/tau^2 Q = 0, H = 1/tau
=> Euler equation: p^2 + 2p + (3k^2+4) = 0 -> p = -1 +- i sqrt(3(k^2+1)): log-periodic, decay tau^-1 (record's v14.991 decay)."""
import numpy as np

k = 2.0
w = np.sqrt(3 * (k**2 + 1))
print(f"k = {k}: omega = sqrt(3(k^2+1)) = {w:.4f}; log-period in ln tau = {2 * np.pi / w:.4f}")
s = np.linspace(0, 2 * (2 * np.pi / w), 20001)          # s = ln tau, two full log-periods
QR = np.cos(w * s)                                       # helicity R amplitude (x tau)
QL = 0.6 * np.cos(w * s - np.pi / 3)                     # helicity L: smaller, phase-shifted
u, v = QR**2, QL**2                                      # intensity pair (common tau^-2 and 1/a^2 factors cancel in ratios)
xi = (u - v) / (u + v)                                   # X/T = Stokes V/I
print(f"V/I range over the run: [{xi.min():+.3f}, {xi.max():+.3f}]
# events: vertices of the pair (v = 0 -> xi = +1; u = 0 -> xi = -1) and diagonal crossings (u = v)
def events(mask, label):
    idx = np.where(mask)[0]
    groups = np.split(idx, np.where(np.diff(idx) > 1)[0] + 1)
    print(label, [f"ln tau = {s[g[0]]:.3f}" for g in groups if len(g)])
events(np.abs(QL) < 2e-3, "pure-R vertices (Q_L node, xi=+1):")
events(np.abs(QR) < 2e-3, "pure-L vertices (Q_R node, xi=-1):")
events(np.abs(u - v) < 2e-3, "diagonal crossings (u = v, V/I = 0):")
print("physical intensity envelope: |h|^2 ~ |Q|^2/a^2 ~ tau^-4 (radiation redshift) vs background rho ~ tau^-2: the wave dilutes away")

np.savez("trajectory.npz", s=s, xi=xi, QR=QR, QL=QL)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))
# background: canonical row/column parabola family, ghosted (cone-figure house style, 2D section)
tt = np.linspace(0, 1, 50)
for uu in np.linspace(0.08, 1.0, 12):
    ax2.plot(tt - uu, np.sqrt(np.clip(uu * (2 * 1 - uu), 0, None)) * np.ones_like(tt) * 0 + np.sqrt(np.clip((tt) * (2 * uu - tt), 0, None)), color="#7fa7cf", lw=0.5, alpha=0.18)
    ax2.plot(tt, np.sqrt(np.clip(tt * (2 * uu - tt), 0, None)), color="#b08fcf", lw=0.5, alpha=0.18)
ax1.plot(s, xi, color="#333333", lw=1.4)
ax1.axhline(0, color="#888888", lw=0.7, ls="--"); ax1.axhline(1, color="#888888", lw=0.5); ax1.axhline(-1, color="#888888", lw=0.5)
ax1.set_xlabel("ln tau  (log-time)"); ax1.set_ylabel("V/I = X/T of the helicity intensity pair")
ax1.set_title("Stokes pair of a k=2 tensor wave on the k4 background")
th = np.linspace(0, np.pi, 200)
ax2.plot(np.cos(th), np.sin(th), color="#333333", lw=1.2)
ax2.plot(xi, np.sqrt(1 - xi**2), color="#c0392b", lw=1.6)
ax2.plot([xi[0]], [np.sqrt(1 - xi[0]**2)], "o", color="#c0392b", ms=6)
ax2.set_xlabel("X/T"); ax2.set_ylabel("G/T"); ax2.set_title("the pair's ride on its semicircle")
ax2.set_aspect("equal"); ax2.set_xlim(-1.1, 1.1); ax2.set_ylim(-0.08, 1.12)
plt.tight_layout(); plt.savefig("stokes_pair.png", dpi=130)
print("figure saved")
