# Cone Derivation Ledger v14.631 — Sandbox companion: duck test, the remaining sectors (shaping negative; acoustics split; Suzuki side bounded)

**Timestamp:** 2026-10-19 (EDT, evening)
**Lane:** Sandbox (little Euler)
**Parents:** v14.628 (duck test, rotor sector — whose scope flags left the remaining sectors untested), v14.630 also being live HEAD at allocation (collision-checked immediately before — next-free was v14.631).
**Status:** companion deposit under Jeremy's explicit 2026-10-19 authorization ("Ledger both"). Answers **no Lane A HANDOFF**; changes no paper, no staged draft, and no certified object.

## Deposits

Research note `Duck_Test_Rest_Sectors.md` (commit `441f9242977058f5fa9306c0de4bea7c632ced7f`, SHA-256 `7cc7ea0bd53760231b2de81cedaf5c4efee3db445a65a6d19b024c6abd488203`); producer `shaping.py` (commit `480885a5d9666b097970edd5cb050120692e3ba3`, SHA-256 `96a0fa7297cc4610a79e85e948706b19dd8e8e534bd6c0c0a1641085e327ab90`). Workspace originals in `lane_b/sandbox/runs/20261019-duck-test-rest/`. Both re-read from the repository and byte-compared.

## Results in brief

Same criterion as v14.628 (identity iff forced, no free parameter in the map).

- **Shaping — analogy by design (negative).** The ferrofluid void's equilibrium (Rosensweig: a |B| level set) is not the model's parabola r² = 2|X| + 1. Single center loop: −12.7% at X = 0.5, +64% at X = 2, and the level set through the throat ceases to exist by |X| ≈ 3 (the void opens). Totient ring set (turns set by the on-axis amplitude criterion, not profile fitting): within ~16% to |X| = 3, then +46% / +53% at X = 4 / 5. Holding the parabola exactly is an inverse-design problem, not an equilibrium identity.
- **Acoustics — split.** Wave level: forced — the focuser selects its center by phase-coherent interference (core-centered caps at exact station distances 3, 4, 6), the overlay's own selection mechanism. Ray level: false — a paraboloid collimates rays from its focus; no retroreflection; the trap is wave/Bjerknes.
- **Suzuki/channel side — no device counterpart.** Recorded as a boundary (shared parabolic-coordinate PDE family only), not a result.

## Scope flags (honest)

`answers_lane_a_handoff = false`; `papers_modified = false`; `certified_objects_modified = false`; `duck_now_fully_scoped = true` (rotor identity v14.628; acoustic identity at wave level; shaping analogy, quantified; Suzuki side untestable); `G_derived = false`; `open_item_count_change = false` (still 2).

## Verification

Shaping level sets recomputed at deposit from the cited producer (first-upward-crossing root isolation; the two-root bracket failure of the first attempt is documented in the run record and was fixed before any numbers were taken). Deposited files byte-verified (SHA-256 above).

## Disposition

The duck test is complete in all sectors it can reach. Live threads unchanged: Lane A's far construction (v14.585 actions 3–4) and v14.550's two G items.
