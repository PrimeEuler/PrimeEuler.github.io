"""4-view bicone figure for the paper: T (top-down), X side, Y side, 3D.
Jeremy 2026-10-07: "do the 4 view. T circle, X-square/circle,
Y-square/circle and then this 3d view". Clean, no backdrop, no artifact.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa

T0 = 3.0
ROW = "#7fa7cf"
COL = "#b08fcf"

def draw_bicone(ax):
    u = np.linspace(0, 2*np.pi, 60); v = np.linspace(0, np.pi, 40)
    xs = T0*np.outer(np.cos(u), np.sin(v))
    ys = T0*np.outer(np.sin(u), np.sin(v))
    ts = T0 + T0*np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(xs, ys, ts, color="#9db8d6", alpha=0.08,
                    edgecolor="none", zorder=1)
    def mesh_cone(Tlo, Thi, mirror):
        us = np.linspace(0.15, 2*T0-0.15, 14)
        for uu in us:
            if mirror:
                lo, hi = Tlo, min(Thi, 2*T0-uu/2)
            else:
                lo, hi = max(Tlo, uu/2)+1e-6, Thi
            if hi <= lo: continue
            Ts = np.linspace(lo, hi, 50)
            Te = (2*T0-Ts) if mirror else Ts
            X = uu-Te
            Y = np.sqrt(np.maximum(uu*(2*Te-uu), 0))
            for sgn in (1,-1):
                ax.plot(X, sgn*Y, Ts, color=ROW, alpha=0.45, lw=0.8, zorder=3)
                ax.plot(Te-uu, sgn*Y, Ts, color=COL, alpha=0.45, lw=0.8, zorder=3)
    mesh_cone(0, T0, mirror=False)
    mesh_cone(T0, 2*T0, mirror=True)
    te = np.linspace(0, 2*np.pi, 200)
    ax.plot(T0*np.cos(te), T0*np.sin(te), np.full_like(te, T0),
            color="#c9962e", lw=2.5, zorder=5)
    ax.scatter([0],[0],[0], color="#333333", s=25, zorder=5)
    ax.scatter([0],[0],[2*T0], color="#333333", s=25, zorder=5)
    ax.set_xlim(-3.8, 3.8); ax.set_ylim(-3.8, 3.8); ax.set_zlim(-0.8, 6.8)
    ax.set_box_aspect((1,1,1))

fig = plt.figure(figsize=(16, 16))
ax1 = fig.add_subplot(221, projection="3d")
draw_bicone(ax1)
ax1.view_init(elev=90, azim=-90)
ax1.set_title("T view: the $T_0$-circle", fontsize=13)
ax1.set_axis_off()
ax2 = fig.add_subplot(222, projection="3d")
draw_bicone(ax2)
ax2.view_init(elev=0, azim=0)
ax2.set_title("X view", fontsize=13)
ax2.set_axis_off()
ax3 = fig.add_subplot(223, projection="3d")
draw_bicone(ax3)
ax3.view_init(elev=0, azim=90)
ax3.set_title("Y view", fontsize=13)
ax3.set_axis_off()
ax4 = fig.add_subplot(224, projection="3d")
draw_bicone(ax4)
ax4.view_init(elev=18, azim=-60)
ax4.set_title("3D: bicone in sphere", fontsize=13)
ax4.set_axis_off()
plt.tight_layout()
plt.savefig("/home/hatch/workspace/d12/explorations/hydrogen-radial/fig_bicone_4view.png", dpi=150, bbox_inches="tight")
plt.savefig("/home/hatch/workspace/d12/explorations/hydrogen-radial/fig_bicone_4view.pdf", bbox_inches="tight")
print("done")
