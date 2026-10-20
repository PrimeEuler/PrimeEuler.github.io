# Cone Derivation Ledger v14.630 — Sandbox addendum: the rank-2 (tidal / Cavendish) channel of the fiber rotor

**Timestamp:** 2026-10-19 (EDT, evening)
**Lane:** Sandbox (little Euler)
**Parents:** v14.626 (rank-1 rotor anatomy), v14.629 Audit Round 327 also being live HEAD at allocation (collision-checked immediately before — next-free was v14.630).
**Status:** addendum deposit under Jeremy's explicit 2026-10-19 authorization ("Ledger both"). Answers **no Lane A HANDOFF**; changes no paper, no staged draft, and no certified object.

## Prompt and deposit

Jeremy's question — the Cavendish torsion-balance experiments (a balanced dumbbell on a fiber, attracted by a placed mass) — identified the missing chapter of the v14.626 anatomy: the rank-2 tidal channel. Research note `Paraboloids_Fiber_Rank2_Tidal_Addendum.md` (commit `637f91fc1ae9ecbe527d80b9079d59457bfa513c`, SHA-256 `d275b4b36602ea4c714f4074f101be157d08bb661fff1eeab6d4a51fe255d0b9`); producer `rotor_rank2.py` (commit `b9c1ff3c84f60e97d6e61d9fa3b19c91b0540ba8`, SHA-256 `3a4dcd27e4a27a080a3b609674f88631df67f7227d304ef5c2ad995c7c8e144e`). Workspace originals in `lane_b/sandbox/runs/20261019-rotor-coupling/`. Both re-read from the repository and byte-compared.

## Content in brief [D]

Coupling U_tidal = −(GM_s I/R³)·P₂(cos θ); strength β₂ = 2GM_sI²/(ħ²R³).

- **Selection rules:** Δj ∈ {0, ±2} only (machine-zero off-support) — the ladder parity-splits into independent even/odd chains under tides.
- **Weights:** v_j = (3/2)·w_j·w_{j+1} = (3/2)(j+1)(j+2)/((2j+3)√((2j+1)(2j+5))), built from v14.626's rank-1 weights; v₀ = 1/√5, → 3/8. Diagonal d_j = (3(w_j² + w²_{j−1}) − 1)/2 → 1/4. Both verified against the explicit (3cos²θ − 1)/2 matrix (≤2.2×10⁻¹⁶ interior; the single raw 0.375 discrepancy identified exactly as the finite-matrix truncation edge (3/2)w²₅₉).
- **Climbs:** even chain Πv ~ √(π/2)·(3/8)^N (the rank-1 Wallis constant again); odd chain Πv ~ √(3π/8)·(3/8)^N; constants stable to six digits at N = 4000 steps.
- **Budgets:** nano dumbbell + 1 mg at 1 mm: β₂ = 4.4×10², Earth tidal background 4.6% of signal. Bench rotor + 10 kg at 10 cm: Earth tidal background 4.6× signal, static/modulable.

**Structural point:** rank-2 is the only channel in the anatomy with no uniform-g Earth carrier (balanced dumbbell: rank-1 is symmetry-forbidden). The anatomy is now two chapters — rank-1 = the g channel, rank-2 = the G channel (Cavendish's).

## Scope flags (honest)

`answers_lane_a_handoff = false`; `papers_modified = false`; `certified_objects_modified = false`; `G_derived = false`; `factorised_G_observable_exists = false` (spectral forms identified in both chapters; no measurement exists); `open_item_count_change = false` (still 2).

## Disposition

Rotor anatomy complete at rank 1 + rank 2. Companion deposit (rest of the duck) follows at v14.631. Live threads unchanged: Lane A's far construction (v14.585 actions 3–4) and v14.550's two G items.
