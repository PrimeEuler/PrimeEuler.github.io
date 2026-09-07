# Cone Derivation Ledger v13.304 — Tail-Localized Coercivity and Analytic Archimedean Bound

**Status:** EXPLICIT INFINITE-TAIL COERCIVITY THRESHOLD IMPROVED FROM MILLIONS TO ~5.24×10^4 MODES; POLE TERM SHOWN RANK ONE IN EVEN SECTOR; ARCHIMEDEAN-REMAINDER CONSTANT REPLACED BY FULLY ANALYTIC MAJORANT. RH/GRH NOT PROVED.

## 1. Purpose

v13.303 proved an explicit high-tail coercivity estimate for the a=1 even-v sector, but it used global bounds for every perturbation. Two of those pieces are compact and should not pay their full global norm on a high-mode tail:

- the cusp Hilbert-Schmidt correction K_cusp;
- the smooth pole contribution.

v13.304 localizes those terms. It also removes a proof-status caveat from the archimedean remainder by replacing the earlier numerically evaluated convergent-series majorant with a closed analytic bound.

The operator model remains

\[
A_{\rm even}=D_{\log}-H_{\rm odd}+K_{\rm cusp}+B_{\rm prime}+K_{\rm arch\,rem}+K_{\rm pole},
\]

with

\[
(D_{\log})_{nn}=\log(n/4),\qquad n=1,3,5,\ldots.
\]

## 2. Permanent noncompact tail costs

The odd Hilbert term is

\[
(H_{\rm odd})_{mn}=\frac1{m+n},
\]

which is one-half the classical Hilbert matrix after odd-mode reindexing. Therefore

\[
\boxed{\|H_{\rm odd}\|=\pi/2.}
\]

The prime-power ramp operator remains a finite sum of truncated shifts. Its exact triangle bound is

\[
\boxed{
\|B_{\rm prime}\|
\le
2\left(
\frac{\log2}{\sqrt2}
+\frac{\log3}{\sqrt3}
+\frac{\log2}{2}
+\frac{\log5}{\sqrt5}
+\frac{\log7}{\sqrt7}
\right)
\approx5.85246836435.
}
\]

These two pieces are not expected to vanish under high-mode compression, so v13.304 retains their full bounds.

## 3. Exact rank-one structure of the pole term

The pole source is

\[
p(t)=-8(\cosh(t/2)-1).
\]

After two integrations by parts,

\[
-p''(x-y)=2\cosh((x-y)/2).
\]

Using

\[
2\cosh\frac{x-y}{2}
=2\cosh\frac x2\cosh\frac y2
-2\sinh\frac x2\sinh\frac y2,
\]

and restricting to the even-v sector, the odd sinh component drops out. Thus the pole operator is rank one on this sector.

For normalized odd Dirichlet mode \(\psi_n\),

\[
\left|\langle \psi_n,\cosh(x/2)\rangle\right|
\le \frac{4\cosh(1/2)}{\pi n}.
\]

Hence on the tail n>=N,

\[
\boxed{
\|P_NK_{\rm pole}P_N\|
\le
\frac{32\cosh^2(1/2)}{\pi^2}
\sum_{\substack{n\ge N\\ n\,\mathrm{odd}}}\frac1{n^2}.
}
\]

Using the elementary tail estimate

\[
\sum_{\substack{n\ge N\\n\,\mathrm{odd}}}\frac1{n^2}
\le \frac1{N^2}+\frac1{2N},
\]

the pole tail is O(1/N).

## 4. Tail-localized cusp correction

From v13.302,

\[
K_{mn}=-\frac{2}{\pi^2mn}+E_{mn}
\]

for distinct odd m,n, with

\[
|E_{mn}|
\le
\frac{2}{\pi}
\frac{n d_m+m d_n}{|m^2-n^2|},
\qquad
 d_j\le \frac{c}{j^3},
\]

where

\[
c=\frac{2}{\pi^3}+\frac{6}{\pi^4}.
\]

Localizing the v13.302 Hilbert-Schmidt estimates gives

\[
\|P_NK_{\rm cusp}P_N\|
\le \|P_NK_{\rm cusp}P_N\|_{HS},
\]

with an explicit sum of:

1. rank-one tail
\[
\frac{2}{\pi^2}
\left(\frac1{N^2}+\frac1{2N}\right),
\]

2. off-diagonal error tail controlled by
\[
2\alpha\sqrt{\frac{\pi^2}{12}
\left(\frac1{N^6}+\frac1{10N^5}\right)},
\]

3. diagonal tail controlled by
\[
C_{\rm diag}
\sqrt{\frac1{N^4}+\frac1{6N^3}}.
\]

Thus the compact cusp correction now contributes an explicitly vanishing tail cost.

## 5. Fully analytic archimedean-remainder bound

The v13.299 series is

\[
r(t)=\frac14\sum_{m\ge2}
\zeta(2-m,1/4)\frac{(-2)^m}{m!}t^m.
\]

For m>=3,

\[
\zeta(2-m,1/4)=-\frac{B_{m-1}(1/4)}{m-1}.
\]

Using the Fourier bound for Bernoulli polynomials,

\[
|B_k(x)|\le\frac{2k!\zeta(k)}{(2\pi)^k},\qquad k\ge2,
\]

one obtains, with \(q=2/\pi\),

\[
\int_0^2|r''(t)|dt
\le
\frac12+\sum_{k\ge2}\frac{\zeta(k)q^k}{k}.
\]

The standard log-Gamma expansion gives

\[
\sum_{k\ge2}\frac{\zeta(k)q^k}{k}
=\log\Gamma(1-q)-\gamma q.
\]

Therefore

\[
\boxed{
\int_0^2|r''(t)|dt
\le
\frac12+\log\Gamma\!\left(1-\frac2\pi\right)-\frac{2\gamma}{\pi}
\approx1.02816934281.
}
\]

The symmetric Schur estimate is then

\[
\boxed{
\|K_{\rm arch\,rem}\|
\le2.05633868561.
}
\]

This is looser than the earlier numerical value ~1.31476, but unlike that number it comes from a closed analytic majorant rather than a finite numerical truncation.

## 6. Tail coercivity inequality

For odd-mode vectors supported on n>=N,

\[
\langle A_{\rm even}c,c\rangle
\ge
\left[\log(N/4)-C_{\rm tail}(N)\right]\|c\|_2^2,
\]

where

\[
C_{\rm tail}(N)
=\frac\pi2
+5.85246836435
+2.05633868561
+\|P_NK_{\rm cusp}P_N\|
+\|P_NK_{\rm pole}P_N\|.
\]

The first odd cutoff found by these conservative analytic estimates is

\[
\boxed{N=52363.}
\]

At this cutoff the individual localized corrections are approximately

\[
\|P_NK_{\rm cusp}P_N\|\lesssim1.95\times10^{-6},
\]

\[
\|P_NK_{\rm pole}P_N\|\lesssim3.94\times10^{-5},
\]

and

\[
C_{\rm tail}(52363)\approx9.47964632585.
\]

The logarithmic diagonal floor exceeds this by about

\[
1.48\times10^{-5}.
\]

So

\[
\boxed{
\langle A_{\rm even}c,c\rangle>0
\quad\text{for all nonzero odd-mode tail vectors supported on }n\ge52363.
}
\]

This improves the v13.303 sufficient cutoff from roughly 5.56 million modes to roughly 52 thousand modes while simultaneously strengthening the archimedean proof status.

## 7. Interpretation

This is an infinite-dimensional tail statement. It means that any zero or negative direction in this even-v sector must involve the finite low-mode region below the certified tail cutoff.

It does NOT prove:

- that such a zero direction exists;
- \(\ker G_1\ne\{0\}\);
- \(\lambda_1=0\);
- RH or GRH.

The finite low-mode problem remains the difficult part.

## 8. Next checkpoint

v13.305 should target the remaining large constant, the prime-shift contribution. Two useful directions are:

1. replace the triangle bound \(\|B_{\rm prime}\|\le5.85247\) by a joint-symbol or matrix norm bound exploiting cancellation between the five shifts;
2. derive a tail-localized bound for the analytic archimedean remainder rather than retaining its full global Schur norm.

Either improvement could lower the explicit cutoff by orders of magnitude.

## 9. Files

- `research-notes/suzuki_tail_localized_coercivity.py`
- this ledger entry
