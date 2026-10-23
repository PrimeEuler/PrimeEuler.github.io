# Cone Derivation Ledger v14.762 — Hyperbolic integration counterpart and compact-fiber flux gate

**Date:** 2026-10-23 EDT. **Lane:** gravity. **Parents:** v14.592, v14.696, v14.731–761. **Live HEAD:** \`238eda5eb074097faffe9b66853db9f2c64667a2\` immediately prior to write; v14.762 free. Additive-only, no Suzuki sandbox use.
**Research note:** \`research-notes/Gravity_Hyperbolic_Integration_Gate.md\`.

## Exact counterpart [D]

The ordinary compact circular Fourier/Bessel integral \(i^mJ_m(z)=(2\pi)^{-1}\int_0^{2\pi}e^{iz\cos\theta-im\theta}d\theta\) has a noncompact boost analogue \(K_\nu(z)=\int_0^\infty e^{-z\cosh u}\cosh(\nu u)du\), \(z>0\). For ν=0, \(K_0(z)=-\ln(z/2)-\gamma+O(z^2|\ln z|)\). Thus hyperbolic orbit integration can genuinely create a logarithm. It is NOT yet the same as the original cone phase integral, and NOT automatically the elliptic separatrix \(K(e)\); a dynamical z(e) dictionary and integration measure remain necessary. Selecting z by fitting the hierarchy would be circular.

## Bundle curvature [D]

For a hyperbolic spatial base \(H^2\) with metric \(a^2(du^2+\sinh^2u\,d\phi^2)\), a local compact-fiber connection \(\mathcal A=p(\cosh u-1)d\phi\) has \(\mathcal F=p\sinh u\,du\wedge d\phi\), flux \(2\pi p(\cosh U-1)\) over a radius-U disk. This is continuous, not quantized: a disk supplies no closed nontrivial two-cycle. A compact quotient/global U(1) bundle with a specified Chern class can furnish integer flux, but its geometry/topology are external until derived from the Cone.

A static globally causal extension can place a spacelike periodic fiber adjacent to noncompact time \(\tau\); that is a different spacetime construction, not a cure for periodically identified timelike Taub–NUT in its original Lorentzian interpretation.

## Selector status

Hyperbolic integration and compact holonomy **give concrete integral machinery**, not yet a physical selection of the coupling split ψ. Missing: action-derived scale/weight z, correct causal-action or worldline measure, global compact cycle and sourced asymmetry. Next gravity-only test: calculate first and second variations of a normalized hyperbolic partition kernel coupled to the monopole fiber and determine whether holonomy actually lifts ψ degeneracy without putting alpha/G into its coefficients.

**Flags:** \`hyperbolic_integral_kernel=EXACT_CLASSICAL\`; \`Cone_phase_identification=OPEN\`; \`monopole_flux_quantization_on_disk=FALSE\`; \`physical_selector=OPEN\`; \`G_derived=false\`; \`Suzuki_sandbox_reserved=true\`; \`far_tail_touched=false\`.
