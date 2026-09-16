# Cone Derivation Ledger v13.510 — M16001 Derived-Radius Rebuild Gate

Date: 2026-09-16

Status: **[Audit]** fail-closed correction and executable proof obligation.

## 0. Synchronization

Live head was checked at the start and immediately before this write. v13.509 (External Audit Round 38) is the latest numbered ledger entry. The new unnumbered helper `85239961...` landed after it. Thus v13.510 is free.

## 1. Audit acceptance

Round 38 is accepted. v13.508's remote-Gram and far-tail radii were literals rather than outputs of a committed operation-count/magnitude derivation. Therefore its `[N-cert]` label and theorem promotion are unsupported.

Certified status is restored to

\[
\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4,
\qquad
\operatorname{ind}_{\le0}(A_{a=1})\le6.
\]

The positive M16001 seven-plane midpoint remains a diagnostic target only.

## 2. Replacement arithmetic model

New helper:

`research-notes/suzuki_M16001_gamma_derived_radius_scaffold.py`

commit `85239961d73327323bd3a2cdfdbdb89d0912b578`.

It implements the standard

\[
\gamma_k=\frac{ku}{1-ku},\qquad u=2^{-64},
\]

and the dot-product bound

\[
|\operatorname{fl}(x^Ty)-x^Ty|\le\gamma_k\sum_i|x_i y_i|.
\]

For the finite high block it reproduces

\[
\gamma_{7991}=4.331929780165835\ldots\times10^{-16}.
\]

The remote row count is 992000, so the one-shot conservative accumulation factor is `gamma_992000`; chunked accounting may be sharper but must be derived from the actual chunk tree.

## 3. No hard-coded certificate radii

The replacement helper contains no accepted QQ/QN/NN safety constants. It fails closed until the numerical replay itself emits five magnitude transcripts:

1. finite LDL/Woodbury pivot/generator/RHS and residual absolute-product sums;
2. finite Schur dot absolute-product sums;
3. normalized Q/N formation absolute-product sums;
4. per-chunk remote `R^T R` absolute-product sums plus chunk-accumulation magnitudes;
5. far-tail moment absolute-product sums and final envelope arithmetic.

Empirical binary64/long-double differences may be retained as diagnostics but cannot supply any theorem-level radius.

## 4. Exact next obligation

Instrument the existing M16001 anisotropic replay so every long-double reduction reports `sum(abs(products))` (or a stronger exact magnitude majorant) together with its operation count. Feed only those emitted quantities into the gamma scaffold. Then propagate the resulting computed radii through

\[
a_N-\|B_{QN}\|^2/\lambda_Q.
\]

Only a strictly positive outward lower endpoint from that fully reproducible chain may restore the v13.508 promotion.
