import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import shutil
import subprocess

# Paper B Figure 2: eigen-coordinate power maps (matplotlib only).
#
# BUILD-ONCE ARCHITECTURE (same as Paper A): every curve is a single 3D point
# set on the cone X=(x-y)/2, Y=+-sqrt(xy), T=(x+y)/2, X^2+Y^2=T^2.
# The four panels are four views (projections) of that SAME object:
#   (a) T-Circle   : look down T -> plot (X, Y)
#   (b) X-Triangle : look down Y -> plot (X, T)
#   (c) Y-Triangle : look down X -> plot (Y, T)
#   (d) 3D Cone    : perspective  -> plot (X, Y, T)
#
# Content: the three power-map constructions of Paper B sections 6-7
#   elliptic   : |z|=1 circle, markers z^k (angle multiplication z -> z^n)
#   hyperbolic : xi_+ xi_-=1 branch, markers k*s0 (rapidity dilation s -> ns)
#   parabolic  : row x=2 -> row x=4 under (x,y) -> (x^2,y^2) (no diagonal
#                eigen-coordinate exists here)

# usetex needs a working LaTeX install *including* the type1cm/type1ec
# packages matplotlib's texmanager requires; pdflatex alone is not enough
# (the VM's TeX Live lacks them), so probe with kpsewhich before enabling.
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

TMAX = 3.4

ELL_COLOR = "#1f5fa8"
HYP_COLOR = "#b3211a"
PAR_COLOR = "#2e7d32"

curves = []    # dict(pts, kind, ...)
markers = []   # dict(pt, kind, label)
arrows = []    # dict(base, head, kind)


def add_curve(pts, kind, **kw):
    curves.append(dict(pts=np.asarray(pts, dtype=float), kind=kind, **kw))


def add_marker(pt, kind, label=None, **kw):
    markers.append(dict(pt=np.asarray(pt, dtype=float), kind=kind,
                        label=label, **kw))


def add_arrow(base, head, kind, **kw):
    arrows.append(dict(base=np.asarray(base, dtype=float),
                       head=np.asarray(head, dtype=float),
                       kind=kind, **kw))


# --- canonical row/column parabolic mesh (same construction as Paper A
#     Figure 1, clipped to this figure's TMAX frame): rows x=u lift to
#     X=u-T, Y=+-sqrt(u(2T-u)); columns y=u lift to X=T-u, same Y ---
ROW_COLOR = "#7fa7cf"
COL_COLOR = "#b08fcf"
for u in range(1, 7):
    Tm = np.linspace(u / 2.0, TMAX, 160)
    Y = np.sqrt(u * (2 * Tm - u))
    for s in (1.0, -1.0):
        add_curve(np.column_stack([u - Tm, s * Y, Tm]), "mesh_row")
        add_curve(np.column_stack([Tm - u, s * Y, Tm]), "mesh_col")

# --- elliptic: base circle T=2, radius 2 (light) ---
th = np.linspace(0, 2 * np.pi, 500)
add_curve(np.column_stack([2 * np.cos(th), 2 * np.sin(th),
                           np.full_like(th, 2.0)]), "ellbase")
# eigen-coordinate z = (X + iY)/2, |z| = 1; seed z = e^{i pi/9}
theta0 = np.pi / 9.0
zlabels = ["$z$", "$z^2$", "$z^3$", "$z^4$"]
zpts = []
for k in range(1, 5):
    t = k * theta0
    p = np.array([2 * np.cos(t), 2 * np.sin(t), 2.0])
    zpts.append(p)
    add_marker(p, "ell", label=zlabels[k - 1])
for k in range(3):
    add_arrow(zpts[k], zpts[k + 1], "pmap", color=ELL_COLOR)

# --- hyperbolic: base branch X=1 (light) ---
Yh = np.linspace(-2.9, 2.9, 500)
add_curve(np.column_stack([np.full_like(Yh, 1.0), Yh,
                           np.sqrt(1.0 + Yh ** 2)]), "hypbase")
# xi_+ = T + Y = e^s, xi_- = T - Y = e^{-s}; seed s0 = 0.35
s0 = 0.35
slabels = ["$s_0$", "$2s_0$", "$3s_0$", "$4s_0$"]
spts = []
for k in range(1, 5):
    s = k * s0
    p = np.array([1.0, np.sinh(s), np.cosh(s)])
    spts.append(p)
    add_marker(p, "hyp", label=slabels[k - 1])
for k in range(3):
    add_arrow(spts[k], spts[k + 1], "pmap", color=HYP_COLOR)

# --- parabolic: row x=2 (solid) and row x=4 = its square image (dashed) ---
# row x=u: X=(u-y)/2, Y=sqrt(u*y), T=(u+y)/2, y>0
# y-ranges chosen so the curves stay inside the (X,Y,T) frame (T<=TMAX)
for u, kind, ymax in ((2.0, "par2", 4.5), (4.0, "par4", 2.6)):
    y = np.linspace(0.02, ymax, 400)
    add_curve(np.column_stack([(u - y) / 2.0, np.sqrt(u * y),
                               (u + y) / 2.0]), kind)
# coordinatewise square (2,y) -> (4,y^2); samples keep images inside frame
for y in (0.5, 1.0, 1.5):
    p = np.array([(2.0 - y) / 2.0, np.sqrt(2.0 * y), (2.0 + y) / 2.0])
    q = np.array([(4.0 - y ** 2) / 2.0, 2.0 * y, (4.0 + y ** 2) / 2.0])
    add_marker(p, "parsrc")
    add_marker(q, "pardst")
    add_arrow(p, q, "pmap", color=PAR_COLOR)


def ring(r, t, n=400):
    a = np.linspace(0, 2 * np.pi, n)
    return np.column_stack([r * np.cos(a), r * np.sin(a), np.full(n, t)])


CONE_RING = ring(TMAX, TMAX)

# --------------------------------------------------------------------------
# Views
# --------------------------------------------------------------------------
def proj(pts, view):
    if view == "a":
        return pts[:, 0], pts[:, 1]
    if view == "b":
        return pts[:, 0], pts[:, 2]
    return pts[:, 1], pts[:, 2]


def curve_style(c, view):
    k = c["kind"]
    if k in ("mesh_row", "mesh_col"):
        color = ROW_COLOR if k == "mesh_row" else COL_COLOR
        if view == "d":
            return dict(color=color, lw=0.9, alpha=0.55, zorder=2)
        return dict(color=color, lw=0.5, alpha=0.33, zorder=1)
    if k == "ellbase":
        return dict(color=ELL_COLOR, lw=1.1, alpha=0.45, zorder=2,
                    label="elliptic orbit $|z|=1$")
    if k == "hypbase":
        return dict(color=HYP_COLOR, lw=1.1, alpha=0.45, zorder=2,
                    label="hyperbolic orbit $\\xi_+\\xi_-=1$")
    if k == "par2":
        return dict(color=PAR_COLOR, lw=1.6, alpha=0.9, zorder=3,
                    label="row $x=2$")
    if k == "par4":
        return dict(color=PAR_COLOR, lw=1.6, alpha=0.9, zorder=3, ls="--",
                    label="row $x=4$; $(x,y)\\mapsto(x^2,y^2)$")
    raise ValueError(k)


def marker_style(m, view):
    k = m["kind"]
    if k == "ell":
        return dict(marker="o", ms=6.5, color=ELL_COLOR, zorder=8)
    if k == "hyp":
        return dict(marker="s", ms=6.0, color=HYP_COLOR, zorder=8)
    if k == "parsrc":
        return dict(marker="o", ms=5.5, color=PAR_COLOR, zorder=8)
    if k == "pardst":
        return dict(marker="D", ms=5.5, color=PAR_COLOR, zorder=8,
                    markerfacecolor="white", markeredgewidth=1.4)
    raise ValueError(k)


def draw_arrow_2d(ax, a, view):
    bx, by = proj(a["base"][None, :], view)
    hx, hy = proj(a["head"][None, :], view)
    ax.annotate("", xy=(hx[0], hy[0]), xytext=(bx[0], by[0]),
                arrowprops=dict(arrowstyle="-|>", color=a["color"],
                                lw=1.6, shrinkA=2, shrinkB=4,
                                mutation_scale=14), zorder=8)


fig = plt.figure(figsize=(20.5, 6.4))
gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1, 1.08], wspace=0.24)

# ------------------------------------------------------------ (a) T-Circle
axA = fig.add_subplot(gs[0, 0])
axA.set_title("(a) T-Circle", fontsize=11)
for c in curves:
    x, y = proj(c["pts"], "a")
    st = curve_style(c, "a")
    lbl = st.pop("label", None)
    if lbl is None:
        axA.plot(x, y, **st)
    else:
        axA.plot(x, y, label=lbl, **st)
for m in markers:
    x, y = proj(m["pt"][None, :], "a")
    st = marker_style(m, "a")
    axA.plot(x, y, ls="none", **st)
    if m["label"] and m["kind"] in ("ell", "hyp"):
        if m["kind"] == "ell":
            dx, dy = m["pt"][0] / 2.0 * 0.24, m["pt"][1] / 2.0 * 0.24
        else:
            dx, dy = 0.15, 0.03
        axA.text(x[0] + dx, y[0] + dy, m["label"], fontsize=8,
                 color="black", zorder=9)
for a in arrows:
    draw_arrow_2d(axA, a, "a")
axA.plot([], [], "o", ms=6.5, color=ELL_COLOR,
         label="$z^k$, $k=1..4$ ($z=e^{i\\pi/9}$)")
axA.plot([], [], "s", ms=6.0, color=HYP_COLOR,
         label="rapidity $ks_0$, $k=1..4$ ($s_0=0.35$)")
axA.plot([], [], "o", ms=5.5, color=PAR_COLOR, label="$(2,y)$ source")
axA.plot([], [], "D", ms=5.5, color=PAR_COLOR, markerfacecolor="white",
         markeredgewidth=1.4, label="$(4,y^2)$ image")
axA.axhline(0, color="0.84", lw=0.7, zorder=0)
axA.axvline(0, color="0.84", lw=0.7, zorder=0)
axA.set_xlim(-TMAX - 0.2, TMAX + 0.2)
axA.set_ylim(-TMAX - 0.2, TMAX + 0.2)
axA.set_xlabel("$X$")
axA.set_ylabel("$Y$")
axA.set_aspect("equal")
legA = axA.legend(fontsize=7.8, loc="lower left", framealpha=1.0)
legA.set_zorder(20)
for spine in ["top", "right"]:
    axA.spines[spine].set_visible(False)

# ----------------------------------------------------------- (b) X-Triangle
axB = fig.add_subplot(gs[0, 1])
axB.set_title("(b) X-Triangle", fontsize=11)
axB.plot([-TMAX, 0, TMAX], [TMAX, 0, TMAX], color="0.45", lw=1.4, zorder=2)
for c in curves:
    x, y = proj(c["pts"], "b")
    axB.plot(x, y, **{k: v for k, v in curve_style(c, "b").items()
                      if k != "label"})
for m in markers:
    x, y = proj(m["pt"][None, :], "b")
    axB.plot(x, y, ls="none", **marker_style(m, "b"))
for a in arrows:
    draw_arrow_2d(axB, a, "b")
axB.set_xlim(-TMAX - 0.2, TMAX + 0.2)
axB.set_ylim(-0.2, TMAX + 0.3)
axB.set_xticks([])
axB.set_yticks([])
axB.set_aspect("equal")
for spine in axB.spines.values():
    spine.set_visible(False)

# ----------------------------------------------------------- (c) Y-Triangle
axC = fig.add_subplot(gs[0, 2])
axC.set_title("(c) Y-Triangle", fontsize=11)
axC.plot([-TMAX, 0, TMAX], [TMAX, 0, TMAX], color="0.45", lw=1.4, zorder=2)
for c in curves:
    x, y = proj(c["pts"], "c")
    axC.plot(x, y, **{k: v for k, v in curve_style(c, "c").items()
                      if k != "label"})
for m in markers:
    x, y = proj(m["pt"][None, :], "c")
    axC.plot(x, y, ls="none", **marker_style(m, "c"))
for a in arrows:
    draw_arrow_2d(axC, a, "c")
axC.set_xlim(-TMAX - 0.2, TMAX + 0.2)
axC.set_ylim(-0.2, TMAX + 0.3)
axC.set_xticks([])
axC.set_yticks([])
axC.set_aspect("equal")
for spine in axC.spines.values():
    spine.set_visible(False)

# ---------------------------------------------------------------- (d) 3D Cone
axD = fig.add_subplot(gs[0, 3], projection="3d")
axD.set_title("(d) 3D Cone", fontsize=11)
axD.plot(CONE_RING[:, 0], CONE_RING[:, 1], CONE_RING[:, 2],
         color="0.45", lw=1.0, zorder=2)
for c in curves:
    p = c["pts"]
    st = {k: v for k, v in curve_style(c, "d").items() if k != "label"}
    axD.plot(p[:, 0], p[:, 1], p[:, 2], **st)
for m in markers:
    p, st = m["pt"], marker_style(m, "d")
    ms = st.pop("ms")
    mfc = st.pop("markerfacecolor", None)
    mew = st.pop("markeredgewidth", None)
    kw = dict(st)
    if mfc is not None:
        kw["facecolors"] = mfc
        kw["edgecolors"] = kw.pop("color")
    if mew is not None:
        kw["linewidths"] = mew
    axD.scatter([p[0]], [p[1]], [p[2]], s=ms ** 2, depthshade=False, **kw)
for a in arrows:
    b, h = a["base"], a["head"]
    d = h - b
    axD.quiver([b[0]], [b[1]], [b[2]], [d[0]], [d[1]], [d[2]],
               length=np.linalg.norm(d), normalize=False,
               color=a["color"], linewidth=1.8, arrow_length_ratio=0.18)

axD.set_box_aspect((1.4, 1.4, 1))
axD.set_xlim(-TMAX, TMAX)
axD.set_ylim(-TMAX, TMAX)
axD.set_zlim(0, TMAX)
axD.set_axis_off()
axD.view_init(elev=16, azim=-52)

output_dir = Path(__file__).resolve().parent
out_pdf = output_dir / "fig_power_maps_4panel.pdf"
out_png = output_dir / "fig_power_maps_4panel.png"
fig.savefig(out_pdf, dpi=220, bbox_inches="tight", facecolor="white")
fig.savefig(out_png, dpi=220, bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"saved {out_pdf}")
print(f"saved {out_png}")
print(f"object: {len(curves)} curves, {len(markers)} markers, "
      f"{len(arrows)} arrows; usetex: {HAS_LATEX}")
