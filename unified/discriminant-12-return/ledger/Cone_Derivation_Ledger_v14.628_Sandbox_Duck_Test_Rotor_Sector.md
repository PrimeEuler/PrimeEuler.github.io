# Cone Derivation Ledger v14.628 — Sandbox note: duck test — the device↔model rhyme is identity in the rotor sector

**Timestamp:** 2026-10-19 (EDT, evening)
**Lane:** Sandbox (little Euler)
**Parents:** v14.626 (rotor coupling anatomy — the axial weights w_j and the Wallis climb), v14.627 (selector scans), v14.625/14.627 live-HEAD chain (collision-checked immediately before — next-free was v14.628).
**Status:** note deposit under Jeremy's explicit 2026-10-19 authorization ("lets ledger that for sure"). Answers **no Lane A HANDOFF**; changes no paper, no staged draft, and no certified object.

## The bet and the test

Jeremy's bet (2026-10-19, recorded in the note verbatim): the device↔model correspondence — one axis, one field that shapes, drives, and reads the paraboloids ↔ envelope (shapes), overlay (drives phase), spectrum (reads out) — is "a very deep rhyme." Criterion stated in advance: the rhyme is identity iff the correspondence is forced — same equations both sides, no free parameter in the map. Tested in the rotor sector, where both sides are a rotor on one axis in rank-1 fields.

## Deposits

Research note `Duck_Test_Rotor_Sector_Identity.md` (commit `bd528b6e603156e95576b30cca86ada5633e713f`, SHA-256 `76866b3b0f604ff2ed336cdecdf1a1f6056e97a5dfe7251d10b0345bb7bab723`); producer `duck_test.py` (commit `588478b54e8aa0f44a8e4ae28cc12ac185d91c2a`, SHA-256 `74f56b6b4018786d9a3c41d3b7cdd65e53eb3f9e2e4b547527d9432c4e9f88fa`). Workspace originals in `lane_b/sandbox/runs/20261019-duck-test/`. Both re-read from the repository and byte-compared.

## Result [D]

The device's shape/read channel is the axial cos θ coupling (weights w_j, v14.626); its drive channel is the transverse tipping field sin θ e^{±iφ} (the gyro build's NMR/Rabi channel), weights u_j = √((j+1)(j+2)/((2j+1)(2j+3))) at m = 0; readout is the transverse channel by reciprocity. The two systems obey the exact per-rung identity **u_j = w_j·√((j+2)/(j+1))** (machine-precision verified), and the climb products obey **Πu = Πw·√(J+1)** exactly at every J tested (1…100) — the drive climb is √(π/2)·√(J+1)·2^{−J}, the axial climb's Wallis skeleton with one exact factor. No adjustable parameter exists in the map: there is one rank-1 rotor coupling theory (Wigner–Eckart) and both sides instantiate it.

**Verdict:** in the rotor sector the rhyme is identity of governing structure, not analogy.

## Scope flags (honest)

`answers_lane_a_handoff = false`; `papers_modified = false`; `certified_objects_modified = false`; `identity_scope = ROTOR_SECTOR_ONLY` (fluid shaping profile, acoustics, and the Suzuki/channel side untested); `designed_in_correspondences_excluded = true` (coil turns wound to model amplitudes are construction, not evidence — the weight identities testify because SO(3) leaves no choice in them); `G_derived = false`; `open_item_count_change = false`.

## Verification

Per-rung ratios and climb-product ratios recomputed at deposit from the cited producer: 1.000000000000000 at every tested rung and J. Deposited files byte-verified (SHA-256 above).

## Disposition

Jeremy's bet is on record with its first exact test passed, scope-delimited. Live threads unchanged: Lane A's far construction (v14.585 actions 3–4) and v14.550's two G items.
