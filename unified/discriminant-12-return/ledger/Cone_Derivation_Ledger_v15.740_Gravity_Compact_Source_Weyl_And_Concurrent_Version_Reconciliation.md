# Cone Derivation Ledger v15.740 — Gravity: compact canonical matter creates scalar Weyl; explicit concurrent-version reconciliation

**Date:** 2026-11-11 US Eastern. **Parents:** v15.727 canonical positive-local-energy spectator scalar, v15.728 traceful scalar-source Ward correction, v15.729 pressure-corrected gauge-invariant source-to-Weyl transfer, v15.730 exact but spatially nonlocalized two-wave on-shell source, v15.731 spatially compact S/V/T Fourier stress and spherical null, and the additive numerical compact-Weyl reproducer introduced in the historical gravity file labeled v15.732. **Status:** [D] finite-energy compact canonical scalar Cauchy data sourcing nonzero initial-slice gauge-invariant K4 electric Weyl, converging as packet radius grows to the exact v15.730 benchmark; [N] source-independent new gravity constant, universally observed triple sector peaks, or a fully retarded detector response; [O] temporal wavepacket propagation and full T/V source-to-curvature channels. **Prewrite live HEAD:** 362d59ffb0d092ca499d2b8fd0cb38135bd63f98. Strictly additive; Suzuki/far-tail frozen objects untouched.

## CONCURRENT VERSION INCIDENT — transparent, additive repair

During the gravity v15.732 research-notes upload, Suzuki independently wrote the R7 unweighted baseline under **v15.732**: Lane A script commits **2ecfadc13abfcc4c54fa09ed597050bddc86c028** and **c249c0a312001044184dd33f723ac434d13ace9a** were already on live HEAD when gravity file **e8e1a7b1f0ab7925cd36a25903c9f1367538bba9** landed. The paths differed, nothing was overwritten, but the version label was duplicated. Lane A acknowledged the collision in its **v15.733** ledger commit **9f75e19cdd877568851d4cdc20c5e6baac3fb4ca**. Gravity also wrote a purely additive **v15.733** replay wrapper (commit **362d59ffb0d092ca499d2b8fd0cb38135bd63f98**) that executes the original gravity v15.732 script, creating another shared version label without a path overwrite. The original gravity v15.732 and Suzuki v15.732/v15.733 artifacts are preserved as historical evidence.

**Repair protocol:** this uniquely named **v15.740 Gravity ledger** records the precise two concurrent collisions and adopts a separated version number to avoid the active Suzuki immediate next-version range. No prior content or SHA was rewritten, silently renamed, or deleted. Audit should treat the original gravity Python script as a *historical, misnumbered but reproducible artifact* referenced by this v15.740 ledger rather than as a claim to ownership of Suzuki v15.732 or v15.733.

## Gate 371 — actual compact canonical Cauchy stress, not freely prescribed signed Fourier matter

On the coasting K4 metric **a(tau)=tau/sqrt(3)**, at the source initial slice tau0=1, use canonical massless scalar initial data

**chi0(x,y,z)=w_R(x,y,z)[cos(2x)+cos(z)]**,

**chi_dot0=-chi0**,

with spatially compact globally C7 cutoff

**w_R= product_{u=x,y,z} h(u/R)**, **h(s)=(1-s²)^8 for |s|<1**, zero outside.

These specify finite-energy real KG Cauchy data from the ordinary positive-energy matter action v15.727, not the signed globally time-compact stress of v15.724–725. In particular, local energy density **rho=(chi_dot²+|grad chi|²/a²)/2≥0**. The KG equation at tau=1 fixes **chi_ddot=3chi+3Delta chi**, and its spatial gradient fixes the *time derivative of the momentum source*. The cutoff and all its first/second spatial derivatives are explicitly retained when calculating source Fourier coefficients at **K=(2,0,1)**, K²=5.

## Gate 372 — correctly normalized complete physical source Fourier coefficients

Fourier-integrate the actual canonical stress on the initial Cauchy slice using the conjugate coefficient exp[-i(2x+z)] and normalize by the effective squared-cutoff volume **I0=∫w_R² d³x**. This normalization is for comparison across packet sizes; absolute physical Fourier stress scales with I0 and with squared field amplitude. For the original K4 +--- scalar ADM conventions take

**J_Phi=a³ rho_K**,

**J_psi=a³ P_trace,K**,

**J_B=i a⁴ K_i T^(0i)_K**,

**J_B_dot= d/dtau [i a⁴ K_i T^(0i)_K]**.

The source energy, isotropic pressure, momentum, and the momentum's time derivative are all derived from the **same canonical KG field**. In particular at tau=1 with f=chi0, a=1/sqrt(3), chi_dot=-f and chi_ddot=3f+3Delta f, the script uses

**J_B=i a² Fourier_K[f (K.grad f)]**,

**J_B_dot= -i a² Fourier_K[(2f+3Delta f)(K.grad f)]**.

This is crucial: setting J_psi=0 or neglecting the envelope gradients would incorrectly transplant the old tracefree source equations onto physical matter.

## Gate 373 — nonzero gauge-invariant initial-slice scalar Weyl and finite-size comparison

Choose K4 **eta=3/4**, k²=5 and the constraint-compatible initial solid displacement **P(1)=P_dot(1)=0**. The pressure-corrected source-first scalar P equation v15.728 gives its initial acceleration; lapse and longitudinal shift are determined by the original constraint matrix, not set to zero.

The original scalar Bardeen potentials are reconstructed with the **complete traceful** v15.729 source-to-metric transfer, and their conformally invariant electric Weyl STF coefficient is

**W_R(1)=K²[Phi_N(1)+Psi_N(1)]/[2a(1)²]**,

**E_ij^Weyl=W_R(Khat_i Khat_j-delta_ij/3)**.

Independent numerical 3D Gauss–Legendre quadrature of the spatially compact stress gives (Fourier coefficients divided by I0):

| R | Quadrature nodes per axis | P_ddot(1) | W_R(1) |
| --- | ---: | ---: | ---: |
| 16 | 96 | ≈0.360000000 | ≈0.7238932648 |
| 32 | 144 | ≈0.360000000 | ≈0.6997233073 |
| Infinite plane-wave normalized limit, v15.730 | — | exactly 9/25 | exactly 83/120≈0.6916666667 |

The finite-window Weyl amplitude is nonzero. The difference from the analytic plane-wave control decreases from about **0.03222660** at R=16 to about **0.00805664** at R=32, approximately a factor of four, consistent with an O(1/R²) leading cutoff-gradient correction. The finite R values should **not** be silently replaced by the noncompact analytic 83/120. The local 2/3 STF identity still gives **E_ij E_ij=(2/3)W_R²** for this scalar Fourier mode, but does not fix the dynamical W_R.

## Gate 374 — scientific limitations and the originality gate

The field is physically defined and positive in local canonical energy, and its Cauchy data are spatially compact. This is a genuine step beyond the idealized signed Fourier source. Yet this result is **on the initial slice** with selected K4 scalar initial data, not a cosmological waveform propagated from a distant source to a detector. The stress is order epsilon² in the spectator field and the induced metric/solid perturbations are calculated at the corresponding leading order. The spatial Fourier normalization by I0 is not an absolute laboratory strain or Newton G calibration. The scalar source has generically nonzero vector/tensor *stress* projectors (v15.731), but their **physical curvature readouts** from this compact field remain open. The earlier K4 three-wave-speed ratio 3 remains conventional relativistic elasticity, not a new Cone mechanism; its measured observability remains conditional on real source and detector preparation.

**Reproducibility:** original source script **research-notes/k4_compact_canonical_weyl_convergence_v15_732.py**, commit **e8e1a7b1f0ab7925cd36a25903c9f1367538bba9**; additive identity-preserving replay **research-notes/k4_compact_canonical_weyl_collision_replay_v15_733.py**, commit **362d59ffb0d092ca499d2b8fd0cb38135bd63f98**. The scripts were tested locally to PASS at both packet radii and verify positive source energy, pressure-corrected scalar acceleration and nonzero gauge-invariant electric Weyl. All prior Suzuki artifacts and historical ledger entries remain unchanged.

**HANDOFF — external audit priority:** audit the race incident and preserve each concurrent SHA; reexecute original gravity v15.732 numerical script and its v15.733 wrapper; check Fourier stress/I0 normalization, all cutoff gradient/Laplacian terms, KG source time derivative of momentum, original K4 +--- sign conventions, source pressure Ward, P acceleration, Bardeen lapse/shift reconstruction and Weyl 2/3 norm. Verify the finite-size convergence without assuming exact plane-wave equality for finite R.

**NEXT:** solve for the **retarded time evolution** of the compact canonical scalar source, including its full traceful stress Fourier convolution, then source the K4 scalar/vector/tensor metric/solid constraints and compute gauge-invariant electric/magnetic curvature as functions of time and detector geometry. Compare explicitly to standard GR+relativistic elasticity and stop any claim that geometry alone fixes the interaction strength.
