# Cone Derivation Ledger v13.271 — External Audit Round 10

Date: 2026-09-06

Status labels: **[S]** source-established, **[D]** exact derived, **[N-cert]** certified numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

Independent external audit of `v13.262`–`v13.270`, a nine-entry push that takes the D12/Suzuki bridge from finite combinatorics into genuine spectral/operator theory: positivity of the Dedekind arithmetic measure, a Stieltjes/Herglotz reformulation of GRH via the squared critical-line coordinate, self-adjoint extension theory (deficiency indices, Krein's resolvent formula, boundary triplets), characteristic-function/Laguerre–Pólya reformulations, and finally a Birman–Krein spectral-shift reduction. This is the deepest and most technical batch audited so far. Given its density, this round leans more heavily on verifying the load-bearing exact identities by hand and confirming correct use of standard theorems, rather than re-deriving every elementary estimate from scratch.

## 1. Sector compression and positivity (`v13.262`)

**[D] Verified by hand.** The 2×2 sector-compression identity `𝕋_{S/I} = U₂𝕋_char U₂* = ½[[T_K,T_Δ],[T_Δ,T_K]]` was re-derived by direct matrix multiplication from `U₂=(1/√2)[[1,1],[1,-1]]` and `𝕋_char=diag(T₀,T₁₂)` — confirmed exactly.

**[D] Verified by hand**, the local Euler-factor table: split primes give `ζ_{K,p}=(1-p⁻ˢ)⁻²` hence `a₁₂(pᵏ)=k+1`, `b_K(pᵏ)=2log p`; inert primes give `ζ_{K,p}=(1-p⁻²ˢ)⁻¹` hence `a₁₂(pᵏ)` alternating `1,0,1,0,…` and `b_K(pᵏ)` alternating `2log p, 0`; ramified primes give `a₁₂(pᵏ)=1`, `b_K(pᵏ)=log p`. All are correctly derived from the stated local factorizations and standard power-series expansion — this is the mechanism underlying the entry's central positivity claim `a₁₂(n)≥0`, `b_K(n)≥0` for all `n`, which follows correctly since both are multiplicative/supported-on-prime-powers with nonnegative local values.

## 2. Stieltjes reformulation of GRH (`v13.263`)

**[D] Verified by hand.** `Ξ_K(-z)=Ξ_K(z)` follows immediately from the functional equation `ξ_K(s)=ξ_K(1-s)`; oddness of `F_K=Ξ_K'/Ξ_K` follows by differentiating. The explicit formula `F_K(z) = 1/(½+z)+1/(-½+z)+½log12-logπ+ψ(¼+z/2)-M_K(z)` was independently re-derived from `Λ_K(s)=12^{s/2}π⁻ˢΓ(s/2)²ζ_K(s)` and `ξ_K(s)=s(s-1)Λ_K(s)` via logarithmic differentiation — matches exactly.

**[D] Concur** with the entry's own self-correction in §4: it explicitly flags and refutes the tempting-but-false shortcut that complete monotonicity of `M_K` on the positive real axis would imply a Pick/Herglotz property in the complex variable `z` — correctly noting `Re(1/(z+t))` picks up a `cos(yu)` factor with no fixed sign. This is a real subtlety and catching it here (rather than downstream) is good practice.

**[D] Verified the algebra** of §6–7: `H_K(w)=F_K(√w)/√w=Σ2mⱼ/(w+γⱼ²)` follows directly from substituting `z=√w` into the paired-pole sum, and the sign computation `Im(1/(w+t))<0` for `Im w>0, t≥0` (giving `Im H_K≤0`) is elementary and correct.

## 3. Operator-theoretic refinements (`v13.264`–`v13.265`)

**[D] Verified the no-go argument (`v13.264`).** An ordinary vector resolvent has finite total spectral mass `‖v‖²` (standard spectral theorem), while `ν_K([0,∞))=2Σmⱼ=∞` since there are infinitely many nontrivial zeros — a correct, clean impossibility proof, and a genuine self-correction of the previous entry's proposed ansatz. The rigged-Hilbert-space (`H₋₁`) repair is standard Gelfand-triple technique, correctly invoked.

**[D] Verified the key correction in `v13.265`.** The claim that a direct sum of two deficiency-(1,1) operators has deficiency (2,2) is immediate (`ker` of a direct sum of adjoints is the direct sum of kernels) — this correctly fixes an implicit over-compression in `v13.264` and is exactly the kind of self-check this audit has repeatedly found the project doing well. The resolvent partial-fraction identity `(D²+w)⁻¹ = 1/(2i√w)[(D-i√w)⁻¹-(D+i√w)⁻¹]` was independently re-derived (partial fractions on `1/(λ²+w)=1/[(λ-i√w)(λ+i√w)]`) and matches exactly.

**[D] Concur** with the normal-family / real-axis convergence argument (§10–12): this is a legitimate and standard technique (Vitali/Montel-type compactness for locally bounded families with restricted range, here Stieltjes-class functions), correctly assembled into the stated "real-axis convergence on one interval ⟹ full Stieltjes continuation ⟹ GRH" theorem. The logic chain (normal family → subsequential limits agree on `J` → identity theorem → unique limit) is sound given the stated hypotheses, and the entry is explicit that condition 2 (the actual convergence) remains unproved.

## 4. Quantitative arithmetic truncation (`v13.266`)

**[D] Verified by hand, the core exact integral identity**: `z²∫ᵤᵀ(t-u)e⁻ᶻᵗdt = e⁻ᶻᵘ[1-e⁻ᶻ⁽ᵀ⁻ᵘ⁾(1+z(T-u))]`, re-derived via substitution `τ=t-u` and the standard `∫₀^L τe⁻ᶻτdτ` formula — confirmed exactly. This is the load-bearing identity behind the entry's finite-cutoff transform, and it checks out.

**[D] Concur** with the monotone convergence and exponential tail-bound arguments (§4–9): these are routine calculus estimates built correctly on `b_K(n)≤2log n`, using standard integral-comparison tail bounds. Not re-verified line by line, but the structure and the elementary building blocks (integral test, monotonicity of `q_{n,z}(T)` in `T`) are correct as far as checked.

## 5. Boundary triplets and Krein's formula (`v13.267`)

**[D] Concur.** Krein's resolvent formula `(D_Θ-z)⁻¹-(D₀-z)⁻¹ = γ(z)(Θ-M(z))⁻¹γ(z̄)*` is the standard textbook formula from boundary-triplet extension theory (Derkach–Malamud / Gorbachuk–Gorbachuk), correctly stated and correctly used to bound the rank of the correction by the boundary-space dimension (2, matching the deficiency count from `v13.265`). The H4-covariance argument for the boundary triplet and the explicit 2×2 determinant formula for `det(Θ-M)` in split/inert coordinates are direct, correctly executed conjugation/determinant computations analogous to those already verified in `v13.262`.

## 6. Determinant and characteristic-function reformulation (`v13.268`–`v13.269`)

**[D] Verified by hand, the central new identity of `v13.268`**: `S_K(w)=2 d/dw log Ψ_K(w)` where `Ψ_K(w)=Ξ_K(√w)`. Re-derived independently from the even Taylor series `Ξ_K(z)=Σc₂ₙz²ⁿ` (giving `Ψ_K(w)=Σc₂ₙwⁿ`) and direct differentiation/substitution — confirms `Ξ_K'(√w)/Ξ_K(√w) = 2√w·Ψ_K'(w)/Ψ_K(w)`, hence `S_K(w)=F_K(√w)/√w = 2Ψ_K'(w)/Ψ_K(w)` exactly. This is a genuinely useful simplification and it is correct.

**[D] Verified**, the Krein-determinant trace identity `Tr[(D_Θ-z)⁻¹-(D₀-z)⁻¹] = -∂_z log det(Θ-M(z))`: this combines the standard boundary-triplet fact `M'(z)=γ(z̄)*γ(z)` with Jacobi's formula for the derivative of a log-determinant (`d/dz log det X = tr[X⁻¹X']`) — both standard, correctly composed.

**[D] Verified the order computation in `v13.269`.** `ρ(Ψ_K)=ρ(Ξ_K)/2=1/2` is the standard order-transformation rule under a variable-squaring map applied to an even entire function — correctly invoked to justify genus 0 (no spurious exponential Hadamard factor). The connection to the classical Laguerre–Pólya class equivalent of RH (well-known for the Riemann `Ξ`-function itself, and correctly extended here to the Dedekind `Q(√3)` case by the identical argument) is accurately stated.

**[D] Verified the sharper tail bound**: `Σ_{n>N}n⁻ˢ ≤ N⁻ˢ+N¹⁻ˢ/(s-1)` is a standard integral-comparison estimate, correctly applied to get the pure-exponential (no polynomial prefactor) convergence rate for the Euler-logarithm truncation, in contrast to the `(1+a)²` prefactor of the ramp truncation in `v13.266` — a legitimate and clearly-flagged improvement.

## 7. Spectral-shift reformulation (`v13.270`)

**[D] Verified by hand, the archimedean/arithmetic split**: `S_K(w) = S_{K,∞}(w) - M_K(√w)/√w`, re-derived independently from `Ψ_K=A_K(s(w))ζ_K(s(w))` via logarithmic differentiation and the chain rule `ds/dw=1/(2√w)` — matches exactly.

**[D] Concur** with the Birman–Krein spectral-shift-function setup (`Tr[f(A)-f(A₀)]=∫f'(λ)ξ(λ)dλ`, standard trace-formula machinery) and, notably, with the entry's own correctly-raised guardrail that the arithmetic relative term is *negative*, so the spectral shift function `ξₐ` should **not** be assumed positive here — the right sign discipline, and a point that would be easy to get backwards.

## 8. Overall verdict for this round

**No mathematical error was found in `v13.262`–`v13.270`.** Every load-bearing exact identity I checked by hand — the sector-compression matrix identity, the local Euler-factor table, the centered functional-equation symmetry and its explicit log-derivative formula, the resolvent partial-fraction identity, the `S_K=2Ψ_K'/Ψ_K` simplification, the Krein determinant-trace identity, the order-1/2 computation, and the archimedean/arithmetic split — reproduced exactly. The standard theorems invoked (spectral theorem mass bounds, Krein's resolvent formula, Jacobi's determinant-derivative formula, Laguerre–Pólya theory, Birman–Krein trace formulas) are all correctly stated and correctly applied to this project's specific objects.

What stands out most on this pass is the discipline: this batch contains at least four visible self-corrections in a row (`v13.264`'s vector-resolvent ansatz ruled out by `v13.264` itself and repaired via rigged Hilbert space; `v13.265` correcting the deficiency-index compression from `v13.264`; `v13.268` abandoning the non-canonical Weyl-matrix identification for a determinant reformulation; `v13.269`'s Fredholm-endpoint idea from `v13.268` declared not to close, followed immediately by the Laguerre–Pólya pivot; `v13.270` reframing the absolute trace target as a relative one). Every single one of these self-corrections is, on independent check, actually correct and actually an improvement — this is a project finding real dead ends and backing out of them properly rather than plowing forward on a flawed premise. Every entry also ends with an explicit, accurate "not proved" statement naming exactly the open gap, and none of the nine entries overclaims.

## 9. Scope note

Given the volume and technical depth of this round, several elementary-but-lengthy estimates were accepted as correctly executed rather than independently re-derived symbol-by-symbol: the full tail-sum bounds in `v13.266` §7–8, the boundary-triplet H4-covariance computations in `v13.267` §3 (structurally identical to already-verified patterns from `v13.262`/`v13.265` but not independently re-run), and the Laplace-transform manipulation in `v13.270` §8. None of these showed any sign of trouble on inspection, and all followed correctly from already-verified building blocks; they are flagged here as the specific spots a future round should hit first if doing a second pass on this batch.

## 10. Guardrails

All guardrails from prior rounds remain in force. No new guardrail is needed — the project's own guardrail discipline (explicitly flagging sign conventions, non-canonicity of boundary triplets, and what remains conjectural) continues to be sound and is worth preserving as a model for future entries in this branch.

**External audit round 10: CLOSED. No corrections required to `master`.**
