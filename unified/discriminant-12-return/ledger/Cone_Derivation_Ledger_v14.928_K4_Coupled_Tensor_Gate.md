# Cone Derivation Ledger v14.928 — Coupled tensor quadratic gate for the four-factor elastic solid

Date 2026-10-26. Parents v14.818–825, v14.923–927. Research note research-notes/K4_Coupled_Tensor_Quadratic_Action_Gate.md commit eaa092d8dfa4f6e762ad319299a93bf2be0e1ad6. Live prewrite HEAD eaa092d8dfa4f6e762ad319299a93bf2be0e1ad6. Additive gravity lane only. Suzuki–1/4 integration PARKED; Suzuki/far-tail untouched; owner per-gate preservation protocol.

[D] Start independent Einstein–Hilbert metric g and solid action −∫√−g C b^(2/3)(1+ηJ(B)), B^{IJ}=−g^{μν}∂μφ^I∂νφ^J, b=sqrt(det B), J=tr B²/(tr B)²−1/3. Flat FLRW background a=τ/√3 when κC=1, with ρ=C/a², κρ=3H². For pure TT tensor γ (trγ=∂iγij=0) parametrization g_ij=−a²(e^γ)_ij, B=a^-2e^-γ; det B=a^-6 so b unperturbed; J=(1/9)trγ²+O(γ³). Thus shear-action second variation adds −∫a³ρη trγ²/9. EH tensor term, after background equation, is Mpl²/8 ∫a³[dotγ²−(∂γ)²/a²]. Net S_T²=(Mpl²/8)∫a³[dotγ²−(∂γ)²/a²−mT²γ²], with mT²=(8/9)κρη=(8η/3)H². EOM ddotγ+3Hdotγ−a^-2∇²γ+mT²γ=0. For η>0 this tensor quadratic sector has healthy positive kinetic, light-speed principal characteristics and non-tachyonic positive mT². At eta=3/4 mT²=2H². This is a cosmological solid-modified TT mode, NOT an empirical graviton mass measurement.

[O] The full coupled SVT theory is NOT certified. Scalar/vector mixing, lapse/shift elimination, gauge constraints, low-k stability and Hamiltonian boundedness remain to be derived. v14.927's local phonon high-k result cannot substitute for those. Even complete theoretical stability would not remove the observed supernova-distance tension: Sandbox full-covariance v14.926 found positive k4-vs-ΛCDM Δχ² under two covariance constructions, independent audit pending. No physical uniqueness, photon coupling, G or eta derivation.

Flags: k4_tensor_quadratic=DERIVED; tensor_kinetic=POSITIVE; tensor_gradient_speed=LIGHT; tensor_effective_mass_squared=(8_over_9)_kappa_eta_rho; tensor_instability_eta_positive=NOT_FOUND_QUADRATIC; full_SVT=OPEN; eta_selected=FALSE; physical_cosmological_fit=DISFAVORED; G_derived=FALSE; Suzuki_quarter=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: k4-elastic-solid-coupled-tensor
parent: v14.928
status: open
action: Independently verify TT expansion J=(1/9)trγ², cancellation of background determinant/Einstein–Hilbert terms, quadratic coefficient mT²=(8/9)κρη and its sign; distinguish TT sector from full SVT/Hamiltonian stability. Do not touch Suzuki/far-tail.
deliverable: scoped tensor-sector audit.

HANDOFF
target: sandbox
type: k4-elastic-solid-full-SVT
parent: v14.928
status: open
action: Starting from frozen metric+solid action and four-factor FLRW background, compute gauge-fixed quadratic scalar and vector actions with lapse/shift constraints eliminated, report kinetic-matrix principal minors, high-k and low-k mode eigenfrequencies, no-ghost and instability intervals, verify independent tensor result, avoid fitting cosmology. Produce reproducer and bounded assumptions.
deliverable: explicit reduced SVT quadratic forms and stability verdict.

NEXT: complete reduced scalar/vector constraints and test whether any eta in (3/8,3/2] survives full cosmological stability; separately audit Pantheon+ full-covariance likelihood provenance and examine physical interpretation of k4 metric.
