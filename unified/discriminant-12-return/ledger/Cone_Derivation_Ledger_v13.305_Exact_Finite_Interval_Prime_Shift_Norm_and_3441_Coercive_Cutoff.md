# Cone Derivation Ledger v13.305 — Exact Finite-Interval Prime Shift Norm and 3441 Coercive Cutoff

**Status:** EXACT SINGLE-SHIFT NORMS ON [-1,1] IDENTIFIED; PRIME OPERATOR TRIANGLE BOUND IMPROVED FROM 5.852468... TO 3.129252...; EXPLICIT EVEN-SECTOR COERCIVE CUTOFF LOWERED TO N=3441. RH/GRH NOT PROVED.

## 1. Purpose

v13.304 showed that, after localizing the compact cusp correction and the rank-one pole term, the dominant permanent perturbation costs in the even-v sector are

\[
\|H_{\rm odd}\|=\frac\pi2,
\qquad
\|B_{\rm prime}\|,
\qquad
\|K_{\rm arch\,rem}\|.
\]

The prime term was still bounded by assigning norm 2 to each truncated shift. v13.305 replaces that with the exact finite-interval norm of each shift operator.

## 2. One-shift operator

For one breakpoint \(\ell\), define on \(L^2(-1,1)\)

\[
(S_\ell f)(x)=f(x-\ell)+f(x+\ell),
\]

with zero extension outside \([-1,1]\).

Decompose \([-1,1]\) into residue classes modulo \(\ell\). On each fiber, the points connected by \(\pm\ell\) form a finite path graph. If the longest fiber contains \(r\) vertices, then the fiber adjacency matrix is \(P_r\), whose norm is

\[
2\cos\frac{\pi}{r+1}.
\]

Therefore

\[
\boxed{
\|S_\ell\|=2\cos\frac{\pi}{r+1}
}
\]

with \(r\) the maximum number of points in an interval of length 2 separated by \(\ell\).

## 3. Suzuki prime-power shifts at a=1

The breakpoints are

\[
\ell_q=\log q,
\qquad q\in\{2,3,4,5,7\}.
\]

For \(q=2\),

\[
2\log2<2<3\log2,
\]

so the longest fiber has three vertices and

\[
\boxed{\|S_{\log2}\|=\sqrt2.}
\]

For \(q=3,4,5,7\), \(1<\log q<2\), so the longest fiber has two vertices and

\[
\boxed{\|S_{\log q}\|=1.}
\]

Thus the previous universal bound \(\|S_\ell\|\le2\) was unnecessarily loose for all five shifts.

## 4. Improved rigorous prime bound

The prime operator is the weighted sum

\[
B_{\rm prime}=-\sum_q \frac{\Lambda(q)}{\sqrt q}S_{\log q}.
\]

Using the exact one-shift norms but still only the triangle inequality between different \(q\),

\[
\|B_{\rm prime}\|
\le
\frac{\log2}{\sqrt2}\sqrt2
+\frac{\log3}{\sqrt3}
+\frac{\log2}{2}
+\frac{\log5}{\sqrt5}
+\frac{\log7}{\sqrt7}.
\]

Numerically,

\[
\boxed{
\|B_{\rm prime}\|\le3.129252291002081.
}
\]

The old v13.298/v13.304 triangle bound was

\[
5.852468364352818.
\]

No cancellation between different prime-power shifts is used here.

## 5. Updated tail coercivity

Retain from v13.304:

\[
\|H_{\rm odd}\|=\frac\pi2,
\]

and the fully analytic archimedean-remainder bound

\[
\|K_{\rm arch\,rem}\|\le2.0563386856\ldots.
\]

The cusp Hilbert-Schmidt correction and even-sector pole term are localized to the tail and decay with the cutoff \(N\). Therefore

\[
\langle A_{\rm even}c,c\rangle
\ge
\left[\log(N/4)-C_{\rm tail}(N)\right]\|c\|_2^2,
\]

where

\[
C_{\rm tail}(N)
=
\frac\pi2
+3.1292522910\ldots
+2.0563386856\ldots
+\|P_NK_{\rm cusp}P_N\|
+\|P_NK_{\rm pole}P_N\|.
\]

Using the same analytic tail estimates as v13.304, the first odd cutoff found is

\[
\boxed{N=3441.}
\]

At this cutoff the compact/rank-one tail costs are already small:

\[
\|P_NK_{\rm cusp}P_N\|\lesssim3.01\times10^{-5},
\]

\[
\|P_NK_{\rm pole}P_N\|\lesssim5.99\times10^{-4}.
\]

The resulting lower-bound margin is positive, approximately

\[
2.06\times10^{-4}.
\]

Thus the explicit sufficient tail threshold has fallen from about \(5.56\times10^6\) in v13.303, to \(52363\) in v13.304, and now to \(3441\).

## 6. Interpretation

This materially strengthens the infinite-dimensional control. The cutoff is still conservative because:

- different prime shifts are still combined only by triangle inequality;
- the Hilbert term is kept at its full norm \(\pi/2\);
- the archimedean-remainder bound is analytic but intentionally coarse.

However, v13.305 no longer needs any conjectural or numerical cancellation in the prime term to reach a few-thousand-mode coercive threshold.

What is established here is a high-tail coercivity bound in the even-v sector. It does **not** establish

- \(\ker G_1\neq\{0\}\),
- \(\lambda_1=0\),
- RH,
- GRH.

## 7. Files

- `research-notes/suzuki_finite_interval_prime_shift_norm.py`
- this ledger entry

## 8. Next checkpoint

v13.306 should test the **joint** five-shift prime operator rather than only summing exact one-shift norms. The right object is the lowest spectral edge / operator norm of

\[
\sum_q \frac{\Lambda(q)}{\sqrt q}S_{\log q}
\]

on the even sector and on high-mode compressions. Any rigorous reduction below 3.129252 would lower the cutoff further. A second route is to sharpen the analytic archimedean-remainder norm, now the next-largest permanent cost after the prime term.
