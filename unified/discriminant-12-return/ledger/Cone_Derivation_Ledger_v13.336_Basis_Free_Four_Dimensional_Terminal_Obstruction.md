# Cone Derivation Ledger v13.336 — Basis-Free Four-Dimensional Terminal Obstruction

## Main idea

Once the exact 10x10 effective core F is enclosed in operator norm around a numerical approximation Fhat,

\[
\|F-\widehat F\|\le\eta,
\]

Weyl's inequality gives

\[
|\lambda_j(F)-\lambda_j(\widehat F)|\le\eta.
\]

The numerically resolved fifth eigenvalue at the N=155 effective scale is

\[
\widehat\lambda_5\approx4.33\times10^{-8}.
\]

Therefore any verified effective-core enclosure with

\[
\boxed{\eta<4.33\times10^{-8}}
\]

certifies

\[
\lambda_5(F)>0.
\]

Since the eigenvalues are ordered increasingly, this proves that at most four eigenvalues of F can be nonpositive.

## Consequence

The terminal four-dimensional obstruction can be certified **without constructing or certifying a particular six-dimensional stiff basis**.

A comfortable design target is

\[
\boxed{\eta\le2\times10^{-8}},
\]

which would leave a fifth-eigenvalue margin above roughly \(2\times10^{-8}\).

This substantially relaxes the first rigorous effective-core target compared with trying to resolve any of the tiny bottom four levels.

## Interaction with v13.335

Using the residual-certified Schur solve,

\[
\|CB^{-1}C^T-CX\|\le\frac{\|C\|}{\gamma}\|R\|,
\]

with amplification about 3.2.  If the entire \(2\times10^{-8}\) operator budget were allocated to the solve residual alone, one would only need residual norm of order

\[
\sim6\times10^{-9}.
\]

In practice the budget will be shared among core-entry, coupling-entry, and solve-residual enclosures, but this shows that the first rigorous 4D-obstruction milestone is numerically modest.

## New proof milestone

A rigorous intermediate theorem can now be stated in a basis-free way:

> The finite buffer is positive and the 10x10 effective core has at most four nonpositive eigenvalues.

Together with the analytic tail coercivity, this would turn the present numerical four-dimensional diagnosis into a certified finite-dimensional obstruction statement.

## Guardrails

The value \(4.33\times10^{-8}\) is still non-interval numerical targeting data.  The theorem requires a verified operator enclosure of F and a verified lower comparison to the numerical fifth eigenvalue.  No exact zero, full positivity, lambda_1=0, RH, or GRH conclusion follows.
