"""Figure 1 for the bicone dipole note: 2p bicone in sphere, 4 views.

Corrected template (j=1/2, T0=1):
  r_cas = sqrt(0.75) ~ 0.866, delta = 1 - sqrt(0.75) ~ 0.134
  Ladder parabolas: u = 1, 2 (blue #7fa7cf solid, X+ and X-)
  Casimir parabolas: u = 0.366, 1.366 (purple #b08fcf dashed, delta-shifted)
  Gold transition circle r=1 at T=1; teal dashed Casimir circle r=0.866 at T=0.866
  Nodes: 2 black transition at (0, +-1, T=1); 4 teal Casimir at (+-0.5, +-0.7071, T=0.866)
Sphere context: bicone sits in sphere X^2+Y^2+(T-1)^2 = 1.

Four views: T (top-down, ticked X/Y backdrop), X side, Y side, 3D.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

T0 = 1.0
R_CAS = np.sqrt(0.75)
DELTA = T0 - R_CAS
ROW = "#7fa7cf"
COL = "#b08fcf"
GOLD = "#c9962e"
TEAL = "#2a9d8f"
BLACK = "#1a1a1a"

U_LADDER = [1.0, 2.0]
U_CASIMIR = [(i + 0.5) - DELTA for i in range(2)]  # 0.3660, 1.3660


def mesh_parabolas(ax, us, color, ls, alpha, lw):
    """Row/column parabola mesh: X = u-Te and X = Te-u, Y = +-sqrt(u(2Te-u))."""
    for uu in us:
        for Tlo, Thi, mirror in [(0, T0, False), (T0, 2 * T0, True)]:
            lo = max(Tlo, uu / 2) + 1e-6 if not mirror else Tlo
            hi = min(Thi, 2 * T0 - uu / 2) if mirror else Thi
            if hi <= lo:
                continue
            Ts = np.linspace(lo, hi, 60)
            Te = (2 * T0 - Ts) if mirror else Ts
            X = uu - Te
            Y = np.sqrt(np.maximum(uu * (2 * Te - uu), 0))
            for sgn in (1, -1):
                ax.plot(X, sgn * Y, Ts, color=color, alpha=alpha, lw=lw,
                        ls=ls, zorder=3)
                ax.plot(Te - uu, sgn * Y, Ts, color=color, alpha=alpha, lw=lw,
                        ls=ls, zorder=3)


def circles_and_nodes(ax):
    te = np.linspace(0, 2 * np.pi, 200)
    # Gold transition circle r=1 at T=1 (also the sphere equator)
    ax.plot(T0 * np.cos(te), T0 * np.sin(te), np.full_like(te, T0),
            color=GOLD, lw=2.5, zorder=5)
    # Teal dashed Casimir circle r=0.866 at T=0.866
    ax.plot(R_CAS * np.cos(te), R_CAS * np.sin(te), np.full_like(te, R_CAS),
            color=TEAL, lw=1.8, ls="--", zorder=5)
    # Mirrored teal Casimir circle on the glued top cone at T=2*T0-R_CAS=1.134
    T_MIRROR = 2 * T0 - R_CAS
    ax.plot(R_CAS * np.cos(te), R_CAS * np.sin(te), np.full_like(te, T_MIRROR),
            color=TEAL, lw=1.8, ls="--", alpha=0.7, zorder=5)
    # 2 black transition nodes at (0, +-1, T=1)
    Xd, Yd = 0.0, 1.0
    ax.scatter([Xd], [Yd], [T0], color=BLACK, s=60, zorder=6)
    ax.scatter([Xd], [-Yd], [T0], color=BLACK, s=60, zorder=6)
    # 4 teal Casimir nodes at (+-0.5, +-0.7071, T=0.866)
    for uu in U_CASIMIR:
        Xc = uu - R_CAS
        Yc = np.sqrt(max(uu * (2 * R_CAS - uu), 0))
        ax.scatter([Xc], [Yc], [R_CAS], color=TEAL, s=80, zorder=6,
                   edgecolors="white", linewidths=0.8)
        ax.scatter([Xc], [-Yc], [R_CAS], color=TEAL, s=80, zorder=6,
                   edgecolors="white", linewidths=0.8)
    # 4 mirrored teal nodes on the glued top cone at T=1.134 (fainter)
    for uu in U_CASIMIR:
        Xc = uu - R_CAS
        Yc = np.sqrt(max(uu * (2 * R_CAS - uu), 0))
        ax.scatter([Xc], [Yc], [T_MIRROR], color=TEAL, s=80, zorder=6,
                   alpha=0.55, edgecolors="white", linewidths=0.8)
        ax.scatter([Xc], [-Yc], [T_MIRROR], color=TEAL, s=80, zorder=6,
                   alpha=0.55, edgecolors="white", linewidths=0.8)


def sphere_wireframe(ax):
    """Sphere X^2+Y^2+(T-1)^2=1 as faint latitude/meridian lines."""
    for h in [-0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75]:
        r = np.sqrt(max(1 - h * h, 0))
        th = np.linspace(0, 2 * np.pi, 80)
        ax.plot(r * np.cos(th), r * np.sin(th), np.full_like(th, 1 + h),
                color="0.75", alpha=0.28, lw=0.7, zorder=2)
    for phi in np.linspace(0, np.pi, 6, endpoint=False):
        th = np.linspace(0, 2 * np.pi, 80)
        ax.plot(np.sin(th) * np.cos(phi), np.sin(th) * np.sin(phi),
                1 + np.cos(th), color="0.75", alpha=0.28, lw=0.7, zorder=2)


def sphere_circle_side(ax, plane):
    """Faint sphere outline circle for side views."""
    th = np.linspace(0, 2 * np.pi, 120)
    if plane == "YT":  # X side view: circle in Y-T plane
        ax.plot(np.zeros_like(th), np.cos(th), 1 + np.sin(th),
                color="0.75", alpha=0.45, lw=1.0, zorder=2)
    else:  # Y side view: circle in X-T plane
        ax.plot(np.cos(th), np.zeros_like(th), 1 + np.sin(th),
                color="0.75", alpha=0.45, lw=1.0, zorder=2)


def style_axes(ax, xticks, yticks, zticks, xlabel="", ylabel="", grid_on=True):
    ax.grid(grid_on, alpha=0.3)
    ax.xaxis.pane.fill = True
    ax.yaxis.pane.fill = True
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_facecolor((1, 1, 1, 0.7))
    ax.yaxis.pane.set_facecolor((1, 1, 1, 0.7))
    ax.xaxis.pane.set_edgecolor("0.7")
    ax.yaxis.pane.set_edgecolor("0.7")
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.set_zticks(zticks)
    ax.tick_params(axis="x", labelsize=7, colors="0.4")
    ax.tick_params(axis="y", labelsize=7, colors="0.4")
    ax.tick_params(axis="z", labelsize=7, colors="0.4")
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=9, color="0.4")
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=9, color="0.4")


fig = plt.figure(figsize=(14, 12))
TICKS_XY = [-1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5]
TICKS_T = [0, 0.5, 1.0, 1.5, 2.0]
LIM = 1.35

# ---- T view (top-down) ----
ax1 = fig.add_subplot(221, projection="3d")
mesh_parabolas(ax1, U_LADDER, ROW, "-", 0.5, 1.1)
mesh_parabolas(ax1, U_CASIMIR, COL, "--", 0.5, 1.1)
circles_and_nodes(ax1)
ax1.set_xlim(-LIM, LIM)
ax1.set_ylim(-LIM, LIM)
ax1.set_zlim(-0.65, 2.65)
ax1.set_box_aspect((1, 1, 1))
ax1.view_init(elev=90, azim=-90)
ax1.set_proj_type("ortho")
ax1.set_title("T (top-down)", fontsize=11)
style_axes(ax1, TICKS_XY, TICKS_XY, [], xlabel="X", ylabel="Y")

# ---- X side view (from +X: T vertical, Y horizontal) ----
ax2 = fig.add_subplot(222, projection="3d")
mesh_parabolas(ax2, U_LADDER, ROW, "-", 0.5, 1.1)
mesh_parabolas(ax2, U_CASIMIR, COL, "--", 0.5, 1.1)
circles_and_nodes(ax2)
sphere_circle_side(ax2, "YT")
ax2.set_xlim(-LIM, LIM)
ax2.set_ylim(-LIM, LIM)
ax2.set_zlim(-0.65, 2.65)
ax2.set_box_aspect((1, 1, 1))
ax2.view_init(elev=0, azim=0)
ax2.set_proj_type("ortho")
ax2.set_title("X side", fontsize=11)
style_axes(ax2, [], TICKS_XY, TICKS_T, ylabel="Y")

# ---- Y side view (from +Y: T vertical, X horizontal) ----
ax3 = fig.add_subplot(223, projection="3d")
mesh_parabolas(ax3, U_LADDER, ROW, "-", 0.5, 1.1)
mesh_parabolas(ax3, U_CASIMIR, COL, "--", 0.5, 1.1)
circles_and_nodes(ax3)
sphere_circle_side(ax3, "XT")
ax3.set_xlim(LIM, -LIM)
ax3.set_ylim(-LIM, LIM)
ax3.set_zlim(-0.65, 2.65)
ax3.set_box_aspect((1, 1, 1))
ax3.view_init(elev=0, azim=90)
ax3.set_proj_type("ortho")
ax3.set_title("Y side", fontsize=11)
style_axes(ax3, TICKS_XY, [], TICKS_T, xlabel="X")
# invert removed; using reversed xlim instead

# ---- 3D view ----
ax4 = fig.add_subplot(224, projection="3d")
mesh_parabolas(ax4, U_LADDER, ROW, "-", 0.42, 1.0)
mesh_parabolas(ax4, U_CASIMIR, COL, "--", 0.42, 1.0)
circles_and_nodes(ax4)
sphere_wireframe(ax4)
ax4.set_xlim(-LIM, LIM)
ax4.set_ylim(-LIM, LIM)
ax4.set_zlim(-0.65, 2.65)
ax4.set_box_aspect((1, 1, 1))
ax4.view_init(elev=16, azim=-62)
ax4.set_proj_type("ortho")
ax4.set_title("3D", fontsize=11)
style_axes(ax4, TICKS_XY, TICKS_XY, TICKS_T, xlabel="X", ylabel="Y")

fig.suptitle("2p bicone in sphere (T0=1, r_cas=%0.3f, δ=%0.4f)" % (R_CAS, DELTA),
             fontsize=13)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("/home/hatch/workspace/d12/arxiv-prep/e2dipole/fig_bicone_sphere.pdf",
            bbox_inches="tight")
plt.savefig("/home/hatch/workspace/d12/figview_tmp/fig1_rebuilt.png", dpi=130,
            bbox_inches="tight")
print("saved PDF and PNG preview")
print("delta check:", DELTA)
print("u_casimir:", ["%.4f" % u for u in U_CASIMIR])
