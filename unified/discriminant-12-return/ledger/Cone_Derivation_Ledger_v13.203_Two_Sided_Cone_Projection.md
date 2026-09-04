# Cone Derivation Ledger v13.203 — Two-Sided Multiplication-Table Cone Projection

Date: 2026-09-03

Status labels: **[S]** source-established, **[D]** exact derived, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## 1. Foundational clarification

**[D]** The multiplication table is first represented as a flat factor triangle in the plane `Y=0` using

\[
X=\frac{x-y}{2},\qquad T=\frac{x+y}{2}.
\]

The geometric-mean coordinate is a normal displacement from this flat carrier. The fundamental cone projection is therefore two-sided:

\[
\boxed{
\Pi_\pm(x,y)=
\left(
\frac{x-y}{2},\ \pm\sqrt{xy},\ \frac{x+y}{2}
\right).
}
\]

Equivalently,

\[
\boxed{Y^2=xy.}
\]

This replaces the earlier foundational wording `Y=+sqrt(xy)` in Paper A. The positive square root remains a legitimate one-sided branch choice for calculations that require a single-valued planar map.

## 2. Cone identity and two geometric images

**[D]** Since

\[
xy=(T+X)(T-X)=T^2-X^2,
\]

both projected points satisfy

\[
\boxed{X^2+Y^2=T^2.}
\]

For `xy>0`, one factor pair has two symmetric cone images. They are exchanged by

\[
\boxed{\iota_Y:(X,Y,T)\mapsto(X,-Y,T).}
\]

The inverse factor coordinates

\[
x=T+X,\qquad y=T-X
\]

do not depend on the sign of `Y`; hence the sign of `Y` is geometric lift data, not additional factor data.

**[D]** On the boundary `xy=0`, the two projections coalesce at `Y=0`.

## 3. Distinguish the two reflections

**[D]** Factor exchange is

\[
(x,y)\mapsto(y,x)
\quad\Longleftrightarrow\quad
X\mapsto-X,
\]

with `Y^2,T` fixed.

**[D]** The two-sided cone involution is instead

\[
Y\mapsto-Y,
\]

with `X,T` fixed.

These are distinct symmetries and must not be conflated.

## 4. Complete conic sections

**[D]** A flat factor-line

\[
ax+by=c
\]

becomes the cutting plane

\[
(a-b)X+(a+b)T=c.
\]

Together with the two-sided relation `Y^2=xy`, its projection supplies the complete `Y -> -Y` symmetric plane-cone section rather than only the upper half.

The Paper A classification remains:

\[
ab>0:\text{ ellipse},\qquad
ab=0:\text{ parabola},
\]

\[
ab<0,\ c\ne0:\text{ nondegenerate hyperbola},
\]

with `ab<0,c=0` the degenerate generator section.

**[Audit]** This clarification removes the artificial `Y>=0` obstruction identified in the first Paper B orbit audit. It does **not** by itself prove that every full conic section is one global one-parameter Lorentz orbit; connected components, time orientation, and hyperbolic branches still require the planned Paper B audit.

## 5. Rows and columns

**[D]** A fixed row `x=u` gives the complete parabola

\[
\boxed{Y^2=u^2-2uX,}
\]

and a fixed column `y=u` gives

\[
\boxed{Y^2=u^2+2uX.}
\]

Both signs of `Y` are part of the same projected row/column. For `u=1`, both cross `X=0` at `Y=+1` and `Y=-1` and continue through the lower half exactly as through the upper half.

## 6. Fixed sums and the circle

**[D]** A flat anti-diagonal

\[
x+y=K
\]

fixes

\[
T=K/2.
\]

After the two-sided projection its image lies on the complete cutting circle

\[
\boxed{X^2+Y^2=(K/2)^2.}
\]

Thus the circle is not an auxiliary object added after the fact: it is the two-sided cone projection of a fixed-sum line in the flat multiplication triangle.

## 7. Constant-product hyperbolas

**[D]** A factor hyperbola

\[
xy=N
\]

projects to the reflected pair of cone levels

\[
\boxed{Y=\pm\sqrt N,}
\]

while both share the same side-view relation

\[
\boxed{T^2-X^2=N.}
\]

For a simultaneous fixed-sum cut `x+y=S`, the intersection points satisfy

\[
Y=\pm\sqrt N,
\qquad
X=\pm\sqrt{S^2/4-N},
\]

whenever the factor-domain conditions are met.

## 8. Exact geometric complex conjugation

**[D]** On a fixed-`T` cutting circle introduce the ordinary complex coordinate

\[
z=X+iY.
\]

The two cone projections of one factor pair are

\[
z_+=X+i\sqrt{xy},\qquad
z_-=X-i\sqrt{xy},
\]

so

\[
\boxed{z_-=\overline{z_+}.}
\]

Moreover,

\[
\boxed{z\bar z=X^2+Y^2=T^2.}
\]

An exact factor-coordinate form is

\[
\boxed{
z_+=\frac{(\sqrt x+i\sqrt y)^2}{2},\qquad
z_-=\frac{(\sqrt x-i\sqrt y)^2}{2}.
}
\]

**[Audit]** This is an exact geometric complexification of each fixed-`T` circle. It is **not** yet identified with the discriminant-12 cyclotomic complexification or its Galois conjugation. Any bridge to `K_12=Q(zeta_12)`, `Z=(H+iI)/2`, or `T_11` requires a separate proof.

## 9. Area-paper convention

**[Audit]** The geometry-only area companion uses the single-valued upper branch

\[
F_+(x,y)=\left(\frac{x-y}{2},+\sqrt{xy}\right).
\]

Its Jacobian, half-disk areas, parabola-secant chamber, and weighted angular measure remain one-sided and unchanged. The lower branch is the reflected copy. Full unsigned geometric area over both lifts doubles the corresponding one-sided image area.

In particular, do not silently replace the area-paper branch by both signs inside a Jacobian calculation.

## 10. Paper A source update

**[S]** `foundations/PaperA_ConicTheorem_v2.2.tex` was revised to make the flat `Y=0` factor triangle and two-sided projection foundational. The source now:

- defines `Pi_+` and `Pi_-` through `Y^2=xy`;
- distinguishes factor exchange `X -> -X` from cone-lift reflection `Y -> -Y`;
- states that rows/columns are complete parabolas under the two-sided projection;
- states that fixed sums give complete circles;
- states that constant products project to `Y=+-sqrt(N)`;
- records `z_- = conjugate(z_+)` and `z conjugate(z)=T^2` as exact geometric facts;
- explicitly keeps the area companion on the upper branch;
- explicitly refuses any automatic arithmetic/cyclotomic identification.

Paper A update commit:

`8ef8d443751decb6cd3b5e2cacaa2559e6010f57`

## 11. Consequence for the Paper B audit

**[I]** The correct foundational carrier for Paper B is now the full two-sided projected conic geometry, not an upper-half `Y>=0` trace. This materially strengthens the possibility that Paper B's intended “complete orbit” theorem can be repaired rather than weakened.

**[O]** The next audit must still establish, case by case, whether the relevant one-parameter subgroup is transitive on the complete section or only on connected components. The earlier warning about the insufficient dimension argument remains in force.

## 12. New publication guardrails

71. Do not describe `Y=+sqrt(xy)` as the fundamental Paper A cone map; the fundamental relation is `Y^2=xy`, with two projections `Pi_+-`.
72. Do not conflate factor exchange `X -> -X` with cone-side reflection `Y -> -Y`.
73. Do not double the area-paper formulas merely by changing notation; they are explicitly upper-branch formulas unless a two-sided area is requested.
74. Do not identify geometric conjugation `X+iY <-> X-iY` with discriminant-12 cyclotomic/Galois conjugation without a proved bridge.
75. Do not infer Paper B global orbit transitivity solely from the newly restored lower cone side; connected-component and subgroup-transitivity proofs are still required.
