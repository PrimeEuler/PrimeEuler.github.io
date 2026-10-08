"""Figure 2 for Paper C: T-view of j=5/2 transition circle with Casimir structure.
State parabolas (ladder + Casimir families), both circles, node dots, unit circle ref.
Jeremy 2026-10-08: template approved from T-view trials.
"""
"""Final T-view: j=5/2, state parabolas, both circles, dots, legend, backdrop, no shading."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
from matplotlib.lines import Line2D

T0 = 3.0
j = 2.5
ROW = "#7fa7cf"
COL = "#b08fcf"
GOLD = "#c9962e"
TEAL = "#2a9d8f"

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")

def mesh_parabolas(us, color, ls, alpha, lw):
    for uu in us:
        for Tlo, Thi, mirror in [(0, T0, False), (T0, 2*T0, True)]:
            if mirror:
                lo, hi = Tlo, min(Thi, 2*T0-uu/2)
            else:
                lo, hi = max(Tlo, uu/2)+1e-6, Thi
            if hi <= lo: continue
            Ts = np.linspace(lo, hi, 60)
            Te = (2*T0-Ts) if mirror else Ts
            X = uu-Te
            Y = np.sqrt(np.maximum(uu*(2*Te-uu), 0))
            for sgn in (1,-1):
                ax.plot(X, sgn*Y, Ts, color=color, alpha=alpha, lw=lw, ls=ls, zorder=3)
                ax.plot(Te-uu, sgn*Y, Ts, color=color, alpha=alpha, lw=lw, ls=ls, zorder=3)

mesh_parabolas([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], ROW, '-', 0.55, 1.0)
mesh_parabolas([1.5, 2.5, 3.5, 4.5, 5.5], COL, '--', 0.55, 1.0)

te = np.linspace(0, 2*np.pi, 200)
ax.plot(T0*np.cos(te), T0*np.sin(te), np.full_like(te, T0), color=GOLD, lw=2.5, zorder=5)
r_cas = np.sqrt(T0**2 - 0.25)
ax.plot(r_cas*np.cos(te), r_cas*np.sin(te), np.full_like(te, T0), color=TEAL, lw=1.8, ls='--', zorder=5)
ax.plot(np.cos(te), np.sin(te), np.full_like(te, T0), color="#999999", lw=1.2, ls=':', zorder=5)

for uu in [1.0, 2.0, 3.0, 4.0, 5.0]:  # 5 J+ transitions; no J+ out of top state (u=6)
    Xd = uu - T0
    Yd = np.sqrt(max(uu*(2*T0-uu), 0))
    ax.scatter([Xd],[Yd],[T0], color="#1a1a1a", s=30, zorder=6)
    if Yd > 1e-9:
        ax.scatter([Xd],[-Yd],[T0], color="#1a1a1a", s=30, zorder=6)
for uu in [1.5, 2.5, 3.5, 4.5, 5.5]:
    Xd = uu - T0
    if abs(Xd) < r_cas:
        Yd = np.sqrt(r_cas**2 - Xd**2)
        ax.scatter([Xd],[Yd],[T0], color=TEAL, s=30, zorder=6)
        ax.scatter([Xd],[-Yd],[T0], color=TEAL, s=30, zorder=6)

ax.scatter([0],[0],[0], color="#333333", s=25, zorder=5)
ax.scatter([0],[0],[2*T0], color="#333333", s=25, zorder=5)

ax.set_xlim(-3.8, 3.8); ax.set_ylim(-3.8, 3.8); ax.set_zlim(-0.8, 6.8)
ax.set_box_aspect((1,1,1))
ax.view_init(elev=90, azim=-90)
ax.set_proj_type('ortho')
ax.set_title("T view: j=5/2 transition circle + Casimir (state parabolas)", fontsize=13)

ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor("0.85")
ax.yaxis.pane.set_edgecolor("0.85")
ax.zaxis.pane.set_edgecolor("0.85")
ax.set_xticks([-T0, 0, T0])
ax.set_yticks([-T0, 0, T0])
ax.set_zticks([0, T0, 2*T0])
ax.tick_params(labelsize=9)

legend_handles = [
    Line2D([0],[0], color=GOLD, lw=2.5, label='Transition circle (T$_{0}$=3)'),
    Line2D([0],[0], color=TEAL, lw=1.8, ls='--', label='Casimir circle ($\\sqrt{T_0^2-1/4}$)'),
    Line2D([0],[0], color=ROW, lw=1.2, label='Ladder parabolas'),
    Line2D([0],[0], color=COL, lw=1.2, ls='--', label='Casimir parabolas'),
    Line2D([0],[0], marker='o', color='#1a1a1a', ls='', ms=7, label='Transition nodes (J$_{+}$ landings)'),
    Line2D([0],[0], marker='o', color=TEAL, ls='', ms=7, label='Casimir nodes (state positions)'),
    Line2D([0],[0], color="#999999", lw=1.2, ls=':', label='Unit circle (ref)'),
]
ax.legend(handles=legend_handles, loc='lower right', fontsize=9, framealpha=0.95)

plt.savefig("/home/hatch/workspace/d12/arxiv-prep/paper_c/fig_tview_casimir_ladder.pdf", bbox_inches="tight")
print("saved")
