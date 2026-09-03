# Cone Derivation Ledger v13.178 — Figure Circle-Layer Audit

**Status:** Source-grounded continuation of v13.177  
**Date:** 2026-09-03  
**Scope:** Audit the actual circle-like objects in `unified/fig_cutting_plane_3panel.py` against the geometric tangent-circle theorem from v13.177.

## Audit convention

- **[S]** source-established
- **[D]** exact derived
- **[I]** interpretation
- **[O]** open
- **[Audit]** correction / limitation

---

## 1. What the current figure source actually draws

The current source `unified/fig_cutting_plane_3panel.py` contains two fundamentally different kinds of visually circular objects.

### 1.1 Geometric anti-diagonal circles

**[S]** In panel (a), the source explicitly draws

\[
X^2+Y^2=T^2
\]

using

```python
for K in range(2, Kmax + 1, 2):
    Tc = K / 2.0
    axA.plot(Tc * cos(theta), Tc * sin(theta), ...)
```

with `Kmax=12`.

Therefore the plotted radii are exactly

\[
\boxed{T=1,2,3,4,5,6.}
\]

These are the projections of the even anti-diagonals

\[
\boxed{x+y=2,4,6,8,10,12.}
\]

because

\[
T=\frac{x+y}{2}.
\]

Panel (c) draws the corresponding circles on the 3D cone at the same fixed values of `T`.

The highlighted dashed circle is

\[
\boxed{x+y=8\iff T=4.}
\]

---

## 2. The small circles around product labels are annotations, not conic geometry

**[S]** For every multiplication-table point, panel (a) writes the product value with

```python
bbox=dict(boxstyle="circle,pad=0.03", fc="white", ec="none", alpha=0.7)
```

and panel (b) uses the same circular bounding-box style.

Thus the source contains many small white circular-looking objects centered on table labels.

**[Audit]** These small circles are typographic bounding boxes. They are not defined by an equation in `(x,y)`, `(X,Y)`, or `(X,Y,T)`, and the code assigns them no mathematical radius in Cone coordinates.

Therefore any apparent tangency involving those particular label circles in this source is not, by itself, a geometric theorem.

This does **not** establish that every visually observed small circle in Paper A v2 is merely an annotation; it establishes only that the current reconstructed `fig_cutting_plane_3panel.py` has a non-geometric circular annotation layer that must be separated from the actual anti-diagonal circles.

---

## 3. Comparison with the v13.177 parabola tangent-circle theorem

v13.177 proved that the row/column parabola at factor level `u` is tangent to the origin-centered fixed-`T` circle

\[
\boxed{T=\frac u2.}
\]

Equivalently the required anti-diagonal is

\[
\boxed{x+y=u.}
\]

The current source, however, plots only even anti-diagonals.

Therefore:

- for even `u`, the exact tangent circle from v13.177 is present;
- for odd `u`, the exact tangent circle is absent from the current background-circle layer.

In particular,

\[
\boxed{u=5\Rightarrow T=2.5}
\]

is not drawn,

\[
\boxed{u=6\Rightarrow T=3}
\]

is drawn,

and

\[
\boxed{u=7\Rightarrow T=3.5}
\]

is not drawn.

**[D]** The current even-`K` circle background samples only every other member of the full parabola-tangent circle family.

---

## 4. Why the half-step radii were hidden

The source loop

\[
K=2,4,6,8,10,12
\]

forces

\[
T=K/2=1,2,3,4,5,6.
\]

But the natural circle attached to integer factor level `u` is

\[
T=u/2.
\]

For consecutive integer levels

\[
u=1,2,3,\ldots,
\]

the complete tangent-circle radius sequence is therefore

\[
\boxed{
\frac12,1,\frac32,2,\frac52,3,\frac72,4,\ldots
}
\]

with spacing

\[
\boxed{\Delta T=\frac12.}
\]

**[D]** The mod-`0.5` radius structure is intrinsic to the complete integer row/column parabola family; the present figure suppresses half of it by drawing only even anti-diagonals.

This is independent of floor quantization and independent of the label-circle annotations.

---

## 5. A more faithful geometric background

To display the complete tangent-circle family for integer rows/columns `u=1,...,12`, the natural loop is not the current even-`K` loop but

\[
\boxed{K=1,2,3,\ldots,12,}
\]

with

\[
\boxed{T=K/2.}
\]

Then every integer factor level `u=K` has its exact tangent circle visible.

For the local `5,6,7` region this would explicitly display

\[
\boxed{T=2.5,3,3.5.}
\]

**[I]** This is likely the cleanest figure-level test of the half-step phenomenon: add the missing odd-`K` anti-diagonal circles and inspect the row/column parabola vertices directly, without relying on the typographic product circles.

---

## 6. The exact tangency points in the flat panel

For fixed row level `u`, the row parabola is

\[
Y^2=u^2+2uX.
\]

Its vertex is

\[
\boxed{V_u^- = \left(-\frac u2,0\right).}
\]

The mirror column parabola has vertex

\[
\boxed{V_u^+ = \left(+\frac u2,0\right).}
\]

The circle

\[
X^2+Y^2=\left(\frac u2\right)^2
\]

passes through both vertices, and v13.177 established tangency there.

Thus the complete integer family produces vertex/tangent points along the `Y=0` axis at

\[
\boxed{X=\pm\frac12,\pm1,\pm\frac32,\pm2,\ldots.}
\]

**[D]** The same half-grid that appears in the radius variable also appears on the flat-panel `X` axis as the exact sequence of parabola vertices.

---

## 7. Relation to the side-view integer mesh

Paper A uses

\[
x=T+X,\qquad y=T-X.
\]

For the row-parabola vertex

\[
(X,Y,T)=\left(-\frac u2,0,\frac u2\right),
\]

we obtain

\[
x=0,\qquad y=u.
\]

For the mirror vertex

\[
(X,Y,T)=\left(+\frac u2,0,\frac u2\right),
\]

we obtain

\[
x=u,\qquad y=0.
\]

So these half-step tangent points are exactly the two axis endpoints of the anti-diagonal

\[
\boxed{x+y=u.}
\]

**[D]** The factor-space integer `u`, the flat-panel circle radius `u/2`, the flat-panel parabola-vertex coordinate `|X|=u/2`, and the anti-diagonal intercepts `(u,0),(0,u)` are four coordinate descriptions of the same exact structure.

---

## 8. What this resolves about the visual observation

There are now three distinct circle-related mechanisms that must not be conflated:

1. **Geometric fixed-`T` circles**
   \[
   X^2+Y^2=T^2,
   \]
   arising from anti-diagonals `x+y=2T`.

2. **Exact parabola tangent circles**
   \[
   T=u/2,
   \]
   one for every row/column level `u`; this is a subfamily of item 1 when the corresponding anti-diagonal is drawn.

3. **Circular text bounding boxes** around multiplication-table product labels in the current Python source; these are annotations only.

**[Audit]** Any future tangent claim from the figure must first identify which of these three layers is involved.

---

## 9. New exact synthesis

For integer level `u`, the chain is

\[
\boxed{
u
\longleftrightarrow
x+y=u
\longleftrightarrow
T=\frac u2
\longleftrightarrow
X^2+Y^2=\frac{u^2}{4}
\longleftrightarrow
X=\pm\frac u2\text{ parabola vertices}.
}
\]

Consequently consecutive integer rows generate a half-step circle foliation:

\[
\boxed{
\Delta u=1
\quad\Longrightarrow\quad
\Delta T=\Delta|X|=\frac12.
}
\]

This is an exact geometric source of the project's recurring half-unit structure.

---

## 10. Next controlled figure experiment

**[O]** Modify the reconstructed cutting-plane figure in a minimal audit version that:

- draws all anti-diagonal circles `K=1,...,12`, not only even `K`;
- distinguishes odd-`K` half-radius circles from even-`K` integer-radius circles;
- marks the exact `u=5,6,7` row/column parabola vertices and their tangent circles;
- temporarily removes circular product-label bounding boxes so no annotation circle can be mistaken for geometry.

That figure will directly test whether the originally observed local small-circle pattern survives after the annotation-circle layer is removed.
