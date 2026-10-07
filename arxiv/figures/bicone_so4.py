"""Bicone (two cones glued T-circle to T-circle) inside the sphere.
SO(4) = su(2)+su(2) geometry: cone 1 carries J, cone 2 carries K,
gluing at common T0 forces j1=j2. Canonical parabola mesh on both cones.

2026-10-07: rebuilt clean per Jeremy's step-by-step diagnosis.
Cones meet exactly at the T0-circle (no gap); the earlier GAP
attempts created visual confusion. Full bicone + sphere + backdrop,
no rendering artifact.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa

T0 = 3.0
ROW = "#7fa7cf"
COL = "#b08fcf"

fig = plt.figure(figsize=(10, 11))
ax = fig.add_subplot(111, projection="3d")

# ---- sphere: X^2+Y^2+(T-T0)^2 = T0^2 ----
u = np.linspace(0, 2 * np.pi, 60)
v = np.linspace(0, np.pi, 40)
xs = T0 * np.outer(np.cos(u), np.sin(v))
ys = T0 * np.outer(np.sin(u), np.sin(v))
ts = T0 + T0 * np.outer(np.ones_like(u), np.cos(v))
ax.plot_surface(xs, ys, ts, color="#9db8d6", alpha=0.08,
                edgecolor="none", zorder=1)

# ---- canonical mesh on both cones, meeting at T0 ----
def mesh_cone(Tlo, Thi, mirror=False):
    us = np.linspace(0.15, 2 * T0 - 0.15, 14)
    for uu in us:
        if mirror:
            lo, hi = Tlo, min(Thi, 2 * T0 - uu / 2)
        else:
            lo, hi = max(Tlo, uu / 2) + 1e-6, Thi
        if hi <= lo:
            continue
        Ts = np.linspace(lo, hi, 60)
        Te = (2 * T0 - Ts) if mirror else Ts
        X = uu - Te
        Y = np.sqrt(np.maximum(uu * (2 * Te - uu), 0))
        for sgn in (1, -1):
            ax.plot(X, sgn * Y, Ts, color=ROW, alpha=0.45, lw=0.9,
                    zorder=3)
            ax.plot(Te - uu, sgn * Y, Ts, color=COL, alpha=0.45, lw=0.9,
                    zorder=3)

mesh_cone(0, T0, mirror=False)
mesh_cone(T0, 2 * T0, mirror=True)

# ---- T0-circle (gold, the gluing), apices ----
te = np.linspace(0, 2 * np.pi, 200)
ax.plot(T0 * np.cos(te), T0 * np.sin(te), np.full_like(te, T0),
        color="#c9962e", lw=3, zorder=5)
ax.scatter([0], [0], [0], color="#333333", s=40, zorder=5)
ax.scatter([0], [0], [2 * T0], color="#333333", s=40, zorder=5)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("T")
ax.set_title("Bicone in the sphere: su(2)$\\oplus$su(2) $\\to$ so(4), "
             "gluing $j_1=j_2$ at the $T_0$-circle",
             fontsize=12)
ax.view_init(elev=18, azim=-60)
ax.set_xlim(-3.8, 3.8)
ax.set_ylim(-3.8, 3.8)
ax.set_zlim(-0.8, 6.8)
ax.set_box_aspect((1, 1, 1))
plt.tight_layout()
plt.savefig("/home/hatch/workspace/d12/explorations/hydrogen-radial/fig_bicone_sphere.png",
            dpi=150)
plt.savefig("/home/hatch/workspace/d12/explorations/hydrogen-radial/fig_bicone_sphere.pdf")
print("done")
