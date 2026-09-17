# Cone Derivation Ledger v13.542 — External Audit Round 46

## Scope

Independent audit of v13.540 and the Suzuki unit-core star interaction diagnostic (originally filed v13.537, colliding with the already-pushed split-matrix congruences entry, renumbered to v13.541). Both fully verified. Also notable: v13.540 explicitly reads and correctly incorporates Round 45's findings (the v13.536 determinant error, the `D²=H` imprecision) before building on that work — good practice, confirmed accurate.

---

## 1. Housekeeping

Collision: two entries both titled "v13.537" — `Split_Matrix_Congruences_and_Combined_C4xS4.md` (13a4c56, 11:43:20) landed first and was already verified in Round 45; `Suzuki_Unit_Core_Star_Source_Interaction_Diagnostic.md` (576ec35, 11:48:18) landed five minutes later and collided. Renumbered the latter to v13.541.

## 2. v13.541 (Suzuki unit-core star source-interaction diagnostic, ex-v13.537) — fully re-executed, every value matches exactly

Re-ran `suzuki_unit_core_star_pairwise_source_interactions.py` directly (no hardcoded literals found in the source). Every reported quantity matches the ledger to full displayed precision:

- Baseline four-star values and `G5=0.228262850555136`: exact match.
- All six single-source rows (arch, q=2,3,4,5,7) and their `G5` values: exact match, including the finding that `q=5` (not `q=3`) is the strongest *isolated* class-5 selector.
- The leave-one-out table (§3) isn't printed by the committed script directly (only consumed internally via `ablate[j]`), so I extracted it myself by calling the script's own `stars(B-C[j])` function for each source — **all six values, including the loss column, matched the ledger exactly** (e.g. `q=3`: my `-0.18564464556871318` vs. ledger's `-.185645`; loss `0.4139074961238487` vs. `+.413907`).
- Pair-only connected `J_ij` values (§4) and full-background `C_ij` interaction values (§5): all matched exactly, including the headline findings `J_{2,3}=+0.069741612660584` and `C_{(2,3)}=+0.361498701067715`.

This is genuine, fully reproducible numerical work — no shortcuts found anywhere. Its guardrails are appropriately scoped (finite `M=3999` binary64 diagnostic only, no theorem/index promotion, explicitly not an algebra/Suzuki intertwiner claim).

## 3. v13.540 (null six-orbit and S4 edge action) — exhaustively verified, and a genuinely good correction

This entry tests the natural next question after Round 45's `C4×S4` finding (does the determinant-one `S4` act on four distinguished null rays the way it acts on the four A3 tetrahedral vertices?) and gets an honest negative-but-useful answer: it doesn't — the natural null ray `[1:0:1]` has a six-element orbit, not four, matching S4's action on tetrahedral *edges*, not vertices.

Independently verified by rebuilding the full order-96 group and its order-24 determinant-one kernel `H` from scratch:

- Orbit of `a=[1:0:1]` under `H`: confirmed size exactly 6, and the six projective points matched the claimed set `𝒩₆={[1:0:1],[1:0:-1],[0:1:1],[0:1:-1],[1:i:0],[1:-i:0]}` exactly (found via direct orbit computation, not assumed).
- The two named generators: confirmed `det(J)=det(s)=1` (both genuinely in `H`), `J⁴=I`, `s³=I`.
- Cycle structure of `J` on the six labeled points: confirmed exactly `(a c b d)` with `e,f` fixed.
- Cycle structure of `s`: confirmed exactly `(a f d)(b e c)`.

No error found. This is a well-caught correction — it would have been easy to force a four-point identification with the A3 vertices and call it a day; instead it computed the actual orbit, found it was six, and correctly reframed the comparison to the tetrahedron's edges instead. It also explicitly cites and correctly restates the two Round 45 findings before building on the corrected model, which is exactly the right way to incorporate audit feedback.

---

## 4. Summary

| Entry | Verdict |
|---|---|
| v13.541 (ex-v13.537, Suzuki diagnostic) | Fully re-executed, every value matches exactly |
| v13.540 (null six-orbit) | Exhaustively verified; correct, well-motivated negative result |

## Guardrail

No RH, GRH, Suzuki-spectral, or critical-line consequence follows from either entry. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. The null-orbit thread's next stated task (label `a..f` by the six unordered pairs of `{1,5,7,11}` matching the already-known A3 edge permutations) remains open.
