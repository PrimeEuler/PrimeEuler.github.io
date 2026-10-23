# Cone Derivation Ledger v14.761 — Gravity selector: classical action obstruction and causal-fermion-system candidate

**Date:** 2026-10-23 EDT. **Lane:** dedicated gravity. **Parents:** v14.696, v14.731–760.
**Live collision check:** \`master\` at \`d757cc92def2864622aae80d3c5ae0eeca52ad51\`; v14.761 was unoccupied. Additive deposit only; Suzuki sandbox and far-tail untouched.
**Research deposit:** \`research-notes/Gravity_Selector_CFS_Action_Matching.md\`.

## Closure of immediate action-coefficient test [D / obstruction]

The naive prescription to derive the convex selector coefficients a,b from Maxwell and Einstein–Hilbert actions is **non-predictive** on its own: Maxwell gauge-field normalization depends on electric charge/compact U(1) matter coupling, while the Einstein–Hilbert coefficient already contains \(G^{-1}\). Point monopole field energies require UV core/renormalization; NUT backgrounds additionally require boundary terms and confront Misner string/time-periodicity causality. Assigning positive unique a,b from these actions without fixing those ingredients would feed the desired physical constants back into the selector. Thus v14.760's mathematical minimum \(\psi_*=\frac14\log(b/a)\) remains conditional.

## CFS candidate [literature/context, no overclaim]

The causal fermion systems causal-action framework provides an upstream variational description whose continuum limit can produce gauge and Einstein-type equations. Existing literature states gauge coupling constants depend on microscopic regularization and, in relevant CFS constructions, Newton's constant scales quadratically with a microscopic regularization length. A curved-spacetime continuum-limit construction (Finster–Fischer, published October 9, 2026) derives Einstein–Dirac equations under globally hyperbolic assumptions. Those premises do **not** give a numerical alpha, G, or the Cone pair selector by themselves.

A useful purely **illustrative dimensionless matching ansatz** is \(G_{\rm eff}=c_g c^3\ell_{\rm reg}^2/\hbar\), \(\alpha_{\rm EM}=c_e\), hence \(\alpha_G(\mu)=c_g(\mu c\ell_{\rm reg}/\hbar)^2\) and \(\alpha_{\rm EM}/\alpha_G(\mu)=(c_e/c_g)(\hbar/\mu c\ell_{\rm reg})^2\). This exhibits a possible *mechanism* for a large hierarchy without building the ratio directly into v14.760's a/b, but is **not a result derived from a CFS minimizer**. To become a selector, it needs a computed and physically normalized CFS family \(\rho_\psi\), a causal-action Hessian along the monopole pair-split direction, an independently fixed regularization scale, and compatibility with both monopole bundles/global spacetime conditions.

Key references and scope are in the research note:
- Finster, *The Continuum Limit of Causal Fermion Systems*, https://causal-fermion-system.com/cfs.pdf
- Finster, baryogenesis/CFS coupling discussion, https://epub.uni-regensburg.de/53613/1/Finster_2022_Class._Quantum_Grav._39_165005.pdf
- Finster–Fischer (2026), https://link.springer.com/article/10.1007/s11005-026-02168-3
- CFS FAQ, https://causal-fermion-system.com/faq/

## Next self-work, not a sandbox assignment

Construct an explicit finite-dimensional **toy causal-action family** with fixed regularization inputs and a monopole-split coordinate \(\psi\), calculate its first and second variations, distinguish an induced selector from a manually inserted asymmetric cost, and test whether it can yield a hierarchical minimum without using target alpha/G values. Then examine whether real CFS regularization permits that family and whether source/global TN conditions are compatible. No measured hierarchy, G, or NUT charge derived.

**Flags:** \`G_derived=false\`; \`physical_selector=OPEN\`; \`naive_Maxwell_EH_coefficients=CIRCULAR\`; \`CFS_selector=CONDITIONAL_CANDIDATE\`; \`CFS_numerical_couplings=NOT_DERIVED\`; \`Suzuki_sandbox_reserved=true\`; \`new_sandbox_handoff=false\`; \`far_tail_touched=false\`.
