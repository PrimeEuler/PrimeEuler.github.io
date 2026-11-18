# Cone Derivation Ledger v15.1126 — Larmor spin cones as transverse Jxy observables, paired bicone correlations and exact relative-phase oscillation

**Date:** 2026-11-17 Eastern. **Lane:** Gravity/Cone. **Status:** [D/R] the established Larmor spin-cone orientation is represented quantum-mechanically through transverse spin quadratics Jxy²=Jx²+Jy²=J²−Jz², already mapped to the cone's half-step parabola midpoints in v15.955; [D] a single j=1/2 cone has constant Jxy²=1/2 I and cannot read its own orientation/aperture through that quadratic; [D] the doubled spin-half bicone has complementary diagonal and relative transverse quadratics, distinguishes singlet and triplet m=0, and under an *independently given* differential Larmor drive exchanges their expectations with a cosine law; [N] no physical spin-cone / causal-circle identification, Hamiltonian frequency, odd-quarter SU2 realization or new G-free gravitational observable follows. **Immediately prewrite live HEAD:** 0149f1fa655035a5c06391dc838e623824110b09. v15.1126 collision-free; additive-only, protected Suzuki, Audit, Sandbox, Muse and certified foundation history untouched.

## Parents and explicit redundancy check
The user's assertion 'the Larmor cones are the Jxy Casimir observables' is interpreted as identifying the cone's transverse angular spread with a **quadratic transverse spin observable**; do not confuse this with claiming an additional independent *central* SU(2) Casimir. The original `research-notes/Jx_Jy_V4_Quarter_Shift_Findings.md` and `Magnetic_Driver_Transverse_J_Casimir_Contact_Correction.md` already distinguish one-edge J± coefficient from the two-edge moment. Gravity v15.955 explicitly proved the D state-center half-row identity `Jxy²=diag[f_D(k+1/2)−1/4]=J²−Jz²` on ordinary Schwinger SU(2) state carriers, with `f_D(K)=K(D−K)`. Gravity v14.863 already proposed **conditional orientation locking** of the reflected AM–GM circle directions to two equal-length classical Larmor vectors and posited an independent exchange Hamiltonian. Gravity v15.1123–1124 supplies the two causal-cone shared-circle U(1) gluing caveat and a correctly sourced double spin-half **relative Zeeman** singlet-triplet mixing formula. Gravity v15.1125 tested mirror-half-parabola Schwinger transition weights and demonstrated arbitrary edge phases are basis gauge on a chain, not a physical connector. The present gate is the new **two-spin quadratic observable** comparator and its exact evolution, not a reannouncement of Jxy² identity. Latest independently completed external Audit observed Round 597/v15.1119; v15.1121–1126 not yet independently audited.

## Gate 1026 — classical spin-orientation cone versus quantum Jxy quadratic
For classical precessing J of fixed norm j and tilt θ about the physical precession/quantization axis z, its transverse squared length is `Jx²+Jy²=j² sin²θ`, while the longitudinal component is `j cosθ`. But in a *quantum* spin-j irrep (with dimensionless J/ℏ),
**Jxy²=J²−Jz²**, and on a magnetic eigenstate `|j,m>`,
**<Jxy²>=j(j+1)−m²**.
For a spin-coherent state oriented at polar angle θ,
**<Jxy²>=j+j(j−1/2)sin²θ**,
because `<Jz²>=j²cos²θ+(j/2)sin²θ`. In particular for **j=1/2**, **Jxy²=I/2 for every state and every θ**; a single spin-half Larmor cone has NO aperture information in this one quadratic, even though its first moments <Jx>,<Jy>,<Jz> depend on θ when a spin-coherent pure state is prepared. A singlet has vanishing first moments of either constituent and cannot be depicted literally as two definite spin arrows without state-preparation/coherent-state assumptions. Jxy² commutes with Jz (and J²), but is **not a second independent full-SU(2) central Casimir**. The old geometry-to-operator dictionary remains valid, but a physical measurement still needs a field/probe coupling to this quadratic.

## Gate 1027 — paired diagonal and relative transverse observables supply nontrivial information
On the old four-state bicone H=C²⊗C² set `J_Ai=σ_i⊗I/2`, `J_Bi=I⊗σ_i/2`, `L_i=J_Ai+J_Bi` and `D_i=J_Ai−J_Bi`. Then
**Lxy²=Lx²+Ly²=I+2(J_Ax J_Bx+J_Ay J_By)**,
**Dxy²=Dx²+Dy²=I−2(J_Ax J_Bx+J_Ay J_By)**,
and **Lxy²+Dxy²=2I** identically. In the canonical |++>,|+−>,|−+>,|−−> basis,
`Lxy²=[[1,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,1]]`,
`Dxy²=[[1,0,0,0],[0,1,-1,0],[0,-1,1,0],[0,0,0,1]]`.
For singlet |S>=(|+−>−|−+>)/sqrt2 and triplet |T0>=(|+−>+|−+>)/sqrt2:
**(Lxy²,Dxy²)|S>=(0,2)|S>**, **(Lxy²,Dxy²)|T0>=(2,0)|T0>**.
Thus a **paired** transverse correlation can sharply distinguish singlet/triplet channels despite each local spin-half Jxy² being constant. This is an ordinary two-spin correlation algebra, not proof that the two causal cone surfaces carry an automatic quantum spin system.

## Gate 1028 — relative Larmor cone phase creates a calculable transverse oscillation
With an independently specified physical relative Zeeman/Larmor Hamiltonian `H_rel=−(ΔΩ/2)D_z`, ℏ=1 and ΔΩ=Ω_A−Ω_B, Gravity v15.1124 derived
`|ψ(t)>=cos(ΔΩt/2)|S>+i sin(ΔΩt/2)|T0>`.
Because the two transverse quadratics are diagonal in `|S>,|T0>`,
**<Lxy²>(t)=2 sin²(ΔΩt/2)=1−cos(ΔΩt)**,
**<Dxy²>(t)=2 cos²(ΔΩt/2)=1+cos(ΔΩt)**,
and their sum is exactly 2. This exact complementary oscillation provides a potential *measurable* correlation signal for an actual double-spin apparatus with state preparation and operator readout. It is NOT a novel gravitational prediction, and its frequency ΔΩ must be sourced by real magnetic/Zeeman couplings or an independently derived interaction. A geometric parameter along the common causal circle is not automatically physical spin-precession time. If ΔΩ=0, an initially prepared singlet stays a singlet and the transverse moments remain (0,2). The **single-spin-half transverse quadratic alone cannot reveal the oscillation**: it is the two-spin correlation/cross term that does so.

## Gate 1029 — three-cone interpretation, physical gaps and Audit
The owner's proposed three-cone dictionary may now be stated precisely:
- two physically distinct causal light-front cones give an intersection circle/boosted ellipse determined by event endpoints (Gravity v15.1121–22);
- two independently specified SU(2) spinor sectors forming the bicone can be prepared and measured along that shared geometric interface, with operator magnitudes encoded by half-step parabolas (old v15.952/v15.955 and Gravity v15.1125);
- a Larmor precession cone supplies spin orientation and—once an external magnetic Hamiltonian and time correlation are specified—an evolving relative phase, which is directly detected by **paired** `Lxy²` and `Dxy²`.

**Positive:** the Larmor cones have exact transverse operator correlators that align with the previously identified Jxy parabola-midpoint observables and offer a sharp singlet-triplet discriminator. **Negative:** individual j=1/2 transverse quadratics are scalar multiples of identity, and the 3D causal geometry does not supply their correlational Hamiltonian, readout or a selected scale. The EM half-step (1/4) completion remains separate from the gravity-only quarter-mesh formal Casimir; no odd-quarter SU2 obstruction is resolved.

Canonical reproducer `research-notes/k4_larmor_cones_jxy_pair_observables_v15_1126.py`, additive commit **0149f1fa655035a5c06391dc838e623824110b09**. Full equivalent local SymPy calculation **executed** and PASS: Pauli/Schwinger matrices, singlet/triplet spectra, Lxy²+Dxy²=2I, relative-phase expectations, and spin-coherent quantum correction. Independent committed-byte Audit pending.

**AUDIT HANDOFF:** verify local spin-half aperture null despite classical cone intuition, `j+j(j−1/2)sin²θ` coherent-state result, complementary matrices/selection on |S>,|T0>, relative Zeeman sign and oscillation, correctly identified Jxy² not full central SU2 Casimir, and sourced-observable vs visual circle distinction. **NEXT:** calculate the response of `Lxy²−Dxy²` under a physically specified magnetic and tidal coupling, compare a standard two-spin ESR/NMR experiment to the matched Cone causal-circle geometry, and demand a new phase or dimensionless coefficient fixed without feeding observed G/frequency. A standard correlation oscillation alone is not new gravity.
