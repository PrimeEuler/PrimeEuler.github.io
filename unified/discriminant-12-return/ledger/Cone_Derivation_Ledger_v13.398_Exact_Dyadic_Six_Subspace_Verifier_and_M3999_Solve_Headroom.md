# Cone Derivation Ledger v13.398 — Exact-Dyadic Six-Subspace Verifier and M3999 Solve Headroom

Date: 2026-09-11

Status labels: **[D]** exact derived, **[N]** numerical, **[N-cert]** validated computational, **[O]** open.

## 1. Structural simplification

The terminal six-direction verifier does **not** need to certify that the chosen basis vectors are exact eigenvectors of a midpoint Schur matrix.

Freeze a rounded high-precision matrix

\[
Q\in\mathbb R^{10\times6}
\]

as exact dyadic verifier input. It is enough that \(Q\) have rank six.

Likewise freeze an invertible

\[
L_0\in\mathbb R^{6\times6}
\]

as exact dyadic verifier input. It is only a coordinate preconditioner and need not be certified as the exact Cholesky factor of any exact matrix.

For the exact finite Schur matrix \(S_F\), define

\[
C=L_0^{-1}(Q^TS_FQ)L_0^{-T}.
\]

For the exact remote residual operator \(R\), define

\[
H=L_0^{-1}(Q^TR^*RQ)L_0^{-T}.
\]

If the checker proves

\[
C\succ0,
\qquad
H<\delta_TC,
\]

then the exact infinite Schur complement is positive on the six-dimensional subspace \(\operatorname{ran}Q\).

Therefore its positive index is at least six, hence its nonpositive index is at most four.

**[D]** No eigenvector enclosure is required for this conclusion.

## 2. Why this matters

The earlier verifier architecture treated midpoint eigendirections and the midpoint Cholesky factor as objects whose perturbations might need interval tracking. That is unnecessary.

The proof may instead regard \(Q\) and \(L_0\) as arbitrary fixed exact dyadic matrices selected for conditioning. All uncertainty is then pushed into the two exact normalized matrices \(C\) and \(H\), which are precisely the objects already budgeted in v13.396-v13.397.

This removes a potentially awkward eigenvector-conditioning problem near the tiny fifth finite-Schur level.

## 3. Fresh M=3999 midpoint solve residual

For

\[
F=\{21,23,\ldots,3999\},
\qquad
C=\{1,3,\ldots,19\},
\]

a fresh ordinary-double source-faithful solve of

\[
A_{FF}X=A_{FC}
\]

gives the residual

\[
R_F=A_{FC}-A_{FF}X.
\]

**[N]** The measured norms are

\[
\boxed{\|R_F\|_2\approx5.1902336852\times10^{-16}},
\]

\[
\|R_F\|_F\approx8.6118427325\times10^{-16},
\]

with maximum entry approximately

\[
2.2204460493\times10^{-16}.
\]

The v13.396 fail-closed target is

\[
\boxed{\|R_F\|<10^{-12}}.
\]

Thus the midpoint solve has more than

\[
\boxed{1900\times}
\]

headroom relative to the verifier target.

This strongly suggests that an outward high-precision replay of the finite solve is a routine certification task rather than a conditioning bottleneck.

## 4. Terminal theorem shape if the checker passes

The current terminal target is now:

1. freeze exact dyadic \(Q\) of rank six;
2. freeze exact dyadic invertible \(L_0\);
3. certify the finite solve residual below \(10^{-12}\);
4. certify
   \[
   C\succeq0.9958I;
   \]
5. certify
   \[
   H\prec0.18025I;
   \]
6. combine with
   \[
   \delta_T>0.1822597637.
   \]

Then

\[
H<\delta_TC
\]

and the exact infinite low-core Schur complement has a six-dimensional positive subspace.

Therefore

\[
\boxed{\operatorname{ind}_{\le0}(S_{10})\le4}
\]

would follow under the completed validated-computational replay.

## 5. Guardrails

This checkpoint does **not** yet claim the index bound as proved because the outward replay of \(C\) and \(H\) remains to be executed.

The remaining four directions are unresolved: they may be positive, zero, or negative within the present evidence. No exact kernel is asserted. No RH, GRH, or exact-zero conclusion follows.
