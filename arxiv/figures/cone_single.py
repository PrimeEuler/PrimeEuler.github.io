"""Single cone ending at the T0-circle (for paper Figure 1).
Lower cone only — no sphere, no upper cone (the upper cone's mesh
creates a visual 'reflection' artifact at the gold circle in 3D).
Canonical parabola mesh.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa

T0 = 3.0
ROW = "#7fa7cf"
COL = "#b08fcf"

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection="3d")

# ---- canonical mesh on the cone, T in [0,T0], apex at T=0 ----
us = np.linspace(0.15, 2 * T0 - 0.15, 14)
for uu in us:
    lo, hi = max(0, uu / 2) + 1e-6, T0
    if hi <= lo:
        continue
    Ts = np.linspace(lo, hi, 60)
    Te = Ts
    X = uu - Te
    Y = np.sqrt(np.maximum(uu * (2 * Te - uu), 0))
    for sgn in (1, -1):
        ax.plot(X, sgn * Y, Ts, color=ROW, alpha=0.35, lw=0.7, zorder=3)
        ax.plot(Te - uu, sgn * Y, Ts, color=COL, alpha=0.35, lw=0.7, zorder=3)

# ---- cone surface (very faint fill) ----
th = np.linspace(0, 2 * np.pi, 60)
Tt = np.linspace(0.02, T0, 30)
TH, TT = np.meshgrid(th, Tt)
ax.plot_surface(TT * np.cos(TH), TT * np.sin(TH), TT,
                color="#7fa7cf", alpha=0.08, edgecolor="none", zorder=2)

# ---- T0-circle (gold), apex ----
te = np.linspace(0, 2 * np.pi, 200)
ax.plot(T0 * np.cos(te), T0 * np.sin(te), np.full_like(te, T0),
        color="#c9962e", lw=2.5, zorder=5)
ax.scatter([0], [0], [0], color="#333333", s=30, zorder=5)

ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("T")
ax.set_title("Cone ending at the $T_0$-circle: $su(2)$", fontsize=13)
ax.view_init(elev=18, azim=-60)
ax.set_xlim(-3.6, 3.6); ax.set_ylim(-3.6, 3.6); ax.set_zlim(-0.6, 6.6)
ax.set_box_aspect((1, 1, 1))
plt.tight_layout()
plt.savefig("/home/hatch/workspace/d12/explorations/hydrogen-radial/fig_cone_single.png", dpi=150)
plt.savefig("/home/hatch/workspace/d12/explorations/hydrogen-radial/fig_cone_single.pdf")
print("done")
