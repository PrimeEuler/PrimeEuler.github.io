import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ---------------------------------------------------------------
# Divisor-summatory figure for n=11, built directly from Paper A's
# fig_cutting_plane_3panel.py geometry and layout.
#
# Paper A coordinates:
#   X=(x-y)/2,  Y=sqrt(xy),  T=(x+y)/2,
#   X^2+Y^2=T^2.
#
# The outer anti-diagonal x+y=12 gives T=6 and contains exactly
# T_11 = 11*12/2 = 66 positive lattice points.
#
# Within that triangle:
#   D(11) = #{(x,y): xy<=11} = 29,
#   A_11  = #{(x,y): x+y<=12 and xy>11} = 37,
# so T_11 = D(11)+A_11 = 66.
#
# The boundary xy=11 becomes
#   Y=sqrt(11) in the flat (X,Y) projection,
#   T^2-X^2=11 in the side (X,T) projection,
# and the vertical plane Y=sqrt(11) cutting the cone in 3D.
# ---------------------------------------------------------------

n = 11
Kmax = 12
Rmax = Kmax / 2.0
sqrt_n = np.sqrt(n)

D = sum(n // k for k in range(1, n + 1))
Tn = n * (n + 1) // 2
An = Tn - D
Hn = sum(1.0 / k for k in range(1, n + 1))
nHn = n * Hn
nlogn = n * np.log(n)

assert D == 29 and Tn == 66 and An == 37

# Full triangular multiplication-table domain used by Paper A.
table_pts = [(xv, yv)
             for xv in range(1, Kmax)
             for yv in range(1, Kmax - xv + 1)]
assert len(table_pts) == Tn

D_pts = [(x, y) for x, y in table_pts if x * y <= n]
A_pts = [(x, y) for x, y in table_pts if x * y > n]
assert len(D_pts) == D and len(A_pts) == An

def cone_coords(points):
    X = np.array([(x-y)/2.0 for x, y in points])
    Y = np.array([np.sqrt(x*y) for x, y in points])
    T = np.array([(x+y)/2.0 for x, y in points])
    return X, Y, T

XD, YD, TD = cone_coords(D_pts)
XA, YA, TA = cone_coords(A_pts)

# Use the same canvas, widths, spacing, and general styling as Paper A.
fig = plt.figure(figsize=(16.5, 6.6))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.05], wspace=0.28)

# restrained classification colors
cD = "#2f6f44"     # divisor region
cA = "#b65a52"     # A_n complement
cH = "#7a3db8"     # n H_n text
cL = "#2f6fb0"     # n log n text
cB = "#8b1a1a"     # xy=n boundary

theta_c = np.linspace(0, 2*np.pi, 300)

# =================================================================
# Panel (a): Paper A flat (X,Y) projection.
# =================================================================
axA = fig.add_subplot(gs[0, 0])
axA.set_title("(a) Flat: projected onto\n"
              r"the $(X,Y)$ plane, out to $x{+}y{=}12$", fontsize=12)

# same even anti-diagonal circles as Paper A
for K in range(2, Kmax + 1, 2):
    Tc = K / 2.0
    axA.plot(Tc*np.cos(theta_c), Tc*np.sin(theta_c),
             color="0.78", lw=0.9, zorder=1)
    axA.annotate(f"$K={K}$",
                 (Tc*np.cos(0.28), Tc*np.sin(0.28)),
                 fontsize=7, color="0.55", zorder=1)

# same row/column parabola mesh
for xv in range(1, Kmax):
    yv = np.linspace(0.25, Kmax - xv, 100)
    Xr = (xv - yv) / 2.0
    Yr = np.sqrt(xv * yv)
    axA.plot(Xr, Yr, color="#7fa7cf", lw=0.6, alpha=0.45, zorder=1)
    axA.plot(Xr, -Yr, color="#7fa7cf", lw=0.3, alpha=0.22, zorder=1)
for yv in range(1, Kmax):
    xv = np.linspace(0.25, Kmax - yv, 100)
    Xc = (xv - yv) / 2.0
    Yc = np.sqrt(xv * yv)
    axA.plot(Xc, Yc, color="#b08fcf", lw=0.6, alpha=0.45, zorder=1)
    axA.plot(Xc, -Yc, color="#b08fcf", lw=0.3, alpha=0.22, zorder=1)

# Full T_11 triangle, partitioned exactly into D(11) and A_11.
axA.scatter(XA, YA, s=19, color=cA, alpha=0.78, zorder=4,
            label=rf"$A_{{11}}={An}$: $xy>11$")
axA.scatter(XD, YD, s=19, color=cD, alpha=0.90, zorder=5,
            label=rf"$D(11)={D}$: $xy\leq 11$")

# xy=11 is a straight line in this projection.
xb = np.linspace(-5, 5, 300)
axA.plot(xb, np.full_like(xb, sqrt_n), color=cB, lw=2.5, zorder=6,
         label=r"$xy=11\;\Longleftrightarrow\;Y=\sqrt{11}$")
axA.plot(xb, -np.full_like(xb, sqrt_n), color=cB, lw=1.1, alpha=0.32, zorder=2)

# exact intersection points with x+y=12
axA.plot([-5, 5], [sqrt_n, sqrt_n], "o", ms=6,
         mfc="white", mec=cB, mew=1.6, zorder=7)
axA.annotate(r"$(1,11)$", (-5, sqrt_n), xytext=(-7, 7),
             textcoords="offset points", ha="right", fontsize=8)
axA.annotate(r"$(11,1)$", (5, sqrt_n), xytext=(7, 7),
             textcoords="offset points", ha="left", fontsize=8)

axA.axhline(0, color="0.85", lw=0.7, zorder=0)
axA.axvline(0, color="0.85", lw=0.7, zorder=0)
axA.set_xlim(-Rmax - 0.4, Rmax + 0.4)
axA.set_ylim(-Rmax - 0.4, Rmax + 0.4)
axA.set_xlabel("$X$")
axA.set_ylabel("$Y$")
axA.set_aspect("equal")
axA.legend(fontsize=7.5, loc="upper right", framealpha=0.92)
for spine in ["top", "right"]:
    axA.spines[spine].set_visible(False)

# =================================================================
# Panel (b): Paper A side (X,T) triangle.
# =================================================================
axB = fig.add_subplot(gs[0, 1])
axB.set_title("(b) Side view: the table filled in\n"
              r"out to the $x{+}y{=}12$ triangle edge", fontsize=12)

# same cone outline
axB.plot([-Rmax, 0, Rmax], [Rmax, 0, Rmax],
         color="0.45", lw=1.4, zorder=1)

# same K-shell labels
for K in range(2, Kmax + 1, 2):
    Tc = K / 2.0
    axB.annotate(f"$K={K}$", (Tc, Tc), textcoords="offset points",
                 xytext=(5, 1), fontsize=7, color="0.55", va="center")

# same row/column straight mesh
for k in range(0, Kmax + 1):
    axB.plot([k/2.0, k-Rmax if k-Rmax <= k/2.0 else k/2.0],
             [k/2.0, Rmax if k-Rmax <= k/2.0 else k/2.0],
             color="0.9", lw=0.4, zorder=0)
for k in range(-2*int(Rmax), 2*int(Rmax)+1):
    axB.plot([k, k-Rmax], [0, Rmax], color="0.88", lw=0.45, zorder=0)
    axB.plot([-k, Rmax-k], [0, Rmax], color="0.88", lw=0.45, zorder=0)

# T_11 point set partitioned by the actual hyperbola.
axB.scatter(XA, TA, s=19, color=cA, alpha=0.78, zorder=3,
            label=rf"$A_{{11}}={An}$")
axB.scatter(XD, TD, s=19, color=cD, alpha=0.90, zorder=4,
            label=rf"$D(11)={D}$")

# Actual hyperbola, clipped exactly at the outer x+y=12 edge:
# sqrt(X^2+11)<=6 => |X|<=5.
Xh = np.linspace(-5, 5, 500)
Th = np.sqrt(Xh**2 + n)
axB.plot(Xh, Th, color=cB, lw=2.6, zorder=5,
         label=r"$T^2-X^2=11$")
axB.plot([-5, 5], [6, 6], "o", ms=6,
         mfc="white", mec=cB, mew=1.6, zorder=6)

# Compact arithmetic key, not a new geometric encoding.
summary = (rf"$T_{{11}}={Tn}=D(11)+A_{{11}}={D}+{An}$" "\n"
           rf"$11\log 11\approx {nlogn:.3f}$"
           rf"$\quad<\quad D(11)={D}\quad<\quad$"
           rf"$11H_{{11}}\approx {nHn:.3f}$")
axB.text(0, 0.72, summary, ha="center", va="bottom", fontsize=8.5,
         bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="0.75", alpha=0.95),
         zorder=10)

axB.legend(fontsize=7.5, loc="upper left", framealpha=0.92)
axB.set_xlim(-Rmax - 0.3, Rmax + 0.3)
axB.set_ylim(-0.3, Rmax + 0.5)
axB.set_xticks([])
axB.set_yticks([])
axB.set_aspect("equal")
for spine in axB.spines.values():
    spine.set_visible(False)

# =================================================================
# Panel (c): Paper A 3D cone and the vertical cutting plane Y=sqrt(11).
# =================================================================
axC = fig.add_subplot(gs[0, 2], projection="3d")
axC.set_title("(c) The divisor plane sliced through\n"
              r"the cone, out to $x{+}y{=}12$", fontsize=12)

theta = np.linspace(0, 2*np.pi, 80)
Tmesh = np.linspace(0, Rmax, 26)
Tg, THg = np.meshgrid(Tmesh, theta)
Xg = Tg * np.cos(THg)
Yg = Tg * np.sin(THg)
axC.plot_surface(Xg, Yg, Tg, color="0.85", alpha=0.25,
                 linewidth=0, antialiased=True, zorder=1)

# same even K rings
for K in range(2, Kmax + 1, 2):
    Tc = K / 2.0
    axC.plot(Tc*np.cos(theta), Tc*np.sin(theta), Tc,
             color="0.45", lw=0.8, zorder=1)

# same row/column mesh visible on cone
for xv in range(1, Kmax):
    yv = np.linspace(0.25, Kmax - xv, 100)
    Xr = (xv-yv)/2.0
    Yr = np.sqrt(xv*yv)
    Tr = (xv+yv)/2.0
    axC.plot(Xr, Yr, Tr, color="#7fa7cf", lw=0.45, alpha=0.25, zorder=1)
for yv0 in range(1, Kmax):
    xv = np.linspace(0.25, Kmax - yv0, 100)
    Xc = (xv-yv0)/2.0
    Yc = np.sqrt(xv*yv0)
    Tc = (xv+yv0)/2.0
    axC.plot(Xc, Yc, Tc, color="#b08fcf", lw=0.45, alpha=0.25, zorder=1)

# lattice points on the positive-Y half of the cone
axC.scatter(XA, YA, TA, s=12, color=cA, alpha=0.78, depthshade=False, zorder=4)
axC.scatter(XD, YD, TD, s=12, color=cD, alpha=0.92, depthshade=False, zorder=5)

# Cutting plane Y=sqrt(11), clipped to the cone segment |X|<=5.
Xp = np.linspace(-5, 5, 2)
Tp = np.linspace(sqrt_n, Rmax, 2)
Xp_, Tp_ = np.meshgrid(Xp, Tp)
Yp_ = np.full_like(Xp_, sqrt_n)
axC.plot_surface(Xp_, Yp_, Tp_, color=cB, alpha=0.13,
                 linewidth=0, zorder=2)

Xsec = np.linspace(-5, 5, 400)
Ysec = np.full_like(Xsec, sqrt_n)
Tsec = np.sqrt(Xsec**2 + n)
axC.plot(Xsec, Ysec, Tsec, color=cB, lw=2.8, zorder=6)
axC.plot([-5, 5], [sqrt_n, sqrt_n], [6, 6], "o",
         ms=5, mfc="white", mec=cB, mew=1.4, zorder=7)

axC.text(0.2, sqrt_n + 0.12, sqrt_n + 0.35,
         r"$Y=\sqrt{11}$", color=cB, fontsize=9)
axC.text(3.0, sqrt_n + 0.18, np.sqrt(20) + 0.25,
         r"$T^2-X^2=11$", color=cB, fontsize=9)

axC.set_box_aspect((1.4, 1.4, 1))
axC.set_xlim(-Rmax, Rmax)
axC.set_ylim(-Rmax, Rmax)
axC.set_zlim(0, Rmax)
axC.set_axis_off()
axC.view_init(elev=16, azim=-52)

fig.suptitle("")
output_dir = Path(__file__).resolve().parent
fig.savefig(output_dir / "fig_divisor_summatory_11_3panel.png",
            dpi=200, bbox_inches="tight", facecolor="white")
print("done:", "T_11 =", Tn, "D(11) =", D, "A_11 =", An)
