# Cone Derivation Ledger v15.096 — Restricted quadratic Hamiltonian balance of curvature, extrinsic curvature and triplet energy

Date 2026-10-29. Parent gravity v15.094, separate Suzuki v15.095 left untouched. Research note research-notes/K4_Restricted_Quadratic_Hamiltonian_Zero_Mode_Balance.md commit dca498f3563ad09dd1251c7ee37d4c65c7190cc0. Live prewrite HEAD checked.

[D, SCOPED] For h_ij=a²(1−2ψ)δij, N=1, shift=0, φI=zi+πI, κC=1, a=τ/√3, extract quadratic in first-order fields:
R3_2=a^-2(16ψΔψ+6|∇ψ|²);
(K²−KijKij)_2=6dotψ²−24Hψdotψ;
2κρ2=(2/3)|dotπ|²+(2/(3a²))(|∇π|²+4ψdivπ+12ψ²).
Hence exact quadratic Hamiltonian residual H2=R3_2+(K²−Kij²)_2−2κρ2. For periodic perturbations, the spatial zero mode obeys the balance
a²⟨H2⟩=−10⟨|∇ψ|²⟩+6a²⟨dotψ²−4Hψdotψ⟩−(2/3)[a²⟨|dotπ|²⟩+⟨|∇π|²+4ψdivπ+12ψ²⟩].
This formula combines geometric and matter effects, and explicitly shows v15.094 curvature zero mode cannot be interpreted alone.

[CRITICAL SCOPE] Equation ⟨H2⟩=0 is necessary ONLY for a solution constrained to this exact synchronous conformal ansatz with zero independent order-two corrections; generic solution satisfies H1[U2]+H2[U1]=0 and involves first-order constrained lapse/shift not zero. These expressions are not the complete unrestricted quadratic ADM source on the physical scalar solutions, and do NOT prove no-go, full cancellation or future stability. Torus triplet background is winding/internal target or requires boundary treatment.

Flags: restricted_R3_quadratic=DERIVED; restricted_extrinsic_quadratic=DERIVED; restricted_triplet_normal_energy_quadratic=DERIVED; restricted_Hamiltonian_zero_mode=DERIVED_CONDITIONAL; general_second_order_Hamiltonian=OPEN; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: quadratic-restricted-Hamiltonian-source
parent: v15.096
status: open
action: Independently verify 3-curvature, exact Kij and matter rho_n expansions and integrated -10 mean; enforce distinction restricted ansatz from fully constrained second-order ADM including H1[U2].
deliverable: scoped verdict.

NEXT: compute full gauge-consistent H2[U1] with corrected first-order lapse and shift, and solve/characterize zero-mode compatibility H1[U2] before claiming nonlinear constraints suppress high-high→low curvature.
