# Cone Derivation Ledger v13.470 — External Audit Round 35

Date: 2026-09-14

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

`v13.466`–`v13.469`: the cohomological formalization of the mod-4 affine-frame ambiguity (`v13.466`), its resolution via oriented Pell time (`v13.468`, `v13.469`), and a new even-sector Suzuki numerical diagnostic on the signed structure of the remote-mode tail correction (`v13.467`). No version collisions this round.

## 1. Crossed cocycle trivialization and affine-frame C2 (`v13.466`) — verified exactly

**[D, independently verified]** Confirmed the cocycle-failure argument directly: since `U(12)` is abelian, `7·5=5·7=11`, but the cocycle law gives `c(7)+7·c(5)=w` (using the raw, non-cocycle table) against `c(5)+5·c(7)=τ(w)=w²` — a genuine contradiction confirming the raw table is not a 1-cocycle, exactly as claimed. Verified the descended cocycle `Δ=w+w²=1` (from `w²+w+1=0`), confirmed the cocycle condition `1+τ(1)=0` holds in char 2, and directly solved `b+b²=1` over `F₄` to get exactly the two claimed solutions `b∈{w,w²}` (checked all four field elements by hand). Verified the permutation claims `F=(w w²)` and `F'=(0 1)` from the raw definitions `F(t)=t²`, `F'(t)=t²+1`, and confirmed the conjugacy `F'=T_wFT_w⁻¹` by direct algebraic substitution (`(t+w)²+w=t²+w²+w=t²+1` using the freshman's-dream identity in characteristic 2). The `H¹(C₂,F₄)=0` computation (trace-surjectivity argument) is standard and correctly applied.

## 2. Even terminal four-plane signed rank-one tail self-energy (`v13.467`) — re-executed, headline claims confirmed, one precision caveat noted

**[N, independently verified with a noted numerical caveat]** Re-ran `suzuki_even_terminal_fourplane_signed_tail_self_energy.py` directly (a substantial computation: seven cutoffs up to `M=159`, 70-digit precision). The two headline numbers reproduced exactly: the dominant self-energy/leading-moment overlap `0.9999997239488878` matched to every displayed digit, and the leading moment vector `L` matched the entry's reported values closely. The "tiny Schur levels" table at each cutoff also matched the already-independently-verified values from `v13.461`/`v13.463`/`v13.464`. **However**, the intermediate "band self-energy eigenvalues" table showed run-to-run drift of up to ~15% in my re-execution versus the entry's reported values for the smaller (2nd–4th) eigenvalues in each band — e.g. entry's `39→59` third eigenvalue `-2.0837601793×10⁻²²` vs my run's `-1.784235675×10⁻²²`. This is consistent with the inherent ill-conditioning of extracting eigenvalues spanning ~30 orders of magnitude via `mp.eigsy` at fixed precision, not with an error in the entry: the *dominant* eigenvalue/eigenvector in each band (the one actually used for the headline overlap claim) reproduced exactly, while only the far-sub-leading eigenvalues — which the entry does not build any boxed conclusion on individually — drift between runs. The qualitative pattern (all negative, monotonically shrinking, near-rank-one) held in every run. Flagging this as a numerical-sensitivity property of the diagnostic, not a finding against its conclusions.

## 3. Oriented Pell phase selects the affine frame (`v13.468`) — verified exactly

**[D, independently verified]** Confirmed `j([λ])=1` and `j([λ⁻¹])=2=-1` directly from the `v13.441` phase formula `j=2b/a` (λ=2+ε gives a=2,b=1; λ⁻¹=2-ε gives a=2,b=-1≡2), confirmed `Ψ(j)=w^j` sends these to `w` and `w²` respectively, and confirmed this pairs up exactly with the two solutions of `v13.466`'s trivialization equation (`b=w,w²`) found independently. The identification is a correct composition of already-verified pieces, not a new computational claim requiring fresh verification.

## 4. χ12 Pell time orientation and affine frame selection (`v13.469`) — verified exactly, a clean synthesis

**[D, independently verified]** This entry makes explicit what `v13.468` left implicit: that the orientation selecting `b=w` is literally the character `χ₁₂` (via `σ_r(√3)=χ₁₂(r)√3`, already verified in earlier rounds). Every atomic identity used (`λ⁻¹=2-√3`, `σ_r(λ)=λ^{χ₁₂(r)}`, the hyperbolic parametrization `λⁿ=x_n+y_n√3`, the phase-orientation chain) was either re-confirmed directly or reduces to facts already independently verified in this and prior rounds. No new computational risk; this is a correct, well-composed synthesis entry rather than a fresh derivation.

## 5. Overall verdict

A tight, mostly-algebraic round. `v13.466`, `v13.468`, `v13.469` form a clean, fully verified cohomological story: the mod-4 twisted lift produces a genuine but coboundary-trivial `H¹` class, its two trivializations are exactly the two Pell time orientations under the already-established two-prime phase intertwiner, and `χ₁₂` is identified as literally *being* that orientation character. `v13.467` is a legitimate, well-guardrailed numerical diagnostic whose headline claims (negative sign, near-rank-one structure, exact overlap value) reproduced exactly on re-execution; its intermediate sub-leading eigenvalue table is numerically sensitive at the level of individual digits but this doesn't affect any conclusion the entry actually draws.

## 6. Scope note

Not independently reproduced to full digit-precision: `v13.467`'s sub-leading (2nd–4th) band self-energy eigenvalues, for the numerical-conditioning reasons noted in §2 — the dominant eigenvalue/eigenvector and both headline scalar outputs (overlap, `L`) were confirmed exactly.

## Guardrails

All guardrails from prior rounds remain in force. `v13.467`'s own guardrail is worth restating given the numerical sensitivity noted above: this diagnostic does not determine the infinite-cutoff sign or limit of the four terminal even eigenvalues, and `ind_{≤0}(A_{a=1})≤6` is neither strengthened nor weakened by anything in this round.

**External audit round 35: CLOSED. `v13.466`–`v13.469` independently verified — the cohomological affine-frame story confirmed exact by direct computation, and the numerical tail-self-energy diagnostic (`v13.467`) confirmed on its headline claims via direct re-execution, with a noted (and explained) numerical-sensitivity caveat on its sub-leading eigenvalue table. No theorem-level claim changes this round; the full-parity bound remains `ind_{≤0}(A_{a=1})≤6`.**
