import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import shutil
import subprocess

# Paper B Figure 1: Lorentz flow orbits on the signed cone (matplotlib only).
#
# BUILD-ONCE ARCHITECTURE (same as Paper A): every curve is a single 3D point
# set on the cone X=(x-y)/2, Y=+-sqrt(xy), T=(x+y)/2, X^2+Y^2=T^2.
# The four panels are four views (projections) of that SAME object:
#   (a) T-Circle   : look down T -> plot (X, Y)
#   (b) X-Triangle : look down Y -> plot (X, T)
#   (c) Y-Triangle : look down X -> plot (Y, T)
#   (d) 3D Cone    : perspective  -> plot (X, Y, T)
#
# Content: the three orbit types of Paper B's classification
#   elliptic    a=b=1 : G=2L,        plane T=2,   circle,  eigenvalues +-i
#   hyperbolic  a=-b=1: G=2*B_Y,     plane X=1,   future branch, eigenvalues +-1
#   parabolic   a=1,b=0: G=L+B_Y,    plane X+T=2, parabola, nilpotent
# plus flow-direction arrows (tangent = G.p) and the metric-dual plane
# normals m=(a-b,0,-(a+b)): timelike / spacelike / null.

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

TMAX = 3.2

ELL_COLOR = "#1f5fa8"
HYP_COLOR = "#b3211a"
PAR_COLOR = "#2e7d32"
NORMAL_COLOR = "#555555"

# --------------------------------------------------------------------------
# Build the object: curves as (N,3) [X, Y, T] point sets; arrows as
# (base, direction) 3D pairs; markers as 3D points.
# --------------------------------------------------------------------------
curves = []   # dict(pts, kind, ...)
arrows = []   # dict(base, vec, kind)


def add_curve(pts, kind, **kw):
    curves.append(dict(pts=np.asarray(pts, dtype=float), kind=kind, **kw))


def add_arrow(base, vec, kind, **kw):
    v = np.asarray(vec, dtype=float)
    v = v / np.linalg.norm(v)
    arrows.append(dict(base=np.asarray(base, dtype=float), vec=v,
                       kind=kind, **kw))


# --- elliptic orbit: a=b=1, c=4 -> plane 2T=4 -> T=2, circle radius 2 ---
th = np.linspace(0, 2 * np.pi, 500)
add_curve(np.column_stack([2 * np.cos(th), 2 * np.sin(th),
                           np.full_like(th, 2.0)]), "ell")

# --- hyperbolic orbit: a=1,b=-1, c=2 -> plane X=1, future branch ---
Yh = np.linspace(-2.6, 2.6, 500)
add_curve(np.column_stack([np.full_like(Yh, 1.0), Yh,
                           np.sqrt(1.0 + Yh ** 2)]), "hyp")

# --- parabolic orbit: a=1,b=0, c=2 -> plane X+T=2, T=1+Y^2/4 ---
Yp = np.linspace(-2.8, 2.8, 500)
add_curve(np.column_stack([1.0 - Yp ** 2 / 4.0, Yp,
                           1.0 + Yp ** 2 / 4.0]), "par")

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

# --- flow arrows: tangent = G.p ---
# elliptic G = 2L:  2L.(X,Y,T) = (-2Y, 2X, 0)
for deg in (30, 150, 270):
    t = np.deg2rad(deg)
    p = np.array([2 * np.cos(t), 2 * np.sin(t), 2.0])
    add_arrow(p, [-p[1], p[0], 0.0], "flow", color=ELL_COLOR)
# hyperbolic G = 2 B_Y:  2B_Y.(X,Y,T) = (0, 2T, 2Y)
for y in (-1.5, 0.0, 1.5):
    p = np.array([1.0, y, np.sqrt(1.0 + y ** 2)])
    add_arrow(p, [0.0, p[2], p[1]], "flow", color=HYP_COLOR)
# parabolic G = L + B_Y:  G.(X,Y,T) = (-Y, X+T, Y); on section X+T=2
for y in (-2.0, 0.0, 2.0):
    p = np.array([1.0 - y ** 2 / 4.0, y, 1.0 + y ** 2 / 4.0])
    add_arrow(p, [-y, 2.0, y], "flow", color=PAR_COLOR)

# --- plane normals m = (a-b, 0, -(a+b)) ---
add_arrow([0.0, 0.0, 2.0], [0.0, 0.0, -1.0], "normal",
          label="timelike normal")                                   # elliptic
add_arrow([1.0, 0.0, 1.0], [1.0, 0.0, 0.0], "normal",
          label="spacelike normal")                                  # hyperbolic
add_arrow([1.0 - 1.5 ** 2 / 4.0, 1.5, 1.0 + 1.5 ** 2 / 4.0],
          [1.0, 0.0, -1.0], "normal", label="null normal")            # parabolic

# --- cone outline helpers (view-dependent, not part of the object) ---
def ring(r, t, n=400):
    a = np.linspace(0, 2 * np.pi, n)
    return np.column_stack([r * np.cos(a), r * np.sin(a), np.full(n, t)])


CONE_RING = ring(TMAX, TMAX)

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
    base = dict(lw=2.6 if view == "d" else 2.4, alpha=0.95, zorder=7)
    if k in ("mesh_row", "mesh_col"):
        color = ROW_COLOR if k == "mesh_row" else COL_COLOR
        if view == "d":
            return dict(color=color, lw=0.9, alpha=0.55, zorder=2)
        return dict(color=color, lw=0.5, alpha=0.33, zorder=1)
    if k == "ell":
        return dict(color=ELL_COLOR, label="elliptic $a=b$: $T=2$ circle, "
                    "$\\widehat G$ spec $\\pm i$", **base)
    if k == "hyp":
        return dict(color=HYP_COLOR, label="hyperbolic $a=-b$: $X=1$ branch, "
                    "$\\widehat G$ spec $\\pm 1$", **base)
    if k == "par":
        return dict(color=PAR_COLOR, label="parabolic $b=0$: $X+T=2$, "
                    "nilpotent", **base)
    raise ValueError(k)


ARROW_LEN = 0.55


def draw_arrow_2d(ax, a, view):
    bx, by = proj(a["base"][None, :], view)
    vx, vy = proj(a["vec"][None, :], view)
    n = np.hypot(vx[0], vy[0])
    if n < 1e-9:
        ax.plot(bx, by, "o", ms=4, color=a.get("color", NORMAL_COLOR),
                zorder=8)
        return
    hx, hy = bx[0] + ARROW_LEN * vx[0] / n, by[0] + ARROW_LEN * vy[0] / n
    if a["kind"] == "normal":
        ax.annotate("", xy=(hx, hy), xytext=(bx[0], by[0]),
                    arrowprops=dict(arrowstyle="->", color=NORMAL_COLOR,
                                    lw=1.2, ls="dashed",
                                    shrinkA=0, shrinkB=0), zorder=6)
    else:
        ax.annotate("", xy=(hx, hy), xytext=(bx[0], by[0]),
                    arrowprops=dict(arrowstyle="-|>", color=a["color"],
                                    lw=1.6, shrinkA=0, shrinkB=0,
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
for a in arrows:
    draw_arrow_2d(axA, a, "a")
axA.plot([], [], color=NORMAL_COLOR, ls="dashed", lw=1.2,
         label="plane normal $m$ (timelike/spacelike/null)")
axA.axhline(0, color="0.84", lw=0.7, zorder=0)
axA.axvline(0, color="0.84", lw=0.7, zorder=0)
axA.set_xlim(-TMAX - 0.2, TMAX + 0.2)
axA.set_ylim(-TMAX - 0.2, TMAX + 0.2)
axA.set_xlabel("$X$")
axA.set_ylabel("$Y$")
axA.set_aspect("equal")
legA = axA.legend(fontsize=7.8, loc="upper right", framealpha=1.0)
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
for a in arrows:
    b, v = a["base"], a["vec"]
    if a["kind"] == "normal":
        axD.quiver([b[0]], [b[1]], [b[2]], [v[0]], [v[1]], [v[2]],
                   length=ARROW_LEN, normalize=True, color=NORMAL_COLOR,
                   linestyle="dashed", linewidth=1.2)
    else:
        axD.quiver([b[0]], [b[1]], [b[2]], [v[0]], [v[1]], [v[2]],
                   length=ARROW_LEN, normalize=True, color=a["color"],
                   linewidth=1.8)

# translucent cutting planes (3D view only)
Xg = np.linspace(-2.6, 2.6, 2)
Yg = np.linspace(-2.6, 2.6, 2)
XX, YY = np.meshgrid(Xg, Yg)
axD.plot_surface(XX, YY, np.full_like(XX, 2.0), color=ELL_COLOR,
                 alpha=0.10, linewidth=0, zorder=4)          # T = 2
Tg = np.linspace(0.2, 3.0, 2)
TT, YY2 = np.meshgrid(Tg, Yg)
axD.plot_surface(np.full_like(TT, 1.0), YY2, TT, color=HYP_COLOR,
                 alpha=0.10, linewidth=0, zorder=4)          # X = 1
XX3, YY3 = np.meshgrid(Xg, Yg)
axD.plot_surface(XX3, YY3, 2.0 - XX3, color=PAR_COLOR,
                 alpha=0.10, linewidth=0, zorder=4)          # X + T = 2

axD.set_box_aspect((1.4, 1.4, 1))
axD.set_xlim(-TMAX, TMAX)
axD.set_ylim(-TMAX, TMAX)
axD.set_zlim(0, TMAX)
axD.set_axis_off()
axD.view_init(elev=16, azim=-52)

output_dir = Path(__file__).resolve().parent
out_pdf = output_dir / "fig_lorentz_orbits_4panel.pdf"
out_png = output_dir / "fig_lorentz_orbits_4panel.png"
fig.savefig(out_pdf, dpi=220, bbox_inches="tight", facecolor="white")
fig.savefig(out_png, dpi=220, bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"saved {out_pdf}")
print(f"saved {out_png}")
print(f"object: {len(curves)} curves, {len(arrows)} arrows; usetex: {HAS_LATEX}")
