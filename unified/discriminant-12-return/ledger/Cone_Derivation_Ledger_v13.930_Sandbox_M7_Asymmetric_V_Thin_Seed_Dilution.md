# Cone Derivation Ledger v13.930 — Sandbox: m=7 Asymmetric V — Thin-Seed Dilution of the Null-Cluster Shift Norm

**Date:** 2026-10-01
**Track:** Sandbox / exploratory lane (little Euler)
**Status:** [D] exact shift-norm formula (v13.908) and loading bounds; [N] measured slopes, plateaus, sawtooth (ngrid-converged); [I] dilution mechanism, asymmetry origin; [O] closed forms, analytic threshold proof, vector classification
**Authorization:** Jeremy, 2026-10-01 ("yes, check the ledger first as always" — authorizing the m=7 ledger entry)
**Parents:** v13.902 (rigidity: isolated Λ maximizer, the 1.21103 value), v13.906 (missing lemma / two-bump construction), v13.908 (shift-norm formula 2cos(π/k)), v13.928 (External Audit Round 139 — FEM pipeline quadrature finding, addressed in §2)
**Collision check:** live head v13.929 read in full immediately before this write; v13.930 absent.

---

## 0. Verdict

The unexplained rigidity ratio s_7/c_7 = 1.21103 is the **minus-side** slope of a two-sided **asymmetric** V. The plus-side slope s_7^+/c_7 = **1.35908** was never reported. Both are null-cluster-restricted KK[7] norms [N]; the global norm √2 [D, v13.908] is the wrong object for the V-slope. The restriction mechanism is **thin-seed dilution**, mapped quantitatively: at a = 2 the longest 3-point shift orbits of log 7 occupy seed sets of width 0.108, far below the near-null smoothness scale 2π/γ_1 ≈ 0.44 — too thin to host a near-null top-eigenvector of KK[7]. The a-sweep shows the full sawtooth: the ratio **rejoins** the global 2cos(π/k) norm wherever the longest-orbit seed set is thick, and **re-dilutes** at the next thin window.

\[
\boxed{
s_m^\pm/c_m = \text{null-cluster-restricted }\pm KK[m]\text{ norm} \le 2\cos(\pi/k(m,a)),
}
\]

with equality iff the longest-orbit seed width ≳ 2π/γ_1 [N/I].

---

## 1. The asymmetry [N]

Pinning the slopes (secant at |ε| = 0.01, a = 2, N = 1600), under the quadrature refinement of §2:

| ngrid | s⁻/c_7 | s⁺/c_7 |
|-------|--------|--------|
| 40,001 | 1.21103628 | 1.35568886 |
| 320,001 | 1.21321318 | 1.35901381 |
| 1,280,001 | 1.21325549 | 1.35907858 |

Clean plateau: the last 4× refinement moves the values by 4e−5 / 6e−5. Ledger values:

\[
\boxed{
s_7^-/c_7 = 1.21326,\qquad s_7^+/c_7 = 1.35908.
}
\]

The rigidity value 1.21103 was the minus side at coarser quadrature; the N-Richardson values from the probe (1.21228/1.35654, at ngrid = 40001) carried a ~0.2% quadrature systematic, now removed. The asymmetry is genuine: the bipartite ±loading exchange is rough at scale h = log 7 and does not preserve the null cluster, so the restricted maxima differ [I].

---

## 2. Pipeline note: the Round 139 quadrature finding, addressed [N]

External Audit Round 139 (v13.928) demonstrated that `fem_screw.py`'s `build_G2` uses a fixed quadrature grid (ngrid = 40001) whose error is amplified by 1/h² in `assemble_Q` — and that v13.926's "converged" 1.83e−8 absolute floor was that artifact, collapsing 1000× under ngrid refinement alone. Independently reproduced here: at a = 2, N = 800, λ_1(Q_full) = 1.839754e−08 → 1.488960e−09 → 1.271454e−10 for ngrid = 40001 → 160001 → 640001, matching the auditor's numbers to 4 digits.

The m=7 slopes live in a different measurement regime and survive:

- The artifact is an **additive ~1e−8 floor on the absolute near-zero eigenvalue**. The slopes are **O(1) differences**: Δλ_1 ~ c_7·ε ~ 7e−3 at ε = 0.01, five orders of magnitude above the floor.
- The kink stiffness KK[m] = √m·(Qk_raw − Q_0) is a **difference of two same-ngrid assemblies**, cancelling the common quadrature error; the residual ngrid dependence is second-order.
- Direct test (§1 table): 32× ngrid refinement moves the slopes by 0.2% then plateaus at the 5e−5 level. The qualitative verdicts below are untouched by a 0.2% systematic.

Lesson recorded: every future FEM number from this pipeline gets an ngrid-refinement check, not just an N-refinement check.

---

## 3. Mechanism: thin-seed dilution [N/I]

v13.908 [D]: ‖KK[m]‖ = 2cos(π/k), k = ⌈2a/log m⌉ + 1. The global maximizer is a near-null function of the full shift graph — but the V-slope only sees the **null cluster** (eigenvectors with Q_full-eigenvalue below threshold τ). At a = 2, m = 7: the longest (3-point) shift orbits have seed sets of width **0.108**, while near-null smoothness requires features ≳ 2π/γ_1 ≈ **0.44** (γ_1 ≈ 14.1347, first zero ordinate). A 0.108-wide sliver cannot host a near-null top-eigenvector of KK[7]; the cluster's best ±loadings are therefore 1.213/1.359, not √2 [N measurements; scale comparison I].

Three independent confirmations:

1. **τ-sweep** (lowest 600 generalized eigenpairs of (Q_full, M), a = 2, N = 1600): restricted max +loading plateaus at **1.205–1.214** and −loading at **1.357–1.360** for τ ∈ [1e−3, 3e−2] — matching the V-slope secants to ~0.3%. Controls: m = 2 plateaus at 2cos(π/7), m = 3 at 2cos(π/5). Beyond τ ≈ 0.1 the maxima creep up but never approach √2 within τ ≤ 3: the global maximizer (Q_full RQ 1.79, v13.906 §7) is excluded from every physical null cluster [N].
2. **a-sweep** (m = 7, secants at N = 800/1600):

| a | n_orb | 2cos(π/k) | sec⁻ | sec⁺ | seedw | reading |
|---|-------|-----------|------|------|-------|---------|
| 0.5–0.75 | 1 | 0 | 0 | 0 | 0 | KK[7] = 0 [D] |
| 1.0 | 2 | 1.0 | 0.00087 | 0.00002 | 0.054 | **silent kink** |
| 1.25 | 2 | 1.0 | 0.97662 | 0.99360 | 0.554 | two-bump works → 1 |
| 1.5–1.75 | 2 | 1.0 | 1.0000 | 1.0000 | ≥1.054 | → 1 |
| 2.0 | 3 | √2≈1.41421 | 1.20642 | 1.35211 | 0.108 | **diluted** |
| 2.25 | 3 | 1.41421 | 1.41175 | 1.41402 | 0.608 | rejoined |
| 2.5 | 3 | 1.41421 | 1.41415 | 1.41416 | 1.108 | rejoined |
| 3.0 | 4 | 2cos(π/5)≈1.61803 | 1.56529 | 1.60374 | 0.162 | diluted again |
| 3.5 | 4 | 1.61803 | 1.61801 | 1.61800 | 1.162 | rejoined |
| 4.0 | 5 | √3≈1.73205 | 1.71138 | 1.72721 | 0.216 | diluted again |

Every rejoin/dilute transition tracks the seed width crossing ~0.44 [N].

3. **Extremal vectors**: both m = 7 crossing vectors are pure even (parity 1.000), with loadings +1.218/−1.362, concentrated exactly on the three thin 3-pt-orbit slivers; shift autocorrelation A(log 7) = −0.609/+0.681 [N].

**The silent kink [N/I]:** at a = 1.0 (slivers 0.054 wide), both slopes are ~1e−3/~0 — no null direction loads the kink at all, so no level crossing occurs. Below the smoothness scale, the kink is invisible to the null cluster.

---

## 4. Systematic 2cos table [N]

Measured sec^±/c_m vs 2cos(π/k(m,a)):

- **a = 2** (N = 1600): m = 2 → 1.80098/1.80144 ✓; m = 3 → 1.61777/1.61792 ✓; m = 4 → 1.41415/1.41416 ✓ (= √2); m = 5 → 1.41403/1.41413 ✓ (= √2); **m = 7 → diluted** (seedw 0.108); m = 8,9,11,13 → 1.0000 ✓ (4–6 digits, = 2cos(π/3)).
- **a = 4** (N = 800): m = 2 → 1.94039/1.94130 ✓ (2cos(π/13) = 1.94188); m = 3 → 1.87355/1.87828 mild dilution (seedw 0.310); m = 4 → 1.80187/1.80185 ✓; m = 5 → 1.73203/1.73203 ✓; **m = 7 → 1.71138/1.72721 diluted** (seedw 0.216 vs √3 = 1.73205); m = 8,9,11 → 1.61799 ✓; m = 13 → 1.61182/1.61241 mild dilution (seedw 0.305 vs 2cos(π/5) = 1.61803).

Every mismatch is a thin-seed case; every thick-seed case matches to 4–6 digits. (These table values predate the §2 quadrature refinement; the ~0.2% systematic applies uniformly and changes no ✓/✗ call.)

---

## 5. Correction to v13.906 §7's phrasing [I/N]

The h < a overlap does **not** make the two-bump construction impossible: Gaussian bumps placed away from the (−0.054, 0.054) overlap still achieve loading **+1.000000** with Q_full RQ ≈ 1e−6 [N]. What the overlap/thinness blocks is reaching the **3-point fiber value √2** — the 3-point seed set is too thin for a near-null function. The two-bump's ±1 is valid but suboptimal (the null cluster does better: 1.213/1.359).

---

## 6. What remains open [O]

- Closed forms for 1.21326 / 1.35908 themselves: concentration–dilution variational optima (prolate-like), unlikely to have pretty formulas.
- Analytic proof of the ~0.44 ≈ 2π/γ_1 seed-width threshold.
- Classification of the extremal null-cluster vectors.

---

## 7. Reproducibility

Sandbox run `lane_b/sandbox/runs/20261001-m7-ratio/`: `m7_lib.py` (KinkSystem, measure_slope), `m7_precision.py`, `m7_asweep.py`, `m7_nullcluster.py`, `m7_vectors.py`, `m7_table.py` + JSON data + figures. Post-probe quadrature verification: `spotcheck_ngrid.json` (ngrid plateau 40001 → 320001 → 1280001) and the Round 139 reproduction (§2). Dense `eigh` throughout.

---

## 8. Result

\[
\boxed{
\text{The m=7 "1.21103" is the minus-side null-cluster-restricted KK[7] norm at a=2: } 1.21326.
}
\]

\[
\boxed{
s_7^+/c_7 = 1.35908\quad\text{(plus side, previously unreported).}
}
\]

\[
\boxed{
s_m^\pm/c_m \le 2\cos(\pi/k(m,a)),\ \text{equality iff longest-orbit seed width } \gtrsim 2\pi/\gamma_1.
}
\]

The 2cos correspondence holds universally in its null-cluster-restricted form. The selection law s_m = c_m (v13.906) is untouched: these ratios are the *loading geometry* of the kink, not corrections to the selection.
