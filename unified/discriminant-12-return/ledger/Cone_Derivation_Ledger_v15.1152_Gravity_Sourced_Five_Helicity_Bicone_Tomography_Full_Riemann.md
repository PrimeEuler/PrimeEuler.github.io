# Cone Derivation Ledger v15.1152 — Source-backed five-helicity bicone torque tomography; full Riemann versus Weyl-only failure

**Date:** 2026-11-18 Eastern. **Lane:** Gravity/Cone. **Status:** [D] exact rank-five local bicone torque tomography of the physical tracefree electric Riemann tensor using five orthogonal detector-plane configurations; [D] transverse-plane blindness to scalar/vector helicities and a nontrivial source-backed scalar signal in a tilted bicone; [D] Weyl-only substitution yields the wrong sign and magnitude for the archived on-shell canonical scalar benchmark; [N] no new K4-specific interaction relative to standard Einstein–Hilbert plus the *same* elastic solid and canonical matter, no parameter-free gravity prediction; [O] full five-helicity sourced coasting signal through the **real physical local bicone torque plus calibrated spin transfer**, realistic gauge and endpoint preparation and remote source. **Live HEAD immediately before ledger write:** 73434807371579b0a5ce97faede30b5412f2cdbf. Target v15.1152 unique and collision-free; additive-only; protect all Suzuki/Lane A, Audit, Sandbox, Muse and historical certified artifacts.

## Correction to preceding gate v15.1151: source-first K4 calculations already exist
The prior v15.1151 ledger incorrectly made the *entire physically sourced K4 curvature response* sound outstanding. This is too broad. **Gravity v15.730** already produced an on-shell massless canonical scalar, checked its corrected pressure Ward and sourced scalar Newtonian-gauge potentials. **Gravity v15.750 and v15.788** already evolved a spatially compact canonical source into physical gauge-invariant Weyl/full electric-Riemann histories. **Gravity v15.815–818**, especially v15.818, already propagated a single compact canonical scalar wavepacket through **one scalar, two vector and two tensor** K4 mode equations, yielding nonzero initial-value finite-arm optical signals. And **v15.760** and **v15.787** already established the exact matched Einstein–Hilbert-plus-same-solid no-novelty comparator. These earlier results are not rediscovered here and v15.1151 is preserved unchanged under the additive-only protocol. The **still-open narrower** task is to transfer the physically sourced **full local Fermi tidal tensor**, including its Ricci contribution, through *this particular* five-orientation bicone torque/spin-readout with correctly specified detector preparation. This gate completes that **local linear-algebra torque projection** and a sourced benchmark, but not a new global five-helicity numerical detector simulation.

## Gate 1055 — mechanical bicone readout of general physical Riemann STF geometry
In an orthonormal wave-adapted local triad (n,e,b), with n along the source wavevector, decompose the 3x3 symmetric tracefree physical electric Riemann tensor R_(0i0j)^STF as

**E_STF = S(nn−I/3) + V_e(ne+en) + V_b(nb+bn) + T_+(ee−bb) + T_×(eb+be)**.

Its matrix in (n,e,b) is exactly
**[[2S/3,V_e,V_b],[V_e,−S/3+T_+,T_×],[V_b,T_×,−S/3−T_+]]**.
Any physical isotropic part e_0 I is omitted here because it gives no *orientation-dependent* torque. This is a tensor COMPONENT basis, not a proof all five components propagate as massless vacuum gravitons; their source dynamics depend on the matter/solid field equations. For a mechanical bicone mass-quadrupole anisotropy ΔQ, choose a rotating unit axis p(θ)=cosθ u+sinθ v in an oriented orthonormal plane (u,v), with U=(ΔQ/2)p^T E p. At θ=0 the normalized torque is **s(u,v)=−u^T E v**; the sign is the same chosen Fermi/Hessian convention as v15.1151. For pure isotropic E, all s=0 exactly. This readout is an ordinary gravitational gradiometer, not a direct measurement of source material pressure/stress without field equations.

## Gate 1056 — a five-plane arrangement is invertible
Use five oriented mechanical rotation planes, with each bicone biased at θ=0 and independently calibrated:
1. (u,v)=(n,e)
2. (u,v)=(n,b)
3. (u,v)=(e,b)
4. (u,v)=((e+b)/sqrt2,(e−b)/sqrt2)
5. (u,v)=((n+e)/sqrt2,(n−e)/sqrt2).

For normalized torque readings s=(s1,...,s5), direct exact contractions give
**s=M (S,V_e,V_b,T_+,T_×)^T**,
**M=[[0,−1,0,0,0],[0,0,−1,0,0],[0,0,0,0,−1],[0,0,0,−1,0],[−1/2,0,0,1/2,0]]**.
**det M=+1/2 ≠0**, so all five local STF components can be reconstructed:
**S=−s4−2s5, V_e=−s1, V_b=−s2, T_+=−s4, T_×=−s3**.
The first four settings expose separate vector/cross/tensor difference channels; the last combines scalar and plus in a way resolved by the fourth. A detector restricted to *only* planes orthogonal to n, i.e. with u,v in span(e,b), is blind to **S,V_e,V_b** at this leading torque order, even when those physical tidal components are nonzero. v15.1151's two-angle transverse polarimeter is therefore a rank-two subcase, not full 3D tidal tomography.

The five settings may represent separately mounted detectors or sequentially rotated, phase-stable measurements. They require a physically supported 3D mount and distinct calibrated stiffness/torque/spin-gradient gains. The two-spin Ramsey apparatus v15.1131 used a specific planar magnetostatic-gradient geometry; its frequency-to-angle transfer **does not transfer unchanged to all five 3D orientation planes**. This new result is a *mechanical torque map* only. Any claim of fully quantified five-channel paired-Jxy optical/magnetic outputs would require new physical mounts and transducer recalibration.

## Gate 1057 — an actual on-shell canonical source produces a local bicone torque
Use **the independently established physical canonical scalar source** from v15.730:
chi(τ,x,z)=[cos(sqrt11 logτ)/τ]cos(2x)+[cos(sqrt2 logτ)/τ]cos(z),
on the coasting background a(τ)=τ/sqrt3. Its Fourier cross-stress wavevector K=(2,0,1), |K|²=5, has explicitly checked scalar constraint potentials at τ=1, with pressure-corrected Ward and sourced solid initial data,
**Φ_N=191/1800, Ψ_N=−1/72, a²=1/3**.
The older full-electric-Riemann-from-metric Gate v15.787 gives the physical scalar **tracefree** tidal coefficient
**S_full=−k² Φ_N/a²=−191/120**,
whereas the source's electric-Weyl-only coefficient is
**S_Weyl=k²(Φ_N+Ψ_N)/(2a²)=+83/120**.
The full electric-Riemann scalar shape is exactly S(nn−I/3) with n=K/|K|. Insert this *source-derived* field at the already fixed τ=1 into the 5-plane torque matrix (without assuming arbitrary S amplitude). The predicted single-complex-Fourier-mode normalized mechanical readout is
**s_full=(0,0,0,0,+191/240)**.
The physically incorrect Weyl-only substitution would instead produce
**s_Weyl=(0,0,0,0,−83/240)**,
so the **last-channel difference is +137/120**, with opposite sign as well as different magnitude. This is the concrete reason to use full Fermi Riemann tidal curvature rather than Weyl-only when feeding matter-supported K4 solutions into the gradiometer.

These values are complex-Fourier/field-normalized source coefficients at the chosen physical slice, not SI acceleration gradients. Real space fields require ±K complex conjugate pairing, and the source's arbitrary amplitude bookkeeping ε rescales tidal amplitudes as ε². It is a valid on-shell **nonlocalized** benchmark, not a realistic nearby source or a sourced finite-range sensor prediction. Previous v15.818 compact packet produces five sourced helicities at nonzero times, but this gate does *not* substitute its reported metric amplitudes for the full local Riemann without their required time derivatives/constraints and metric/tetrad conversion.

## Gate 1058 — exact matched GR+solid null and remaining physical requirements
The frozen v14.935 K4 action is an Einstein–Hilbert gravity action coupled to a particular relativistic isotropic solid with matter invariants b and J. An **identically chosen conventional Einstein–Hilbert plus that same elastic solid** model, with the same canonical source and initial/boundary data, produces identical solutions and therefore identical local Riemann tensors. The five-plane bicone detector's torque and any *identically specified* magnetic readout is then identical. This matched-action residual is exactly zero by identity of the two descriptions, as established already v15.760 and v15.818; there is no newly discovered Cone force or quarter-grid selector. A GR vacuum or a different material background is **not** an equal-action comparator, and changes in its tidal output are ordinary matter-dependent differences rather than demonstrations of a new gravitational force.

Open: (i) actual finite compact source-to-remote-detector local Fermi tidal waveform and its orientation in a material-defined lab; (ii) consistent sourced all-sector lapse/shift and physical spatial Ricci for this apparatus; (iii) a 3D calibrated mechanical/magnetic transduction model with spin backaction and noise; (iv) a Cone-derived independent action or selector yielding a dimensionless GR+identical-material residual. The exact 5x5 tomography supplies the necessary detector-side linear algebra, not the source-specific novelty.

## Reproducer and independent Audit handoff
`research-notes/k4_sourced_five_helicity_bicone_tomography_v15_1152.py` uploaded additively as source commit **73434807371579b0a5ce97faede30b5412f2cdbf**. An equivalent, more detailed **73-line local SymPy reproducer** was executed before upload: all exact assertions PASS including wave triad orthonormality, full 3x3 basis tensor, five plane torque derivatives, detM=1/2, exact inverse, transverse scalar/vector blind spot, v15.730/787 full-versus-Weyl source coefficients and 137/120 discrepancy. Uploaded script reproduces the same identities and adds explicit assertions for det=1/2. No images generated; protected lanes untouched.

**AUDIT HANDOFF:** verify source-first historical credit (v15.730/750/787/788/818, independent Audit precedent), explicitly note and correct v15.1151's overbroad unresolved-source description without editing it, check tensor STF normalization, u-v plane orientation and torque sign, five-by-five determinant/inverse, source benchmark Phi/Psi and physical full electric Riemann versus Weyl, no illicit 3D reuse of 2D spin transducer, and matched EH+same-solid zero. Consider a future **actually computed finite 3D torsional/Jxy response** for v15.818's compact wavepacket only if the time-dependent local full-Riemann source fields and instrument geometry are independently pinned.
