import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import shutil
import subprocess

# Paper A 4-view cutting-plane figure generator (matplotlib only, no image model).
#
# BUILD-ONCE ARCHITECTURE: every curve is a single 3D point set on the cone
#   X=(x-y)/2, Y=+-sqrt(xy), T=(x+y)/2, X^2+Y^2=T^2,
# bounded by x+y<=12 (T<=6). The row/column parabolic mesh is determined by
# the x,y rows/columns, lifted to the cone once. The four panels are four
# views (projections) of that SAME object:
#   (a) T-Circle   : look down T -> plot (X, Y)
#   (b) X-Triangle : look down Y -> plot (X, T)
#   (c) Y-Triangle : look down X -> plot (Y, T)
#   (d) 3D Cone    : perspective  -> plot (X, Y, T)

# usetex needs a working LaTeX install *including* the type1cm/type1ec
# packages matplotlib's texmanager requires; pdflatex alone is not enough
# (this VM's TeX Live lacks them), so probe with kpsewhich before enabling.
def _has_full_latex():
    if not shutil.which("pdflatex") or not shutil.which("kpsewhich"):
        return False
    try:
        return subprocess.run(["kpsewhich", "type1cm.sty"],
                              capture_output=True).returncode == 0
    except Exception:
        return False


HAS_LATEX = _has_full_latex()
plt.rcParams.update({
    "text.usetex": HAS_LATEX,
    "font.family": "serif",
    "font.size": 10,
})
if HAS_LATEX:
    plt.rcParams["text.latex.preamble"] = r"\usepackage{amsmath}\usepackage{amssymb}"

KMAX = 12
RMAX = KMAX / 2.0
TANGENT_LEVELS = (5, 6, 7)

ROW_COLOR = "#7fa7cf"
COL_COLOR = "#b08fcf"
SHELL_COLOR = "0.80"
HIGHLIGHT_SHELL = "#24527a"
TANGENT_SHELL = "#2f6fb0"

CUTS = [
    dict(a=8, b=4, c=32, color="#b3211a", label="$8x+4y=32$"),
    dict(a=4, b=8, c=32, color="#7a3db8", label="$4x+8y=32$"),
]

# --------------------------------------------------------------------------
# Build the object: curves as (N,3) [X, Y, T] point sets, plus marker points.
# --------------------------------------------------------------------------
curves = []    # dict(pts, kind, ...)
markers = []   # dict(pt, kind)


def add_curve(pts, kind, **kw):
    curves.append(dict(pts=np.asarray(pts, dtype=float), kind=kind, **kw))


def add_marker(pt, kind, **kw):
    markers.append(dict(pt=np.asarray(pt, dtype=float), kind=kind, **kw))


def ring(r, t, n=400):
    th = np.linspace(0, 2 * np.pi, n)
    return np.column_stack([r * np.cos(th), r * np.sin(th), np.full(n, t)])


# Row/column parabolic mesh, lifted to the cone:
#   row x=u:    X = u-T, Y = +-sqrt(u(2T-u))
#   column y=u: X = T-u, Y = +-sqrt(u(2T-u)),  T in [u/2, 6]
for u in range(1, KMAX):
    T = np.linspace(u / 2.0, RMAX, 160)
    Y = np.sqrt(u * (2 * T - u))
    emph = u in TANGENT_LEVELS
    for s in (1.0, -1.0):
        add_curve(np.column_stack([u - T, s * Y, T]), "row", u=u, emph=emph)
        add_curve(np.column_stack([T - u, s * Y, T]), "col", u=u, emph=emph)

# Fixed-sum shells x+y=K -> ring of radius K/2 at height T=K/2
for K in range(1, KMAX + 1):
    add_curve(ring(K / 2.0, K / 2.0), "shell", K=K, emph=(K in TANGENT_LEVELS))

# Highlight shell x+y=8
add_curve(ring(4.0, 4.0), "shell8", label="$x+y=8$")

# The two conic sections, both Y signs
for cut in CUTS:
    x = np.linspace(0.001, cut["c"] / cut["a"] - 0.001, 600)
    y = (cut["c"] - cut["a"] * x) / cut["b"]
    ok = y > 0
    x, y = x[ok], y[ok]
    X, Yv, T = (x - y) / 2.0, np.sqrt(x * y), (x + y) / 2.0
    add_curve(np.column_stack([X, Yv, T]), "cut",
              color=cut["color"], label=cut["label"])
    add_curve(np.column_stack([X, -Yv, T]), "cut", color=cut["color"])

# Marker points (3D objects too)
for u in TANGENT_LEVELS:          # tangency: (X,Y,T) = (+-u/2, 0, u/2)
    add_marker([u / 2.0, 0.0, u / 2.0], "tangent")
    add_marker([-u / 2.0, 0.0, u / 2.0], "tangent")
add_marker([-1.0, 2 * np.sqrt(2), 3.0], "ymax")   # Y^2max at (x,y)=(2,4)
add_marker([0.0, 4.0, 4.0], "shell8pt")           # (x,y)=(4,4) on x+y=8
add_marker([0.0, -4.0, 4.0], "shell8pt")


# --------------------------------------------------------------------------
# Views: project the same object four ways.
# --------------------------------------------------------------------------
def proj(pts, view):
    if view == "a":
        return pts[:, 0], pts[:, 1]
    if view == "b":
        return pts[:, 0], pts[:, 2]
    return pts[:, 1], pts[:, 2]


def curve_style(c, view):
    k = c["kind"]
    if k in ("row", "col"):
        color = ROW_COLOR if k == "row" else COL_COLOR
        if view == "d":
            # clearly visible mesh in 3D
            return dict(color=color, lw=1.3 if c["emph"] else 0.9,
                        alpha=0.9 if c["emph"] else 0.55,
                        zorder=3 if c["emph"] else 2)
        return dict(color=color, lw=1.35 if c["emph"] else 0.5,
                    alpha=0.90 if c["emph"] else 0.33,
                    zorder=4 if c["emph"] else 1)
    if k == "shell":
        if c["emph"]:
            return dict(color=TANGENT_SHELL, lw=1.6 if view != "d" else 1.55,
                        ls="-", alpha=0.95, zorder=3)
        if view == "a":
            return dict(color=SHELL_COLOR, lw=0.65, ls=":", alpha=0.72, zorder=1)
        if view == "d":
            return dict(color="0.50", lw=0.6, ls=":", alpha=0.8, zorder=1)
        return dict(color="0.88", lw=0.55, ls=":", alpha=0.9, zorder=0)
    if k == "shell8":
        return dict(color=HIGHLIGHT_SHELL, lw=2.1, ls="--", alpha=0.95, zorder=5)
    if k == "cut":
        ls = "--" if (view == "c" and c.get("color") == "#b3211a") else "-"
        return dict(color=c["color"], lw=2.6 if view == "d" else 2.4,
                    ls=ls, alpha=0.95, zorder=7)
    raise ValueError(k)


def marker_style(m, view):
    k = m["kind"]
    if k == "tangent":
        return dict(marker="o", ms=5.0, color="#111111", zorder=8)
    if k == "ymax":
        return dict(marker="^", ms=7, color="#b3211a", zorder=8)
    if k == "shell8pt":
        return dict(marker="o", ms=5.5, color=HIGHLIGHT_SHELL, zorder=7)
    raise ValueError(k)


fig = plt.figure(figsize=(20.5, 6.4))
gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1, 1.08], wspace=0.24)

# ------------------------------------------------------------ (a) T-Circle
axA = fig.add_subplot(gs[0, 0])
axA.set_title("(a) T-Circle", fontsize=11)
for c in curves:
    x, y = proj(c["pts"], "a")
    st = curve_style(c, "a")
    axA.plot(x, y, label=c.get("label"), **st)
for m in markers:
    x, y = proj(m["pt"][None, :], "a")
    st = marker_style(m, "a")
    axA.plot(x, y, ls="none", **st)
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

# ----------------------------------------------------------- (b) X-Triangle
axB = fig.add_subplot(gs[0, 1])
axB.set_title("(b) X-Triangle", fontsize=11)
axB.plot([-RMAX, 0, RMAX], [RMAX, 0, RMAX], color="0.45", lw=1.4, zorder=2)
for c in curves:
    x, y = proj(c["pts"], "b")
    axB.plot(x, y, **curve_style(c, "b"))
for m in markers:
    x, y = proj(m["pt"][None, :], "b")
    axB.plot(x, y, ls="none", **marker_style(m, "b"))
axB.set_xlim(-RMAX - 0.3, RMAX + 0.3)
axB.set_ylim(-0.3, RMAX + 0.5)
axB.set_xticks([])
axB.set_yticks([])
axB.set_aspect("equal")
for spine in axB.spines.values():
    spine.set_visible(False)

# ----------------------------------------------------------- (c) Y-Triangle
axC = fig.add_subplot(gs[0, 2])
axC.set_title("(c) Y-Triangle", fontsize=11)
axC.plot([-RMAX, 0, RMAX], [RMAX, 0, RMAX], color="0.45", lw=1.4, zorder=2)
for c in curves:
    x, y = proj(c["pts"], "c")
    axC.plot(x, y, **curve_style(c, "c"))
for m in markers:
    x, y = proj(m["pt"][None, :], "c")
    axC.plot(x, y, ls="none", **marker_style(m, "c"))
axC.set_xlim(-RMAX - 0.3, RMAX + 0.3)
axC.set_ylim(-0.3, RMAX + 0.5)
axC.set_xticks([])
axC.set_yticks([])
axC.set_aspect("equal")
for spine in axC.spines.values():
    spine.set_visible(False)

# ---------------------------------------------------------------- (d) 3D Cone
axD = fig.add_subplot(gs[0, 3], projection="3d")
axD.set_title("(d) 3D Cone", fontsize=11)
axD.plot(RMAX * np.cos(np.linspace(0, 2 * np.pi, 400)),
         RMAX * np.sin(np.linspace(0, 2 * np.pi, 400)),
         np.full(400, RMAX), color="0.45", lw=1.0, zorder=2)
for c in curves:
    p = c["pts"]
    axD.plot(p[:, 0], p[:, 1], p[:, 2], **curve_style(c, "d"))
for m in markers:
    p = m["pt"]
    st = marker_style(m, "d")
    axD.scatter([p[0]], [p[1]], [p[2]], s=(st.pop("ms") ** 2),
                color=st["color"], depthshade=False, zorder=st["zorder"])

# translucent cutting planes (3D view only)
for cut in CUTS:
    Xp = np.linspace(-4.5, 4.5, 2)
    Yp = np.linspace(-3.5, 3.5, 2)
    XXp, YYp = np.meshgrid(Xp, Yp)
    TTp = (cut["c"] + (cut["b"] - cut["a"]) * XXp) / (cut["a"] + cut["b"])
    axD.plot_surface(XXp, YYp, TTp, color=cut["color"], alpha=0.12,
                     linewidth=0, zorder=4)

axD.set_box_aspect((1.4, 1.4, 1))
axD.set_xlim(-RMAX, RMAX)
axD.set_ylim(-RMAX, RMAX)
axD.set_zlim(0, RMAX)
axD.set_axis_off()
axD.view_init(elev=16, azim=-52)

output_dir = Path(__file__).resolve().parent
out_pdf = output_dir / "fig_cutting_plane_4panel.pdf"
out_png = output_dir / "fig_cutting_plane_4panel.png"
fig.savefig(out_pdf, dpi=220, bbox_inches="tight", facecolor="white")
fig.savefig(out_png, dpi=220, bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"saved {out_pdf}")
print(f"saved {out_png}")
print(f"object: {len(curves)} curves, {len(markers)} markers; usetex: {HAS_LATEX}")
