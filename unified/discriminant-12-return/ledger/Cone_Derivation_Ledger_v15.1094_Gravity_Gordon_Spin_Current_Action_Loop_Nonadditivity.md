# Cone Derivation Ledger v15.1094 — Dirac/Pauli Gordon spin-current versus charged-seat action-loop, and nonadditivity of half-moments

**Date:** 2026-11-17 Eastern. **Gravity/Cone lane. Status:** [D] normalizable localized spinor produces full Dirac leading g=2 magnetic moment solely through Gordon magnetization curl even when convection current is zero; [N] no independent addition of classical seat loop's g=1 moment, no derived Compton radius or novel gravity coupling. **Immediately prewrite live HEAD:** 0b5d4d681bffeca47770462c9572d61144db3788 (new reproducer). Additive only; no Suzuki, Audit, Sandbox, Muse, old certified objects edited.

## Protocol and prior art
Sandbox v15.1091 (commit 5976de3a31100e641a35acc4510fd070d44f9dcd) showed a boosted charged seat's azimuthal B, and its **idealized**, not literal electron, Zitterbewegung loop with r=hbar/(2mc), omega=2mc²/hbar, angular momentum hbar/2, and loop moment qhbar/(4m) (nominal g=1). It described Dirac/Gordon spin-density curl as an imported other half. Gravity v15.1093 contrasted such azimuthal B to our sourceless compact packet's initially generated axial B, and distinguished Faraday electric circulation from mechanical action; that entry includes an explicitly disclosed corrected SymPy structural assertion. External Audit Round 592/v15.1092 (commit ba571054759c6b4d727c33db57812ef483923871) independently confirmed earlier Sandbox v15.1091 and Gravity v15.1089–1090. No new unverified novelty is inferred here.

## Gate 925 — actual low-energy spin-current identity
The standard gauge-coupled Dirac action is S_D=integral sqrt(-g) barPsi(i hbar c gamma^mu D_mu-m c²)Psi (schematic fixed-unit convention). Its electrically coupled current is q barPsi gamma^mu Psi. The Gordon decomposition and Pauli nonrelativistic limit (in flat space, no external vector potential here) yield
j = j_conv + (q hbar/(2m)) curl(chi^dagger sigma chi),
with spin-density spinor chi and the **signed** electric charge q. j_conv=(q/m)Re[chi^dagger(-i hbar grad-q A)chi]. The magnetization term is divergence-free identically as curl of local spin density, but can produce a real magnetic dipole. This coefficient follows from imported standard Dirac/Pauli dynamics. It does NOT emerge from the Cone action circle.

## Gate 926 — explicit localized counterexample to two equal additive currents
Choose normalized real Gaussian orbital probability density rho(x)=exp(-r²/L²)/(pi^(3/2)L³), L>0, spinor chi=sqrt(rho)|up_z>, with zero A and constant up spin direction. Convection current j_conv=0 since the spatial wavefunction is real and the phase is constant. The Gordon magnetization current is
j_spin=(q hbar/(2m)) curl(rho zhat)
=(q hbar/(2m))(partial_y rho,-partial_x rho,0)
=-(q hbar/(m L²))rho(y,-x,0).
It satisfies div j_spin=0 exactly and is nonzero for generic off-axis points. The normalized Gaussian has integral rho=1, integral x² rho=integral y² rho=L²/2. The local-current magnetic moment in this approximation is
mu_z=1/2 integral (x j_y-y j_x) d³x
=(q hbar/(2m L²)) integral(x²+y²)rho d³x
=q hbar/(2m).
Thus even when j_conv=0, the spin current yields the **full leading Dirac moment**, associated with g=2 for S_z=hbar/2. No fixed localization width L is selected. This is a magnetic-moment identity for a specified spinor state (not a claim that the Gaussian is a free Dirac energy eigenstate or a literally rotating charge sphere).

Sandbox's imposed uniform classical ring of radius r=hbar/(2mc), circulating with speed c, instead gives mu_ring=q c r/2=q hbar/(4m), half that value. This is a **different model**, not an independent measured contribution that can be added to the spin current. Simply writing mu_Dirac=mu_ring+mu_ring would be numerically true but does not identify two physically distinct or independently sourced pieces of the actual Dirac state. Spin-orbit effects and bound-state convection can exist in other states; their contributions require the actual wavefunction and gauge field, not this special ring.

## Gate 927 — implications for gravity and Cone selection
A vector magnetic moment calculation by itself is not a gravitational stress tensor or Einstein–K4 source. A physical Dirac-Maxwell-to-K4 construction requires varying the full curved spinor action with respect to tetrad/metric, retaining spin connection, consistent Maxwell current and stress-energy, and solving matter + gravitational constraints. The Belinfante-improved symmetric stress energy incorporates spin effects in standard Dirac gravity, but a magnetization curl coefficient cannot simply be counted as a separate gravitational charge. The gravity one-tag mass vs EM two-tag (m,q) dictionary of Sandbox v15.1088 remains an interpretation; spin moment does not derive q, G, spin metric action or quarter-grid coupling. A *new* Cone operator must be independently derived and produce a matched ordinary Dirac–Maxwell–Einstein+elastic-solid residual.

## Gate 928 — reproducibility, comparison and next test
Exact symbolic reproducer `research-notes/k4_gordon_spin_current_v15_1094.py`, additive commit 0b5d4d681bffeca47770462c9572d61144db3788. Locally executed before upload, PASS: divergence-free spin curl, Gaussian normalization and second moments, integrated mu_spin=q hbar/(2m), loop q hbar/(4m), factor-two. The calculation uses a formal real Gaussian of width L with the stated assumptions and is an exact nonrelativistic spin-current model, not a full quantum field propagator. Independent Audit pending.

**Positive:** the physically normalized spin current shows exactly how the full leading magnetic moment arises from Dirac structure without an extra classical action-loop current. **Negative:** Maxwell curl and action-circle numerology still do not select an extra coupling, free Compton radius, novel gravity response or G. **Next gate:** compare covariant Dirac tetrad/spin-connection stress-energy (and conserved Maxwell source) with the existing EH+K4 action, and ask whether any independently justified Cone/quarter-mesh term survives a matched baseline subtraction rather than assuming one.

**AUDIT HANDOFF:** verify sign and coefficient of Gordon/Pauli magnetization current, no-convection limit, Gaussian moment calculation, that g=2 is the total moment of the model rather than sum of two independent classical currents, that standard Dirac spin is not a literal Zitterbewegung trajectory, and that no spin-current-to-gravity source has yet been derived.
