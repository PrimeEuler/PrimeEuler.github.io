# Cone Derivation Ledger v14.950 — Opposite squeeze self-adjoint spectrum is continuous

Date 2026-10-26. Parents v14.944–949 and historic v13.583. Research note research-notes/Opposite_Squeeze_Selfadjoint_Continuous_Spectrum.md commit 583c2ff7ca2821906d814e6c06be9f5cc57476c1. Prewrite live HEAD 583c2ff7ca2821906d814e6c06be9f5cc57476c1. Gravity-only additive write; Suzuki spectral-quarter identification remains PARKED; no Suzuki/far-tail files touched.

[D] On H=L²(R_+²,du dv), opposite symmetric dilation P_s=(u p_u+p_u u)/2−(v p_v+p_v v)/2=−iℏ(u∂u−v∂v), initially defined on compactly supported smooth functions. The exact canonical coordinates ρ=√uv>0, s=1/2log(u/v)∈R give Jacobian 2ρ, so H≅L²(R_+,2ρ dρ)⊗L²(R,ds) and P_s≅−iℏ∂s. The latter is essentially self-adjoint, with purely absolutely continuous spectrum R and no normalizable point eigenstates. Fourier-transform in s directly verifies. Hence original positive-factor configuration space does NOT quantize the opposite-squeeze charge.

[D/I] Fixed Schwinger SU2 Casimir C=j(j+1)=T²−1/4 or SU11 metaplectic Casimir −3/16 does not alter the spectrum absent an explicit representation/boundary map. Extra compactification s~s+L would yield discrete 2πℏ(n+θ/2π)/L with extra boundary holonomy θ; original s∈R has no such periodicity. The Noether Q=∫ΣF(ρ)n·∂s remains arbitrary initial/boundary data in a chosen action; physical gravity/charge normalization NOT derived. This is a scoped negative result, not a contradiction of exact quarter invariants.

Flags: positive_quadrant_quantum_dilation=ESSENTIALLY_SELFADJOINT; opposite_squeeze_spectrum=REAL_CONTINUOUS; natural_point_spectrum=EMPTY; Casimir_quarter_enforces_discrete_flux=FALSE; s_compactification=ADDITIONAL_ASSUMPTION; G_derived=FALSE; Suzuki_quarter=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: opposite-squeeze-spectrum
parent: v14.950
status: open
action: Check unitary Jacobian, domains/essential selfadjointness, spectral type and whether independent SU2/SU11 Casimirs impose any restriction. Note artificial compactification is not inherited.
deliverable: scoped mathematical verdict.

NEXT: inspect natural product-Hessian kinetic metric as candidate selecting F(ρ), with invariance tests. Maintain separate full-SVT Sandbox work.
