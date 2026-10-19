# Cone Derivation Ledger v14.596 — Sandbox closure: overlay P exhibited in the distribution class; E·P = A₁₂ verified

**Timestamp:** 2026-10-18 (EDT, night)
**Lane:** Sandbox (little Euler)
**Parents:** v14.593 (dictionary closure; it closed the J₁/D_exp item and explicitly left the helix-representation obstruction open — this entry closes that item), v14.592 §3, the sandbox product-form brief and reports of 2026-09-28 (`lane_b/sandbox/runs/20260928-005525-spherical-archimedean/PRODUCT_FORM_BRIEF.md`; `20260928-010240-spherical-archimedean-2/archimedean_report_2.md` §§3–4 + STATUS follow-up), v14.595 also being live HEAD at allocation (collision-checked immediately before — next-free was v14.596).
**Status:** closure entry under Jeremy's explicit 2026-10-18 authorization ("Ledger the P closure"). Answers **no Lane A HANDOFF**; changes no paper, no staged draft, and no certified object (v13.258's closed form is used read-only). The item left open at v14.593 is **closed in the distribution class, by explicit construction and numerical verification** — the strongest form the obstruction itself permits (see scope).

## The obligation as staged (2026-09-28)

The product-form brief asked for A₁₂ = E·P with E = Ã ≥ 0 the envelope (positivity-neutral) and P a helix overlay Σ cₖ e^{iτₖx(t)} matching the quotient T = A₁₂/Ã. Report 2 §3 proved this impossible in the finite class: in x-coordinates T̃(x) = −s·log(L/x) + O(1) at the centre, s = −C₁/12 = 0.24060639745313878…, C₁ = ψ(1/4) + log(12/π), while every ℓ¹/finite-measure Fourier representation is bounded. The representing object is a tempered distribution. §4 and the STATUS follow-up prescribed the remaining work verbatim: "build P explicitly as the measured 1/n tempered distribution Σ cₙ cos(πnx/L), studying its conditional convergence."

## The construction [D, exhibited]

Deposit: research note `Overlay_P_Distribution_Class_Closure.md` (commit `a62f62cc3c5191917d4b4c867fd529ea3e028e8c`, SHA-256 `18828ece50635b68b123fc9762ca5e3ebeb79322216a82ce5b77f55233fd8b6f`), producer `overlay_P.py` (commit `ac8037346449558342681cb1dc1adc6445623b97`, SHA-256 `fbef5a0b207f5a9a18e3776fa7ec53da6fe6676d839777a10e8c634664747f70`). Workspace originals in `lane_b/sandbox/runs/20261018-overlay-P/`.

With the D_exp dictionary (L = 12/11, closed at v14.593) and T̃(x) = a₀/2 + Σ_{n≥1} aₙ cos(πnx/L), the split aₙ = −s/n + rₙ resums the singular part in closed form, since Σ_{n≥1} (−s/n)cos(πnx/L) = s·log(2 sin(πx/(2L))):

$$P(x) = a_0/2 \;+\; s\,\log\bigl(2\sin(\pi x/(2L))\bigr) \;+\; \sum_{n\ge1} r_n \cos(\pi n x/L).$$

The log kernel is the centre dive itself — the distribution-class heart. The remainder is an ordinary absolutely summable helix series (verified next), so P is exhibited as (explicit singular distribution) + (ℓ¹ overlay), exactly the class §3 forces.

## Verification [D, computed]

- **Coefficients.** a₀/2 = 0.035905161267; aₙ (n ≤ 512) by Clenshaw–Curtis on the log-subtracted integrand h(u) = T(−log u) − s·log u, 8192 Chebyshev–Lobatto points at dps 30. Independent quadrature anchors at n ∈ {1,2,3,5,8,13,21} (dps 40) agree to ≤ 8×10⁻¹³.
- **Tail law.** rₙ ≈ A·n^{−3/2} + B·(−1)ⁿ(log n)n^{−3/2} + C·n^{−5/2} on n ∈ [48,512]: A = 0.150064 (predicted 0.15 — twice report 2's 0.075 transient, in aₙ units), B = −0.014744 (predicted ≈ −0.015 from its cusp fit), C = −0.0008; Σ_{n≤512}|rₙ| = 0.3920. Absolute summability of the remainder is measured, not assumed.
- **Product.** On 78 t-points in [0.02, 30]: max |Ã(t)·P(x(t)) − A₁₂(t)| = 1.03×10⁻³ (at t = 30, |A₁₂| ≈ 41); rms 2.2×10⁻⁴; max relative error where |A₁₂| > 1: 3.5×10⁻⁵. **Error budget (complete):** the product error is Ã × (tail-model error beyond n = 512, ≈ 1.7×10⁻⁴, uniform in x); the kernel is exact and the coefficients are 1e-12-accurate, so refinement is more coefficients and nothing else.
- **Sign anatomy.** Reconstructed P vanishes at t = 1.912049582569 vs exact t₀ = 1.912049280865 (3.0×10⁻⁷): with E ≥ 0, sign(P) = sign(A₁₂) is verified quantitatively — the factorisation's positivity-neutrality is a measured fact.
- **Centre constant.** a₀/2 + s·log π + R(0) = 0.7163830844 vs ζ(2,1/4)/24 = 0.7165553814 (1.7×10⁻⁴, the same tail-model limit).
- **Conditional convergence (as prescribed).** Raw partial sums obey S_N(0) + s·log N → a₀/2 + R(0) − sγ = 0.30207197 (values 0.26294, 0.28303, 0.29275, 0.29753 at N = 64, 256, 1024, 4096; approach ~ 0.3/√N, the rate the rₙ tail predicts). Crossover: the 512-mode raw sum tracks T̃ with errors 0.111 / 0.0168 / 0.0050 / 0.0012 at x = c·L/512, c = 0.5/1/2/4 — resolution to a few × L/N, degrading inside, as §3 requires.
- Sanity anchors reproduced in-run: s to 20 digits; t₀ to STATUS digits; T(30) direct = tail formula.

## Scope flags (honest)

`answers_lane_a_handoff = false`; `papers_modified = false`; `certified_objects_modified = false`; `product_form_step2 = DISCHARGED_IN_DISTRIBUTION_CLASS`; `helix_representation_obstruction = CLOSED_IN_DISTRIBUTION_CLASS_NUMERICALLY_VERIFIED`; `verification_is_proof = false` (numerical, on t ∈ [0.02, 30], tolerances stated; report 2 §3a remains the class proof); `phase_derived_from_helix_first_principles = false` (P is the quotient's own spectral distribution, exhibited per the 2026-09-28 prescription — the strongest form the obstruction permits, not an independent geometric derivation); `G_derived = false`.

## Disposition

The 2026-09-28 product-form arc is now closed on both staged items (dictionary at v14.593, overlay here). A companion same-session scoping — the conductor family of channels (Suzuki zero-free formula at a = 1/4 even / 3/4 odd; s(χ) = −C₁(χ)/q tabulated for q ∈ {3,4,5,7,8,11,12,13,21,24}; dive threshold q < π·e^{−ψ(a)} = 215.33 even / 9.31 odd) — remains sandbox-only (`runs/20261018-conductor-channels/`), not deposited, awaiting Jeremy's line. Per-channel P constructions were not run; the construction is s- and L-covariant.
