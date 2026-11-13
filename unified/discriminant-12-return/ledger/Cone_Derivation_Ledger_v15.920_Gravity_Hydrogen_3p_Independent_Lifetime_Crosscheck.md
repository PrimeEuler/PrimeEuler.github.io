# Cone Derivation Ledger v15.920 — Independent measured hydrogen 3p lifetime from 2p calibration

**Date:** 2026-11-13 US Eastern. **Track:** Gravity/EM lifetime bridge. **Parents:** Gravity v15.919 radiative obstruction and conditional lifetime-ratio framework; staged `arxiv/note-bicone-dipole-alpha/Note_BiconeDipole_FineStructure_v1.0.tex`; `arxiv/note-bicone-dipole-alpha/HANDOFF_MultipleBicones_HydrogenicGeneralization.md`; classical Coulomb/SO(4,2) dipole theory. **Live master HEAD immediately prewrite:** 417020b6a8557e907c69da7d3b108677ce2dcb65. Target confirmed absent. Additive-only; Audit, Suzuki, Sandbox and protected results unchanged.

**New source finding:** E. L. Chupp, L. W. Dotchin, and D. J. Pegg, *Radiative Mean-Life Measurements of Some Atomic-Hydrogen Excited States Using Beam-Foil Excitation*, Phys. Rev. **175**, 44 (1968), DOI **10.1103/PhysRev.175.44**, independently report **H(2p)=(1.60±0.01) ns** and **H(3p)=(5.5±0.2) ns**. Source accessible through https://journals.aps.org/pr/abstract/10.1103/PhysRev.175.44 (publisher abstract explicitly labels 2p and 3p). This supplies a distinct measured n=3 line, not just another Z-scaled 2p ion. The earlier staged bicone handoff reported missing independently measured 3s/3d lifetimes; that does not exclude this experimentally measured 3p state. The 1973 Tielert 2p value 1.592±0.025 ns is separately available but **do not mix 1973 2p and 1968 3p errors as if correlated**. This test deliberately uses both lifetimes from the same 1968 experiment.

**Status:** [D] exact standard Coulomb radial E1 matrix elements, frequency and lifetime ratios; [N] independent measured lifetime agrees within approximately 1.07 combined standard deviations; [N] this tests standard Coulomb/SO(4,2), not a novel Cone-only operator; [O] actual derivation of these cross-shell E1 factors from the (n+k)/(n−k) secant transition rule without importing Schrödinger radial wavefunctions.

## Gate 637 — distinct measured 3p decay total, not one branch

Hydrogen H(3p) decays via two E1 channels, **3p→1s** and **3p→2s**, neglecting much weaker non-E1 corrections. Therefore **tau(3p)^{-1}=A_31+A_32**; using only A_31 would mispredict the lifetime. H(2p) has one dominant E1 channel **2p→1s**, so A_21≈1/tau(2p). These lifetimes are directly experimental, not taken from NIST-calculated A values.

The nonrelativistic Coulomb radial integrals in units of a0, using individually normalized hydrogen radial functions, are exactly:

**R21=∫ R10(r)r R21(r)r²dr /a0 =128 sqrt6/243**;
**R31=∫ R10(r)r R31(r)r²dr /a0 =27 sqrt6/128**;
**R32=∫ R20(r)r R31(r)r²dr /a0 =27648 sqrt3/15625**.

The same p→s angular E1 factor applies to all three branches (after averaging/summing magnetic substates). For hydrogen E_n=−Ry/n², angular frequency ratios are **ω31/ω21=32/27**, **ω32/ω21=5/27**. Standard E1 rate scales as **ω³|R|²**. Consequently the exact dimensionless individual rates relative to the 2p→1s reference are

**A_31/A_21=(32/27)³(R31/R21)²=2187/8192=0.2669677734375**,

**A_32/A_21=(5/27)³(R32/R21)²=69984/1953125=0.035831808**.

The predicted **total** ratio is **(A_31+A_32)/A_21=4844793303/16000000000=0.3027995814375**, with branching fractions approximately 0.8816649355 and 0.1183350645. This ratio eliminates charge, Bohr radius, epsilon0, absolute line normalization and a shared detector scale. It is a **conventional hydrogen SO(4,2)/Coulomb identity**; it has not been derived independently from the fixed-D `J_+` secant-geometry operator.

## Gate 638 — one-line calibration, independent second lifetime

Take measured tau_21=(1.60±0.01) ns from Chupp et al. (1968) as the ONE lifetime calibration. Predict

**tau_3p,pred = tau_21 / 0.3027995814375 = (5.284023156 ±0.033025145) ns** (uncertainty propagated solely from measured tau_21; theoretical higher-order atomic/QED corrections excluded in this nonrelativistic benchmark).

Compare to independently measured **tau_3p=(5.5±0.2) ns**. Residual **(5.5−5.2840)/sqrt(0.2²+0.0330²)=1.06545627 σ**, assuming independent errors. Both lifetimes came from the same beam-foil study, so fully rigorous statistical significance would require their cross-covariance, not provided in the abstract; the quoted pull is the *uncorrelated-error approximation*. The prediction is within stated measurement uncertainty and strongly avoids the circular strategy of testing a theoretical dipole against a theoretical tabulated Einstein A.

This is a legitimate positive **empirical scale-transfer benchmark**: a single experimentally measured lifetime calibrates the common EM rate, and exact quantum matrix-element ratios predict a second measured lifetime. It is not a new independent determination of G, the electron's physical velocity X, or a novel alpha or gravity theory.

## Gate 639 — sharp separation from the secant J+ hypothesis

The v15.906 fixed-sum factor ladder **(n,k)→(n+1,k−1)** has operator coefficient sqrt(nk), yet total oscillator occupation and isotropic oscillator energy do not change, so it alone does NOT radiate an E1 photon. The physical H(2p) and H(3p) lifetime channels change Coulomb principal quantum number and use **SO(4,2) cross-shell electric dipoles**, including radial physics. Specifically, the ratio 0.3027995814 comes from three unequal radial integrals and frequency-cubed factors: there is no proof that any uncorrected rule A∝nk maps all three branches. If one simply sets dipole magnitude squared∝nk and ignores cross-shell SO(4,2) factors, no justified physical state-to-factor assignment or emission rule is present; do not claim a derived lifetime.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_hydrogen_3p_lifetime_crosscheck_v15_920.py`, additive commit **417020b6a8557e907c69da7d3b108677ce2dcb65**. Locally executed against SymPy's exact normalized Coulomb `R_nl` functions: PASS for all three radial integrals, exact rate fractions, both branch fractions, measured-versus-predicted discrepancy. Independent external Audit pending.

## Next physically discriminating gate

1. Derive physically normalized **cross-shell** electric-dipole operators in the project's native parabolic/bicone (n,k) variables, including the KS measure and SO(4,2) sector change, for **2p→1s, 3p→1s and 3p→2s**. Compare term-by-term with the exact radial coefficients here. A unique new coefficient must survive this conventional-control comparison rather than be a relabeling.
2. Validate state identification and experiment's measured transition branching separately from total lifetimes, including polarization and cascade effects. Obtain covariance or separate independent lifetime measurement if claiming precision beyond the approximate 1.07σ test.
3. Only after the physical dipole map is complete, ask if independently measured linewidth sets an SI time scale for the Cone's **m/s-labelled** X nodes. It will fix an EM decay time for a particular atomic transition, but does not on its own establish particle acceleration or select an EM→gravity universal frequency.

**HANDOFF Audit/Muse:** independent checks of 3p two-branch total; exact 2187/8192 and 69984/1953125 rates, Chupp 1968 independent experimental provenance, the experimental covariance caveat, and most importantly the absence of an independently derived (n+k)/(n−k) to cross-shell E1 mapping. Existing Audit round 573 completed v15.916 fixes; no file collision introduced.
