# Cone Derivation Ledger v13.347 — Coarse Rational Witness Certificate and 0.176 Full-Infinite Margin

## Main simplification

The fixed rational \(77\times6\) witness from v13.345 has so much numerical slack that the final interval proof should not attempt to preserve the midpoint values accurately.

It is enough to certify the rounded inequalities

\[
\boxed{W^TA_{0,FF}W\succeq0.18\,I_6}
\]

and

\[
\boxed{\|W^TA_{0,F,[155,3001]}\|_F<0.009}.
\]

Combine these with the robust analytic targets

\[
\boxed{\beta_{n\ge3003}<1.5\times10^{-4}}
\]

and

\[
\boxed{\alpha_{155}>0.0249}.
\]

The last inequality uses the deliberately weakened but interval-friendly prime target \(\|B_{\rm prime}\|<2.05\) from v13.346.

## Full-tail consequence

The total coupling is then bounded by

\[
\beta_{\rm total}<0.009+0.00015=0.00915.
\]

Hence the infinite-tail Schur correction on the six-plane is at most

\[
\frac{0.00915^2}{0.0249}<3.37\times10^{-3}.
\]

Therefore the pole-free full infinite quadratic form retains the six-dimensional lower bound

\[
0.18-\frac{0.00915^2}{0.0249}
>
\boxed{0.1766}.
\]

Since the pole term is positive semidefinite, adding it back preserves this positive subspace.

## Why this matters computationally

The midpoint finite-tail Frobenius norm is

\[
8.730696686\times10^{-3}.
\]

The rounded target 0.009 leaves slack

\[
2.69303\times10^{-4}.
\]

There are \(6\times1424=8544\) projected coupling entries.  Even if every projected entry were independently enclosed with the same radius \(\varepsilon\), the Frobenius perturbation is at most \(\sqrt{8544}\,\varepsilon\).  Thus the target permits roughly

\[
\boxed{\varepsilon\approx2.9\times10^{-6}}
\]

per projected coupling entry.

This is extremely coarse compared with the available analytic formulas.

Likewise the midpoint finite protected minimum is about

\[
0.1874455915.
\]

To certify the rounded lower bound 0.18, a crude symmetric \(6\times6\) entrywise enclosure radius around

\[
\frac{0.1874455915-0.18}{6}
\approx
\boxed{1.24\times10^{-3}}
\]

would already suffice by the operator bound \(\|E\|_2\le6\max|E_{ij}|\).

Thus the final rational proof does not require delicate interval arithmetic.  The desired finite form and finite-tail coupling bounds tolerate errors many orders of magnitude larger than the natural rational-series enclosures developed in v13.339--343.

## Updated proof architecture

A minimal full-infinite certificate can now be organized around four finite/analytic checks:

1. **Prime tail gap:** interval-certify the finite k=16 Schur sweep below \(2.05^{16}\), giving \(\alpha_{155}>0.0249\).
2. **Finite witness positivity:** certify the fixed rational \(W\) satisfies \(W^TA_{0,FF}W\succeq0.18I\).
3. **Intermediate tail:** certify \(\|W^TA_{0,F,[155,3001]}\|_F<0.009\).
4. **Remote tail:** use the analytic channel/moment remainder bound \(<1.5\times10^{-4}\) for \(n\ge3003\).

These imply a six-dimensional positive subspace of the full pole-free infinite operator with margin \(>0.1766\).  Adding the PSD pole preserves that subspace.

## Guardrails

This is still a certificate design until the finite interval evaluations are actually instantiated.  The large margin makes those checks straightforward in principle but does not replace them.

No exact zero mode, \(\lambda_1=0\), RH, or GRH conclusion follows.
