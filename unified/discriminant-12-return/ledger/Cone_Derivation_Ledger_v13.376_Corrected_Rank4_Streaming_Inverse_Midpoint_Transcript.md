# Cone Derivation Ledger v13.376 — Corrected Rank-4 Streaming Inverse Midpoint Transcript

Date: 2026-09-09

Status labels: **[D]** exact derived, **[N]** midpoint numerical, **[Target]** validation target, **[O]** open.

## 1. Purpose

v13.375 derived an O(N)-memory inverse-factor majorant for the corrected rank-four LDL:

\[
y_i=1+\sum_{j<i}|l_{ij}|y_j,
\qquad
\|L^{-1}\|_\infty\le y_{\max}.
\]

The intentionally loose design target was `y_max < 25`.  This checkpoint executes that streaming recurrence on the corrected full-scale midpoint factor for modes `21..16001` and removes `25` as an unsupported numerical assumption.

The executable reconstruction is

`research-notes/suzuki_corrected_rank4_streaming_midpoint_transcript.py`.

It rebuilds the scalar data from the prime/cusp formulas and the degree-65 rational archimedean polynomial, runs the corrected displacement-rank-four LDL, and streams the inverse and factor-growth quantities without storing a dense matrix or packed factor.

## 2. [N] Corrected full-scale midpoint transcript

For

\[
B=A_{0,[21,16001]}-0.22I,
\qquad N=7991,
\]

the corrected rank-four midpoint recurrence gives

\[
\boxed{d_{\min}^{\rm mid}=0.25547908458536\ldots}
\]

at mode

\[
\boxed{n=29}.
\]

The streamed absolute-factor norms are

\[
\boxed{\||L|\|_1\approx43.02616786684},
\]

\[
\boxed{\||L|\|_\infty\approx3.72623077509}.
\]

The forward inverse majorant is

\[
\boxed{y_{\max}^{\rm mid}\approx18.13687509296}
\]

with maximum attained near mode

\[
\boxed{n=345}.
\]

Thus the deliberately loose v13.375 design target `y_max < 25` is comfortably satisfied at midpoint.

## 3. [N] Fresh crude inverse and residual allowance

Using only

\[
\|L^{-1}\|_2\le\sqrt N\,\|L^{-1}\|_\infty
\le\sqrt N\,y_{\max},
\]

the midpoint corrected factor gives

\[
\|L^{-1}\|_2
\lesssim
\sqrt{7991}(18.13687509296)
\approx1621.30.
\]

Therefore the corresponding midpoint a-posteriori residual allowance is

\[
\boxed{
\frac{d_{\min}}{N y_{\max}^2}
\approx9.71917\times10^{-8}.
}
\]

This is nearly twice the deliberately conservative design allowance from v13.375,

\[
5.00563\times10^{-8},
\]

and about 97 times the proposed arithmetic target `1e-9`.

## 4. Comparison with the superseded rank-two factor

The legacy factor had midpoint diagnostics

\[
d_{\min}\approx0.2542996,
\qquad
\|L^{-1}\|_\infty\lesssim21.2201.
\]

The corrected factor therefore has both

- a slightly larger minimum pivot, and
- a smaller streamed infinity inverse majorant.

This strengthens the numerical conditioning of the repaired finite-block route.  It does **not** by itself replace the directed-rounded arithmetic residual certificate.

## 5. What remains open

**[O]** Re-run the local arithmetic-defect accumulation for the corrected four-generator recurrence under the stated long-double/IEEE arithmetic model or, preferably, the two-precision directed-rounded replay.

The final transcript must validate rather than merely midpoint-estimate:

\[
d_{\min}>0.25,
\qquad y_{\max}<25,
\]

and must produce a rigorous total residual below the validated allowance.

The dimension-free matrix uncertainty target remains

\[
E_{\rm matrix}<2\times10^{-13}.
\]

## Guardrail

This checkpoint is a reproducible full-scale **midpoint** transcript.  It is strong evidence that the corrected finite-block certificate will close with ample margin, but `A_{0,[21,16001]}\succeq0.22I` is not re-promoted as certified until the corrected arithmetic residual replay is completed.  The infinite high complement and `S_10` remain downstream.  No exact-zero, RH, or GRH claim follows.
