# Cone Derivation Ledger v13.395

## Fixed-Preconditioner Six-Direction Error Budget

### Status
**[Proof-design / certification budget].** No completed validated replay yet. No exact-zero, final inertia, RH, or GRH claim.

## 1. Motivation

v13.394 proposed preconditioning the terminal six-dimensional pencil by a Cholesky factor of the finite positive block. For interval work, however, repeatedly factoring an interval matrix is unnecessary and can introduce avoidable dependency inflation.

Instead freeze a high-precision midpoint factor \(L_0\), stored as exact dyadic verifier input, and work entirely in its coordinates.

For the exact six-dimensional matrices

\[
B=Q^TS_FQ,
\qquad
G=R_Q^*R_Q,
\]

define

\[
C=L_0^{-1}BL_0^{-T},
\qquad
H=L_0^{-1}GL_0^{-T}.
\]

Then

\[
G<\delta_TB
\iff
H<\delta_TC.
\]

This is the preferred terminal formulation.

## 2. Available source-faithful margin

The reinstated Schur-tail floor is

\[
\delta_T>0.18225976374175623.
\]

The v13.393 hybrid midpoint generalized residual upper target is

\[
h_{\rm mid}=0.17910434985544155.
\]

Thus the raw normalized-coordinate slack is

\[
\boxed{
\delta_T-h_{\rm mid}=0.003155413886314684
}.
\]

Relative to \(\delta_T\), this is

\[
\boxed{1.73127289399189\%}.
\]

## 3. Split the validation budget

Choose the finite-Schur metric target

\[
\boxed{C\succeq0.995I}.
\]

This spends only one half percent on the finite \(B\) side.

Then it suffices to prove

\[
\lambda_{\max}(H)<0.995\,\delta_T.
\]

Numerically,

\[
0.995\,\delta_T
=0.18134846492304744\ldots
\]

so the entire residual-Gram validation may move upward from the midpoint by

\[
\boxed{
0.18134846492304744-0.17910434985544155
>2.2441\times10^{-3}.
}
\]

This is the working outward-error allowance for the residual side.

## 4. Why the metric matters

The smallest finite candidate-positive Schur direction is only order \(4\times10^{-8}\). Therefore a raw Euclidean operator bound on \(B-B_0\) is poorly scaled and can appear artificially demanding.

The correct object to certify is directly

\[
L_0^{-1}BL_0^{-T},
\]

because that measures perturbations relative to the natural finite-Schur geometry. A 0.5% metric enclosure is compatible with the tiny fifth raw scale while still being a moderate normalized verification problem.

## 5. Terminal certificate conditions

A successful fixed-preconditioner replay need only establish

\[
\boxed{C\succeq0.995I}
\]

and

\[
\boxed{\lambda_{\max}(H)<0.1813484649}.
\]

These two inequalities imply

\[
H<\delta_TC,
\]

hence positivity of the six candidate-positive low-core directions after coupling to the full high complement.

## 6. Remaining finite obstruction

Even after the six-dimensional sector is certified, the first four numerical near-zero directions remain a separate terminal \(4\times4\) problem. Nothing in this checkpoint identifies them as exact kernels or assigns their signs.

## 7. Guardrails

- v13.395 is a verifier budget, not a completed validated computation.
- No exact-zero or final inertia statement is made.
- No RH or GRH conclusion follows.
