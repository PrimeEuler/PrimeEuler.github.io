# Cone Derivation Ledger v13.391 — Independent Raw Tail Coercivity Revalidation

## Status

**Analytic / validated-input checkpoint.**

This note isolates and revalidates the raw odd-tail lower bound at the
source-faithful split \(N=16003\), without using the audited v13.365 six-plane
cross certificate.

## 1. Tail decomposition

For the pole-free source-faithful operator on odd modes \(n\ge N\), use the
lower bound

\[
A_{0,\,\text{tail}}
\succeq
\left[
\log(N/4)
-\frac{\pi}{2}
-\|B_{\rm prime}\|
-\beta_{\rm cusp}(N)
-\beta_{\rm arch}(N)
\right]I.
\]

The ingredients are:

- exact Hilbert contribution \(\|H_{\rm odd}\|=\pi/2\);
- robust prime target \(\|B_{\rm prime}\|<2.05\) from the v13.363 power-Schur
  certificate;
- explicit source-faithful cusp-tail localization;
- explicit source-faithful smooth archimedean tail localization.

No finite-high / remote-tail cross estimate enters this calculation.

## 2. Explicit localization bounds

For odd \(n\ge N\), define

\[
s_2(N)=N^{-2}+(2N)^{-1},
\]
\[
s_4(N)=N^{-4}+(6N^3)^{-1},
\]
\[
s_6(N)=N^{-6}+(10N^5)^{-1}.
\]

The smooth archimedean remainder obeys

\[
\beta_{\rm arch}(N)
=
C_r\frac{4}{\pi^2}s_2(N),
\]

with

\[
C_r=rac{19}{12}+4\,r_4,
\qquad
r_4=
\frac{\zeta(3)q^3}{4(1-q)^3},
\qquad q=\frac{2}{\pi}.
\]

At \(N=16003\),

\[
\beta_{\rm arch}(16003)
\le
1.0191055832\times10^{-4}.
\]

The cusp localization gives

\[
\beta_{\rm cusp}(16003)
\le
6.3941584001\times10^{-6}.
\]

## 3. Revalidated raw tail gap

Using the deliberately rounded robust prime bound \(2.05\),

\[
\begin{aligned}
\alpha_{16003}
&=
\log(16003/4)
-\frac{\pi}{2}
-2.05
-\beta_{\rm cusp}(16003)
-\beta_{\rm arch}(16003)\\[4pt]
&=4.673332491014484\ldots
\end{aligned}
\]

Therefore

\[
\boxed{A_{0,[16003,\infty)}\succeq4.6732\,I}
\]

under the already stated robust-prime validated-computational input and the
analytic cusp/arch localization estimates.

This recovers the old raw-tail target with roughly

\[
1.32\times10^{-4}
\]

of numerical margin over \(4.6732\).

## 4. What this does and does not repair

This result **does** repair one independent ingredient needed by the terminal
Schur argument: the remote raw tail is strongly coercive.

It **does not** repair the audited v13.365 full-cross estimate
\(\|G\|<0.994\), and therefore does not by itself imply positivity of the full
high complement after coupling the finite high block to the remote tail.

The remaining bottleneck is now sharply identified as the coupling / effective
tail correction, not the raw tail diagonal lower bound.

## 5. Relation to v13.390

v13.390 replaced the overly strong ten-column uniform residual target by the
six-dimensional quadratic condition

\[
\delta_{\rm certified}
>
\lambda_{\max}\!\left(
S_W^{-1/2}R_W^*R_WS_W^{-1/2}
\right).
\]

v13.391 shows that the raw tail entering that construction starts from a large
coercive scale, \(>4.6732\).  The next task is to certify how much of this gap
is lost when the finite high block is eliminated, using a source-faithful
cross/residual calculation rather than the superseded v13.365 projection
claim.

## 6. Code checkpoint

Added:

`research-notes/suzuki_source_faithful_tail_coercivity_revalidation.py`

The script independently recomputes the cusp and arch tail bounds with the
robust \(2.05\) prime input and asserts

\[
\alpha_{16003}>4.6732.
\]

## Guardrails

- No restoration of v13.365 or v13.366.
- No full high-complement positivity claim yet.
- No exact-zero or kernel claim.
- No final inertia theorem.
- No RH or GRH conclusion.
