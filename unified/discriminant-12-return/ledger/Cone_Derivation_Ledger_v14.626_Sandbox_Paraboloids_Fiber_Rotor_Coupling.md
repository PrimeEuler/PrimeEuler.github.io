# Cone Derivation Ledger v14.626 — Sandbox note: paraboloids on a fiber — the cos θ coupling anatomy; item (ii) takes a concrete candidate shape

**Timestamp:** 2026-10-19 (EDT, evening)
**Lane:** Sandbox (little Euler)
**Parents:** v14.621 (G ingredients assembled; the selector discussion), v14.620 (consecutive-split anchor), v14.550 §3 (the two open G items), v14.625 also being live HEAD at allocation (collision-checked immediately before — next-free was v14.626).
**Status:** note deposit under Jeremy's explicit 2026-10-19 authorization ("Thats worth writing up"). Answers **no Lane A HANDOFF**; changes no paper, no staged draft, and no certified object.

## Deposit

Research note `Paraboloids_on_a_Fiber_Rotor_Coupling.md` (commit `4e9533e85748971d78f2b4943738bfa89cf16488`, SHA-256 `1e568736fdb88f452cabaaf00550c4a54b685bbcc4343d6c3f026ec465491436`). Workspace original in `d12/explorations/unit-circle-secant/`; producer `lane_b/sandbox/runs/20261019-rotor-coupling/rotor_coupling.py`.

## Content in brief

Jeremy's system for the selector hunt: the double paraboloid as a dumbbell on its axis fiber — a quantum rotor (comb = the ladder, E_j ∝ j(j+1)); made asymmetric, a quantum pendulum with gravity entering as the rank-1 cos θ coupling. It is the only object in the program carrying the full α-note anatomy (spectrum + selecting coupling + cone body) at once. Computed anatomy [D]:

- **Weights.** ⟨j+1,0|cos θ|j,0⟩ = (j+1)/√((2j+1)(2j+3)), Δj = ±1 only; w₀ = 1/√3, settling to 1/2 with excess ~1/(8j²) — maximally democratic, no rung singled out.
- **Climb.** Π_{j<J} w_j = 2^J(J!)²/((2J)!√(2J+1)) ~ √(π/2)·2^{−J} (Wallis), verified to 12 digits, J ≤ 300. The coupling's generated chain has unselected length.
- **Spectrum.** H = −∂² − β cos θ, β = 2IMgl/ħ²: β=0 comb 0,1,1,4,4,9; doublets split (β=1: 0.918/1.293); deep-well spacings → √(2β) from below (β=256: 22.37→22.63) — the ½-power warp in a second system after the bouncer.

## Readout

Consistent with the sandbox selector scans (uniform ratio chains, α steps, prime steps, field-regulator orbits — all negative inside the ±1.1×10⁻⁵ window; `runs/20261019-chain-selector/RESULTS.md`, sandbox-only, not deposited), the physical coupling also selects no finite chain. Item (ii), however, takes a concrete candidate shape: β factorises as (geometry I, l) × (mass M) × (field g)/ħ², so β-spectroscopy of this rotor over a calibrated source mass is a G-meter whose every non-G factor is ladder arithmetic. On Earth it reads g, not G.

## Scope flags (honest)

`answers_lane_a_handoff = false`; `papers_modified = false`; `certified_objects_modified = false`; `G_derived = false`; `hierarchy_generator_found = false`; `factorised_G_observable_exists = false` (candidate form identified only); `open_item_count_change = false` (still 2).

## Verification

Weights, climb product, and spectrum recomputed at deposit from the cited producer (product vs closed form: ratio 1.000000000000 at every tested J; spacing law confirmed against √(2β)). Deposited note re-read from the repository and byte-compared (SHA-256 above).

## Disposition

The gravity thread's system-level anatomy is on record. Live threads unchanged: Lane A's far construction (v14.585 actions 3–4) and v14.550's two G items, both still open.
