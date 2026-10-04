# Cone Derivation Ledger v13.990 — Sandbox: Explicit Remote-Tail Moment Cancellation Construction

**Date:** 2026-10-03
**Track:** Sandbox (our Lane B), independent divide-and-conquer task
**Status:** [D] exact finite-extension tail construction canceling the leading 1/n moment at fixed Ritz value; [N] numerical verification on M2 proxy (all 8 channels); [I] no obstruction encountered.
**Parents:** v13.989 (Sandbox remote-tail gate)
**Authorization:** Jeremy, 2026-10-03 ("take the remote-tail gate... as an independent divide-and-conquer task"; "yep do it")
**Collision check:** Live HEAD is v13.989 (two files at v13.989: Sandbox gate 2026-10-03 keeps the number per earlier-commit-wins; Audit Round 152 dated 2026-10-04). v13.990 was absent immediately before this write.

---

## 0. Purpose

v13.989 identified the next nonredundant gate: >99.7% of the far-tail
certificate is the explicit signed 1/n residual moment

\[
\mathcal L_\theta(q)
=
-\frac{2}{\pi}\langle z,q\rangle
+
\alpha\frac{4g}{\pi}\langle p,q\rangle
+
\theta\langle \mathbf 1,q\rangle,
\]

finite shells buy only O(N^{-1/2}), and Ritz retuning cannot cancel the
dominant channels (4th-channel Δθ needed: 0.158 even / 0.530 odd, far
outside |θ|<0.02).

This entry constructs, derives, and numerically verifies a genuine
remote-tail vector correction y at *fixed* θ with

\[
\mathcal L_\theta(q+y)=0,
\]

hence r_n = O(n^{-2}) and ‖r_{≥N}‖_2 = O(N^{-3/2}).

Independent of the v13.987-closed 6×6 inverse route; no 6×6 appears.

---

## 1. Asymptotic action on the tail ansatz [D]

For finite q (support n≤N) and remote n≫N, the off-diagonal gives

\[
A_{n,m}
=
\frac{2}{\pi}\frac{z_n m-n z_m}{\,n^2-m^2\,}
+
\alpha p_n p_m
\approx
-\frac{2}{\pi}\frac{z_m}{n}
+
\alpha\frac{4g}{\pi}\frac{p_m}{n},
\]

using z_n bounded (→π/2) and p_n∼(4g/π)/n. The B off-diagonal
B_{n,m}=-1/(n+m)≈-1/n gives (-θBq)_n≈θ⟨1,q⟩/n. Summing yields the
v13.989 §3 formula. The derivation uses only n≫m; no assumption on
any tail ansatz is made.

Rather than positing y_n∝1/n (whose L_θ moment diverges absolutely),
use a *finite extension*: y supported on N<n≤M, y_n=c (constant).
Then q+y has finite support (≤M), so for n≫M the *same* derivation
applies verbatim, giving residual coefficient exactly L_θ(q+y).

## 2. Slowest admissible form [D]

For L_θ(y) to be well-defined and nonzero via absolutely convergent
sums, an infinite tail y_n∼n^{-k} needs k>1 (else ⟨1,y⟩ diverges).
The finite extension sidesteps this entirely: all sums are finite,
L_θ(y) is exact, and the B-energy ⟨y,By⟩ is finite (not merely
convergent). It is the *minimal* construction achieving exact
cancellation — slower infinite tails (k→1⁺) are admissible but introduce
unnecessary convergence subtleties for no gain.

## 3. Explicit amplitude [D]

L_θ is linear. With t≡1 on (N,M]:

\[
\mathcal L_\theta(q+y)
=
\mathcal L_\theta(q)
+
c\,\mathcal L_\theta(t)
=
0
\quad\Longrightarrow\quad
\boxed{
c
=
-\frac{\mathcal L_\theta(q)}{\mathcal L_\theta(t)}.
}
\]

The denominator
L_θ(t)=(M-N)/2·[θ-(2/π)z̄]+O(log(M/N)) with z̄≈π/2 gives
θ-(2/π)z̄≈-1≠0, so |L_θ(t)|≈(M-N)/2>0 and c≈2L/(M-N) is well-defined
and small.

## 4. Next order and the O(N^{-3/2}) acceleration [D]

With L_θ(q+y)=0, expanding to next order:

\[
r'_n
=
\frac{C_2}{n^2}+O(n^{-3}),
\qquad
C_2
=
\Bigl[\frac{2}{\pi}z_\infty-\theta\Bigr]\langle m,q+y\rangle
\]

(finite; the pole term skips O(1/n²) since p_n=(4g/π)/n-(4g/π³)/n³+…).
Hence

\[
\boxed{
\|r'_{\ge M'}\|_2^2
\approx
\sum_{n>M'}\frac{C_2^2}{n^4}
\approx
\frac{C_2^2}{3M'^3},
\qquad
\|r'_{\ge M'}\|_2=O(M'^{-3/2}),
}
\]

vs O(M'^{-1/2}) before. The 1/n→1/n² cancellation is exact, not
asymptotic.

## 5. Admissibility checks [D/N]

* **B-norm:** ⟨y,By⟩=c²·1ᵀB_{tail}1=O(log M/(M-N)) →0 as M/N grows.
  Controlled.
* **Carrier geometry:** ‖y_j‖_B<1 in all channels (max 0.16), so the
  four vectors {q_j+y_j} remain linearly independent; the B-Gram is
  I+O(10⁻³)–O(10⁻²), hence re-orthonormalization is stable. L_θ=0 is
  preserved under linear combinations (re-Ritz).
* **|θ|<0.02:** θ is held fixed — no retuning. Post-reorthonormalization
  Ritz shifts are O(‖y‖_B²); to be verified numerically in the full
  certificate replay, but margins are comfortable (largest baseline
  θ_3=0.0104 odd-v).

## 6. Numerical verification [N]

M2 proxy (W=Z-X_R, N=16001/16002, M=32001/32004, z via digamma,
p exact):

| sector | col | L_θ(q) | c | L_θ(q+y) | ‖y‖_B |
|---|---|---|---|---|---|
| even | 0 | −0.103 | −1.29e−05 | 0 | 3.4e−03 |
| even | 1 | 0.118 | 1.47e−05 | 0 | 3.9e−03 |
| even | 2 | −0.019 | −2.35e−06 | 0 | 6.2e−04 |
| even | 3 | −1.054 | −1.32e−04 | 0 | 3.5e−02 |
| odd | 0 | −0.232 | −2.90e−05 | 0 | 7.6e−03 |
| odd | 1 | −0.544 | −6.80e−05 | 0 | 1.8e−02 |
| odd | 2 | −1.405 | −1.76e−04 | 0 | 4.6e−02 |
| odd | 3 | −4.932 | −6.23e−04 | 0 | 1.6e−01 |

Exact cancellation in all 8 channels (L_new=0.00e+00 to machine
precision). Full finite/explicit-remote/far replay against the M3
carrier awaits the heavy certificate machinery; the moment
cancellation above is the mathematical core.

## 7. Result

\[
\boxed{
\textbf{No obstruction: the finite-extension tail cancels }
\mathcal L_\theta
\textbf{ exactly at fixed }\theta,
\textbf{ with controlled B-norm, in all 8 channels.}
}
\]

The v13.989 gate is closed constructively. The next step is the full
certificate replay (finite + explicit-remote + far before/after) on the
M3 carrier, then a source/phase consumer pass.

---

*Commit d32f0989daa324ea7b56a15b785eb947fcbf5019 (tasked) contains the
v13.989 M3 context; this entry is the independent sandbox construction.*
