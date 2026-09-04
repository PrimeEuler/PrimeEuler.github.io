# Cone Derivation Ledger v13.209 — Casimir / Null-Diamond Audit

Date: 2026-09-04

Scope: mathematical and dependency audit of
`papers/Casimir_Null_Diamond_Standalone_v2_Audited.tex` against the current
Paper A / Paper B / Paper C / Discriminant-12 project baseline.

## Status

**Core result: PASS.**

The standalone note should be treated as an **active audited foundation
candidate**, not as an exploratory paper. Its core theorem is independent of
the unsettled global power-map claims in Paper B and survives the current
Paper-C reconciliation issues.

Recommended placement after correction: `foundations/`, as a bridge note
between the cone geometry / rank-one ladder algebra and the discriminant-12
arithmetic return. Preserve the current v2 PDF/TeX in `papers/` as a historical
audited snapshot until a corrected foundation version is created and built.

## 1. Primitive null-edge geometry — PASS

For

\[
Q(\alpha,\beta)=\left(\frac{\alpha^2-\beta^2}{2},\alpha\beta,
\frac{\alpha^2+\beta^2}{2}\right)
\]

with Lorentz form

\[
\langle(X,Y,T),(X',Y',T')\rangle_\eta
=TT'-XX'-YY',
\]

direct expansion gives

\[
\langle Q(a,b),Q(c,d)\rangle_\eta
=\frac12(ad-bc)^2.
\]

Hence for midpoint and half-difference

\[
M_F=\frac{Q_1+Q_2}{2},\qquad D_F=\frac{Q_1-Q_2}{2},
\]

one obtains

\[
M_F^2=\frac{\Delta^2}{4},\qquad
D_F^2=-\frac{\Delta^2}{4},\qquad
\langle M_F,D_F\rangle_\eta=0,
\]

where \(\Delta=ad-bc\). For a primitive unimodular pair,
\(|\Delta|=1\), therefore

\[
\boxed{M_F^2=\frac14}.
\]

Scaling the cone coordinates by a lattice spacing \(\delta\) gives

\[
\boxed{M_F^2=\frac{\delta^2}{4}}.
\]

This derivation is exact.

### Minor wording correction

The statement that primitive integer spinors with \(|\Delta|=1\) give Farey
adjacent projective ratios should specify the usual choice of reduced
projective representatives / denominator orientation. The determinant theorem
does not depend on this convention.

## 2. SU(2) Casimir completion — PASS

With highest-weight scale \(J\), weight spacing \(\delta\), and

\[
C_+=J(J+\delta),\qquad R_+=J+\frac\delta2,
\]

one has exactly

\[
R_+^2=C_++\frac{\delta^2}{4}=C_++M_F^2.
\]

For the raising coefficient,

\[
A_+^2=(J-q)(J+q+\delta)
=C_+-q(q+\delta),
\]

and with

\[
Z_+=q+\frac\delta2
\]

this becomes

\[
\boxed{A_+^2=R_+^2-Z_+^2}.
\]

The corresponding cone point \((X,Y,T)=(Z_+,A_+,R_+)\) is null. The lowering
formula is identical with \(Z_-=q-\delta/2\).

No defect found.

## 3. SU(1,1) Casimir completion — PASS, with downstream convention guardrail

For a positive-discrete-series parameter \(K\),

\[
C_-=K(K-\delta),\qquad R_-=K-\frac\delta2,
\]

so

\[
R_-^2=C_-+\frac{\delta^2}{4}=C_-+M_F^2.
\]

The raising coefficient

\[
A_+^2=q(q+\delta)-C_-
\]

becomes

\[
\boxed{A_+^2=Z_+^2-R_-^2},
\qquad Z_+=q+\frac\delta2.
\]

Thus \((X,Y,T)=(R_-,A_+,Z_+)\) is null. The standalone theorem is correct.

### Important Paper-C convention issue

The present Paper C source states, for the two-mode realization, that the
positive-discrete-series Bargmann index is

\[
k=\frac{n_1-n_2+1}{2}=X
\]

for every Fock state. Globally this is not the positive discrete-series index.
For fixed number difference \(d=n_1-n_2\), the standard positive-discrete-series
parameter is

\[
\boxed{k=\frac{|d|+1}{2}}.
\]

If one restricts to the oriented sector \(d\ge0\), then
\(k=(d+1)/2=X\) under the current Paper-C dictionary. The null-diamond
standalone theorem does not require the incorrect global identification, but
its source note must not cite Paper C as already audited until this is fixed.

## 4. Four-corner oscillator transition cell — PASS

For a two-mode number state \(|p,q\rangle\), the four standard quadratic
transition amplitudes are

\[
K_-:pq,\qquad
J_+:(p+1)q,\qquad
J_-:p(q+1),\qquad
K_+:(p+1)(q+1),
\]

up to the common \(\delta^2\) scale used in the note. With factor-cell center

\[
(u_c,v_c)=\delta\left(p+\frac12,q+\frac12\right),
\]

the four transition vertices are cardinal half-steps

\[
(\Delta X,\Delta T)
=\left(\pm\frac\delta2,0\right),
\quad
\left(0,\pm\frac\delta2\right),
\]

and the four cone identities reproduce the four amplitudes exactly.

This gives a valid geometric realization of the same half-edge square
\(\delta^2/4\).

### Clarification recommended

The factor-cell construction and the Paper-C state dictionary
\(x=n_1+1,\ y=n_2\) are related but are not literally the same point: the
Paper-C state point occupies one transition vertex of the four-corner cell.
The next version should say this explicitly.

## 5. Cyclotomic normalization — PASS

The note uses

\[
g_{12}=\begin{pmatrix}3&1\\2&1\end{pmatrix},\qquad
H=g_{12}-2I=\begin{pmatrix}1&1\\2&-1\end{pmatrix},
\]

for which

\[
H^2=3I.
\]

Then

\[
\mathcal Z=\frac{H+iI}{2}
\]

satisfies

\[
\boxed{\mathcal Z\overline{\mathcal Z}=I}.
\]

Its eigenvalues are primitive twelfth roots, and the normalization agrees with
the current Discriminant-12 paper. The note correctly distinguishes this
relative norm from the Lorentz norm and from the representation-theoretic
Casimir.

The order statement

\[
\mathcal O_K/\mathcal O_0\cong(\mathbb F_2)^2,
\qquad
\mathcal O_0=\mathbb Z[\sqrt3,i],
\]

is consistent with the current v0.3.3 computation
\([\mathcal O_K:\mathcal O_0]=4\).

## 6. Ramified Boolean return — PASS

Modulo two,

\[
\bar g_{12}=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

Under the relabeling

\[
\Phi(x,y)=(\varepsilon_1,\varepsilon_2)=(x,x+y),
\]

one obtains

\[
\boxed{\Phi\bar g_{12}\Phi^{-1}
(\varepsilon_1,\varepsilon_2)
=(\varepsilon_2,\varepsilon_1)}.
\]

Thus the return is factor exchange, not a nonzero Boolean translation. Also

\[
\bar q_{12}=\varepsilon_1\oplus\varepsilon_2.
\]

The extension

\[
V_4^{\rm tr}\rtimes C_2\cong D_8
\]

is correct, and the note properly distinguishes this translation \(V_4\), the
cyclotomic Galois \(V_4\), the ramified Boolean quotient, and the cyclotomic
integral-closure quotient.

This matches the current Discriminant-12 v0.3.3 framework.

## 7. Scope discipline — PASS

The note explicitly does **not** claim:

- that Farey/null-edge arithmetic causes the Weyl or Casimir shift;
- that the compact and noncompact ladder systems are the same algebra;
- that the Lorentz norm, Casimir, and cyclotomic relative norm are one universal
  quadratic form;
- that the several four-state quotients are canonically identical.

Those guardrails should be preserved.

## 8. Required corrections before foundation promotion

Create a next source version rather than silently editing the historical v2
snapshot. The next version should:

1. replace the phrase `existing audited quantum-realization manuscript` with a
   statement that Paper C is the current working quantum-realization manuscript
   and remains under audit;
2. state the two-mode positive-discrete-series convention
   \(k=(|n_1-n_2|+1)/2\), with \(k=X\) only after choosing the oriented
   \(n_1\ge n_2\) sector under the current dictionary;
3. clarify that the Paper-C state point is a transition vertex of the
   four-corner factor cell, not the cell center;
4. add the standard projective-orientation qualification to the Farey-adjacency
   sentence.

These are correction/clarification items; none changes the core
Casimir--null-edge theorem.

## 9. Placement decision

**Recommendation: move the corrected next version into `foundations/`.**

Reason: the paper supplies a reusable exact bridge

\[
\text{factor cone}
\longleftrightarrow
\text{rank-one Casimir completion}
\longleftrightarrow
\text{primitive null-edge centering}
\]

and independently reproduces the discriminant-12 cyclotomic/Boolean return.
It is therefore upstream structural material rather than merely a downstream
application of the principal Discriminant-12 paper.

Suggested role in the foundation chain:

1. Paper A v2.4 — cone geometry.
2. Paper B v2 — Lorentz orbit/eigen-coordinate structure (after audit).
3. Paper C — oscillator realizations (after correction/reconciliation).
4. **Casimir / Null-Diamond bridge note** — exact edge-centered Casimir and
   arithmetic null-edge invariant; independent core theorem, with oscillator
   and discriminant-12 interfaces.
5. Principal Discriminant-12 paper — arithmetic return built on the shared
   geometric language.

The current `papers/Casimir_Null_Diamond_Standalone_v2_Audited.{tex,pdf}` should
remain untouched as the historical audited v2 snapshot until the corrected
foundation version is created and compiled.
