"""Roadmap map figure: one 3D cone carrying labeled readings (legend, not tags).

Schematic only. Canonical row/column parabola mesh with hidden-line
removal so curves wrap the silhouette edge (front solid, back ghost);
the 2 unit parabolas (u=1 row+column) slightly forward; cone rim drawn
first so every parabola lands visibly on it; two generator rays;
labeled features drawn solid on top (house style):
  - divisor-summatory base (Paper A)
  - totient hyperbola arc r=11 (Totient note)
  - fixed-T SU(2) ring (Paper C)
  - fixed-X SU(1,1) branch (Paper C)
  - screw helix toward the analytic summit (ledger / Sieve note)
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

TMAX = 6.0
ELEV, AZIM = 24, -62

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")

# no pane grids / backdrops: the gray 3D box is pure noise here
ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
    axis.pane.set_edgecolor("0.85")

# --- hidden-line note ---
# Deliberately NO occlusion: the canonical figures draw the mesh as a
# plain low-alpha projection, and the see-through ghost is what makes
# the parabolas read as wrapping the cone. Occlusion splitting was
# tried and caused the gapping at the silhouette. (Jeremy, 2026-10-05)


# --- cone rim: the edge the parabolas land on (plain circle, canonical style)
thr = np.linspace(0, 2 * np.pi, 160)
ax.plot(TMAX * np.cos(thr), TMAX * np.sin(thr), np.full_like(thr, TMAX),
        color="0.45", lw=1.0)

# --- the two generator rays in the Y=0 plane: the cone's skeleton ---
ax.plot([0, TMAX], [0, 0], [0.02, TMAX], color="0.45", lw=1.0)
ax.plot([0, -TMAX], [0, 0], [0.02, TMAX], color="0.45", lw=1.0)

# --- canonical row/column parabola mesh (plain projection, canonical alpha)
for u in [1.0, 2.0, 3.0, 4.0, 5.0]:
    tt = np.linspace(u / 2 + 0.03, TMAX, 80)
    yy = np.sqrt(u * (2 * tt - u))
    ax.plot(u - tt, yy, tt, color="#7fa7cf", lw=0.6, alpha=0.25)
    ax.plot(u - tt, -yy, tt, color="#7fa7cf", lw=0.6, alpha=0.25)
    ax.plot(tt - u, yy, tt, color="#b08fcf", lw=0.6, alpha=0.25)
    ax.plot(tt - u, -yy, tt, color="#b08fcf", lw=0.6, alpha=0.25)

# --- the 2 unit parabolas (u=1 row + u=1 column), slightly forward ---
# they cross at the r=1 unit-shell points (0, +/-1, 1)
tu = np.linspace(0.53, TMAX, 100)
yu = np.sqrt(2 * tu - 1.0)
ax.plot(1 - tu, yu, tu, color="#7fa7cf", lw=1.1, alpha=0.85)
ax.plot(1 - tu, -yu, tu, color="#7fa7cf", lw=1.1, alpha=0.85)
ax.plot(tu - 1, yu, tu, color="#b08fcf", lw=1.1, alpha=0.85)
ax.plot(tu - 1, -yu, tu, color="#b08fcf", lw=1.1, alpha=0.85)

# --- labeled features: solid on top (house style) ---
# divisor-summatory base ring (Paper A)
thd = np.linspace(0, 2 * np.pi, 72)
ax.plot(0.9 * np.cos(thd), 0.9 * np.sin(thd), [0.9] * len(thd),
        color="#8a6d3b", lw=2.0)

# totient hyperbola arc, r=11: X=5/2, T^2-Y^2=(5/2)^2 (Totient note)
c = 2.5
tt = np.linspace(c, 3.0, 40)
yy = np.sqrt(tt ** 2 - c ** 2)
ax.plot([c] * len(tt), yy, tt, color="#d99a06", lw=2.6)
ax.plot([c] * len(tt), -yy, tt, color="#d99a06", lw=2.6)
ax.scatter([c], [0], [c], color="white", edgecolors="black",
           s=60, depthshade=False)

# SU(2) ring at T=4 (Paper C)
thr2 = np.linspace(0, 2 * np.pi, 140)
ax.plot(4 * np.cos(thr2), 4 * np.sin(thr2), [4.0] * len(thr2),
        color="#2a7fbf", lw=2.4)

# SU(1,1) branch at X=1 (Paper C)
ttb = np.linspace(1.0, 4.2, 60)
yyb = np.sqrt(ttb ** 2 - 1.0)
ax.plot([1.0] * len(ttb), yyb, ttb, color="#c0392b", lw=2.2)
ax.plot([1.0] * len(ttb), -yyb, ttb, color="#c0392b", lw=2.2)

# screw helix on the cone (Sieve / ledger)
tth = np.linspace(1.6, TMAX, 200)
ax.plot(tth * np.cos(1.4 * tth), tth * np.sin(1.4 * tth), tth,
        color="#6a3fb5", lw=1.6, alpha=0.9)

# --- legend instead of floating tags ---
legend_elements = [
    Line2D([0], [0], color="#8a6d3b", lw=2.0,
           label="divisor summatory $D(n)$ \u2014 Paper A"),
    Line2D([0], [0], color="#d99a06", lw=2.6,
           label="totient hyperbolas $V_4\\leftrightarrow QR(12)$ \u2014 Totient note"),
    Line2D([0], [0], color="#2a7fbf", lw=2.4,
           label="$\\mathrm{SU}(2)$ ring \u2014 Paper C"),
    Line2D([0], [0], color="#c0392b", lw=2.2,
           label="$\\mathrm{SU}(1,1)$ branch \u2014 Paper C"),
    Line2D([0], [0], color="#6a3fb5", lw=1.6,
           label="screw $\\to$ zeta zeros \u2014 Sieve / ledger"),
    Line2D([0], [0], color="#7fa7cf", lw=1.2,
           label="parabola mesh (background)"),
]
ax.legend(handles=legend_elements, loc="upper left", fontsize=8,
          framealpha=0.92, edgecolor="0.8")

ax.set_xlabel("X", fontsize=9)
ax.set_ylabel("Y", fontsize=9)
ax.set_zlabel("T", fontsize=9)
ax.view_init(elev=ELEV, azim=AZIM)
ax.set_box_aspect((1, 1, 0.9))
plt.tight_layout()
plt.savefig("/home/hatch/workspace/d12/arxiv-prep/roadmap/fig_cone_roadmap.pdf",
            bbox_inches="tight")
plt.savefig("/home/hatch/workspace/d12/arxiv-prep/roadmap/fig_cone_roadmap.png",
            dpi=150, bbox_inches="tight")
print("wrote fig_cone_roadmap.pdf/.png")
