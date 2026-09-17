import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

plt.rcParams.update({
    "text.usetex": True,
    "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}",
})

# -----------------------------------------------------------------
# Signed discriminant-12 carrier on the AM-GM double cone.
#
# Positive arithmetic labels r in U(12)={1,5,7,11} use the factor
# pair (r,1):
#       X=(r-1)/2=c,  T=(r+1)/2=R,  Y^2=r.
# Factor exchange supplies X=-c on the same shell.
#
# The lower cone carries the NEGATED ARITHMETIC LABELS -r.  This is
# a signed-carrier label, not the assertion Y^2=-r (which would have
# no real AM-GM lift).  The real cone invariant remains
#       T^2-X^2=Y^2=|r|.
# The lower sheet is the central cone reflection T -> -T, with the
# same shell radius |T| and the same two-sided Y lift.
#
# Thus the displayed arithmetic carrier is
#       {+/-1,+/-5,+/-7,+/-11} = U(24),
# while every plotted point remains on X^2+Y^2=T^2.
# -----------------------------------------------------------------
data = [
    dict(r=1,  c=0, R=1, color="#b3211a"),
    dict(r=5,  c=2, R=3, color="#e07b1a"),
    dict(r=7,  c=3, R=4, color="#e8a324"),
    dict(r=11, c=5, R=6, color="#f0c419"),
]
Rmax = 6

def shell_label(r, sheet):
    signed_r = sheet * r
    return rf"${signed_r:+d}$" if signed_r < 0 else rf"${signed_r:d}$"

fig = plt.figure(figsize=(16.5, 7.4))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.08], wspace=0.28)

axA = fig.add_subplot(gs[0, 0])
axA.set_title("(a) Transverse view: signed shell pairs", fontsize=12)

theta = np.linspace(0, 2 * np.pi, 400)
for d in data:
    R = d["R"]
    axA.plot(R * np.cos(theta), R * np.sin(theta), color="0.25", lw=1, zorder=1)

for d in data:
    c, r, col = d["c"], d["r"], d["color"]
    half = np.sqrt(r)
    xs = [c, -c] if c != 0 else [0]
    for x in xs:
        axA.plot([x, x], [-half, half], color=col, lw=2.6, zorder=3)
        axA.plot([x], [half], "o", color=col, ms=5, zorder=4)
        axA.plot([x], [-half], "o", color=col, ms=5, zorder=4)
    axA.annotate(rf"$\pm {r}$", (c, half), textcoords="offset points",
                 xytext=(0, 7), ha="center", fontsize=9, color=col)

for cmesh in range(1, 2 * Rmax + 1):
    Tc = np.linspace(cmesh / 2, Rmax, 200)
    Yc = np.sqrt(cmesh * (2 * Tc - cmesh))
    for Xp in (cmesh - Tc, Tc - cmesh):
        axA.plot(Xp, Yc, color="#2f6fb0", lw=0.7, alpha=0.22, zorder=1)
        axA.plot(Xp, -Yc, color="#2f6fb0", lw=0.7, alpha=0.22, zorder=1)

Tp = np.linspace(0.5, Rmax, 300)
Ycol = np.sqrt(2 * Tp - 1)
Xcol = Tp - 1
Xrow = 1 - Tp
for Xp in (Xcol, Xrow):
    axA.plot(Xp, Ycol, color="#2f6fb0", lw=1.6, alpha=0.75, zorder=2)
    axA.plot(Xp, -Ycol, color="#2f6fb0", lw=1.6, alpha=0.75, zorder=2)

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

axB = fig.add_subplot(gs[0, 1])
axB.set_title("(b) Side view: $U(24)$ on the double cone", fontsize=12)
axB.plot([-Rmax, 0, Rmax], [Rmax, 0, Rmax], color="0.55", lw=1.2, zorder=1)
axB.plot([-Rmax, 0, Rmax], [-Rmax, 0, -Rmax], color="0.55", lw=1.2, zorder=1)

for d in data:
    c, r, R, col = d["c"], d["r"], d["R"], d["color"]
    xs = [c, -c] if c != 0 else [0]
    for sheet in (+1, -1):
        Tline = sheet * R
        axB.plot([-R, R], [Tline, Tline], color="0.30", lw=0.9, zorder=1)
        for x in xs:
            axB.plot([x], [Tline], "s", color=col, ms=5, zorder=4)
        xlab = c if c != 0 else 0
        dy = 6 if sheet > 0 else -12
        axB.annotate(shell_label(r, sheet), (xlab, Tline),
                     textcoords="offset points", xytext=(5, dy),
                     ha="left", fontsize=9, color=col)

axB.axhline(0, color="0.35", lw=0.9)
axB.axvline(0, color="0.75", lw=0.6)
axB.set_xlim(-Rmax - 0.8, Rmax + 0.8)
axB.set_ylim(-Rmax - 0.7, Rmax + 0.7)
axB.set_xticks([])
axB.set_yticks([-6, -4, -3, -1, 0, 1, 3, 4, 6])
axB.set_aspect("equal")
for spine in axB.spines.values():
    spine.set_visible(False)

axC = fig.add_subplot(gs[0, 2], projection="3d")
axC.set_title("(c) Signed discriminant-12 double cone", fontsize=12)

for phi in np.linspace(0, 2 * np.pi, 16, endpoint=False):
    tt = np.linspace(0, Rmax, 80)
    xx = tt * np.cos(phi)
    yy = tt * np.sin(phi)
    axC.plot(xx, yy, tt, color="0.82", lw=0.45, alpha=0.55, zorder=0)
    axC.plot(xx, yy, -tt, color="0.82", lw=0.45, alpha=0.55, zorder=0)

for d in data:
    c, r, R, col = d["c"], d["r"], d["R"], d["color"]
    for sheet in (+1, -1):
        axC.plot(R * np.cos(theta), R * np.sin(theta), sheet * R,
                 color="0.25", lw=1.0, alpha=0.9, zorder=1)
    xs = [c, -c] if c != 0 else [0]
    for sheet in (+1, -1):
        for x in xs:
            y0 = np.sqrt(r)
            axC.plot([x], [y0], [sheet * R], "s", color=col, ms=4.5, zorder=4)
            axC.plot([x], [-y0], [sheet * R], "s", color=col, ms=4.5, zorder=4)
        xlab = c if c != 0 else 0
        ylab = np.sqrt(r)
        zlab = sheet * R
        axC.text(xlab, ylab + 0.25, zlab + (0.16 if sheet > 0 else -0.28),
                 shell_label(r, sheet), color=col, fontsize=8)

axC.scatter([0], [0], [0], s=10, color="0.25")
axC.set_box_aspect((2, 2, 2))
axC.set_xlim(-Rmax, Rmax)
axC.set_ylim(-Rmax, Rmax)
axC.set_zlim(-Rmax, Rmax)
axC.set_axis_off()
axC.view_init(elev=18, azim=-60)

fig.suptitle(r"Signed mod-$12$ unit carrier: $U(24)=\{\pm1,\pm5,\pm7,\pm11\}$", fontsize=14)

output_path = Path(__file__).with_name("mod12_v4_cone_triple.png")
fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
print("done")
