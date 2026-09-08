# Cone Derivation Ledger v13.344 — Nominal Residual Certificate and Seven-Nanounit Effective-Core Budget

## First complete midpoint certificate prototype

At the N=155 split

\[
C=\{1,3,\ldots,19\},\qquad B=\{21,23,\ldots,153\},
\]

the current finite matrix assembly gives

\[
\lambda_{\min}(B)\approx0.2720147601690829.
\]

For the numerical Cholesky factor L,

\[
\|B-LL^T\|_2\approx8.95\times10^{-16}.
\]

With Y=L^{-1},

\[
\|I-YL\|_2\approx1.98\times10^{-16},
\]

which reconstructs the nominal lower bound

\[
B\succeq0.2720147601690794 I.
\]

For the Schur solve X=B^{-1}C^T,

\[
\|C^T-BX\|_2\approx3.36\times10^{-16}.
\]

Thus the numerical linear algebra is negligible compared with the interval-entry budget.

## Fixed rational six-dimensional positive-subspace candidate

Using the fixed rational 10x6 matrix V from the v13.343 chain,

\[
\operatorname{spec}(V^T F V)\approx
\{4.32640081\times10^{-8},
2.55123442\times10^{-4},
0.831001270,
1.70560298,
2.01774663,
2.35191099\}.
\]

Also

\[
\|V\|_2\approx1.000000000760053.
\]

Therefore any rigorous effective-core enclosure

\[
\|F-\widehat F\|\le7.1\times10^{-9}
\]

would perturb the projected matrix by essentially the same amount and leave a first projected positive margin of about 3.6e-8.

This certifies the design principle

\[
V^T F V\succ0
\quad\Longrightarrow\quad
\operatorname{ind}_{\le0}(F)\le4.
\]

## Direct interval-width prototype for prime and pole pieces

At 50 decimal-digit interval precision, direct interval evaluation across all finite prime entries gives maximum entry radius

\[
2.01\times10^{-48},
\]

while the pole-vector interval radius is below

\[
9.4\times10^{-51}.
\]

These are not the final rational proof intervals; they show that the prime and pole transcendental-evaluation errors are negligible by dozens of orders of magnitude compared with the finite-matrix target.  The final proof should still use the rational-series closure from v13.342.

## Consolidated Schur budget

Use conservative design values

\[
\delta_A=\delta_B=\delta_C=7\times10^{-11},
\qquad
\gamma=0.15,
\qquad
\|C\|\le0.8.
\]

The block-assembly perturbation formula gives

\[
\delta_{\rm block}\approx2.80778\times10^{-9}.
\]

With verified solve residual target

\[
\|R\|\le8\times10^{-10},
\]

the residual contribution is

\[
\delta_{\rm solve}\le\frac{0.8}{0.15}(8\times10^{-10})
\approx4.26667\times10^{-9}.
\]

Hence

\[
\boxed{
\eta_F\approx7.07445\times10^{-9}.
}
\]

Against the nominal rational-subspace first level

\[
4.3264\times10^{-8},
\]

this leaves a margin of approximately

\[
\boxed{3.62\times10^{-8}}.
\]

So the finite obstruction certificate has roughly a factor-six safety margin at the current design tolerances.

## What remains

The remaining work is no longer conceptual.  It is to instantiate the rational interval matrix and verify the finite list of inequalities:

1. coarse rational enclosure proving B>0;
2. fine rational midpoint matrix plus certified residual for BX=C^T;
3. operator enclosure for the 10x10 Schur core below 7.1e-9;
4. positive definiteness of the 6x6 rational projected matrix V^T F V.

No exact zero, positivity of the full Suzuki operator, lambda_1=0, RH, or GRH conclusion follows yet.