# Cone Derivation Ledger v14.627 — Sandbox note: the chain-selector scans — no arithmetic selector for ψ_D (companion to v14.621, v14.626)

**Timestamp:** 2026-10-19 (EDT, evening)
**Lane:** Sandbox (little Euler)
**Parents:** v14.621 (ingredients assembled; ψ_D = 45.310004305 pinned; the selector named as the wall), v14.626 (rotor anatomy — this entry's note is its companion), v14.616 (the Dirac ratio's five meaningful figures → the ±1.1×10⁻⁵ window), v14.626 also being live HEAD at allocation (collision-checked immediately before — next-free was v14.627).
**Status:** companion deposit under Jeremy's explicit 2026-10-19 authorization ("might as well"). Answers **no Lane A HANDOFF**; changes no paper, no staged draft, and no certified object. All results are negatives, recorded with their chance accounting.

## Deposits

Research note `Chain_Selector_Scans.md` (commit `91a061aa117a0f746e1903e6affe7a0b59795dbe`, SHA-256 `7ed52475b65d2a53b5f002066a11d24cd28687e0ee436f6836ec414b3eda66e0ee`); producers `chain_selector.py` (`6a5c41cd95e85a3ece3e6ef48462a76e7cddc7b5`, SHA-256 `4c1ed3b3c96c71d6a4baa1ee108dfdf558a8bee096685eaebb13c593a8233233`), `em_steps.py` (`6c5d239dc46d8c66d9484269cd0af493b2af9215`, SHA-256 `94c707311f91c6bcfcb63aa6a41c1c4adbc8d2eb599d8e15a62fd4b4fd6348c0`), `regulator_chains.py` (`7b42654f551f275cc4cb3cedc6448cb1f470ae6f`, SHA-256 `448192ad065e4ba1a4b8e3061204a2702be689fa64f74992b895e3e26938fc7c`). Workspace originals in `lane_b/sandbox/runs/20261019-chain-selector/`. All four re-read from the repository after commit and byte-compared.

## Results in brief (all negative)

Candidate sets declared in advance; window ±1.1×10⁻⁵ in ψ throughout.

- **Uniform ratio chains** (r ∈ consecutive (n+1)/n, prime p/1, 12/1): no hit; expected chance hits 0.0034. Best (4/3)³¹⁵ at 7.8×10⁻⁵ (7× outside; implied ratio off 1.6×10⁻⁴ — beyond G's uncertainty, physically excluded; ~2% luck).
- **EM steps** (Jeremy's direction): −ln α, −(½)ln α, −ln α/(2π) chains — residuals ≥ 0.109; α-repairs of the best chain fail; ln α_G/ln α = 17.890344 (Eddington-zone non-integer); totient-block ladder residual 0.175.
- **Prime chain** of the nearest integer to the Dirac value: exists trivially (2²¹·3·5²¹·13·31·12537181·14967301), unselected (two ~10⁷ prime steps; smoothness Dickman-chance). Recorded catch: an initial float64 factorisation "found" 2⁸⁰ — the double's ulp; redone exactly.
- **Regulator orbits** (fundamental-unit steps of the six real quadratic channel fields + all two-field mixes): no hit; best mix 1.3×10⁻⁴, ≥12× outside, at generic Diophantine density.

Near-misses cluster at ~10⁻⁴ across all four systems — chance density, not an approached mechanism. **The selector is not in the step arithmetic.** The note's live reading [O]: EM's contribution in the α precedent was selection rules (a coupling's Wigner factors), not a number — leaving the hierarchy item as a construction problem, with v14.626's rotor as its arena (whose coupling also selects no finite chain).

## Scope flags (honest)

`answers_lane_a_handoff = false`; `papers_modified = false`; `certified_objects_modified = false`; `G_derived = false`; `hierarchy_generator_found = false`; `selector_found = false`; `open_item_count_change = false` (still 2).

## Disposition

The full selector hunt (scans + rotor anatomy at v14.626) is now on record. Live threads unchanged: Lane A's far construction (v14.585 actions 3–4) and v14.550's two G items.
