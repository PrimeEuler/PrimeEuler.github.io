import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

plt.rcParams.update({
    "text.usetex": True,
    "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}",
})

# Canonical Paper A cutting-plane figure generator.
#
# Geometry:
#   X=(x-y)/2,
#   Y^2=xy,
#   T=(x+y)/2,
#   X^2+Y^2=T^2.
#
# The positive-factor triangle is bounded by x+y=12, hence T<=6.
# The fundamental projection is two-sided, so panel (a) and the conic
# sections in panel (c) include both signs Y=+-sqrt(xy). Panel (b) is the
# flat carrier Y=0 in (X,T) coordinates.
#
# Publication checks encoded here:
#   * every fixed-sum shell K=1,...,12 is shown at T=K/2;
#   * the exact tangent levels u=5,6,7 are emphasized;
#   * row x=u and column y=u side-view segments are clipped to the positive
#     factor triangle, with no negative/duplicate factor levels;
#   * the reflected cuts 8x+4y=32 and 4x+8y=32 appear as complete sections;
#   * the x+y=8 shell is highlighted consistently in all three panels.

KMAX = 12
RMAX = KMAX / 2.0
TANGENT_LEVELS = (5, 6, 7)

ROW_COLOR = "#7fa7cf"
COL_COLOR = "#b08fcf"
SHELL_COLOR = "0.80"
HIGHLIGHT_SHELL = "#24527a"
TANGENT_SHELL = "#2f6fb0"

CURVES = [
    dict(a=8, b=4, c=32, color="#b3211a", label=r"$8x+4y=32$"),
    dict(a=4, b=8, c=32, color="#7a3db8", label=r"$4x+8y=32$"),
]


def cone_curve(a, b, c, samples=500):
    """Positive-factor part of ax+by=c, with upper cone lift returned."""
    x = np.linspace(0.001, c / a - 0.001, samples)
    y = (c - a * x) / b
    valid = y > 0
    x = x[valid]
    y = y[valid]
    X = (x - y) / 2.0
    Y = np.sqrt(x * y)
    T = (x + y) / 2.0
    return X, Y, T


for curve in CURVES:
    curve["X"], curve["Y"], curve["T"] = cone_curve(
        curve["a"], curve["b"], curve["c"]
    )

TABLE_POINTS = [
    (x, y)
    for x in range(1, KMAX)
    for y in range(1, KMAX - x + 1)
]
assert len(TABLE_POINTS) == 66

XSTAR = (2 - 4) / 2.0
TSTAR = (2 + 4) / 2.0

fig = plt.figure(figsize=(16.8, 6.8))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.05], wspace=0.28)

theta = np.linspace(0, 2 * np.pi, 500)

axA = fig.add_subplot(gs[0, 0])
axA.set_title(
    "(a) Flat: complete fixed-sum shells\n"
    "and two-sided conic sections",
    fontsize=12,
)

for K in range(1, KMAX + 1):
    Tc = K / 2.0
    tangent = K in TANGENT_LEVELS
    axA.plot(
        Tc * np.cos(theta),
        Tc * np.sin(theta),
        color=TANGENT_SHELL if tangent else SHELL_COLOR,
        lw=1.6 if tangent else 0.65,
        ls="-" if tangent else ":",
        alpha=0.95 if tangent else 0.72,
        zorder=2 if tangent else 1,
    )

for u in range(1, KMAX):
    y = np.linspace(0.001, KMAX - u, 240)
    X = (u - y) / 2.0
    Y = np.sqrt(u * y)
    emph = u in TANGENT_LEVELS
    axA.plot(X, Y, color=ROW_COLOR, lw=1.35 if emph else 0.5,
             alpha=0.90 if emph else 0.33, zorder=4 if emph else 1)
    axA.plot(X, -Y, color=ROW_COLOR, lw=0.8 if emph else 0.28,
             alpha=0.55 if emph else 0.18, zorder=3 if emph else 1)

for u in range(1, KMAX):
    x = np.linspace(0.001, KMAX - u, 240)
    X = (x - u) / 2.0
    Y = np.sqrt(x * u)
    emph = u in TANGENT_LEVELS
    axA.plot(X, Y, color=COL_COLOR, lw=1.35 if emph else 0.5,
             alpha=0.90 if emph else 0.33, zorder=4 if emph else 1)
    axA.plot(X, -Y, color=COL_COLOR, lw=0.8 if emph else 0.28,
             alpha=0.55 if emph else 0.18, zorder=3 if emph else 1)

for x, y in TABLE_POINTS:
    X = (x - y) / 2.0
    Y = np.sqrt(x * y)
    axA.text(X, Y, str(x * y), fontsize=5.1, color="#333333",
             ha="center", va="center", zorder=6)

label_offsets = {5: (14, -19), 6: (24, -31), 7: (34, -43)}
for u in TANGENT_LEVELS:
    Tc = u / 2.0
    axA.plot([-Tc, Tc], [0, 0], "o", ms=5.0, color="#111111", zorder=8)
    dx, dy = label_offsets[u]
    axA.annotate(
        rf"$u={u}$",
        (Tc, 0),
        textcoords="offset points",
        xytext=(dx, dy),
        ha="left",
        va="center",
        fontsize=8,
        arrowprops=dict(arrowstyle="-", color="#555555", lw=0.65),
        zorder=9,
    )

axA.plot(
    4 * np.cos(theta), 4 * np.sin(theta),
    color=HIGHLIGHT_SHELL, lw=2.1, ls="--", zorder=5,
    label=r"$x+y=8$",
)

for curve in CURVES:
    axA.plot(curve["X"], curve["Y"], color=curve["color"], lw=2.4,
             zorder=7, label=curve["label"])
    axA.plot(curve["X"], -curve["Y"], color=curve["color"], lw=2.4,
             zorder=7)

axA.axhline(0, color="0.84", lw=0.7, zorder=0)
axA.axvline(0, color="0.84", lw=0.7, zorder=0)
axA.set_xlim(-RMAX - 0.4, RMAX + 0.4)
axA.set_ylim(-RMAX - 0.4, RMAX + 0.4)
axA.set_xlabel("$X$")
axA.set_ylabel("$Y$")
axA.set_aspect("equal")
axA.legend(fontsize=7.8, loc="upper right", framealpha=0.9)
for spine in ["top", "right"]:
    axA.spines[spine].set_visible(False)

axB = fig.add_subplot(gs[0, 1])
axB.set_title(
    "(b) Side: flat factor triangle at $Y=0$\n"
    "with exact row/column mesh",
    fontsize=12,
)

axB.plot([-RMAX, 0, RMAX], [RMAX, 0, RMAX], color="0.45", lw=1.4, zorder=2)

for K in range(1, KMAX + 1):
    Tc = K / 2.0
    tangent = K in TANGENT_LEVELS
    axB.plot(
        [-Tc, Tc], [Tc, Tc],
        color=TANGENT_SHELL if tangent else "0.88",
        lw=1.4 if tangent else 0.55,
        ls="-" if tangent else ":",
        zorder=2 if tangent else 0,
    )

for u in range(1, KMAX):
    emph = u in TANGENT_LEVELS
    axB.plot(
        [u / 2.0, u - RMAX],
        [u / 2.0, RMAX],
        color=ROW_COLOR,
        lw=1.15 if emph else 0.45,
        alpha=0.80 if emph else 0.35,
        zorder=3 if emph else 1,
    )
    axB.plot(
        [-u / 2.0, RMAX - u],
        [u / 2.0, RMAX],
        color=COL_COLOR,
        lw=1.15 if emph else 0.45,
        alpha=0.80 if emph else 0.35,
        zorder=3 if emph else 1,
    )

for x, y in TABLE_POINTS:
    X = (x - y) / 2.0
    T = (x + y) / 2.0
    axB.text(X, T, str(x * y), fontsize=5.1, color="#333333",
             ha="center", va="center", zorder=5)

for u in TANGENT_LEVELS:
    Tc = u / 2.0
    axB.plot([-Tc, Tc], [Tc, Tc], "o", ms=5.2, color="#111111", zorder=7)
    axB.annotate(rf"$u={u}$", (Tc, Tc), textcoords="offset points",
                 xytext=(5, 3), fontsize=7.5, color="#111111")

axB.plot([-4, 4], [4, 4], color=HIGHLIGHT_SHELL, lw=2.3, ls="--",
         zorder=6, label=r"$x+y=8$")
axB.plot([0], [4], "o", color=HIGHLIGHT_SHELL, ms=5.5, zorder=7)

Xb = np.linspace(-RMAX, RMAX, 500)
for curve in CURVES:
    Tb = (curve["c"] + (curve["b"] - curve["a"]) * Xb) / (curve["a"] + curve["b"])
    valid = (Tb >= np.abs(Xb)) & (Tb <= RMAX)
    axB.plot(Xb[valid], Tb[valid], color=curve["color"], lw=2.4,
             zorder=6, label=curve["label"])

axB.plot([XSTAR], [TSTAR], "^", color="#b3211a", ms=7, zorder=7,
         label=r"$Y^2_{\max}$ at $(x,y)=(2,4)$")

axB.legend(fontsize=7.1, loc="upper left", framealpha=0.9)
axB.set_xlim(-RMAX - 0.3, RMAX + 0.3)
axB.set_ylim(-0.3, RMAX + 0.5)
axB.set_xticks([])
axB.set_yticks([])
axB.set_aspect("equal")
for spine in axB.spines.values():
    spine.set_visible(False)

axC = fig.add_subplot(gs[0, 2], projection="3d")
axC.set_title(
    "(c) 3D: two-sided cone projection\n"
    "and literal cutting-plane sections",
    fontsize=12,
)

th = np.linspace(0, 2 * np.pi, 140)
r = np.linspace(0, RMAX, 32)
RR, TH = np.meshgrid(r, th)
XC = RR * np.cos(TH)
YC = RR * np.sin(TH)
TC = RR
axC.plot_surface(XC, YC, TC, color="0.85", alpha=0.22,
                 linewidth=0, antialiased=True, zorder=1)

for K in range(1, KMAX + 1):
    Tc = K / 2.0
    tangent = K in TANGENT_LEVELS
    axC.plot(
        Tc * np.cos(th), Tc * np.sin(th), np.full_like(th, Tc),
        color=TANGENT_SHELL if tangent else "0.50",
        lw=1.55 if tangent else 0.6,
        ls="-" if tangent else ":",
        zorder=3 if tangent else 1,
    )

for u in TANGENT_LEVELS:
    Tc = u / 2.0
    axC.scatter([-Tc, Tc], [0, 0], [Tc, Tc], s=20,
                color="#111111", depthshade=False)

axC.plot(4 * np.cos(th), 4 * np.sin(th), np.full_like(th, 4),
         color=HIGHLIGHT_SHELL, lw=2.0, ls="--", zorder=4)

for curve in CURVES:
    axC.plot(curve["X"], curve["Y"], curve["T"],
             color=curve["color"], lw=2.6, zorder=6)
    axC.plot(curve["X"], -curve["Y"], curve["T"],
             color=curve["color"], lw=2.6, zorder=6)

    Xp = np.linspace(curve["X"].min(), curve["X"].max(), 2)
    Yp = np.linspace(-curve["Y"].max() - 0.6, curve["Y"].max() + 0.6, 2)
    XXp, YYp = np.meshgrid(Xp, Yp)
    TTp = (curve["c"] + (curve["b"] - curve["a"]) * XXp) / (curve["a"] + curve["b"])
    axC.plot_surface(XXp, YYp, TTp, color=curve["color"], alpha=0.16,
                     linewidth=0, zorder=4)

axC.set_box_aspect((1.4, 1.4, 1))
axC.set_xlim(-RMAX, RMAX)
axC.set_ylim(-RMAX, RMAX)
axC.set_zlim(0, RMAX)
axC.set_axis_off()
axC.view_init(elev=16, azim=-52)

output_dir = Path(__file__).resolve().parent
out_pdf = output_dir / "fig_cutting_plane_3panel.pdf"
out_png = output_dir / "fig_cutting_plane_3panel.png"
fig.savefig(out_pdf, dpi=220, bbox_inches="tight", facecolor="white")
fig.savefig(out_png, dpi=220, bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"saved {out_pdf}")
print(f"saved {out_png}")
print("table points:", len(TABLE_POINTS))
print("tangent-circle radii:", [u / 2 for u in TANGENT_LEVELS])
