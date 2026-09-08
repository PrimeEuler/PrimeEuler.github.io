# Cone Derivation Ledger v13.331 — Pole-Free Buffer Gap and Single-Integral Certification Target

## Structural simplification

The pole term in the even-v sector is exactly positive semidefinite:

\[
P_{pole}=2cc^T\ge0.
\]

Therefore it does not need to be enclosed at all when proving a lower bound for the finite buffer.  It may simply be dropped.

For

\[
B_0=C_{cusp}+B_{prime}+K_{arch}
\]

on modes 21 through 153, a fresh numerical audit gives

\[
\lambda_{min}(B_0)\approx0.238481965.
\]

Adding the pole raises the numerical gap to about 0.272014760, but the smaller pole-free value is already very comfortable.

## Certification consequence

The finite-buffer proof now requires rigorous treatment of only three pieces:

1. **cusp:** explicit Si/Ci formulas;
2. **prime:** finite exact five-shift formulas;
3. **arch:**
   \[
   (K_{arch})_{mn}=-\int_0^2 h(t)S_{mn}(t)\,dt.
   \]

The first two are finite special-function/algebraic evaluations.  The only genuine continuous enclosure problem is the single smooth one-dimensional archimedean integral.

Since h(t)=r''(t) has a removable value h(0)=1/4 and is analytic on the real interval after that filling, while S_mn(t) is entire, rigorous interval quadrature is straightforward in principle.

Using the pole-free numerical gap, even the crude entrywise perturbation condition

\[
67\epsilon<\frac12(0.23848)
\]

allows

\[
\epsilon\lesssim1.78\times10^{-3}.
\]

So a rigorous arch entry enclosure at merely 1e-4 accuracy would leave more than an order of magnitude of safety.

## Why this is substantial

The buffer-certification problem has reduced from a 67x67 high-precision spectral problem to a **coarse enclosure of one family of smooth 1-D integrals**.  The positive pole term can be discarded, and no tiny-scale arithmetic is needed until after the buffer Schur complement is formed.

## Next target

Move to the Schur correction itself.  Determine how accurately Delta=A_CB A_BB^{-1}A_BC must be enclosed to resolve the 10x10 effective-core inertia, and identify whether the first three unresolved directions can be isolated as a 3x3 terminal Schur block.

## Guardrail

The 0.23848 pole-free gap is currently a floating diagnostic, not yet an interval-certified lower bound.  It is used to design the rigorous enclosure target only.  No full positivity/RH conclusion follows.