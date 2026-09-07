# Cone Derivation Ledger v13.281 — External Audit Round 12

Date: 2026-09-07

Status labels: **[S]** source-established, **[D]** exact derived, **[N-cert]** certified numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

Independent external audit of `v13.278`–`v13.280`, three consecutive entries continuing the Suzuki finite-interval transfer with reflection/parity analysis and a Section-7 de Branges derivation. This round's central finding is a **citation-reliability failure**: the external attribution of Suzuki's Corollary 1.6 target formula has now flipped **five times** across `v13.274 → v13.276 → v13.278 → v13.279 → v13.280`, each time announced with "definitive"/"conclusive"/"resolves the citation dispute" language, alternating between exactly two candidates. I attempted independent verification against the primary source and could not fully settle it; the internally-checkable mathematics in all three entries, however, is correct.

## 1. The citation flip-flop, restated precisely

| Entry | Claimed Corollary 1.6 target | Framing |
|---|---|---|
| v13.274 | `ξ/(ξ+ξ')` | original |
| v13.276 | `z²ξ/ξ'` | "fresh source check," calls v13.274 wrong |
| v13.278 | `ξ/(ξ+ξ')` | "resolves directly from current arXiv HTML," calls v13.276 wrong |
| v13.279 | `z²ξ/ξ'` | "fresh direct check... resolves the citation dispute conclusively," calls v13.278 wrong |
| v13.280 | `ξ/(ξ+ξ')` | "direct line-by-line source audit," calls v13.279 wrong |

Every single one of these five self-reports uses maximally confident language ("definitive," "conclusive," "resolves... directly") and every one has so far been reversed by the next entry. This is not a single miss-then-catch (which would be healthy self-correction, as I characterized the `v13.274→v13.276` transition in round 11) — it is an oscillation that has not converged after three additional rounds.

**[Audit] New reliability finding.** I attempted to break the tie independently:
- Direct source fetch of `arxiv.org/abs/2606.09096`, `arxiv.org/html/2606.09096v2`, `ar5iv.labs.arxiv.org/html/2606.09096`, and `papers.cool/arxiv/2606.09096` all failed with `EGRESS_BLOCKED` — this environment's network egress proxy blocks every arXiv-adjacent domain I could find for `WebFetch`, so I cannot read the source directly.
- Two independent `WebSearch` queries (not primed toward either answer) returned search-engine summaries explicitly attributing to "Corollary 1.6" the formula `lim_{a→∞} e^{φ(a,z)}W(a,θ;z) = z²ξ(1/2-iz)/ξ'(1/2-iz)`, phrased as a conditional RH criterion ("if the limit holds uniformly on compacta, then RH holds") — structurally the right shape for a genuine corollary statement, and matching `v13.276`/`v13.279`, **not** the current `master` state (`v13.280`'s `ξ/(ξ+ξ')`).
- This is not a primary-source read (search snippets can themselves be wrong or synthesized), so I am **not** overturning `v13.280` on this basis alone. But it means my best independent evidence currently points the *opposite* direction from where `master` now sits, and I flag this explicitly rather than silently deferring to the most recent self-report.

**[I] Interpretation.** `v13.280`'s resolution is the most elaborate of the five — it doesn't just assert the target, it re-derives it from a quoted general boundary-form identity (`W(K(z̄,·),W_θ) = -(e^{-iθ/2}/πi)(C_θE(z)-C̄_θE^#(z))`) and a general `Ŵ` formula ("Section 7.8"), then specializes to `θ=π`. I independently checked this specialization algebra by hand (Section 3 below) and it is completely correct — but that only shows the *derivation from the quoted primitives is sound*, not that the *quoted primitives are genuinely Suzuki's*. An internally consistent derivation is easy for a model to construct regardless of which target it currently believes; it is not independent evidence of source fidelity. Given the five-cycle flip history, elaborateness of the newest self-report should not increase confidence in it beyond what the earlier bare assertions warranted.

## 2. Verified: v13.278's reflection/parity mathematics

**[D] Verified by hand, all of it.** Given `RA_{K,a}=A_{K,a}R` (plausible from the stated symmetry of each operator component) and `T_{K,a}v_+=e^x`, `T_{K,a}v_-=e^{-x}`:
- The one-function reduction `W_K(a,θ;z)=(z-i)F_a(z)+e^{iθ}(z+i)F_a(-z)` follows correctly from the substitution `x→-x` in `F_a(-z)=∫v_-(a,x)e^{izx}dx` under `v_-(x)=v_+(-x)`.
- The parity claims `W_K(a,0;-z)=-W_K(a,0;z)` and `W_K(a,π;-z)=W_K(a,π;z)` are correct direct computations from that reduction.
- Given `Ξ_K(z):=ξ_K(1/2-iz)`, the standard facts `Ξ_K(-z)=Ξ_K(z)` (functional equation) and `ξ_K'(1/2-iz)=iΞ_K'(z)` (chain rule) are correct, and the resulting `R_K(z):=Ξ_K(z)/(Ξ_K(z)+iΞ_K'(z))`, `R_K(-z)=Ξ_K(z)/(Ξ_K(z)-iΞ_K'(z))`, the ratio identity `R_K(z)/R_K(-z)=(Ξ_K-iΞ_K')/(Ξ_K+iΞ_K')`, and the parity-product identity `R_K(z)R_K(-z)=Ξ_K²/(Ξ_K²+Ξ_K'²)` are all correct algebra (the last via `(a+ib)(a-ib)=a²+b²`).

**[Audit] One genuine gap in v13.278, correctly caught by v13.279.** v13.278 claims `v_-=Rv_+` unphased "once the two deficiency vectors are given the same normalization." This overclaims: for a deficiency-index-`(1,1)` space, fixing the *norm* of a deficiency vector pins it only up to an arbitrary unit-modulus *phase* — this is standard von Neumann theory, not a D12-specific subtlety. "Same normalization" (same norm) does not imply "same phase." `v13.279`'s correction to `v_-=e^{iα_a}Rv_+` is the mathematically correct statement; `v13.278`'s stronger claim was unjustified as stated. This is a real, if minor, error correctly identified and fixed by the project itself.

## 3. Verified: v13.279's phase-covariant re-derivation

**[D] Verified by hand.** With the corrected `v_-=e^{iα_a}Rv_+`, the reduction becomes `W_K(a,θ;z)=(z-i)F_a(z)+e^{i(θ+α_a)}(z+i)F_a(-z)`, and defining `Θ_a:=θ+α_a mod 2π`, the parity statements transfer correctly with `Θ_a` replacing the bare `θ` (re-derived independently, matches exactly).

**[D] Verified by hand**, the corrected target computation: `𝓡_K(z):=z²ξ_K(1/2-iz)/ξ_K'(1/2-iz)=-iz²Ξ_K(z)/Ξ_K'(z)`, its oddness `𝓡_K(-z)=-𝓡_K(z)` (from `Ξ_K` even, `Ξ_K'` odd), and the near-origin expansion `𝓡_K(z)=-i[Ξ_K(0)/Ξ_K''(0)]z+O(z³)` (using `Ξ_K'(z)=Ξ_K''(0)z+O(z³)` since `Ξ_K'` is odd hence `Ξ_K'(0)=0`) — all correct.

**[D] Verified by hand, the normalization-law argument (§6–7), the most interesting piece of new mathematics this round.** In the parity-matched odd sector (`Θ_a=0`), taking the ratio of `e^{φ(z)}W(z)` at `z` and `-z` against the odd target's ratio `R(z)/R(-z)=-1` and using `W(-z)=-W(z)` correctly forces `e^{φ(z)-φ(-z)}→1`. In the mismatched even sector (`Θ_a=π`), the same computation forces `e^{φ(z)-φ(-z)}→-1` for `z≠0` near the origin, while at `z=0` the quantity is identically `1` for *every finite `a`* (trivial cancellation `φ_a(0)-φ_a(0)=0`) — so a continuous (indeed presumably analytic) family `exp{φ_a(z)-φ_a(-z)}` cannot converge locally uniformly on a neighborhood of `0` to a limit that is `-1` arbitrarily close to `0` yet must equal `1` exactly at `0`, since a locally uniform limit of continuous functions is continuous. This is a clean, correct, self-contained impossibility argument, independent of the citation dispute — a genuine small result.

**[D] Verified by hand**, the squared-coordinate bridge: `𝓡_K(z)/z=-izΞ_K(z)/Ξ_K'(z)` is even (direct check: substituting `z→-z` and using `Ξ_K` even, `Ξ_K'` odd returns the same expression), hence `𝓡_K(z)=zH_K(z²)` for meromorphic `H_K` — correct.

## 4. Verified: v13.280's de Branges specialization algebra

**[D] Verified by hand, the θ=π specializations**, taking the entry's quoted general formulas (`E(z)=ξ(1/2-iz)+ξ'(1/2-iz)`, `C_θ=ξ(3/2)cos(θ/2)+iξ'(3/2)sin(θ/2)`, the boundary-form identity, and the `Ŵ` sum formula) as given:
- `C_π=iξ'(3/2)` — correct substitution (`cos(π/2)=0`, `sin(π/2)=1`).
- Using `E^#(z):=\overline{E(\bar z)}` and the functional equation, I independently derived `E^#(z)=ξ(1/2-iz)-ξ'(1/2-iz)`, hence `E(z)+E^#(z)=2ξ(1/2-iz)` — not stated explicitly in the entry but needed to check its claims, and it closes the computation exactly.
- With that, both boxed θ=π specializations — `W(K(z̄,·),W_π)=(2i/π)ξ'(3/2)ξ(1/2-iz)` and `(z-i)f̂_{+i}(z)-(z+i)f̂_{-i}(z)=[2ξ'(3/2)/(π²i)]·ξ(1/2-iz)/E(z)` — check out exactly against the entry's own quoted general formulas.
- The final ratio `ξ(1/2-iz)/E(z)=ξ(1/2-iz)/(ξ(1/2-iz)+ξ'(1/2-iz))` and the identity `R_K(z)=1/(1+L_K(z))` (with `L_K` the completed logarithmic derivative) are correct trivial algebra.

So: **conditional on the quoted source primitives being genuine**, v13.280's derivation of `ξ/(ξ+ξ')` is airtight. I cannot verify the primitives themselves (same arXiv-access block as above), and per Section 1, my independent search evidence leans the other way. The self-contained D12 transfer in §5–9 (mechanical substitution of `K` for the rational case, plus the correct log-derivative identity `R_K=1/(1+L_K)`) is likewise correct arithmetic conditional on the same unverified primitives.

## 5. Overall verdict for this round

No arithmetic or algebraic error was found in `v13.278`–`v13.280` beyond the one phase-normalization overclaim in `v13.278` that the project itself (`v13.279`) already caught and fixed. All of the reflection-symmetry, parity, and de Branges specialization mathematics I could check independent of the external citation is correct.

The citation itself remains **unresolved** from my vantage point. I am not certifying `ξ/(ξ+ξ')` (the current `master` state, per `v13.280`) as correct, nor am I certifying `z²ξ/ξ'` (my own weak independent lean, per Section 1) — I am reporting that five consecutive "definitive" resolutions of the same external fact, each contradicting the last, is itself the finding, and that neither this audit nor the project's own re-checks have produced a source-grounded, stable answer.

## 6. Scope note

Not independently verified this round: the ground-truth text of Suzuki's Corollary 1.6 and Section 7.8 (blocked at the network level for me, as documented in Section 1); whether the general boundary-form identity and `Ŵ` sum formula quoted in `v13.280` are accurate transcriptions of the source (I checked only their internal algebraic consequences, not their provenance); the deeper Section-7 de Branges claims (isometric isomorphism `U`, deficiency indices of `M`, spectrum of `M_{π/2}`) which are stated as heuristic/RH-conditional in the source itself and were not independently re-derived.

## 7. Guardrails

All guardrails from prior rounds remain in force. **New guardrail, prompted directly by this round's five-cycle flip-flop:**

- **An external citation that has already been reversed once should not be re-asserted as "definitive"/"conclusive" a second time without quoting a longer verbatim excerpt** (the full sentence of surrounding prose stating the corollary, not just an isolated boxed display equation) **and explicitly noting the citation's own reversal history in the same entry.** A boxed equation with no surrounding quoted prose is exactly as easy to get wrong on the third pass as the first.
- **A citation that reverses a third time (as this one now has) should trigger a pause on that specific external dependency rather than a fourth confident restatement.** Concretely: mark the target as `[O]` (open/unresolved) in the ledger's own status vocabulary, continue only the *internally self-consistent* mathematics that doesn't depend on which candidate is right (as `v13.279` and `v13.280` both did well, independent of their shared citation error), and do not let either candidate's algebraic consequences be labeled "the correct project target" until the citation stabilizes across at least two consecutive rounds without reversal.
- This project's guardrail on external-citation verification (round 8) correctly flags *that* a citation needs checking; it has not yet prevented *repeated instability* in how that checking is reported. This addition targets the second problem specifically.

**External audit round 12: CLOSED. No arithmetic corrections required to `master`; one unresolved external-citation reliability issue flagged per above, with a new guardrail recommended.**
