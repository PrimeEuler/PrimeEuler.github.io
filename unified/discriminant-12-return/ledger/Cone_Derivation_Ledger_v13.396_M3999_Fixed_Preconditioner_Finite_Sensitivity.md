# Cone Derivation Ledger v13.396 — M3999 Fixed-Preconditioner Finite-Side Sensitivity

Date: 2026-09-11

Status labels: **[D]** exact derived, **[N]** numerical, **[N-cert]** validated computational, **[O]** open.

## 1. Purpose

Continue the v13.395 fixed-preconditioner terminal verifier by quantifying the finite-side normalized error budget at the source-faithful cutoff

\[
C=\{1,3,\ldots,19\},\qquad F=\{21,23,\ldots,3999\}.
\]

The finite Schur complement is

\[
S_F=A_{CC}-A_{CF}A_{FF}^{-1}A_{FC}.
\]

Let \(B_0\) denote the midpoint restriction of \(S_F\) to the six candidate-positive directions, and let \(L_0L_0^T=B_0\). The terminal verifier uses

\[
C_{\rm pre}=L_0^{-1}BL_0^{-T}.
\]

The v13.395 design target is \(C_{\rm pre}\succeq0.995I\).

## 2. M=3999 fifth midpoint level

**[N]** Fresh source-faithful assembly gives

\[
\boxed{\lambda_5(B_0)\approx3.85764945\times10^{-8}}.
\]

The first four levels remain numerical-zero-scale and are not interpreted as exact kernels.

Because

\[
\|L_0^{-1}\|^2=\lambda_{\min}(B_0)^{-1},
\]

a raw six-dimensional Schur perturbation \(\varepsilon_S\) produces normalized distortion at most

\[
\eta_B\le \frac{\varepsilon_S}{\lambda_5(B_0)}.
\]

## 3. Fully analytic C-F coupling bound

Use existing componentwise operator bounds:

\[
\|C_{\rm cusp}^{CF}\|\le \frac\pi2+0.706,
\]

\[
\|B_{\rm prime}^{CF}\|<2.05,
\]

\[
\|K_{\rm arch}^{CF}\|<0.4598463265.
\]

For the pole term \(P=2cc^T\),

\[
c_n=\frac{2k_n\cosh(1/2)}{k_n^2+1/4}
\le \frac{4\cosh(1/2)}{\pi n}.
\]

Using the odd tail bound

\[
\sum_{\substack{n\ge N\\n\ \mathrm{odd}}}\frac1{n^2}
\le N^{-2}+(2N)^{-1}
\]

and overbounding the low core by the full odd sum gives

\[
\|P^{CF}\|=2\|c_C\|\|c_F\|<0.74.
\]

Hence a rounded analytic target is

\[
\boxed{\|A_{CF}\|<K=5.53}.
\]

## 4. Exact-vs-nominal Schur perturbation

From v13.357, the dimension-free exact-vs-nominal operator uncertainty is

\[
\varepsilon_A<2\times10^{-13}.
\]

The certified finite-high floor gives

\[
A_{FF}\succeq \mu I,\qquad \mu=0.22.
\]

For a block perturbation of norm at most \(\varepsilon_A\), the standard inverse-resolvent estimate yields

\[
\|\Delta S_F\|
\le
\varepsilon_A
+\frac{2K\varepsilon_A}{\mu-\varepsilon_A}
+\frac{\varepsilon_A^2}{\mu-\varepsilon_A}
+\frac{K^2\varepsilon_A}{\mu(\mu-\varepsilon_A)}.
\]

With \(K=5.53\),

\[
\boxed{\|\Delta S_F\|<1.37\times10^{-10}}.
\]

Relative to \(\lambda_5(B_0)\), this consumes less than about \(0.356\%\) normalized distortion.

## 5. Point-solve arithmetic target

For an approximate finite solve

\[
A_{FF}\widehat X\approx A_{FC}
\]

with residual

\[
R=A_{FC}-A_{FF}\widehat X,
\]

positivity gives

\[
\|X-\widehat X\|\le \mu^{-1}\|R\|,
\]

and therefore the induced Schur error obeys

\[
\|A_{CF}(X-\widehat X)\|
\le \frac{K}{\mu}\|R\|.
\]

Choose the concrete verifier target

\[
\boxed{\|R\|<10^{-12}}.
\]

Then

\[
\boxed{\|\Delta S_{\rm solve}\|<2.52\times10^{-11}}.
\]

Combining exact-vs-nominal and solve budgets gives

\[
\|\Delta S_{\rm finite}\|<1.63\times10^{-10},
\]

so

\[
\eta_{\rm finite}<0.0043.
\]

Thus the existing budgets support the stronger design statement

\[
\boxed{C_{\rm pre}\succeq0.9957I},
\]

provided the M=3999 solve residual and midpoint factor are replayed with validated arithmetic.

## 6. Consequence for residual-Gram budget

Using

\[
\delta_T>0.18225976374175623
\]

and the v13.393 hybrid residual midpoint

\[
h_{\rm mid}=0.17910434985544155,
\]

the stronger finite-side lower factor leaves more than

\[
\boxed{2.35\times10^{-3}}
\]

for outward residual-Gram validation.

This is slightly better than the conservative v13.395 \(0.995I\) design.

## 7. Proof status and next target

**[D/N-target]** The sensitivity reduction is analytic except for the midpoint \(\lambda_5(B_0)\) used to set scale. The finite M=3999 point solve still needs high-precision replay with outward residual enclosure.

The next concrete verifier milestone is therefore:

1. freeze the six-dimensional basis and \(L_0\) as exact dyadic data;
2. replay the M=3999 finite solve at high precision;
3. certify \(\|R\|<10^{-12}\);
4. certify the normalized finite matrix \(C_{\rm pre}\succeq0.9957I\);
5. then spend the remaining \(>2.35\times10^{-3}\) budget on the residual-Gram side.

Guardrails: no exact-zero claim, no final inertia claim, and no RH/GRH conclusion follows.