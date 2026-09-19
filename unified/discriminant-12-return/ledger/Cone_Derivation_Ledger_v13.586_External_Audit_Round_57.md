# Cone Derivation Ledger v13.586 — External Audit Round 57

## Scope

Independent audit of everything committed since my last push (`92edfed`, Round 56): a follow-up to v13.583 that tightens the `J_+`/`J_-` operator-ordering convention and its exact match to the cone's ordered factor-edge coordinates. One version collision found and fixed (new work landed in the v13.584 slot my own Round 56 entry had just taken). Every operator identity independently re-derived and matrix-checked. No errors found.

---

## 1. Housekeeping

`Cone_Derivation_Ledger_v13.584_Zeeman_Basis_Ladder_Ordering_and_Ordered_Edge_Factor_Dictionary.md` (commit `d2a3e33`, 2026-09-18 20:45:22 -0400 = 2026-09-19 00:45:22 UTC) collided with my own `Cone_Derivation_Ledger_v13.584_External_Audit_Round_56.md` (commit `92edfed`, 22:30:47 UTC the previous day — earlier). Renumbered the colliding file to **v13.585**. No inbound cross-references existed to fix.

## 2. v13.585 (ex-v13.584, Zeeman-basis ladder ordering) — verified exactly

This is a careful tightening of v13.583's SU(2)-ladder/cone bridge: it fixes the exact operator-ordering convention (`J_-J_+` vs. `J_+J_-`, which matters because raising/lowering are not self-adjoint) and shows the raising and lowering edges correspond to literally the *same* ordered `(x,y)` factor pair viewed from its two endpoints — not just matching products, matching pairs.

Rather than accept the stated algebra, I re-derived the standard angular-momentum identities from scratch and then matrix-checked them numerically:

- **Schwinger realization.** Confirmed by hand: `a₁†a₂|n₁,n₂⟩=√((n₁+1)n₂)|n₁+1,n₂-1⟩` (standard raising/lowering on independent bosonic modes), and using `a₁a₁†=n₁+1`, `a₂a₂†=n₂+1`: `J₋J₊=(n₁+1)n₂` and `J₊J₋=n₁(n₂+1)` — both confirmed exactly, matching `A₊²=(j-q)(j+q+1)` and `A₋²=(j+q)(j-q+1)` under `n₁=j+q,n₂=j-q`.
- **Ordered-edge factor pairs.** `x₊=n₁+1=j+q+1, y₊=n₂=j-q` gives `x₊y₊=A₊²`, `X₊=(x₊-y₊)/2=q+1/2`, `T=(x₊+y₊)/2=j+1/2` — confirmed exactly (trivial algebra, and `X₊²+Y₊²=T²` follows from the general identity `(x-y)²/4+xy=(x+y)²/4`). Same check for the lowering edge `x₋=j+q, y₋=j-q+1`.
- **Shared-edge identity.** Independently checked `(x₊,y₊)_q=(j+q+1,j-q)` literally equals `(x₋,y₋)_{q+1}=(j+(q+1),j-(q+1)+1)=(j+q+1,j-q)` — confirmed exactly as the same ordered pair, not merely the same product. This is a genuine strengthening of v13.583's §7 (which only established the centers/products agree).
- **Operator-level completion-of-square identities.** `(J_z+½I)²+J₋J₊=(j+½)²I` and `(J_z-½I)²+J₊J₋=(j+½)²I`. Re-derived symbolically from `[J_x,J_y]=iJ_z` (`J₋J₊=j(j+1)I-J_z(J_z+I)`, `J₊J₋=j(j+1)I-J_z(J_z-I)`), then independently matrix-checked both completion-of-square identities and both product formulas against explicit spin matrices for `j=1/2,1,3/2,2,5/2` in sympy — all confirmed exactly (exact symbolic zero matrices, not numerical approximation).

The Zeeman-energy guardrail (§7: `J_+` raises the magnetic quantum number `q` but does not universally raise energy, since `E_q=-γBq` depends on the sign of `γB`) is a correct and important physical caution, and the entry's own guardrails (§9) explicitly decline to identify any electromagnetic `(E,B)` amplitude with the external Zeeman field, correctly flagging that the next EM-facing question needs to distinguish a static field (coupling through `J_z`) from a transverse driving field (coupling through `J_±`) before any such identification could be promoted. This is disciplined, appropriately incremental work.

---

## 3. Summary

| Entry | Verdict |
|---|---|
| v13.585 (ex-v13.584, Zeeman ladder ordering) | Verified exactly — Schwinger realization, ordered-edge factor pairs, the shared-edge pair identity, and both operator completion-of-square identities all independently re-derived and matrix-checked across five spin representations |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. v13.585 correctly declines to promote any electromagnetic-field identification pending an explicit Hamiltonian-level bridge distinguishing static vs. transverse coupling.
