# Cone Derivation Ledger v13.350

## Near/far Gram threshold audit and return to the N≈10003 working split

### Purpose

Test whether the corrected low-rank far-tail factorization from v13.349 is already sufficient to prove the entire high complement positive at the smaller split `N=6003`.

### Near/far decomposition

For finite high modes `21..6001`, split the tail columns into

- near: `6003..16003`,
- far: `>=16005`.

Write

\[
G=[G_{\rm near}\;G_{\rm far}].
\]

Since the column sets are disjoint,

\[
GG^T=G_{\rm near}G_{\rm near}^T+G_{\rm far}G_{\rm far}^T,
\]

so

\[
\|G\|^2\le \|G_{\rm near}\|^2+\|G_{\rm far}\|^2.
\]

This is substantially better than the triangle bound
`||G|| <= ||G_near||+||G_far||`.

### Current targeting data

From the existing finite moving-interface audit,

\[
\|G_{\rm near}\|\approx0.883639329283.
\]

From v13.349's combined pole-free Cauchy low-rank far-tail audit,

\[
\|G_{\rm far}\|\approx0.45807.
\]

Hence the coarse Gram estimate is

\[
\boxed{
\|G\|\lesssim
\sqrt{0.883639329283^2+0.45807^2}
\approx0.9953123.
}
\]

### Schur threshold at N=6003

The finite high block has midpoint minimum

\[
\gamma_F\approx0.227336299782,
\]

and the robust analytic tail gap based on the rounded prime bound is

\[
\alpha_T\approx3.6926350482594.
\]

A sufficient Schur condition is

\[
\|G\|<\sqrt{\gamma_F\alpha_T}.
\]

Numerically,

\[
\boxed{
\sqrt{\gamma_F\alpha_T}\approx0.916226.
}
\]

Thus the coarse near/far Gram estimate does **not** close at `N=6003`.

The corresponding adverse penalty is about

\[
\frac{0.9953123^2}{3.692635}\approx0.26828,
\]

which exceeds the finite gap `~0.22734`.

### Consequence

The `N=6003` route is superseded **for this coarse norm-combination method**. This is not evidence that the actual high complement is nonpositive; it only shows that the current sufficient inequalities are too weak there.

The preferred main split returns to approximately

\[
N=10003,
\]

where the analytic tail gap is about

\[
\alpha_{10003}\approx4.2034.
\]

If the finite high-block minimum remains near `0.227`, the allowable cross norm is approximately

\[
\sqrt{0.227\times4.2034}\approx0.977.
\]

That is much closer to the observed moving-interface coupling scale.

### Next proof object

At the `N≈10003` split:

1. certify the finite pole-free high block `21..10001`;
2. certify a finite near-tail cross block;
3. represent the separated far block by the exact rank-`2K` Cauchy expansion of v13.349;
4. combine near and far contributions at the Gram-matrix level;
5. compare the resulting cross norm against `sqrt(gamma_F alpha_T)`.

### Guardrails

- All displayed finite/cross values are still targeting numerics, not interval certificates.
- v13.350 is a negative result about one sufficient bound, not about the operator's true sign.
- No exact-zero, `lambda_1=0`, RH, or GRH conclusion follows.
