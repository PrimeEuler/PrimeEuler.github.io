# Cone Derivation Ledger v15.878 — Gravity: conventional Gertsenshtein EM–gravity wave mixing; polarization, conversion unitarity, and EM-half/G-quarter selector null

**Date:** 2026-11-13 US Eastern. **Parent inputs:** original K4 EH+relativistic solid v14.935; exact five-helicity photon/mirror/clock detector v15.815–818; force/half-quarter/phase/pump sequence v15.857–876; Muse/Sandbox node and transition-parabola v15.866–869; External Audit Round 567/v15.877 (independently confirmed v15.870–876 and Sandbox v15.869). **Prewrite live HEAD:** 07cfff9e72f58104e34b87a3beca2d31593c979f. Target file absent; additive-only, no edits to audited/Suzuki/Sandbox payloads.

**Classification:** [D] conventional Maxwell stress crossed with an external static transverse magnetic field; [D] polarization-resolved Hermitian 4-channel photon–graviton WKB propagation and exact homogeneous probability; [N] magnetic orientation / incoming phase leaves the *total* homogeneous field conversion probability invariant when both photon dispersion channels are equal; [N] h_EM=1, q_EM=1/2 and h_G=1/2, q_G=1/4 do **not** independently determine conversion length, phase or mixing; [O] K4+Maxwell covariant constrained initial-value derivation, real field source, physical medium profiles, unique novel Cone operator and unambiguous experimental residual.

## Gate 513 — real Einstein–Maxwell coupling as the comparator

Unlike v15.875's freely chosen EM–elastic oscillator coupling, **ordinary Einstein–Maxwell theory** already contains a photon–graviton interaction in an external electromagnetic field through the Maxwell action

**S_EM = −(1/4)∫√(−g) F_μν F^μν d⁴x**.

Expand F=F^(0)+f and g=g^(0)+h. The term linear in h and f about a nonzero electromagnetic background F^(0) is the Gertsenshtein mixing source. In the usual weak-field external-background approximation, a uniform transverse static B field may be treated as prescribed while gravitational backreaction and its supporting current are neglected. This is **not** an exact self-gravitating uniform-magnetic-field spacetime, and K4's nonzero background solid adds further scalar/vector constraints not included in this comparator.

For propagation +z, let transverse background **B=(B_x,B_y,0)** and propagating radiation **E=(E_x,E_y,0)**. Faraday relation gives the radiation magnetic fluctuation **b_wave = zhat×E=(−E_y,E_x,0)** in c=1 units. The anisotropic cross term of the ordinary Maxwell spatial stress is

**δT_ij = −(B_i b_j+b_i B_j)+δij (B·b)**.

Its two gravitational TT driving polarizations are exactly

**δT_+ ≡ (δT_xx−δT_yy)/2 = B_x E_y+B_y E_x**,

**δT_× ≡ δT_xy = −B_x E_x+B_y E_y**.

This directly checks the polarization selection: at B_y=0, **h_+ ↔ A_y** and **h_× ↔ A_x** (cross channel may carry a conventional minus sign). A scalar EM Casimir value or quarter mesh does not appear in the Maxwell stress. The calculation is a first-order stress expansion, not a claim that all K4 Maxwell constraints have been solved.

## Gate 514 — exact coupled WKB photon/graviton mixing and conversion probability

Let photon amplitudes be (A_x,A_y) and graviton amplitudes (h_+,h_×) with canonical flux normalization. A standard lossless, homogeneous, weak-background-field WKB mixing model is

**i dΨ/dz = H Ψ**, **Ψ=(A_x,A_y,h_+,h_×)**,

**H = [[Δ I_2, C],[C^T,0]]**,

**C = μ [[sin θ,−cos θ],[cos θ,sin θ]]**,

with external transverse magnetic field angle θ, real mixing μ proportional to the **physical** transverse magnetic field and square root of the Einstein gravitational coupling in the convention selected, and real photon–graviton refractive mismatch Δ (from plasma, QED dispersion or other physical propagation corrections). The 4×4 Hamiltonian is manifestly Hermitian and conserves |Ψ|², so a graviton-to-photon transition exchanges normalized wave energy without free creation. This 4-channel matrix is the ordinary, analytically tractable comparator; it does NOT derive the exact K4+Maxwell coupled SVT response or give an independent prediction for μ.

The geometric coupling matrix satisfies **C^T C=μ² I_2** for every θ. Therefore both polarization branches have the same exact homogeneous conversion probability

**P_(g→γ) = [4 μ²/(Δ²+4μ²)] sin²[(L/2)√(Δ²+4μ²)]**,

under the stated *equal photon dispersion* assumption. At Δ=0 the conversion becomes **sin²(μL)**. At small μ and finite Δ it reduces to **(μL)² sinc²(Δ L/2)**, where sinc(x)=sin(x)/x. These formulas agree with standard Gertsenshtein weak-mixing and medium-mismatch literature, notably PRL 132,131402 (2024), PRD 110,083042 (2024), and later full polarization discussions. Magnetic orientation affects **which polarization** receives the converted wave, but not total P in this ideal equal-dispersion, uniform-field limit.

**Test-only, arbitrary dimensionless parameters:** μ=0.083, Δ=0.14, L=14 produce **P≈0.5828565490569763**. These numbers do not stand for physical tesla/metres, don't estimate laboratory conversion and are **not** generated by the Cone 1/4 grid.

## Gate 515 — half/quarter phase is a label until dynamically locked

Muse/Sandbox's EM half-step and G quarter-step define valid *sector-relative* phase dictionaries, not a physical law enforcing coherent photon–graviton relative phase or adjusting B_T. In the uniform equal-dispersion model, rotate the incoming pure graviton polarization by any phase θ_p or assign phases 0, π/4, π/2 to the two graviton components. The total outgoing photon probability is identical for the same normalized incoming graviton because both polarizations share the same singular mixing strength μ: **P=scalar × (|h_+|²+|h_×|²)**. One can change which photon polarization is produced or the outgoing Stokes parameters without creating a new total conversion enhancement.

Distinguish a *global* phase (completely unobservable in single pure-state conversion intensity) from a *relative* phase (observable through the photon polarization/Stokes parameters); neither supplies a coupling enhancement in the ideal uniform equal-dispersion case. If the physical medium is birefringent, the magnetic field rotates along the path, or photon/graviton birefringence differs by polarization, this symmetry need not persist, and ordinary phase-dependent conversion can occur **without** any Cone-specific effect. The exact mesoscopic EM/G mesh phase correlation would still need a physical phase-locking operator from the action, not be input as a number.

## Gate 516 — numerical controls and independent verification

The reproducer performs the following checks with exact SymPy and standard NumPy/SciPy:

1. Derive both Maxwell mixed TT stress components directly, including signs.
2. Verify C^T C=μ² I for symbolic magnetic-field orientation.
3. Compare **4×4 unitary matrix exponentiation** for four B orientations, three graviton input polarization angles and three photon detunings against the exact analytic P, with absolute errors below 2×10^-14 and wave-norm conservation.
4. Test coherent relative phases of the incoming graviton doublet against the identical total P.
5. Verify perfect conversion is mathematically possible at Δ=0, L=π/(2μ) in this toy normalized two-state model; verify weak-mixing sinc expansion at finite Δ.
6. Evolve a **spatially variable** 4×4 Hermitian magnetic/mismatch model by numerical ordered integration, checking norm conservation below 2×10^-10. This is a path-dependent ordinary scattering/oscillation calculation, not an exact magnetosphere model or a new phase-locking law.

**Original script:** research-notes/k4_einstein_maxwell_gertsenshtein_v15_877.py, additive commit **1d70433c77d025d47ba283c22b37677bd584f6a3**. An equivalent local Python reproducer executed PASS for all headline checks; the committed bytes and specific new wrapper remain to be independently reexecuted. A version-label overlap occurred because **External Audit Round 567 independently claimed ledger v15.877** (commit 2e2d48ae75de...) immediately before Gravity's Gertsenshtein script was committed under a v15.877 filename. No files were overwritten. Unique additive Gravity **v15.878 replay** script research-notes/k4_gertsenshtein_v15_878_replay.py, commit **07cfff9e72f58104e34b87a3beca2d31593c979f**, runs the original script by adjacent path and reserves **Gravity v15.878** as the unique authoritative ledger label. Both original historical files preserved unchanged.

## Gate 517 — novelty verdict and next physically relevant directions

**Positive:** we now have an actual Einstein–Maxwell EM↔G transfer baseline with derived Maxwell polarization selection, Hermitian energy-conserving mixing, physical dependence on B_T, L and Δ, and analytically exact input-phase and medium controls. Unlike our freely inserted parametric oscillator λ, the structure of this interaction is part of known generally covariant field theory.

**Negative:** none of the Cone quarter/half mesh values selects B_T, Δ, magnetic-field path, L, polarization coherence, physical graviton/EM frequency, or a new coupling. There is no Cone-only conversion effect in the Einstein–Maxwell action; adding the already frozen K4 standard EH+solid dynamics does not by itself create a different gravitational action from conventional GR+the same solid. No proposal that this effect replaces quantum hydrogen stability is warranted.

**NEXT:** if we want a genuine Cone novelty test, identify an **independently justified new gauge/diffeomorphism-invariant interaction operator** generated by the Cone half/quarter mesh, derive a dimensionless new phase/coefficient without inserting empirical G, and show it changes a polarization-resolved conversion observable after subtraction of standard Einstein–Maxwell+elastic-solid birefringence, magnetic geometry and plasma/QED propagation. A fully sourced Einstein–Maxwell+K4 magnetic-region initial-value simulation with Maxwell stress, supporting currents, solid response and finite-distance observer is a separate costly comparator gate.

**External audit handoff:** reexecute original committed v15.877 producer and v15.878 replay; scrutinize cross-stress sign convention, polarization mixing matrix, its normalization, the idealized equal-dispersion assumption, static magnetic-field stress/backreaction omission, 2×2 analytic P and 4×4 numeric unitarity, and the explicitly negative Cone selector result. Never silently edit the prior v15.877 Audit Round 567 or Gravity's v15.877 script.
