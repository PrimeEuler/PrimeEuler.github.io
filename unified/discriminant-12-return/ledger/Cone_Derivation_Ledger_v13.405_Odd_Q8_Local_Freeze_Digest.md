# Cone Derivation Ledger v13.405 — Odd Q8 Exact Local Freeze Digest

Date: 2026-09-13

Status labels: **[D]** exact derived, **[N]** numerical, **[O]** open.

## 1. Context

Continue v13.404's odd-sector index-2 certification route.  The candidate-positive subspace is the eight-dimensional span corresponding to midpoint odd-sector Schur directions 3 through 10 for

\[
C=\{2,4,\ldots,20\},\qquad D_{800}=\{22,24,\ldots,800\}.
\]

The source-faithful midpoint spectrum reproduces v13.403, with third through tenth levels approximately

\[
1.7363\times10^{-10},
3.4729\times10^{-6},
8.4899\times10^{-3},
0.65154,
1.51336,
1.81625,
2.25428,
2.54666.
\]

## 2. Exact dyadic freeze

The 10x8 basis Q8 and 8x8 lower-triangular preconditioner L0 were frozen as exact IEEE-754 binary64 dyadics.  Treating each hexadecimal literal as its exact rational value, the determinant of the first eight rows of Q8 is

\[
\frac{-10946282287692322734862838818994592553456000625805095770280762736893456055317711927485881030481401503384380297001630830384147693083}{46517678354918840995156723704832290198633047083988355858015372747560914439257467092876227245680868195888801382801035387746214504231337984}.
\]

Hence

\[
\boxed{\operatorname{rank}Q_8=8}
\]

exactly.  The decimal value of this exact minor is approximately

\[
-2.353144583909538\times10^{-7}.
\]

The frozen L0 is lower triangular with eight nonzero exact-dyadic diagonal entries, so it is exactly invertible.

## 3. Payload digests

The canonical compact JSON serialization of the exact hexadecimal Q8 rows has SHA-256

`a97a93e342aee50efea6c588c0be44221e4906f1a5124f32370cd9604eb98d30`.

The corresponding L0 serialization has SHA-256

`6b29e1c347faaeec71b854ec508be15749aa84404ffe51177f0e73548d666870`.

These digests identify the locally frozen exact data used in the continuing audit.

## 4. Repository packaging note

An attempted direct connector upload of the full hexadecimal payload was blocked by the connector payload/safety gate.  The incomplete placeholder artifacts were removed immediately and are not part of the proof record.  Until the complete exact payload is successfully committed or otherwise reproduced from an audited artifact, this checkpoint does **not** promote the odd-sector index theorem.

## 5. Next verifier targets

The remaining odd-sector certification targets from v13.404 are:

\[
A_{FF}\succeq0.53I,
\qquad
A_{TT}\succeq2.58I,
\qquad
\|A_{FT}\|<1.013,
\]

which imply a conservative effective tail floor

\[
\delta_{\rm odd}>0.64.
\]

The eight-direction normalized residual-Gram diagnostic remains far below this scale, near 0.225 after the analytic infinite-tail charge.

## 6. Guardrails

- Exact rank(Q8)=8 is established for the locally frozen dyadic payload identified above.
- The full exact payload is not yet stored in the repository.
- No odd-sector inertia theorem is promoted in this checkpoint.
- The first two tiny odd-sector directions are not called exact kernels.
- No RH, GRH, or exact-zero conclusion follows.
