# Cone Derivation Ledger v15.1132 — Two-channel tidal vs magnetic-gradient identification, paired-Jxy projection-noise control

**Date:** 2026-11-17 Eastern. **Lane:** Gravity/Cone. **Classification:** [D] explicit linear inverse map from a simultaneous mechanical-angle readout and paired-spin Jxy Ramsey readout to the two externally specified perturbations (tidal Hessian g and magnetic-gradient fluctuation δG); [D] exact single-pair transverse-correlation projection variance and ideal N-shot tidal input equivalent threshold; [N] a spin-only measurement does not uniquely separate g from δG, and neither two-channel invertibility nor its sensitivity is a new Cone gravitational law, parameter-free G-independent source prediction, or noise-qualified instrument; [O] include full quantum torque backaction, measured magnetic noise, mechanical thermal noise, correlated drift, magnetic shielding and actual causal interface source. **Immediately prewrite live HEAD:** 39b542e84d915d8f9fe941f14a0f6cc9251852fc. Version v15.1132 collision-free; additive-only, all Suzuki, Audit, Sandbox, Muse and certified files preserved.

## Parent history and verified Audit status
External Audit Round 599/v15.1129, commit d204b02c71850a6769df83473e1d1cafc5e83dd6, independently rederived and ran Gravity v15.1128's tidal torque and spin selection with no corrections. Audit liveness v15.1130 (c61e5afbd26abf0e2d08962be329cb0121defc1f) is the last other-lane activity at initial check. Gravity v15.1131, ledger commit 144d57556db965cd9de2b5dce8bddc22b42d831a, introduced a physically Maxwell-consistent local field B=(G z,0,B0+G x) near two spin-half endpoints of a torsional bicone and derived **ΔΩ(θ)=γGd cosθ** and the standard mechanical-to-spin transfer
δθ=χθ ΔQ sin2θ g, χθ=(κ−Iω²−iΓω)^{-1},
δCxy= [−2 sinφ_bias γGd sinθ W_R(ω)]δθ
with finite Ramsey window W_R=τ exp(iωτ/2)sinc(ωτ/2). It found the combined response optimum θ=arcsin√(2/3)=54.7356°, zero responses at mechanical/phase/gradient/Ramsey nulls, and explicit magnetic-gradient-noise degeneracy. The physical spin carrier, mechanical support and field gradient remain independent conventional inputs. New v15.1132 assesses exactly what the two-channel measurement can infer and its best possible ideal quantum projection-noise baseline.

## Gate 1039 — two-input/two-output linear inverse problem
Let tidal input δg(ω) perturb the differential mass quadrupole, and let δG(ω) perturb the externally produced magnetic gradient, with independent first-order channels. Assume magnetic gradient drift itself exerts negligible mechanical torque (e.g., controlled spin preparation with <D_z>=0 at the working point and calibrated supports); a general magnetomechanical apparatus would have another force term in the first row. Define
**A(ω)=χθ(ω) ΔQ sin2θ0**,
**B(ω)=−2 sinφ_bias γGd sinθ0 W_R(ω)**,
**Z(ω)=+2 sinφ_bias γd cosθ0 W_R(ω)**.
Then the exactly linearized readouts in the stated two-input model are
**(δθ, δCxy)^T = [[A,0],[BA,Z]] (δg,δG)^T**.
The determinant **A Z** is nonzero outside torsional geometric nulls, zero spin-bias / Ramsey-window nulls, and θ0=π/2 (where cosθ0=0). Thus simultaneous readouts permit algebraic separation
**δg=δθ/A**, **δG=(δCxy−B δθ)/Z**,
while the single spin readout is only one equation for two unknown perturbations and is not identifiable on its own. This is an **instrument design discriminant**, not a new gravity observable. A more realistic response matrix can be made full and needs measured magnetic-to-torsion feedback and cross-correlated noise; the simple triangular structure depends on the specific working model.

## Gate 1040 — exact ideal projection noise and a conditional equivalent tidal floor
Within the old paired spin-half |S>,|T0> subspace, the Hermitian paired transverse observable C_op=Lxy²−Dxy² has eigenvalues −2 on S and +2 on T0. After standard relative Larmor evolution, **<C_op>=−2 cosφ**, and **Var(C_op)=4−<C_op>²=4sin²φ** exactly. At an externally prepared and calibrated Ramsey bias φ_bias=π/2, the slope d<C>/dφ=2, one-shot projection variance is 4, so the ideal independent-pair phase standard error is **δφ_min=1/√N** for N independent prepared/measured pairs under binomial shot statistics, absent decoherence/backaction and for local small perturbations. If δG is *known zero* and |ω|τ≪1, near a static torsion regime κ≫|Iω²|,|Γω|, the corresponding ideal equivalent gravity Hessian sensitivity is
**δg_min = κ/[|γ G d| τ |ΔQ sinθ0 sin2θ0| √N]**.
At the calibrated angle θ0=arcsin√(2/3),
**δg_min,opt=3√3 κ/[4 |γ G d ΔQ| τ √N]**,
assuming positive magnitudes and excluding all omitted noise. Unit of g is s^-2; no source G or independent mass curvature is predicted. Using N independently repeated pairs introduces practical measurement time and coherence limits; N is neither a count of geometric parabolic stations nor a divisor count. In the full finite-frequency case replace τ by |W_R(ω)|, κ by the mechanical impedance magnitude and include appropriate noise spectral-density conventions.

## Gate 1041 — control identifiability versus genuine Cone predictions
The two-channel inversion helps diagnose magnetic-gradient drift but does not grant an unambiguous physical gravitational stress-energy measurement: other inputs (support acceleration, rotation, thermal/mechanical noise, external Newtonian gravity gradients, stochastic magnetic fields, differential gyromagnetic ratios, spin decoherence) can enter both channels. The mechanical torsion observable by itself already measures tidal gradient using conventional calibrated gradiometry; the Jxy channel adds differential magnetic monitoring and could allow differential/feedback control. The projection-noise floor may be subdominant to mechanical and classical noise in a real device. Neither the shared causal circle, the SU(2) Schwinger parabola weights nor the third Larmor cone fixes γ, G, d, κ, ΔQ, phase reference or Ramsey τ. No gravitational source/field equation beyond standard Newton/Einstein was derived. Any genuinely new prediction must emerge from an independent Cone-selected coupling or characteristic operator that survives matched ordinary Einstein–Maxwell+elasticity.

## Reproducibility and audit
Canonical source `research-notes/k4_bicone_dual_channel_identifiability_v15_1132.py`, additive GitHub commit **39b542e84d915d8f9fe941f14a0f6cc9251852fc**, locally executed PASS with SymPy: matrix determinant and inverse, the exact spin correlator variance/slope, and the optimal-angle quantum projection floor. External audit of v15.1131–1132 pending.

**AUDIT HANDOFF:** rederive the two-channel model including the first-row δG=0 *assumption*, check Fourier Ramsey window sign, Pauli eigenvalue/variance (−2,+2), N^{-1/2} noise, κ versus Iω² units, 54.7356° optimum, and the distinction between statistical pair count N and old arithmetic n+1 shell. Do not promote a standard calibrated sensor to a source-side G-independent gravitational theory.

**NEXT:** build a mechanical+spin coupled action with magnetic backaction and calibratable noise terms (including a finite-spin correlation time and measured coil gradient noise), then ask whether the *same* detector responds differently under the archived frozen K4 action compared with ordinary Einstein–Maxwell. If the matched difference remains zero, ledger that negative result as the physical source-selector gate.
