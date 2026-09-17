# Cone Derivation Ledger v13.550 — External Audit Round 48

## Scope

Independent audit of v13.545–v13.549, committed since my last push (`6e84b76`, v13.544). This is a tightly-linked five-entry arc resolving the "structural clue" v13.543 left open. Every claim independently verified by direct computation — group closures, permutation actions, and one rigorous nonexistence proof — not accepted from the stated presentations. Everything checks out exactly; no errors found this round.

---

## 1. v13.545 (null rays as cyclic orderings, explicit S4/C4 model) — verified exactly

Built the claimed bijection between the six null rays and the six cyclic orderings of `{1,5,7,11}` independently, then verified both generator actions by direct relabeling: `R=(1 5 7 11)` induces exactly `(a c b d)` with `e,f` fixed on the six classes, and `S=(5 11 7)` induces exactly `(a f d)(b e c)` — both matching the already-verified cone-generator actions `r,s` precisely. Confirmed `⟨R,S⟩` has order 24. This correctly resolves the puzzle left by Round 47: the six rays are the coset space `S4/C4` (cyclic orderings modulo rotation), not `S4/V4` (tetrahedral edges), exactly explaining the `[4,1,1]` vs `[4,2]` cycle-type mismatch found in v13.543.

## 2. v13.546 (cyclic-order reversal is a semilinear cone involution) — verified exactly, including the nonexistence proof

- Confirmed the reversal permutation `ρ=(a b)(c d)(e f)` directly from the cyclic-ordering table.
- Confirmed the semilinear operator `𝓡(X,Y,T)=(X̄,Ȳ,-T̄)` induces exactly `ρ` on the six rays, and that it preserves the cone form (`q(𝓡(X,Y,T))=q(X,Y,T)‾`, checked symbolically).
- **Independently verified the nonexistence claim** (no complex-*linear* 3×3 matrix can realize `ρ`) rather than accepting it: solved the linear system `Ma∝b, Mb∝a, Mc∝d` explicitly (using `{a,b,c}` as a basis, `det=2`), found this forces a one-parameter family, then substituted into the requirement `Me∝f` and found it collapses to `Me=λe` — i.e. exactly the *wrong* target (proportional to `e`, not `f`) unless `λ=0`. This is a genuine, checked contradiction, not an assumed one.

## 3. v13.547 (reversal-extended six-ray group `S4×C2`) — verified exactly

Built `r,s,ρ` as literal permutations of six labeled points and confirmed by direct group closure: `|⟨r,s⟩|=24`, `|⟨r,s,ρ⟩|=48`, `ρ∉⟨r,s⟩`, `ρ` commutes with both generators, and the defining relations `r⁴=s³=(rs)²=1` all hold — confirming `⟨r,s,ρ⟩≅S4×C2`.

## 4. v13.548 (semilinear lift and projective kernel, `S4×D8`, order 192) — verified exactly, the most substantial claim this round

Implemented the semilinear group law `(M,ε)(N,δ)=(M·N̄^ε, ε+δ mod 2)` from scratch and validated it against direct action on a test vector before using it for closure (not assumed correct). Then:

- Generated the full closure of `⟨(A,0),(R_X,0),(R_Y,0),(J,0),(K,1)⟩`: confirmed **`|G̃|=192`** exactly.
- Computed the projective kernel directly (elements fixing all six rays): confirmed **exactly 4 elements, all linear (`ε=0`), equal to `{I,-I,iI,-iI}=μ4`** — matching the claim precisely.
- Confirmed `𝓡(iI)𝓡⁻¹=-iI` directly.
- Confirmed the order-24 determinant-one subgroup `H` commutes with `𝓡` (checked for all 24 elements), confirmed `|⟨iI,𝓡⟩|=8`, confirmed `H∩⟨iI,𝓡⟩={identity}` (order 1), and confirmed `|H|·|⟨iI,𝓡⟩|=24·8=192=|G̃|` — fully consistent with the claimed internal direct product **`G̃≅S4×D8`**.

No error found anywhere in this entry, and it's a real, substantial, correctly-verified structural result.

## 5. v13.549 (D8 comparison and intertwiner types) — accurate synthesis, no new unverified claims

This entry catalogs and carefully keeps distinct four different `D8` appearances found across this project (intrinsic fixed-shell, A3-transverse, arithmetic-lift, and the new semilinear one from v13.548), correctly citing the Round 45 obstruction and the exact intertwiner `P` between the first two. All four component facts were independently verified either in this round or Round 45; this entry introduces no new unverified claim, only the comparison itself, which is accurate.

---

## 6. Summary

| Entry | Verdict |
|---|---|
| v13.545 | Verified exactly — correct `S4/C4` resolution of v13.543's open question |
| v13.546 | Verified exactly, including an independently-checked nonexistence proof |
| v13.547 | Verified exactly (`S4×C2`, order 48) |
| v13.548 | Verified exactly (`S4×D8`, order 192) — the strongest claim this round, fully confirmed |
| v13.549 | Accurate synthesis of already-verified facts |

## Guardrail

No RH, GRH, Suzuki-spectral, or critical-line consequence follows from any entry this round, and all correctly self-limit to exact finite/representation-theoretic algebra with no Pell/QR dynamical claim. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`.
