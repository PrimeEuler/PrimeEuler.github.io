# Cone Derivation Ledger v13.391 — Quadratic Six-Plane Tail-Residual Reduction

Date: 2026-09-10

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[N-cert]** validated-computational under the stated model, **[O]** open, **[Audit]** correction/limitation.

## 1. Context

External Audit Round 24 (`v13.390`) independently retracted Round 20's archimedean objection and confirmed the resolution already recorded in `v13.387`: the source-faithful off-diagonal archimedean term is the original rank-two formula

\[
K_{\rm arch}(m,n)=-\frac4\pi\frac{nH_m-mH_n}{n^2-m^2}.
\]

Therefore the `v13.373`–`v13.386` rank-four detour remains superseded. The valid source-faithful high-block machinery is the rank-two chain used in `v13.362`–`v13.365`.

## 2. Exact Schur-of-Schur identity

**[D]** Split the high complement as

\[
\mathcal D=F\oplus T,
\qquad
F=\operatorname{span}\{\psi_n:21\le n\le M,\ n\text{ odd}\},
\]

and let

\[
S_F=A_{CC}-A_{CF}A_{FF}^{-1}A_{FC},
\]

\[
R=A_{TC}-A_{TF}A_{FF}^{-1}A_{FC},
\]

\[
T_{\rm eff}=A_{TT}-A_{TF}A_{FF}^{-1}A_{FT}.
\]

Eliminating `F` first and then `T` gives exactly

\[
\boxed{S_\infty=S_F-R^*T_{\rm eff}^{-1}R.}
\]

Thus the infinite-tail correction is positive-semidefinite and **quadratic** in the residual coupling `R`.

## 3. Effective-tail coercivity at the certified split

For the final split

\[
F=[21,16001]_{\rm odd},\qquad T=[16003,\infty)_{\rm odd},
\]

the existing source-faithful validated-computational inputs are

\[
A_{0,FF}\succeq0.22I,
\qquad
A_{0,TT}\succeq4.6732I,
\qquad
\|A_{0,FT}\|<0.994.
\]

Therefore **[N-cert, conditional on the v13.362/v13.365 validation model]**

\[
T_{{\rm eff},0}
\succeq
\left(4.6732-\frac{0.994^2}{0.22}\right)I
\]

with

\[
\boxed{\delta:=4.6732-0.994^2/0.22
=0.1821272727\ldots>0.182.}
\]

The full even-sector operator satisfies `A=A0+P_pole` with `P_pole >= 0`. By the variational characterization of the Schur complement,

\[
y^TT_{\rm eff}(A)y=\min_x [x;y]^TA_D[x;y],
\]

so adding the PSD pole cannot lower the effective tail. Hence

\[
\boxed{T_{\rm eff}(A)\succeq \delta I}
\]

under the same validated-computational assumptions.

## 4. Six-plane positivity criterion

Let `Q` have six orthonormal columns spanning a candidate positive subspace of the ten-dimensional low core, numerically chosen from the fifth through tenth finite-Schur eigendirections. Then **[D]**

\[
Q^TS_\infty Q
=Q^TS_FQ-(RQ)^*T_{\rm eff}^{-1}(RQ).
\]

Since `T_eff >= delta I`,

\[
Q^TS_\infty Q
\succeq
Q^TS_FQ-\delta^{-1}(RQ)^*(RQ).
\]

Therefore the terminal sufficient condition is

\[
\boxed{
Q^TS_FQ-\delta^{-1}G_R\succ0,
\qquad
G_R:=(RQ)^*(RQ).
}
\]

This is strictly sharper than the `v13.389` brute-force target of certifying every one of ten solve residuals near `1e-11`: the omitted tail enters quadratically, and the residual is strongly anisotropic.

## 5. Numerical residual anatomy

**[N only]** Smaller-cutoff direct solves, with `R` sampled on only the next equal-width tail band, give:

| M | sigma1(R) | sigma2/sigma1 | partial delta_crit |
|---:|---:|---:|---:|
| 199 | 0.39070542 | 5.03e-3 | 0.4702043 |
| 399 | 0.30397291 | 2.125e-3 | 0.3978217 |
| 799 | 0.23431651 | 9.117e-4 | 0.2713112 |
| 1199 | 0.20109175 | 5.529e-4 | 0.2108109 |

Here

\[
\delta_{\rm crit}=\lambda_{\max}
\left(S_W^{-1/2}R_W^*R_WS_W^{-1/2}\right)
\]

is computed only from that sampled finite tail band. These values are diagnostics, not enclosures for the full infinite tail.

At `M=1199`, the dominant residual right singular vector has approximate absolute overlaps

\[
|\langle r_1,v_5\rangle|\approx2.13\times10^{-5},
\]

\[
|\langle r_1,v_6\rangle|\approx0.108,
\qquad
|\langle r_1,v_7\rangle|\approx0.994,
\qquad
|\langle r_1,v_8\rangle|\approx0.020.
\]

Thus the largest residual channel is almost orthogonal to the tiny fifth Schur direction and lands primarily in a much larger positive direction. This is the geometric reason the quadratic six-plane test is promising.

## 6. New terminal target

**[O]** At the actual split `F=[21,16001]`:

1. Fix a reproducible six-plane `Q`.
2. Compute and validate the finite matrix `Q^T S_F Q`.
3. Compute an upper enclosure for the **full infinite** residual Gram
   \[
   G_R=(RQ)^*(RQ),\qquad T=[16003,\infty),
   \]
   using the source-faithful rank-two/Cauchy expansion and analytic tail machinery already used in `v13.365`.
4. Verify by a small validated `6x6` LDL/eigenvalue certificate that
   \[
   Q^TS_FQ-\delta^{-1}G_R\succ0.
   \]

If this succeeds, the full ten-dimensional Schur complement has at least six positive directions. Because the high complement is positive, this gives the desired global bound of at most four nonpositive directions in this sector. It still does **not** identify any exact zero directions.

## 7. Guardrails

- The partial-tail `delta_crit` trend is not a proof and must not be extrapolated to `M=16001`.
- The first four finite Schur eigenvalues remain numerical near-zeros only; no exact kernel/nullity statement is made.
- This checkpoint does not prove RH/GRH and does not establish `lambda_1=0`.
- `v13.389` remains useful as a generic residual bound, but its uniform `~1e-11` ten-column target is superseded as the preferred terminal strategy by the quadratic six-plane criterion above.

## Companion executable

`research-notes/suzuki_source_faithful_six_plane_tail_residual_diagnostic.py`
