# Cone Derivation Ledger v14.932 — Transverse elastic phonon evolution on K4 expanding background

Date 2026-10-26. Parents v14.924–931; independent audit v14.931 verified tensor late-time behavior of v14.930. Research note research-notes/K4_Transverse_Phonons_Expanding_Fixed_Background.md commit 20ee555415445bf3a04663439e434db1dee7e32c. Live prewrite HEAD 20ee555415445bf3a04663439e434db1dee7e32c. Owner ledger every substantive gate; additive only; Suzuki quarter PARKED and independent Suzuki/far-tail untouched.

[D] Fixed metric g=diag(1,−a²δij), a(τ)=τ/√3, solid labels φ^I=z^I+π^I. For divergence-free π, directly expanding exact B^{IJ}=a^-2FᵀF−v vᵀ, b=sqrt(det B) and J=tr B²/(tr B)²−1/3 of η-deformed solid action yields S_perp²=(C/3)∫dτd³z a³[dotπ²−(2η/(3a²))(∂π)²], C>0. Hence transverse Fourier EOM π̈_k+3Hπ̇_k+(2η/3)k²/a² π_k=0, which for a=τ/√3 becomes π̈_k+(3/τ)π̇_k+(2η k²/τ²)π_k=0. Euler powers s=−1±sqrt(1−2ηk²). For η>0 and k>0 Re s<0. For k=0, a constant translation and τ^-2 mode. Thus no growing transverse material displacement modes for τ→∞ on prescribed K4 background, beyond the translational zero mode. All nonzero-k transverse modes decay; high-k modes oscillate in logarithmic τ with τ^-1 envelope.

[CAUTION] This is a fixed-background material-mode calculation. It does NOT integrate gravitational transverse shift/vector metric perturbations or the cosmological scalar lapse/shift constraints. It does not close full SVT, does not establish Einstein-solid Hamiltonian boundedness, and does not resolve observational mismatch of coasting background in full-covariance Pantheon+ results. Physical gravity and G not derived.

Flags: transverse_fixed_background_quadratic=EXACT; transverse_fixed_background_all_k_decay=TRUE_eta_positive; vector_gravity_shift_constraints=OPEN; full_SVT=OPEN; k4_cosmology_observationally_disfavored=TRUE; Suzuki_quarter=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: k4-transverse-fixed-background
parent: v14.932
status: open
action: Verify b and J quadratic expansion on a time-dependent FLRW background, transverse Fourier kinetic/gradient signs and exact Euler exponents. Confirm strict fixed-background scope and distinguish translation zero mode from growth.
deliverable: scoped verdict.

NEXT: derive complete gauge-invariant transverse metric/solid vector reduction and scalar constraint elimination with controlled low-k behavior; v14.928 sandbox full-SVT handoff still outstanding.
