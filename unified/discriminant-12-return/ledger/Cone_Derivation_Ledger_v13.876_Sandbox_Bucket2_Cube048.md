# Cone Derivation Ledger v13.876 — Sandbox Bucket 2: CUBE-048 — Twisted Convolution Identity (Corrected); "No Area" Made Exact; Kink/Hyperbola Duality; 12-Correspondence Refuted; Nesting Coordinates

Date: 2026-09-29

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[D]** exact identities and geometry; **[N]** verified numbers; **[I]/[O]** interpretation. No RH/positivity/Hilbert–Pólya claim.

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by request and with the authorization of the project owner. Full report (for-review, not part of this repo): `~/workspace/d12/lane_b/sandbox/runs/20260929-cube048/CUBE048_Report_ForReview.md` (+ scripts, data).

Parents: v13.875 (WH-EDGE — the kink deltas this entry grounds arithmetically), v13.872 Part A (the three objects; all results here concern object (iii), the χ₁₂-twisted sandbox summand).

Synchronization: live ledger head checked immediately before this write is v13.875. No collision on the present version number. **This entry does not audit v13.875 or earlier.**

## Origin

The project owner observed that the kink deltas at \(t_m = \log m\) (v13.875 §1) resonate with the \(n\log n\) hyperbolic area — the diamond/square under the hyperbola projecting as a "rest square/cube" alongside the rest circle/sphere projection, the Penrose double cone as a cube inside the sphere. This entry develops that thread with full [D]/[I]/[O] discipline. The exact anchor: \(\sum_{n\le x}\log n = \sum_{d\le x}\Lambda(d)\lfloor x/d\rfloor\) — the \(x\log x\) area assembled from Λ-supported (prime-power = kink-location) atoms via Dirichlet convolution.

## 1. The twisted convolution identity — stated form refuted, corrected form proved [D/N]

The identity as first posed, \(\sum_{n\le x}\chi_{12}(n)\log n = \sum_{d\le x}\chi_{12}(d)\Lambda(d)\lfloor x/d\rfloor\), is **false** for the twisted case — numerics refuted it (residual \(1.4\times10^5\) at \(x = 3\times10^5\)). The inner sum must be the character summatory, not the floor. **Corrected identity (★):**

\[
\sum_{n\le x}\chi_{12}(n)\log n \;=\; \sum_{d\le x}\chi_{12}(d)\Lambda(d)\,M(x/d), \qquad M(y) = \sum_{m\le y}\chi_{12}(m).
\]

**Proof [D]:** one line. \(\chi_{12}\) is completely multiplicative, so \(\chi_{12}(n) = \chi_{12}(d)\chi_{12}(n/d)\) for \(d\mid n\), and \((\chi_{12}\Lambda)\ast\chi_{12} = \chi_{12}\cdot\log\) follows from \(\Lambda\ast 1 = \log\). **Numerical verification [N]:** (★) holds to \(3.6\times10^{-12}\) at \(x = 3\times10^5\); the untwisted floor version verifies to \(9.9\times10^{-8}\) on the same machinery, so the refutation of the twisted floor form is not a code artifact.

**"No area" made exact [D/N]:** the twisted strips have **bounded** height \(|M|\le 1\) (computed) where the untwisted strips grow as \(\lfloor x/d\rfloor\). The owner's "rest square has no area, only oscillation" is not approximate — it is exact at the level of the summatory weights. Main-term cancellation confirmed numerically: \(|S_{tw}(x)|\lesssim 1.1\log x\) (global max 13.93 at \(x = 3\times10^5\)) vs the untwisted \(x\log x - x\) matching to 7.4.

## 2. The fluctuation decomposes into character ripple + zero spectrum [N/I]

Two scales found in \(S_{tw}\): (a) **character ripple** — an approximate period-300 pattern cycling \(+10.2/-1.3/-12.8\), 49,983 zero-crossings, purely arithmetic; (b) **zero oscillation** — Gaussian-smoothed FFT peaks at \(f \approx 0.55, 1.09, 1.37\) cycles/log-\(x\) with decaying amplitudes \(218\to 50\to 14\to 1\), sitting on the independently computed \(L(s,\chi_{12})\) zero frequencies \(\gamma_1/2\pi = 0.6055\), \(\gamma_2/2\pi = 1.0651\), \(\gamma_3/2\pi = 1.4150\) (FFT bin width 0.137; 36 zeros in \((0,60)\), complete per \(N(T)\), Newton-refined to \(|L| < 10^{-7}\); first \(\gamma_1 = 3.8046\)). **Honest caveats [O]:** one unmatched FFT peak at \(f = 0.41\) (likely window leakage); the match is at the bin-width level — recorded as [N]/[I], suggestive, not established.

**Kink connection [D/N]:** \(\psi_{tw}(x) = \sum_{p^k\le x}\chi_{12}(p^k)\log p\) jumps **exactly** at prime powers with size \(\chi_{12}(p^k)\log p\) (verified: \(25\to+1.6094\), \(49\to+1.9459\), \(27\to 0\)). Under \(x = e^t\) these are the v13.875 kink locations, with t-domain strengths \(c_m = \chi(m)\Lambda(m)/\sqrt{m}\) carrying the \(1/\sqrt{m}\) critical-line normalization. \(\psi_{tw}\) oscillates in \([-495,+444]\) at \(x = 3\times10^5\) vs \(\psi_1 \sim x\). The WH-EDGE kink arithmetic is the log-side shadow of this object.

## 3. Hyperbola geometry [D/N]

The Dirichlet split (tails + central square \([1,\sqrt{x}]^2\)) verified to \(10^{-13}\) for twisted and untwisted alike. The square term \(F(\sqrt{x})G(\sqrt{x})\): **twisted oscillates \(\pm 20\) around 0** (sampled: 4.21, 17.40, −9.43, 21.84, −6.30) **vs untwisted \(\approx x\)** (9404.5 → 297046.7). The twisted "rest square" contains no area, only fluctuation — the owner's picture, as numbers.

## 4. The nesting — exact coordinates, one correction [D/I]

Unit sphere ⊃ inscribed cube (vertices \((\pm 1/\sqrt{3})^3\)) ⊃ equatorial square ⊃ circumcircle of radius **\(\sqrt{2/3}\approx 0.8165\)**. **Correction [D]: the circumcircle is a small circle, NOT a great circle** — recorded plainly, since the thread began with the great-circle reading. It remains consistent with the owner's corrected double-cone geometry (cones share the SU(2) circle as base; the geometry permits a latitude circle). **Orientation freedom [D]:** 3 choices of polar 4-fold axis × roll \(\theta\in S^1\) (roll preserves squareness, verified). **Interpretation [I]:** the owner's axis lock (GM = Y polar, Larmor about Y) fixes the axis choice, leaving exactly the \(S^1\) roll — the natural reading is roll ≡ Larmor phase freedom. Suggested, not derived.

## 5. The twelve — refuted in natural form [D/O]

All verified computationally: (a) the 12 edge-midpoints project equatorially to **8 distinct angles** (multiples of 45°), not 12; (b) the binary octahedral group \(2O\) (constructed as 48 unit quaternions, closure checked) has element orders \(\{1,2,3,4,6,8\}\) — **no element of order 12**, so \(C_{12}\not\subset 2O\) and the 12 nodes cannot sit in the cube's binary symmetry group; (c) the preimage of the coordinate Klein four in \(2O\) is **\(Q_8\) (non-abelian), not \(V_4\)** — "48/4 = 12 via \(V_4\)" is false; correctly \(12 = |O|/|\mathrm{Stab}(\text{edge})| = 24/2\). **Verdict [O]: the two 12s are independent** — 12 edges from octahedral combinatorics, 12 nodes from 12th roots with the Galois \(V_4 = (\mathbb{Z}/12)^\times\) action (verified: every non-identity unit squares to 1 mod 12). No natural equivariant edges→nodes map found; both natural candidates fail. 12 is just 12, pending a subtler map (the icosahedron's 12 vertices unexplored).

## 6. The duality, with its mechanism [I/D]

Clean sorting: **continuous side** (SU(2) rotations, Larmor frequencies, Casimir J amplitudes, \(A_{12}(t)\), zeros \(\rho\), smooth test functions) vs **discrete side** (12 nodes as roots of unity, kink positions \(\log m\), hyperbola lattice + diamond, prime powers, Λ weights, kink deltas, Galois \(V_4\)). **[D] mechanism:** the log is the additive coordinate of the multiplicative group (Haar measure \(dx/x\) made additive) — which is why the kinks sit at \(\log m\) and the area accumulates \(\log\). The explicit formula is the unconditional bridge (\(\sum_\rho = \sum_{p,k} + \text{archimedean}\)); the twisted case is its purest form, both sides pure fluctuation. **Creed applied:** the cone selects the duality (the formula is unconditional); the cube picture, the 12-map, and roll≡phase are permitted, not selected.
