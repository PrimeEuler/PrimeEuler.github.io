# Cone Derivation Ledger v13.300 — Cusp Logarithmic Diagonal and Compact-Remainder Audit

> **v13.301 correction / supersession note.** The compact-remainder interpretation below is superseded. The exact cusp formula derived in v13.301 shows
> \[
> C-D_{\log}=-H_{\rm odd}+K,
> \qquad (H_{\rm odd})_{mn}=\frac1{m+n},
> \]
> where \(H_{\rm odd}\) is one-half of the classical Hilbert matrix and is bounded but noncompact. The apparent norm decay of high-mode finite compressions in this v13.300 experiment was a finite-window truncation effect. After subtracting the explicit Hilbert term, the new residual \(K\) is the compact/Hilbert-Schmidt candidate. All statements below suggesting that \(C-D_{\log}\) itself may be compact should be read as superseded by v13.301.

**Status:** CUSP OFF-DIAGONAL STRUCTURE ISOLATED; FINITE HIGH-MODE RESIDUAL NORMS DECAY; ORIGINAL COMPACT-REMAINDER INTERPRETATION SUPERSEDED BY v13.301 EXACT HILBERT DECOMPOSITION. RH/GRH NOT PROVED.

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

v13.301 explains the dominant decay explicitly as the Hankel term \(-1/(m+n)\).

## 5. Finite-section residual norm audit

Using the first 30 odd modes \(n=1,3,\ldots,59\), the full residual spectral norm is approximately

\[
\|R\|_2\approx1.1651.
\]

Nested high-mode blocks in that fixed finite window gave

\[
\|R_{n\ge11}\|_2\approx0.4294,
\quad
\|R_{n\ge21}\|_2\approx0.2713,
\]

\[
\|R_{n\ge31}\|_2\approx0.1732,
\quad
\|R_{n\ge41}\|_2\approx0.1019.
\]

The corresponding maximum absolute row sums were

\[
0.6254,\ 0.3457,\ 0.2022,\ 0.1113.
\]

**Superseded interpretation:** these decreasing values do not show that the infinite high-mode compression norm tends to zero. v13.301 identifies a noncompact Hilbert component whose norm is not seen correctly when the upper endpoint of the finite matrix is held fixed while the lower cutoff is moved upward.

## 6. What remains valid

Established exactly:

- the linear \(At\) part is purely diagonal with value \(-2A\);
- the full cusp matrix has the exact one-dimensional overlap representation;
- the logarithmic diagonal model is the correct leading diagonal behavior from v13.298.

Established numerically in v13.300:

- representative off-diagonal entries decrease strongly with frequency;
- fixed-window high-mode compressions shrink, but that observation alone does not determine compactness.

Superseded:

- the inference that \(C-D_{\log}\) itself is compact.

Still not established:

- a fully rigorous infinite-tail coercivity constant;
- \(\ker G_1\neq\{0\}\), \(\lambda_1=0\), RH, or GRH.

## 7. Corrected operator picture from v13.301

The correct leading cusp structure is

\[
C=D_{\log}-H_{\rm odd}+K,
\qquad
(H_{\rm odd})_{mn}=\frac1{m+n}.
\]

With odd indices \(m=2j+1\), \(n=2k+1\),

\[
(H_{\rm odd})_{jk}=\frac1{2(j+k+1)},
\]

so \(H_{\rm odd}\) is one-half the classical Hilbert matrix and

\[
\|H_{\rm odd}\|=\frac\pi2.
\]

The residual \(K\), not \(C-D_{\log}\), is the compact/Hilbert-Schmidt candidate.

## 8. Files

- `research-notes/suzuki_cusp_offdiagonal_audit.py`
- this ledger entry
- superseding analysis: `research-notes/suzuki_cusp_exact_hilbert_decomposition.py`
