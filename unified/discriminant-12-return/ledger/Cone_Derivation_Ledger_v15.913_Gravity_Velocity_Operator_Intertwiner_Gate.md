# Cone Derivation Ledger v15.913 — Velocity operator versus kinetic imbalance: physical intertwiner test

**Date:** 2026-11-13 US Eastern. **Gravity lane.** Parents: v15.884–885 (owner's m/s X axis), v15.906–911 (Schwinger ladder and local-circle radii), v15.912 (actual Fermi tidal detector projection), Paper C two-mode Fock dictionary. **Immediately prewrite HEAD:** 6a93dd3a317b008f8d60b7fd252b93178b2b7829. Ledger target confirmed absent. Additive-only; certified, Suzuki, Audit and Sandbox files untouched.

**Research question:** Can the Cone's X=u(Jz+1/2), already assigned physical units m/s by the owner, be the *actual physical velocity operator* p_i/M of the two-dimensional oscillator used in the tidal coupling calculation? If not, is a different experimentally grounded observable represented by X?

**Status:** [D] exact oscillator number-shell selection rules; [D] exact quadratic kinetic-energy correspondence; [N] literal velocity-intertwiner no-go within a fixed shell; [O] measurement/calibration that turns the energy-imbalance-scaled coordinate into a physical velocity.

## Gate 620 — literal oscillator velocity fails at fixed D

Let the physical detector be the isotropic two-dimensional oscillator with mass M and base frequency omega* (both externally specified). Its physical Cartesian velocity quadratures are **v_i=p_i/M=i sqrt[hbar omega*/(2M)](a_i†−a_i)**. They change total oscillator occupation **N=N1+N2** by ±1. Let P_N project to one fixed Cone outer diameter **D=N+1** (the Paper C correspondence).

The exact selection rule is **P_N v_i P_N=0** for each i, in any basis on that fixed shell. By contrast the proposed Cone velocity-coordinate operator is **X_Cone=u(J_z+1/2)** with nonzero and generally distinct eigenvalues on this shell. Consequently **no unitary intertwiner that stays entirely in one fixed-N shell can identify the full literal physical oscillator velocity p_i/M with X_Cone**. This is stronger than a unit-calibration objection: it is a spectral/selection-rule obstruction for the explicit Fermi oscillator comparator. It does NOT prove that no more general physical Cone X-velocity representation can exist with different matter dynamics or a different Hilbert space.

A finite-dimensional Hermitian coordinate and momentum also cannot obey the exact canonical commutator [Q,P]=i hbar I because its trace would be nonzero. This is a second limitation on interpreting finite D as a complete canonical phase space; projected operators need not retain the full canonical algebra.

## Gate 621 — exact positive quadratic momentum / kinetic correspondence

The physical velocity squared is not confined to ΔN=±1: **P_N v_i² P_N** is nonzero. Using p_i=i sqrt[M hbar omega*/2](a_i†−a_i),

**P_N [(p_1²−p_2²)/(2M)] P_N = hbar omega* J_z**,

and independently

**P_N [p_1p_2/M]P_N=hbar omega* J_x**.

These follow by keeping the number-conserving parts of quadratic oscillator momentum operators. They are ordinary bosonic Schwinger identities, not new K4/GR physics.

Therefore exactly *on the fixed-N subspace*,

**X_Cone=u/2 + (u/(hbar omega*)) P_N[(p_1²−p_2²)/(2M)]P_N**.

The right-hand side has velocity units provided u has m/s units and hbar omega* has energy units. It is a scaled *kinetic-energy imbalance*, not the physical velocity of an individual oscillator. The factor u/(hbar omega*) must be established by an actual measurement/calibration; choosing it to manufacture m/s would be a label, not a derived physical identification. The shared cross-momentum J_x relates kinetic correlations to the same geometric ladder amplitudes sqrt(nk) found in the tidal cross-coordinate interaction. For the isotropic stationary number eigenstates, <p_i>=0 but <p_i²> differs, illustrating why the quadratic observable is the appropriate candidate.

**Important:** P_N(p_i²)P_N ≠ [P_N p_i P_N]². Projecting a quadratic observable is not equivalent to squaring its zero fixed-shell linear projection. The two-sided shell-changing virtual/quadrature paths are essential.

## Gate 622 — consequence for physical acceleration and nested parabolas

If X is interpreted literally as measured particle velocity, the J_x-driven within-shell waveform of v15.910–911 cannot be the Fermi oscillator particle's p_i/M expectation; the latter vanishes in all fixed-shell states and fixed-shell unitary evolutions, while X_Cone's expectation oscillates. Instead the calculated waveform describes redistribution of a scaled *kinetic imbalance* or other pseudospin observable within the chosen two-mode system.

This sharpens rather than erases the owner's geometrical insight: the velocity-axis X labels can still be used with u in m/s, but a measured acceleration a=d<v_phys>/dt requires a true physical velocity readout, not a reinterpreted scaled kinetic difference. The parabola and local circle curvatures remain in velocity-coordinate units if u is calibrated that way, but do not supply a time parameter or mechanical acceleration. Neither the inner sqrt(nk) circles nor their Schwinger ladder operators fix a coupling frequency, G or a new tidal observable.

## Gate 623 — verification and next gate

**Reproducer:** research-notes/k4_velocity_operator_intertwiner_v15_913.py, additive commit **6a93dd3a317b008f8d60b7fd252b93178b2b7829**. Locally executed Python/SymPy PASS for occupation N=1..4, using full truncated two-mode Fock space N≤6 before fixed-shell projections: zero P v_i P, exactly projected kinetic-energy difference and cross momentum, separate P v² P, diagonal Jz spectrum and finite-trace restriction. Independent Audit pending.

**NEXT:** Test the physical time evolution of the kinetic-imbalance observable under the same locally sourced tidal interaction, including ΔN=±2 terms, and compare with actual oscillator velocity and acceleration readouts. Identify whether a joint measurement involving kinetic-energy imbalance and transverse momentum correlation gives a *new* coupling-independent Cone response after subtracting ordinary SU(2) predictions. Separately, keep open other physically justified velocity-axis embeddings that are not the particular two-mode oscillator comparator. No invented K4 coupling or forced n+1 temporal clock.

**HANDOFF Audit/Muse:** check sign and factor in P_N p1p2/M P_N=+hbar omega* Jx; verify velocity selection rule and trace no-go are scoped to fixed-N representation; check that X_Cone remains *not* literal physical particle velocity in this comparator. Retain previous Audit Round571 missing script process gaps for v15.888/890/895/897.
