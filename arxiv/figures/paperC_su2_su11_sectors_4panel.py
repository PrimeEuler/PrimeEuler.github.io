import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import shutil
import subprocess

# Paper C Figure 1: the two sector foliations of the two-mode realization
# (matplotlib only).
#
# BUILD-ONCE ARCHITECTURE (same as Papers A/B): every curve is a single 3D
# point set on the cone X=(x-y)/2, Y=+-sqrt(xy), T=(x+y)/2, X^2+Y^2=T^2.
# The four panels are four views (projections) of that SAME object:
#   (a) T-Circle   : look down T -> plot (X, Y)
#   (b) X-Triangle : look down Y -> plot (X, T)
#   (c) Y-Triangle : look down X -> plot (Y, T)
#   (d) 3D Cone    : perspective  -> plot (X, Y, T)
#
# Content: Paper C's dictionary x=n1+1, y=n2 gives X=(n1-n2+1)/2,
# T=(n1+n2+1)/2, Y=+-sqrt((n1+1)*n2).
#   su(2)  : fixed N <-> fixed T=j+1/2 rings; 2j+1 Fock points at
#            X=m+1/2 (J_z levels); J+- ladder arrows along the j=2 ring.
#   su(1,1): fixed D=n1-n2 <-> fixed X=(d+1)/2 branches; Fock points at
#            T=k+(d+1)/2, Y=sqrt(k*(k+d+1)); K+- ladder arrows up the
#            d=0 branch (N -> N+-2 at fixed D).

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

TMAX = 3.8

SU2_COLOR = "#1f5fa8"
SU11_COLOR = "#b3211a"
ROW_COLOR = "#7fa7cf"
COL_COLOR = "#b08fcf"

curves = []    # dict(pts, kind, ...)
markers = []   # dict(pt, kind)
arrows = []    # dict(base, head, kind)


def add_curve(pts, kind, **kw):
    curves.append(dict(pts=np.asarray(pts, dtype=float), kind=kind, **kw))


def add_marker(pt, kind, **kw):
    markers.append(dict(pt=np.asarray(pt, dtype=float), kind=kind, **kw))


def add_arrow(base, head, kind, **kw):
    arrows.append(dict(base=np.asarray(base, dtype=float),
                       head=np.asarray(head, dtype=float),
                       kind=kind, **kw))


def ring(r, t, n=400):
    a = np.linspace(0, 2 * np.pi, n)
    return np.column_stack([r * np.cos(a), r * np.sin(a), np.full(n, t)])


# --- canonical row/column parabolic mesh (standing rule), clipped to TMAX ---
for u in range(1, 8):
    Tm = np.linspace(u / 2.0, TMAX, 160)
    Y = np.sqrt(u * (2 * Tm - u))
    for s in (1.0, -1.0):
        add_curve(np.column_stack([u - Tm, s * Y, Tm]), "mesh_row")
        add_curve(np.column_stack([Tm - u, s * Y, Tm]), "mesh_col")

# --- su(2) spin-sector rings: fixed T = j + 1/2 ---
for j, emph in ((1, False), (2, True), (3, False)):
    T = j + 0.5
    add_curve(ring(T, T), "su2ring", j=j, emph=emph)
    for m in range(-j, j + 1):
        n1, n2 = j + m, j - m
        X = m + 0.5
        Yv = np.sqrt((n1 + 1) * n2)
        for s in (1.0, -1.0):
            if Yv == 0.0 and s < 0:
                continue
            add_marker([X, s * Yv, T], "fock2", j=j, m=m)

# --- J+- ladder arrows along the upper semicircle of the j=2 ring ---
j = 2
T2 = j + 0.5
up2 = []
for m in range(-j, j + 1):
    n1, n2 = j + m, j - m
    up2.append(np.array([m + 0.5, np.sqrt((n1 + 1) * n2), T2]))
for k in range(len(up2) - 1):
    add_arrow(up2[k], up2[k + 1], "jladder")

# --- su(1,1) sectors: fixed X = (d+1)/2 branches ---
for d, emph, kmax in ((0, True, 3), (2, False, 2)):
    Xc = (d + 1) / 2.0
    Tv = np.linspace(Xc, TMAX, 300)
    Yv = np.sqrt(Tv ** 2 - Xc ** 2)
    add_curve(np.column_stack([np.full_like(Tv, Xc), Yv, Tv]),
              "su11branch", d=d, emph=emph, upper=True)
    add_curve(np.column_stack([np.full_like(Tv, Xc), -Yv, Tv]),
              "su11branch", d=d, emph=emph, upper=False)
    for k in range(kmax + 1):
        Tk = k + (d + 1) / 2.0
        Yk = np.sqrt(k * (k + d + 1))
        for s in (1.0, -1.0):
            if Yk == 0.0 and s < 0:
                continue
            add_marker([Xc, s * Yk, Tk], "fock11", d=d, k=k)

# --- K+- ladder arrows up the d=0 branch (upper side) ---
kup = [np.array([0.5, np.sqrt(k * (k + 1)), k + 0.5]) for k in range(4)]
for k in range(3):
    add_arrow(kup[k], kup[k + 1], "kladder")

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
    if k == "su2ring":
        if c["emph"]:
            return dict(color=SU2_COLOR, lw=2.6, alpha=0.95, zorder=4,
                        label="su(2) sector: fixed $T=j+1/2$ ring")
        return dict(color=SU2_COLOR, lw=1.4, alpha=0.7, zorder=3)
    if k == "su11branch":
        if c["emph"] and c.get("upper"):
            return dict(color=SU11_COLOR, lw=2.4, alpha=0.95, zorder=4,
                        label="su(1,1) sector: fixed $X=(d+1)/2$ branch")
        return dict(color=SU11_COLOR, lw=1.4, alpha=0.7, zorder=3)
    raise ValueError(k)


def marker_style(m, view):
    k = m["kind"]
    if k == "fock2":
        return dict(marker="o", ms=5.5, color="#0d3a6b", zorder=7)
    if k == "fock11":
        return dict(marker="o", ms=5.5, color="#6b0d0d", zorder=7)
    raise ValueError(k)


def draw_arrow_2d(ax, a, view):
    bx, by = proj(a["base"][None, :], view)
    hx, hy = proj(a["head"][None, :], view)
    color = "#0d3a6b" if a["kind"] == "jladder" else "#6b0d0d"
    ax.annotate("", xy=(hx[0], hy[0]), xytext=(bx[0], by[0]),
                arrowprops=dict(arrowstyle="-|>", color=color,
                                lw=1.7, shrinkA=3, shrinkB=5,
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
    axA.plot(x, y, ls="none", **marker_style(m, "a"))
for a in arrows:
    draw_arrow_2d(axA, a, "a")
# sqrt altitude labels on the emphasized j=2 ring (upper semicircle)
for m, txt in ((-2, "$2$"), (-1, "$\\sqrt{6}$"),
               (0, "$\\sqrt{6}$"), (1, "$2$")):
    n1, n2 = 2 + m, 2 - m
    axA.text(m + 0.5, np.sqrt((n1 + 1) * n2) + 0.16, txt, fontsize=7,
             ha="center", va="bottom", color="0.25", zorder=9)
axA.plot([], [], "o", ms=5.5, color="#0d3a6b",
         label="Fock state $|n_1,n_2\\rangle$")
axA.plot([], [], "-", color="#0d3a6b", lw=1.7,
         label="$J_\\pm$ ladder ($\\Delta m=\\pm1$, fixed $j$)")
axA.plot([], [], "-", color="#6b0d0d", lw=1.7,
         label="$K_\\pm$ ladder ($\\Delta N=\\pm2$, fixed $d$)")
axA.axhline(0, color="0.84", lw=0.7, zorder=0)
axA.axvline(0, color="0.84", lw=0.7, zorder=0)
axA.set_xlim(-TMAX - 0.2, TMAX + 0.2)
axA.set_ylim(-TMAX - 0.2, TMAX + 0.2)
axA.set_xlabel("$X$")
axA.set_ylabel("$Y$")
axA.set_aspect("equal")
legA = axA.legend(fontsize=7.4, loc="lower left", framealpha=1.0)
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
    axD.scatter([p[0]], [p[1]], [p[2]], s=ms ** 2, depthshade=False, **st)
for a in arrows:
    b, h = a["base"], a["head"]
    d = h - b
    color = "#0d3a6b" if a["kind"] == "jladder" else "#6b0d0d"
    axD.quiver([b[0]], [b[1]], [b[2]], [d[0]], [d[1]], [d[2]],
               length=np.linalg.norm(d), normalize=False,
               color=color, linewidth=1.8, arrow_length_ratio=0.22)

axD.set_box_aspect((1.4, 1.4, 1))
axD.set_xlim(-TMAX, TMAX)
axD.set_ylim(-TMAX, TMAX)
axD.set_zlim(0, TMAX)
axD.set_axis_off()
axD.view_init(elev=16, azim=-52)

output_dir = Path(__file__).resolve().parent
out_pdf = output_dir / "fig_su2_su11_sectors_4panel.pdf"
out_png = output_dir / "fig_su2_su11_sectors_4panel.png"
fig.savefig(out_pdf, dpi=220, bbox_inches="tight", facecolor="white")
fig.savefig(out_png, dpi=220, bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"saved {out_pdf}")
print(f"saved {out_png}")
print(f"object: {len(curves)} curves, {len(markers)} markers, "
      f"{len(arrows)} arrows; usetex: {HAS_LATEX}")
