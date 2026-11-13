# Cone Derivation Ledger v15.873 — Gravity/Muse: does Casimir offset originate in maximum restoring force? Paired-level identity versus physical parametric exchange

**Date:** 2026-11-13 (US Eastern). **Parents:** EM half-turn/quarter-rate and gravity-rescaled lattice v15.866–867, v15.869 and gravity v15.871–872; original v14.620/v14.904 paired-level AM–GM/Casimir construction; audited gravity conventional EH+solid no-novelty controls. **Prewrite live HEAD:** c52face60cc97c878e1f66047bb645a665d5dcb0, target path absent; additive only. This gate addresses the user's explicit hypothesis that Casimir observables may be caused by coincident maximum restoring-force points.

**Status:** [D] exactly distinguished algebraic half-step Casimir corrections from dynamical force extrema and parametric energy exchange; [N] exact first-order pump phase dependence, independent of h; [N] numerical full oscillator shows second-order nonzero quadrature energy despite first-order zero; [O] independent physical EM/solid/G phase selector and action-derived coupling.

## Gate 499 — the actual Casimir offset has no oscillator phase in its derivation

For a transition pair at levels jh and (j+1)h, its arithmetic midpoint is AM=h(j+1/2). The geometric pair invariant is

**GM²=h²j(j+1)=AM²−(h/2)²**.

Thus the squared offset **q²=h²/4** is an algebraic identity for all j and all nonzero step h. In Muse's h_EM=1 dictionary q_EM²=1/4; in the h_G=1/2 dictionary q_G²=1/16. They are **distinct sector corrections**; the EM 1/4 Casimir is not an identical gravitational 1/4 Casimir, as corrected and confirmed in v15.866. The paired-level algebra does not mention an EM current, physical time, resonant restoring force, applied torque or charge response. The bare coincidence of a quarter-turn displacement antinode with maximal harmonic restoring-force magnitude cannot derive the identity or prove that it causes a physical Casimir observable. The experimentally measurable quantum electrodynamic Casimir force between boundaries is a *different* high-stakes interpretation requiring boundary-condition QFT, not established by the above algebra.

## Gate 500 — turning points have force maximum but zero instantaneous mechanical F·v power

Take an *ordinary* harmonic coordinate x=A cos(ωt) with spring stiffness k0=mω². The restoring force F=−mω²x has maximum **magnitude** at the turning points t=nπ/ω, where the velocity vanishes. The work rate of that force is **F xdot**, which vanishes there. At quarter-cycle offsets of the harmonic displacement, F=0 and speed is maximal. Max restoring force, max velocity, and max power are not the same event. It is therefore mathematically invalid to identify the EM 1/4 or G 1/16 Casimir correction with the force maximum without a separate operator or conservation law.

## Gate 501 — a physically specified variable stiffness can pump at the turning point

The parametric-oscillator model has an *actual time-dependent stiffness*

**k(t)=mω²+δk sin(2ωt+φ)**,

and obeys **m xddot+k(t)x=0**. Its instantaneous mechanical energy is **E=m xdot²/2+k(t)x²/2**. Differentiation, *using the true equation of motion*, yields the exact energy-transfer law

**dE/dt=(1/2)kdot(t)x(t)²**.

The energy comes from (or goes to) the **external stiffness-changing actuator**. Even at xdot=0 and maximal restoring-force magnitude, dE/dt can be nonzero if kdot≠0, because the actuator changes the potential energy at fixed displacement; this is not mechanical F·xdot work. Conversely if the stiffness itself peaks at a turning point, kdot=0, and instantaneous parametric energy exchange is ZERO despite maximal |F|. Maximum force and maximum pump energy therefore do not generically coincide.

In the weak-modulation first-order approximation evaluate the exact energy-transfer identity along the unperturbed orbit **x0=A cos(ωt)** over one unperturbed cycle T=2π/ω. The explicitly integrated energy exchange is

**ΔE^(1)=π A² δk cosφ / 2**.

Therefore:
- φ=0 yields **positive pump work** ΔE^(1)=+πA²δk/2;
- φ=π/2 yields **zero first-order net work**;
- φ=π yields **negative work** ΔE^(1)=−πA²δk/2.

The Casimir half-step h does not occur in the result, and the geometry alone does not supply δk, φ, a physical clock or the actuator's energy.

**Exact SymPy reproducer:** research-notes/k4_casimir_restoring_parametric_gate_v15_873.py, additive commit **12b3a614b15774dcb05c6b5e247550d792b7e9cc**. Executed locally to PASS for all paired-level corrections, full energy derivative identity, pump phases, positive/negative/zero first-order work and h-independence. Committed-byte independent audit pending.

## Gate 502 — full ODE beyond first order and the important zero-work caveat

To check the perturbation expansion rather than assuming its predictions hold exactly, integrate the **actual time-dependent equation** xddot+[1+εsin(2t+φ)]x=0 numerically over one unperturbed period 2π, using m=ω=A=1, x(0)=1, xdot(0)=0. Compute E at both endpoints using the actual time-dependent stiffness, not the fixed-stiffness approximation. For ε=0.01:

| φ | leading predicted ΔE | full ODE ΔE |
| --- | ---: | ---: |
| 0 | +0.01570796327 | **+0.01595709459** |
| π/2 | 0 | **+0.00024814913** |
| π | −0.01570796327 | **−0.01546357031** |

The quadrature phase has zero **first-order**, but not identically zero **all-order**, energy change; its residual is O(ε²). Halving ε from 0.01 to 0.005 reduces that residual by a factor approximately four, as expected. The positive/negative pump phases and the full-ODE values are reproduced independently with high-accuracy SciPy integration. This is the conventional Mathieu/parametric amplifier energy transfer, not a new Cone interaction or quantum-mechanical Casimir result.

**Numerical reproducer:** research-notes/k4_parametric_exact_ode_vs_first_order_v15_874.py, additive commit **c52face60cc97c878e1f66047bb645a665d5dcb0**. Executed locally at ε=0.02,0.01,0.005 and φ=0,π/2,π; verifies O(ε²) first-order error, correct gain/loss signs and quadrature residual convergence. Awaiting external independent audit.

## Gate 503 — scientific answer and missing selector

The hypothesis that max-restoring-force points **align with** the Casimir-related quarter lattice is a useful geometric/dynamical correspondence; it does not establish **causation**. A physical origin claim would require an independently derived map from the discrete paired transition operator (h,j) to a dynamical time-dependent EM or gravitational stiffness k(t), the origin of its 2ω modulation, coupling strength and phase φ, and a gauge-invariant observable distinguishable from conventional GR+elasticity+Maxwell dynamics. There is no such map yet in the frozen K4 action. The hypothetical EM↔G modulation is a classical energy-conserving exchange with an external actuator, not energy creation from static charge or geometry.

A falsifiable next test is to take an **action-derived, conserved EM+elastic/metric coupling** rather than a hand-prescribed k(t), derive the mechanical/EM energy balance and phase locking, and explicitly subtract the matched ordinary Maxwell+GR+solid prediction. The already verified paired-level corrections, `1/4` (EM) and `1/16` (G mesh), remain exact without establishing a new physical transition-frequency or quantum Casimir force.

**HANDOFF — external audit and Muse:** independently reexecute v15.873 symbolic and v15.874 numerical reproducer; check sign and factor-of-two in kdot*x²/2, perturbative versus exact zero work at φ=π/2, h-independence, the distinction between EM 1/4 and gravity 1/16 and the absent physical selector. Preserve this as a new causal-candidate test, not an assertion that extrema cause Casimirs. Avoid modifying prior certified source objects.
