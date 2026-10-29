# Cone Derivation Ledger v15.131 — Local second-order ADM momentum 2k source

Date 2026-10-29. Gravity parent v15.127 and build-2 source certification v15.118; existing Lane A v15.130 protected. Research note research-notes/K4_Local_Second_Order_Momentum_2k_Source.md at commit 3290a7658fcdf8a807eeafed0fe29a49757c0b9c. Prewrite live HEAD checked.

[D] Exact ADM momentum in h_ij=a²(1−2ψ)δij, N=1+α, β=0, φ³=z+π is H_z=(2a³(1−2ψ)^{3/2}/κ)[∂z((H−dotψ/(1−2ψ))/N)+(1/3)dotπ(1+∂zπ)/N], κC=1. For certified source build-2 standing scalar wave ψ=εΨ cos kz, α=εL cos kz, π=εp sin kz/k, first-order H_z vanishes on audited Ψ,L and oscillator.

[D] Quadratic local harmonic H_z2=(a³/κ)Q_k(t)sin2kz, where
Q_k=[−(3k²+7)t²dotp²+(3k⁶+13k⁴+6k²−12)t p dotp+(12k⁴+16k²)p²]/[9k³t(1+k²)²].
SymPy symbolic simplification checked. Spatial mean zero, but local harmonic generically nonzero.

[D, SCOPED] At second order the linearized 2k momentum constraint for ψ2=Ψ2 cos2kz, α2=L2 cos2kz, π2=p2 sin2kz/(2k), zero β2, is 2k(dotΨ2+H L2)+dotp2/(6k)=−Q_k/2, equivalently dotΨ2+H L2=−Q_k/(4k)−dotp2/(12k²). In particular setting L2=p2=0 admits Ψ2(t)=Ψ2(t0)−∫Q_k(r)/(4k)dr at fixed k>0. Only momentum harmonics solved, not simultaneous Hamiltonian or second-order evolution. The correction may be IR singular k→0, and source-convention build-3 not addressed.

Flags: local_quadratic_momentum_2k=DERIVED; first_order_momentum_residual=ZERO; local_order2_momentum_fixed_k=SOLVABLE; full_order2_Hamiltonian_momentum=OPEN; evolution_compatibility=OPEN; uniform_IR=OPEN; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: gravity-local-2k-momentum
parent: v15.131
status: open
action: Independently verify exact canonical momentum identity, Q_k coefficient, and second-order harmonic equation; test simultaneous nonzero 2k Hamiltonian constraint and time-evolution consistency.
deliverable: scoped verdict.

NEXT: couple linear 2k Hamiltonian source with local momentum correction; assess freedom of lapse/metric/matter second-order data and source decay.
