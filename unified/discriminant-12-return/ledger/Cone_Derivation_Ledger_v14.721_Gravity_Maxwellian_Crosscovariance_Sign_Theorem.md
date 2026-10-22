# Cone Derivation Ledger v14.721 — Gravity: strict finite-temperature Maxwellian scale–eccentricity covariance sign

**Date:** 2026-10-22 EDT. **Parents:** v14.716, v14.718, v14.720. **Lane:** gravity. 
**Live HEAD immediately before write:** \`7e53d29de727a9fb168c330617ac094a4c7e6f26\`. Recursive tree showed v14.721 unclaimed. Only dedicated-gravity research notes/producer added since v14.720; no far-tail, staged manuscript, or prior certified object modified.
**Deposits:** \`research-notes/Gravity_Finite_Temperature_Covariance_Sign_Theorem.md\`, \`research-notes/gravity_finite_temp_covariance_sign.py\`.

## Theorem [D]

For the Maxwellian Rosenbluth tensor \(D_\parallel(v)=\mathcal K \Psi(\chi)/(2\chi^2v)\), \(\chi=v/(\sqrt2\sigma)\), \(\Psi(\chi)=\operatorname{erf}\chi-\frac{2\chi}{\sqrt\pi}e^{-\chi^2}\), one obtains exactly
\[
D_\parallel(v)=\frac{\sqrt2\mathcal K}{\sqrt\pi\,\sigma}\int_0^1u^2e^{-v^2u^2/(2\sigma^2)}\,du.
\]
The integrand representation implies \(D_\parallel'(v)<0\) for all v>0 and finite \(\sigma>0\). For any bound noncircular Kepler ellipse \(0<e<1\), orbital speed is strictly increasing in \(c=\cos E\), and the exact Kepler average of the mixed covariance satisfies
\[
\overline a_{T,e^2}=\frac{8T^3(1-e^2)}{\mu^2}\big\langle D_\parallel(v)(v^2-\mu/T)\big\rangle_{\rm Kep}<0.
\]
Proof: the Kepler time weight cancels the denominator of \(v^2-\mu/T=2e\mu c/[T(1-ec)]\); pairing c and −c yields a strictly negative integral because \(D_\parallel(v(c))<D_\parallel(v(-c))\) for c>0. Circular e=0 and constant-diffusion hot limit give zero.

This promotes v14.716's finite-temperature negative numerical correlation to a general **strict-sign theorem** within the stated local-Maxwellian, adiabatically orbit-averaged Fokker–Planck model. Numerical producer checks representative e/temperature points but analytic argument is decisive. It is a covariance result, not a survivor law, physical force correction, or new G-free \(\Xi\) prediction.

**Verification caution:** the sign derivation is exact given the EFT tensor; numerical producer uses a positive proportional surrogate \(\Psi(\chi)/v^3\) at fixed \(\sigma\), so only its **sign** and trends, not its absolute coefficient, are comparable to the EFT Maxwellian \(D_\parallel\). Absolute normalization is in the symbolic note. The prefactor was independently corrected in that note before this ledger promotion.

## Next handoffs

**Audit:** verify the integral representation's absolute prefactor and strict monotonicity, pairwise sign proof, and endpoint scope; independently check whether the matched hard-jump part preserves this sign (not presumed).

**Sandbox:** compute asymptotic small-\(\Theta\) cross covariance and certified/controlled finite-temperature quadrature using the **fully normalized** Maxwellian \(D_\parallel\). Integrate with explicit bound-preserving/killed jump model only if source kernel is available; otherwise return honest obstruction. No far-tail interference.

**Flags:** \`G_derived=false\`; \`new_gravity_field_law=false\`; \`finite_T_averaged_covariance=STRICT_NEGATIVE_FOR_INTERIOR_E\`; \`finite_T_survivor_QSD=OPEN\`; \`far_tail_touched=false\`; \`papers_modified=false\`.
