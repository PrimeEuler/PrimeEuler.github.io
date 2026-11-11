# Cone Derivation Ledger v15.712 — Gravity: explicit source-to-scalar mixed interaction from the original full K4 quadratic action

**Date:** 2026-11-11 US Eastern. **Parents:** v14.928 original Einstein–Hilbert+K4 solid; v14.935 archived full scalar/vector/tensor stability payload; v15.708 a common conserved local Fourier stress; v15.709 local gauge-invariant SVT electric-tidal transfer gap; v15.710 vector sourced shift and pole; v15.711 K4 scalar lapse/shift auxiliary Hessian. **Audit:** Round 544/v15.707 verified gravity through v15.706; v15.708–711 not yet independently audited. **Status:** [D] sourced scalar mixed ADM interactions recovered by regenerating the original archived v14.935 EH/matter quadratic actions; [N] no fully time-dependent sourced scalar pole/metric-potential transfer yet; [O] covariantly conserved common source and Fermi-frame scalar metric readout. **Immediately prewrite live HEAD:** 4cba365a2e72c070f96b001895614e2ed1b52f9a; v15.712 target path absent. Additive only; all Suzuki/far-tail frozen work untouched.

## Gate 305 — independently reconstruct the entire archived scalar quadratic action, not just its auxiliary block

Re-executed the actual frozen v14.935 payloads **matter_sector.py** and **eh_scalar.py**, using their original determinant expansions, and applied the original **assemble.py** E=0 scalar-gauge Fourier map:

**B_z=-k B, B_zz=-k² B, psi_z=-k psi, P_zz=-k² P, P_zt=-k P_dot**,

with the corresponding time-derivative and E Fourier substitutions. The complete quadratic action has scalar propagating variables (psi,P) and nondynamical auxiliaries (Phi,B). This independently reproduces the v15.711 auxiliary Hessian H exactly, now with all mixed propagating terms present.

An initial local test used differently assumed SymPy symbols from those serialized in the archived pickles and therefore produced a misleading structural mismatch. This was corrected by using the **same unqualified symbol identities** as the source archive before comparing or substituting. The final reproducer checks **entrywise mathematical equivalence by simplify**, not bare structural equality, and passes all claimed identities.

## Gate 306 — full mixed auxiliary-to-propagating constraint vector on coasting K4

Write the original quadratic scalar action in block form

**L^(2) = (1/2) q_aux^T H q_aux + q_aux^T d(psi,P,psi_dot,P_dot) + L_free(psi,P,psi_dot,P_dot)**,

where **q_aux=(Phi,B)^T**.

At the same coasting K4 tau=1 normalization used in v15.711,

**kappa=C=1, a=adot=1/sqrt(3), k>0**,

the archive-derived mixed constraint vector is exactly

**d_Phi = [2 sqrt(3)/9] (k² P-3 k² psi-3 psi-3 psi_dot)**,

**d_B = -[2 k²/9](P_dot-3 psi_dot)**.

This is the **source-free constraint forcing from the physical scalar perturbation fields**. It is not arbitrary and does not depend on the shear eta within these two mixed coefficients; the rest of the reduced scalar dynamics still has eta-dependent elastic terms.

The Hessian from the same full action is independently confirmed as

**H = [[-2/sqrt(3),2 k²/3],[2 k²/3, 2 k²/(3 sqrt(3))]]**,

**det H=-4 k²(1+k²)/9**.

## Gate 307 — exact source-first scalar interaction after lapse/shift elimination

Add formal scalar auxiliary source coefficients **J=(J_Phi,J_B)^T** to the *unreduced* quadratic action, and eliminate Phi,B. Then

**L_red(J)=L_red(0)-J^T H^(-1)d-(1/2) J^T H^(-1)J**.

The first term linear in external source is now explicitly known:

**delta L_linear=J_Phi F_Phi+J_B F_B**,

with

**F_Phi=[k² P+k² P_dot-3 k² psi-3 k² psi_dot-3 psi-3 psi_dot]/[3(1+k²)]**,

**F_B= -sqrt(3)[k² P-P_dot-3 k² psi-3 psi]/[3(1+k²)]**.

These formulas are exact under the original archived cos-mode bookkeeping on the tau=1 background. They determine the relative local ADM source couplings to the scalar perturbation fields, **without selecting source amplitudes or fitting a coupling**. The pure-source quadratic contact remains the one calculated at v15.711.

The independently reconstructed reduced source-free quadratic action passes the archive's scalar kinetic-rank checks on this normalization:

**coefficient of psi_dot² = 0**,

**coefficient of psi_dot P_dot = 0**,

**coefficient of P_dot² = sqrt(3) k⁴/[27(1+k²)] > 0** for k>0.

The absence of a quadratic psi-dot kinetic term does not mean psi-dot never appears linearly; the actual sourced auxiliary equations can include derivatives of J after integration by parts. This is why the scalar propagator must be computed with care.

## Gate 308 — strict limit: sourced scalar Green function not yet established

The archived v14.935 scalar mode analysis retained the full tau-dependent coefficients in its Euler–Lagrange equations before freezing the state-space system. An incorrect shortcut would freeze the *Lagrangian* to tau=1 first and then differentiate it in time: such a shortcut would miss derivatives of a(t),H(t), constraint coefficients and source normalization, and could generate a false scalar frequency or residue.

Thus the present gate claims a new exact sourced interaction **on the specified instantaneous coasting slice**, not a complete scalar pole, cosmological tidal readout or measurable three-sector transfer ratio. To obtain those, insert a covariantly conserved physical source into the tau-dependent v14.935 action *prior to* the sourced constraint elimination, derive and vary the resulting time-dependent reduced action, and reconstruct gauge-invariant metric curvature as in v15.709.

No unique Cone quarter-grid signature or new Newton G is obtained by this action-level computation. The established K4 three-sector ratio remains a conventional relativistic-elasticity identity with conditional measurement status.

**Reproducibility:** research-notes/k4_full_scalar_sourced_mixed_v15_712.py, additive commit 4cba365a2e72c070f96b001895614e2ed1b52f9a. This script regenerates v14.935 EH+matter scalar payloads in a temporary directory, reconstructs E=0 Fourier action, exactly checks full H and d, source linear F_Phi/F_B, and the scalar kinetic rank. Independently executed locally to PASS; no image generation and no edits to archived scripts.

**HANDOFF:** external audit/gravity/sandbox: rerun the reproducer, compare its H and mixed d against v14.935 original and v15.711 auxiliary-only result, check all cos-Fourier signs and temporal-source terms, and insist on tau-dependent source equations before any scalar-mode pole prediction. Ensure the existing independent K4 cosmology-fit objection is not confused with local linear stability.

**NEXT:** the genuinely decisive gate is the time-dependent sourced scalar Green function plus a common covariantly conserved stress tensor, including source-dependent lapse/shift and gauge-invariant scalar electric-tidal readout. Treat it as a substantial separate derivation, not an algebraic relabeling of the homogeneous dispersion. If that sourced calculation cannot be closed with independently justified physical matter/source, freeze the K4 triple-observable claim as an exact but presently unmeasured elasticity control.
