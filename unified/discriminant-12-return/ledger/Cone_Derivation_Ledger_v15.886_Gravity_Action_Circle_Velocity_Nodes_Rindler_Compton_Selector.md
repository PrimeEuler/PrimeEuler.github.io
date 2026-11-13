# Cone Derivation Ledger v15.886 — Gravity: action-circle/velocity-node traversal and the conditional Compton–Rindler closure

**Date:** 2026-11-13 US Eastern. **Parents:** Sandbox v14.620 action-circle interpretation, v15.233 Rindler/parabola tangency, v15.857 HJ fixed-force inversion, v15.864 tangency chain, v15.866 per-sector quantum circle; Gravity v15.883 action-phase cycle, v15.884 physical m/s velocity axis, v15.885 exact velocity traversal and fixed-action counterfamily. **HEAD checked immediately before commit:** 9c4b9bab54e706faf6bd41270edc9f6fb20be008. Target absent and additive only, no certified/Suzuki/Audit/Sandbox changes.

**Question:** Could matching the geometric acceleration length to the action circle's physical Compton length close the m/s-velocity-node clock and uniquely determine a foundational frequency?

**Status:** [D] exact conditional length-weld algebra and SI clock; [N] arbitrary positive dimensionless ratio rho survives, so uniqueness fails; [O] a law that fixes rho without importing mass, measured G or externally specified acceleration.

## Gate 540 — the natural-looking *conditional* Compton/Rindler scale equality

For constant-proper-acceleration SR motion, define the characteristic acceleration (Rindler) length

**L_R=c²/a**.

A massive quantum rest state with independently specified inertial mass m has reduced Compton length

**lambda_Cbar=hbar/(mc)**.

If one **postulates** L_R=lambda_Cbar, then

**a_*=mc³/hbar**,

**c/a_*=hbar/(mc²)=1/omega_C**, with **omega_C=mc²/hbar**.

This is an exactly consistent *dimensional identification*. The action circle's phase-rate E/hbar gives the same angular frequency if one additionally supplies E=mc². The full 2pi winding occurs at period 2pi/omega_C and carries action h=2pi hbar; a one-radian interval 1/omega_C carries action hbar. Neither one-radian interval nor the equality between two independently defined length scales was proved by the tangency geometry itself.

For the **conditional example** that velocity-axis nodes occur at v=c/4 and c/2, the v15.885 lab traversal interval becomes

**Delta t=(1/omega_C)(1/sqrt(3)-1/sqrt(15))**,

only if the extra closure L_R=lambda_Cbar is imposed. This velocity traversal is not by itself a repeated oscillator cycle, so it does not independently constitute an atomic transition frequency.

## Gate 541 — the independent continuous ratio rho is the scale obstruction

Instead, let the Rindler length equal an arbitrary positive multiple rho of the reduced Compton length:

**L_R=rho lambda_Cbar**.

The derived quantities are then

**a(rho)=mc³/(rho hbar)**,

**c/a(rho)=rho/omega_C**,

**Delta t_nodes(rho)=(rho/omega_C)[1/sqrt(3)-1/sqrt(15)]**.

All prior normalized acceleration parabolas, relativistic hyperbolas, null ray ±c m/s tags, action-quantum phase identities and corresponding vertex tangent relations remain valid for every rho. No prior identity supplies an equation setting rho=1. Choosing rho=1 labels a useful comparator case, not a unique solution forced by the Cone. Rest mass m is also supplied, not derived. The equality may be interesting as an additional *hypothesis*, but without its justification and a distinct dimensionless observable it does not beat conventional quantum/relativistic length algebra.

## Gate 542 — no unique Gertsenshtein physical reversal length yet

Even if the Compton frequency were given as an input, the standard photon–graviton quasi-phase-matching length additionally requires an independently specified propagation mismatch

**Lambda_QPM=2pi/|Delta k|=c/[f |n_gamma−n_g|]**

under the v15.882 simple index model. The action circle alone fixes neither rho nor physical source frequency f nor photon/graviton dispersion indices. A massless freely propagating null ray has no rest Compton period. Thus the conditional Compton–Rindler weld does not predict the real magnetic domain reversal positions used in v15.879–880.

## Gate 543 — verification, negative verdict, next physical selector

**Reproducer v15.885:** research-notes/k4_velocity_node_tangency_action_acceleration_selector_v15_885.py, commit **9433dc7a6bb7799a51c8d8232bd0a165fad311e2**. Final exact local SymPy run PASS for the constant proper-acceleration trajectory, shared tangent expansion, conditional c/4→c/2 velocity-node lab/proper times, rescaling, the independent constant-force Newtonian bouncer action and the fixed J=2pi hbar N counterexample a→8a,E→4E,T→T/4.

**Reproducer v15.886:** research-notes/k4_rindler_compton_action_closure_v15_886.py, commit **ad2891467cc676789df2c7ec20637e6a643df91a**. Exact local SymPy run PASS for L_R=lambda_Cbar conditional a, omega_C, arbitrary rho and node interval rho dependence. Post-commit independent audit of both is pending. No historical objects overwritten.

**Verdict:** The user-specified m/s velocity nodes and action-circle tangency provide an organized geometric candidate for a clock; and **equating** the Rindler length with the reduced Compton length produces a definite conditional acceleration. But this equality and a rest mass are additional inputs. The unbroken rho family is an exact no-unique-selector witness.

**NEXT:** find a *physical constraint* that derives rho=1 (or another definite dimensionless constant), or derives a phase-space node recurrence and its period from the frozen K4+Maxwell action. A self-adjoint spectral problem with actual boundary conditions or a covariant force law could in principle supply constraints; a diagrammatic contact or SI unit conversion alone cannot. Compare any such candidate with standard GR+relativistic solid and quantum electromagnetism before claiming novelty.

**HANDOFF External Audit/Muse:** independently re-execute both scripts; confirm SR lab-time vs proper-time distinction, the Newtonian bouncer period from dJ/dE, fixed-J a/E family and conditional rho scaling. Pay particular attention that c/4 and c/2 node velocities are illustrative assumptions, not a mesh theorem, and that identifying action quantum hbar per radian with a full-cycle action h is a factor-of-2pi mistake. Preserve the negative selector result if no equation for rho exists.
