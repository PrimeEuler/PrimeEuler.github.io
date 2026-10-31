# Cone Derivation Ledger v15.190 — Independent ADM spatial trace closes corrected 2k scalar harmonic

Date 2026-10-30. Gravity parents v15.188-v15.189, External Audit Round 416 v15.182. Concurrent Lane A v15.189 kept intact. Research note research-notes/K4_Independent_ADM_Trace_2k_Closure.md committed e10f933eaadb27d48dc2f7e733acfe07ad8936d6. Prewrite live HEAD checked. Additive only.

[D, FIXED-K SCOPED] On source build-2 zero-shift conformal ansatz with a=t/sqrt3, k>0, κC=1, the exact trace ADM evolution identity for positive extrinsic convention Kij=dot h_ij/(2N) is 3dotV=D²N−3NV²−(2/3)dotφI dotφI/N, V=(H−dotψ/(1−2ψ))/N. Its cos(2kz) second-order residual on corrected v15.142 solution is
R=3dotV2+(4k²Y+k² P A/2)/a²+3[2H V2+(V1²+2AHV1)/2+H²Y]−d²/(3k²),
where d=pdot, P=first-order ψ cosine, A=first-order lapse cosine, D=dotP, V1=−D−HA, V2=−dotX−HY+[(A−2P)D+HA²]/2. Substitute first-order oscillator, corrected v15.189 quadratic forcing for q, v15.142 constraint corrections X,Y, and their time derivatives. Independent SymPy exact factor result R=0. Thus the previously untested second-order 2k spatial trace equation closes in this gauge, extending v15.188 audited scalar-wave closure and v15.137 constraints plus corrected traceless equation.

[SCOPING] This is not a general global second-order Einstein solution: homogeneous zero-mode trace, arbitrary Fourier interactions, build-3 original-action check, complete vector/tensor Einstein equations, k→0 uniform estimates and future nonlinear stability OPEN. Source-side full ADM action independent external check pending. Results based on Einstein trace equation convention, not source-script direct EL execution.

Flags: spatial_trace_2k=EXACT_SYMBOLIC_ZERO; 2k_scalar_constraints_traceless_wave_trace=CONSISTENT_FIXED_K; homogeneous_trace=OPEN; full_order2_evolution=OPEN; IR_uniformity=OPEN; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit,sandbox
type: gravity-independent-2k-trace
parent: v15.190
status: open
action: Independently derive trace ADM evolution from original corrected source action, confirm displayed trace residual and symbolic cancellation; test homogeneous zero-mode trace alongside v15.124 Hamiltonian quadrature, then check source build-3.
deliverable: independent source-faithful trace certificate and homogeneous compatibility, or exact discrepancy.

NEXT: homogeneous second-order trace compatibility, then multi-mode convolution and IR.
