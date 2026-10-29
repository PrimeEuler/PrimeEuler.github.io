# Cone Derivation Ledger v15.109 — Integrated complete quadratic Hamiltonian source

Date 2026-10-29. Gravity parent v15.107. Concurrent Lane A v15.108 has priority; gravity renumbered to v15.109. Research note research-notes/K4_Full_Quadratic_Hamiltonian_Integrated_Zero_Mode.md committed 6af42f1e2cfae7ae6e81b324c0fb1dcc061cd921. Prewrite live HEAD checked. Protected Lane A/Suzuki/Sandbox files untouched, physical quarter weld PARKED.

[D] The complete v15.107 quadratic Hamiltonian source in conformal ADM gauge h_ij=a²(1−2ψ)δij, N=1+α, shift β^i and φI=zi+πI integrates on periodic spatial domain to
⟨H2⟩=−10a^-2⟨|∇ψ|²⟩+6⟨dotψ²⟩+24H⟨αdotψ−ψdotψ⟩+18H²⟨α²⟩−12H⟨ψθ⟩+4⟨dotψθ⟩+8H⟨αθ⟩+⟨θ²−SijSij⟩−(2/3)⟨|dotπ−β|²⟩−(2/(3a²))⟨|∇π|²+4ψdivπ+12ψ²⟩,
where θ=div β, Sij=(∂iβj+∂jβi)/2. Exact integrations use ⟨ψΔψ⟩=−⟨|∇ψ|²⟩ and ⟨β·∇ψ⟩=−⟨ψθ⟩. This is the first-order-generated quadratic SOURCE, not the full second-order Hamiltonian equation. The source includes indefinite gravitational correlations; neither universal zero-mode obstruction nor automatic source cancellation has been established.

[O] To evaluate source on physical linear scalar mode, insert the separately audited ψ strain reconstruction and fully consistent lapse/shift with v14.996 sign/gauge conventions; constraints and second-order homogeneous response must be solved together. Correct full equation H1[U2]+H2[U1]=0; on torus, with conformal second-order fields 12H⟨dotψ2⟩+12H²⟨ψ2+α2⟩=⟨H2[U1]⟩. A nonzero quadratic zero mode alone does not prove inconsistency or nonlinear instability. No future nonlinear stability proof.

Flags: full_quadratic_Hamiltonian_source_integrated=EXACT_IN_GAUGE; lapse_shift_matter_correlation_terms=RETAINED; first_order_physical_mode_substitution=OPEN; nonlinear_zero_mode_solvability=OPEN; future_nonlinear_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: integrated-quadratic-Hamiltonian-gauge-source
parent: v15.108
status: open
action: Independently verify sign coefficients and periodic integration against v15.107, then test source after consistent v14.996 scalar mode substitution and second-order constraint compatibility.
deliverable: scoped verdict.

NEXT: reconstruct compatible first-order lapse and shift, substitute the exact ψ strain formula and test low-K Fourier convolution and late-time norm bounds.
