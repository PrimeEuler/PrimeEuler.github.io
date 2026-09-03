import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ---------------------------------------------------------------
# Geometric mod-12 unit-shell data for The Discriminant-12 Return.
# For r in U(12)={1,5,7,11}, the factor pair (r,1) has
#   T=(r+1)/2=R, |X|=(r-1)/2=c, and Y^2=r=K4.
# ---------------------------------------------------------------
data = [
    dict(K4=1,  c=0, R=1, color="#b3211a", label=r"$\sqrt{1}$"),
    dict(K4=5,  c=2, R=3, color="#e07b1a", label=r"$\sqrt{5}$"),
    dict(K4=7,  c=3, R=4, color="#e8a324", label=r"$\sqrt{7}$"),
    dict(K4=11, c=5, R=6, color="#f0c419", label=r"$\sqrt{11}$"),
]
Rmax = 6

fig = plt.figure(figsize=(16.5, 6.6))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.05], wspace=0.28)

# =================================================================
# Panel (a): flat top-down view -- circles + vertical totative segments
# =================================================================
axA = fig.add_subplot(gs[0, 0])
axA.set_title("(a) Flat: totatives as\nvertical segments", fontsize=12)

theta = np.linspace(0, 2 * np.pi, 400)
for d in data:
    R = d["R"]
    axA.plot(R * np.cos(theta), R * np.sin(theta), color="0.25", lw=1, zorder=1)

for d in data:
    c, K4, R, col = d["c"], d["K4"], d["R"], d["color"]
    half = np.sqrt(K4)
    xs = [c, -c] if c != 0 else [0]
    for x in xs:
        axA.plot([x, x], [-half, half], color=col, lw=2.6, zorder=3)
        axA.plot([x], [half], "o", color=col, ms=5, zorder=4)
        axA.plot([x], [-half], "o", color=col, ms=5, zorder=4)
        axA.annotate(d["label"], (x, half), textcoords="offset points",
                     xytext=(0, 7), ha="center", fontsize=9, color=col)

# Full row/column parabola grid, at the same unit spacing as panel (b)'s
# mesh (c = 1 .. 2*Rmax, matching k = -2*Rmax .. 2*Rmax there): a row x=c
# has X=c-T, Y=sqrt(c(2T-c)); a column y=c is the mirror, X=T-c. Drawn
# light so the highlighted x=1/y=1 pair below still reads as the special
# curve that hits every marker.
for c in range(1, 2 * Rmax + 1):
    Tc = np.linspace(c / 2, Rmax, 200)
    Yc = np.sqrt(c * (2 * Tc - c))
    for Xp in (c - Tc, Tc - c):
        axA.plot(Xp, Yc, color="#2f6fb0", lw=0.7, alpha=0.28, zorder=1)
        axA.plot(Xp, -Yc, color="#2f6fb0", lw=0.7, alpha=0.28, zorder=1)

# The column y=1 (and its mirror, row x=1) parabola: since R-c=1 for every
# entry in `data`, every totative point lies at y=1, i.e. exactly on this
# one parabola. Sampled at T=R it gives X=c precisely for each row above,
# so it threads through all four square-marker points, not just near them.
Tp = np.linspace(0.5, Rmax, 300)
Ycol = np.sqrt(2 * Tp - 1)
Xcol = Tp - 1
Xrow = 1 - Tp
for Xp in (Xcol, Xrow):
    axA.plot(Xp, Ycol, color="#2f6fb0", lw=1.6, alpha=0.85, zorder=2)
    axA.plot(Xp, -Ycol, color="#2f6fb0", lw=1.6, alpha=0.85, zorder=2)

axA.axhline(0, color="0.5", lw=0.8, zorder=0)
axA.axvline(0, color="0.5", lw=0.8, zorder=0)
axA.set_xlim(-Rmax - 0.6, Rmax + 0.6)
axA.set_ylim(-Rmax - 0.6, Rmax + 0.6)
axA.set_xticks(range(-Rmax, Rmax + 1))
axA.set_yticks([])
axA.set_aspect("equal")
for spine in ["top", "right", "left"]:
    axA.spines[spine].set_visible(False)
axA.tick_params(axis="x", labelsize=8)

# =================================================================
# Panel (b): side view of the cone -- (X, T) plane, Y suppressed.
# Each totative's curve has FIXED X = c, so it projects to a
# vertical segment running from the generator T=|X| (vertex, Y=0)
# UP TO its own matched residue circle T=R (Y=sqrt(K4)) -- and
# must stop there, not at the outermost circle.
# =================================================================
axB = fig.add_subplot(gs[0, 1])
axB.set_title("(b) Side view: vertex on the\ngenerator, at X = c", fontsize=12)

# cone outline (the generators, Y=0)
axB.plot([-Rmax, 0, Rmax], [Rmax, 0, Rmax], color="0.55", lw=1.2, zorder=1)

# faint row/column mesh (X+T=const, T-X=const) at unit spacing,
# matching the integer grid used for the axis ticks and residue circles
for k in range(-2 * Rmax, 2 * Rmax + 1):
    axB.plot([k, k - Rmax], [0, Rmax], color="0.88", lw=0.6, zorder=0)
    axB.plot([-k, Rmax - k], [0, Rmax], color="0.88", lw=0.6, zorder=0)
axB.set_xlim(-Rmax - 0.8, Rmax + 0.8)
axB.set_ylim(-0.3, Rmax + 0.5)

# highlighted x=1, y=1 pair (mirror images), matching panels (a) and (c):
# in this (X,T) projection they are straight lines X=1-T and X=T-1, part
# of the grey mesh above but drawn bold here since R-c=1 for every row of
# the totative data -- every square marker below sits exactly on one of them.
Tb = np.linspace(0.5, Rmax, 2)
axB.plot(1 - Tb, Tb, color="#2f6fb0", lw=2.0, alpha=0.85, zorder=2)
axB.plot(Tb - 1, Tb, color="#2f6fb0", lw=2.0, alpha=0.85, zorder=2)

# residue-circle horizontal lines, clipped to the triangle |X|<=T
for Rline in sorted({d["R"] for d in data}):
    axB.plot([-Rline, Rline], [Rline, Rline], color="0.25", lw=1, zorder=1)
    axB.text(-Rmax - 0.75, Rline, str(Rline), va="center", ha="right", fontsize=9)

axB.plot([-Rmax - 0.8, Rmax + 0.8], [0, 0], color="0.25", lw=1, zorder=1)

for d in data:
    c, K4, R, col = d["c"], d["K4"], d["R"], d["color"]
    xs = [c, -c] if c != 0 else [0]
    for x in xs:
        vertexT = abs(x)          # sits on the generator T=|X|
        axB.plot([x, x], [vertexT, R], color=col, lw=2.6, zorder=3)
        axB.plot([x], [vertexT], "o", color=col, ms=5, zorder=4, mfc="white", mew=1.6)
        axB.plot([x], [R], "s", color=col, ms=5, zorder=4)
        axB.annotate(d["label"], (x, R), textcoords="offset points",
                     xytext=(0, 6), ha="center", fontsize=9, color=col)

axB.set_xticks([])
axB.set_yticks(sorted({d["R"] for d in data}))
axB.set_yticklabels([])
axB.set_aspect("equal")
for spine in axB.spines.values():
    spine.set_visible(False)

# =================================================================
# Panel (c): full 3D cone. Each totative's curve is the actual
# hyperbola T^2 - Y^2 = c^2 at fixed X=c, run from the vertex
# (Y=0, on the generator, T=|c|) up to Y=sqrt(K4) where T=R --
# i.e. clipped exactly at its own matched residue ring, not the
# outermost one.
# =================================================================
axC = fig.add_subplot(gs[0, 2], projection="3d")
axC.set_title("(c) The cone in 3D", fontsize=12)

Tmesh = np.linspace(0, Rmax, 26)
th = np.linspace(0, 2 * np.pi, 60)

for Rline in sorted({d["R"] for d in data}):
    axC.plot(Rline * np.cos(theta), Rline * np.sin(theta), Rline,
              color="0.2", lw=1.1, zorder=1)

for d in data:
    c, K4, R, col = d["c"], d["K4"], d["R"], d["color"]
    xs = [c, -c] if c != 0 else [0]
    for x in xs:
        Yv = np.linspace(0, np.sqrt(K4), 80)
        Tv = np.sqrt(Yv**2 + x**2)
        Xv = np.full_like(Yv, x)
        axC.plot(Xv, Yv, Tv, color=col, lw=2.4, zorder=3)
        axC.plot(Xv, -Yv, Tv, color=col, lw=2.4, zorder=3)  # mirror in Y too
        axC.plot([x], [0], [abs(x)], "o", color=col, ms=4, zorder=4, mfc="white", mew=1.2)
        axC.plot([x], [np.sqrt(K4)], [R], "s", color=col, ms=4, zorder=4)
        axC.text(x, np.sqrt(K4) + 0.3, R + 0.15, d["label"], color=col, fontsize=8)

for c in range(1, 2 * Rmax + 1):
    Tc = np.linspace(c / 2, Rmax, 150)
    Yc = np.sqrt(c * (2 * Tc - c))
    for Xp in (c - Tc, Tc - c):
        axC.plot(Xp, Yc, Tc, color="#2f6fb0", lw=0.6, alpha=0.22, zorder=1)
        axC.plot(Xp, -Yc, Tc, color="#2f6fb0", lw=0.6, alpha=0.22, zorder=1)

for Xp in (Xcol, Xrow):
    axC.plot(Xp, Ycol, Tp, color="#2f6fb0", lw=1.6, alpha=0.85, zorder=2)
    axC.plot(Xp, -Ycol, Tp, color="#2f6fb0", lw=1.6, alpha=0.85, zorder=2)

axC.set_box_aspect((2, 2, 1))
axC.set_xlim(-Rmax, Rmax)
axC.set_ylim(-Rmax, Rmax)
axC.set_zlim(0, Rmax)
axC.set_axis_off()
axC.view_init(elev=18, azim=-60)

fig.suptitle("")
# Caption removed here deliberately: paper.tex supplies its own \caption{} for this
# figure via the normal LaTeX figure environment. Baking the caption text into the
# image pixels as well would duplicate it in the compiled PDF.

output_path = Path(__file__).with_name("mod12_v4_cone_triple.png")
fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
print("done")
