# Cone Derivation Ledger v14.829 — Coupled pendulum/displacement elastic modes

Date 2026-10-24. Gravity subgate. Parents v14.626, v14.826–828. Audit v14.828 verified v14.825–827. Research note research-notes/Hyperbola_Pendulum_Micropolar_Displacement_Rotor_Gate.md, commit dae6319ddfd239eb831b00393d43cffba1b1fb0b. Prewrite HEAD dae6319ddfd239eb831b00393d43cffba1b1fb0b. Additive only, Suzuki/far-residual untouched.

## Translation-invariant micropolar medium [D]
Introduce three-component displacement u, independent microrotation θ, densities ρ_m>0, j>0, elastic bulk modulus B, deviatoric shear μ>0, rotor–curl coupling γ>=0, pendulum restoring stiffness K>=0 and rotor gradient coefficient A>=0:
\[
\mathcal L={ρ_m\over2}|\dot u|²+{j\over2}|\dot θ|²
-{B\over2}(\operatorname{div}u)²-\mu|\operatorname{dev}\operatorname{sym}\nabla u|²
-{\gamma\over2}|\operatorname{curl}u-2θ|²
-{K\over2}|θ|²-{A\over2}|\nabla θ|².
\]
This action is invariant under translations u→u+constant, avoiding the pinned-displacement defect of v14.827. K pins *orientation*, not displacement. The model is nonrelativistic and constitutive: it is not an independently derived GR matter action.

## Fourier-sector gate [D]
For wavevector magnitude q, longitudinal displacement decouples from rotor via curl(grad φ)=0:
\[
\omega_L²=(B+4\mu/3)q²/ρ_m.
\]
Longitudinal rotor has \(\omega_{\theta L}²=(K+4γ+Aq²)/j\).
Each transverse helicity has mass-weighted stiffness eigenvalues
\[
\omega_\pm²=\frac12\left[a+d\pm\sqrt{(a-d)²+4b²}\right],
\]
with \(a=(\mu+\gamma)q²/ρ_m,\ d=(4γ+K+Aq²)/j,\ b=-2γq/\sqrt{ρ_mj}\). The transverse stiffness determinant is \(q²[4γ\mu+(\mu+\gamma)K+(\mu+\gamma)Aq²]\), nonnegative for nonnegative parameters. Hence acoustic transverse and optical rotor modes can be nonnegative, while longitudinal waves require \(B+4\mu/3≥0\). Stronger positivity of bulk energy requires B≥0 separately.

## Gravity compatibility remains conditional [O]
The effective relativistic fluid's w=-1/3 gives negative adiabatic bulk sound-speed squared; neither the pendulum K nor rotor curl coupling γ changes the decoupled longitudinal criterion. A relativistic isotropic elastic completion with adequate μ could alter the longitudinal speed, but its moduli, energy conditions, and covariant perturbation equations have NOT been derived from this rotor action. Newton G remains externally specified.

Next: formulate covariant material-coordinate shear invariants and test background p=-ρ/3 against scalar/vector perturbations and thermodynamic stability; preserve independent spin-2 graviton sector.

Flags: translation_invariance=EXACT; transverse_two_branches=EXACT; longitudinal_rotor_decoupling=EXACT; longitudinal_stability_conditional=TRUE; full_covariant_medium=OPEN; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: micropolar-lattice-stability-review
parent: v14.829
status: open
action: Recompute variational Euler-Lagrange equations and helicity-block stiffness eigenvalues, check q→0 spectrum and compression criterion, and verify relativistic scope constraints. No Suzuki/far-tail writes.
deliverable: independent scoped verdict.
