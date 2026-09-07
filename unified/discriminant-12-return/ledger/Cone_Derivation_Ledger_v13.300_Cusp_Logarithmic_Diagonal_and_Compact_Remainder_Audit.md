# Cone Derivation Ledger v13.300 — Cusp Logarithmic Diagonal and Compact-Remainder Audit

**Status:** CUSP OFF-DIAGONAL STRUCTURE ISOLATED; FINITE HIGH-MODE RESIDUAL NORMS DECAY; COMPACT-REMAINDER INTERPRETATION NUMERICALLY SUPPORTED BUT NOT PROVED. RH/GRH NOT PROVED.

## 1. Purpose

v13.299 reduced every smooth source contribution to a bounded L2 operator, leaving the singular local cusp

\[
s(t)=\frac12 t\log t + A t,
\qquad
A=\frac12(\log(2\pi)+\gamma-1)
\]

as the only unresolved source of unbounded high-mode growth in the even-v sector. v13.300 asks whether the cusp operator itself has the form

\[
C = D_{\log}+R,
\qquad
(D_{\log})_{nn}=\log n-\log4,
\]

with R bounded or compact.

## 2. Exact linear-term simplification

For \(v\in H_0^1(-1,1)\),

\[
\iint v'(x) A|x-y| v'(y)\,dx\,dy
= -2A\|v\|_2^2.
\]

Thus the linear \(At\) term is exactly diagonal in every orthonormal Dirichlet basis. Consequently all off-diagonal cusp structure comes from

\[
\frac12 |x-y|\log|x-y|.
\]

This is useful because it isolates the genuinely singular part without mixing it with the regular linear correction.

## 3. Cusp matrix

For odd Dirichlet modes \(m,n\), the one-dimensional reduction from v13.290 gives

\[
C_{mn}=\int_0^2 s(t)S_{mn}(t)\,dt,
\]

with the exact analytic overlap \(S_{mn}\). The v13.300 control evaluates these entries using the endpoint change \(t=2u^2\), which resolves the logarithmic cusp numerically.

The residual matrix is

\[
R_{mn}=C_{mn}-\delta_{mn}(\log n-\log4).
\]

## 4. Representative off-diagonal entries

The cusp off-diagonal entries decrease strongly at high mode number. Representative values are

\[
C_{1,3}\approx-0.3088441,
\]

\[
C_{3,5}\approx-0.1381431,
\]

\[
C_{9,11}\approx-0.0520385,
\]

\[
C_{31,33}\approx-0.0158230,
\]

\[
C_{31,35}\approx-0.0153382,
\]

\[
C_{31,41}\approx-0.0140483.
\]

This is consistent with a boundary/Hankel-type correction whose strength decays as both frequencies move outward.

## 5. Finite-section residual norm audit

Using the first 30 odd modes \(n=1,3,\ldots,59\), the full residual spectral norm is approximately

\[
\|R\|_2\approx1.1651.
\]

More importantly, nested high-mode tail blocks show clear norm decay:

\[
\|R_{n\ge11}\|_2\approx0.4294,
\]

\[
\|R_{n\ge21}\|_2\approx0.2713,
\]

\[
\|R_{n\ge31}\|_2\approx0.1732,
\]

\[
\|R_{n\ge41}\|_2\approx0.1019.
\]

The corresponding maximum absolute row sums also decrease:

\[
0.6254,\ 0.3457,\ 0.2022,\ 0.1113.
\]

This is stronger than simple boundedness. In finite sections it is numerically consistent with

\[
R=C-D_{\log}
\]

being compact, because the norm of the high-mode compression appears to tend to zero.

## 6. What is established and what is not

Established exactly:

- the linear \(At\) part is purely diagonal with value \(-2A\);
- the full cusp matrix has the exact one-dimensional overlap representation;
- the logarithmic diagonal model is the correct leading diagonal behavior from v13.298.

Established numerically:

- finite high-mode compressions of \(C-D_{\log}\) have rapidly decreasing spectral norms through odd mode 59;
- representative off-diagonal entries decrease strongly at high frequency.

Not established:

- a rigorous formula proving \(C-D_{\log}\) is compact;
- a certified infinite-tail operator norm bound;
- a complete coercivity theorem for the Suzuki tail;
- \(\ker G_1\neq\{0\}\), \(\lambda_1=0\), RH, or GRH.

## 7. Updated operator picture

Combining v13.298-v13.300 gives the evidence-backed structural model

\[
A_{\rm even}
= D_{\log}
+ R_{\rm cusp}
+ B_{\rm prime}
+ K_{\rm smooth},
\]

where

\[
D_{\log}=\operatorname{diag}(\log n-\log4),
\]

\(B_{\rm prime}\) is bounded by the exact shift-operator argument of v13.298,
\(K_{\rm smooth}\) is bounded by the regularity reduction of v13.299, and
\(R_{\rm cusp}\) is numerically consistent with compactness.

If compactness of \(R_{\rm cusp}\) can be proved, then the high-mode tail becomes a diverging diagonal plus bounded/compact perturbations, which is the right framework for a rigorous tail-coercivity statement.

## 8. Next checkpoint

v13.301 should derive an explicit closed or semi-closed formula for \(C_{mn}\) in terms of the sum and difference frequencies \(m\pm n\), likely involving sine/cosine-integral expressions. The goal is to prove an estimate of the form

\[
|R_{mn}|\le \frac{C}{m+n}+\frac{C'}{1+|m-n|}\,\eta_{mn},
\]

with enough decay to imply compactness or at least vanishing high-mode compression norm.

## 9. Files

- `research-notes/suzuki_cusp_offdiagonal_audit.py`
- this ledger entry
