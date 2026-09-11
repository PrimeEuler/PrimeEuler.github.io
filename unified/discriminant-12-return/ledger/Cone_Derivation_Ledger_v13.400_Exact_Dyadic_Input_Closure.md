# Cone Derivation Ledger v13.400 — Exact Dyadic Verifier-Input Closure

Date: 2026-09-11

Status labels: **[D]** exact derived, **[N]** numerical, **[N-cert]** validated computational, **[O]** open.

## 1. Frozen-input file is now self-verifying

The terminal verifier input file

`research-notes/suzuki_M3999_frozen_dyadic_Q_L0.py`

has been upgraded so that it checks the rank of the frozen six-dimensional basis using exact rational arithmetic rather than a floating diagnostic.

Each hexadecimal binary64 literal is converted to its exact dyadic rational by `as_integer_ratio`, and the determinant of the first 6x6 row minor is evaluated with exact Fraction/Bareiss elimination.

## 2. Exact nonzero minor

The exact determinant of the first-six-row minor of the frozen \(Q\) is

\[
\frac{
1795308499156921328504675698957198911069798836146299290831861630469317641019312377789718059
}{
143343663499379469475676305956380433799785311823017570233599302461682679755530300504376159569382855409664
}.
\]

The numerator is nonzero. Therefore

\[
\boxed{\operatorname{rank}Q=6}
\]

is proved exactly for the frozen verifier input.

Its decimal value is only a readability aid:

\[
\det Q_{1:6,1:6}\approx1.2524505480946447\times10^{-14}.
\]

The small size of this particular coordinate minor is irrelevant once nonzeroness is checked exactly.

## 3. Exact invertibility of L0

The stored \(L_0\) is lower triangular and all six diagonal entries are nonzero exact dyadics. Hence

\[
\boxed{L_0\text{ is invertible}}
\]

exactly.

No interval eigenvector or Cholesky argument remains in the proof architecture.

## 4. What remains

The terminal six-dimensional verifier now has fully fixed exact coordinate data. Its only unresolved tasks are operator enclosures:

\[
C=L_0^{-1}(Q^TS_FQ)L_0^{-T}\succeq0.9958I,
\]

and

\[
H=L_0^{-1}(Q^TR^*RQ)L_0^{-T}\prec0.18025I.
\]

Together with the already certified source-faithful tail floor

\[
\delta_T>0.18225976374175623,
\]

these imply

\[
H<\delta_TC,
\]

so the exact infinite low-core Schur complement is positive on the exact six-dimensional subspace \(\operatorname{ran}Q\).

Once the outward replay certifies those two inequalities, the theorem-level finite-index conclusion would be

\[
\boxed{\operatorname{ind}_{\le0}(S_{10})\le4}.
\]

## 5. Guardrails

The operator replay has not yet been executed, so the index bound is not promoted as proved in this checkpoint. The remaining four directions are unresolved and are not called exact kernels. No RH, GRH, or exact-zero conclusion follows.
