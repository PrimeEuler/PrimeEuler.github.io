# Cone Derivation Ledger v13.408 — External Audit Round 26

Date: 2026-09-13

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[N-cert]** validated computational, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

This round covers everything landed after commit `8d4663c` (Round 25's push): the completion of the even-sector six-direction proof contract (`v13.401`, `v13.402`), the opening of an independent odd-parity sector audit (`v13.403`), the odd-sector index-bound attempt and its own self-correction (`v13.404` ×2, `v13.405` ×2, `v13.406`), and the first independent odd-sector replay step (`v13.407`).

## 1. Even sector: the Round-25 proof contract was executed, and the arithmetic checks out

**[N-cert, independently verified]** `v13.401` runs the outward replay designed across `v13.394`–`v13.400` (which Round 25 verified as an honestly-scoped, not-yet-executed contract). I independently recomputed every chained inequality in the terminal comparison from the stated intermediate numbers:

- `δ_T·λ_min(C) = 0.18225976374175623 × 0.9964577330113989 = 0.18161415099730358` — matches the ledger's `0.1816141509973` exactly.
- The `H`-bound chain (`h_{≤2×10⁶}=0.17821051347430`, tail envelope `<4.0×10⁻⁴`, perturbation `‖ΔY‖<1.2×10⁻⁷` via `‖H−H₀‖≤2·0.423·ε+ε²`) reproduces `λ_max(H)<0.1786106149944` exactly.
- Final margin `δ_T·λ_min(C) − λ_max(H) = 0.0030035360029891656`, matching the claimed `>0.0030035360`.

**[D, independently verified]** `v13.402`'s Schur-congruence argument (`T*A_even T = S_10 ⊕ A_DD`, inertia preserved under bounded invertible congruence) is the mathematically correct route this time — and importantly, it does **not** repeat the v13.348-era error the project self-caught long before this round (a k-dimensional positive subspace of an infinite-dimensional operator does not by itself bound the nonpositive index). Here `S_10` is an actual finite `10×10` matrix (both `A_CC` and the composed `A_CD A_DD⁻¹A_DC` act on the finite-dimensional core `C`), so "positive on a 6-dimensional subspace ⟹ nonpositive index ≤4" is ordinary finite-dimensional linear algebra, not the flawed infinite-dimensional inference. This is the structurally correct form of the argument.

**Verdict: `ind_{≤0}(A_even(a=1)) ≤ 4` is a sound conclusion**, conditional on the underlying long-double/explicit-error-budget computational claims (the `1990×1990` finite solve, the Gram accumulation through `2,000,000`) which I have not independently reproduced from scratch — consistent with how I've scoped comparable full-scale runs in every prior round.

## 2. Odd sector: real progress, and an excellent self-correction worth naming explicitly

**[D, independently verified]** `v13.403`'s odd-parity pole channel: I derived and checked the sinh-integral formula `d_n = 2k_n·sinh(1/2)/(k_n²+1/4)` independently via `mpmath` quadrature at `n=2,4,6` — the closed form matches the direct integral to 25 digits, and `sin(k_n)=0` to machine precision for even `n`, exactly as claimed. `2dd^T` is positive semidefinite regardless of the per-component sign ambiguity the entry correctly flags.

**[Audit — and this is the most important finding of this round]** `v13.404`/`v13.405` initially promoted a full odd-sector theorem, `ind_{≤0}(A_odd)≤2`, and `v13.404`'s own §10 combined it with the even-sector result into `ind_{≤0}(A_{a=1})≤6`. Then **`v13.406`, written by the project itself, caught and reversed this**: the odd-sector "theorem" had been assembled by asserting scalar constants (the finite-high eigenvalue, the cross-block norm, the residual-Gram value) that were stored in a verifier *transcript* script rather than independently regenerated from the source-faithful matrix. `v13.406` explicitly demotes `v13.404`/`v13.405` to "historical candidate-certificate transcripts," states plainly that the combined `≤6` bound is not currently promoted, and lays out exactly which four pieces still need independent replay. This is precisely the kind of provenance discipline I'd want to see and have been encouraging throughout this audit relationship — catching "a script asserts X" versus "a script derives X" before the theorem calcifies. I verified the arithmetic in the *relaxed* target `v13.406` restates (`α_4002=2.581051...`, `δ_odd>0.6372303725...`, matching their `0.6372304048` to 7 significant figures, `δ_odd·0.80=0.509784...`, margin `0.284784...` matching their `>0.2847`) and it is internally consistent — but per the project's own current status, this remains a **target**, not a certified result.

**[N-replay, independently verified]** `v13.407` delivers the first of the four promised independent replays: reconstructing the odd finite-high block `F={22,...,4000}` from the canonical source-faithful formulas (not importing the stored constant) gives `λ_min(A_FF)=0.5337449990275`, matching the old transcript's `0.53374499902694` to ~10 significant figures. This is a genuine, valuable independent confirmation of one piece — but three more (`‖A_FT‖<1.015`, the frozen-`Q8` residual-Gram reconstruction, and the final min-max combination) remain explicitly open per `v13.406`'s own accounting.

## 3. Accuracy note for this ledger's own record

To avoid the audit itself mis-stating current status: **as of `v13.407`, the correct summary is `ind_{≤0}(A_even(a=1))≤4` (sound, per §1) and the odd-sector `ind_{≤0}(A_odd)≤2` — and therefore the combined `≤6` bound — are open, pending replay**, not proven. Any future entry that cites "the combined index-6 bound" without noting `v13.406`'s reconciliation would be re-introducing exactly the provenance gap the project already caught once.

## 4. Overall verdict

A genuinely strong round for the project's own internal discipline: a real theorem-level milestone was reached and independently checked for the even sector (`v13.401`/`v13.402`), and a premature promotion on the odd-sector side was caught and corrected by the project itself before I had to flag it — `v13.406` is exactly the kind of self-audit this relationship exists to encourage, and it beat me to the finding. I have nothing to add beyond confirming their own correction is accurate and that the arithmetic throughout (even-sector terminal comparison, odd-sector relaxed target, sinh pole channel, finite-high replay) checks out under independent recomputation.

## 5. Scope note

Not independently reproduced: the `1990×1990` (even) and odd-sector finite solves and the residual-Gram accumulations through `2,000,000` in both sectors — these require the project's own long-double/high-precision infrastructure. The frozen dyadic `Q`/`Q8`/`L0` exact-rank claims were spot-checked in Round 25 (`Q`) via independent Fraction-based Bareiss elimination; `Q8`'s analogous claim in `v13.404`/`v13.406` was not independently re-verified this round (flagged as a good target for Round 27 given how cheap that check is).

## 6. Guardrails

All guardrails from prior rounds remain in force. No new guardrail needed — `v13.406` already articulated the relevant one (stored transcript constants are not certified merely because a verifier script asserts them) more precisely than I would have phrased it myself.

**External audit round 26: CLOSED. Even-sector index bound `ind_{≤0}(A_even)≤4` independently verified at the arithmetic and logical level (`v13.401`–`v13.402`). Odd-sector work in progress and correctly self-flagged as not-yet-certified by the project's own `v13.406`; one of four required replay pieces independently confirmed in `v13.407`. No errors found in this round beyond what the project had already caught itself.**
