# Cone Derivation Ledger v13.512 — M16001 Transcripted Gamma Replay Instrumentation

Date: 2026-09-16

Status: **[Audit] / [N]**. No theorem promotion.

## 0. Synchronization

Live ledger checked at start and immediately before this write. v13.511 (External Audit Round 39) is latest numbered entry and independently confirms the v13.510 correction. Round 39 also catches a cosmetic count error: the explicit odd remote rows are **991999**, not 992000. The executable scaffold already had the correct formula/count.

## 1. Instrumented replay

New helper:

`research-notes/suzuki_M16001_gamma_transcripted_replay.py`

commit `473ad523d9def8b2559c672deb3a4b27fa5ff37b`.

The helper instruments the existing M16001 anisotropic replay so reductions produce their own standard-gamma radii from

\[
\gamma_k\sum_i |x_i y_i|.
\]

It covers:

- finite `S*B` and `B^T S B` projection reductions;
- explicit remote `R^T R` chunk dot products for 991999 rows, plus chunk-addition rounding;
- the three far-moment reductions `sum ZW`, `sum jW`, and `sum j^2 ZW`.

No empirical double/long-double discrepancy is converted into a certificate radius.

## 2. Remaining finite-solve obligation

The structured LDL/Woodbury solution `X` must still receive a reproducible residual transcript for

\[
R_F=A_{FF}X-A_{FC}.
\]

That residual must be formed with the source-faithful high-block action and each 7991-term reduction charged by its actual absolute-product sum and `gamma_7991`. Only then may the residual be propagated through the inverse/coercivity bound into the finite Schur and Q/N blocks.

This is deliberately left fail-closed rather than importing the v13.508 literal.

## 3. Certified status

Unchanged:

\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4},\qquad
\boxed{\operatorname{ind}_{\le0}(A_{a=1})\le6}.
\]

Next: implement the source-faithful `A_FF X` residual action without materializing the 7991x7991 dense matrix, using the displacement/rank-one structure already used by the structured solver, and emit the final missing gamma transcript.