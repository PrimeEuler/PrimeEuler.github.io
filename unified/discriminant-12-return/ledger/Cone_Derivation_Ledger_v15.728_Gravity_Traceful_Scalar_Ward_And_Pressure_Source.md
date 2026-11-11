# Cone Derivation Ledger v15.728 — Gravity: pressure-corrected K4 scalar Ward and physical traceful source forcing

**Date:** 2026-11-11 US Eastern. **Parents:** v14.935 original source-free EH+K4-solid scalar action and auxiliary constraints, v15.712 full reconstructed scalar mixed coupling, v15.713 full tau-dependent sourced scalar Euler equations, v15.716–717 conserved but *spatially tracefree* coasting FLRW stress and its restricted Ward identity, v15.727 canonical positive-local-energy scalar matter action whose stress is generally **traceful**. **Status:** [D] correct generalized linear-metric source coefficients and scalar Ward identity; [D] exact extra source forcing of the K4 P mode; [O] full traceful Bardeen/Weyl transfer, concrete physical source stress spectral history and detector realization. **Immediately prewrite live HEAD:** 09ccf9a0c87db92014cb8f31299e0bcfe6d3733c; v15.728 ledger target absent. Strictly additive, Suzuki unchanged.

## Gate 356 — canonical matter adds a direct spatial-metric source

The old source in v15.716/717 was chosen to have spatial trace zero, so it coupled only to the lapse and shift in scalar E=0 gauge. A conventional canonical massless matter field from v15.727 has generally nonzero spatial trace. At source order O(epsilon²) use the linearized, externally prescribed stress of its unperturbed background wave solution, with **delta S_matter=(1/2)∫a³ T^(mu nu)delta g_(mu nu)** (the v14.935 scalar +--- metric convention). For an exp(+ikz) source Fourier mode paired with an exp(-ikz) metric mode, the scalar gauge perturbations obey

**delta g_00=2Phi, delta g_0z=+ik a B, delta g_ij=2a² psi delta_ij**.

The full source coefficients are now

**J_Phi=a³rho, J_B=ik a⁴T^(0z), J_psi=a⁵delta_ij T^(ij)=a³ P_trace**,

where **P_trace=a²delta_ijT^(ij)** denotes the physical spatial-stress trace, **not** the propagating longitudinal solid displacement P of the archived K4 action. This new **J_psi psi** term must be included in the *original unreduced* scalar source before integrating out lapse/shift. Its sign is fixed by the stated covariant metric/stress variation; independent audit should check global sign conventions when changing from the -+++ convention used to derive canonical scalar stress to the frozen K4 +--- one.

## Gate 357 — full cosmological energy conservation supplies the corrected Ward identity

The ν=0 energy component of **nabla_mu T^(mu nu)=0** for the FLRW background and the same Fourier convention is

**rho_dot+3Hrho+H P_trace+ik T^(0z)=0**, H=1/tau.

Multiply by tau a³ and use sqrt(3)a=tau. Exactly,

**tau J_Phi_dot+sqrt(3)J_B+J_psi =0**.

Compare with v15.713 and v15.717: the source-free scalar psi Euler equation of the original K4 reduced action was identically zero, and the old *tracefree* matter source gave **E_psi=-tau J_Phi_dot-sqrt(3)J_B**. Including the direct linear **+J_psi psi** term changes that to

**E_psi=-tau J_Phi_dot-sqrt(3)J_B-J_psi**.

Its vanishing is precisely the physical FLRW matter energy Ward equation above. For **J_psi=0** the old result is recovered exactly. This is a consistent correction, not an attack on the previously audited tracefree source formula.

For the canonical scalar with gradient squared G² and time derivative chi_dot,

**rho=(chi_dot²+G²/a²)/2**,

**P_trace=(3chi_dot²-G²/a²)/2**,

which is **not generally zero**; e.g., at a point with zero spatial gradient and nonzero chi_dot, it equals 3chi_dot²/2. Thus the pressure correction cannot be omitted in a physical positive-energy scalar-source calculation.

## Gate 358 — exact pressure-corrected sourced physical K4 scalar equation

From the exact time-dependent original EH+solid scalar action rebuilt at v15.713, the physical P Euler equation before imposing the source Ward identity has source numerator

**F=[k² tau J_Phi_dot+sqrt(3)k²J_B+sqrt(3)tau J_B_dot+sqrt(3)J_B]/[3(1+k²)]**.

The sourced psi equation now imposes

**tau J_Phi_dot= -sqrt(3)J_B-J_psi**.

Hence the corrected numerator becomes

**F=[-k² J_psi+sqrt(3)(tau J_B_dot+J_B)]/[3(1+k²)]**.

The physical scalar kinetic coefficient derived and independently audited from the original action is

**A_P=2sqrt(3)k⁴tau³/[27(1+k²)]**, k>0.

Consequently the full source-driven scalar displacement equation is

**P_ddot+(3/tau)P_dot+[beta/tau²]P =
  3sqrt(3)J_psi/[2k²tau³] - 9(tau J_B_dot+J_B)/[2k⁴tau³]**,

with **beta=[8eta(1+k²)-3k²]/3**.

The first right-hand-side term is **new relative to the tracefree stress calculation**. The second is exactly the prior v15.713 forcing. The old v15.714 retarded Green function still applies because the homogeneous differential operator is unchanged, but its convolution must now use the **complete physical source combination**.

## Gate 359 — actual matter realization changes the selector question

This gate repairs a material gap: the tracefree signed source of v15.724/725 made a convenient exact source control, but a canonical physical scalar generates a traceful stress at quadratic order and the forcing cannot be obtained by replacing its anisotropy alone in the tracefree formulas. Any proposed electromagnetic-to-gravity or quarter-grid parametric coupling would require a physical source action and the complete stress variation too.

**Reproducibility:** research-notes/k4_traceful_scalar_ward_v15_728.py, additive commit 09ccf9a0c87db92014cb8f31299e0bcfe6d3733c. Sympy PASS on pressure Ward vs FLRW conservation, algebraic source forcing, correct tracefree limit, canonical scalar pressure trace. No image generation or edits of historical certified files.

**HANDOFF:** audit v15.727 canonical stress and v15.728 pressure-corrected Ward directly against the sign conventions of original v14.935 quadratic action; specifically check whether a full external scalar's Fourier pressure/trace is represented by +J_psi psi at source order and whether the direct source trace alters the previously claimed scalar gauge identity exactly as written. Reproduce P forcing independently. The old v14.935 symbolic 0/0 psi-slaving defect and Round 545's no-visible-crash clarification remain preserved.

**NEXT:** recompute gauge-invariant Newtonian potentials and electric Weyl amplitude for the full traceful source, keeping the source pressure coefficient. Then use a wavepacket solution of the canonical scalar KG equation to obtain a physical stress Fourier history and retarded K4 curvature, instead of assuming a source pulse can vanish globally after finite time.
