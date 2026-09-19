# Cone Derivation Ledger v13.598 — Synthesis Note: One Parabola Through Three Levels

## Status

Synthesis/highlight only. No new derivation. Every identity cited here has already been independently verified in prior external audit rounds; this entry exists to name the throughline explicitly so it is not lost across the intervening technical checkpoints.

## The observation

The same elementary shape — the product of two quantities with a fixed sum, traced as a downward parabola in the free variable — appears, honestly and by direct substitution rather than by re-derivation, at three separate levels of this project's construction:

**Level 1 — divisor pairs (v13.574).** For fixed `n`, the factor pair `(u,n/u)` gives cone coordinates `T_n(u)=(u+n/u)/2, X_n(u)=(n/u-u)/2, Y²=n`. The distinguished `u=1` slice gives the literal parabola

`T=(1+Y²)/2`

(v13.577 §3, the Y-Triangle projection of the unit family).

**Level 2 — SU(2) ladder amplitudes (v13.583, v13.585).** Under the audited Paper-C dictionary, the same factor-pair algebra realizes the angular-momentum raising/lowering amplitude

`A_q²=(j-q)(j+q+1)=Y_q²`,

exactly the divisor-pair product, now indexed by the ladder position `q` at fixed total spin `j`.

**Level 3 — resonant magnetic-driver coupling (v13.595, independently verified in External Audit Round 62).** With `M=2j+1` and `r=j+q+1`, the same quantity is exactly

`Y_r²=r(M-r)`,

and this is literally the squared off-diagonal matrix element of the physical resonant-drive Hamiltonian `H_rot=-γB1J_x` — the real coupling strength between adjacent Zeeman sublevels of an actual driven spin multiplet, largest at the center of the ladder and vanishing at the edges, exactly as the elementary AM-GM/parabola shape requires.

## Why this is worth naming, not just re-deriving

Each step in this chain was checked independently and holds exactly:
- `T=(1+Y²)/2` (Level 1) is the same parabola as `r(M-r)` (Level 3) under the correspondence `r↔y_+=j-q` at the near-maximal-weight edge, and both are instances of the identical algebraic fact underlying the whole cone construction since its first entry: for `a+b` fixed, `ab` is a parabola in either variable, maximized at the midpoint.
- Nothing about this recurrence is mysterious or requires new machinery — every step is a direct, auditable substitution through already-certified dictionaries (v13.574→v13.583 via the Paper-C map; v13.583→v13.595 via the Schwinger/rotating-frame construction). That is precisely what makes it worth keeping visible: it is a genuine, checkable throughline, not a coincidence resting on shared vocabulary.
- Across ~60 external audit rounds and dozens of technical checkpoints, a clean throughline like this is easy to lose inside the sequence of individually-scoped entries. This note exists only to mark it as a named result of the discriminant-12 program: **the same elementary parabola is the divisor-pair product, the SU(2) ladder amplitude, and the physical Rabi coupling profile.**

## Guardrail

This is a naming/synthesis note. It asserts nothing beyond what v13.574, v13.577, v13.583, v13.585, and v13.595 already established and what External Audit Rounds 53, 56, 57, and 62 already independently verified. It does not promote a new theorem, does not touch the Suzuki/M16001 certification chain, and does not claim any physical or arithmetic significance beyond the elementary algebraic identity that produces the parabola at each level.
