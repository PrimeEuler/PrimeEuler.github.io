import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

plt.rcParams.update({
    "text.usetex": True,
    "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}",
})

# ---------------------------------------------------------------
# Divisor-summatory figure for n=11, using Paper A's canonical geometry.
#
# Fundamental Paper A v2.4 relation:
#   X=(x-y)/2,  Y^2=xy,  T=(x+y)/2,
#   X^2+Y^2=T^2.
#
# This particular counting figure intentionally displays the UPPER lift
# Y=+sqrt(xy) only. The reflected lower lift contains the same factor data
# and is omitted here so the discrete counts D(11)=29 and A_11=37 remain
# visually readable. This is a presentation convention, not a restriction
# on Paper A's two-sided cone geometry.
# ---------------------------------------------------------------

n = 11
Kmax = 12
Rmax = Kmax / 2.0
sqrt_n = np.sqrt(n)

D = sum(n // k for k in range(1, n + 1))
Tn = n * (n + 1) // 2
An = Tn - D
Hn = sum(1.0 / k for k in range(1, n + 1))
nHn = n * Hn
nlogn = n * np.log(n)

assert D == 29 and Tn == 66 and An == 37

table_pts = [(xv, yv)
             for xv in range(1, Kmax)
             for yv in range(1, Kmax - xv + 1)]
assert len(table_pts) == Tn

D_pts = [(x, y) for x, y in table_pts if x * y <= n]
A_pts = [(x, y) for x, y in table_pts if x * y > n]
assert len(D_pts) == D and len(A_pts) == An


def upper_cone_coords(points):
    X = np.array([(x-y)/2.0 for x, y in points])
    Y = np.array([np.sqrt(x*y) for x, y in points])
    T = np.array([(x+y)/2.0 for x, y in points])
    return X, Y, T


XD, YD, TD = upper_cone_coords(D_pts)
XA, YA, TA = upper_cone_coords(A_pts)

fig = plt.figure(figsize=(16.5, 6.6))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.05], wspace=0.28)

cD = "#2f6f44"
cA = "#b65a52"
cH = "#7a3db8"
cL = "#2f6fb0"
cB = "#8b1a1a"

theta_c = np.linspace(0, 2*np.pi, 300)

axA = fig.add_subplot(gs[0, 0])
axA.set_title("(a) Upper lift: divisor cells in\n"
              r"the $(X,Y)$ projection, $Y=+\sqrt{xy}$", fontsize=12)

for K in range(2, Kmax + 1):
    r = K / 2.0
    lw = 1.15 if K == Kmax else 0.55
    alpha = 0.65 if K == Kmax else 0.18
    axA.plot(r*np.cos(theta_c), r*np.sin(theta_c), color="0.35", lw=lw, alpha=alpha)

axA.axhline(sqrt_n, color=cB, lw=2.0, ls="--",
            label=r"$xy=11\iff Y=+\sqrt{11}$")
axA.scatter(XD, YD, s=34, color=cD, alpha=0.88,
            edgecolors="white", linewidths=0.35, label=r"$D(11)=29$")
axA.scatter(XA, YA, s=34, color=cA, alpha=0.82,
            edgecolors="white", linewidths=0.35, label=r"$A_{11}=37$")
axA.scatter([-5, 5], [sqrt_n, sqrt_n], s=52, color=cB, zorder=5)
axA.annotate(r"$(1,11)$", (-5, sqrt_n), xytext=(-4.75, sqrt_n+0.45), fontsize=9)
axA.annotate(r"$(11,1)$", (5, sqrt_n), xytext=(3.65, sqrt_n+0.45), fontsize=9)
axA.text(0, 5.65, r"$x+y=12\iff T=6$", ha="center", fontsize=10)
axA.text(0, 0.42, rf"$11\log 11\approx {nlogn:.3f}$", color=cL, ha="center", fontsize=9.5)
axA.text(0, 0.08, rf"$11H_{{11}}\approx {nHn:.3f}$", color=cH, ha="center", fontsize=9.5)
axA.set_xlim(-6.35, 6.35)
axA.set_ylim(-0.2, 6.35)
axA.set_aspect("equal", adjustable="box")
axA.set_xlabel(r"$X=(x-y)/2$")
axA.set_ylabel(r"$Y=+\sqrt{xy}$")
axA.grid(alpha=0.12)
axA.legend(loc="lower right", fontsize=8, frameon=False)

axB = fig.add_subplot(gs[0, 1])
axB.set_title("(b) Side: multiplication table\n"
              r"in the $(X,T)$ plane", fontsize=12)
xx = np.linspace(-6.2, 6.2, 300)
axB.plot(xx, np.abs(xx), color="0.45", lw=1.0, alpha=0.55)
for K in range(2, Kmax + 1):
    r = K / 2.0
    axB.hlines(r, -r, r, color="0.4", lw=0.5, alpha=0.16)
Xh = np.linspace(-5, 5, 500)
Th = np.sqrt(Xh**2 + n)
axB.plot(Xh, Th, color=cB, lw=2.0, ls="--", label=r"$T^2-X^2=11$")
axB.scatter(XD, TD, s=34, color=cD, alpha=0.88,
            edgecolors="white", linewidths=0.35, label=r"$D(11)=29$")
axB.scatter(XA, TA, s=34, color=cA, alpha=0.82,
            edgecolors="white", linewidths=0.35, label=r"$A_{11}=37$")
axB.scatter([-5, 5], [6, 6], s=52, color=cB, zorder=5)
axB.text(0, 6.08, r"$x+y=12$", ha="center", va="bottom", fontsize=10)
axB.text(0, 0.45, r"$T_{11}=66$ cells in $x+y\leq12$", ha="center", fontsize=9.5)
axB.set_xlim(-6.35, 6.35)
axB.set_ylim(0, 6.55)
axB.set_aspect("equal", adjustable="box")
axB.set_xlabel(r"$X=(x-y)/2$")
axB.set_ylabel(r"$T=(x+y)/2$")
axB.grid(alpha=0.12)
axB.legend(loc="lower right", fontsize=8, frameon=False)

axC = fig.add_subplot(gs[0, 2], projection="3d")
axC.set_title("(c) Upper lift: constant-product plane\n"
              r"$Y=+\sqrt{11}$ cuts the cone", fontsize=12)
theta = np.linspace(0, np.pi, 80)
radii = np.linspace(0, Rmax, 45)
RR, TH = np.meshgrid(radii, theta)
XC = RR * np.cos(TH)
YC = RR * np.sin(TH)
TC = RR
axC.plot_surface(XC, YC, TC, color="0.82", alpha=0.13,
                 linewidth=0, antialiased=True)
th = np.linspace(0, np.pi, 300)
axC.plot(Rmax*np.cos(th), Rmax*np.sin(th), np.full_like(th, Rmax),
         color="0.35", lw=1.25, alpha=0.7)
Xp = np.linspace(-5.5, 5.5, 2)
Tp = np.linspace(sqrt_n, 6.25, 2)
XXp, TTp = np.meshgrid(Xp, Tp)
YYp = np.full_like(XXp, sqrt_n)
axC.plot_surface(XXp, YYp, TTp, color=cB, alpha=0.13, linewidth=0)
Xcurve = np.linspace(-5, 5, 400)
Tcurve = np.sqrt(Xcurve**2 + n)
Ycurve = np.full_like(Xcurve, sqrt_n)
axC.plot(Xcurve, Ycurve, Tcurve, color=cB, lw=2.2, ls="--")
axC.scatter(XD, YD, TD, s=22, color=cD, alpha=0.9, depthshade=False)
axC.scatter(XA, YA, TA, s=22, color=cA, alpha=0.82, depthshade=False)
axC.scatter([-5, 5], [sqrt_n, sqrt_n], [6, 6], s=45,
            color=cB, depthshade=False)
axC.set_xlim(-6.2, 6.2)
axC.set_ylim(0, 6.2)
axC.set_zlim(0, 6.4)
axC.set_xlabel(r"$X$", labelpad=6)
axC.set_ylabel(r"$Y$", labelpad=6)
axC.set_zlabel(r"$T$", labelpad=6)
axC.view_init(elev=24, azim=-62)
axC.grid(alpha=0.16)

fig.text(0.5, 0.012,
         r"$T_{11}=66=D(11)+A_{11}=29+37$;  "
         r"$(1,11),(11,1)\leftrightarrow(X,T)=(-5,6),(5,6)$",
         ha="center", fontsize=10)
fig.subplots_adjust(bottom=0.09, top=0.88)
out_dir = Path(__file__).resolve().parent
out_pdf = out_dir / "fig_divisor_summatory_11_3panel.pdf"
out_png = out_dir / "fig_divisor_summatory_11_3panel.png"
fig.savefig(out_pdf, bbox_inches="tight")
fig.savefig(out_png, dpi=220, bbox_inches="tight")
print(f"saved {out_pdf}")
print(f"saved {out_png}")
plt.close(fig)
