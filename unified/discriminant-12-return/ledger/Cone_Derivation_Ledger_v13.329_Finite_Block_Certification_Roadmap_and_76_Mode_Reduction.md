# Cone Derivation Ledger v13.329 — Finite-Block Certification Roadmap and 76-Mode Reduction

## Status

This checkpoint changes the main Suzuki task from remote-tail asymptotics to finite-block certification.

The v13.328 six-dimensional protected line has a conservative adverse-tail crossover at odd mode N=155, essentially the first coercive tail scale.  Continuing to sharpen remote-tail constants is therefore low leverage.

## Finite reduction

Use the odd Dirichlet decomposition

\[
C=\{1,3,\ldots,19\},\qquad
B=\{21,23,\ldots,153\},\qquad
T=\{155,157,\ldots\}.
\]

Thus

- core dimension = 10;
- finite buffer dimension = 67;
- finite core+buffer dimension = 77 (not 76; explicit count check retained as a guardrail);
- the analytic remote tail begins at N=155.

The exact matrix anatomy is already available:

1. cusp entries from the Si/Ci formulas of v13.301;
2. prime entries from the exact joint-prime factorization of v13.315;
3. smooth archimedean entries from a one-dimensional integral against the exact shift matrix element;
4. pole contribution as a positive rank-one matrix.

## Certification architecture

Do not attempt to certify signs by diagonalizing a floating matrix whose first effective eigenvalues are at 1e-17 or below.  Instead certify the block algebra itself.

For the finite block

\[
A_{C\oplus B}=\begin{pmatrix}A_{CC}&A_{CB}\\A_{BC}&A_{BB}\end{pmatrix},
\]

perform:

1. outward-rounded entry enclosures;
2. interval LDL^T certification of A_BB>0;
3. interval solve for A_BB^{-1}A_BC;
4. interval Schur complement
   \[
   F=A_{CC}-A_{CB}A_{BB}^{-1}A_{BC};
   \]
5. interval inertia / pivot certification of the resulting 10x10 F.

The reason this is promising is structural: the buffer itself is not close to singular.  The earlier finite-section audit gave a buffer gap near 0.267 at M=399.  The severe cancellation occurs only after the Schur correction reaches the 10-dimensional low core.

Therefore numerical effort should be concentrated on accurately enclosing the 10x10 effective core, rather than globally increasing precision on hundreds of modes.

## Why LDL/inertia rather than eigenvalues

The unresolved first three effective eigenvalues are below the trustworthy sign scale of the hybrid assembly.  Eigenvalue evaluation asks for the final answer after all cancellation has occurred.  Block LDL^T exposes the cancellation sequentially and allows each pivot to be enclosed directly.

A rigorous result could therefore take the form:

- all buffer pivots positive;
- a specified number of effective-core pivots have certified sign;
- remaining pivot interval(s) contain zero and identify the exact unresolved dimension.

Even partial certification would materially sharpen the problem by replacing the current vague three-dimensional ultra-near-null subspace with an exact inertia enclosure.

## Guardrails

- v13.328 N=155 is based on non-interval channel/effective-basis data and an analytic tail-gap framework; it is not itself a positivity proof.
- Tiny effective eigenvalue signs remain unresolved.
- No exact zero mode, lambda_1=0, RH, or GRH conclusion follows.

## Next target

Build an interval-capable 77x77 finite assembly at N=155, but exploit the 67x67 positive buffer so that only the final 10x10 Schur complement needs extreme precision.  First objective: certify the buffer inertia and quantify a rigorous enclosure radius for the Schur correction.