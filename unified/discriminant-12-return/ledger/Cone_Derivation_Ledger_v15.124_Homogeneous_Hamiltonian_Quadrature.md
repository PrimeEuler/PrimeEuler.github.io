# Cone Derivation Ledger v15.124 — Homogeneous second-order Hamiltonian quadrature

Date 2026-10-29. Gravity source-certified parent v15.118, externally checked R403 v15.119, and integrated response parent v15.102. Research note research-notes/K4_Homogeneous_Second_Order_Hamiltonian_Quadrature.md commit d585e738776958312524d61d6d0a791b84a9d403. Prewrite live HEAD checked. Protected Lane A, Sandbox, Audit and Suzuki physical-quarter weld untouched.

[D, SCOPED] For periodic conformal gauge in source ψ sign, spatially averaged order-two Hamiltonian constraint 12H⟨dotψ2⟩+12H²⟨ψ2+α2⟩=F(t), F=⟨H2[U1]⟩ source-certified by v15.118 for fixed single nonzero scalar Fourier mode, H=1/t. Let m=⟨ψ2⟩, n=⟨α2⟩. Then exact d(t m)/dt=t²F/12−n, with explicit quadrature m=t^-1[t0m(t0)+∫_{t0}^t(r²F(r)/12−n(r))dr]. This proves the SCALAR SPATIAL-AVERAGE Hamiltonian equation has a homogeneous response for prescribed n and smooth integrable F; the nonzero source is not itself a no-go.

[D, FIXED-K CONDITIONAL] For the certified linear k>0 scalar oscillator p=O_k(t^-1), dotp=O_k(t^-2), full source-certified lapse α, ψ=O_k(t^-1), ψdot=O_k(t^-2), F=O_k(t^-4). For n=0, homogeneous solution m=C∞/t+O_k(t^-2). Future-normalized integration constant C∞=0 gives m=−(12t)^-1∫_t^∞r²F(r)dr=O_k(t^-2). k-dependent constants and summing over k may be IR singular; no uniform stability theorem.

[OPEN] The full LOCAL constraint operator, second-order momentum constraint, Bianchi/evolution propagation, homogeneous time gauge validity, coupled nonzero modes, and nonlinear future stability not solved. This is an integrated equation only. Build-3 auxiliaries not certified by v15.118.

Flags: homogeneous_order2_Hamiltonian_quadrature=EXACT; fixed_k_source_decay=O_T_MINUS4; homogeneous_metric_response=O_T_MINUS1_WITH_TUNED_O_T_MINUS2; full_order2_constraint_solvability=OPEN; low_k_uniformity=OPEN; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: homogeneous-Hamiltonian-quadrature
parent: v15.124
status: open
action: Verify averaged H1 sign and quadrature, fixed-k O(t^-4) source using deposited v15.118 coefficient formula, and distinguish spatially averaged Hamiltonian from full second-order local Einstein constraints; identify global momentum compatibility.
deliverable: scoped independent verdict.

NEXT: derive exact integrated second-order momentum identity and test whether conserved/zero total momentum provides a separate necessary condition for homogeneous solvability.
