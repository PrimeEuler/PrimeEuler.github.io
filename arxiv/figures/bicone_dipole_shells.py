"""Bicone shells n=1 (T0=0.5) and n=2 (T0=1.0) for the 1s->2p dipole.
Clean version 2026-10-07: no suptitle/panel-title collision, no backdrop
(matching Fig 1's approved clean style), no gap artifact.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa

ROW = "#7fa7cf"
COL = "#b08fcf"

fig = plt.figure(figsize=(14, 7))

for idx, T0 in enumerate([0.5, 1.0]):
    ax = fig.add_subplot(1, 2, idx+1, projection="3d")
    n = int(2*T0)
    # sphere
    u = np.linspace(0, 2*np.pi, 60); v = np.linspace(0, np.pi, 40)
    xs = T0*np.outer(np.cos(u), np.sin(v))
    ys = T0*np.outer(np.sin(u), np.sin(v))
    ts = T0 + T0*np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(xs, ys, ts, color="#9db8d6", alpha=0.10, edgecolor="none", zorder=1)
    # mesh (meets at T0-circle, no gap)
    us = np.linspace(0.1, 2*T0-0.1, 10)
    for uu in us:
        for mirror, (Tlo, Thi) in [(False, (0, T0)), (True, (T0, 2*T0))]:
            if mirror:
                lo, hi = Tlo, min(Thi, 2*T0-uu/2)
            else:
                lo, hi = max(Tlo, uu/2)+1e-6, Thi
            if hi <= lo: continue
            Ts = np.linspace(lo, hi, 40)
            Te = (2*T0-Ts) if mirror else Ts
            X = uu-Te; Y = np.sqrt(np.maximum(uu*(2*Te-uu), 0))
            for sgn in (1,-1):
                ax.plot(X, sgn*Y, Ts, color=ROW, alpha=0.4, lw=0.7, zorder=3)
                ax.plot(Te-uu, sgn*Y, Ts, color=COL, alpha=0.4, lw=0.7, zorder=3)
    # gold T0-circle
    te = np.linspace(0, 2*np.pi, 100)
    ax.plot(T0*np.cos(te), T0*np.sin(te), np.full_like(te, T0),
            color="#c9962e", lw=2.5, zorder=5)
    ax.scatter([0],[0],[0], color="#333333", s=20, zorder=5)
    ax.scatter([0],[0],[2*T0], color="#333333", s=20, zorder=5)
    # in-figure labels (no panel titles; LaTeX caption covers it)
    label = "|1s⟩" if n == 1 else "|2p⟩"
    lcolor = "#b03030" if n == 1 else "#3030b0"
    ax.text(0, 0, T0, label, fontsize=16, color=lcolor, zorder=10,
            ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.85))
    ax.text(0, 0, -0.15*T0, f"n={n}", fontsize=12, color="#333333",
            ha='center', va='center')
    ax.view_init(elev=18, azim=-60)
    lim = T0*1.35
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-0.25*T0, 2*T0+0.25*T0)
    ax.set_box_aspect((1,1,1))
    ax.set_axis_off()

plt.tight_layout(pad=0.5)
plt.savefig("/home/hatch/workspace/d12/explorations/parabolic-dipole/fig_bicone_dipole_shells.png",
            dpi=150, bbox_inches="tight", pad_inches=0.1)
plt.savefig("/home/hatch/workspace/d12/explorations/parabolic-dipole/fig_bicone_dipole_shells.pdf",
            bbox_inches="tight", pad_inches=0.1)
print("done")
