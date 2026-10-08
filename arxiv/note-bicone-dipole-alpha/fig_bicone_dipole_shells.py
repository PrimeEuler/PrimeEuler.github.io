"""Fig 2: Dipole transition |1s> -> |2p>, concentric nested bicones, corrected template."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROW = "#7fa7cf"; COL = "#b08fcf"; GOLD = "#c9962e"; TEAL = "#2a9d8f"
T0_2p = 1.0
r_cas = np.sqrt(0.75)
delta = T0_2p - r_cas

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection="3d")

def parabolas(T0, T_shift, alpha, lw):
    # Ladder parabolas (blue solid): both X-mirrors for each u
    for uu in [float(i) for i in range(1, int(2*T0)+1)]:
        for lo, hi, mirror in [(uu/2, T0, False), (T0, 2*T0-uu/2, True)]:
            if hi <= lo: continue
            Ts = np.linspace(max(lo,0.01), hi, 40)
            Te = (2*T0-Ts) if mirror else Ts
            X = uu-Te
            Y = np.sqrt(np.maximum(uu*(2*Te-uu), 0))
            Tg = Ts + T_shift
            for sgn in (1,-1):
                ax.plot(X, sgn*Y, Tg, color=ROW, alpha=alpha, lw=lw, zorder=3)
                ax.plot(Te-uu, sgn*Y, Tg, color=ROW, alpha=alpha, lw=lw, zorder=3)
    # Casimir parabolas (purple dashed): both X-mirrors, delta-shifted
    if T0 > 0.6:  # Casimir only for non-degenerate (2p)
        for i in range(int(2*T0)):
            uu = (i+0.5)-delta
            if uu <= 0: continue
            for lo, hi, mirror in [(uu/2, T0, False), (T0, 2*T0-uu/2, True)]:
                if hi <= lo: continue
                Ts = np.linspace(max(lo,0.01), hi, 40)
                Te = (2*T0-Ts) if mirror else Ts
                X = uu-Te
                Y = np.sqrt(np.maximum(uu*(2*Te-uu), 0))
                Tg = Ts + T_shift
                for sgn in (1,-1):
                    ax.plot(X, sgn*Y, Tg, color=COL, alpha=alpha+0.1, lw=lw, ls='--', zorder=3)
                    ax.plot(Te-uu, sgn*Y, Tg, color=COL, alpha=alpha+0.1, lw=lw, ls='--', zorder=3)

# 2p mesh (T0=1, no shift, T in [0,2])
parabolas(1.0, 0, 0.32, 1.0)
# 1s mesh (T0=0.5, shift +0.5, T in [0.5,1.5])
parabolas(0.5, 0.5, 0.32, 1.0)

te = np.linspace(0, 2*np.pi, 150)
# Gold circles (both at T=1, concentric)
ax.plot(1.0*np.cos(te), 1.0*np.sin(te), np.full_like(te, 1.0), color=GOLD, lw=2.5, zorder=5)
ax.plot(0.5*np.cos(te), 0.5*np.sin(te), np.full_like(te, 1.0), color=GOLD, lw=2.0, alpha=0.9, zorder=5)
# 2p teal Casimir
for Tc in [1-(1-r_cas), 1+(1-r_cas)]:
    ax.plot(r_cas*np.cos(te), r_cas*np.sin(te), np.full_like(te, Tc),
            color=TEAL, lw=1.6, ls='--', zorder=5, alpha=0.9)
# 2p nodes
for Tc in [1-(1-r_cas), 1+(1-r_cas)]:
    for Xc, Yc in [(0.5, 0.7071), (0.5, -0.7071), (-0.5, 0.7071), (-0.5, -0.7071)]:
        a = 0.95 if Tc < 1 else 0.6
        ax.scatter([Xc],[Yc],[Tc], color=TEAL, s=50, zorder=6, alpha=a,
                   edgecolors="white", linewidths=0.7)
ax.scatter([0],[1.0],[1.0], color="#1a1a1a", s=50, zorder=6)
ax.scatter([0],[-1.0],[1.0], color="#1a1a1a", s=50, zorder=6)
# 1s node
ax.scatter([0],[0],[1.0], color=TEAL, s=130, zorder=7, edgecolors="white", linewidths=1.2)

# Labels
ax.text(0, 0, 1.0, "|1s⟩", fontsize=14, color="#c0392b", ha='center', va='center',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="0.7", alpha=0.9), zorder=9)
ax.text(0.75, 0, 1.0, "|2p⟩", fontsize=14, color="#2c3e90", ha='center', va='center',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="0.7", alpha=0.9), zorder=9)
ax.text(0, 0, 0.35, "n=1", fontsize=11, color="0.4", ha='center', zorder=8)
ax.text(0, 0, 2.15, "n=2", fontsize=11, color="0.4", ha='center', zorder=8)

# Transition arrow (1s -> 2p)
ax.annotate("", xy=(0.35, 0.5), xytext=(0.15, 0.5),
            arrowprops=dict(arrowstyle="->", color="#c9962e", lw=2),
            xycoords='data', textcoords='data')
# Note: 3D annotate is tricky, skip arrow for now

ax.set_box_aspect((1,1,1.25))
ax.view_init(elev=16, azim=-60)
ax.set_proj_type('ortho')
ax.set_title("Dipole transition |1s⟩ → |2p⟩: nested bicone shells (shared center T=1)", fontsize=13)
ax.grid(False)
ax.xaxis.pane.fill = False; ax.yaxis.pane.fill = False; ax.zaxis.pane.fill = False
ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
plt.savefig("/tmp/fig2_dipole.pdf", bbox_inches="tight")
print("saved PDF")
