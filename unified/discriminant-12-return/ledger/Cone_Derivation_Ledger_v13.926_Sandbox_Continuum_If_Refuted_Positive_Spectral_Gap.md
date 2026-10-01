# Cone Derivation Ledger v13.926 — Sandbox: Continuum 'If' Refuted — Positive Spectral Gap, V-Shape Sandwich

**Date:** 2026-10-01
**Track:** Sandbox / exploratory lane (little Euler)
**Status:** [D] exact conditional/logic; [N] numerical refutation with converged positive gap; [I] mechanism; [O] analytic lower-bound proof, exact minimizer closed form
**Authorization:** Jeremy, 2026-10-01 ("we should ledger your results")
**Parents:** v13.906 (missing lemma / null cluster / two-bump construction), v13.910 (V-shape refinement; the conditional under test), v13.902 (rigidity: isolated Λ maximizer)
**Collision check:** live head v13.925 read in full immediately before this write; v13.926 absent.

---

## 0. The question

v13.910 §7 proved [D, conditional]:

> **If** inf_{u ∈ H¹_0(−a,a)} RQ_full(u) = 0, **then** f_cont(ε) = −c_m|ε| exactly (a genuine kink at 0).

The 'if' was [O]. The rigidity report's recommended next step was the analytic origin of the unit kink-loadings — "where a theorem might live." This entry closes the 'if' in the negative [N] and records what survives.

Here a = 2, m = 9 (h = log 9 ≈ 2.197 > a), Q_full the full-Λ screw form, RQ the Rayleigh quotient against the L² mass norm. Sandbox investigation only; scripts and JSON data retained in the run directory (see §8).

---

## 1. Verdict: REFUTED [N]

\[
\boxed{
\inf_{H^1_0(-2,2)} RQ_{\rm full} = 1.83\times10^{-8} > 0.
}
\]

The infimum is positive, N-stable, and O(h²)-converged. The v13.910 conditional's hypothesis is false; the exact continuum V-shape does not follow. What holds instead is a V of slope c_m shifted up by 10⁻⁸–10⁻⁷ (§5).

---

## 2. Numerical proof of a positive gap [N]

FEM λ₁ vs N (dense `eigh`, P1, a = 2):

| N    | λ₁         | λ₂         | λ₃         | freqRQ | sign changes |
|------|------------|------------|------------|--------|--------------|
| 400  | 1.8854e−08 | 7.7796e−08 | 1.8863e−07 | 0.6417 | 0            |
| 800  | 1.8398e−08 | 7.4020e−08 | 1.8093e−07 | 0.6318 | 0            |
| 1600 | 1.8294e−08 | 7.3352e−08 | 1.7968e−07 | 0.6300 | 0            |
| 3200 | 1.8282e−08 | 7.3244e−08 | 1.7952e−07 | 0.6298 | 0            |
| 6400 | 1.8277e−08 | 7.3226e−08 | 1.7949e−07 | 0.6297 | 0            |

λ₁ decreases monotonically with shrinking increments (−4.56, −1.04, −0.12, −0.05)×10⁻¹⁰ — the textbook O(h²) signature of a genuine positive eigenvalue converging, not a numerical floor decaying toward zero [N]. By P1-density in H¹_0 and continuity of Q on H¹_0 [D, standard FEM theory], lim_{N→∞} λ₁(N) = inf_{H¹_0} RQ_full. Hence the boxed value above.

The gap λ₂/λ₁ ≈ 4.0 is N-stable, so λ₁ is simple [N] (consistent with v13.910's Danskin analysis). The minimizer is a legitimate low-frequency H¹ function — freqRQ ≈ 0.63 (frequency √0.63 ≈ 0.79 rad/unit ≪ γ₁) and zero sign changes at every N [N]: a smooth single-signed bump, not mesh-scale noise escaping to high frequency.

---

## 3. Mechanism: RQ is a high-pass filter [N/I]

For u_ω(x) = b(x)cos(ωx) with b a fixed C_c^∞ bump:

| ω | 0 | 2 | 5 | 10 | 14.13 (=γ₁) | 15 | 20 | 30 | 50 | 120 |
|---|---|---|---|----|----|----|----|----|----|-----|
| RQ | 9.4e−04 | 1.1e−04 | 3.2e−04 | 3.9e−02 | **1.49** | 1.32 | 1.26 | 1.77 | 2.57 | 2.71 |

RQ sits at ~10⁻⁴ below γ₁, then **explodes by four orders of magnitude crossing the first zeta zero** and never comes back down (grows slowly ~log ω after) [N]. A function with frequency content ≳ γ₁ resonates with the zeta zeros — whose density ~(log T)/2π grows without bound — so its zero-sum Σ_ρ|Φ(ρ)|² is O(1) or larger. Consequence [I, mechanism; numerics [N]]: no RQ-minimizing sequence can escape to high frequency. Minimizers are trapped in the low-frequency regime, where the effectively finite-dimensional problem attains a positive minimum.

---

## 4. Two-bump Ritz plateau and the kink-loading tradeoff [N]

Two-bump Ritz over sine-series bumps (the extremal-loading family; loading exactly ±1 for every profile [D, shift-pairing from v13.906]):

| J (sine modes) | 2 | 4 | 8 | 16 | 32 | 64 |
|---|---|---|---|----|----|----|
| min RQ | 3.71e−04 | 4.84e−07 | 1.92e−07 | 1.24e−07 | 1.10e−07 | 1.07e−07 |

The minimum decreases then **plateaus at ≈ 1.07×10⁻⁷** [N]. The J = 64 optimizer uses essentially low-frequency modes (dominant j = 1 at 1.74 rad/unit; coefficients for j > 32 below 4.4×10⁻⁵), so J = 64 is more than sufficient — the plateau is real, not a truncation artifact. Interpretation [I]: cancelling more zeros demands higher-frequency bumps, which overlap *higher* zeros — a whack-a-mole with an optimal finite tradeoff, hence a positive floor even in the loading-saturated family.

Kink-loading (KK[9] from g₉(t) = (|t| − log 9)_+ [D]; |loading| ≤ 1 [D, contraction]):

- FEM λ₁-eigenvector v₁: RQ_full = 1.8282e−08 (minimal), loading₉ = **−0.462** (not extremal) [N] — reproduces v13.910's −0.461.
- Two-bump Ritz minimizer: RQ_full = 1.0713e−07, loading₉ = **+1.000000** exactly [N, confirms the [D] shift-pairing].

So the RQ-minimizer does not saturate loading, and the loading-saturator does not minimize RQ. Both directions are near-null (RQ ~ 10⁻⁸–10⁻⁷), but **no function has RQ → 0**, with or without the loading constraint [N].

---

## 5. Consequence for the V-shape [D/N]

Since inf RQ_full = 1.83e−08 > 0 [N], the v13.910 conditional is vacuous. For f_cont(ε) = inf_u[Q_full(u) + ε·c_m·loading_m(u)]:

- **Lower bound** [D]: f_cont(ε) ≥ 1.83e−08 − c_m|ε| (inf RQ + contraction bound on loading).
- **Upper bound** [N]: f_cont(ε) ≤ 1.07e−07 − c_m|ε| (two-bump test functions with loading ∓1, RQ ≈ 1.07e−07).

Hence f_cont(ε) is a **V of slope c_m shifted up by 10⁻⁸–10⁻⁷** [N] — the exact V f_cont(ε) = −c_m|ε| is false, but only by a ~10⁻⁷ additive offset. Consequences:

- v13.906's s_m = c_m stands as a **finite-scale law** [D] (already qualified by v13.910); the infinitesimal-derivative reading was already refuted [N] there.
- The selection/rigidity conclusions (v13.902) are unaffected: the V's *slope* — which selects Λ — is c_m regardless of the 10⁻⁷ offset [I].
- The [D] sandwich |f(ε) − (λ₁ − c_m|ε|)| ≤ η of v13.910 is consistent: the continuum f_cont sits λ_* ≈ 1.83e−08 above −c_m|ε|, within η ~ 6e−6 [N].

---

## 6. Analytic obstructions mapped (why inf = 0 fails) [I]

Not proofs — a map of exactly where the 'if' breaks:

1. **High-frequency route fails** [I/N]. u_ω = b·cos(ωx) gives Q ≲ ω²·(zero-density); the ω² from differentiating beats the largest zero gaps (~(log ω)²) for every fixed smoothness, and raising smoothness hits the non-analyticity derivative-growth wall. §3 [N] confirms: no dip anywhere above γ₁.
2. **Smoother-bump route stalls** [I]. IBP gives Q ≤ C·r_K²·γ₁^{−2K} with r_K = min_{H^K_0}‖b^{(K)}‖/‖b‖, but the sharp H^K_0 constants (beam eigenvalues; K = 2: (4.73/|L|)²) exceed the Poincaré-chaining lower bound (π/|L|)^K used in the naive estimate — the "r_K^{1/K} < γ₁" requirement is not satisfiable by the book estimate, and Gaussian bumps fail outright (r_K^{1/K} ~ σ⁻¹√(2K/e) → ∞, Hermite growth).
3. **Compact-operator view** [I]. If inf were 0, a minimizing sequence with bounded ‖u_n'‖₂ would (Rellich + compactness of G) converge to a nonzero null vector — but λ₁ > 0 rules that out [N]; so minimizers would need ‖u_n'‖₂ → ∞, i.e. escape to high frequency — which §3 [N] forbids. The two requirements are mutually exclusive; hence the gap.

---

## 7. What this is not

- **Not an analytic proof.** The positive lower bound is proved numerically (converged, N-stable, mechanism-mapped) but not analytically. A rigorous high-pass estimate plus a low-frequency finite-dimension gap remains [O].
- **Not a statement about the exact continuum minimizer's closed form** — the FEM mode is a smooth single-signed bump at frequency ~0.8; its closed form is unknown [O].
- **Not a touch on the twisted/D12 channel, the de Branges odd sector, or the zero ordinates.** The gap is a property of the full-Λ screw form's bottom spectrum, nothing more.
- **Not in tension with v13.925.** That entry's "no null vector" results (trivial ker K_Φ, empty point spectrum of Q) live in the compression-cone operator lane; this entry's positive gap lives in the screw-form variational lane. Both say "no null direction," in different houses — noted as resonance, not claimed as one theorem.

---

## 8. Reproducibility

Sandbox run directory `lane_b/sandbox/runs/20261001-continuum-if/` (scripts + JSON, dense `eigh` throughout): `exp1_lambda_vs_N.py` → `lambda_vs_N.json`; `exp2_twobump_ritz.py` → `exp2_twobump_ritz.json`; `exp2b_coeffs.py` → `exp2b_coeffs.json`; `exp3_freq_response.py` → `exp3_freq_response.json`; `exp4_loadings.py` → `exp4_loadings.json`. FEM pipeline from the validated `fem_screw.py` (reproduces Kim's R7 −4.97 at a = 2 [N]).

---

## 9. Result

\[
\boxed{
\text{The v13.910 'if' is closed — REFUTED [N].}
}
\]

inf_{H¹_0} RQ_full = 1.83×10⁻⁸ > 0. The exact continuum V-shape does not follow; instead

\[
\boxed{
1.83\times10^{-8} - c_m|\varepsilon|
\le
f_{\rm cont}(\varepsilon)
\le
1.07\times10^{-7} - c_m|\varepsilon|.
}
\]

The slope that selects Λ is c_m either way. The remaining analytic prize is a non-numerical proof of the positive lower bound.
