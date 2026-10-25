# Cone Derivation Ledger v14.830 — Covariant elastic-solid stability window

Date 2026-10-24. Gravity lane. Parents v14.821–822 and v14.826–829. Research note research-notes/Cone_Covariant_Elastic_Solid_Candidate.md, commit a54b24c7f161a0c4c4f50362ebd2e61abb7c9e8a. Prewrite live HEAD a54b24c7f161a0c4c4f50362ebd2e61abb7c9e8a; additive only. Protected Suzuki and far-residual work untouched.

## Generally covariant solid action [D]
For comoving material scalars φ^I define \(B^{IJ}=-g^{μν}\partial_μφ^I\partial_νφ^J\), \(b=\sqrt{\det B}\), \(q=\mathrm{tr}B/[3(\det B)^{1/3}]-1\). A fixed internal Euclidean metric identifies trace. Consider
\[
S=\int\sqrt{-g}\,[R/(2κ)-b^{2/3}(C+Dq)]\,d⁴x,\quad κ,C>0,\ D≥0.
\]
By AM–GM q≥0 for positive-definite B; q and its first variation vanish at B∝I. Thus for flat FLRW φ^I=z^I this shear term leaves the background \(ρ=C/a²,\ p=-ρ/3,\ a=\sqrt{κC/3}(\tau-\tau_0)\) intact.

## Local perturbative characteristic test [D]
Around an isotropic comoving state q=(2/3)e_dev:e_dev+O(π³) in displacement strain, yielding shear modulus \(μ=2Dρ/(3C)\). Under the standard isotropic relativistic-solid local characteristic formulas with inertia \(ρ+p=2ρ/3\),
\[
\boxed{c_T²=D/C,\qquad c_L²=-1/3+4D/(3C)}.
\]
Hence a candidate nonnegative subluminal window is \(1/4≤D/C≤1\), with strict positive longitudinal speed when D/C>1/4. At D/C=1/2, \(c_T²=1/2,\ c_L²=1/3\). This establishes a *local principal-symbol target*, not global cosmological, nonlinear, or Hamiltonian stability.

## Open microscopic and physical selection [O]
The rotor lattice from v14.829 is not directly contained in this action; identifying D/C with its microscopic couplings requires explicit coarse-graining, including translation/rotation symmetries. Tensor EH principal kinetic term remains positive for κ>0 but material anisotropic stress modifies tensor mode equations. Complete coupled scalar/vector constraints and long-wavelength stability remain open. The Hessian Cone is an admitted background, not dynamically selected; κ, D/C and Newton G are not derived.

Flags: covariant_isotropic_solid_action=EXACT; w=-1/3_background_preserved=TRUE; local_shear_modulus=2Dρ/(3C); local_speeds=CONDITIONAL_EXACT; local_causal_window=1/4_to_1; global_stability=OPEN; rotor_coupling_derived=NO; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: covariant-elastic-solid-variation-and-characteristics
parent: v14.830
status: open
action: Independently expand shape invariant q to quadratic strain, vary stress tensor on FLRW, derive longitudinal/transverse local principal symbols, and verify window 1/4<=D/C<=1. Check that stability claims remain strictly local and no rotor-to-modulus selection is asserted.
deliverable: scoped verdict, leave Suzuki/far-tail untouched.
