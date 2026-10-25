# Cone Derivation Ledger v14.874 — Numerical retarded Maxwell seat pole

Date 2026-10-25. Parent v14.873. Research note research-notes/Maxwell_Seat_Retarded_Complex_Pole_Reproducer.md commit 02329dcfd97a45a92be725b03b1cf88e6eba3c05. Live prewrite HEAD 02329dcfd97a45a92be725b03b1cf88e6eba3c05. Additive only; Suzuki/far-tail unchanged.

[D, conditional frozen-orbit model] Let z=a ω/c, F(z)=1+i√π z exp(-z²)erfc(-iz), D(z)=1/4-z²F(z), using Gaussian regulated retarded transverse Maxwell response plus balanced-seat electrostatic curvature from v14.873, without mechanical supports or additional bare inertia. mpmath numerical complex root verification with residual <1e-25 gives z±=±0.4108337143730426−0.1700926343728676i (positive frequency and reflection pair), damped for e^-iωt; frequency ω=(c/a)z. Search also locates higher complex roots but is not a complete pole census.

[D/O] The naive constant-inertia frequency z=1/2 lies outside controlled |z|<<1, while full retarded response has damped complex poles. This establishes a model-dependent electromagnetic resonance of the frozen source effective kernel, NOT a complete physical bicone mode, Higgs, gravitational monopole, or stable elementary-particle mass; widths/support dynamics remain undetermined. No positive-growth root was found in scanned seeds, but global upper-half-plane pole exclusion has NOT been established.

[D/O] Full finite-Ω_L source is periodic and requires Floquet matrix calculation with specified Ω_L a/c and R/a and convergence diagnostics; no finite rotation spectrum certified in this round. Distinguish static-source damped response from actual rotating bicone dynamics.

Flags: frozen_retarded_nearest_oscillatory_pair=NUMERIC_VERIFIED; leading_pole_real=0.4108337143730426; leading_pole_imag=-0.1700926343728676; causal_model_resonance=DAMPED; physical_inertial_mass=NOT_DERIVED; finite_rotation_poles=OPEN; G_and_Higgs=UNPROVED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: retarded-maxwell-complex-pole
parent: v14.874
status: open
action: Independently reproduce root of D(z), verify retarded sheet/sign, check model dependence and whether additional upper-half-plane zeros exist, distinguish frozen source resonance from finite-rotation physical eigenmode. Preserve Suzuki/far-tail.
deliverable: scoped verdict.
