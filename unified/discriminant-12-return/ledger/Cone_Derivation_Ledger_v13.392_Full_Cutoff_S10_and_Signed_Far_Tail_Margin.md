# Cone Derivation Ledger v13.392 — Full-Cutoff S10 and Signed Far-Tail Margin

Date: 2026-09-10

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[N-cert]** validated-computational under the stated model, **[O]** open.

## 1. Full source-faithful finite solve at the actual interface

Using the restored source-faithful rank-two matrix, the actual finite high block

\[
F=\{21,23,\ldots,16001\},\qquad \dim F=7991,
\]

was factored by the exact displacement-generator LDL recurrence.  The full even-sector pole was included by a rank-one Woodbury update.  The resulting ten-dimensional finite Schur matrix

\[
S_F=A_{CC}-A_{CF}A_{FF}^{-1}A_{FC}
\]

has **[N]** eigenvalues

\[
\lambda_1,\ldots,\lambda_4\sim10^{-13}\text{--}10^{-12},
\]

\[
\boxed{\lambda_5(S_F)\approx3.82590205\times10^{-8}},
\]

\[
\boxed{\lambda_6(S_F)\approx2.14472468\times10^{-4}},
\]

followed approximately by

\[
0.769095194,\quad1.70185089,\quad2.01522883,\quad2.34737759.
\]

The first four values are numerical near-zeros only.  No exact kernel claim is made.

This is the first direct 7991-mode `S_F` computation in the post-audit source-faithful chain and extends the finite-section sequence from v13.388.

## 2. Actual-interface six-plane residual geometry

Let `Q` consist of the fifth through tenth numerical eigenvectors of `S_F`, and let

\[
R=A_{TC}-A_{TF}A_{FF}^{-1}A_{FC},
\qquad T=\{16003,16005,\ldots\}.
\]

On the first equal-width tail band `16003..31983`, **[N]**

\[
\sigma(RQ)\approx
(5.94798\times10^{-2},\ 1.53299\times10^{-6},\ 3.45792\times10^{-9},\ 7.58\times10^{-14},\ldots).
\]

Thus the projected residual is numerically almost rank one at the actual certified interface.

Writing

\[
D_W=\operatorname{diag}(\lambda_5(S_F),\ldots,\lambda_{10}(S_F)),
\]

the first-band normalized Gram has

\[
\boxed{
\lambda_{\max}(D_W^{-1/2}(RQ)^*(RQ)D_W^{-1/2})
\approx0.02748277.
}
\]

The available effective-tail coercivity from v13.391 is

\[
\delta\ge4.6732-\frac{0.994^2}{0.22}
=0.1821272727\ldots,
\]

so the first tail band alone has a factor greater than 6.6 of numerical margin.

## 3. Cumulative tail diagnostic

Direct chunked accumulation gives the following **[N]** cumulative normalized-Gram values:

| tail endpoint | cumulative value |
|---:|---:|
| 31,983 | 0.02748277 |
| 63,999 | 0.04170390 |
| 127,999 | 0.04894821 |
| 255,999 | 0.05260991 |
| 511,999 | 0.05445132 |
| 1,023,999 | 0.05537475 |

Each doubled band's incremental contribution is approximately halving.  This is diagnostic only and is not extrapolated as a proof.

## 4. Exact signed far-tail expansion

**[D]** For one projected direction, combine its core and eliminated-finite coefficients into `w_j`, `j<=16001`.  From the exact source-faithful rank-two formula,

\[
r_n^{(0)}=\frac2\pi\left[
\frac{Z_n}{n^2}\sum_j\frac{j w_j}{1-j^2/n^2}
-\frac1n\sum_j\frac{Z_j w_j}{1-j^2/n^2}
\right].
\]

The pole adds `2 c_n p`, where

\[
p=\sum_j c_jw_j.
\]

Using

\[
c_n=\frac{4\cosh(1/2)}{\pi n}\frac1{1+1/(\pi^2n^2)},
\]

the signed leading coefficient is

\[
\boxed{
L=-\frac2\pi\sum_jZ_jw_j+\frac{8\cosh(1/2)}\pi p.
}
\]

For `n>=N>16001`, set `rho=16001/N`.  Then

\[
|r_n-L/n|\le B/n^2+C/n^3,
\]

with

\[
B=\frac{16/\pi}{1-\rho^2}\sum_j|jw_j|,
\]

and

\[
C=\frac{2/\pi}{1-\rho^2}\sum_j|j^2Z_jw_j|
+\frac{8\cosh(1/2)}{\pi^3}|p|.
\]

The key improvement over the crude v13.389 norm estimate is that the leading `1/n` term is retained **with sign**, including its cancellation against the pole.

## 5. Far-tail Z envelope

**[D]** From

\[
Z_n=2A_n+\Im\psi\!\left(\frac14+i\frac{n\pi}{4}\right)
+n\pi\sum_{k\ge0}\frac{e^{-2a_k}}{a_k^2+(n\pi/2)^2},
\]

we have

\[
|A_n|\le\sum_q\frac{\Lambda(q)}{\sqrt q}=2.9262341821\ldots.
\]

For `y=n*pi/4`, the positive series representation gives

\[
0<\Im\psi(1/4+iy)
=\sum_{k\ge0}\frac{y}{(k+1/4)^2+y^2}
\le \frac1y+\frac\pi2.
\]

The remaining exponential series is `O(1/n)`.  Hence the deliberately loose envelope

\[
\boxed{|Z_n|<8}
\]

holds throughout the far-tail range used here.

## 6. Numerical far-tail margin

Using the actual 7991-mode midpoint six-plane coefficients in the exact bounds above, **[N]** the normalized Frobenius/operator tail contribution from

\[
N=128001
\]

onward is bounded by

\[
\boxed{\Delta_{\rm far}<0.00866328}.
\]

Combining this midpoint-coefficient far-tail bound with the directly accumulated Gram through `127999` gives the diagnostic total

\[
\boxed{\delta_{\rm crit}^{\rm diagnostic}<0.05762},
\]

versus

\[
\boxed{\delta\ge0.18212727}.
\]

The raw margin is therefore greater than a factor of 3.1.

## 7. What remains for certification

**[O]** The remaining task is no longer numerically delicate:

1. outward-enclose the six-dimensional finite matrix `Q^T S_F Q`;
2. outward-enclose the residual Gram for `16003<=n<=127999`;
3. outward-enclose the signed far-tail moment vectors `L,B,C`;
4. combine them into a validated upper matrix/scalar tail bound;
5. verify the resulting `6x6` lower matrix is positive by validated LDL.

Because the diagnostic target is about `0.0576` against an available `0.1821`, this stage has roughly a factor-three gross margin and should not require resolution at the `lambda_5~4e-8` scale entry-by-entry.

## 8. Guardrails

- The 7991-mode solve and finite-tail accumulation reported here are ordinary floating-point diagnostics, not outward-rounded enclosures.
- The far-tail inequality is exact structurally, but its displayed numerical coefficient uses midpoint solve/Q data and therefore is not yet a validated bound.
- The first four near-zero finite Schur eigenvalues are not exact kernels.
- No RH/GRH or `lambda_1=0` claim follows.

## Companion executable

`research-notes/suzuki_source_faithful_S10_full_cutoff_tail_diagnostic.py`
