# Cone Derivation Ledger v15.902 — Inner sqrt(n) half-cycle arc and outer n+1 node pitch

**Date:** 2026-11-13 US Eastern. **Gravity track.** Parents: v15.867 node transition lattice, v15.869 rate parabola, v15.895–901 two-circle geometry, turning radii and conditional n+1 phase-station model. **Live master HEAD immediately before ledger write:** 839a88b2b0bb70697aee430b5dc9d02268ddfafa. Target path checked absent. Additive-only; no certified/Audit/Sandbox/Suzuki edits.

**User proposal:** The inner sqrt(n) circle's pi sqrt(n) corresponds to the first half-cycle frequency transition, and its relation to the outer n+1 circle determines node spacing.

## Gate 581 — exact geometric arc relation

For grid factor u>0 and normalized shell index n>=1, inner radius R_i=u sqrt(n), outer radius R_o=u(n+1)/2. **The inner semicircle has geometric arc length S_half=pi R_i=pi u sqrt(n)** (units of u). A half-turn ANGLE is pi radians, independently of radius: the value pi sqrt(n) is an arc length in units u, not an angle in radians unless an independent coordinate convention specifies a dimensionless arc parameter.

Under the *additional hypothesis* that the outer circle carries N=n+1 equally spaced phase stations, its angular station spacing is 2pi/N and **outer arc pitch delta S_o=2pi R_o/N=pi u**. Hence the exactly dimensionless comparison

**S_half / delta S_o = sqrt(n).**

For perfect square n=k² this is precisely k outer arc pitches; e.g. n=4 -> 2, n=9 -> 3. For nonsquare positive integer n it is irrational. This establishes an integer *arc-pitch commensurability* on square shells under a shared length normalization, not time-phase locking. The self-paired divisor at sqrt(n)=k is also arithmetic fact; no causal association between it and physical frequency follows from coincident integer labels.

## Gate 582 — first transition is conditional on wave and mode convention

If the inner circle hosts a **one-winding sine phase wave** f(theta)=sin(theta), its nodes occur at theta=0,pi,2pi: first following sign transition lies at theta=pi, a half-cycle, covering physical/geometric arc S_half. But a mode f(theta)=sin(m theta), integer m>1, has first following node after angular phase pi/m and corresponding arc pi R_i/m. Thus the proposal selects **one winding** (m=1) as an extra physical boundary-mode input, not deduced by the circle radius.

The N=n+1 equal phase *marks* on the outer circle are not necessarily standing-wave zero nodes. A real sin(m theta) on a full circle has 2m zeros, so N zero nodes require even N and m=N/2. A complex winding exp(iN theta) has N equal-phase stations but 2N zeros in the real-part sine wave; do not conflate these counts. If one calls outer spacing wavelength, distinguish full-mode wavelength from adjacent zero-node separation.

## Gate 583 — propagation and dimensional tests

The two compared arcs generally belong to different concentric circles/sections. Equal arc LENGTHS or integer length ratios do not establish a common wave speed, shared proper time, coupled phase function, or actual motion between the circles. At specified propagation speed v_prop on both circles, half-cycle time of inner one-winding mode would be pi R_i/v_prop and outer station passage interval pi u/v_prop, ratio sqrt(n). But v_prop and its universality across circles must be established; in previous proposals radius itself can have m/s units, in which case a circle arc has velocity units and must NOT be divided by a speed to claim time. The physical radius/velocity/action conversion remains unresolved.

In a rotor with fixed L, angular speed is radius-dependent: omega_i/omega_o=gamma_n². Hence phase-passage time ratios follow this dynamics instead of the simple arc-length ratio unless a separate propagation-speed law is proved. No intrinsic frequency in Hz is selected by this identity.

**Reproducer:** research-notes/k4_inner_half_cycle_outer_pitch_v15_902.py, commit 839a88b2b0bb70697aee430b5dc9d02268ddfafa. Exact local SymPy verification PASS of outer pitch, ratio sqrt(n), square-shell integer alignment, and sample n values. Independent Audit pending.

**Verdict:** The user's pi sqrt(n) first-transition arc interpretation is consistent with the two-circle geometry, if the inner ring carries the first one-winding half-turn and the outer has N=n+1 uniform phase stations. Those mode identifications are conditional. Exact arc-pitch ratio sqrt(n) is a useful discrete geometric discriminator; not by itself a new spectral/frequency law.

**Next:** check actual Cone action operator / boundary conditions for the allowed inner winding m and outer zero-node mode count, particularly n=k² versus nonsquare shells; separately compare transport at equal wave speed with conserved-L rotor transport. A nontrivial physical selector requires a measured field response or an independently derived joint wave equation rather than assigned node counts.

**HANDOFF Audit/Muse:** verify pi radians versus pi u sqrt(n) arc, N station vs real sine zero count, and whether the observed square-shell commensurability is more than arithmetic; retain negative time-selector finding.
