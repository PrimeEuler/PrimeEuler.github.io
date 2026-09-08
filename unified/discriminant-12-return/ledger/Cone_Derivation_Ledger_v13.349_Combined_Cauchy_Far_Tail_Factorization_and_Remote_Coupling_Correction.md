# Cone Derivation Ledger v13.349

## Combined Cauchy far-tail factorization and remote-coupling correction

### Status

This checkpoint corrects an overly optimistic intermediate estimate and replaces it with a structurally stronger far-tail representation. It does **not** certify the full high complement positive yet.

### Correction

The earlier hope that the remote block from finite modes `21..6001` into `n>=16005` would be only a few `1e-3` is false. The noncompact prime channel leaves an `O(10^-1)` remote coupling. A midpoint low-rank audit puts the combined pole-free remote norm near

\[
\|A_{0,[21,6001],[16005,\infty)}\|_2\approx 0.45807.
\]

This means entrywise triangle estimates are inappropriate for the global high-complement proof.

### Exact combined Cauchy identity

For off-diagonal odd modes define

\[
Z_j=2A_j+\operatorname{Si}(j\pi)+2H_j.
\]

Using the exact prime, cusp and smooth archimedean formulas,

\[
\boxed{
(A_0)_{mn}
=-\frac{2}{\pi}\frac{nZ_m-mZ_n}{n^2-m^2}
},\qquad m\ne n.
\]

Thus the three pole-free cross blocks are not separate certification problems.

### Separated far-tail factorization

For `m<=M<R<=n`,

\[
\frac1{n^2-m^2}
=\frac1{n^2}\sum_{k\ge0}\left(\frac mn\right)^{2k}.
\]

Hence

\[
(A_0)_{mn}
=-\frac2\pi\sum_{k\ge0}
\left[
\frac{m^{2k}Z_m}{n^{2k+1}}
-\frac{m^{2k+1}Z_n}{n^{2k+2}}
\right].
\]

Every term is rank at most two. At

\[
M=6001,\qquad R=16005,
\]

one has

\[
M/R<0.375,
\]

so the factorization converges quickly.

A `K=5` truncation has rank at most ten. The proof object can therefore be a tiny Gram matrix, not a huge rectangular matrix. The remaining series tail is bounded geometrically.

### Safe global bounds

The existing exact finite-prime setup gives a safe

\[
|A_j|\le 2.927.
\]

Also one may use

\[
|\operatorname{Si}(j\pi)|\le2,
\qquad
|H_j|\le\int_0^2h(t)dt\le\frac12,
\]

hence

\[
|Z_j|\le8.854.
\]

Using interval-certified finite `Z_m` values in the left factor, the midpoint targeting remainder after `K=5` is about `3.2e-6`, and after `K=6` about `4e-7`. These are not yet interval certificates.

### Consequence for the global strategy

The corrected architecture is now:

1. certify the finite high block;
2. treat a contiguous near-tail block numerically/interval-wise;
3. treat the separated remote block by the exact low-rank Cauchy expansion;
4. combine the near and far pieces at the Gram-matrix level rather than by triangle inequality whenever possible;
5. use the analytic logarithmic tail coercivity only after the full cross norm is enclosed.

This preserves the cancellation responsible for the observed cross norm below one.

### Guardrails

- The midpoint `0.45807` far norm is targeting data, not certified.
- Full high-complement positivity is not yet proved.
- The previous `few 1e-3` remote-coupling expectation is superseded.
- No exact-zero, `lambda_1=0`, RH, or GRH claim follows.
