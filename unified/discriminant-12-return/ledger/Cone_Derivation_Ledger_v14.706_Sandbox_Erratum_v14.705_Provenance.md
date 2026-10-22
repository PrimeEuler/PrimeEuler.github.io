# Cone Derivation Ledger v14.706 — Sandbox erratum to v14.705: provenance of the bath-note corpus corrected (a pre-expansion bath note IS repo-resident at unified/Bath_Note.tex)

**Timestamp:** 2026-10-22 (EDT)
**Lane:** Sandbox (little Euler)
**Parent:** v14.705 (sandbox deposit of the expanded bath-note results). Filed promptly on the correction being identified — by Jeremy, who pointed at the file — following the program's errata pattern (v13.918, v13.933, v14.502, v14.698). No result, number, or claim of v14.705 changes; this erratum corrects only its provenance paragraph.

## The correction

v14.705's provenance stated that the bath note "was never previously moved into this repo or a foundations folder," based on a deposit-time check of `research-notes/` and the ledger. That check did not cover the repo's `unified/` directory, and the statement is **wrong as written about the bath-note corpus**. The pre-expansion bath-note corpus has (at least) two distinct members:

1. **`unified/Bath_Note.tex`** — repo-resident since 2026-08-26 (commit `faec0d2`, "Add files via upload"; fetched and read at this erratum's filing, SHA-256 prefix `cd61d8c006b4aa34`). Title: *"The Cone in a Bath: Boson, Gravitational, and Plasma Relaxation of the Semi-Major Axis."* Contents: exact Lindblad relaxation of the cone coordinates (Ṫ = −κ(T − n̄ − ½), Ẋ = −κ(X − ½), ⟨Y²⟩_ss = n̄(n̄+1), cone identity exact at moment level); the classical stochastic-bath ⟨Ṫ⟩ formula with its Itô/Jensen convexity term (caught by a 20σ ensemble disagreement, corrected formula verified to 0.09σ); plasma diffusion and dynamical-friction coefficients from Rutherford scattering (3×10⁶ simulated encounters), cancelling exactly at equal test/field masses in the monoenergetic shell model. This note concerns relaxation of **T**; it is **not** the direct parent of the v14.705 expansion.
2. **The Kepler/cone EFT draft v3.4** (`Kepler_Cone_Revised_EFT_Draft_v3_4_Elevated_Hot_Benchmark`) — the Maxwellian-bath note carrying the eccentricity shape coordinate q and the hot-bath fixed point q₀ = 1/√3. Mac-local in origin (Jeremy's statement, 2026-10-22); the copy the sandbox worked from is the workspace file at `explorations/kepler-eft/`. This **is** the direct parent of the expansion results deposited in v14.705, and v14.705's parentage, numbers, and claim discipline stand as deposited.

Amended provenance sentence for v14.705, to be read in place of the original: "The expansion's direct parent is the EFT draft v3.4 (Mac-local; workspace copy `explorations/kepler-eft/`), one of (at least) two pre-expansion bath notes; the other, *The Cone in a Bath*, is repo-resident at `unified/Bath_Note.tex` (2026-08-26) and is a distinct note, not expanded by the 2026-10-21 run."

## Scope flags (honest)

`erratum_to = v14.705 (provenance only)`; `v14_705_results_changed = false`; `answers_lane_a_handoff = false`; `far_tail_touched = false`; `papers_modified = false`; `G_derived = false`.
