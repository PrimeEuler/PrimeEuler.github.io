# Cone Derivation Ledger v14.731 — Sandbox: the gravitational dyon pair — quarter quantisation on the Poincaré cone (note deposited)

**Date:** 2026-10-22 EDT. **Lane:** sandbox (our Lane B). **Parents:** v14.550 (diameter–secant machine), v14.592 (the 1/4 family; parabolic segment / bouncer warp), v14.620 (ħ as unit circle), v14.696 (gravity-selector closure; Sciama pairing, seat at −½ / balance at +½, apex at 0 open). External: Misner (J. Math. Phys. 4 (1963) 924–937), Dowker (Gen. Rel. Grav. 5 (1974) 603–613), Luna–Monteiro–O'Connell–White (JHEP 11 (2015) 143; refs [67, 68] therein = Misner, Dowker).
**Directive:** Jeremy, 2026-10-22 — the (m, l) pair examined at his line ("that pair seems like an interesting pair to look at with regards gravity"; pair test run on his go; parabolic verification on his go); note drafted on his go ("very substantial and well worth a note or a paper"), updated with §§6, 9 on his lines, deposited on his explicit line ("lets update the note and get it in the ledeger and the repo. then lets explore a path to a EFT" — the EFT exploration is follow-up sandbox work, not part of this deposit).
**Collision check:** live HEAD checked via commits API immediately before drafting: max ledger version v14.730 (Audit liveness); v14.731 free.
**Deposits:** `research-notes/payloads/sandbox_gravitational_dyon_pair_v14_731/` — `note.tex` + `note.pdf` (7 pp., "The Gravitational Dyon Pair: Quarter Quantisation on the Poincaré Cone", J. Ebert), producers `killing.py`, `charges.py`, `numeric_check.py`, `mic_sep.py`, `tn_sector.py`, and `RESULTS.md` (session record). All identities below verified by exact symbolic computation (sympy) in the deposited producers; `numeric_check.py` adds a 200-point numeric confirmation of §1.

Conventions: geometric units in derivations; ε = specific energy of a test particle (−p_t per unit mass); k = p_φ; dual mass M̃ = c²l/G; α_G(μ) = Gμ²/ħc.

## §1 The pair product [D]

Taub–NUT, ds² = −fχ² + f⁻¹dr² + (r²+l²)dΩ², χ = dt + 2l cosθ dφ, f = (r²−2mr−l²)/(r²+l²). The SU(2) Killing triad was solved from the Killing equation with f(r) arbitrary; the t-shifts are forced (opposite sign fails) and the triad closes, [ξ_i, ξ_j] = −ε_ijk ξ_k, **only** with ξ_z = ∂_φ (the combination ∂_φ + 2l∂_t is Killing but does not close the algebra — triad uniqueness). Conserved charges give, exactly,

  J·n̂ = −2εl,   J² = Σ²θ̇² + (p_φ + 2εl cosθ)²/sin²θ + (2εl)²,   Σ = r²+l²

— the Poincaré charge–monopole structure with eg → 2εl. Route B (independent): Misner regularity forces t-period 8πl/c, energy steps ħc/(4l), same lattice. Hence

  μcl/ħ ∈ (1/4)ℤ   (G cancels identically),   α_G(μ)·α_G(M̃) = (k/4)²,  minimum 1/16,

against the electromagnetic α·α_m = (1/2)² = 1/4. Gravity's pair quantum is ħ/4; the deciding factor is the fibration's 2 in χ, read by both routes. The pair's "electric" member is energy ε (Kaluza–Klein: charge = t-fiber momentum); ε = 1 at rest.

## §2 Parabolic seats [D]

MIC–Kepler Hamilton–Jacobi separates in parabolic coordinates exactly (residual 0; the Zwanziger +s²/r² term is load-bearing — without it a −s²/(ξ+η) remainder obstructs separation). Seats: ξ carries ((k−s)/2)², η carries ((k+s)/2)² — centre k/2, offset s/2; hydrogen (s = 0) recovers both seats (k/2)², the (n₁, n₂) structure of the programme's α extraction. Taub–NUT minus MIC (s := 2εl), exactly:

  TN − MIC = −(2mr + l²) p_r² − (2εl)²,

purely radial (the sector the Iwai–Katayama time reparametrisation absorbs; cited, not re-derived). Taub–NUT's parabolic seats are therefore **k/2 ± εl**: diameter k, AM centre k/2, offset = the pair product εl. Product lattice denominator 4 vs state lattice 2 — one additional power of 2 of resolution.

## §3 The monopole is the offset [D identity; spectrum cited]

From J² = L² + s²: the MIC mechanical angular momentum obeys Λ(Λ+1) = j(j+1) − s², i.e. Λ + ½ = √((j+½)² − s²) — the diameter–secant split with AM = j+½, offset = s, GM = Λ+½; bound spectrum hydrogenic in N = n_r + Λ + 1 (McIntosh–Cisneros, cited). Both monopoles (s = eg; s = 2εl) enter the machine through the offset slot alone and inherit its power laws (segment 3/2 = 1+½; warp 2/3 = 1/(1+½); dyadic half→quarter). The (n, k) machine's offset — its free parameter — has a physical occupant: the pair product. "What fixes the offset" = "what carries monopole charge, and how much" (open).

## §4 Intertwining [D]

eg/ħc ∈ (1/2)ℤ ⊂ (1/4)ℤ ∋ μcl/ħ: the electromagnetic half-lattice is the **even sublattice** of the gravitational quarter-lattice; EM's minimal pair quantum ħ/2 is gravity's k = 2 rung. One grid, fixed by single-valuedness in both theories.

## §5 Boost decomposition [D, kinematics]

A boost along the axis acts on the pair through ε alone (k, l, |J| fixed): seats k/2 ± l cosh ψ split hyperbolically about the fixed centre, and the Casimir budget J² = (orbital)² + (2εl)² transfers from the orbital leg to the pair leg — the boost decomposes the state into the pair. Saturation at orbital leg zero:

  γ_max = 2√(j(j+1))/n,   ψ_max = arcosh γ_max,   μcl/ħ = n/4.

Minimal state (j, n) = (½, 1): γ_max = √3, ψ_max ≈ 1.146, rest split pair 1/3 / orbital 2/3 (recorded as minimal-rung arithmetic). Shell j admits at rest only n ≤ 2√(j(j+1)). Source-side ψ→∞ image: Aichelburg–Sexl shockwave (cited). Boosts create no charge: boosted Schwarzschild carries no NUT charge; the H_g sector's boost *symmetry* is the observable part (frame-dragging mixing; GW propagation on the cone), the charge l itself unobserved.

## §6 The action is the integration [D framing]

The Hamilton–Jacobi function W = U(ξ) + V(η) is Hamilton's action for the pair system; every quantisation above is a period statement about it (angular period: J as SU(2) action variable, Route A; time period: Misner cycle, Route B; segment area ∝ h^{3/2} as the bouncer's action, warp its Bohr–Sommerfeld shadow, Maslov quarter included). The quarter lattice is the period lattice of the pair's action in units of ħ. Classification: exact period data / matching conditions for a **worldline** EFT of the pair; the field layer (a joint gravitoelectric–gravitomagnetic Lagrangian density with an organised expansion) is absent and is the follow-up exploration Jeremy directed. The structure is a unified *kinematics* of dyon pairs, not a unified field theory: α and α_G remain independent inputs, their realised rungs are not related, and nothing here fixes the balance (the (e, G) product remains e^{2ψ}, v14.696 anchors unchanged).

## §7 Novelty accounting [I]

Known, and credited in the note: the gravitational-dyon reading of NUT (Demiański–Newman; Dowker 1974) and the existence of a mass–NUT quantisation condition via time periodicity (Misner 1963; stated in Luna–Monteiro–O'Connell–White as the Dirac-equivalent condition). Not found in print by the sandbox's searches (abstracts/passages; Dowker 1974 not read in full — novelty stated with that bound): the coefficient in closed pair-product form (k/4)² / 1/16 with pair quantum ħ/4 set against α·α_m = 1/4; Route A via Killing-triad closure with the triad-uniqueness point; the parabolic seats k/2 ± εl; the offset law §3 as a named slot; the even-sublattice intertwining §4; the boost separatrix table §5. The dyadic mechanism (half → quarter under a quadratic operation) is the author's own prior taxonomy in "Casimir Completion and Primitive Null Diamonds" (four realisations); the pair product is dyadic depth two and its first realisation in a product of charges. Jeremy's assessment, recorded as his: the assembled structure "has to be a first."

## §8 Scope and flags

NUT charge is unobserved; Taub–NUT carries the Misner string or, with periodic time, closed timelike curves. This entry constrains permitted pairs and their kinematics; it detects nothing, derives no coupling, and supplies no enumerator: the selector slot (v14.696) is unchanged — the lattice is a selection *principle* for pairs whose physical realisation still waits on a pair with one member known.

**Flags:** `G_derived=false`; `NUT_charge_observed=false`; `pair_product_quantisation=(k/4)^2_D_two_routes`; `unified_field_theory=false`; `worldline_EFT_period_data=EXACT`; `field_layer_EFT=OPEN_directed_followup`; `selector_status=UNCHANGED_seat_open`; `far_tail_touched=false`; `papers_modified=false` (new note deposited as payload, not a foundations-paper edit).
