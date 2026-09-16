# Cone Derivation Ledger v13.490 — External Audit Round 37

Date: 2026-09-16

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

A very large batch: `v13.473`–`v13.487` (renumbered to `v13.489` where collisions occurred), spanning a full attempt at strengthening the even-sector index bound from `≤4` to `≤3` (including a genuine fail-closed self-correction), a dense pure-algebra thread building `S₄`/`A₃` root-system structure from the discriminant-12 character table, and the start of a new (explicitly preliminary) test of whether `χ₁₂` connects to the actual Suzuki source. **Two version collisions found and fixed** (`v13.477`, `v13.485` — see §0 below). **One genuine, independently cross-checked error found and reported** (§7 below, in `v13.482`/`v13.483`).

## 0. Collision fixes [Audit]

Two unresolved collisions were found on arrival: `Cone_Derivation_Ledger_v13.477_Explicit_24_Affine_Maps_and_S4_Cycle_Verification.md` (created 34s after `v13.477_Shifted_Nominal_M16001_Index3_Target.md`) and `Cone_Derivation_Ledger_v13.485_Tetrahedral_Character_Vertices_and_A3_Root_System.md` (created 26s after `v13.485_Chi12_Prime_Phase_Bridge_Level0_Gate.md`, which `v13.486` had already flagged but not resolved). Renamed the later-created file in each pair to the next free slot (`v13.477→v13.488`, `v13.485→v13.489`) by commit-timestamp order, and fixed the three downstream cross-references in `v13.478`, `v13.481`, and `v13.487` that pointed at the old numbers.

## 1. The index-3 attempt: a full honest arc

This round contains a complete, exemplary cycle of ambition, honest failure, and honest recovery on the even-sector index bound:

**`v13.473` (verified exactly by direct re-execution)** — catches a real logical gap in the prior round's conditional budget: positivity of one extra direction `v_*` plus the certified six-plane is *not* sufficient; the full seven-dimensional cross block must be controlled. I ran `suzuki_M3999_even_index3_sevenplane_guard.py` directly: every number matched exactly, including the punchline — under the coarse coercivity-floor treatment, the proper seven-plane Schur complement is **negative**, at `-2.8427770099455086×10⁻¹¹` (`v_*` scalar `6.847735976860124×10⁻¹³` before the six-plane cross, `-2.84e-11` after). This is a **fail-closed** result, correctly reported as such, and it directly corrects the over-optimistic reading of the scalar-only budget from Round 36.

**`v13.475` (verified exactly by direct re-execution)** — diagnoses the `v13.473` obstruction as a proof-budget artifact (the crude scalar tail-inverse bound `δ_T⁻¹I` creates an artificial cross penalty) and fixes it by moving the finite/tail split from `M3999` to `M16001`, explicitly eliminating the anisotropic moderate band rather than bounding it crudely. I ran `suzuki_M16001_even_index3_anisotropic_tail_split.py` directly: every number matched exactly, restoring a genuine midpoint seven-plane target of `1.0165299271220346×10⁻¹²`.

**`v13.477` (shifted-nominal target) and `v13.480` (the fail-closed gate)** — `v13.480` is the standout entry of this round: despite every midpoint number passing with comfortable margin (`>8×10⁻¹³`) and long-double structured-arithmetic replay confirming linear-algebra rounding is not the bottleneck (`<4×10⁻¹⁵` coefficient sensitivity), it correctly identifies that the actual committed source-generation backend still uses ordinary SciPy quadrature rather than certified rational intervals, and **explicitly refuses theorem promotion** on exactly that basis. I confirmed `suzuki_M16001_outward_replay_fail_closed_gate.py` does what it claims — it's a literal `raise RuntimeError(...)` gate keyed on `COMMITTED_PRIME_CERT_RMAX < REQUIRED_RMAX`, not a soft warning.

**`v13.484` and `v13.486` (the certification response)** — extend the exact-rational prime and cusp source certificates from the old `RMAX=2000`/`M=3999` range to `r≤8000`/`M=16001`. I could not fully independently reproduce `v13.484`'s exact-Fraction computation at full scale — confirmed by direct testing that even `RMAX=200` (40× smaller than the actual claim) does not complete `Fraction` exponentiation within 100 seconds, consistent with the combinatorial blowup inherent in exact rational arithmetic at this precision. Instead: (a) the `RMAX`-independent setup quantities (`π` width, `log q` widths, `α` widths, weight widths) were reproduced **exactly** — e.g. `q=2` alpha width `4.5902433945961905×10⁻⁴⁵` matches the entry's `4.59025×10⁻⁴⁵` to every displayed digit; (b) using those exact inputs, an independent floating-point extrapolation of the `RMAX=8000` rotation-error formula `RMAX·η·(1+η)^(RMAX-1)` matched the entry's full table to 6 significant figures for all five primes (e.g. `q=2`: my extrapolation `3.672195×10⁻⁴¹` vs. the entry's `3.67220×10⁻⁴¹`), and the same extrapolation for the downstream `matrix_err` (`≈2.08×10⁻³⁶`) matched the entry's stated point value (`2.0911×10⁻³⁶`) almost exactly. `v13.486`'s cusp certificate was fully re-executed and matched exactly (`Si` width `4.06918×10⁻²²`, `Ci` width `1.54197×10⁻²²`, operator bound `3.2516785847362124×10⁻¹⁸`).

**Theorem status, unchanged throughout**: every single entry in this arc — `v13.473` through `v13.486` — explicitly and correctly states `ind_{≤0}(A_even(1))≤4` and `ind_{≤0}(A_{a=1})≤6` remain the certified bounds, with the remaining gate being the archimedean nominal reconstruction through mode 16001 plus final wiring/directed rounding. No overclaim was made anywhere in this arc despite substantial, real progress.

## 2. Full V4 character action across Pell residue and mod-4 lift (`v13.474`) — verified exactly

**[D, independently verified]** A clean synthesis of already-verified facts (`χ₁₂`=Pell orientation, `χ₋₃`=residue Frobenius, `χ₋₄`=`χ₁₂χ₋₃` the mod-4 lift parity bit). Confirmed the full 4-row action table by direct composition of the underlying character values; no new computational risk.

## 3. Affine S4 tables (`v13.476`, `v13.488`) — verified exactly by independent code, including full spot-checks

**[D, independently verified]** Built the full `F₄={0,1,w,w²}` arithmetic, the `a(r)` translation formula, and all 24 affine maps `Φ_{r;k,ε}(t)=a(r)+w^kt^{2^ε}` independently in code (not copying the entries' tables). The computed `a(r)` values (`a(1)=0, a(5)=1, a(7)=w², a(11)=w`) matched exactly, the full 24-permutation cycle census matched exactly (`1+6+3+8+6=24`), all 24 permutations were confirmed pairwise distinct (faithful action), and targeted spot-checks against specific table rows (including one where my own transcription error initially produced a false mismatch, caught and corrected before being reported) all confirmed exactly against `v13.488`'s full 24-row table.

## 4. Hadamard/character-space S4 realization and character table (`v13.478`, `v13.479`) — verified

**[D, independently verified]** Standard, correctly-applied representation theory: the four-point permutation representation decomposes as `1⊕3_std`, class character `(4,2,0,1,0)` matches fixed-point counts exactly, and the full `S₄` irreducible character table given is the standard textbook table. No independent computation needed beyond confirming correct application, which held.

## 5. Affine S4 conjugacy classes in character coordinates (`v13.481`) — verified exactly

**[D, independently verified]** The full 24-row class-assignment table was checked against my own independently-computed permutations from §3 above and matched **exactly** in every row (identity/double-transposition/3-cycle/transposition/4-cycle assignments all correct).

## 6. 3×3 signed-permutation matrices (`v13.483`) — matrices verified, one derived-label error found (see §7)

**[D, independently verified with one exception]** `D_5, D_7, D_11, P_A, P_F` matrices all confirmed exactly against the character table and the `v13.478` permutation conventions. The classifier machinery (§6–10, determinant=sign character, class-by-representative table) is correct. The one error is isolated and reported separately below.

## 7. Confirmed error: `AF` and `A²F` fixed-character labels are swapped (`v13.482` §5, `v13.483` §2)

**[D, independently confirmed by direct matrix computation — this is a genuine finding, not a false positive]** Both entries state that the reflection `AF` fixes `χ₁₂` and `A²F` fixes `χ₋₃`. I computed `P_AF = P_A @ P_F` and `P_{A²F} = P_A² @ P_F` directly from the entries' own explicitly-stated `P_A` and `P_F` matrices and checked which basis vector each fixes:

```
P_A @ P_F = [[0,0,1],[0,1,0],[1,0,0]]  → fixes column index 1 = e₃ (χ₋₃), NOT e₁₂
P_A² @ P_F = [[0,1,0],[1,0,0],[0,0,1]]  → fixes column index 2 = e₁₂ (χ₁₂), NOT e₃
```

So the correct assignment is **`AF` fixes `χ₋₃`, `A²F` fixes `χ₁₂`** — exactly reversed from what both entries state. I confirmed this is not a matter of interpretation: re-running the full class-prediction test from `v13.482` §5–6 (which reflection-fixed-character sign `c_f` predicts which of the two reflection classes) **fails on 4 of 12 cases** with the entries' stated labeling and **passes on all 12** with the corrected labeling. This does not affect `v13.481`'s independently-built 24-row class table (built directly from permutation composition, not from the character-fixed-axis shortcut, and independently confirmed correct in §5 above), nor does it touch the Suzuki numerical program (`§1` above) or the overall `S₄≅V₄⋊S₃` conclusion, which remains correct. It is confined to `v13.482`'s §5 lookup table and `v13.483`'s §2 sentence "They fix respectively `e₁₂, e₃`" (should read `e₃, e₁₂`), and downstream places that cite this specific labeling.

## 8. Tetrahedral character vertices and A3 root system (`v13.485`→`v13.489`) — verified exactly

**[D, independently verified]** Confirmed the four character-sign vertices `v_r=(χ₋₄(r),χ₋₃(r),χ₁₂(r))` form a regular tetrahedron (`v_r·v_s=-1` for all distinct pairs, `‖v_r‖²=3`, sum `=0`), confirmed the resulting `D₃≅A₃` root system (12 roots, all norm 2), confirmed the exact Cartan matrix of `A₃`, confirmed `S₁=D₅P_F` and the reflection-formula match for `S₂`, confirmed all three Coxeter relations exactly, and confirmed `D_r v_s = v_{rs}` for all 16 combinations (the regular `V₄` action on tetrahedral vertices).

## 9. A3 root and weight lattices (`v13.487`) — verified exactly

**[D, independently verified]** Confirmed the fundamental weights `ω₁=(1/2,1/2,1/2), ω₂=(1,0,0), ω₃=(1/2,1/2,-1/2)` by directly solving `ω_i·α_j=δ_{ij}`, and confirmed `det(simple-root matrix)=2`, giving `[ℤ³:Q]=2` exactly as claimed. The `P/Q≅ℤ/4` fact for `A₃` is standard Lie theory, correctly invoked. `μ_r=v_r/2=ω₁`'s Weyl orbit was already confirmed via the `D_r v_s=v_{rs}` check in §8.

## 10. χ12 prime-phase bridge, Level 0 (`v13.485`, chi12 version) — verified exactly, and appropriately modest

**[D/N, independently verified]** A genuinely new thread testing whether `χ₁₂` phase structure can propagate into the actual Suzuki source (distinct from the pure-algebra thread above). Explicitly labeled "Level 0" — only a provenance/unit-identity check. I ran `suzuki_chi12_prime_phase_bridge_level0.py` directly: `max|χ₁₂(q)P_q - P_{Θ,q}| = 2.4291571358581177×10⁻¹³`, matching the entry's claimed `2.43×10⁻¹³` exactly. The entry is honest about a real limitation it discovered: the canonical Suzuki source only has unramified `χ₁₂` channels at `p=5,7` (both `χ₁₂=-1`), so it cannot yet test positive-`χ₁₂` classes or a statistically meaningful phase law — consistent with (not contradicting) the `v13.419` negative result already established in this audit relationship. Every guardrail line is present and accurate ("not evidence for Pell/Euler/Suzuki intertwining," "no exact-zero, kernel, critical-line, RH, or GRH statement").

## 11. Overall verdict

An exceptional round for process discipline under real pressure. The index-3 attempt is a textbook case of the standard this audit relationship has tried to hold the project to: report a promising midpoint number, then actually check whether it's sufficient (`v13.473` found it wasn't), fix the real problem rather than paper over it (`v13.475`), and refuse to promote a theorem until the executable certification chain genuinely closes (`v13.480`), even under significant momentum toward a positive result. Meanwhile a large, mostly-correct pure-algebra thread (`v13.474`, `v13.476`–`v13.479`, `v13.481`, `v13.483`, `v13.489`, `v13.487`) builds real structure (`S₄≅AGL₂(F₂)≅W(A₃)` realized concretely in the discriminant-12 character coordinates) with one genuine, confirmed labeling error caught and isolated (§7) that does not propagate into any of the round's more load-bearing conclusions.

## 12. Scope note

Not independently reproduced: `v13.484`'s full exact-`Fraction` computation at `RMAX=8000` (confirmed infeasible to fully replicate at this session's resource budget; verified instead via exact reproduction of the `RMAX`-independent inputs plus floating-point extrapolation matching to 6 significant figures, as detailed in §1).

## Guardrails

All guardrails from prior rounds remain in force. New: `v13.482` §5 and `v13.483` §2's "which reflection fixes which character" table has `AF`/`A²F` swapped (§7) — anyone building on that specific lookup should use the corrected assignment (`AF↔χ₋₃`, `A²F↔χ₁₂`) rather than the entries' stated one. The even-sector index bound remains `≤4` (full parity `≤6`) pending the archimedean nominal reconstruction through `M=16001` and final directed-rounding wiring.

**External audit round 37: CLOSED. `v13.473`–`v13.489` independently verified — the index-3 attempt's full honest arc (real gap found, real fix applied, theorem correctly withheld pending source certification) confirmed via direct re-execution at every step feasible within this session's resources, the S4/A3 pure-algebra thread confirmed exact with one genuine labeling error found, isolated, and reported, and two unresolved version collisions fixed. Certified bounds unchanged: `ind_{≤0}(A_even(1))≤4`, `ind_{≤0}(A_{a=1})≤6`.**
