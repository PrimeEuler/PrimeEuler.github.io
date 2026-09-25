# Cone Derivation Ledger v13.810 — Outward Endpoint Remote-Tail Floors at \(4001/4002\) and Combined Frozen Finite-Side Margins

Date: 2026-09-25

Lane: A.

Status: [C] outward interval tail-floor certificate for the \(\rho=0.10\) minus endpoint in both parity sectors; [C] combined terminal lower bounds with the frozen finite-side certificate v13.809; [G] remote residual-Gram ceiling remains the only unresolved load-bearing subtraction.

Parents: v13.363, v13.804, v13.809.

Research artifact:

- research-notes/suzuki_endpoint_M3999_outward_tail_floor_certificate.py
- commit 3a8ecfb6873e21a20131a22913148c1f348f16bf.

The script was dry-run end-to-end before commit with the same interval formulas and PASS thresholds. No GitHub workflow/status run is attached.

## 1. Target endpoint and exact remote starts

The endpoint is
\[
F^-_{0.10}
=
A-0.10B_{\rm sm}.
\]

The remote parity tails start at
\[
\boxed{n=4001}
\]
for even-v and
\[
\boxed{n=4002}
\]
for odd-v.

The v13.804 lower-bound formula is
\[
\gamma_e(N)
=
0.9\left[\log(N/4)-\frac{\pi}{2}\right]
-2.05
-\beta_{\rm cusp}(N)
-\beta_{\rm arch}(N),
\]
and in corrected odd-v
\[
\gamma_o(N)
=
\gamma_e(N)
-
\beta_{\rm pole}(N).
\]

Here
\[
\beta_{\rm pole}(N)
=
\frac{32\sinh^2(1/2)}{\pi^2}
s_2(N),
\qquad
s_2(N)=N^{-2}+\frac1{2N}.
\]

## 2. Outward arithmetic model [C]

All transcendental arithmetic is evaluated with mpmath interval arithmetic at 80 decimal digits.

No interval zeta routine is assumed. Instead
\[
\zeta(3)
=
\sum_{k=1}^{M}\frac1{k^3}
+
\sum_{k>M}\frac1{k^3},
\qquad
M=20000,
\]
with
\[
\frac1{2(M+1)^2}
\le
\sum_{k>M}\frac1{k^3}
\le
\frac1{2M^2}.
\]

Thus every use of \(\zeta(3)\) in the archimedean tail constant is outward enclosed independently.

The same interval context encloses \(\pi\), \(\log\), exponentials, square roots, and
\[
\sinh(1/2)=\frac{e^{1/2}-e^{-1/2}}2.
\]

The prime contribution uses the already validated strict bound
\[
\|B_{\rm prime}\|<2.05.
\]

## 3. Even-v tail at \(N=4001\) [C]

The bulk term lies in
\[
4.80348802884820301080\ldots
\le
0.9\left[\log(4001/4)-\frac\pi2\right]
\le
4.80348802884820301081\ldots.
\]

The adverse tail components satisfy
\[
\beta_{\rm cusp}(4001)
<
0.000025832732302577564,
\]
\[
\beta_{\rm arch}(4001)
<
0.000407769557809603.
\]

Therefore
\[
\gamma_e(4001)
\in
[
2.7530544265580908304947\ldots,
2.7530544265580908645523\ldots
].
\]

Hence
\[
\boxed{
\gamma_e(4001)
>
2.75305442655809082.
}
\]

## 4. Corrected odd-v tail at \(N=4002\) [C]

The bulk term lies in
\[
4.80371294450600233266\ldots
\le
0.9\left[\log(4002/4)-\frac\pi2\right]
\le
4.80371294450600233267\ldots.
\]

The adverse tail components satisfy
\[
\beta_{\rm cusp}(4002)
<
0.000025826212109529260,
\]
\[
\beta_{\rm arch}(4002)
<
0.000407667615471052,
\]
and the corrected negative-pole allowance satisfies
\[
\boxed{
\beta_{\rm pole}(4002)
<
0.000110051117980132.
}
\]

Therefore
\[
\gamma_o(4002)
\in
[
2.7531693995604416206902\ldots,
2.7531693995604416547393\ldots
].
\]

Hence
\[
\boxed{
\gamma_o(4002)
>
2.75316939956044161.
}
\]

## 5. Combination with the frozen finite-side certificate [C]

v13.809 proved
\[
\boxed{
C_+>0.9999992082\,I,
}
\]
\[
\boxed{
C_->0.9999999425\,I.
}
\]

Therefore
\[
\boxed{
\gamma_e C_+
>
2.7530522466895958\,I,
}
\]
and
\[
\boxed{
\gamma_o C_-
>
2.7531692412532011\,I.
}
\]

The finite-side normalization consumes less than
\[
\boxed{
2.18\times10^{-6}
}
\]
of the even-v raw tail floor and less than
\[
\boxed{
1.59\times10^{-7}
}
\]
of the odd-v raw tail floor.

## 6. Exact remaining inequality

The infinite six-plane Schur positivity test is now
\[
H_e<\gamma_e C_+,
\qquad
H_o<\gamma_o C_-.
\]

The right-hand sides are fully outward-certified:
\[
\boxed{
\gamma_e C_+
>
2.7530522466895958\,I,
}
\]
\[
\boxed{
\gamma_o C_-
>
2.7531692412532011\,I.
}
\]

Thus the remote-Gram replay only needs to prove
\[
\lambda_{\max}(H_e)
<
2.7530522466895958,
\]
\[
\lambda_{\max}(H_o)
<
2.7531692412532011.
\]

The midpoint/far-envelope targets from v13.807 are roughly \(0.178\) and \(0.0122\), but those remote-Gram ceilings remain a logically separate outward-certification gate.

## Result

\[
\boxed{
\textbf{The }\rho=0.10\textbf{ endpoint remote tails are rigorously positive from }4001/4002\textbf{ onward.}
}
\]

\[
\boxed{
\gamma_e(4001)>2.75305442655809082,
\qquad
\gamma_o(4002)>2.75316939956044161.
}
\]

After combining with the frozen finite-side certificate,
\[
\boxed{
\gamma_e C_+>2.7530522466895958\,I,
\qquad
\gamma_o C_->2.7531692412532011\,I.
}
\]

The only remaining load-bearing step for the six positive directions at the \(\rho=0.10\) minus endpoint is the outward remote residual-Gram ceiling.
