# Cone Derivation Ledger v13.909 — Sandbox Strong Form: From Selected Weights to Zero Ordinates

Date: 2026-10-01

Author: LIttle Euler (sandbox track). Authorization: project owner, 2026-10-01 ("ledger all three!" following the weights→ordinates report).

Predecessors: v13.902 (rigidity: Λ isolated maximizer, exact V-slopes s_m = c_m [N]), v13.904 (analytic skeleton: contraction theorem, kink stiffness as truncated shift [D], missing lemma posed [O]), v13.906 (missing lemma closed: null cluster saturates the contraction bound [D]; weights→zeros chain listed as the remaining downstream [O]). Sandbox report: `weights_to_ordinates.md` (run dir `runs/20260930-divisor-tension/`; scripts/data in /tmp — `Ma_map.json`, `rigid_support.json`, `freq_a2.0.npy`, `freq_a3.0.npy` — ephemeral; key numbers in the report's §5 tables).

Status: **[D]** for the sharp accounting decomposition and the route verdicts' logical content; **[N]** for the new numerics (M(a) map, all-scale rigidity, support probe, frequency probe); **[I]/[O]** for interpretation and the ranked open sub-questions. No RH/GRH claim beyond the stated equivalence RH ⟺ M(a) ≥ 0 ∀a [D, Weil's criterion rephrased]. Sandbox scope only — nothing in this entry touches Lane A or the prime ramp.

## 1. The question

The rigidity arc (v13.902 → v13.904 → v13.906) selects the **weight sequence** Λ = argmax_w λ₁(Q_w) [D]. The chain from the weights to the **zero ordinates** {γ_n} runs through the explicit formula — an independent theorem, not a consequence of maximality. This entry investigates exactly what the selection principle says about the ordinates themselves, via four routes (A–D), and decomposes the strong form into precisely located pieces [D/N/I/O]. **Verdict [D/I]:** the selection principle locates Λ [D]; the *value* M(a) = max_w λ₁(Q_w^{(a)}) rephrases RH as a threshold [D/I]; the *specific ordinate locations* are neither derived nor constrained by the selection — they ride along via the explicit formula. Uniqueness transports [D] but does not explain [I].

## 2. Sharp accounting: where the hardness lives [D/N/I]

Decompose M := max_w λ₁(Q_w) (scale-invariant; measured at a ∈ {0.5,…,4}):

| Piece | Status |
|---|---|
| Location: argmax = Λ (unique maximizer) | **[D]** (concavity [D, zero-free] + contraction s_m ≤ c_m [D] + saturation [D, uses qualitative zero-free region], modulo the [N] V-shape) |
| Value, upper bound: M(a) ≤ 0 | **[D]** via explicit smooth near-null vectors (explicit formula + unconditional zero-free region — theorems, not circular, but zero-location information is used) |
| Value, lower bound: M(a) ≥ 0 | **[N]** (numerical floor ≈ +1.8e−8); this **is** weak RH — **unproved [O]** |
| Ordinate locations {γ_n} | **unconstrained [O]** — not seen by the selection beyond the dictionary |

Consequence **[D, Weil's criterion rephrased]:** **RH ⟺ M(a) ≥ 0 for all a.** Given the [D] location result (argmax uniquely Λ), M(a) = λ₁(Q_Λ^{(a)}), and Weil's criterion is exactly λ₁(Q_Λ) ≥ 0. So the strong form decomposes into (a) the lower bound M ≥ 0 — which *is* RH-hard [O] — and (b) *deriving* {γ_n} from the selection — which no known template achieves and which may be impossible beyond transitive selection [O/I]. **The hardness lives in (a), not the location.** There is no additional mystery beyond RH; but also no bypass around it.

## 3. Route A — zero-side variational principle: clean negative [O]

**Duality [D]:** the explicit formula gives, for w = Λ, Q_Λ(u,u) = Σ_ρ |Φ_u(ρ)|² with Φ_u(ρ) = ∫u'(x)e^{(ρ−1/2)x}dx [D, Guinand–Weil]. For general w there is no zero-side representation — the explicit formula is tied to the arithmetic content of Λ. A formal transport max_Z λ₁(Q_{w(Z)}) exists and is maximized by the actual zeros (since w(Z_actual) = Λ).

**Where circularity enters [I]:** the map Z ↦ w(Z) **is** the explicit formula — zeta-specific (Euler product, archimedean factors). A "variational principle over zero multisets" built on it does not *select* zeta's zeros; it *rephrases* "Λ is the maximizer" in zero language. Any functional reverse-engineered this way is circular (the F3 failure mode). The *non-circular residue* is Bombieri–Lagarias-type: positivity characterizes *critical-line* multisets, not zeta's *specific* zeros — RH-shaped, blind to ordinate locations.

**Spectral-measure picture [D/I]:** at the maximizer Q ≥ 0, so by Bochner-type spectral theory Q(u,u) = ∫|Φ_u(ξ)|²dμ(ξ) for a positive measure μ [D, standard]. The explicit formula *identifies* μ = Σ_ρ δ_ρ [D]. But positivity alone gives a *measure* — possibly continuous; the *discreteness* (pure atomicity at specific locations) is zeta-specific content from the explicit formula, not from the variational principle.

**Deflating the suggestive fact [I]:** "Λ is precisely the weight sequence for which the form diagonalizes over the zeros as a manifest sum of squares" is true [D] — but the *diagonalization* is the explicit formula (input), not a *consequence* of maximality. The coincidence of the maximizer with the explicit-formula sequence is exactly what needs explaining, and the current proof assumes the explicit formula to get there.

**The X for Route A [O]:** a *variational* derivation of (a weak form of) the explicit formula — prove from the variational principle alone that the maximizer's spectral measure *must* be discrete, without invoking Guinand–Weil as a black box. Not achieved. This is not a conceptual impossibility — the explicit formula *is* a theorem — but proving it *from* the variational principle means *re-proving* hard analytic number theory, not bypassing it.

## 4. Route B — the transition scale: precise blocker [O]

**Phenomenon [N]:** frequency probe u_ξ(x) = sin(ξx)·(smooth bump), RQ(ξ) = v_ξᵀQ_Λv_ξ/v_ξᵀMv_ξ:

| ξ | 8.5 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|
| RQ (a=2) | 1e−4 | 2e−2 | 6e−5 | 0.26 | 1.38 | **2.35** | 1.74 |
| RQ (a=3) | 7e−4 | 4e−3 | 2e−2 | 1e−3 | 0.97 | **3.50** | 1.73 |

RQ transitions ~10⁻⁴ → O(1) sharply at ξ ≈ 14 ≈ γ₁ = 14.1347, peaking in resonance with the first zero — **a-independent** (identical at a=2 and a=3). The form "knows" γ₁, and the phenomenon does not *input* γ₁: Q_Λ is built from primes only. Mechanism [D/I]: RQ(ξ) = Σ_ρ |Φ_{v_ξ}(ρ)|²/‖v_ξ‖²_M resonates when Im(ρ) ≈ ±ξ; first kick-in at the smallest |Im(ρ)| = γ₁.

**Logical audit of the selection proof's zero-input [D/I]:** the *saturation* (v13.906) used the explicit formula + zero-free region for near-nullity; but *qualitative* near-nullity needs only **∃c > 0** with no zeros in |Im| < c — a qualitative zero-free strip, not the *value* c = 14.1347. *Epistemically*, we only know "∃c > 0" *via* the computed γ₁ — there is no *theoretical* (non-computational) c > 0 in the literature for the imaginary direction. So: *logically* the specific value γ₁ is **not** an input to the selection proof (only ∃c>0 is); *practically* it is. **A selection proof that *theoretically* establishes ∃c>0 (without computing zeros) would make the emergent γ₁ a *genuine prediction*.** Sharply posed, hard — this is the precise X for Route B [O].

**M(a): the sharp prime-side quantity [N new, I]:** M(a) := max_w λ₁(Q_w^{(a)}), defined *purely prime-side* (no zeros in the definition):

| a | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 4.0 |
|---|---|---|---|---|---|---|---|
| M(a) = λ₁ | 9.96e−7 | 2.51e−8 | 2.02e−8 | 1.84e−8 | 1.92e−8 | 1.77e−8 | 1.40e−8 |

**M(a) ≈ 0 (positive floor) at every scale — the knife-edge is scale-invariant [N]** (at a=0.5 the floor is slightly higher, 1e−6; only one kink active there). The *value* — not just the *location* — carries the RH content, and it is *exactly* as hard as RH: the de Bruijn–Newman analogy made precise (see §6).

## 5. Route C — uniqueness transport: valid but empty [D/I]

**Transport is valid but empty [D/I]:** the explicit formula is (essentially) a bijection between prime distribution and zero distribution [D, classical], so "Λ is the unique maximizer" *implies* "the zero multiset is rigidly determined" [D] — but the *determination* goes through zeta-specific machinery; it *computes* the ordinates from the primes, it does not *explain* them. Contrapositive [I]: any other axiomatic zero multiset Z' ≠ Z_ζ has dual weights w' ≠ Λ, so its "Weil form" is indefinite — true [D, modulo the duality being well-defined for Z'], but the content is just "Λ is the unique maximizer," transported.

**Best positive reframing — selection among L-functions [D/I]:** the variational problem is over *all* weight sequences, including the natural weights of *other* L-functions. ζ's weights beat every other L-function's weights — concretely, the χ₁₂-twisted natural weights give an *indefinite* form (positive only for a ≲ 0.33) [N, sandbox twisted-channel study], so they are not maximizers. Hence: **ζ is the unique L-function whose natural weights maximize λ₁; its zeros are therefore the selected zeros — as "the zeros of the winning L-function."** [D/I] Transitive (via the explicit formula) but *comparative* (ζ vs. others) — strictly more than "Λ is a maximizer in abstract weight space." It does not derive ordinate values, but it *ranks* the zero multisets.

**Support: the primes are partially discovered [N/I]:** the rigidity theorem was proved on prime-power weight space (support = input). New probe — *additive* perturbations w_m = 0 → ±ε for *non*-prime-power m:

| m (non-pp) | 10 | 12 | 14 | 15 |
|---|---|---|---|---|
| dλ₁/dw_m (+direction) | −0.32 | −0.29 | −0.27 | −0.26 |
| dλ₁/dw_m (−direction) | 0.00 | 0.00 | 0.00 | 0.00 |

*Increasing* any non-prime-power weight *decreases* λ₁ (support *locally* stable [N]), but the slope is ≈ −0.3, **not** −1, and the *negative* direction is *flat* (0.00) — contrast prime-power kinks, whose symmetric V has slope ∓c_m to 4 digits in the observed finite-ε (post-level-crossing) regime [N]. Interpretation [I]: the *exact symmetric saturation* (±1) is *specific* to prime-power kinks — it is the *signature* of maximality, not a general geometric fact. The selection *distinguishes* prime powers from other integers *in the response*, not just in the weights: the primes are *partially discovered* (local stability [N]), but *full-space* global uniqueness (which would *derive* the support) remains [O]. The asymmetry (d− = 0) means the *nonnegative* maximizer is locally Λ, but the full-space (signed) maximizer is not pinned at first order.

## 6. Route D — literature: what extremal principles have ever selected [I]

| Approach | What it selects | Specific locations? |
|---|---|---|
| Weil function-field (intersection-pairing positivity) | |ω_i| = √q (a *region*: the circle) | No — only the modulus |
| Lee–Yang (ferromagnetic positivity) | zeros on unit circle (a *region*) | No |
| de Bruijn–Newman (heat-flow threshold) | Λ_dBN = 0 (a *threshold*; RH ⟺ threshold) | No — one number, not locations |
| Li / Bombieri–Lagarias (λ_n ≥ 0) | critical-line multisets (a *region*) | No — the line, not ζ's zeros |
| Connes (absorption spectrum) | zeros as missing lines; needs Weil positivity (the missing step) | No |
| Ours (max_w λ₁) | Λ (a *specific sequence*) → zeros via explicit formula | *Transitively* — the sequence is specific, the locations ride along |

**Verdict [I]:** *no* known variational/positivity approach has *ever* derived *specific* zero locations from an extremal principle. They yield *regions* (circle, line), *thresholds* (dBN), or *specific auxiliary objects* (our Λ) with locations *inherited* via a dictionary. The specific ordinates (14.1347, 21.0220, …) are *always* arithmetic input in known mathematics. Expecting the selection to "output" 14.1347 may be a **category error** [I] — what it *can* output is Λ, and Λ *encodes* the ordinates. Stating this as a clean negative is itself a result. **de Bruijn–Newman is the closest template [I]:** RH ⟺ (threshold = 0); ours: RH ⟺ (M(a) ≥ 0 ∀a), with M(2) ≈ 0 [N] the observed threshold. In both, the object sits *exactly at the boundary* — "only barely" (Newman).

## 7. New numerics (this investigation) [N]

1. **M(a) map** (§4): M(a) ≈ +1.4e−8 to +2.5e−8 for a ∈ {1, 1.5, 2, 2.5, 3, 4} — scale-invariant knife-edge.
2. **Rigidity at all scales:** single-kink V-shape with s_m/c_m = 0.99992 (a=2, m=23), 0.99986 (a=3, m=137), 0.99955 (a=4, m=1009), 0.99265 (a=1, m=4) — exactness is scale-invariant.
3. **a=1, m=4 gives s_m = c_m** (not √2·c_m): at a=1, log 4 = 1.386 > a so m=4 is *well-resolved*, and the √2 anomaly *disappears* — confirming the shift-norm finite-a analysis (the √2 was the 2cos(π/4) finite-a effect, not tower physics).
4. **Support probe** (§5): non-prime-power directions have negative (≈−0.3) but inexact, asymmetric derivatives; negative direction flat.
5. **Frequency probe** (§4): transition at ξ ≈ γ₁, a-independent, sharp.

## 8. Ranked open sub-questions [O]

1. **[O, = RH] Prove M(a) ≥ 0 prime-side** (λ₁(Q_Λ^{(a)}) ≥ 0 ∀a) without the explicit formula's sum-of-squares. This *is* weak RH. Hard — but it is the *exact* missing piece, not a vague "bridge."
2. **[O, sharp] Theoretically establish ∃c>0** (zero-free strip |Im| < c) *from* the variational principle, without computing zeros. Would make γ₁ a genuine *prediction* (§4). No known approach.
3. **[O, concrete] Full-space global uniqueness:** extend rigidity from prime-power support to *all* n (is Λ the unique maximizer over all weight sequences?). Support probe gives local stability [N]; global needs the full strictness.
4. **[O, conceptual] Variational explicit formula:** derive (weak) atomicity of the maximizer's spectral measure from the variational principle alone (§3). Essentially re-proving hard analytic number theory — not a shortcut.
5. **[O] Zero-side functional:** a *non-circular* functional on zero multisets whose extremizer is ζ's zeros. May be impossible in principle (§6 verdict).
6. **[N→D] Map M(a) at larger a** with refinement; check the floor stays ≈ 0 (numerical evidence for (1)).

## 9. Bottom line and scope

- **The selection principle does not see the ordinates.** It *locates* Λ [D]; the ordinates come via the *explicit formula*, an independent theorem. Uniqueness *transports* [D] but doesn't *explain* [I].
- **The *value* M(a) = max_w λ₁ is the right object.** RH ⟺ M(a) ≥ 0 ∀a [D]. M(a) ≈ 0 at all scales [N]. The *hardness* is *exactly* the lower bound — i.e., RH itself. No additional mystery beyond RH; no bypass around it.
- **No template exists** for deriving *specific* ordinate locations from an extremal principle. Expecting "14.1347" as output may be a category error.
- **Most promising positive reframings [I]:** *selection among L-functions* (§5) — ζ uniquely maximizes λ₁, so its zeros are *the* selected zeros; and *M(a) as threshold* (§4/§6) — the dBN-shaped "only barely" statement.
- **The precise X:** a *zero-free* (no explicit formula) proof of near-nullity/saturation. Without it, the selection *recovers* zero information; with it, the selection might *predict* it. Sharply posed analytic number theory, not a vague hope.
- This entry investigates — and precisely decomposes — the last [O] item of v13.906 §8 (the weights→zeros chain). Sandbox scope only: no ledger/repo/research-notes writes beyond this entry; no claims about Lane A.

## Synchronization

Live ledger head checked immediately before this write: v13.907 (audit thread, External Audit Round 131 — read in full; PASS on v13.906, independently confirming the sign erratum, the γ₁ frequency transition, and the two-bump construction). No collision on v13.909.
