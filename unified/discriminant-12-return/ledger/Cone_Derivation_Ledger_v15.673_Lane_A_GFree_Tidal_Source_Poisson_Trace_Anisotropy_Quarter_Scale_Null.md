# Cone Derivation Ledger v15.673 — Gravity lane: G-free rotor ratio is an exact Poisson-source trace diagnostic, not a quarter-grid gravitational prediction

**Date:** 2026-11-11. **Parents:** v14.680–700 cone phase/rotor hierarchy; specifically **v14.700 already proved** the calibrated dimensionless rotor ratio Xi=(1−R Phi''/Phi')/3 and its point-mass Xi=1, finding it standard gradiometry; `research-notes/Cone_Phase_Response_Equivalence_and_Eccentric_Obstruction.md` already proved the rho_ecc=1 cone phase states unitarily equivalent to spherical harmonics and flagged rho_ecc≠1 as source-unselected; v14.925 source nonuniqueness; `research-notes/Gravity_Pivot_Source_and_Field_Equation_Gate.md`; v15.544 and audited v15.524 standard tidal rank-two anatomy; v15.672 closes ancillary Euclidean TN ladder as source-unselected. **Status:** [D] exact new **source-side rewrite and separating tests** of an existing observable, within Newtonian spherical weak-field and a separately specified cosmological source; [N] exact SymPy reproducibility; [O] original Cone-selected stress-energy, modified field equation, parameter-free observable. **Live prewrite HEAD:** cbbbdf3314066455d136b182e49a7cd715de3b13 (new additive script), no filename v15.673 collision found. No Suzuki original frozen or other protected object touched; no re-numbering old historical collision files.

## Redundancy boundary

Xi is **NOT new** here; v14.700 fully derived and classified it. So is the unitary equivalence of rho_ecc=1 phase-integral rotor. This gate does not repeat either as an originality claim. It tests the missing source field equation, the `1/4` versus `1/2` pure-scale hypothesis, and standard matter/Lambda contamination with independent exact formulas.

## Gate 188 — Xi is exactly the normalized local Poisson source in a spherical Newtonian field

Let g(R)=Phi'(R), t=g/R, lambda_r=Phi'' and lambda_t=g/R (the two degenerate transverse Hessian eigenvalues). The static trace is

**tr Hess Phi=lambda_r+2 lambda_t=∇²Phi**, and the traceless tide is lambda_t−lambda_r. The already-certified rotor ratio can be rewritten

**Xi=(lambda_t−lambda_r)/(3lambda_t)=1−(∇²Phi)/(3lambda_t).**

If a conventional Newtonian potential obeys ∇²Phi=4πG rho_m−Lambda c², this becomes

**Xi=1−[(4πG rho_m−Lambda c²) R]/(3g).**

These are identities of the specified nonrelativistic spherical model, not a new gravitational equation derived from the Cone. In an exact Newtonian, spherical, matter-free domain with Lambda=0, Xi=1 independently of point-source mass and G. Any Xi≠1 can originate from local matter density or Lambda, or outside the assumptions from nonsphericity, relativistic effects, or nonstandard dynamics. **Measuring Xi alone cannot uniquely identify a Cone source.** It is not generally correct to call Xi≠1 evidence of modified gravity without independently excluding conventional sources and calibration/systematics. For full GR, covariant geodesic-deviation tidal tensors and observer frames are required; the Newtonian Hessian must not be promoted as an exact GR observable.

## Gate 189 — exact trace/traceless separation in the Schwarzschild–de Sitter weak-field comparator

Use Phi=−A/R−Lambda c² R²/6, A>0 (A=GM only as an ordinary GR/Newton comparator). The Hessian eigenvalues are

**lambda_r=−2A/R³−Lambda c²/3**,
**lambda_t=A/R³−Lambda c²/3**.

Hence **tr Hess Phi=−Lambda c²**, while **lambda_r−lambda_t=−3A/R³** exactly. The cosmological-constant part is isotropic and disappears from the orientation-sensitive quadrupole tracefree Hessian, while the rank-one gravitational acceleration is **g=A/R²−Lambda c²R/3**. Thus **Xi_SdS=1/[1−Lambda c² R³/(3A)]**, where the denominator is nonzero (g≠0). This is a known standard-source effect and needs independent Lambda and A to predict a number; its equality to a Cone grid offset is not demonstrated. A nonzero Lambda changes the normalized rank-one/rank-two ratio even though the tidal anisotropy remains point-mass-like. Distinguish isotropic Ricci-type source from tracefree Weyl-type tidal geometry; no claim this Newtonian decomposition proves full GR Ricci/Weyl identities.

## Gate 190 — half-grid/quarter-grid geometry does not alter scale-free point-source Xi

For ordinary Phi=−A/R, under a *physical* R→R/2 comparison with the same A, g scales ×4, each Hessian component scales ×8 and **Xi remains exactly 1**. The EM grid parameter u=1/2 versus gravitational parameter u=1/4 is a geometrically prescribed **factor-grid label**, not automatically a physical radial coordinate. Even if one provisionally identifies their ratio with a factor-two physical radius map, this yields *no distinct dimensionless tidal Xi*: scale covariance cancels, leaving the standard gradiometry result. A physically different Xi requires a modified source, non-1/R radial law, independent metric coupling, or changes in probe response, each requiring derivation.

## Gate 191 — explicit source nonuniqueness with fixed Cone data

As a second algebraic witness, the family Phi_B=−A/R−B/R³ (with B a free dimensional coefficient), has

**Xi_B=(A R²+5B)/(A R²+3B)**,
**∇²Phi_B=−6B/R^5** for R>0. This can be interpreted under the conventional Poisson equation as a distributed density (sign depends on B) rather than a new gravitational law. It is a mathematical source-nonuniqueness witness, not a claim that every B gives a globally regular positive-density isolated source. The underlying Cone identity T²=X²+Y², its half/quarter grid placements, and standard rank-1/rank-2 Wigner weights do not fix B, rho_m, Lambda, or even which covariant metric/stress tensor completion to choose (as separately proven in the gravity pivot and v14.925). Thus any nonunity Xi obtained by selecting one of these sources is **source input**, not a dimensionless physics prediction deduced from the Cone.

## Verdict, exact reproducer and audit

**Proved:** Existing G-free `Xi` is a normalized Poisson-source/trace observable; the rank-two traceless tide cancels isotropic Lambda, while rank-one acceleration does not; the point-source Xi is invariant under scale-only half-grid/quarter-grid identification; explicit free source coefficients can vary Xi without changing any Cone factor identity. **Negative gate:** no uniquely sourced non-GR gravitational/tidal number follows from this route. **Still open:** derive a specific metric/stress-energy equation or physical probe action from intrinsic Cone dynamics with all free dimensions and selectors accounted for. The rho_ecc≠1 phase family, separatrix logarithm, apex seat, physical Suzuki-quarter weld remain separate hypotheses, not silently used here.

**Reproducer:** `research-notes/gravity_xi_poisson_source_v15_673.py`, committed at cbbbdf3314066455d136b182e49a7cd715de3b13. Independently executed exact SymPy derivation locally (PASS): Xi/Laplacian relation, Λ trace cancellation and Xi, point-source half-radius g×4/Hessian×8 with unchanged Xi, and Phi_B source nonuniqueness. Avoid image generator.

**HANDOFF** external audit, gravity and sandbox: verify the exact Hessian eigenvalues/Poisson rewrite, correct sign and distinction of Lambda, the radial similarity null, and provenance attribution to already audited v14.700. Flag any spurious GR-covariant overinterpretation of the Newtonian tensor. Preserve protected Suzuki lane, audit history and historical filename collisions.

**NEXT GATE:** If returning to physics discovery, demand an explicit **source selector** and an independently varied action/coupling whose stationary solution predicts an invariant beyond standard Poisson/GR; otherwise close weak-field scale-only quarter-grid hypotheses as dimensionless tidal non-predictions. Test anisotropic/shear model only with conserved stress energy and stability (v14.925, v14.955) before reporting a physical tidal deviation.
