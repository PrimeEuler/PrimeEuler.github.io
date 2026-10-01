# Cone Derivation Ledger v13.906 — Sandbox Missing Lemma Closed: the Null Cluster Saturates the Contraction Bound [D]

Date: 2026-10-01

Author: LIttle Euler (sandbox track). Authorization: project owner, 2026-10-01 ("yes ledger this!" following the missing-lemma report).

Predecessors: v13.902 (rigidity: Λ isolated maximizer, exact V-slopes s_m = c_m [N]), v13.904 (analytic skeleton: Danskin equivalence, kink stiffness as truncated shift, contraction theorem ⇒ s_m ≤ c_m [D], missing lemma posed [O]). Sandbox report: `missing_lemma_saturation.md` (run dir `runs/20260930-divisor-tension/`; scripts in /tmp, key data in /tmp/ml_shapes.npz — ad hoc but documented).

Status: **[D]** for the lemma and its three steps (proofs sketched in full); **[N]** for the smoking-gun numerics and construction verification; **[I]/[O]** for interpretation and the remaining open items. No RH/GRH claim — the argument uses only the unconditional zero-free region |Im(ρ)| < 14.13. This entry closes the [O] missing lemma of v13.904 and promotes s_m = c_m to [D] (modulo the [N] V-shape).

## 1. The lemma (sharp statement) [D]

> **Lemma.** For each kink m with h := log m > a, the near-null cluster of Q_full contains explicit smooth functions φ^±_m with kink-loading exactly ±1 and Q_full(φ^±_m, φ^±_m) ≈ 0 (arbitrarily small with smoothness). Consequently the V-slope satisfies s_m = c_m.

## 2. Step 1 — the explicit formula identity [D]

Guinand–Weil, applied to the autocorrelation F = u' ⋆ ũ' of u ∈ C_c^∞(−a,a): the screw construction (Suzuki) makes ∫∫g(x−y)u'(x)u'(y)dxdy equal the explicit-formula RHS (pole + prime-kink sum + archimedean), which equals Σ_ρ F̂(ρ). For this F, F̂(ρ) = |∫u'(x)e^{(ρ−1/2)x}dx|². Hence:

> Q_full(u,u) = Σ_ρ |∫_{−a}^{a} u'(x) e^{(ρ−1/2)x} dx|², sum over all nontrivial zeros ρ of ζ. [D, standard]

**Smoking gun [N]:** for u(x) = sin(ξx)·(smooth window), Q_full(u,u) ∝ Σ_γ |û'(γ)|² (consistent ratio ≈ 0.01 across ξ), and both sides undergo a sharp transition from ~10⁻⁶ to ~2.7 **exactly at ξ = γ₁ ≈ 14.1347** (first zero ordinate). Frequencies below γ₁ are near-null; at/above γ₁ they are O(1).

## 3. Step 2 — low-frequency nullity [D]

Write ρ − 1/2 = β + iγ, β ∈ [−1/2, 1/2] (critical strip, unconditional). Then ∫u'(x)e^{(ρ−1/2)x}dx = \widehat{(u'e^{β·})}(γ), the Fourier transform of a C_c^∞ function — hence O(|γ|^{−N}) for every N (Paley–Wiener/integration by parts). **Key fact [D, known]:** every nontrivial zero satisfies |Im(ρ)| ≥ γ₁ ≈ 14.1347. Zero density O(log T) makes Σ_ρ |γ_ρ|^{−2N} convergent, so Q_full(u,u) = O_N(γ₁^{−2N+1} log γ₁) — arbitrarily small with smoothness. **Smoothness ⟹ near-nullity. [D]** (Not a tautology: it converts smoothness into nullity via the explicit formula and the zero-free region.)

## 4. Step 3 — explicit saturating construction [D]

Let h = log m > a; L = (−a, a−h), R = (−a+h, a) are disjoint (L ⊂ (−a,0), R ⊂ (0,a)). Take b ∈ C_c^∞(L), b ≠ 0, and set φ^+_m = b on L, −b(·−h) on R (antisymmetric pairing; φ^−_m with +b(·−h) for symmetric). Using the corrected δ″ identity (§6), KK[m](φ,φ) = −2∫φ(z+h/2)φ(z−h/2)dz gives **loading exactly +1** (resp. −1) [D]. Since φ^±_m is smooth and compactly supported, Step 2 gives Q_full(φ^±_m, φ^±_m) ≈ 0 [D].

**Verification [N]:** a=2, N=800, Gaussian bumps — m=9: loading ±1.0000 exactly, Q_full RQ 5.9e−6/4.1e−6; m=16: ±1.0000, RQ 1.6e−3.

## 5. Saturation: s_m = c_m [D, modulo V-shape]

Upper bound s_m ≤ c_m from the v13.904 contraction corollary [D]. Lower bound: the construction gives, for any η > 0, a φ_η with loading −1 and Q_full RQ < η; the variational principle gives λ₁(ε) ≤ η − c_mε (ε > 0), so the minimizer drops at least c_m per unit ε — if s_m < c_m the observed V-slope would contradict this bound [D]. Hence **s_m = c_m [D]**. *Caveat [N]:* the V-shape itself (well-defined one-sided derivatives) is observed numerically, not proved; given it, the slope is pinned.

**Conceptual picture [I]:** the zeros live at high frequency (|Im| ≥ 14.13); the kink-maximizers can be built at low frequency (smooth two-bumps); hence the maximizers are null. The contraction bound is saturated.

## 6. Erratum: sign in the δ″ identity [D]

v13.904 §2 stated KK[m](u,v) = +∫∫[δ(x−y−h)+δ(x−y+h)]u(x)v(y)dxdy. **The sign is wrong;** two integrations by parts give **−**∫∫[δ_h+δ_{−h}]uv [D] (the y-integration contributes a second minus sign). Consequences: "loading = 2R_u(h)" becomes −2R_u(h); the +1 maximizer is antisymmetric-paired (matches numerics). The contraction theorem, its corollary, and all v13.904 numerical values are **unaffected** (the bound is symmetric; values were computed from matrices directly).

## 7. The m=7 exception explained [D/N]

For m=7, h = log 7 ≈ 1.946 < a = 2: L and R **overlap**, so the clean two-bump construction is geometrically impossible — the contraction theorem does not apply. The global KK[7]-maximizer (loading √2) has Q_full RQ = +1.79, hence is excluded from the null cluster; smooth functions achieve only 1.21 [N]. The exception **confirms** the mechanism (saturation fails exactly where the construction is impossible). The analytic origin of 1.21 remains [O].

## 8. What remains [O]

- Prove ‖KK[m]‖ = 2cos(π/k) for h < a and identify k(m,a) (sketch in sandbox report §9: truncated-shift/path-graph spectral fact).
- The m=7 value 1.21.
- Vector-anatomy classification (existence now [D]; classification [O]).
- Downstream weights→zeros chain: the [D] rigidity theorem selects the weight sequence Λ = argmax λ₁; the strong form (selecting the ordinates) is untouched.

**Version note:** drafted as v13.905; the audit thread's v13.905 (External Audit Round 130 — read in full; it independently re-derived and numerically confirmed v13.904's contraction theorem: PASS, and it left v13.902's exactness numerics as "unconfirmed-by-me but not contradicted" on proxy-object grounds — a caveat this entry's §5 now supersedes by promoting the exactness to [D]) landed mid-write, so this takes v13.906.

## Synchronization

Live ledger head checked immediately before this write: v13.905 (audit thread, Round 130 — read in full). No collision on v13.906.
