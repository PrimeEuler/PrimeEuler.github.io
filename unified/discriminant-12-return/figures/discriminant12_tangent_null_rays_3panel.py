import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

plt.rcParams.update({
    "text.usetex": True,
    "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}",
})

# Dedicated Discriminant-12 Return tangent/null-ray figure.
# This is intentionally independent of Paper A's publication figure pipeline.
#
# It reproduces the v0.3.3 visual theorem figure:
#   * every fixed-sum shell K=1,...,12, so T=K/2;
#   * emphasized row/column parabola levels u=5,6,7;
#   * exact tangencies at (X,Y)=(+-u/2,0);
#   * corresponding side-view null-generator points (X,T)=(+-u/2,u/2).

Kmax = 12
Rmax = Kmax / 2.0
TANGENT_LEVELS = (5, 6, 7)

curves = [
    dict(a=8, b=4, c=32, color="#b3211a", label=r"$8x+4y=32$"),
    dict(a=4, b=8, c=32, color="#7a3db8", label=r"$4x+8y=32$"),
]


def cone_curve(a, b, c, samples=400):
    x = np.linspace(0.001, c / a - 0.001, samples)
    y = (c - a * x) / b
    valid = y > 0
    x, y = x[valid], y[valid]
    return (x - y) / 2, np.sqrt(x * y), (x + y) / 2


for curve in curves:
    curve["X"], curve["Y"], curve["T"] = cone_curve(
        curve["a"], curve["b"], curve["c"]
    )

Xstar, Tstar = (2 - 4) / 2.0, (2 + 4) / 2.0

table_pts = [
    (xv, yv)
    for xv in range(1, Kmax)
    for yv in range(1, Kmax - xv + 1)
]
assert len(table_pts) == 66

fig = plt.figure(figsize=(16.8, 6.8))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.05], wspace=0.28)

# =================================================================
# Panel (a): flat (X,Y) projection
# =================================================================
axA = fig.add_subplot(gs[0, 0])
axA.set_title(
    "(a) Flat audit: all $K=1,\\ldots,12$ circles\n"
    "with exact $u=5,6,7$ parabola tangencies",
    fontsize=12,
)

theta_c = np.linspace(0, 2 * np.pi, 500)

for K in range(1, Kmax + 1):
    Tc = K / 2.0
    is_tangent_level = K in TANGENT_LEVELS
    axA.plot(
        Tc * np.cos(theta_c),
        Tc * np.sin(theta_c),
        color="#2f6fb0" if is_tangent_level else "0.80",
        lw=1.8 if is_tangent_level else 0.75,
        ls="-" if is_tangent_level else ":",
        alpha=0.95 if is_tangent_level else 0.72,
        zorder=2 if is_tangent_level else 1,
    )

for u in TANGENT_LEVELS:
    Tc = u / 2.0
    angle = 0.23
    axA.annotate(
        rf"$u={u}:\ T={u}/2$",
        (Tc * np.cos(angle), Tc * np.sin(angle)),
        textcoords="offset points",
        xytext=(5, 2),
        fontsize=8,
        color="#2f6fb0",
        zorder=8,
    )

for xv in range(1, Kmax):
    yv = np.linspace(0.001, Kmax - xv, 220)
    Xr = (xv - yv) / 2.0
    Yr = np.sqrt(xv * yv)
    emphasize = xv in TANGENT_LEVELS
    axA.plot(Xr, Yr, color="#7fa7cf",
             lw=1.5 if emphasize else 0.55,
             alpha=0.95 if emphasize else 0.35,
             zorder=4 if emphasize else 1)
    axA.plot(Xr, -Yr, color="#7fa7cf",
             lw=0.8 if emphasize else 0.28,
             alpha=0.55 if emphasize else 0.18,
             zorder=3 if emphasize else 1)

for yv in range(1, Kmax):
    xv = np.linspace(0.001, Kmax - yv, 220)
    Xc_ = (xv - yv) / 2.0
    Yc_ = np.sqrt(xv * yv)
    emphasize = yv in TANGENT_LEVELS
    axA.plot(Xc_, Yc_, color="#b08fcf",
             lw=1.5 if emphasize else 0.55,
             alpha=0.95 if emphasize else 0.35,
             zorder=4 if emphasize else 1)
    axA.plot(Xc_, -Yc_, color="#b08fcf",
             lw=0.8 if emphasize else 0.28,
             alpha=0.55 if emphasize else 0.18,
             zorder=3 if emphasize else 1)

for u in TANGENT_LEVELS:
    Tc = u / 2.0
    axA.plot([-Tc, Tc], [0, 0], "o", ms=5.8, color="#111111", zorder=9)
    axA.annotate(rf"$(-{u}/2,0)$", (-Tc, 0),
                 textcoords="offset points", xytext=(-4, -14),
                 ha="right", fontsize=7.5)
    axA.annotate(rf"$({u}/2,0)$", (Tc, 0),
                 textcoords="offset points", xytext=(4, -14),
                 ha="left", fontsize=7.5)

for xv, yv in table_pts:
    Xl = (xv - yv) / 2.0
    Yl = np.sqrt(xv * yv)
    axA.text(Xl, Yl, str(xv * yv), fontsize=5.1, color="#333333",
             ha="center", va="center", zorder=5)

axA.plot(4 * np.cos(theta_c), 4 * np.sin(theta_c),
         color="#24527a", lw=2.1, ls="--", zorder=5,
         label=r"$x+y=8$")

for curve in curves:
    axA.plot(curve["X"], curve["Y"], color=curve["color"],
             lw=2.4, zorder=6, label=curve["label"])
    axA.plot(curve["X"], -curve["Y"], color=curve["color"],
             lw=2.4, zorder=6)

axA.axhline(0, color="0.83", lw=0.7, zorder=0)
axA.axvline(0, color="0.83", lw=0.7, zorder=0)
axA.set_xlim(-Rmax - 0.4, Rmax + 0.4)
axA.set_ylim(-Rmax - 0.4, Rmax + 0.4)
axA.set_xlabel("$X$")
axA.set_ylabel("$Y$")
axA.set_aspect("equal")
axA.legend(fontsize=7.8, loc="upper right", framealpha=0.9)
for spine in ["top", "right"]:
    axA.spines[spine].set_visible(False)

# =================================================================
# Panel (b): side view (X,T)
# =================================================================
axB = fig.add_subplot(gs[0, 1])
axB.set_title(
    "(b) Side audit: half-step $T=K/2$ shells\n"
    "and the $u=5,6,7$ generator tangencies",
    fontsize=12,
)

axB.plot([-Rmax, 0, Rmax], [Rmax, 0, Rmax], color="0.45", lw=1.4, zorder=1)

for K in range(1, Kmax + 1):
    Tc = K / 2.0
    is_tangent_level = K in TANGENT_LEVELS
    axB.plot([-Tc, Tc], [Tc, Tc],
             color="#2f6fb0" if is_tangent_level else "0.88",
             lw=1.5 if is_tangent_level else 0.6,
             ls="-" if is_tangent_level else ":",
             zorder=2 if is_tangent_level else 0)

# Preserve the v0.3.3 display mesh so the publication figure remains visually stable.
for k in range(0, Kmax + 1):
    axB.plot([k / 2.0, k - Rmax if k - Rmax <= k / 2.0 else k / 2.0],
             [k / 2.0, Rmax if k - Rmax <= k / 2.0 else k / 2.0],
             color="0.91", lw=0.4, zorder=0)
for k in range(-2 * int(Rmax), 2 * int(Rmax) + 1):
    axB.plot([k, k - Rmax], [0, Rmax], color="0.90", lw=0.4, zorder=0)
    axB.plot([-k, Rmax - k], [0, Rmax], color="0.90", lw=0.4, zorder=0)

for xv, yv in table_pts:
    Xl = (xv - yv) / 2.0
    Tl = (xv + yv) / 2.0
    axB.text(Xl, Tl, str(xv * yv), fontsize=5.1, color="#333333",
             ha="center", va="center", zorder=3)

for u in TANGENT_LEVELS:
    Tc = u / 2.0
    axB.plot([-Tc, Tc], [Tc, Tc], "o", ms=5.8, color="#111111", zorder=7)
    axB.annotate(rf"$u={u}$", (Tc, Tc), textcoords="offset points",
                 xytext=(5, 3), fontsize=7.5, color="#111111")

axB.plot([-4, 4], [4, 4], color="#24527a", lw=2.3, ls="--",
         zorder=5, label=r"$x+y=8$")
axB.plot([0], [4], "o", color="#24527a", ms=6, zorder=6)

Xb = np.linspace(-Rmax, Rmax, 300)
for curve in curves:
    Tb = (curve["c"] + (curve["b"] - curve["a"]) * Xb) / (curve["a"] + curve["b"])
    validb = (Tb >= np.abs(Xb)) & (Tb <= Rmax)
    axB.plot(Xb[validb], Tb[validb], color=curve["color"],
             lw=2.4, zorder=5, label=curve["label"])

axB.plot([Xstar], [Tstar], "^", color="#b3211a", ms=7, zorder=6,
         label=r"$Y^2_{\max}$ at $(x,y)=(2,4)$")

axB.legend(fontsize=7.2, loc="upper left", framealpha=0.9)
axB.set_xlim(-Rmax - 0.3, Rmax + 0.3)
axB.set_ylim(-0.3, Rmax + 0.5)
axB.set_xticks([])
axB.set_yticks([])
axB.set_aspect("equal")
for spine in axB.spines.values():
    spine.set_visible(False)

# =================================================================
# Panel (c): full 3D cone with every half-step fixed-T circle
# =================================================================
axC = fig.add_subplot(gs[0, 2], projection="3d")
axC.set_title(
    "(c) 3D audit: complete fixed-$T$ circle family\n"
    "through the $x+y=12$ boundary",
    fontsize=12,
)

theta = np.linspace(0, 2 * np.pi, 120)
Tmesh = np.linspace(0, Rmax, 30)
Tg_, THg = np.meshgrid(Tmesh, theta)
Xg = Tg_ * np.cos(THg)
Yg = Tg_ * np.sin(THg)
axC.plot_surface(Xg, Yg, Tg_, color="0.85", alpha=0.22,
                 linewidth=0, antialiased=True, zorder=1)

for K in range(1, Kmax + 1):
    Tc = K / 2.0
    is_tangent_level = K in TANGENT_LEVELS
    axC.plot(Tc * np.cos(theta), Tc * np.sin(theta), Tc,
             color="#2f6fb0" if is_tangent_level else "0.50",
             lw=1.7 if is_tangent_level else 0.65,
             ls="-" if is_tangent_level else ":",
             zorder=3 if is_tangent_level else 1)

for u in TANGENT_LEVELS:
    Tc = u / 2.0
    axC.scatter([-Tc, Tc], [0, 0], [Tc, Tc], s=20,
                color="#111111", depthshade=False)

axC.plot(4 * np.cos(theta), 4 * np.sin(theta), 4,
         color="#24527a", lw=2.0, ls="--", zorder=4)

for curve in curves:
    axC.plot(curve["X"], curve["Y"], curve["T"],
             color=curve["color"], lw=2.6, zorder=5)
    axC.plot(curve["X"], -curve["Y"], curve["T"],
             color=curve["color"], lw=2.6, zorder=5)

    Xp = np.linspace(curve["X"].min(), curve["X"].max(), 2)
    Yp = np.linspace(-curve["Y"].max() - 0.6, curve["Y"].max() + 0.6, 2)
    Xp_, Yp_ = np.meshgrid(Xp, Yp)
    Tp_ = (curve["c"] + (curve["b"] - curve["a"]) * Xp_) / (curve["a"] + curve["b"])
    axC.plot_surface(Xp_, Yp_, Tp_, color=curve["color"],
                     alpha=0.16, linewidth=0, zorder=3)

axC.set_box_aspect((1.4, 1.4, 1))
axC.set_xlim(-Rmax, Rmax)
axC.set_ylim(-Rmax, Rmax)
axC.set_zlim(0, Rmax)
axC.set_axis_off()
axC.view_init(elev=16, azim=-52)

output_dir = Path(__file__).resolve().parent
out_pdf = output_dir / "discriminant12_tangent_null_rays_3panel.pdf"
out_png = output_dir / "discriminant12_tangent_null_rays_3panel.png"
fig.savefig(out_pdf, dpi=220, bbox_inches="tight", facecolor="white")
fig.savefig(out_png, dpi=220, bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"saved {out_pdf}")
print(f"saved {out_png}")
print("table points:", len(table_pts))
print("tangent-circle radii:", [u / 2 for u in TANGENT_LEVELS])