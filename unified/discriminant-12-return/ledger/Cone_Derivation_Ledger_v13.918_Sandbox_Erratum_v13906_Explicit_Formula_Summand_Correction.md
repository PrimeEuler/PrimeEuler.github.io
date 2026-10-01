# Cone Derivation Ledger v13.918 — Sandbox Erratum to v13.906 §2: the Explicit-Formula Summand Is a Product, Not a Square

Date: 2026-10-01

Author: LIttle Euler (sandbox track). Authorization: project owner, 2026-10-01 ("yes ledger that").

Predecessors: v13.906 (the entry corrected here); v13.915 §1 / v13.916 (Round 135, whose open G₋ ≥ 0 question this erratum's provenance touches — see §5).

Current live predecessor at write time: v13.917. Collision check performed immediately before write.

## 1. The error [D]

v13.906 §2 states, marked "[D, standard]":

> For this F, F̂(ρ) = |∫u'(x)e^{(ρ−1/2)x}dx|². Hence Q_full(u,u) = Σ_ρ |∫_{−a}^{a} u'(x) e^{(ρ−1/2)x} dx|², sum over all nontrivial zeros ρ of ζ.

This is incorrect as stated. For F = u' ⋆ ũ' (ũ' the reversal), the Fourier–Mellin transform factors as

> F̂(s) = û'(s) · û'(1−s),   û'(s) := ∫u'(x)e^{(s−1/2)x}dx,

hence

> **F̂(ρ) = û'(ρ) · û'(1−ρ)**  [D]

— a product, not a square. For real u', overline{û'(ρ)} = û'(ρ̄), so |û'(ρ)|² = û'(ρ)û'(ρ̄); the product equals the square iff ρ̄ = 1−ρ, i.e. iff ρ is on the critical line. The corrected identity is therefore

> Q_full(u,u) = Σ_ρ û'(ρ)·û'(1−ρ),  sum over all nontrivial zeros ρ of ζ.  [D]

The Guinand–Weil step itself (Σ_ρ F̂(ρ) = explicit-formula RHS; Suzuki's g built so ∫∫g(x−y)u'(x)u'(y)dxdy equals that RHS) is unaffected — only the factored form of the summand was misstated.

## 2. How it was found

During the authorized sandbox attack on G₋ ≥ 0 (2026-10-01; report `runs/20260930-divisor-tension/g_minus_positivity.md`, sandbox only, not ledgered). The attack needed the summand's exact form; the "manifest sum of squares" reading would have made positivity unconditional — which would prove RH by Weil's criterion — and that contradiction flagged the factorization. Direct computation (above) confirmed the product form.

## 3. Impact on v13.906: the [D] conclusion stands [D]

v13.906's Step 2 (§3) never used squareness — only the decay bound. Writing ρ−1/2 = β+iγ with β ∈ [−1/2,1/2] (critical strip, unconditional), each factor satisfies |û'(ρ)| = O(e^{a|β|}(1+|γ|)^{−N}) for every N (Paley–Wiener/integration by parts, u' ∈ C_c^∞(−a,a)), so the product satisfies the same O(|γ|^{−2N}) bound up to the bounded factor e^{a}. Every nontrivial zero still satisfies |Im(ρ)| ≥ γ₁ ≈ 14.1347 [D, known]. Hence **smoothness ⟹ near-nullity [D] stands exactly as written**, and the saturation conclusion **s_m = c_m [D] is unaffected**. The smoking-gun numerics summed on-line zeros only — unaffected. The explicit two-bump ±1 construction — unaffected.

## 4. What the correction does change [D]

The sum-of-squares *positivity* reading of the identity — Q_full as a manifest sum of nonnegative terms — is **RH-dependent, not unconditional**. Off the critical line the summands û'(ρ)û'(1−ρ) have indefinite sign and no unconditional argument controls them. v13.906 never claimed Q_full ≥ 0 and never needed it; this section records the boundary so no later entry leans on the misstatement for a lower bound.

## 5. Note for the audit thread (pointer, not a ledgered claim)

Round 135 (v13.916) leaves analytic G₋ ≥ 0 as "the single highest-value remaining step." The sandbox attack that produced this erratum found the obstruction is exactly §4's point: the Guinand–Weil summand for the odd sector is likewise a product, indefinite off the line, and the available proof goes through RH (oddness makes every critical-line term a manifest square B(γ)² ≥ 0). Verdict in the sandbox report: RH-hard. Details are in `runs/20260930-divisor-tension/g_minus_positivity.md` — **sandbox only, no claim entered into the ledger by this entry**; recorded here so the audit thread does not spend verification budget re-deriving the obstruction.

## Result

\[
\boxed{\textbf{v13.906 §2's summand is corrected from } |\cdot|^2 \textbf{ to the product } \hat u'(\rho)\hat u'(1-\rho)\textbf{. The entry's estimates, numerics, construction, and its } s_m=c_m\ \textbf{[D] conclusion are unchanged; only the (never-used) sum-of-squares positivity reading is withdrawn as RH-dependent.}}
\]
