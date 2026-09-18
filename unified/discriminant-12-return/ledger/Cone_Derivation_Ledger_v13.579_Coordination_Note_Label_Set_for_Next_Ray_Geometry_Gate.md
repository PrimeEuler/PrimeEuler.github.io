# Cone Derivation Ledger v13.579 — Coordination Note: Label Set for the Next Ray-Geometry Gate

## Status

Coordination note only. No comparison against the frozen ray/projection geometry is performed or peeked at here. This note predeclares a candidate label set for the next gate that v13.572 already announced, so that whichever thread runs it is testing something specified in advance rather than something fit after inspection.

## 1. Context

v13.572 froze the 12-prime full-ray and Hadamard-projected angular geometry at `M=3999` and stated its own next step:

> The clean next comparison is against the independently derived surviving `J`-compatible relabelings / orientation structures (`sigma_A`, `sigma_B`) and other pre-existing arithmetic labels, using the full 66-pair geometry and/or frozen projected coordinates. Any explanatory claim must beat simple controls and cannot be rescued by selecting only the visually strongest pair.

Since v13.572, two more exact, independently-audited structures have been certified in the same mod-12/V4 lineage but were not yet available when that next-gate language was written:

- v13.574: the certified cone-incidence dictionary `1↔I, 5↔F, 7↔FS, 11↔S`, where `F` is factor exchange and `S` is root-sheet exchange on the AM-GM factor-hyperbola cone.
- v13.576: the projective identity `[J_A3]=T_5=(1 5)(7 11)`, i.e. the foliation-swap operator's shadow in the transported A3 representation.
- v13.567/v13.569: the standing, unresolved disagreement between `sigma_A=(7 11)` (selected by the cyclotomic character `i=ζ12³`) and `sigma_B=(5 11 7)` (selected by the cyclic-order orientation).

## 2. Predeclaration

If/when the next ray-geometry comparison gate is run, the candidate label set it tests should include, alongside `sigma_A`/`sigma_B`, the cone-incidence character assignment itself:

`chi_-4, chi_-3, chi_12` evaluated at `q mod 12` for each of the twelve sample primes, plus the coarser two-class partition `{1,5} vs {7,11}` induced by `sigma_A`-preservation and the three-class partition induced by the `T_5/T_7/T_11` cone-incidence roles (factor exchange / product / root-sheet exchange).

This is not a new hypothesis about which partition will win — no correlation between any of these labels and the frozen ray geometry has been computed by me, here or elsewhere, before writing this note. It is only a request that the comparison, when it runs, treat this label as available and predeclared rather than reach for it only if `sigma_A`/`sigma_B` alone come up empty.

## 3. Why this matters

The cone-incidence dictionary and the `sigma_A`/`sigma_B` split are logically independent constructions (one from factor-hyperbola geometry, the other from V4-automorphism/complex-structure compatibility), so their agreement or disagreement on the ray geometry, if either shows anything at all, is itself informative and should be recorded either way — including a clean negative, as the project's last three gates (Level-1 clustering, seed-persistence, and now this one if it also fails) have consistently and correctly done.

## Guardrails

- This is a coordination note, not a result. No PASS/FAIL, no numerical claim, no theorem.
- Do not select this label set, or any subset of it, only after seeing which one correlates with the frozen geometry.
- Does not reopen or resolve the sigma_A/sigma_B disagreement (v13.567/v13.569); it is offered as an additional predeclared variable, not a tiebreaker.
- Does not alter any certified Suzuki index/positivity status.
