# Cone Derivation Ledger v13.531 — External Audit Round 44

## Scope

Independent audit of the U(24)-to-cone character intertwiner (originally v13.528, then briefly v13.529, renumbered to v13.530 during this round after colliding twice with concurrently-created entries) and v13.529 (ambiguity stabilizer). Both fully verified by direct computation.

**Housekeeping first.** Two consecutive collisions were found and fixed: the intertwiner entry was first filed as v13.528, colliding with my own already-pushed `Cone_Derivation_Ledger_v13.528_External_Audit_Round_43.md`; renumbered to v13.529, which then collided with a second genuine entry (`Cone_Derivation_Ledger_v13.529_Ambiguity_Stabilizer_after_Chi4_and_Chi12.md`, which explicitly and directly answers the intertwiner entry's own "next target" question). Renumbered a second time to v13.530, with a renumbering note recording both prior collisions.

---

## 1. v13.530 (U(24), character dual, and cone C2³ intertwiner) — exhaustively verified

This entry builds an explicit isomorphism `Φ: U(24) → G_cone = ⟨R_X,R_Y,S_T⟩ ≅ C2³` and argues that one leg (`χ-4 ↔ R_Y`) has independent cyclotomic justification, while carefully flagging the other two legs as a compatible-but-unforced choice. Independently verified every claim:

- The cyclotomic identity anchoring the one "forced" leg: `σ_r(i) = ζ₁₂^{3r} = χ-4(r)·i` for all `r∈U(12)`, computed directly with `cmath` — confirmed exactly for `r=1,5,7,11`.
- The complex forms of the three cone involutions (`R_X:(z,T)↦(-z̄,T)`, `R_Y:(z,T)↦(z̄,T)`, `R_XR_Y:(z,T)↦(-z,T)`): confirmed by direct complex-number computation.
- The full 8-element correspondence table `Φ(5^a7^b(-1)^c) = R_X^aR_Y^bS_T^c`: confirmed exactly against independently computed `r(a,b,c) mod 24` for all 8 states.
- The homomorphism property `Φ(vw)=Φ(v)Φ(w)`: confirmed for **all 64 ordered pairs**, not spot-checked.
- Kernel triviality: confirmed directly.
- §9's cyclotomic-decomposition claims (`χ-4↔i, χ-3↔i√3, χ12↔√3`): independently verified `σ_r(√3)=χ12(r)√3` via `2cos(rπ/6)` for all four totatives (matching the established Pell/√3 orientation exactly), and confirmed algebraically that `σ_r(i√3)=χ-4(r)χ12(r)·i√3=χ-3(r)·i√3` using `χ12=χ-4·χ-3` and `χ-4²=1`.

No error found anywhere. The entry's own guardrails (§10: only the `χ-4/R_Y` leg has the stronger justification; the other two legs are an explicit compatible choice, not yet proved canonical) are accurate and not overclaimed — confirmed independently by the analysis in v13.529 below, before I even reached it.

## 2. v13.529 (ambiguity stabilizer after χ-4 and χ12) — exhaustively verified

This entry directly and rigorously answers the "next target" question posed at the end of the intertwiner entry: exactly how much of the three-generator assignment is forced versus a free choice. Independently verified the entire `GL_3(F2)` stabilizer chain by brute-force enumeration of all invertible 3×3 matrices over `F2`, not by trusting the stated group-theory facts:

- `|GL_3(F2)|=168`: confirmed by direct enumeration of independent ordered triples.
- `|Stab(χ-4)|=24` (stabilizer of one nonzero vector): confirmed by direct enumeration.
- `|Stab(χ-4,χ12)|=4`: confirmed by direct enumeration, and the four resulting images for `L(σ)` matched the claimed set `{S_T, R_XS_T, R_YS_T, R_XR_YS_T}` exactly (in coordinates, `{f3,f1+f3,f2+f3,f1+f2+f3}`).
- The forcing argument `L(χ-3)=L(χ12)+L(χ-4)=(f1+f2)+f2=f1` (via `F2` linearity, `2f2=0`): confirmed.
- §6's characterization of `S_T` as the unique residual candidate fixing `z` pointwise while reversing `T` (the "pure sheet reversal" normalization): confirmed by checking all four candidates' complex action directly — only `S_T` fixes `z`.
- §7's circularity guardrail — that identifying the QR-deck involution `K` with the full cone antipode `R_XR_YS_T` is *algebraically equivalent* to `σ↦S_T` once the other two legs are fixed, not independent evidence for it — confirmed directly via the same linear-algebra identity `L(K)=(f1+f2)+L(σ)`.

No error found. This is careful, honest mathematics: it identifies exactly the `168→24→4→1` reduction chain, correctly separates what's forced from what's a normalization choice, and explicitly flags a circularity risk that a less careful treatment could easily have missed.

---

## 3. Summary

| Entry | Verdict |
|---|---|
| v13.530 (ex-v13.528/529, intertwiner) | Exhaustively verified, all 64 homomorphism checks + cyclotomic identity confirmed |
| v13.529 (ambiguity stabilizer) | Exhaustively verified, full `GL_3(F2)` chain confirmed by brute-force enumeration |

## Guardrail

No RH, GRH, Suzuki-spectral, or critical-line consequence follows from either entry, consistent with their own stated guardrails. No Pell-to-cone or Pell-to-QR dynamical map is established — both entries correctly limit themselves to exact finite/representation-theoretic statements. Certified Suzuki status is unaffected: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`.
