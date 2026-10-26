"""EM (h=1, q=1/2) vs gravitational-dyon (h=1/2, q=1/4) grids in the
cone's parabolic coordinates (X = offset, Y = GM). Canonical mesh:
rows #7fa7cf, columns #b08fcf, low alpha, drawn behind the nodes.
Crossing of raw members (x,y): (X, Y) = ((x-y)/2, sqrt(xy)).
Shells xy = const are horizontal lines Y = sqrt(xy); r = log(xy),
so r = 0 is the line Y = 1 in BOTH sectors - what differs is which
lattice nodes exist and what grid shell index n = ab = xy/h^2 the
dictionary assigns to that line: n = 1 (EM) vs n = 4 (gravity)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROW, COL = "#7fa7cf", "#b08fcf"
TMAX, YMAX, XMAX = 6.0, 3.55, 5.0

def mesh(ax, us):
    t = np.linspace(0, TMAX, 400)
    for u in us:
        tt = t[t >= u]
        Y = np.sqrt(u * (2 * tt - u))
        ax.plot(u - tt, Y, color=ROW, lw=0.7, alpha=0.45)   # row x=u:  X = u - T
        ax.plot(tt - u, Y, color=COL, lw=0.7, alpha=0.45)   # col y=u:  X = T - u

def panel(ax, h, title, sub):
    us = np.arange(h, TMAX + 1e-9, h)
    mesh(ax, us)
    # nodes: grid members a,b>=1, raw members x=ha, y=hb
    amax = int(TMAX / h)
    pts = []
    for a in range(1, amax + 1):
        for b in range(1, amax + 1):
            x, y = h * a, h * b
            if (x + y) / 2 > TMAX or np.sqrt(x * y) > YMAX:
                continue
            pts.append((a, b, (x - y) / 2, np.sqrt(x * y)))
    X = [p[2] for p in pts]; Y = [p[3] for p in pts]
    ax.scatter(X, Y, s=9, color="#333333", zorder=5, linewidths=0)
    # r = 0 shell: raw product xy = 1 -> Y = 1
    ax.axhline(1.0, color="#c0392b", lw=1.4, ls="--", zorder=4)
    on = [p for p in pts if abs(p[0] * p[1] * h * h - 1) < 1e-9]
    ax.scatter([p[2] for p in on], [p[3] for p in on], s=64,
               facecolors="none", edgecolors="#c0392b", lw=1.6, zorder=6)
    # unit raw pair (1,1): grid a=b=1/h -> (0,1), shell index n = 1/h^2
    ax.scatter([0], [1], marker="*", s=300, color="#c0392b", zorder=7)
    n0 = int(round(1 / h ** 2))
    ax.annotate(f"unit pair (1,1)\nshell n = {n0}", (0, 1), (0.55, 1.35),
                fontsize=8.5, color="#c0392b",
                arrowprops=dict(arrowstyle="->", color="#c0392b", lw=1.0))
    # smallest parabolas' vertices at X = +/- h/2 = +/- q
    q = h / 2
    for sgn in (-1, 1):
        ax.scatter([sgn * q], [0], marker="v", s=70, color="#e67e22", zorder=7)
    ax.annotate(f"vertices $\\pm q = \\pm{np.format_float_positional(q, trim='-')}$",
                (q, 0), (q + 0.35, 0.28), fontsize=8.5, color="#e67e22")
    # offset ruler
    ks = np.arange(-4, 5)
    ax.scatter(ks * q, [-0.33] * len(ks), marker="|", s=90, color="#555555")
    ax.annotate(f"offsets $X \\in ({np.format_float_positional(q, trim='-')})\\mathbb{{Z}}$",
                (0, -0.62), ha="center", fontsize=8.5, color="#555555")
    ax.set_xlim(-XMAX, XMAX); ax.set_ylim(-0.85, YMAX + 0.25)
    ax.set_xlabel("X  (offset)"); ax.set_title(f"{title}\n{sub}", fontsize=10.5)
    ax.grid(alpha=0.15)

fig, axes = plt.subplots(1, 2, figsize=(11.5, 5.2), sharey=True)
panel(axes[0], 1.0, "EM:  $h = 1$,  $q = 1/2$",
      r"pair products $(k/2)^2$;  $r = \log n$;  $r=0$ at shell $n = 1$")
panel(axes[1], 0.5, "Gravitational dyons:  $h = 1/2$,  $q = 1/4$",
      r"pair products $(k/4)^2$;  $r = \log(n/4)$;  $r=0$ at shell $n = 4$")
axes[0].set_ylabel("Y  (GM, geometric mean)")
fig.tight_layout()
fig.savefig("grids_parabolic.png", dpi=200)
print("saved grids_parabolic.png")
