from pathlib import Path

# Publication wrapper for fig_cutting_plane_tangent_circle_audit.py.
# It preserves the audited geometry exactly while changing only publication
# presentation details: compact tangent labels and neutral panel titles.

source = Path(__file__).with_name("fig_cutting_plane_tangent_circle_audit.py")
text = source.read_text()

old = '''# Exact tangent points for u=5,6,7: vertices of the mirror parabolas.
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

new = '''# Exact tangent points for u=5,6,7: vertices of the mirror parabolas.
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

# Remove audit-only wording without changing any plotted geometry.
text = text.replace("(a) Flat audit:", "(a) Flat:")
text = text.replace("(b) Side audit:", "(b) Side:")
text = text.replace("(c) 3D audit:", "(c) 3D:")

exec(compile(text, str(source), "exec"), {"__file__": str(source), "__name__": "__main__"})
