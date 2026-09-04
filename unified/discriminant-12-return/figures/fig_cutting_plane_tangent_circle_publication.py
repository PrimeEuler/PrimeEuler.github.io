from pathlib import Path

# Publication wrapper for fig_cutting_plane_tangent_circle_audit.py.
# It preserves the audited geometry exactly while changing only publication
# presentation details: compact tangent labels and neutral panel titles.

source = Path(__file__).with_name("fig_cutting_plane_tangent_circle_audit.py")
text = source.read_text()

old = r'''# Exact tangent points for u=5,6,7: vertices of the mirror parabolas.
for u in TANGENT_LEVELS:
    Tc = u / 2.0
    axA.plot([-Tc, Tc], [0, 0], "o", ms=5.8, color="#111111", zorder=9)
    axA.annotate(
        rf"$(-{u}/2,0)$",
        (-Tc, 0),
        textcoords="offset points",
        xytext=(-4, -14),
        ha="right",
        fontsize=7.5,
    )
    axA.annotate(
        rf"$({u}/2,0)$",
        (Tc, 0),
        textcoords="offset points",
        xytext=(4, -14),
        ha="left",
        fontsize=7.5,
    )
'''

new = r'''# Exact tangent points for u=5,6,7: vertices of the mirror parabolas.
# Publication layout: keep both mirror points, but label only the +X side.
# The coordinate formula (T,X)=(u/2,+-u/2) is already stated in the text
# and caption, so compact u-labels are clearer here than six coordinate labels.
label_offsets = {
    5: (18, -22),
    6: (28, -36),
    7: (38, -50),
}
for u in TANGENT_LEVELS:
    Tc = u / 2.0
    axA.plot([-Tc, Tc], [0, 0], "o", ms=5.2, color="#111111", zorder=9)
    dx, dy = label_offsets[u]
    axA.annotate(
        rf"$u={u}$",
        (Tc, 0),
        textcoords="offset points",
        xytext=(dx, dy),
        ha="left",
        va="center",
        fontsize=8.0,
        color="#111111",
        arrowprops=dict(arrowstyle="-", color="#555555", lw=0.65),
        zorder=10,
    )
'''

if old not in text:
    raise RuntimeError("Expected audited annotation block was not found; aborting publication patch.")

text = text.replace(old, new, 1)

# Remove audit-only wording while retaining the audited full K=1,...,12 shell
# family and the exact u=5,6,7 tangent-circle checks.
text = text.replace(
    '"(a) Flat audit: all $K=1,\\\\ldots,12$ circles\\n"\n    "with exact $u=5,6,7$ parabola tangencies"',
    '"(a) Flat: complete fixed-sum circle family\\n"\n    "with $u=5,6,7$ parabola tangencies"',
)
text = text.replace(
    '"(b) Side audit: half-step $T=K/2$ shells\\n"\n    "and the $u=5,6,7$ generator tangencies"',
    '"(b) Side: multiplication table and half-step shells\\n"\n    "with the $u=5,6,7$ tangent levels"',
)
text = text.replace(
    '"(c) 3D audit: complete fixed-$T$ circle family\\n"\n    "through the $x+y=12$ boundary"',
    '"(c) 3D: complete fixed-$T$ circle family\\n"\n    "through the $x+y=12$ boundary"',
)

exec(compile(text, str(source), "exec"), {"__file__": str(source), "__name__": "__main__"})
