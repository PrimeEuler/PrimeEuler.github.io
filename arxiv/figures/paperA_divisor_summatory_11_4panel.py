import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import shutil
import subprocess

# Paper A Figure 2: divisor-summatory geometry for n=11, four views.
# (matplotlib only, no image model.)
#
# BUILD-ONCE ARCHITECTURE (same as Figure 1): every curve and point set is a
# single 3D point set on the cone X=(x-y)/2, Y=+-sqrt(xy), T=(x+y)/2,
# X^2+Y^2=T^2, bounded by x+y<=12. The four panels are four views
# (projections) of that SAME object:
#   (a) T-Circle   : look down T -> plot (X, Y)
#   (b) X-Triangle : look down Y -> plot (X, T)
#   (c) Y-Triangle : look down X -> plot (Y, T)
#   (d) 3D Cone    : perspective  -> plot (X, Y, T)
#
# Content: the 66 cells inside x+y<=12 split into D(11)=29 (xy<=11, green)
# and A_11=37 (xy>11, red) on the upper lift Y=+sqrt(xy); the xy=11 boundary
# as the secant Y=sqrt(11) / hyperbola T^2-X^2=11; even fixed-sum shells.

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

n = 11
KMAX = 12
RMAX = KMAX / 2.0
SQN = np.sqrt(n)

D = sum(n // k for k in range(1, n + 1))
TN = n * (n + 1) // 2
AN = TN - D
HN = sum(1.0 / k for k in range(1, n + 1))
assert D == 29 and TN == 66 and AN == 37

cD = "#2f6f44"   # D(11) points: xy <= 11
cA = "#b65a52"   # A_11 points:  xy > 11
cB = "#8b1a1a"   # xy=11 boundary
ROW_COLOR = "#7fa7cf"
COL_COLOR = "#b08fcf"

table_pts = [(x, y) for x in range(1, KMAX) for y in range(1, KMAX - x + 1)]
D_pts = [(x, y) for x, y in table_pts if x * y <= n]
A_pts = [(x, y) for x, y in table_pts if x * y > n]
assert len(D_pts) == D and len(A_pts) == AN

# --------------------------------------------------------------------------
# Build the object.
# --------------------------------------------------------------------------
curves = []    # dict(pts (N,3), kind, ...)
scatters = []  # dict(pts (N,3), kind)
markers = []   # dict(pt (3,), kind)


def add_curve(pts, kind, **kw):
    curves.append(dict(pts=np.asarray(pts, dtype=float), kind=kind, **kw))


def add_scatter(pts, kind, **kw):
    scatters.append(dict(pts=np.asarray(pts, dtype=float), kind=kind, **kw))


def add_marker(pt, kind, **kw):
    markers.append(dict(pt=np.asarray(pt, dtype=float), kind=kind, **kw))


def ring(r, t, nn=300):
    th = np.linspace(0, 2 * np.pi, nn)
    return np.column_stack([r * np.cos(th), r * np.sin(th), np.full(nn, t)])


# Row/column parabolic mesh (background), lifted to the cone.
for u in range(1, KMAX):
    T = np.linspace(u / 2.0, RMAX, 120)
    Y = np.sqrt(u * (2 * T - u))
    for s in (1.0, -1.0):
        add_curve(np.column_stack([u - T, s * Y, T]), "row")
        add_curve(np.column_stack([T - u, s * Y, T]), "col")

# Even fixed-sum shells.
for K in range(2, KMAX + 1, 2):
    add_curve(ring(K / 2.0, K / 2.0), "shell", K=K)

# The xy=11 boundary: upper secant emphasized, lower reflected lightly.
Xb = np.linspace(-5, 5, 400)
Tb = np.sqrt(Xb ** 2 + n)
add_curve(np.column_stack([Xb, np.full_like(Xb, SQN), Tb]), "secant", branch=+1)
add_curve(np.column_stack([Xb, np.full_like(Xb, -SQN), Tb]), "secant", branch=-1)


def lift(points):
    P = np.array(points, dtype=float)
    x, y = P[:, 0], P[:, 1]
    return np.column_stack([(x - y) / 2.0, np.sqrt(x * y), (x + y) / 2.0])


add_scatter(lift(D_pts), "D")
add_scatter(lift(A_pts), "A")

# Endpoints (1,11) and (11,1): (X,Y,T) = (-5,sqrt(11),6), (5,sqrt(11),6).
add_marker([-5.0, SQN, 6.0], "endpoint", xy="(1,11)")
add_marker([5.0, SQN, 6.0], "endpoint", xy="(11,1)")


# --------------------------------------------------------------------------
# Views.
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
        upper = c["pts"][0, 1] > 0
        if view == "d":
            return dict(color=color, lw=0.45, alpha=0.25, zorder=1)
        if upper:
            return dict(color=color, lw=0.6, alpha=0.45, zorder=1)
        return dict(color=color, lw=0.3, alpha=0.22, zorder=1)
    if k == "shell":
        if view == "d":
            return dict(color="0.45", lw=0.8, zorder=1)
        return dict(color="0.78", lw=0.9, zorder=1)
    if k == "secant":
        if c["branch"] > 0:
            return dict(color=cB, lw=2.8 if view == "d" else 2.5, zorder=6)
        return dict(color=cB, lw=1.1, alpha=0.32, zorder=2)
    raise ValueError(k)


def scatter_style(s, view):
    if s["kind"] == "D":
        return dict(color=cD, s=12 if view == "d" else 19,
                    alpha=0.92 if view == "d" else 0.90)
    return dict(color=cA, s=12 if view == "d" else 19,
                alpha=0.78)


fig = plt.figure(figsize=(20.5, 6.4))
gs = fig.add_gridspec(1, 4, width_ratios=[1, 1, 1, 1.08], wspace=0.24)

# ------------------------------------------------------------ (a) T-Circle
axA = fig.add_subplot(gs[0, 0])
axA.set_title("(a) T-Circle", fontsize=11)
for c in curves:
    x, y = proj(c["pts"], "a")
    st = curve_style(c, "a")
    label = None
    if c["kind"] == "secant" and c["branch"] > 0:
        label = r"$xy=11\;\Longleftrightarrow\;Y=\sqrt{11}$"
    axA.plot(x, y, label=label, **st)
for K in range(2, KMAX + 1, 2):
    Tc = K / 2.0
    axA.annotate(rf"$K={K}$", (Tc * np.cos(0.28), Tc * np.sin(0.28)),
                 fontsize=7, color="0.55", zorder=1)
for s in scatters:
    x, y = proj(s["pts"], "a")
    st = scatter_style(s, "a")
    label = rf"$D(11)={D}$: $xy\leq 11$" if s["kind"] == "D" \
        else rf"$A_{{11}}={AN}$: $xy>11$"
    axA.scatter(x, y, label=label, zorder=5, **st)
for m in markers:
    x, y = proj(m["pt"][None, :], "a")
    axA.plot(x, y, "o", ms=6, mfc="white", mec=cB, mew=1.6, zorder=7, ls="none")
axA.annotate(r"$(1,11)$", (-5, SQN), xytext=(-7, 7), textcoords="offset points",
             ha="right", fontsize=8)
axA.annotate(r"$(11,1)$", (5, SQN), xytext=(7, 7), textcoords="offset points",
             ha="left", fontsize=8)
axA.axhline(0, color="0.85", lw=0.7, zorder=0)
axA.axvline(0, color="0.85", lw=0.7, zorder=0)
axA.set_xlim(-RMAX - 0.4, RMAX + 0.4)
axA.set_ylim(-RMAX - 0.4, RMAX + 0.4)
axA.set_xlabel(r"$X$")
axA.set_ylabel(r"$Y$")
axA.set_aspect("equal")
axA.legend(fontsize=7.5, loc="upper right", framealpha=0.92)
for spine in ["top", "right"]:
    axA.spines[spine].set_visible(False)

# ----------------------------------------------------------- (b) X-Triangle
axB = fig.add_subplot(gs[0, 1])
axB.set_title("(b) X-Triangle", fontsize=11)
axB.plot([-RMAX, 0, RMAX], [RMAX, 0, RMAX], color="0.45", lw=1.4, zorder=1)
for K in range(2, KMAX + 1, 2):
    Tc = K / 2.0
    axB.annotate(rf"$K={K}$", (Tc, Tc), textcoords="offset points",
                 xytext=(5, 1), fontsize=7, color="0.55", va="center")
for c in curves:
    x, y = proj(c["pts"], "b")
    st = curve_style(c, "b")
    label = r"$T^2-X^2=11$" if (c["kind"] == "secant" and c["branch"] > 0) else None
    axB.plot(x, y, label=label, **st)
for s in scatters:
    x, y = proj(s["pts"], "b")
    st = scatter_style(s, "b")
    label = rf"$D(11)={D}$" if s["kind"] == "D" else rf"$A_{{11}}={AN}$"
    axB.scatter(x, y, label=label, zorder=4, **st)
for m in markers:
    x, y = proj(m["pt"][None, :], "b")
    axB.plot(x, y, "o", ms=6, mfc="white", mec=cB, mew=1.6, zorder=6, ls="none")
nlogn = n * np.log(n)
nHn = n * HN
summary = (
    rf"$T_{{11}}={TN}=D(11)+A_{{11}}={D}+{AN}$" "\n"
    rf"$11\log 11\approx {nlogn:.3f}$"
    rf"$\quad<\quad D(11)={D}\quad<\quad$"
    rf"$11H_{{11}}\approx {nHn:.3f}$"
)
axB.text(0, 0.72, summary, ha="center", va="bottom", fontsize=8.5,
         bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="0.75", alpha=0.95),
         zorder=10)
axB.legend(fontsize=7.5, loc="upper left", framealpha=0.92)
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
axC.plot([-RMAX, 0, RMAX], [RMAX, 0, RMAX], color="0.45", lw=1.4, zorder=1)
for c in curves:
    x, y = proj(c["pts"], "c")
    axC.plot(x, y, **curve_style(c, "c"))
for s in scatters:
    x, y = proj(s["pts"], "c")
    axC.scatter(x, y, zorder=4, **scatter_style(s, "c"))
for m in markers:
    x, y = proj(m["pt"][None, :], "c")
    axC.plot(x, y, "o", ms=6, mfc="white", mec=cB, mew=1.6, zorder=6, ls="none")
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
axD.plot(RMAX * np.cos(np.linspace(0, 2 * np.pi, 300)),
         RMAX * np.sin(np.linspace(0, 2 * np.pi, 300)),
         np.full(300, RMAX), color="0.45", lw=1.0, zorder=2)
for c in curves:
    p = c["pts"]
    axD.plot(p[:, 0], p[:, 1], p[:, 2], **curve_style(c, "d"))
for s in scatters:
    p = s["pts"]
    st = scatter_style(s, "d")
    axD.scatter(p[:, 0], p[:, 1], p[:, 2], depthshade=False, zorder=5, **st)
for m in markers:
    p = m["pt"]
    axD.scatter([p[0]], [p[1]], [p[2]], s=25, c="white", edgecolors=cB,
                linewidths=1.4, depthshade=False, zorder=7)

# Translucent divisor plane Y=sqrt(11) (3D view only).
Xp = np.linspace(-5, 5, 2)
Tp = np.linspace(SQN, RMAX, 2)
Xp_, Tp_ = np.meshgrid(Xp, Tp)
axD.plot_surface(Xp_, np.full_like(Xp_, SQN), Tp_, color=cB, alpha=0.13,
                 linewidth=0, zorder=2)
axD.text(0.2, SQN + 0.12, SQN + 0.35, r"$Y=\sqrt{11}$", color=cB, fontsize=9)
axD.text(3.0, SQN + 0.18, np.sqrt(20) + 0.25, r"$T^2-X^2=11$", color=cB,
         fontsize=9)

axD.set_box_aspect((1.4, 1.4, 1))
axD.set_xlim(-RMAX, RMAX)
axD.set_ylim(-RMAX, RMAX)
axD.set_zlim(0, RMAX)
axD.set_axis_off()
axD.view_init(elev=16, azim=-52)

output_dir = Path(__file__).resolve().parent
out_png = output_dir / "fig_divisor_summatory_11_4panel.png"
out_pdf = output_dir / "fig_divisor_summatory_11_4panel.pdf"
fig.savefig(out_png, dpi=220, bbox_inches="tight", facecolor="white")
fig.savefig(out_pdf, bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"saved {out_png}")
print(f"saved {out_pdf}")
print("T_11 =", TN, "D(11) =", D, "A_11 =", AN)
print(f"object: {len(curves)} curves, {len(scatters)} scatters, "
      f"{len(markers)} markers; usetex: {HAS_LATEX}")
