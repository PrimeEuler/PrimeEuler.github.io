# Cone Derivation Ledger v13.205 — Paper A Figure Pipeline Audit

Date: 2026-09-04

Labels: `[S]` source / `[D]` derived / `[Audit]` verified / `[Fix]` corrected / `[Guardrail]`

## 1. Scope `[S]`

This checkpoint audits the figure-generation pipeline for the authoritative
Paper A working source

`foundations/PaperA_ConicTheorem_v2.4.tex`

inside the project root

`unified/discriminant-12-return/`.

The audit covers repository placement, shell build paths, figure-source/output
precedence, and the mathematics encoded by the two Paper A generators.

## 2. Canonical figure location `[Fix]`

Paper A previously had `fig_cutting_plane_3panel.py` and generated
`fig_cutting_plane_3panel.pdf/.png` inside `foundations/`.

That was structurally unsafe because Paper A uses

```tex
\graphicspath{{./}{../figures/}}
```

so a stale local figure in `foundations/` shadows the canonical asset in
`figures/`.

The project convention is now:

- foundation TeX/build scripts remain in `foundations/`;
- all active figure generators and generated figure assets live in `figures/`;
- no Paper A figure generator or generated Paper A figure is retained in
  `foundations/`.

The old foundation-local generator and stale PDF/PNG were removed.

## 3. Paper A build script `[Fix]`

`foundations/build_paper_a.sh` now targets

`PaperA_ConicTheorem_v2.4.tex`

and generates both Paper A figures from

`../figures/`:

```bash
python3 "$FIG/fig_cutting_plane_3panel.py"
python3 "$FIG/fig_divisor_summatory_11_3panel.py"
```

The area companion build already generated its figure from `figures/`, so no
path correction was required there. The Paper B build currently performs no
figure-generation step.

## 4. Cutting-plane generator audit `[Audit][Fix]`

Canonical source:

`figures/fig_cutting_plane_3panel.py`

The earlier generator lost geometric detail and inherited an incorrect side-view
mesh. The audited canonical generator is now self-contained and encodes the
following exact geometry.

### 4.1 Fundamental two-sided projection `[D]`

\[
X=\frac{x-y}{2},\qquad Y^2=xy,\qquad T=\frac{x+y}{2},
\]

with

\[
X^2+Y^2=T^2.
\]

Panel (a) and the conic sections in panel (c) display both signs
\(Y=\pm\sqrt{xy}\). Panel (b) is the flat carrier at \(Y=0\).

### 4.2 Complete fixed-sum shell family `[Fix]`

The previous canonical generator drew only the even shells
\(K=2,4,\ldots,12\).

The audited generator now draws every shell

\[
K=1,2,\ldots,12,
\qquad T=K/2,
\qquad X^2+Y^2=(K/2)^2.
\]

This restores the half-step radius structure needed by the tangent-circle
statement.

### 4.3 Exact tangent examples `[D]`

The levels

\[
u=5,6,7
\]

are emphasized. For each level the row/column parabola vertices are

\[
(X,Y)=\left(\pm\frac u2,0\right),
\]

and the tangent fixed-sum circle has radius

\[
T=\frac u2.
\]

Thus the highlighted radii are

\[
\frac52,\ 3,\ \frac72.
\]

### 4.4 Positive-factor side-view mesh `[Fix]`

The old side-view loop extended lines from \(T=0\), duplicated levels, and
included negative factor levels outside the positive-factor triangle.

The corrected row segment for fixed \(x=u\) is

\[
T+X=u,
\]

with endpoints

\[
\left(\frac u2,\frac u2\right)
\longrightarrow
\left(u-6,6\right),
\]

corresponding to \(y=0\) and \(x+y=12\).

The corrected column segment for fixed \(y=u\) is

\[
T-X=u,
\]

with endpoints

\[
\left(-\frac u2,\frac u2\right)
\longrightarrow
\left(6-u,6\right).
\]

Only \(u=1,\ldots,11\) is drawn for the integer positive-factor mesh.

### 4.5 Reflected cutting planes `[Audit]`

The figure retains the Paper A pair

\[
8x+4y=32,
\qquad
4x+8y=32,
\]

and plots both \(Y\)-lifts of their ellipse sections.

The side-view cutting-plane relation is

\[
(a+b)T+(a-b)X=c,
\]

or equivalently

\[
T=\frac{c+(b-a)X}{a+b}.
\]

For the red cut, the maximum \(Y^2\) point remains

\[
(x,y)=(2,4),
\qquad
(X,T)=(-1,3).
\]

### 4.6 Table domain `[Audit]`

The integer factor triangle

\[
x,y\ge1,
\qquad x+y\le12
\]

contains exactly

\[
T_{11}=66
\]

cells. The canonical generator asserts this count explicitly.

Integer product labels are shown on the upper lift only for readability; the
lower geometric parabolas and conic sections remain present. This is a display
choice, not a one-sided foundational map.

## 5. Divisor-summatory generator audit `[Audit][Fix]`

Canonical source:

`figures/fig_divisor_summatory_11_3panel.py`

The arithmetic content is correct:

\[
D(11)=29,
\qquad
T_{11}=66,
\qquad
A_{11}=66-29=37.
\]

The constant-product boundary is

\[
xy=11,
\qquad
T^2-X^2=11,
\]

and it meets \(x+y=12\) at

\[
(1,11),(11,1)
\longleftrightarrow
(X,T)=(-5,6),(5,6).
\]

The generator previously described \(Y=\sqrt{xy}\) as though it were the
fundamental Paper A map. That wording has been corrected.

The divisor figure intentionally displays only the upper lift

\[
Y=+\sqrt{xy}
\]

in its `(X,Y)` and 3D panels so the 29/37 discrete classification remains
readable. The reflected lower lift carries identical factor data and is omitted
only as a visualization convention. Paper A itself remains two-sided:

\[
Y^2=xy.
\]

## 6. Redundant helper-generator cleanup `[Fix]`

The temporary tangent-circle audit/publication wrapper scripts were removed
after their verified content was consolidated into the single canonical
`fig_cutting_plane_3panel.py`.

This leaves one unambiguous Paper A cutting-plane generator.

## 7. Generated-asset guardrail `[Guardrail]`

After generator changes, stale generated binaries must not remain in the
repository under the same filename.

The old divisor PNG was therefore removed. The current Paper A figure assets
must be regenerated by `foundations/build_paper_a.sh` before compiling v2.4.

Do not compile Paper A directly against an older committed PNG/PDF after a
figure-generator change.

## 8. Project documentation `[Fix]`

`README.md` now states that:

- figure generators belong in `figures/`, not `foundations/`;
- Paper A's active source is v2.4;
- `fig_cutting_plane_3panel.py` is the self-contained canonical generator;
- the divisor figure is intentionally an upper-lift visualization;
- the Paper A build script regenerates both figures before TeX compilation.

## 9. Publication status `[Audit]`

The Paper A figure **source pipeline** is now mathematically and structurally
audited.

A fresh v2.4 PDF should be built only after regenerating the two figures from the
current canonical generators. Until that regeneration occurs, no older Paper A
figure binary should be treated as the v2.4 publication asset.
