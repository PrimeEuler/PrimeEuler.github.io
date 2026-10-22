# Cone Derivation Ledger v14.723 — Gravity self-executed killed-jump, survival-conditioning and Xi gates

**Date:** 2026-10-22 EDT. **Lane:** dedicated gravity. **Parents:** v14.700, v14.705–722, source EFT v3.4.
**Live collision check:** before this write HEAD \`c18b39e7d4ec421dcef9dd593c6213c9872bc185\`; no v14.723 occupied. Strictly additive. User's Suzuki priority honored: no sandbox or audit compute request.
**Proof deposit:** \`research-notes/Gravity_Killed_Jump_And_Survivor_Closure.md\`.

## Results [D]

For hard Rutherford/Boltzmann collision rate kernel \(\nu_x(dx')\), split bound outcomes \(h'<0\) from escape \(h'\ge0\), \(\lambda(x)=\nu_x(h'\ge0)\). For cemetery-valued test functions f(\dagger)=0, the killed operator satisfies exactly
\[
J_{\mathrm{kill}} f=\int_{h'<0}(f(x')-f(x))\nu_x(dx')-\lambda(x)f(x)
=J_{\mathrm{cens}} f-\lambda(x)f(x).
\]
Use only \(L_{\mathrm{soft}}^{\mathrm{BPS-FP}}+J_{\mathrm{hard}}^{\mathrm{exact}}\) (or the equivalent full BPS-FP plus exact-hard-minus-hard-FP residual); full FP plus full hard counts a component twice.

The normalized surviving density \(\pi=p/S\) of the killed process solves
\[
\partial_t\pi=L_{\mathrm{cens}}^*\pi-(\lambda-\langle\lambda\rangle_\pi)\pi;
\quad
\frac d{dt}\langle f\rangle_\pi=
\langle L_{\mathrm{cens}}f\rangle_\pi-\operatorname{Cov}_\pi(f,\lambda).
\]
This is the exact missing population-level correction for the jump-safe shape \(s=1-q\); it explains why the preexisting BPS fold-local **killed moment** and **bound/censored drift** do not determine the shape drift of the whole surviving population.

A QSD requires the global eigenproblem \(L_{\mathrm{kill}}^*\pi=-\kappa\pi\). The EFT v3.4 gives fold-local hard residuals/hazard numbers, not the full global jump kernel and matched soft coefficient fields. Therefore a unique numerical finite-temperature BPS survivor distribution/QSD **cannot be honestly computed from those numbers alone**. It remains open, with the exact missing data specified; neither a fake diffusive absorber nor invented kernel is substituted.

The bath-jump operator provides no new central radial potential \(\Phi\), rotor–bath Hamiltonian, or detector response coupling. Thus no derived correction to \(\Xi=(1-R\Phi''/\Phi')/3\), no value of G, and no new gravity field law. The existing null \(\Xi=1\) for a Newtonian point source remains standard gradiometry.

## Disposition of the three requested open gates

1. Exact killed versus censored **jump-operator structure and matching rule: CLOSED MATHEMATICALLY**; global source-specific kernel evaluation still open.
2. Exact surviving population **evolution and hazard-covariance identity: CLOSED MATHEMATICALLY**; finite-temperature BPS numerical QSD not established for lack of global collision data.
3. Derived \(\Xi\) coupling **NEGATIVE under available physical operators**; new interaction would be an extra assumption, not a Cone prediction.

**Operations:** all this research performed in gravity lane, **no sandbox handoff** while Suzuki uses compute. No papers, far-tail, or prior ledger objects touched.

**Flags:** \`sandbox_compute_reserved_for_suzuki=true\`; \`new_sandbox_handoff=false\`; \`G_derived=false\`; \`Xi_novel_signal=false\`; \`full_BPS_QSD=UNRESOLVED_MISSING_GLOBAL_KERNEL\`; \`survivor_selection_identity=EXACT\`; \`far_tail_touched=false\`.
