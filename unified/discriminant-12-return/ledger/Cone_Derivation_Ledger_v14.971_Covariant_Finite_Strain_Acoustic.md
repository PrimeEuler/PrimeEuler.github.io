# Cone Derivation Ledger v14.971 — Covariant longitudinal acoustic instability at finite strain

Date 2026-10-26. Gravity parent canonical v14.970. Research note research-notes/Covariant_Finite_Strain_Longitudinal_Acoustic_Symbol.md committed a4164402ec7c796bd35e63406efa73b3859aca70. Prewrite HEAD a4164402ec7c796bd35e63406efa73b3859aca70. Additive gravity only; independent Sandbox spectral/spectral-SVT and Suzuki quarter physics weld untouched/PARKED.

[D] Material action L_m=−W(B), B^IJ=−g^μν∂μφ^I∂νφ^J, W(B)=C(det B)^(1/3)[1+ηJ(B)], J=tr B²/(trB)²−1/3. On local Minkowski metric background φ^I=(tx¹,x²,x³), B=diag(t²,1,1), t>0, perturb φ¹=tx¹+π(τ,x¹). Exact quadratic principal Lπ=W'(t)/(2t) dotπ²−W''(t)/2 (∂1π)², with W(t)=C t^(2/3)[1+η((t⁴+2)/(t²+2)²−1/3)]. Thus longitudinal c_L²(t)=tW''(t)/W'(t) where W'>0. At t=1, W'(1)=2C/3, W''(1)=2C(8η−3)/27, c_L²(1)=(8η−3)/9, exactly reproducing prior isotropic v14.926 sound speed. For any η≥0 and t sufficiently large, W'∼(2C/3)(1+2η/3)t^(-1/3)>0, W''∼−(2C/9)(1+2η/3)t^(-4/3)<0 and c_L²→−1/3. Therefore genuine high-frequency longitudinal GRADIENT INSTABILITY arises in locally flat prescribed anisotropic material backgrounds; global material high-strain stability fails even inside isotropic acoustic window 3/8<η≤3/2.

[N] η=3/4: c_L²(1)=+1/3, c_L²(2)=1/13, c_L²(3)=−0.3312273, c_L²(5)=−0.4657172, c_L²(10)=−0.3978833. Check via direct analytic derivatives recorded in source.

[SCOPE/O] Constant-gradient background solves material field equation on fixed flat metric but its nonzero stress generally violates vacuum flat-metric Einstein equations; no claim of existence of same finite strain in fully coupled K4 Einstein+material background or complete scalar/vector constraint stability. The isolated material principal-symbol instability is stronger than mere v14.970 static rank-one failure, but does NOT certify entire dynamical gravity system. Repair requires constitutive modification with separately justified source principle, potentially altering coasting background and other modes. Quarter/Noether charge and Newton G remain unselected.

Flags: covariant_matter_finite_strain_symbol=DERIVED; local_isotropic_sound_speed=VERIFIED_MATCH; large_strain_longitudinal_cs²=NEGATIVE; fixed_metric_material_gradient_instability=PROVED; full_perturbed_Einstein_system=NOT_CERTIFIED; Newton_G=NOT_DERIVED; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: finite-strain-covariant-longitudinal-acoustic
parent: v14.971
status: open
action: Independently vary B11 including velocity sign, verify kinetic W'/t, gradient W'', isotropic speed/large-t negative limit, and keep fixed-metric matter principal-symbol scope separate from a complete coupled Einstein solution.
deliverable: scoped verdict.

NEXT: test modified non-saturating finite-strain mean-gap constitutive functions and evaluate whether they preserve K4 coasting background, η acoustic window, and positivity for all principal gradients; coordinate separate Sandbox scalar/vector work without changing its frozen payloads.
