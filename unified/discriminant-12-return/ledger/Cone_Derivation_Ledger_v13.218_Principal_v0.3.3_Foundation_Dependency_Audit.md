# Cone Derivation Ledger v13.218 — Principal v0.3.3 Foundation Dependency Audit

Date: 2026-09-04

Status labels: [S] source-established, [D] exact derived, [Audit] correction/reconciliation, [Pub] publication/pipeline status.

## Scope

This checkpoint performs the downstream audit requested by ledger v13.217: `papers/Discriminant_12_Return_v0.3.3.tex` is checked against the now-stabilized foundation chain

1. Paper A v2.4;
2. Area note v1.1;
3. Paper B v2.1;
4. Paper C v1.1;
5. Casimir / Null-Diamond v2.1.

The purpose is not to re-prove the already audited discriminant-12 algebra, but to identify any remaining category, notation, or carrier mismatches introduced by the newer foundation reconciliations.

## 1. Executive verdict

The principal paper's algebraic spine remains valid. No failure was found in the centered-Cayley identities, trace-4 selection, period-[1,2] normalization, discriminant 12, ramified ideal realization, Pell-Lorentz form, cyclotomic integral carrier, index-4 suborder calculation, `F_4` residue field, finite-field trace calculation, or the `n=11` narrow-class / Artin specialization.

However, the stabilized foundation chain exposes one **important finite-reduction category correction** and several synchronization repairs. These are significant enough to warrant a new source version rather than silently editing v0.3.3.

Recommended next source: `papers/Discriminant_12_Return_v0.3.4.tex`.

## 2. [Audit — important] Frobenius is a transported mod-2 matrix action, not the literal residue reduction of multiplication by the Pell unit

The current abstract and theorem say, in effect, that the "reduced Pell return is Frobenius" on the cyclotomic residue field. The matrix statement behind this is exact, but the carrier language must be sharpened.

On the ramified ideal basis `f=(f_1,f_2)=(2,sqrt(3)-1)`, reduction modulo `2` gives

\[
\bar g_{12}=\begin{pmatrix}1&1\\0&1\end{pmatrix}
\]

on the additive four-state module `p_2/2p_2`.

Under the explicit `F_2`-linear identification

\[
f_1\mapsto 1,\qquad f_2\mapsto \omega^2,
\]

this matrix becomes the Frobenius map on the additive group of `F_4`. Thus

\[
\boxed{\psi\,\bar g_{12}\,\psi^{-1}=\operatorname{Fr}}
\]

as an `F_2`-linear action.

This is **not** the same as reducing multiplication by the Pell unit `lambda=2+sqrt(3)` directly modulo the cyclotomic prime `P_2`. In the residue field,

\[
\sqrt3\equiv -1\equiv 1\pmod{\mathfrak P_2},
\qquad
2\equiv0,
\]

so

\[
\lambda=2+\sqrt3\equiv1\pmod{\mathfrak P_2}.
\]

Therefore literal residue-field multiplication by `lambda` is the identity, not Frobenius.

The publication-safe statement is:

> the mod-2 coordinate reduction of the Pell return on the ramified ideal, transported through the compatible additive `F_2`-linear identification with `F_4`, is Frobenius.

By contrast, multiplication by `zeta_12` does reduce literally on `O_K/P_2` to multiplication by `omega` of order 3.

This distinction strengthens the existing ring guardrail and prevents two different reduction procedures from being conflated.

## 3. [D] The finite `S_3` compatibility survives the correction

The correction above does not destroy the finite group result. On the common additive `F_2^2` carrier after the explicit linear identification,

\[
M_\omega=\begin{pmatrix}0&1\\1&1\end{pmatrix},
\qquad
\operatorname{Fr}=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\]

and

\[
\operatorname{Fr}M_\omega\operatorname{Fr}^{-1}=M_\omega^{-1}.
\]

Hence

\[
\langle M_\omega,\operatorname{Fr}\rangle=GL_2(\F_2)\cong S_3.
\]

The point is categorical: the order-3 map is a literal residue-field multiplication, while the order-2 Frobenius is the transported mod-2 Pell matrix action.

## 4. [Audit] Distinguish ideal-lattice coordinates from factor-cone coordinates

v0.3.3 uses `(x,y)` first as coefficients in

\[
\alpha=xf_1+yf_2
\]

and immediately afterward reuses `(x,y)` for Paper-A factor coordinates with

\[
X=(x-y)/2,\quad T=(x+y)/2,\quad Y^2=xy.
\]

These are different carriers. The shared letters make the phrase "the same return" look like literal coordinate equality when it is a representation correspondence through the common Lorentz structure.

Recommended repair for v0.3.4:

- use `(m,n)` for coefficients of the ramified ideal basis;
- reserve `(x,y)` for Paper-A factor/null coordinates;
- write `q_{12}(m,n)=2m^2-2mn-n^2` and `(U,V)=(2m-n,sqrt(3)n)`;
- then introduce the factor-cone representation separately.

This is a notation correction, not a change to either representation.

## 5. [Audit] Synchronize the principal paper with Paper A v2.4's two-sided cone

Paper A v2.4 uses

\[
Y^2=xy,
\qquad
Y=\pm\sqrt{xy},
\]

and explicitly separates factor exchange `X -> -X` from cone-side reflection `Y -> -Y`.

v0.3.3 still introduces the factor cone by writing only

\[
Y=\sqrt{xy}.
\]

The principal paper should instead use the two-sided equation `Y^2=xy` and, when a particular positive lift is needed for rapidity or a plotted label, say so explicitly.

The mod-12 unit shell should therefore be written

\[
Y_r=\pm\sqrt r
\]

for the full cone, with `+sqrt(r)` only as an upper-lift label when desired.

## 6. [Audit] Row/column naming should match Paper A v2.4

Paper A v2.4 fixes the convention

\[
x=u\quad\Longrightarrow\quad Y^2=u^2-2uX,
\]

with vertex `(u/2,0)`, and

\[
y=u\quad\Longrightarrow\quad Y^2=u^2+2uX,
\]

with vertex `(-u/2,0)`.

v0.3.3 calls the `+2uX` branch the row parabola. The tangency and null-ray equations are still correct, but the row/column names are reversed relative to the current authoritative Paper A.

v0.3.4 should adopt the Paper-A convention so the foundation chain uses one vocabulary.

## 7. [Audit] The `n=11` geometric specialization is also two-sided

For the two factor pairs `(11,1)` and `(1,11)`, the full Paper-A cone has four lifted points:

\[
X=\pm5,
\qquad
Y=\pm\sqrt{11},
\qquad
T=6.
\]

v0.3.3 writes only `(X,Y,T)=(\pm5,\sqrt{11},6)`. This is correct for the upper lift but no longer represents the full v2.4 geometry.

The revised text and figure caption should say that the displayed upper points have `Y=+sqrt(11)` while the reflected lower lift is also part of the cone.

## 8. [D] Paper B and Paper C do not force new principal-paper power-map claims

The principal paper does not rely on Paper B's old universal/canonical power-map language and does not import Paper C's quantum realization claims into the discriminant-12 theorem. Therefore the v13.213--v13.217 corrections do not invalidate the principal theorem.

This is an important dependency result: the principal algebraic chain remains independent of the power-map hierarchy, the scoped `B_X` question, and the quantum revival-period refinements.

## 9. [D] Null-diamond bridge remains compatible

The current null-diamond v2.1 corrections do not alter the principal paper's discriminant-12 algebra. The shared `SU(1,1)` convention and transition-vertex guardrails matter downstream in oscillator interpretations, but are not premises of the principal theorem.

No null-diamond theorem needs to be imported into the principal paper for v0.3.4.

## 10. [D] `n=11` arithmetic specialization remains valid

The calculations

\[
N_{F/\Q}(1+2\sqrt3)=-11,
\]

\[
(1+\sqrt3)(1+2\sqrt3)=7+3\sqrt3
\]

with total positivity, and hence

\[
[\mathfrak p_{11}]=[\mathfrak p_2]
\]

in the narrow class group remain valid.

Likewise the identification of the nontrivial element of `Gal(K_12/F)` with the cyclotomic automorphism `T_{11}` / complex conjugation remains publication-safe, provided the text continues to say that `T_{11} <-> J` is a representation correspondence rather than literal equality.

## 11. [Pub] Version and workflow consequence

Because the finite-reduction clarification changes theorem/abstract wording and the Paper-A synchronization changes geometric notation, v0.3.3 should remain a historical publication snapshot.

The corrected source should be created as

`papers/Discriminant_12_Return_v0.3.4.tex`.

When that source is promoted, the CI invariant requires the same change set to update:

- `papers/build_discriminant12_v0.3.3.sh` -> a v0.3.4 build entry point;
- `.github/workflows/build-discriminant12-paper.yml` -> v0.3.4 source/build/output paths;
- project README active mapping;
- any publication-status inventory or ledger references.

No figure generator rename is required by this audit.

## Final classification

- [D] Centered Cayley / discriminant-12 algebra: PASS.
- [D] Ramified ideal and cyclotomic integral carrier: PASS.
- [D] `F_4`, trace/XOR, `S_3`, `A_4`, `S_4` calculations: PASS after carrier clarification.
- [Audit] "reduced Pell return is Frobenius" must be replaced by the transported `F_2`-linear statement; literal residue multiplication by `lambda` is identity.
- [Audit] ideal coefficients and factor coordinates must use distinct notation.
- [Audit] principal cone notation must synchronize to Paper A v2.4's two-sided `Y^2=xy` geometry.
- [Audit] row/column naming must match Paper A v2.4.
- [Audit] `n=11` geometry must acknowledge both cone lifts.
- [Pub] a v0.3.4 revision is warranted before further principal-paper expansion.

**Principal v0.3.3 downstream dependency audit: COMPLETE.**