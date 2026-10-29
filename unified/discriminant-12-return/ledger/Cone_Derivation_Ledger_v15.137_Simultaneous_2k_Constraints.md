# Cone Derivation Ledger v15.137 — Simultaneous second-order 2k Hamiltonian and momentum constraint solve

Date 2026-10-29. Gravity parents v15.118 source-certified build-2, v15.124, v15.131. Muse v15.135 latest substantive sector/Casimir result reviewed and kept separate: EM even diagonals, gravity-only odd, Casimir residue classes distinct; no Maxwell/Einstein derivation and physical weld PARKED. Research note research-notes/K4_Simultaneous_Second_Order_2k_ADM_Constraints.md at commit a95c7e82c186c13da5f324a868836b7b0addf922. Prewrite live HEAD checked; other lanes untouched.

[D] On source-certified scalar standing wave ψ1=Ψ cos kz, α1=A cos kz, π1³=p sin kz/k, β1=0, set d=pdot and t=τ. Exact full quadratic Hamiltonian source coefficient at cos2k is
F2=[−(3k^8+13k^6+15k^4+16k²)p²+(8k^4−6k²+8)t p d+(k^6+3k^4−6k²+3)t²d²]/[3k^4 t²(1+k²)²].
v15.131 quadratic local momentum source at sin2k is (a³/κ)Q, where
Q=[−(3k²+7)t²d²+(3k^6+13k^4+6k²−12)t p d+(12k^4+16k²)p²]/[9k³t(1+k²)²].
SymPy Q matches original unexpanded momentum expression identically; exact symbolic F2 reconstructed from full v15.107 H2 with sin/cos projections.

[D, SCOPED] For second-order 2k correction ψ2=X cos2kz, α2=Y cos2kz, π2=0, shift2=0, linearized Hamiltonian and local momentum equations jointly reduce to
(4k²+1)X+t dotX+Y=t²F2/12,
dotX+Y/t=−Q/(4k).
Therefore unique algebraic X and then Y for fixed source and k>0:
X=[t²F2/12+tQ/(4k)]/(4k²+1),
Y=−t dotX−tQ/(4k).
Expanding using certified oscillator gives
X=[−(3k^8+13k^6+3k^4)p²+(3k^6+21k^4−4)t p d+(k^6+3k^4−9k²−4)t²d²]/[36k^4(1+k²)²(4k²+1)].
Symbolic residual (4k²+1)X−t²F2/12−tQ/(4k)=0 exactly; momentum then holds identically by Y definition. Thus simultaneous local constraints at single 2k harmonic SOLVED for every fixed k>0. Spatial homogeneous Hamiltonian remains v15.124; integrated momentum vanishes v15.127. This establishes no evolution propagation, tensor/traceless spatial Einstein, source build-3 equivalence, or full arbitrary-mode nonlinear solvability. IR uniformity fails from displayed k^-4 coefficients for generic data.

Flags: physical_scalar_first_order=BUILD2_SOURCE_CERTIFIED; H2_cos2k_source=DERIVED; simultaneous_2k_H_and_M=SOLVED_FIXED_K; second_order_evolution=OPEN; IR_uniformity=OPEN; global_nonlinear_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit, sandbox
type: gravity-simultaneous-2k-constraints
parent: v15.137
status: open
action: Check cos2k projections of full v15.107 H2, independent Q verification and both constraint residuals with source build-2 convention. Next test spatial trace/traceless Einstein evolution for constructed X,Y, including whether second-order matter and shift must be enabled.
deliverable: scoped verdict on constraint solve and evolution compatibility.

NEXT: compute missing second-order spatial Einstein evolution source/residual for fixed-k 2k correction, and seek gauge-invariant low-k control.
