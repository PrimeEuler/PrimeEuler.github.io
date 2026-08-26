import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ---------------------------------------------------------------
# Everything is framed by the anti-diagonal x+y=12 (K=12, T=6):
# this is the outer triangle edge in panel (b) and the outer
# circle edge in panels (a)/(c). The two example curves -- the
# anti-diagonal x+y=8 and the general line 2x+5y=20 -- both sit
# entirely below (inside) that K=12 boundary. The full
# multiplication table is filled in out to the same edge.
# ---------------------------------------------------------------
a, b, c = 2, 5, 20          # rescaled from 2x+5y=40 so it fits under x+y=12
Kmax = 12
Rmax = Kmax / 2.0           # = 6, the outer T (and circle/triangle) radius

# the ellipse curve: the constant-c line's (x,y) points mapped to (X,Y,T)
xline = np.linspace(0.001, c / a - 0.001, 400)
yline = (c - a * xline) / b
valid = yline > 0
xline, yline = xline[valid], yline[valid]
Xe = (xline - yline) / 2
Ye = np.sqrt(xline * yline)
Te = (xline + yline) / 2
# the Y^2-maximizing point: x=c/(2a)=5, y=c/(2b)=2 -> X=1.5, T=3.5
Xstar, Tstar = (5 - 2) / 2.0, (5 + 2) / 2.0

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

# row AND column parabola arcs (Theorem 3.2's two mirror-image
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

# the general line's ellipse, projected: just (Xe,Ye), forgetting T
axA.plot(Xe, Ye, color="#b3211a", lw=2.4, zorder=4, label=r"$2x+5y=20$")
axA.plot(Xe, -Ye, color="#b3211a", lw=2.4, zorder=4)
axA.plot([Xstar], [np.sqrt(10)], "^", color="#b3211a", ms=7, zorder=5)

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
axB.plot([-4, 4], [4, 4], color="#2f6fb0", lw=2.4, ls="--", zorder=3)
axB.plot([0], [4], "o", color="#2f6fb0", ms=6, zorder=4)  # the tangency point x=y=4
axB.annotate(r"$x+y=8$", (-4, 4), textcoords="offset points",
             xytext=(-4, 10), fontsize=8.5, color="#2f6fb0", ha="right")

# the cutting plane -3X + 7T = 20, edge-on as a straight line: T = (20+3X)/7
Xb = np.linspace(-Rmax, Rmax, 200)
Tb = (c + (b - a) * Xb) / (a + b)
validb = (Tb >= np.abs(Xb)) & (Tb <= Rmax)
axB.plot(Xb[validb], Tb[validb], color="#b3211a", lw=2.4, zorder=3)
axB.plot([Xstar], [Tstar], "^", color="#b3211a", ms=7, zorder=4)
axB.annotate(r"$Y^2_{\max}$ at $(x,y){=}(5,2)$", (Xstar, Tstar), textcoords="offset points",
             xytext=(10, 8), fontsize=8.5, color="#b3211a")

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

# the ellipse
axC.plot(Xe, Ye, Te, color="#b3211a", lw=2.6, zorder=4)
axC.plot(Xe, -Ye, Te, color="#b3211a", lw=2.6, zorder=4)

# the cutting plane, spanned exactly over the ellipse's own X-range
Xp = np.linspace(Xe.min(), Xe.max(), 2)
Yp = np.linspace(-Ye.max() - 0.6, Ye.max() + 0.6, 2)
Xp_, Yp_ = np.meshgrid(Xp, Yp)
Tp_ = (c + (b - a) * Xp_) / (a + b)
axC.plot_surface(Xp_, Yp_, Tp_, color="#b3211a", alpha=0.20, linewidth=0, zorder=3)

axC.set_box_aspect((1.4, 1.4, 1))
axC.set_xlim(-Rmax, Rmax)
axC.set_ylim(-Rmax, Rmax)
axC.set_zlim(0, Rmax)
axC.set_axis_off()
axC.view_init(elev=16, azim=-52)

fig.savefig("fig_cutting_plane_3panel.pdf", dpi=200, bbox_inches="tight", facecolor="white")
fig.savefig("fig_cutting_plane_3panel.png", dpi=200, bbox_inches="tight", facecolor="white")
print("done, table points:", len(table_pts))
