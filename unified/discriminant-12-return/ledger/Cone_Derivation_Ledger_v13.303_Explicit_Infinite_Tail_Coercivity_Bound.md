# Cone Derivation Ledger v13.303 — Explicit Infinite-Tail Coercivity Bound

**Status:** EXPLICIT HIGH-MODE COERCIVITY ESTIMATE OBTAINED FOR THE a=1 EVEN-v SECTOR. CUTOFF IS VERY CONSERVATIVE. THIS DOES NOT PROVE `ker(G_1) != {0}`, `lambda_1=0`, RH, OR GRH.

## 1. Purpose

v13.302 proved that the corrected cusp remainder is Hilbert–Schmidt. This checkpoint combines all previously isolated pieces into one explicit lower bound on the infinite odd-mode tail.

The operator decomposition is

\[
A_{\rm even}
=
D_{\log}-H_{\rm odd}+K_{\rm cusp}+B_{\rm prime}+K_{\rm smooth},
\]

with

\[
(D_{\log})_{nn}=\log(n/4)
\]

on odd positive mode indices.

## 2. Exact/bounded pieces already established

From v13.301,

\[
(H_{\rm odd})_{mn}=\frac1{m+n},
\qquad
\|H_{\rm odd}\|=\frac\pi2.
\]

From v13.298, the prime-ramp contribution is a finite sum of truncated shifts. The triangle estimate gives

\[
\|B_{\rm prime}\|
\le
2\sum_{q\in\{2,3,4,5,7\}}\frac{\Lambda(q)}{\sqrt q}
\approx 5.85247.
\]

From v13.299, the smooth pole plus archimedean remainder obey the conservative Schur bound

\[
\|K_{\rm smooth}\|
\lesssim
1.31476+4.70080
=6.01556.
\]

## 3. Global Hilbert–Schmidt bound for the cusp correction

v13.302 gave, for distinct odd m,n,

\[
K_{mn}
=-\frac{2}{\pi^2mn}+E_{mn},
\]

and

\[
|E_{mn}|
\le
\frac{2}{\pi}\frac{n d_m+m d_n}{|m^2-n^2|},
\qquad
 d_j\le \frac{c}{j^3},
\]

where

\[
c=\frac{2}{\pi^3}+\frac{6}{\pi^4}.
\]

### 3.1 Rank-one leading term

Because

\[
\sum_{n\ {\rm odd}}\frac1{n^2}=\frac{\pi^2}{8},
\]

the Hilbert–Schmidt norm of the rank-one matrix \(-2/(\pi^2mn)\) is exactly

\[
\frac14.
\]

### 3.2 Off-diagonal remainder

Using

\[
|m^2-n^2|=|m-n|(m+n),
\]

one obtains

\[
|E_{mn}|
\le
\alpha\left(
\frac1{m^3|m-n|}+\frac1{n^3|m-n|}
\right),
\]

with

\[
\alpha=\frac{2c}{\pi}.
\]

For distinct odd indices, \(|m-n|\ge2\). Summing the square bound and using

\[
\sum_{r\ge1}\frac1{(2r)^2}=\frac{\pi^2}{24},
\qquad
\sum_{m\ {\rm odd}}\frac1{m^6}=\frac{\pi^6}{960},
\]

gives the conservative numerical estimate

\[
\|E\|_{\rm HS}<0.146.
\]

### 3.3 Diagonal correction

The v13.302 diagonal estimate is

\[
|K_{nn}|
\le
\frac{2}{x^2}+\frac{2}{x^3}+\frac{2}{x^4}+\frac{6}{x^5},
\qquad x=\pi n.
\]

Thus

\[
|K_{nn}|\le \frac{C_d}{n^2},
\]

where

\[
C_d=
\frac{2}{\pi^2}+\frac{2}{\pi^3}+\frac{2}{\pi^4}+\frac{6}{\pi^5}.
\]

Using

\[
\sum_{n\ {\rm odd}}\frac1{n^4}=\frac{\pi^4}{96}
\]

gives

\[
\|K_{\rm diag}\|_{\rm HS}<0.310.
\]

Combining the three pieces by the triangle inequality,

\[
\boxed{
\|K_{\rm cusp}\|
\le
\|K_{\rm cusp}\|_{\rm HS}
<0.706.
}
\]

The audit script evaluates the bound more precisely as approximately

\[
0.705243.
\]

## 4. Total bounded perturbation

Combining the global bounds gives

\[
C_{\rm pert}
=
\frac\pi2
+5.85247
+6.01556
+0.705243
<14.145.
\]

Therefore, for any coefficient vector supported on odd modes \(n\ge N\),

\[
\langle A_{\rm even}c,c\rangle
\ge
\left(\log(N/4)-C_{\rm pert}\right)\|c\|_2^2.
\]

This is an infinite-dimensional tail estimate, not a finite-section singular-value observation.

## 5. Explicit coercive cutoff

A sufficient condition is

\[
\log(N/4)>C_{\rm pert}.
\]

Using the conservative constants above,

\[
4e^{C_{\rm pert}}
\approx 5.56\times 10^6.
\]

Thus any odd cutoff above this threshold is sufficient. The audit script reports the first odd integer above the computed continuous threshold.

The size of this cutoff is not expected to be sharp. It is large because every bounded component was estimated globally and by triangle inequalities; no tail-localized decay of the compact/smooth pieces was used.

## 6. What this establishes

This checkpoint establishes a concrete mechanism and explicit finite threshold beyond which the infinite odd-mode tail of the a=1 even-v sector is coercive.

The important structural conclusion is

\[
\boxed{
\text{all possible near-zero behavior is confined to a finite-dimensional low-mode window.}
}
\]

That statement is sector-specific and uses the exact/bounded decomposition developed through v13.298–v13.302.

It does **not** establish:

- that a zero eigenvalue exists;
- that the numerical near-null Ritz vector converges to a true kernel vector;
- that \(\lambda_1=0\);
- RH or GRH.

## 7. Why this matters for the next audit

The previous H1-tail problem has changed character. We no longer need to control infinitely many modes by extrapolating coefficient decay alone. The coercivity estimate says the genuinely unresolved spectral problem is finite-dimensional after a sufficiently high cutoff.

The current cutoff is millions of modes and therefore useless computationally as-is, but it provides a rigorous template. The next task is to replace global perturbation bounds by **tail-localized** bounds:

- the Hilbert compression can be bounded more sharply on a tail;
- `K_cusp` has explicit HS tail decay;
- the smooth kernels are compact and should have small high-frequency compressions;
- the prime shift term is the principal bounded noncompact perturbation that remains.

A successful localized estimate could reduce the certified cutoff by orders of magnitude.

## 8. Files

- `research-notes/suzuki_explicit_tail_coercivity_bound.py`
- this ledger entry
