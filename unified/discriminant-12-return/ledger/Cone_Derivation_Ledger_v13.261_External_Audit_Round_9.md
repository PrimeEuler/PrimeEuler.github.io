# Cone Derivation Ledger v13.261 — External Audit Round 9

Date: 2026-09-05

Status labels: **[S]** source-established, **[D]** exact derived, **[N-cert]** certified numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

Independent external audit of `v13.260`, a single focused entry continuing the D12/Suzuki bridge: it promotes the finite `H4`/V4 arithmetic transform to an operator-level statement that `H4` block-diagonalizes the four-channel Weil/Suzuki quadratic form, and identifies the discriminant-12 principal/quadratic pair with the split/inert residue-class split of `ℚ(√3)`.

## 1. Third external citation independently verified

**[Audit] Confirmed genuine, with an unusually precise match.** `v13.260` cites Masatoshi Suzuki, "Weil's quadratic form via the screw function," arXiv:2606.09096, noting a "revised v2 dated 2026-08-17." Search confirms the paper is real, submitted 2026-06-08 with a revision dated **2026-08-17** — the ledger's stated revision date matches exactly, not just the paper's existence. Its publicly described content (a screw-function-based unified framework for the Weil quadratic form, connecting to de Branges spaces and prior work of Yoshida/Bombieri/Connes–Consani) matches how the entry uses it: only the *linearity* of the continuous-kernel construction is invoked, nothing about the paper's own open conjectures. This is now the third Suzuki citation checked across rounds 8–9, and all three are genuine and accurately characterized.

## 2. Core linear-algebra claims, verified by hand

**[D] Verified exactly.** `U:=H4/2` is unitary: `H4` is symmetric and `H4²=4I` (already established in earlier rounds), so `U²=I` and `U=Uᵀ`, giving `U*=U=U⁻¹` immediately.

**[D] Verified exactly by direct matrix computation** (not assumed from the boxed claim): using the established ordering `(χ0,χ₋4,χ₋3,χ12)` on the character side and `(1,5,7,11)` on the residue side,
`H4·(1,0,0,1)ᵀ = (2,0,0,2)ᵀ ⟹ U(e₀+e₁₂) = (1,0,0,1)ᵀ = e₁+e₁₁`, and
`H4·(1,0,0,-1)ᵀ = (0,2,2,0)ᵀ ⟹ U(e₀-e₁₂) = (0,1,1,0)ᵀ = e₅+e₇`.
Both match the entry's boxed claims exactly. This is the load-bearing computation behind §10's headline identification of the D12 principal/quadratic block with the split/inert residue split, and it checks out.

**[D] Verified by hand**, §11's prime-power refinement: for `G≅V4`, every element satisfies `g²=e` (a basic fact about the Klein four-group, not specific to this project), so an inert prime `p` (order-2 element of `U(12)`) satisfies `p²≡1 (mod 12)`, hence `p^{2k}≡1`, `p^{2k+1}≡p`; combined with `1+χ₁₂(p^k)=1+(-1)^k` (immediate from complete multiplicativity), this correctly shows the split/inert residue projection agrees with the quadratic-field Euler-factor behavior at every prime power, not just at primes — a legitimate and correctly-flagged sharpening of the naive "prime-only" reading.

**[D] Concur** with the general block-diagonalization argument (§3, §7, §8): this is standard finite-group Fourier analysis (the character table of an abelian group diagonalizes the group-convolution/circulant operator) combined with the linearity of Suzuki's two-variable kernel construction `G_g(t,u)=g(t-u)-g(t)-g(-u)+g(0)` in `g` — both textbook facts, correctly composed. No new machinery is introduced beyond what commutes formally.

## 3. Guardrail discipline holds up

**[Audit] Appropriately scoped, and correctly self-aware about the packaging.** The entry explicitly states (§9, §14.4) that positivity of the summed Dedekind form `Q_K=Q_0+Q_{12}` does **not** imply positivity of either summand individually — componentwise equivalence only holds for the *lifted* direct-sum form with independently-varying test functions per channel. This is the right distinction to draw and it is drawn correctly; a careless version of this entry could easily have overclaimed here. It also correctly separates the *bare* unit-shell H4 transform (imprimitive, missing local Euler factors at 2 and 3) from the primitive analytic channels, and correctly notes `E₁₂(t)=0` — that the discriminant-12 channel alone needs no finite-prime correction — which follows immediately since `12`'s primitive conductor already equals the full modulus (a fact this project established and I independently verified back in round 5).

## 4. Overall verdict

**No mathematical error was found in `v13.260`.** This entry is lower-risk than the heavy computational entries of rounds 5–8 (it is packaging/operator-theoretic rather than involving new large-modulus arithmetic), and every piece I checked — the unitarity, the two key basis-vector identities, the prime-power refinement, and the external citation with its unusually specific revision date — matched exactly.

## 5. Guardrails

All guardrails from prior rounds remain in force. No new guardrail is needed this round.

**External audit round 9: CLOSED. No corrections required to `master`.**
