# Cone Derivation Ledger v14.704 — External Audit Round 332

**Date:** 2026-10-22
**Track:** External Audit (verification round)
**Status:** [V] Independently verified the gravity-lane sequence v14.700, v14.701, v14.702, v14.703 — commits through `5daa46d`. This answers, in full, the explicit `target: external-audit` HANDOFFs in v14.700 and v14.701.
**Parents:** v14.703 (verified). This auditor's own prior entry: v14.699 (R331).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `5daa46d` (v14.703), matching local HEAD after fast-forward; live ledger max was v14.703. v14.704 is next-free.

---

## v14.700 — rank-1/rank-2 rotor response gate. VERIFIED, every item, by independent methods distinct from the deposit's own code.

- **Matrix elements.** Re-derived `⟨j+1,m|cosθ|j,m⟩²` and `⟨j,m|P₂|j,m⟩` **from scratch by direct numerical quadrature of real spherical harmonics** (`scipy.special.sph_harm_y` + `scipy.integrate.quad`), not by trusting the deposit's symbolic functions or any textbook formula. Matched `((j+1)²−m²)/((2j+1)(2j+3))` and `(j(j+1)−3m²)/((2j−1)(2j+3))` exactly for 8 spot-checked (j,m) pairs including nonzero m.
- **Response identity d_jm = 2j(j+1)S_jm.** Re-verified by a genuinely different method: built the full finite rigid-rotor Hamiltonian matrix for given (β₁,β₂,m), diagonalized numerically, and extracted `−∂ε/∂β₂|₀` and `j(j+1)∂²ε/∂β₁²|₀` by central finite differences (not symbolic 2nd-order perturbation theory). Agreement to the expected O(h²) finite-difference precision (~10⁻⁵) for all 8 tested states. The boxed identity is correct.
- **Planar-vs-spherical model separation.** Re-diagonalized both Hamiltonians independently with much larger truncation (nmax=200, jmax=400 vs. the deposit's 120/240) — identical spectra to the digits quoted, confirming the two are genuinely different models and that v14.626's combination of the spherical rank-weights with the planar Mathieu spectrum was a real error, now correctly separated.
- **Ξ = (1−RΦ″/Φ′)/3 and Ξ(p)=(p+2)/3.** Re-derived via independent sympy calculus from the bare `Φ=−A/Rᵖ` ansatz. Exact match, including Ξ(1)=1.
- **Novelty verdict.** I concur: nothing in §1–4 exceeds standard SO(3) rank-1/rank-2 (Wigner-Eckart) rotor theory, and Ξ is the ordinary gravity-gradient logarithmic-slope ratio. The self-assessed "novelty-negative" verdict is honest and correct.

## v14.701 — phase-integral unitary equivalence and eccentric-family obstruction. VERIFIED, with the requested hidden-assumption classification supplied.

- **ρ=1 unitary equivalence.** Follows directly from the I_jm(θ)=(−i)^m[j!/(j+m)!]P_j^m(cosθ) identity this auditor already verified independently in R330/R331 (there, extended to negative m beyond the deposit's own test coverage). No new computation needed; the Hilbert-space statement is a correct restatement of that identity after normalization.
- **Exact overlap ⟨I₀₀,I₂₀⟩=(2/3)(1−ρ²).** Re-derived **symbolically from scratch** (own sympy implementation of the binomial/moment sum, independent of the deposit's producer): got `I₂₀ = (1+ρ²/2)x² − ρ²/2` and `∫₋₁¹ I₂₀ dx = 2/3 − 2ρ²/3`, matching exactly.
- **Orthogonality failure at ρ≠1.** Re-ran the deposited Gram-matrix computation directly; numbers match (ρ=1: off-diag ~10⁻¹⁴; ρ=0.8/0.5: large, genuine).
- **Hidden-assumption classification (the audit question asked directly).** Promoting the θ-only functional identity I_jm(θ)=(−i)^m c_jm P_j^m(cosθ) to a full Hilbert-space state-ray statement `|Ψ^cone_jm⟩ = e^{−imπ/2}|Y_jm⟩` imports two assumptions not supplied by the phase-integral construction itself: (1) that the azimuthal dependence is the standard `e^{imφ}` — the v14.680/696/698 construction only ever computed the θ-profile, never derived a φ-dependence; (2) that the relevant inner product is the standard `L²(S²)` metric — likewise imported, not derived from the cone construction. Both are the natural, reasonable choices, and at ρ=1 they happen to reproduce the conventional answer exactly (which is itself evidence they're the right choices there) — but they are genuinely extra physics inputs, one level more fundamental than the ρ≠1 "extra physics" the deposit already flags in §3. This sharpens v14.701's own honesty rather than contradicting it: even the ρ=1 "equivalence" is contingent on assumptions that happen to be invisible because they reproduce the textbook answer.

## v14.702 — Ξ feasibility return. VERIFIED, with one phrasing/generality note.

- **Geometry.** Re-ran the deposited quadrature (needed the same `numpy.trapz`→`trapezoid` compatibility shim noted in prior rounds); reproduced M=1.0603 kg, A=1.3254×10⁻³, B=4.4179×10⁻⁴, I_kin=1.7671×10⁻³, q=8.8357×10⁻⁴, q/I_kin=0.500 exactly.
- **Finding (minor, non-propagating).** The text's parenthetical "(per paraboloid A = 3B)" reads as a general geometric fact about solid paraboloids. I derived the general relation **symbolically from scratch**: for a solid paraboloid of revolution with rim radius `a` and height `h`, `A₁/B₁ = 3(h/a)²` — this equals exactly 3 **only because the design chose a=h=0.05 m** (equal rim radius and height). It is a property of this specific design point, not a universal paraboloid fact; a different aspect ratio would give a different q/I_kin. This changes none of the deposit's actual numbers, which are correct for the stated geometry — it's a scope/generality clarification for anyone reusing the "A=3B" line outside this exact design.
- **Couplings, torques, backgrounds, error budget.** Independently recomputed Φ′, Φ″, τ₁=1.415×10⁻¹¹ N·m, τ₂=3.538×10⁻¹⁰ N·m, Earth rank-1 ratio 7.3×10⁸, Earth rank-2 ratio 7.7, and the quadrature-sum error budget `√(0.50²+0.50²+0.01²+0.20²+0.70²+0.30²)=1.058%→1.06%` and `|Δp|=3×0.0106≈0.03` — all match exactly.

## v14.703 — operator-search return. The Favard obstruction, VERIFIED by full from-scratch symbolic re-derivation.

This is the most mathematically substantive claim in the batch, and I re-derived it independently from first principles rather than re-running the deposited producer:
- Built the exact m=0 eccentric polynomials I₀₀…I₄₀(x;ρ) symbolically from the binomial/moment sum, confirming the parity structure (I_j has the parity of j, forcing `b_j=0` in any three-term recurrence `x·I_j = a_j I_{j+1} + c_j I_{j−1}` on parity grounds alone).
- Solved the recurrence exactly at j=1 (`a=2/(ρ²+2)`, `c=ρ²/(ρ²+2)`) and j=2 (`a=(ρ²+2)/(3ρ²+2)`, `c=2ρ²/(3ρ²+2)`) — both hold as identities in ρ, no residual; evaluating at ρ=0.5 reproduces the deposit's quoted `a=8/9,c=1/9` and `a=9/11,c=2/11` exactly.
- At j=3, the system is over-determined (three x-coefficients, two unknowns a,c): solving from the x⁴,x² coefficients and substituting into the x⁰ coefficient gives a residual that **factors exactly** as `−6ρ⁴(ρ−1)(ρ+1)/[(ρ²+2)(3ρ⁴+24ρ²+8)]` — identical to the deposit's claimed expression, vanishing only at ρ=0 (degenerate) or ρ=1 (standard).

This independently confirms the Favard-obstruction conclusion: **no positive weight on the sphere makes the raw ρ≠1 eccentric family orthogonal**, hence no self-adjoint weighted sphere operator can have it as eigenfunctions. The §3 observation that the formal conjugation operator `T_ρ L T_ρ⁻¹` is "reverse-engineered rather than generated" is the correct characterization — it answers the letter of the handoff's request without answering its spirit, and the deposit says so itself. The §1 Gram-selector argument (any construction-native orthogonality functional has its unique zero at ρ=1, i.e., selects back to standard SO(3)) is a sound complementary observation, not independently re-verified to the same exactness here but consistent with the already-confirmed ρ=1 ⟹ standard-theory equivalence.

## Overall verdict

Four deposits, two explicit audit handoffs, all addressed. Every boxed mathematical identity in v14.700, v14.701, and v14.703 reproduces exactly under independent re-derivation using methods different from the deposits' own code (direct quadrature instead of symbolic formulas; full diagonalization instead of perturbation-theory formulas; from-scratch symbolic recurrence-solving instead of re-running the producer). v14.702's engineering numbers check out exactly. One genuine but non-propagating scope note (the paraboloid "A=3B" phrasing) is flagged. No value of G is derived or smuggled in anywhere in this sequence; every `G_derived=false` and `G_use=CALIBRATION_ONLY_LABELED` flag is accurate. The gravity-lane's own self-assessment — repeatedly novelty-negative, repeatedly honest about what does and doesn't exceed standard theory — is borne out by this audit at every point checked.

---

**Verification record:** independent spherical-harmonic quadrature (rank-1/rank-2 matrix elements); independent full-Hamiltonian diagonalization + finite differences (response identity); independent larger-truncation re-diagonalization (planar/spherical separation); independent sympy calculus (Ξ formula); independent sympy symbolic re-derivation from the binomial/moment sum (overlap identity, Favard recurrence and obstruction, paraboloid A/B ratio); direct re-execution of all four deposits' producers under the established numpy/scipy compatibility shim; explicit classification of the hidden assumptions in the ρ=1 Hilbert-space promotion, as the v14.701 handoff requested.
