"""2p T-view with nested 1s, ticked backdrop with numbering."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

T0 = 1.0
r_cas = np.sqrt(0.75)
delta = T0 - r_cas
ROW = "#7fa7cf"; COL = "#b08fcf"; GOLD = "#c9962e"; TEAL = "#2a9d8f"

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")

def mesh_parabolas(us, color, ls, alpha, lw):
    for uu in us:
        for Tlo, Thi, mirror in [(0, T0, False), (T0, 2*T0, True)]:
            lo, hi = (Tlo, min(Thi, 2*T0-uu/2)) if mirror else (max(Tlo, uu/2)+1e-6, Thi)
            if hi <= lo: continue
            Ts = np.linspace(lo, hi, 60)
            Te = (2*T0-Ts) if mirror else Ts
            X = uu-Te
            Y = np.sqrt(np.maximum(uu*(2*Te-uu), 0))
            for sgn in (1,-1):
                ax.plot(X, sgn*Y, Ts, color=color, alpha=alpha, lw=lw, ls=ls, zorder=3)
                ax.plot(Te-uu, sgn*Y, Ts, color=color, alpha=alpha, lw=lw, ls=ls, zorder=3)

u_ladder = [1.0, 2.0]
u_casimir = [(i+0.5)-delta for i in range(2)]
mesh_parabolas(u_ladder, ROW, '-', 0.5, 1.2)
mesh_parabolas(u_casimir, COL, '--', 0.5, 1.2)

te = np.linspace(0, 2*np.pi, 200)
ax.plot(T0*np.cos(te), T0*np.sin(te), np.full_like(te, T0), color=GOLD, lw=2.5, zorder=5)
ax.plot(r_cas*np.cos(te), r_cas*np.sin(te), np.full_like(te, r_cas), color=TEAL, lw=1.8, ls='--', zorder=5)
ax.plot(0.5*np.cos(te), 0.5*np.sin(te), np.full_like(te, T0), color=GOLD, lw=2.0, alpha=0.9, zorder=5)

uu = 1.0
Xd, Yd = uu-T0, np.sqrt(max(uu*(2*T0-uu), 0))
ax.scatter([Xd],[Yd],[T0], color="#1a1a1a", s=60, zorder=6)
ax.scatter([Xd],[-Yd],[T0], color="#1a1a1a", s=60, zorder=6)
for uu in u_casimir:
    Xc = uu-r_cas
    Yc = np.sqrt(max(uu*(2*r_cas-uu), 0))
    ax.scatter([Xc],[Yc],[r_cas], color=TEAL, s=80, zorder=6, edgecolors="white", linewidths=0.8)
    ax.scatter([Xc],[-Yc],[r_cas], color=TEAL, s=80, zorder=6, edgecolors="white", linewidths=0.8)
ax.scatter([0],[0],[T0], color=TEAL, s=120, zorder=7, edgecolors="white", linewidths=1.0)

lim = 1.65
ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-0.3, 2.3)
ax.set_box_aspect((1,1,1)); ax.view_init(elev=90, azim=-90); ax.set_proj_type('ortho')
ax.set_title("2p with nested 1s (concentric, shared center T=1)", fontsize=13)

# Ticked backdrop with numbering (like 5/2 figure)
ax.grid(True, alpha=0.3)
ax.xaxis.pane.fill = True
ax.yaxis.pane.fill = True
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_facecolor((1,1,1,0.7))
ax.yaxis.pane.set_facecolor((1,1,1,0.7))
ax.xaxis.pane.set_edgecolor("0.7")
ax.yaxis.pane.set_edgecolor("0.7")
# X and Y ticks with numbers (T is depth in this view)
ticks = [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5]
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_zticks([])
ax.tick_params(axis='x', labelsize=8, colors='0.4')
ax.tick_params(axis='y', labelsize=8, colors='0.4')
ax.set_xlabel("X", fontsize=10, color='0.4')
ax.set_ylabel("Y", fontsize=10, color='0.4')

plt.savefig("/tmp/tview_nested_ticks.pdf", bbox_inches="tight")
print("saved")
