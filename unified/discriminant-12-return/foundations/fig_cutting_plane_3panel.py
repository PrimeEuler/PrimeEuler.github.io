import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ---------------------------------------------------------------
# Everything is framed by the anti-diagonal x+y=12 (K=12, T=6):
# this is the outer triangle edge in panel (b) and the outer
# circle edge in panels (a)/(c). The examples are the anti-diagonal
# x+y=8 and the reflected pair 8x+4y=32, 4x+8y=32 used in Paper A v2.
# The full multiplication table is filled in out to the same edge.
# ---------------------------------------------------------------
Kmax = 12
Rmax = Kmax / 2.0           # = 6, the outer T (and circle/triangle) radius

curves = [
    dict(a=8, b=4, c=32, color="#b3211a", label=r"$8x+4y=32$"),
    dict(a=4, b=8, c=32, color="#7a3db8", label=r"$4x+8y=32$"),
]


def cone_curve(a, b, c, samples=400):
    """Map the positive part of ax+by=c to Paper A's (X,Y,T) cone."""
    x = np.linspace(0.001, c / a - 0.001, samples)
    y = (c - a * x) / b
    valid = y > 0
    x, y = x[valid], y[valid]
    return (x - y) / 2, np.sqrt(x * y), (x + y) / 2


for curve in curves:
    curve["X"], curve["Y"], curve["T"] = cone_curve(
        curve["a"], curve["b"], curve["c"]
    )

# Y^2 is maximal at (x,y)=(c/(2a),c/(2b))=(2,4) on the red cut.
Xstar, Tstar = (2 - 4) / 2.0, (2 + 4) / 2.0

# the full multiplication table, out to the x+y=12 triangle/circle edge
table_pts = [(xv, yv) for xv in range(1, Kmax) for yv in range(1, Kmax - xv + 1)]

fig = plt.figure(figsize=(16.5, 6.6))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.05], wspace=0.28)

# =================================================================
# Panel (a): flat (X,Y) projection -- looking straight down the
# T-axis. Anti-diagonal circles X^2+Y^2=T^2 at fixed T appear as
# concentric circles; the whole table is filled in out to the
# outer T=6 (K=12) circle, and both example curves sit inside it.
# =================================================================
axA = fig.add_subplot(gs[0, 0])
axA.set_title("(a) Flat: projected onto\nthe $(X,Y)$ plane, out to $x{+}y{=}12$", fontsize=12)

theta_c = np.linspace(0, 2 * np.pi, 300)
for K in range(2, Kmax + 1, 2):
    Tc = K / 2.0
    axA.plot(Tc * np.cos(theta_c), Tc * np.sin(theta_c), color="0.78", lw=0.9, zorder=1)
    axA.annotate(f"$K={K}$", (Tc * np.cos(0.28), Tc * np.sin(0.28)),
                 fontsize=7, color="0.55", zorder=1)

# row AND column parabola arcs (the conic theorem's two mirror-image
# families), each clipped at the triangle edge x+y=12. Rows (fixed x,
# y varying) and columns (fixed y, x varying) are mirror images of
# each other across X=0; together they form the same fine triangular
# mesh visible in the (X,T) side view, now projected onto the circles.
# This pairing -- a row arm and a column arm meeting at the diagonal
# x=y -- is exactly the gnomon shape used later for D(n).
for xv in range(1, Kmax):
    yv = np.linspace(0.25, Kmax - xv, 100)
    Xr = (xv - yv) / 2.0
    Yr = np.sqrt(xv * yv)
    axA.plot(Xr, Yr, color="#7fa7cf", lw=0.6, alpha=0.45, zorder=1)
    axA.plot(Xr, -Yr, color="#7fa7cf", lw=0.3, alpha=0.22, zorder=1)
for yv in range(1, Kmax):
    xv = np.linspace(0.25, Kmax - yv, 100)
    Xc_ = (xv - yv) / 2.0
    Yc_ = np.sqrt(xv * yv)
    axA.plot(Xc_, Yc_, color="#b08fcf", lw=0.6, alpha=0.45, zorder=1)
    axA.plot(Xc_, -Yc_, color="#b08fcf", lw=0.3, alpha=0.22, zorder=1)

# every table entry out to the edge, labeled by its product
for xv, yv in table_pts:
    Xl = (xv - yv) / 2.0
    Yl = np.sqrt(xv * yv)
    axA.text(Xl, Yl, str(xv * yv), fontsize=5.3, color="#333333",
              ha="center", va="center", zorder=5,
              bbox=dict(boxstyle="circle,pad=0.03", fc="white", ec="none", alpha=0.7))

# the anti-diagonal x+y=8 (T=4) highlighted
axA.plot(4 * np.cos(theta_c), 4 * np.sin(theta_c), color="#2f6fb0", lw=2.2, ls="--", zorder=3,
         label=r"$x+y=8$")

# the reflected ellipses, projected by forgetting T
for curve in curves:
    axA.plot(curve["X"], curve["Y"], color=curve["color"], lw=2.4,
             zorder=4, label=curve["label"])
    axA.plot(curve["X"], -curve["Y"], color=curve["color"], lw=2.4, zorder=4)

axA.axhline(0, color="0.85", lw=0.7, zorder=0)
axA.axvline(0, color="0.85", lw=0.7, zorder=0)
axA.set_xlim(-Rmax - 0.4, Rmax + 0.4)
axA.set_ylim(-Rmax - 0.4, Rmax + 0.4)
axA.set_xlabel("$X$")
axA.set_ylabel("$Y$")
axA.set_aspect("equal")
axA.legend(fontsize=8.5, loc="upper right", framealpha=0.9)
for spine in ["top", "right"]:
    axA.spines[spine].set_visible(False)

# =================================================================
# Panel (b): side view of the cone, (X,T) plane, Y suppressed.
# The triangle's own edges (the cone's generators) now ARE the
# x+y=12 boundary: they run from the origin up to (+-Rmax, Rmax).
# The whole table is filled in out to that edge; both example
# curves sit inside it.
# =================================================================
axB = fig.add_subplot(gs[0, 1])
axB.set_title("(b) Side view: the table filled in\nout to the $x{+}y{=}12$ triangle edge", fontsize=12)

# cone outline (the generators, Y=0) -- exactly the K=12 boundary
axB.plot([-Rmax, 0, Rmax], [Rmax, 0, Rmax], color="0.45", lw=1.4, zorder=1)

# label the even anti-diagonal shells along the right generator
for K in range(2, Kmax + 1, 2):
    Tc = K / 2.0
    axB.annotate(f"$K={K}$", (Tc, Tc), textcoords="offset points",
                 xytext=(5, 1), fontsize=7, color="0.55", va="center")

# faint row/column mesh X+T=k, T-X=k at integer spacing, clipped to the triangle
for k in range(0, Kmax + 1):
    axB.plot([k / 2.0, k - Rmax if k - Rmax <= k / 2.0 else k / 2.0],
             [k / 2.0, Rmax if k - Rmax <= k / 2.0 else k / 2.0], color="0.9", lw=0.4, zorder=0)
for k in range(-2 * int(Rmax), 2 * int(Rmax) + 1):
    axB.plot([k, k - Rmax], [0, Rmax], color="0.88", lw=0.45, zorder=0)
    axB.plot([-k, Rmax - k], [0, Rmax], color="0.88", lw=0.45, zorder=0)

# every table entry out to the triangle edge, labeled by its product
for xv, yv in table_pts:
    Xl = (xv - yv) / 2.0
    Tl = (xv + yv) / 2.0
    axB.text(Xl, Tl, str(xv * yv), fontsize=5.3, color="#333333",
              ha="center", va="center", zorder=2,
              bbox=dict(boxstyle="circle,pad=0.03", fc="white", ec="none", alpha=0.7))

# the anti-diagonal x+y=8: constant T=4, but X=(x-y)/2 still varies
# as x ranges over the pairs summing to 8 -- so this is a full
# horizontal line segment at T=4, not a single point. (The point
# X=0 on it is just the AM-GM tangency x=y=4, one point among many.)
axB.plot([-4, 4], [4, 4], color="#2f6fb0", lw=2.4, ls="--", zorder=3,
         label=r"$x+y=8$")
axB.plot([0], [4], "o", color="#2f6fb0", ms=6, zorder=4)  # the tangency point x=y=4

# the two cutting planes, edge-on as reflected straight lines
Xb = np.linspace(-Rmax, Rmax, 300)
for curve in curves:
    Tb = (curve["c"] + (curve["b"] - curve["a"]) * Xb) / (curve["a"] + curve["b"])
    validb = (Tb >= np.abs(Xb)) & (Tb <= Rmax)
    axB.plot(Xb[validb], Tb[validb], color=curve["color"], lw=2.4,
             zorder=3, label=curve["label"])
axB.plot([Xstar], [Tstar], "^", color="#b3211a", ms=7, zorder=4,
         label=r"$Y^2_{\max}$ at $(x,y)=(2,4)$")

# Match Paper A v2's legend order: circle, red cut, purple cut, maximum.
handles, labels = axB.get_legend_handles_labels()
order = [0, 1, 2, 3]
axB.legend([handles[i] for i in order], [labels[i] for i in order],
           fontsize=7.2, loc="upper left", framealpha=0.9)

axB.set_xlim(-Rmax - 0.3, Rmax + 0.3)
axB.set_ylim(-0.3, Rmax + 0.5)
axB.set_xticks([])
axB.set_yticks([])
axB.set_aspect("equal")
for spine in axB.spines.values():
    spine.set_visible(False)

# =================================================================
# Panel (c): full 3D cone, drawn out to the same x+y=12 (T=6)
# boundary circle, with the cutting plane and both example curves.
# =================================================================
axC = fig.add_subplot(gs[0, 2], projection="3d")
axC.set_title("(c) The cutting plane sliced through\nthe cone, out to $x{+}y{=}12$", fontsize=12)

theta = np.linspace(0, 2 * np.pi, 80)
Tmesh = np.linspace(0, Rmax, 26)
Tg_, THg = np.meshgrid(Tmesh, theta)
Xg = Tg_ * np.cos(THg)
Yg = Tg_ * np.sin(THg)
axC.plot_surface(Xg, Yg, Tg_, color="0.85", alpha=0.25, linewidth=0, antialiased=True, zorder=1)

for K in range(2, Kmax + 1, 2):
    Tc = K / 2.0
    axC.plot(Tc * np.cos(theta), Tc * np.sin(theta), Tc, color="0.45", lw=0.8, zorder=1)

# the anti-diagonal circle x+y=8 highlighted (T=4)
axC.plot(4 * np.cos(theta), 4 * np.sin(theta), 4, color="#2f6fb0", lw=2.0, ls="--", zorder=2)

# the reflected ellipses and their cutting planes
for curve in curves:
    axC.plot(curve["X"], curve["Y"], curve["T"], color=curve["color"], lw=2.6, zorder=4)
    axC.plot(curve["X"], -curve["Y"], curve["T"], color=curve["color"], lw=2.6, zorder=4)

    Xp = np.linspace(curve["X"].min(), curve["X"].max(), 2)
    Yp = np.linspace(-curve["Y"].max() - 0.6, curve["Y"].max() + 0.6, 2)
    Xp_, Yp_ = np.meshgrid(Xp, Yp)
    Tp_ = (curve["c"] + (curve["b"] - curve["a"]) * Xp_) / (curve["a"] + curve["b"])
    axC.plot_surface(Xp_, Yp_, Tp_, color=curve["color"], alpha=0.16,
                     linewidth=0, zorder=3)

axC.set_box_aspect((1.4, 1.4, 1))
axC.set_xlim(-Rmax, Rmax)
axC.set_ylim(-Rmax, Rmax)
axC.set_zlim(0, Rmax)
axC.set_axis_off()
axC.view_init(elev=16, azim=-52)

output_dir = Path(__file__).resolve().parent
fig.savefig(output_dir / "fig_cutting_plane_3panel.pdf", dpi=200,
            bbox_inches="tight", facecolor="white")
fig.savefig(output_dir / "fig_cutting_plane_3panel.png", dpi=200,
            bbox_inches="tight", facecolor="white")
print("done, table points:", len(table_pts))
