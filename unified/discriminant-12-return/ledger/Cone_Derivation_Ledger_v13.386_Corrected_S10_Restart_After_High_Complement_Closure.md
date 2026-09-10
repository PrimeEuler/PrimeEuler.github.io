# Cone Derivation Ledger v13.386 — Corrected S10 Restart After High-Complement Closure

Date: 2026-09-10

Status labels: **[D]** exact derived, **[N-cert]** validated computational under stated arithmetic model, **[N]** numerical diagnostic, **[O]** open, **[Audit]** correction/limitation.

## 1. Restored premise

The corrected post-audit chain now establishes positivity of

\[
\mathcal D=\overline{\operatorname{span}}\{\psi_n:n\ge21,\ n\ \mathrm{odd}\}
\]

for the pole-free operator `A0` under the stated validated-computational model.

Use the rounded certified inputs

\[
A_{0,F}\succeq0.22I,\qquad
A_{0,T}\succeq4.6733I,\qquad
\|G_{FT}\|<1.00303,
\]

where `F=21..16001` odd and `T>=16003` odd.

Then

\[
\gamma_{\mathcal D}
:=0.22-\frac{1.00303^2}{4.6733}
>0.0047197.
\]

Therefore

\[
\boxed{A_{0,\mathcal D\mathcal D}\succeq\gamma_{\mathcal D}I>0}
\]

and

\[
\boxed{\|A_{0,\mathcal D\mathcal D}^{-1}\|<211.9.}
\]

This replaces the superseded pre-audit inverse bound `<116.7`.

## 2. Exact inertia reduction

Let

\[
C=\operatorname{span}\{\psi_1,\psi_3,\ldots,\psi_{19}\},
\qquad \dim C=10.
\]

Since the high block is strictly positive, exact block congruence yields

\[
\operatorname{inertia}(A_0)
=\operatorname{inertia}(S_{10})
 +\operatorname{inertia}(A_{0,\mathcal D\mathcal D}),
\]

with

\[
\boxed{
S_{10}
=A_{CC}-A_{C\mathcal D}
A_{\mathcal D\mathcal D}^{-1}
A_{\mathcal D C}.
}
\]

Hence every possible nonpositive direction of the pole-free even-sector operator lies in this ten-dimensional Schur complement.

## 3. Corrected solve-error target

For a point approximation

\[
X\approx A_{\mathcal D\mathcal D}^{-1}A_{\mathcal DC}
\]

with residual

\[
R=A_{\mathcal DC}-A_{\mathcal D\mathcal D}X,
\]

we have

\[
\|X-X_*\|\le\frac{\|R\|}{\gamma_{\mathcal D}}.
\]

Thus

\[
\|A_{C\mathcal D}(X-X_*)\|
\le
\frac{\|A_{C\mathcal D}\|}{\gamma_{\mathcal D}}\|R\|.
\]

A practical final Schur enclosure target remains

\[
\eta_{S10}<3\times10^{-9}.
\]

For a certified coupling bound `Cnorm=||A_CD||` this requires

\[
\boxed{
\|R\|<\frac{3\times10^{-9}\,\gamma_{\mathcal D}}{Cnorm}.
}
\]

For `Cnorm=1`,

\[
\|R\|<1.42\times10^{-11}.
\]

## 4. What is not inherited from v13.366

**[Audit]** The old finite-model diagnostic placing the fifth ordered Schur eigenvalue near `4.3e-8` is not carried forward as evidence.  It was produced before the archimedean formula correction and must be recomputed on the intended operator.

Likewise, no old low-mode Schur matrix entries should be reused unless they are independently shown not to involve the corrected arch off-diagonal term.

## 5. Next computation

The next proof object is a corrected ten-column solve for

\[
A_{\mathcal D\mathcal D}X=A_{\mathcal DC}
\]

using the centered rank-four representation on the finite high block plus certified tail elimination.  The output should include:

1. a certified bound for `||A_CD||`;
2. ten solve residual norms;
3. the corrected `10x10` Schur matrix;
4. interval/eigenvalue enclosures at scale below `3e-9`;
5. inertia only after the eigenvalue intervals are separated from zero.

No exact-zero, RH, or GRH conclusion follows from this checkpoint.
