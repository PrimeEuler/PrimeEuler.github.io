# Cone Derivation Ledger v15.1398 — Canonical quartic Weyl–Maxwell–H² vertex retains arbitrary couplings; quarter radius cancels

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Status:** [D/PASS] symbolic canonical-field normalization of the chosen curvature–Maxwell–internal-area EFT operator; [EXACT NEGATIVE] the geometric quarter radius r=1/4 does not set the amplitude of the canonically normalized four-field vertex; [CONDITIONAL] schematic scaling of the reduced four-wave Hamiltonian coupling with independent EFT scales and spatial mode overlap; [OPEN] gauge-fixed tensor overlap, full interacting field variation, finite-packet energy exchange, physical carrier and independent Cone quarter selector. Everything additive, historical assets unchanged.

## Gate 1322 — target and gravitational canonical normalization

Use the actual continuous H² sigma model, not the finite SU2 quarter ladder itself. Write its radius-r target metric as `r² G_AB` and the physical target area as `r² Omega_AB`, with independent kinetic scale f and bare curvature-mixing coefficient g=zeta/Lambda². The leading interactions near the target apex are

`L_sigma=−(f²r²/2)[(∂u)²+(∂v)²]+...`,

`L_int=−(g r²/2) C_mu nu rho sigma F^mu nu (∂^rho u∂^sigma v−∂^rho v∂^sigma u)+...`.

Define canonical sigma fields `U_c=f r u` and `V_c=f r v`. For a local gravitational plus-mode normalized by `e+_ij e+_ij=2`, the Einstein-Hilbert quadratic kinetic coefficient is `M_Pl²(∂h)²/4` under conventional `M_Pl² R/2` normalization, so a canonical real plus-wave field is `G_c=M_Pl h/sqrt2`. Maxwell A is already conventionally normalized. Consequently the **schematic on-shell quartic vertex prefactor**, before tensor/momentum contraction, is

`g r² * (sqrt2/M_Pl) * (1/(f²r²)) = sqrt2*zeta/(Lambda²*M_Pl*f²)`.

The r factors cancel **exactly**. There is no unique r=1/4 dimensionless constant; all the physical scales and the dimensionless coefficient ζ must be separately selected.

For discrete normalized plane-wave modes in finite volume V, every canonical field contributes `(2ωV)^(-1/2)`, the spatial integral supplies V and the operator supplies five derivatives in a momentum-contraction polynomial `P5`. Thus a **schematic** rotating-wave interaction frequency has scaling

`κ_eff ∝ [sqrt2*zeta/(Lambda² M_Pl f²)] P5 / [4 V sqrt(ω_A ω_G ω_U ω_V)]`.

The **equality coefficient cannot be fixed by this dimensional/normalization argument**, since gauge constraints, TT polarization, photon tensor normalization, reality/conjugate branches, overlap integrals and EFT field redefinitions remain to be calculated. A localized packet replaces the simple 1/V overlap by an actual spatial integral. The earlier v15.1396 resonant Hamiltonian κ=.05 was *chosen*, not obtained from this expression.

## Gate 1323 — exact radius reparameterization test

For any two positive radii r and R, rescale `f'=f*r/R` and `g'=g*r²/R²`. Both bare target kinetic term `f²r² G_AB` and physical area coupling `g r² Omega_AB` are invariant under this change. The canonically normalized quartic coefficient is therefore identical. Independently, when using the **normalized** area form from the earlier v15.1380 formulation, r never appears in the coupling at all.

The actual local SymPy source `/mnt/data/cone_gate/quarter_canonical_vertex_scaling_v15_1398.py` passed all exact symbolic checks and printed the non-radius-dependent expression. **Additive committed reproducer:** `research-notes/k4_quarter_weyl_canonical_vertex_v15_1398.py`, SHA **0bf1fadaeafb2eebe5dc5c82e102c62412849311**, independently authored with the same symbolic identities and awaiting external committed-byte replay. This is a rigorous obstruction **within this continuous extra-field EFT with free f,g**. It is *not* a no-go theorem against any future finite/discrete quarter-grid interaction that genuinely fixes its own physical normalization.

## Gate 1324 — implications and Audit handoff

The finite-mode pump depletion of v15.1396 is a transparent conserved Hamiltonian demonstration, while the conditional finite-SU2 tensor rank selection of v15.1397 restricts proposed low-rank bosonic bridges. Neither identifies the continuous H² sigma field with the archived finite quarter-ladder carrier. The proposed Weyl–F–area model is a permissible extended effective field theory with a nonzero radiation channel, but no unique quarter-specific parameter or source has emerged.

**Audit:** replay v15.1396–1398 exact committed Python, independently derive four-wave Hamiltonian invariants and conditional Wigner–Eckart center parity, and verify canonical sigma and TT normalization and mass dimension of the quartic Weyl vertex. Do not present schematic κ as a computed physical coefficient. Check the r reparameterization with both normalized and unnormalized target area conventions. Investigate possible on-shell EFT redundancies and optical observables.

**NEXT:** derive the **actual polarization and spatial packet overlap** of the quartic vertex from the covariant Weyl action, compute its reduced Hamiltonian coupling with fully specified canonical normalizations, and run a controlled backreacting finite-packet truncation. For a **Cone-only observable**, exhibit a physical finite quarter operator/action that breaks the degeneracy without arbitrary extra fields/scales; until then the matched identical enlarged EFT exactly reproduces the candidate.
