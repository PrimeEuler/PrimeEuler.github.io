# Cone Derivation Ledger v13.295 — Parity-Reduced H1 Extension to 20 Modes

**Status:** PARITY-REDUCED HIGH-PRECISION FINITE-SECTION EXTENSION — LOWEST EVEN-v RITZ CANDIDATE TRACKED THROUGH M=20 — POST-M=12 H1 DIFFERENCES DECREASE STRONGLY — NUMERICAL STRONG-H1 CONVERGENCE SUPPORTED BUT NOT PROVED — RH/GRH NOT PROVED

## 1. Purpose

v13.294 established that the Suzuki a=1 near-null Ritz sequence is low-frequency and H1-bounded through M=14, but the successive H1 differences were not yet monotone enough to call the sequence numerically Cauchy.

v13.295 exploits the exact parity decomposition.  In the direct Dirichlet variable v, the observed lowest branch lies in the even-v sector, corresponding to odd mode numbers

\[
n=1,3,5,\dots.
\]

Restricting the matrix to this block roughly halves the dimension and allows a high-precision extension through M=20.

This is a numerical finite-section audit.  None of the results below proves a nontrivial kernel of G_1, lambda_1=0, RH, or GRH.

## 2. Exact parity reduction

At a=1,

\[
\psi_n(x)=\sin\!\left(\frac{n\pi(x+1)}2\right).
\]

For odd n=2j+1,

\[
\psi_{2j+1}(x)=(-1)^j\cos\!\left(\frac{(2j+1)\pi x}{2}\right),
\]

so odd Dirichlet indices span the even-v sector.  Because the kernel is even under x -> -x, the even and odd v sectors decouple exactly.

The v13.295 control therefore assembles only the odd-index block and computes all smaller mode counts as principal submatrices of the largest M=20 block.

## 3. Lowest finite Ritz values and derivative norms

Using arbitrary-precision matrix assembly with the same pole/prime/archimedean source decomposition as v13.291-v13.294 gives:

| M | lowest even-v Ritz value | ||Dv_M||_2 |
|---:|---:|---:|
| 6  | 3.23765425890539e-11 | 2.53158292071049 |
| 8  | 1.41673165707955e-12 | 2.81643648919963 |
| 10 | 1.23215811746107e-13 | 2.84421762549673 |
| 12 | 1.82275268672806e-15 | 2.97886840027967 |
| 14 | 4.52234990685279e-17 | 3.07033965781033 |
| 16 | 8.31579174921404e-19 | 3.15046593621518 |
| 18 | 3.99064640493536e-20 | 3.20884094046407 |
| 20 | 1.12389415798953e-20 | 3.23024819326202 |

The derivative norm grows slowly and remains O(1).  There is no numerical indication of the norm growth expected from a sequence escaping into higher and higher frequencies.

The finite Ritz values remain positive at working precision through M=20.  They are finite-dimensional upper bounds only and do not establish lambda_1>0.  Conversely, their collapse toward zero does not establish lambda_1=0.

## 4. Nested-space Cauchy diagnostics

For sign-aligned nested candidates, define

\[
\delta v_{M,N}=v_N-v_M,
\]

where v_M is zero-padded into the larger basis.  Since the Dirichlet basis is L2-orthonormal and diagonalizes the derivative seminorm,

\[
\|\delta v\|_2^2=\sum_n|\delta c_n|^2,
\qquad
\|D\delta v\|_2^2=\sum_n k_n^2|\delta c_n|^2.
\]

The measured successive differences are:

| step | embedded overlap | L2 difference | derivative difference | relative u difference |
|---:|---:|---:|---:|---:|
| 6 -> 8   | 0.99687279689165 | 7.90848e-2 | 4.98840e-1 | 1.77117e-1 |
| 8 -> 10  | 0.99997449622877 | 7.14196e-3 | 4.45773e-2 | 1.56730e-2 |
| 10 -> 12 | 0.99943246109952 | 3.36909e-2 | 2.17838e-1 | 7.31277e-2 |
| 12 -> 14 | 0.99975701080947 | 2.20449e-2 | 1.46544e-1 | 4.77290e-2 |
| 14 -> 16 | 0.99982328001816 | 1.88000e-2 | 1.27039e-1 | 4.03240e-2 |
| 16 -> 18 | 0.99990994042638 | 1.34208e-2 | 9.21338e-2 | 2.87125e-2 |
| 18 -> 20 | 0.99998815931578 | 4.86635e-3 | 3.37444e-2 | 1.04464e-2 |

## 5. Interpretation of the M=10 -> 12 rebound

The v13.294 concern was the rebound in the derivative difference at M=10 -> 12:

\[
0.0446\to0.2178.
\]

The extended sequence now shows that this does not persist.  From M=12 onward,

\[
0.1465,\ 0.1270,\ 0.0921,\ 0.0337
\]

is a clear decreasing trend in the derivative difference, while the L2 differences similarly decrease:

\[
0.0220,\ 0.0188,\ 0.0134,\ 0.00487.
\]

The corresponding overlaps approach one, reaching approximately

\[
0.99998816
\]

for M=18 -> 20.

Thus the simplest numerical interpretation is now that the M=10 -> 12 rebound was a finite-mode correction within an otherwise stabilizing low-frequency branch.

## 6. What v13.295 strengthens

The combined v13.291-v13.295 evidence now has four mutually consistent features:

1. high-precision finite Ritz values remain positive while collapsing rapidly toward zero;
2. the corresponding vectors remain low-frequency and centrally concentrated rather than boundary-localized;
3. independent off-grid P_1 G_1 u_M residuals decrease strongly through the range already tested;
4. the parity-reduced sequence through M=20 now shows decreasing post-M=12 L2 and derivative differences.

This is substantially stronger numerical evidence for a genuine limiting kernel candidate than was available at v13.294.

## 7. What remains open

The data do **not** yet prove that the sequence is Cauchy in H0^1.  A finite decreasing tail of successive differences is evidence, not a convergence theorem.  To obtain a legitimate limiting argument one still needs, at minimum, one of:

- a certified summable bound on the coefficient tail;
- a contraction or recurrence controlling the odd-mode coefficients;
- a rigorous residual estimate plus an operator-theoretic compactness/closedness argument that identifies a nonzero limit;
- interval or otherwise certified arithmetic excluding sign/cancellation ambiguity in the decisive tail.

Exact lambda_1=0 remains unproved.  No RH or GRH conclusion is claimed.

## 8. New control file

`research-notes/suzuki_parity_reduced_h1_extension.py`

The script assembles the M=20 even-v block once, extracts all nested principal subproblems, and reports the derivative norms and Cauchy diagnostics above.

## 9. Next checkpoint

The next useful audit is not simply M=22,24,... .  v13.296 should examine the stabilized odd-mode coefficient tail itself and ask whether it obeys a quantitative decay law or recurrence strong enough to control

\[
\sum_n n^2|c_n|^2
\]

and the H1 tail.  A demonstrable exponential/superalgebraic tail or a source-derived coefficient recurrence would turn the present convergence evidence into a route toward a certified limiting argument.
