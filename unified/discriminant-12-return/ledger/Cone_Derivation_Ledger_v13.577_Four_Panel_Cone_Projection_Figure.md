# Cone Derivation Ledger v13.577 — Four-Panel Cone Projection Figure

**Renumbering note:** originally filed as v13.575, which collided with the already-pushed `Cone_Derivation_Ledger_v13.575_External_Audit_Round_53.md`. Renumbered to v13.577 during External Audit Round 54. Content is unchanged.

## Status
Figure/source integration only. No new theorem is promoted in this entry. The geometry is the already-established AM-GM cone geometry and arithmetic-incidence structure; this entry records the approved visualization and its projection interpretation.

## 1. Source update

The figure source

`unified/discriminant-12-return/figures/discriminant12_mod12_v4_cone_triple.py`

was updated from the earlier three-panel construction to the approved clean four-panel construction.

Source-update commit:

`62396d6a6e2137cf18f82fe9fc64caeecbf61135`

The output filename remains

`mod12_v4_cone_triple.png`.

The exact panel titles are frozen as:

- `(a) T-Circle`
- `(b) X-Triangle`
- `(c) Y-Triangle`
- `(d) 3D Cone`

No inline `T_5`, `T_11`, or `T_7` labels are used, and no V4 legend is used. Their certified arithmetic meaning remains in v13.574/v13.557 and is not reassigned to figure colors.

## 2. Geometry retained

The cone is

`X^2 + Y^2 = T^2`.

The colored family is the fixed-X family. For the mod-12 shell data

`r in {1,5,7,11}`,

with

`c=(r-1)/2`,  `R=(r+1)/2`,

the colored cone curves satisfy

`X=+/-c`

and therefore

`T^2-Y^2=c^2`.

The black family is the fixed-r/fixed-Y family:

`Y=+/-sqrt(r)`,

hence

`T^2-X^2=r`.

The blue arithmetic mesh and the distinguished unit family are retained from the prior construction.

## 3. Complementary triangle projections

Panel (b), the X-Triangle, is the X-T projection.

Under this projection the colored fixed-X curves collapse to straight vertical carriers, while the black fixed-r/fixed-Y curves remain hyperbolas

`T=sqrt(X^2+r)`.

The distinguished blue unit family projects to the straight pair

`X=+/-(T-1)`.

Panel (c), the Y-Triangle, is the complementary Y-T projection.

Under this projection the black fixed-Y curves collapse to straight vertical carriers

`Y=+/-sqrt(r)`,

while the colored fixed-X curves remain hyperbolas

`T=sqrt(c^2+Y^2)`.

The distinguished blue unit family projects to the parabola

`T=(1+Y^2)/2`.

Thus the two triangle panels show the same cone families under complementary coordinate projections: a family that appears curved in one projection can appear straight in the other.

## 4. T-Circle and 3D panels

Panel (a) retains the fixed-T circular shells, colored vertical carriers, blue arithmetic mesh/unit curves, and the black horizontal fixed-r carriers.

Panel (d) retains the corresponding objects on the 3D cone itself:
- fixed-T shell circles;
- colored fixed-X curves;
- black fixed-Y/fixed-r curves;
- blue row/column mesh;
- distinguished blue unit curves.

The triangle panels are projections of these same 3D families; they are not independent recolorings or reassigned curve families.

## 5. Styling decision

The approved line-weight reduction applies only to the principal shell/carrier curves. The fine lattice/mesh widths remain unchanged so the arithmetic background does not disappear.

The rejected V4 annotations/legend are intentionally absent. In particular, figure colors are not assigned a second meaning as `T_5`, `T_11`, or `T_7`. Any later Paper A / Discriminant-12 Return discussion should describe the certified V4 correspondence in prose and cite the appropriate ledger entries rather than encode it by an unsupported color legend.

## Guardrails

- This entry records a visualization/source change, not a new proof.
- Do not identify the cone `(X,Y,T)` basis with the character basis.
- Preserve the v13.557/v13.574 projective correspondence independently of the figure colors.
- The X-Triangle and Y-Triangle must remain complementary projections of the same 3D cone families.
- Do not use generative-image tools for this technical figure. The canonical figure is generated from the checked-in Python/Matplotlib source.
