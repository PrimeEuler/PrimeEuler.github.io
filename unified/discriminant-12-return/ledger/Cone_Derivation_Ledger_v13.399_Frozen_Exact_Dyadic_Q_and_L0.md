# Cone Derivation Ledger v13.399 — Frozen Exact-Dyadic Q and L0

Date: 2026-09-11

Status labels: **[D]** exact derived, **[N]** numerical, **[N-cert]** validated computational, **[O]** open.

## 1. Purpose

Remove the last moving-coordinate ambiguity from the terminal six-direction verifier by freezing the M=3999 midpoint basis and preconditioner as exact dyadic inputs.

The repository now contains

`research-notes/suzuki_M3999_frozen_dyadic_Q_L0.py`

with every entry stored as a hexadecimal binary64 literal.

A hexadecimal binary64 literal represents its underlying dyadic rational exactly. The final checker is therefore instructed to treat these entries as fixed mathematical constants, not values to be regenerated from a numerical eigensolver.

## 2. Frozen six-dimensional subspace

Let

\[
Q\in\mathbb R^{10\times6}
\]

be the stored dyadic matrix.

The first six rows form a 6x6 dyadic minor. Exact rational Bareiss/Gaussian elimination gives a nonzero determinant. Its ordinary decimal diagnostic is

\[
\boxed{1.2524505480946447\times10^{-14}}.
\]

Therefore

\[
\boxed{\operatorname{rank}Q=6}
\]

is an exact rational statement about the frozen verifier input.

The ordinary floating Gram diagnostic is

\[
\|Q^TQ-I\|_2\approx1.29\times10^{-15},
\]

but this near-orthogonality is not needed for the proof; full rank is enough.

## 3. Frozen coordinate preconditioner

Let

\[
L_0\in\mathbb R^{6\times6}
\]

be the stored lower-triangular dyadic matrix.

All six diagonal entries are nonzero exact dyadics, hence

\[
\boxed{L_0\text{ is invertible}}
\]

exactly.

No claim that \(L_0\) is an exact Cholesky factor of an exact operator is required. It is only a fixed invertible coordinate transformation.

## 4. Consequence for the verifier

The final checker now has immutable inputs \(Q,L_0\). It needs only to certify the exact source-faithful operator inequalities

\[
C=L_0^{-1}(Q^TS_FQ)L_0^{-T}\succeq0.9958I,
\]

and

\[
H=L_0^{-1}(Q^TR^*RQ)L_0^{-T}\prec0.18025I.
\]

Together with

\[
\delta_T>0.18225976374175623,
\]

these imply

\[
H<\delta_TC.
\]

Hence the exact infinite low-core Schur complement is positive on the fixed six-dimensional subspace \(\operatorname{ran}Q\).

The resulting theorem-level conclusion, once the outward replay passes, is only

\[
\operatorname{ind}_{\le0}(S_{10})\le4.
\]

The remaining four directions stay unresolved.

## 5. Guardrails

This checkpoint freezes verifier data but does not itself execute the outward operator replay. It does not assert exact kernels or determine the signs of the remaining four directions. No RH, GRH, or exact-zero conclusion follows.
