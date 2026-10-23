# Cone Derivation Ledger v14.759 — Gravity selector: canonical areal radius and coupling-product degeneracy

**Date:** 2026-10-23 EDT. **Lane:** gravity, self-executed. **Parents:** v14.696 (seat/selector remains open), v14.731–739 (monopole-pair angular and radial series), current external-audit liveness through v14.758.
**Live HEAD/collision:** \`76f6e96e0dc670c58f3eef81322d0262e99e0592\` checked before write; v14.759 unoccupied. No sandbox handoff, no Suzuki/far-tail modifications, no manuscript editing.
**Research note:** \`research-notes/Gravity_Selector_Areal_Radius_Degeneracy.md\`.

### Areal-radius check [D]
With \(R=\sqrt{r^2+l^2}\), canonical one-form preservation requires \(p_R=p_r R/r\). Expanding the source-verified TN radial HJ at large R:
\[
p_R^2=(\varepsilon^2-1)+\frac{2m(2\varepsilon^2-1)}R+
\frac{-J^2+(9\varepsilon^2-3)l^2+(12\varepsilon^2-4)m^2}{R^2}+O(R^{-3}).
\]
Therefore the standard flat MIC radial action at matched leading energy/Coulomb terms still has mismatch \(\Delta_R=(9\varepsilon^2-3)l^2+(12\varepsilon^2-4)m^2\); merely using the TN geometric areal radius does NOT erase it. This is not a proof against all nonlinear canonical maps.

### Selector obstruction [D]
For dual NUT mass \(\widetilde M=c^2l/G\),
\[
\alpha_G(\mu)\alpha_G(\widetilde M)=
\frac{G\mu^2}{\hbar c}\frac{G\widetilde M^2}{\hbar c}
=(\mu cl/\hbar)^2=n^2/16.
\]
This product is **independent of G** for fixed \(\mu,l\). The quantized period data constrain only the product, leaving a continuous split \(\alpha_{1,2}=(|n|/4)e^{\pm\psi}\). Neither the lattice nor the areal-radius corrected radial action supplies an equation fixing \(\psi\) or the relative EM/gravity hierarchy. Geometric mass m can be expressed in terms of G and source mass, but that alone changes names of inputs and does not select G.

### Working decision
Do not claim the fine-structure/gravity hierarchy follows from the observed radial mismatch; it remains an **open selector problem with an explicit degeneracy**. A valid selector must add a coordinate/gauge-invariant, non-circular physical law (UV/IR boundary, globally consistent variational/spectral condition, or specified EFT flow) fixing the split, and produce an independent falsifiable dimensionless observable. Continue to treat v14.696's apex/initial seat as a hypothesis, not an achieved prediction.

**Flags:** \`G_derived=false\`; \`selector=OPEN_one_parameter_split\`; \`areal_radius_simple_match=FAIL_GENERIC\`; \`angular_unification=PASS\`; \`Suzuki_sandbox_reserved=true\`; \`new_sandbox_handoff=false\`; \`far_tail_touched=false\`.
