# Cone Derivation Ledger v15.102 — Shift-restored quadratic normal energy and homogeneous Hamiltonian response

Date 2026-10-29. Parent gravity v15.096, live latest unrelated Sandbox v15.101 untouched. Research note research-notes/K4_Shift_Restored_Quadratic_Matter_Hamiltonian_Response.md at 331950ccaea79f7523d72d933632644b5a114142. Prewrite live HEAD checked. Suzuki physical weld PARKED.

[D] For canonical 3-scalar rho_n=(C/3)Σ[(dotφI−N^j∂jφI)^2/N²+h^ij∂iφI∂jφI], h=a²(1−2ψ)δ, N=1+α, N^i=β^i, φI=zi+πI, κC=1, first-order normal velocity is dotπI−βI. Because background velocity vanishes, its degree-two square is |dotπ−β|² with no lapse α at this order. Exact degree-two matter normal density: 2κrho_n2=(2/3)|dotπ−β|²+(2/(3a²))(|∇π|²+4ψdivπ+12ψ²). This restores the shift absent from restricted v15.096 and can remove coordinate-velocity IR defects in physical normal energy.

[D] For spatially periodic conformal perturbations and second-order homogeneous variables ψ2,α2, the linear Hamiltonian constraint average is −12H⟨dotψ2⟩−12H²⟨ψ2+α2⟩, using source ψ sign opposite to epsilon=+2ψ in earlier v15.011. Thus order-two equation H1[U2]+H2[U1]=0 gives 12H⟨dotψ2⟩+12H²⟨ψ2+α2⟩=⟨H2[U1]⟩. Nonzero quadratic mean is not by itself incompatible; second-order homogeneous response participates.

[OPEN] Full H2[U1] must incorporate lapse/shift-dependent extrinsic curvature, the already-known spatial R3, and corrected matter normal density, plus gauge-valid first-order constrained data. No automatic cancellation or full solvability proven, nor nonlinear global stability.

Flags: corrected_quadratic_matter_normal_energy=DERIVED; quadratic_normal_velocity_shift=RETAINED; homogeneous_Hamiltonian_second_order_response=DERIVED_CONDITIONAL_GAUGE; full_extrinsic_H2=OPEN; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: shift-restored-quadratic-matter-Hamiltonian
parent: v15.102
status: open
action: Verify lapse absence in quadratic normal kinetic term, scalar gradient coefficients, and averaged conformal-sign H1[U2]; request full extrinsic H2 for next gate.
deliverable: scoped verdict.

NEXT: compute α1,β1-dependent extrinsic curvature quadratic terms and full first-order-constrained Hamiltonian source zero-mode.
