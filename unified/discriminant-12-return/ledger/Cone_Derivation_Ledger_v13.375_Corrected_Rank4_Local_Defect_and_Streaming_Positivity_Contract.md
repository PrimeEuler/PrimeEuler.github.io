# Cone Derivation Ledger v13.375 — Corrected Rank-4 Local Defect and Streaming Positivity Contract

Date: 2026-09-09

Status labels: **[D]** exact derived, **[N]** midpoint numerical, **[Target]** validation target, **[O]** open, **[Audit]** correction/limitation.

## 1. Context

External Audit Rounds 20–21 invalidated the legacy rank-two unified off-diagonal representation because the archimedean term had been cross-paired incorrectly.  v13.373–v13.374 rebuilt the intended operator with the corrected formula

\[
K_{\rm arch}(m,n)
=\pi mn\frac{nH_n-mH_m}{m^2-n^2}
\]

and showed that the corrected full pole-free matrix is still Cauchy-like, now with displacement rank at most four.

The corrected full-scale midpoint LDL run on modes `21..16001` gave

\[
\boxed{d_{\min}^{\rm mid}\approx0.255479084585364}
\]

at mode `n=29`.

This checkpoint rebuilds the *certificate architecture* around that corrected rank-four factorization rather than reusing any legacy rank-two transcript.

## 2. [D] Corrected rank-four local reconstruction defect

For one trailing state write

\[
M_{ij}
=c_1\frac{p_iq_j-q_ip_j}{x_i-x_j}
+c_2\frac{r_is_j-s_ir_j}{x_i-x_j},\qquad i\ne j,
\]

with

\[
c_1=\frac2\pi,\qquad c_2=\pi.
\]

Initially the two generator pairs are

\[
(p,q)=(U,n),\qquad (r,s)=(n,n^2H_n).
\]

At one scalar LDL step let `a` be the pivot, let `b_*` be the exact first column reconstructed from the current stored point generators, and define

\[
\ell_*=b_*/a.
\]

The exact Schur state is

\[
d_*'=d_{\rm tail}-b_*^2/a,
\]

\[
p_*'=p_{\rm tail}-\ell_*p_1,
\quad q_*'=q_{\rm tail}-\ell_*q_1,
\]

\[
r_*'=r_{\rm tail}-\ell_*r_1,
\quad s_*'=s_{\rm tail}-\ell_*s_1.
\]

For stored next-state values define discrepancies

\[
e_\ell=\widehat\ell-\ell_*,\quad e_d=\widehat d'-d_*',
\]

\[
e_p=\widehat p'-p_*',\quad e_q=\widehat q'-q_*',
\]

\[
e_r=\widehat r'-r_*',\quad e_s=\widehat s'-s_*'.
\]

Then the same block reconstruction argument as v13.359 gives

\[
\|\Delta\|_F
\le
\sqrt2|a|\|e_\ell\|_2
+\|e_d\|_2
+\delta_{\rm off}
+|a|\|e_\ell\|_2(\|\ell_*\|_2+\|\widehat\ell\|_2),
\]

where the corrected off-diagonal state mismatch is

\[
\boxed{
\delta_{\rm off}
\le \frac{2}{D_{\min}}
\left[
|c_1|\bigl(\|e_p\|_2\|q_*'\|_2+\|\widehat p'\|_2\|e_q\|_2\bigr)
+|c_2|\bigl(\|e_r\|_2\|s_*'\|_2+\|\widehat r'\|_2\|e_s\|_2\bigr)
\right].
}
\]

This follows pairwise from

\[
B(u,v)=uv^T-vu^T,
\qquad
\|B(y,z)\|_F\le2\|y\|_2\|z\|_2.
\]

For odd Fourier modes the trailing denominator separation remains explicit:

\[
D_{\min}=(n+2)^2-n^2=4n+4.
\]

## 3. [D] Global residual composition is unchanged

If `Delta_k` is the local reconstruction defect at step `k`, then exactly

\[
E=\sum_k P_k\Delta_kP_k^T,
\]

so

\[
\boxed{
\|E\|_2
\le
\||L|\|_1\,\||L|\|_\infty
\sum_k\|\Delta_k\|_F.
}
\]

Thus the corrected replay retains the v13.359–360 strategy: high-precision point factorization plus a higher-precision directed-rounded local checker, with no interval generator state propagated through all 7991 steps.

## 4. [D] O(N)-memory inverse-factor majorant

A second simplification removes the need to reconstruct the old packed-L column bound from v13.356.

For unit lower-triangular `L`, define recursively

\[
y_i=1+\sum_{j<i}|l_{ij}|y_j.
\]

Forward-substitution majorization gives

\[
|L^{-1}|\mathbf1\le y,
\]

hence

\[
\boxed{
\|L^{-1}\|_\infty\le y_{\max}:=\max_i y_i.
}
\]

Because column `j` is produced only after `y_j` is finalized, the recurrence can be accumulated online:

\[
a_i\leftarrow a_i+|l_{ij}|y_j.
\]

Then when row `i` reaches its pivot,

\[
y_i=1+a_i.
\]

Only O(N) storage is required.

Using

\[
\|L^{-1}\|_2\le\sqrt N\,\|L^{-1}\|_\infty,
\]

a sufficient positivity condition for

\[
B=A_{0,[21,16001]}-0.22I=LDL^T+E_{\rm total}
\]

is

\[
\boxed{
\|E_{\rm total}\|_2
<\frac{d_{\min}}{N y_{\max}^2}.
}
\]

## 5. [Target] Deliberately loose corrected replay targets

The corrected midpoint minimum pivot is about `0.255479`, so choose

\[
\boxed{d_{\min}>0.25}.
\]

The legacy infinity inverse majorant was about `21.22`, but that value is **not inherited**.  A deliberately loose corrected target is

\[
\boxed{y_{\max}<25}.
\]

If both targets validate, then with `N=7991`,

\[
\frac{0.25}{7991\cdot25^2}
=
\boxed{5.005631335\times10^{-8}}.
\]

The dimension-free exact-vs-nominal matrix uncertainty remains naturally at the previous scale because the arch correction is the correct algebraic form of the same compressed integral kernel:

\[
\boxed{E_{\rm matrix}<2\times10^{-13}}
\]

remains a reasonable validation target.

Choose the new arithmetic target

\[
\boxed{E_{\rm arith}<10^{-9}}.
\]

Then

\[
E_{\rm total}<1.0002\times10^{-9},
\]

which would leave a safety factor greater than 49 against the coarse `y_max<25` positivity allowance.

## 6. Required corrected transcript

A completed 7991-step directed-rounded replay should report only:

1. dimension and shift;
2. factor precision and checker precision;
3. validated minimum pivot and mode;
4. validated `y_max`;
5. `|| |L| ||_1` and `|| |L| ||_inf`;
6. `sum delta_k`;
7. arithmetic residual bound;
8. matrix uncertainty bound;
9. total residual bound;
10. `d_min/(N y_max^2)`;
11. PASS/FAIL.

## 7. Status

**[D]** The corrected rank-four local-defect bound is derived.

**[D]** The global residual composition remains exact.

**[D]** The O(N)-memory infinity inverse majorant is sufficient to avoid the old packed-L inverse calculation.

**[O]** The corrected 7991-step directed-rounded replay has not yet been executed.

**[Audit]** The old `3.15e-6` residual allowance from v13.356 is not automatically inherited.  It depended on the legacy factor's inverse norm.  This checkpoint replaces it with a fresh corrected target that will be computed from the corrected factor itself.

## Guardrail

No finite high-block positivity claim is re-promoted yet.  v13.362/v13.365 remain superseded as certificates until the corrected replay validates the new transcript.  No exact-zero, RH, or GRH claim follows.
