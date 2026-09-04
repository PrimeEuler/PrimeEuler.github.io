#!/usr/bin/env python3
"""Two-panel area-measure comparison for the n=11 shell.

Left: factor-plane triangle x+y<=12 with xy=11.
Right: flat (X,Y) half-disk of radius 6 with secant Y=sqrt(11).

The figure distinguishes ordinary factor-plane area, raw Euclidean circle area,
and the exact transported factor-area measure

    dmu = 2 cos(theta) dX dY.

No claim identifies raw circle area with divisor counts.
"""

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "text.usetex": True,
    "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb}",
})

n = 11
S = n + 1
R = S / 2
sqrt_n = math.sqrt(n)
D = sum(n // k for k in range(1, n + 1))
Tn = n * (n + 1) // 2
An = Tn - D
Hn = sum(1.0 / k for k in range(1, n + 1))
nHn = n * Hn
nlogn = n * math.log(n)

theta_n = math.acos(2 * sqrt_n / (n + 1))
A_half = math.pi * R * R / 2
A_cap = R * R * theta_n - (n - 1) * sqrt_n / 2
A_below = A_half - A_cap
W_L = (2.0 / 3.0) * (n - 1) * sqrt_n

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.6, 5.8))

x_shell = np.linspace(0, S, 600)
y_shell = S - x_shell
ax1.plot(x_shell, y_shell, lw=1.5, label=r"$x+y=12$")
ax1.fill_between(x_shell, 0, y_shell, alpha=0.08)

x_h = np.linspace(1, n, 700)
y_h = n / x_h
ax1.plot(x_h, y_h, lw=2.2, label=r"$xy=11$")
ax1.fill_between(x_h, 0, y_h, alpha=0.16,
                 label=rf"central area $11\log 11={nlogn:.3f}$")

pts = [(x, y) for x in range(1, S) for y in range(1, S - x + 1)]
Dp = [(x, y) for x, y in pts if x * y <= n]
Ap = [(x, y) for x, y in pts if x * y > n]
ax1.scatter([p[0] for p in Dp], [p[1] for p in Dp], s=22,
            label=rf"$D(11)={D}$")
ax1.scatter([p[0] for p in Ap], [p[1] for p in Ap], s=22,
            label=rf"$A_{{11}}={An}$")

ax1.set_xlim(-0.2, S + 0.2)
ax1.set_ylim(-0.2, S + 0.2)
ax1.set_aspect("equal")
ax1.set_xlabel("$x$")
ax1.set_ylabel("$y$")
ax1.set_title("(a) Factor-plane area")
ax1.legend(fontsize=8, loc="upper right")

factor_text = (
    rf"$T_{{11}}={Tn}$" "\n"
    rf"$11\log 11={nlogn:.3f}$" "\n"
    rf"$D(11)={D}$" "\n"
    rf"$11H_{{11}}={nHn:.3f}$"
)
ax1.text(0.45, 2.0, factor_text, fontsize=9,
         bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="0.7", alpha=0.95))

t = np.linspace(0, math.pi, 800)
Xc = R * np.cos(t)
Yc = R * np.sin(t)
ax2.plot(Xc, Yc, lw=1.7, label=r"$X^2+Y^2=36$")
ax2.plot([-R, R], [0, 0], lw=0.8)

Xs = np.linspace(-(n - 1) / 2, (n - 1) / 2, 500)
Ys = np.full_like(Xs, sqrt_n)
ax2.plot(Xs, Ys, lw=2.2, label=r"$Y=\sqrt{11}$")

xc_fill = np.linspace(-R, R, 1000)
ycircle = np.sqrt(np.maximum(0, R * R - xc_fill * xc_fill))
ax2.fill_between(xc_fill, 0, ycircle, alpha=0.07)
mask = np.abs(xc_fill) <= (n - 1) / 2
ax2.fill_between(xc_fill[mask], sqrt_n, ycircle[mask],
                 where=ycircle[mask] >= sqrt_n, alpha=0.18,
                 label=rf"raw cap area $={A_cap:.3f}$")

th = np.linspace(-math.pi / 2, math.pi / 2, 9)
rr = 5.45
for ang in th:
    x0 = rr * math.sin(ang)
    y0 = rr * math.cos(ang)
    w = max(0.0, math.cos(ang))
    ax2.scatter([x0], [y0], s=18 + 55 * w, alpha=0.55)

ax2.set_xlim(-R - 0.4, R + 0.4)
ax2.set_ylim(-0.25, R + 0.45)
ax2.set_aspect("equal")
ax2.set_xlabel("$X$")
ax2.set_ylabel("$Y$")
ax2.set_title("(b) Circle view: raw area vs transported measure")
ax2.legend(fontsize=8, loc="upper right")

circle_text = (
    rf"raw half-disk $={A_half:.3f}$" "\n"
    rf"raw below-secant $={A_below:.3f}$" "\n"
    rf"raw image of $11\log 11$: $W_L={W_L:.3f}$" "\n"
    r"exact factor-area measure:" "\n"
    r"$d\mu=2\cos\theta\,dX\,dY$"
)
ax2.text(-5.55, 0.38, circle_text, fontsize=8.8,
         bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="0.7", alpha=0.95))

fig.suptitle(
    r"$n=11$: the same hyperbola/secant partition under two different area measures",
    fontsize=13,
)
fig.tight_layout(rect=(0, 0, 1, 0.95))

out = Path(__file__).resolve().parent
fig.savefig(out / "fig_area_measure_11_2panel.png", dpi=200,
            bbox_inches="tight", facecolor="white")
fig.savefig(out / "fig_area_measure_11_2panel.pdf",
            bbox_inches="tight", facecolor="white")
print("done:", out / "fig_area_measure_11_2panel.png")
