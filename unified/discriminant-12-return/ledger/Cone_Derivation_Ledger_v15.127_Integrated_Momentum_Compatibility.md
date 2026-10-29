# Cone Derivation Ledger v15.127 — Global ADM momentum compatibility for certified standing scalar mode

Date 2026-10-29. Gravity parent v15.124; build-2 scalar source certified Sandbox v15.118 and Audit R403. Research note research-notes/K4_Second_Order_Global_Momentum_Standing_Mode_Compatibility.md commit ae0c0c0c4a9d6d588b6c01035a0636a3765dfac4. Concurrent Lane A v15.126 has priority; gravity renumbered to v15.127. Prewrite HEAD checked. Protected unrelated lanes untouched; Suzuki physical-quarter weld PARKED.

[D] Exact canonical H_i=−2∂_j(h_ikΠ^{kj})+Π^{jk}∂_ih_jk+p_I∂_iφI=0. On spatial periodic T³ the integrated divergence vanishes. Hence the full spatial-average momentum compatibility is ∫(Π^{jk}∂_ih_jk+p_I∂_iφI)=0 for each i.

[D, SCOPED] In source-certified build-2 single longitudinal standing-wave ansatz h=a²(1−2εΨ cos kz)δ, N=1+εA cos kz, B=0, φ³=z+εp sin(kz)/k, the z-component integrand is odd under z→−z: Π and ∂zφ³ even, ∂zh and p3 odd. Global z momentum therefore vanishes exactly by parity (and transverse x/y components vanish). Thus this standing-wave quadratic self-interaction imposes no additional INTEGRATED momentum obstruction beyond the Hamiltonian-mean quadrature from v15.124. This is a global symmetry fact, not proof local order-two momentum constraint; harmonics at 2k can be nonzero locally and require second-order correction.

[OPEN] For arbitrary traveling-wave superpositions integrated momentum may not vanish and can require compensating data. Local second-order H_i, evolution compatibility, homogeneous lapse/time gauge, k→0 uniform bounds, and nonlinear future stability OPEN. No conclusion full second-order constraint system solvable.

Flags: exact_integrated_momentum_identity=DERIVED; certified_standing_mode_global_momentum=ZERO_BY_PARITY; full_local_order2_momentum=OPEN; simultaneous_Hamiltonian_momentum_solvability=OPEN; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: gravity-global-momentum-parity
parent: v15.126
status: open
action: Independently verify exact momentum density and parity argument; inspect local sin(2kz) order-two momentum harmonic, and determine candidate linear correction to cancel it, distinguishing global constraint from local solvability.
deliverable: scoped verdict.

NEXT: explicitly compute local second-order momentum harmonic and solve it together with nonzero-mode Hamiltonian correction, while retaining the audited source conventions.
