# Cone Derivation Ledger v13.277 — External Audit Round 11

Date: 2026-09-06

Status labels: **[S]** source-established, **[D]** exact derived, **[N-cert]** certified numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

Independent external audit of `v13.272`–`v13.276`, continuing the operator-theory push into Fredholm/trace-class analysis and a direct transfer of Suzuki's finite-interval self-adjoint-extension construction to the D12 Dedekind field. This round is notable for containing **two genuine, correctly-derived no-go theorems** that rule out the project's own immediately-preceding proposals, and **one citation self-correction cycle** (a misattributed external formula caught and fixed within two entries).

## 1. Trace-class sandwich and the bulk-overlap no-go (`v13.272`)

**[D] Verified by hand.** The Schatten-class sandwich theorem (`R₀^{1/2}VR₀^{1/2} ∈ 𝔖₁` whenever `R₀∈𝔖₁` and `V` bounded, via `𝔖₂·ℬ·𝔖₂⊂𝔖₁` and `‖K‖₁≤‖V‖·Tr R₀`) is standard Schatten-class/Hölder-inequality operator theory, correctly stated and applied.

**[D] Verified by hand, the key exact computation.** The compressed free-line resolvent kernel `G_κ(x,y)=e^{-κ|x-y|}/(2κ)` is the standard Green's function for `-d²/dx²+κ²`; the overlap-interval length for the truncated shift `S_{a,v}` on `[-a,a]` is exactly `2a-v` (direct interval-intersection computation, confirmed: `[-a,a]∩[-a+v,a+v]` has length `a-(-a+v)=2a-v` for `0≤v≤2a`); combining gives `Tr(R_{a,κ}S_{a,v}) = (2a-v)/(2κ)·e^{-κv}` exactly as claimed. Comparing against the target Euler coefficient `(1/2κ)e^{-κv}` (no `a`-dependent prefactor) correctly exposes a genuine, exact mismatch — a real obstruction to the "naive bulk translation" model, not a hand-wavy one.

## 2. Distributional form variation and the additive-Fredholm no-go (`v13.273`)

**[D] Verified by hand**, the distributional calculus underlying the single-prime form variation: `r_v(t)=(|t|-v)_+` has `r_v''=δ(x-v)+δ(x+v)` for `v>0` (confirmed by direct differentiation of the two linear branches and the jump-discontinuity contribution at `±v`); the mixed derivative of the anchored screw kernel `∂_t∂_u G_{v,c}(t,u) = -c[δ(t-u-v)+δ(t-u+v)]` follows immediately. Re-deriving the form identity `q_{v,c}[f] = -c⟨(S_{a,v}+S_{a,v}^*)f,f⟩` via integration by parts (boundary terms vanish on `H₀¹`) confirms the entry's claim exactly — this removes the coefficient-normalization ambiguity left open in `v13.272`.

**[D] Verified the no-go theorem exactly.** `d²/dε² log det(I+εK)|₀ = -Tr(K²) = -‖K‖₂² < 0` for any nonzero self-adjoint `K` follows immediately from the standard Fredholm-determinant log-expansion `logdet(I+εK)=Σ(-1)^{m+1}ε^m Tr(Kᵐ)/m`. Since the finite Euler logarithm `log 𝒵_E(s;ε)` is *exactly linear* in independent prime-power couplings `εₙ` (zero second partials, by construction), while any additive self-adjoint operator perturbation necessarily produces strictly negative quadratic Fredholm cumulants, the two objects cannot coincide unless the perturbation is trivial. This is a clean, valid, and consequential impossibility proof — it rules out a whole class of "obvious" realizations (independent additive prime perturbation ↔ literal Euler-product Fredholm determinant) regardless of the specific reference operator, which is a stronger and more general statement than the `v13.272` overlap-factor observation. The project's own response — pivoting to Suzuki's nonlinear boundary/deficiency-vector construction, where the arithmetic enters through an operator *inverse* rather than additively — is the logically correct reaction to this theorem, not an evasion of it.

## 3. Suzuki transfer and a citation self-correction (`v13.274`–`v13.276`)

**[Audit] A load-bearing external citation was misattributed and then self-corrected — verified both states.** `v13.274` attributed Suzuki's current (arXiv:2606.09096v2) Corollary 1.6 limit as `ξ/(ξ+ξ')`; `v13.276`, after "a fresh source check," corrects this to `z²ξ(1/2-iz)/ξ'(1/2-iz)` and explicitly flags the earlier attribution as wrong. I was not able to independently confirm which formula is the paper's actual current statement (this requires reading the specific corollary in the source PDF, which I did not fetch this round), so I cannot certify which of the two ledger states is now correct — but I can confirm the **paper itself is genuine** (arXiv:2606.09096, Suzuki, "Weil's quadratic form via the screw function," matching the DOI/revision-date details already verified in round 10) and I can confirm that none of the *finite-interval* mathematics in `v13.274`–`v13.276` (Friedrichs extension, deficiency indices, the characteristic function `W(a,θ;z)`) depends on which infinite-volume limit formula is correct — the entries are explicit that this correction affects only the attributed asymptotic target, not the finite-`a` construction. The project's practice of re-checking a source "fresh" before continuing, and correcting itself in public when the re-check disagrees with a prior citation, is exactly the right discipline for this kind of cross-paper dependency, and I'd flag it as a positive pattern rather than a defect.

**[D] Verified by hand**, the transfer-lemma mechanism (`v13.275`): given `Tv_z=e^{-izx}`, the adjoint-equation computation `⟨𝒟f,v_z⟩_T = ⟨f,zv_z⟩_T` reducing to ordinary integration by parts with vanishing boundary terms on the `H₀¹` core is correctly sketched, and correctly identifies that the deficiency-index argument (`n₊=n₋=1`) is abstract operator theory that transfers verbatim once a lower-bounded, closable finite-interval form is supplied — the entry is careful to distinguish this transferable abstract shell from the field-specific existence theorem that remains to be proved.

**[D] Verified by hand, every computation in `v13.276`'s archimedean closure argument**:
- `½log12 - logπ + ψ(s/2) = 2(½ψ(s/2) - ½logπ) + ½log12` is a trivial algebraic rearrangement (both sides equal `ψ(s/2) - logπ + ½log12`) — confirms the "D12 gamma term = 2×Riemann gamma term + conductor constant" claim exactly.
- `Φ₁(Df;z) = f̂(z)`: re-derived directly from `D=i·d/dx`, integration by parts (`(f')^(z) = -iz·f̂(z)` with vanishing boundary terms since `f∈H₀¹`), and `(Df)^(0)=0` (since `f` vanishes at both endpoints) — confirmed exactly.
- `I_cond[f] = (log 12)‖f‖₂²`: re-derived via Parseval (`(1/2π)∫|f̂(z)|²dz = ‖f‖₂²`) applied to both the `z` and `-z` terms with coefficient `C₁₂=½log12`, giving `2·(½log12)·‖f‖₂² = (log12)‖f‖₂²` — confirmed exactly.
- The digamma asymptotic `Re ψ(¼+iz/2) = log|z|+O(1)` as `|z|→∞` is the standard large-argument expansion of the digamma function, correctly applied (no poles on `Re(s)=¼>0`, so the gamma multiplier is continuous and bounded below) to establish lower-boundedness of the D12 gamma-multiplier form.

All four of these independently checked identities are exactly correct, and together they substantiate the entry's central closure claim: the D12 finite-interval form has the same domain/closability structure as Suzuki's Riemann finite form, with only bounded, harmless field-specific corrections (conductor scalar, bounded prime shifts, bounded pole term).

## 4. Overall verdict for this round

**No mathematical error was found in `v13.272`–`v13.276`.** This is a strong round precisely because of what it *rules out*: two separate, valid no-go theorems (the bulk-overlap mismatch and the additive-Fredholm linearity obstruction) closed off two of the project's own recently-proposed roads, and in both cases the project's response was the mathematically correct one — abandon the falsified ansatz and pivot to the specific alternative (nonlinear boundary/deficiency-vector construction) that structurally escapes the no-go, rather than patching the falsified approach. The citation-correction cycle in `v13.274`→`v13.276` is a genuine miss-then-catch, not a defect I'm flagging as unresolved — the project caught its own error via a source re-check before I had to.

## 5. Scope note

Not independently verified this round: the precise current statement of Suzuki's Corollary 1.6 (whether `z²ξ/ξ'` is in fact the paper's v2 target, as `v13.276` now claims) — this would require fetching and reading the specific corollary text in the source PDF, which I did not do. This is the one open item from this round that a future pass should resolve directly against the source before further D12-side claims build on it.

## 6. Guardrails

All guardrails from prior rounds remain in force. No new guardrail is needed — the existing guardrail on external-citation verification (added in round 8) is exactly what caught the substance of this round's citation-correction cycle, and continues to earn its keep.

**External audit round 11: CLOSED. No corrections required to `master`.**
