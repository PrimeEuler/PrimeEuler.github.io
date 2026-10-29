# Cone Derivation Ledger v15.138 — Spatial traceless evolution rejects restricted 2k correction

Date 2026-10-29. Gravity parent v15.137, research note research-notes/K4_Second_Order_2k_Traceless_Spatial_Obstruction.md commit 7afdd5988d3d24dc6428d5d7bfc00dc4fcb2ace7. Live prewrite HEAD checked. Other lanes untouched, Suzuki physical-quarter weld PARKED.

[D, SCOPED] For h=a²(1−2ψ)δ, N=1+α, β=0, triplet φ³=z+π and κC=1, traceless spatial Einstein equation (zz−xx) gives exact necessary condition
E=−N''+2ω'N'+N[−ω''+ω'^2−(2/3)(2π'+π'^2)]=0, ω=(1/2)ln(1−2ψ), primes ∂z. At linear order k²(A−Ψ)−4p/3=0, satisfied by source-certified build-2 fields from v15.118.

[D, RESTRICTED SECOND ORDER] Insert ψ=εΨ cos kz+ε²X cos2kz, α=εA cos kz+ε²Y cos2kz, π=ε p sin kz/k, no order-2 π nor shift, conformal spatial metric throughout. cos2k component is E2=4k²(Y−X)−(3/2)k²AΨ−(5/2)k²Ψ²−(2/3)Ap−p²/3. For v15.137 simultaneous 2k Hamiltonian/momentum X,Y and certified oscillator, symbolic residual
E2=−[(12k²+5)t²pdot²+(40k⁴+86k²+32)t p pdot+(3k⁶+43k⁴+71k²+24)p²]/[9k²(1+k²)²(4k²+1)].
Hence e.g. p=0,pdot!=0 gives E2=−(12k²+5)t²pdot²/[9k²(1+k²)²(4k²+1)] ≠0. The earlier displayed -5 numerator without 12k² is only its k→0 leading coefficient; exact result includes (12k²+5).

[VERDICT] Restricted choice π2=0, β2=0 and conformal h2 only is NOT an Einstein spatial evolution solution for generic standing-wave data, although both second-order constraint harmonics solve exactly. This does not imply full nonlinear GR-triple instability or second-order no-go; must enlarge ansatz by order-two anisotropic h2, scalar matter correction, or shift and satisfy trace/matter-wave evolution, with IR estimates still open. Extrinsic shear vanishes within restricted β=0 conformal metric, which is why spatial traceless equation becomes elliptic and supplies separate obstruction.

Flags: spatial_traceless_2k_residual=GENERIC_NONZERO_RESTRICTED; constraints_2k=SOLVED_AS_V15_137; restricted_evolution=FAILS_GENERICALLY; full_order2_evolution=OPEN; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit, sandbox
type: gravity-traceless-2k-evolution
parent: v15.138
status: open
action: Independently reconstruct ADM spatial traceless (zz−xx) equation from full source build (including matter), verify linear k²(A−Ψ)=4p/3 and the displayed quadratic source/residual. Expand second-order ansatz to include appropriate traceless metric shear/matter displacement and/or shift, test all equations and IR. Distinguish restricted failure from full-system failure.
deliverable: scoped independent verdict and minimal extra-field recommendation.

NEXT: allow anisotropic metric scalar shear and source-faithful second-order scalar displacement; solve traceless evolution together with trace, constraints, and matter wave.
