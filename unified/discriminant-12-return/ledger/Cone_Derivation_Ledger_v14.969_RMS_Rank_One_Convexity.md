# Cone Derivation Ledger v14.969 — RMS shear finite-strain rank-one convexity fails

Date 2026-10-26. Parent gravity v14.965. Live HEAD prewrite 81bc625a6e37dc9930f904a0e07e6671a0254c6e. Separate Lane A v14.966-968 read and collision avoided. Research note research-notes/Finite_Strain_Rank_One_Elastic_RMS_Ellipticity_Test.md commit 81bc625a6e37dc9930f904a0e07e6671a0254c6e. Additive gravity-only; Suzuki physical quarter connection PARKED and protected spectral/far-tail files untouched.

[D] Static material W(F)=C(detF)^(2/3)[1+ηJ(FF^T)] for F∈GL+(3), C>0. The line F(t)=diag(t,1,1) is rank-one because F'=e1⊗e1. With J(t)=(t⁴+2)/(t²+2)²−1/3, W(t)=Ct^(2/3)(1+ηJ(t)). Exactly W''(1)=2C(8η−3)/27, recovering η>3/8 local longitudinal stability threshold. At large t, W''(t)~−C(4η+6)t^(−4/3)/27 <0 for η≥0. Thus global rank-one convexity of this selected energy FAILS for every η in previously derived local acoustic window 3/8<η≤3/2. Exact full derivative and small-t asymptotic recorded in research note. This is a genuine rank-one direction, stronger than prior v14.965 log-deformation nonconvexity.

[scope] The rank-one test applies to static stored energy under B=FF^T and is not identical to the relativistic coupled metric/matter principal acoustic tensor; no claim complete gravitational SVT instability is made. It proves the local near-isotropic elastic health statement cannot be promoted to arbitrary finite strain using mean positivity alone. RMS electric-power analogy remains algebraic, not electromagnetic coupling.

Flags: rank_one_direction=EXPLICIT; at_isotropy_longitudinal_threshold=eta_gt_3_over_8; global_rank_one_convexity=FALSE_FOR_ETA_POSITIVE; full_covariant_principal_symbol=NOT_TESTED; global_GR_stability=NOT_DERIVED; G=NOT_DERIVED; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: finite-strain-rank-one-RMS-energy
parent: v14.969
status: open
action: Check symbolic W'' exact derivative and limits, rank-one line admissibility, recovery local eta threshold and distinction between material rank-one convexity versus covariant relativistic full SVT dynamics.
deliverable: scoped verdict.

NEXT: derive finite-background covariant elastic principal symbol / deformation gradient map, assess if a physically selected modification can preserve healthy behavior without arbitrary fit; keep separate Lane A and Sandbox spectral results untouched.
