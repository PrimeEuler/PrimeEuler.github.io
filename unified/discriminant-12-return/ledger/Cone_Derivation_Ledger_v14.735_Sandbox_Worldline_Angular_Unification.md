# Cone Derivation Ledger v14.735 — Sandbox: one worldline angular action for both dyon pairs — the angular-sector unification test

**Date:** 2026-10-22 EDT. **Lane:** sandbox (our Lane B). **Parents:** v14.731 (dyon-pair deposit), v14.734 (R338 HJ closure). Test posed by the gravity lane ("the most important next test is whether a single duality-covariant worldline action can reproduce both the electromagnetic Dirac-monopole and gravitational Taub–NUT angular sectors while respecting their distinct gauge and diffeomorphism symmetries"), relayed and endorsed by Jeremy; ledgered on Jeremy's explicit line ("we should update the ledger with the wordline finding too").
**Collision check:** live HEAD checked via commits API immediately before drafting: max ledger version v14.734 (this lane's HJ closure); v14.735 free.
**Deposits:** `research-notes/payloads/sandbox_worldline_angular_unify_v14_735/` — `angular_unify_test.py` (producer; sympy, ~3 s) and `ANGULAR_UNIFY.md` (full record).

## Verdict [D/N as marked]

**PASS at the angular-sector level.** A single first-order worldline angular structure — sphere kinetic term plus a Wess–Zumino/minimal-coupling term of coefficient s — reproduces both sectors' angular theory exactly. With canonical (θ, φ, p_θ, p_φ), twisted momentum Π_φ = p_φ + s cosθ, the one vector formula

  J = p_θ φ̂ − (Π_φ/sinθ) θ̂ − s n̂      (mechanical angular momentum − s along n̂)

gives, for all s, verified in the producer:
- **J·n̂ = −s** exactly (symbolic); **J_z = p_φ** identically.
- **J² = A_s := p_θ² + (p_φ + s cosθ)²/sin²θ + s²** exactly (symbolic) — A_s is the angular HJ function of both backgrounds (EM: MIC/monopole HJ at s = eg, gauge A_φ = −g cosθ; TN: the HJ of v14.734 at s = 2εl, via the exact TN−MIC sector identity).
- **{J_i, J_j} = +ε_ijk J_k** and {J_i, A_s} = 0: symbolic derivatives evaluated at 300 random phase-space points, 900/900 bracket checks, worst deviation 5.8e-15.
- **TN specialisation:** J(s = 2εl) equals the Killing-triad charges Q_x, Q_y, Q_z of v14.731's `charges.py` at 300 random points with f(r) an arbitrary numeric value — worst deviation 7.1e-15.
- **Seats:** the parabolic seat squares ((k∓s)/2)² specialise to the MIC seats at s = eg and to (k/2 ∓ εl)² at s = 2εl (algebra).

## Where the distinct symmetries live [D bookkeeping]

The action is shared; the composition and quantisation of s is not. EM: s = eg, a product of two couplings on an internal U(1) fiber, fibration weight 1; gauge invariance (string/patch independence) quantises s directly, eg/ħ ∈ (1/2)ℤ. Gravity: s = 2εl, a background coupling l times a state variable ε = −p_t (the momentum conjugate to the timelike fiber), fibration weight 2 (χ = dt + 2l cosθ dφ); the action is a spacetime scalar (diffeomorphism-invariant; no dual gauge field appears), and quantisation arrives through the fiber's topology — Misner periodicity quantises ε in steps ħ/(4l), and s inherits it. Two consistency points: (i) {ε, J_i} = 0 in the full phase space (the triad is t-independent), so s being state-dependent on the gravity side does not spoil the closure; (ii) the pair-product quarter (k/4)² of v14.731 is the conversion between the two normalisations — the angular momentum itself stays half-lattice in both theories, as SU(2) requires; the quarter appears only when the pair product is rebuilt from the rest fiber momentum (μ) and M̃ = c²l/G separately.

## Scope of "duality-covariant" [I]

What survives: the angular action depends on the pair only through **s = (fiber momentum) × (monopole charge) × (fibration weight)**, and in both theories the period lattice is the single-valuedness condition of whichever fiber carries the momentum; EM duality acts on s by leaving it invariant. What does not exist: a single duality group acting on both sectors alike — EM duality rotates couplings within one theory, while the gravitational side maps between backgrounds/solutions. The single action respects the distinct symmetries precisely by keeping the two fibers distinct (internal circle vs spacetime time); in the Kaluza–Klein reading both fibers are spacetime one dimension up, which is why one formula covers both. This entry covers the angular sector only — the test as posed. Radial/boost completion, the 1PM two-dyon amplitude, and the field layer remain open as scoped in the sandbox EFT memo (`explorations/nut-pair-test/EFT_PATH.md`, workspace only).

**Flags:** `angular_unification=PASS_exact`; `single_duality_group=false`; `worldline_EFT_angular_core=CONSTRUCTED`; `field_layer_EFT=OPEN`; `G_derived=false`; `far_tail_touched=false`; `papers_modified=false`.
