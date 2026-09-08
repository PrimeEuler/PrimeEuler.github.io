# Cone Derivation Ledger v13.343 — Compact Residual Certificate and Rational Six-Dimensional Positive Subspace

The finite certification can be reduced further; interval eigensolvers are unnecessary.

## Buffer positivity

Let B be the rigorous 67x67 interval buffer matrix and L a fixed rational/rounded numerical Cholesky candidate.  Set
\[
E=B-LL^T.
\]
Let Y approximate L^{-1} and suppose
\[
\rho=\|I-YL\|<1.
\]
Then
\[
\|L^{-1}\|\le\frac{\|Y\|}{1-\rho},
\]
so
\[
LL^T\succeq\left(\frac{1-\rho}{\|Y\|}\right)^2I.
\]
Therefore B>0 follows from the single residual inequality
\[
\|E\|<\left(\frac{1-\rho}{\|Y\|}\right)^2.
\]

## Effective-core obstruction

Let F be the rigorous 10x10 effective-core interval matrix.  Choose any fixed rational 10x6 matrix V.  If
\[
V^TFV\succ0,
\]
then V automatically has rank six and span(V) is a six-dimensional positive subspace.  Hence the nonpositive index of F is at most four.

A 12-decimal rationalized candidate V has nominal projected eigenvalues
\[
4.32680308\times10^{-8},\ 2.55123446\times10^{-4},\ 0.831001272,\ 1.70560298,\ 2.01774663,\ 2.35191099.
\]
The smallest projected scale is unchanged from the fifth nominal effective level, while the remaining five are much stiffer.

## End-to-end design budget

With a full finite-matrix operator enclosure about 7e-11, γ>=0.15, ||C||<=0.8, and verified solve residual ||R||<=8e-10, the current Schur-error design is about 7.1e-9.  This is well below the ~4.3e-8 projected positive scale.

Thus the next concrete milestone is no longer conceptual: instantiate the rational interval matrix, compute fixed rational L,Y,X,V data, and verify a short list of norm/residual inequalities.

Guardrail: none of those inequalities has yet been instantiated as a full machine-checked certificate in this ledger.  No positivity theorem for the infinite operator, exact zero, λ1=0, RH, or GRH conclusion follows.