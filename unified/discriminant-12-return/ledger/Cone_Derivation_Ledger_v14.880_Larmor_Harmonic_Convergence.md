# Cone Derivation Ledger v14.880 — Finite-Larmor harmonic convergence gate

Date 2026-10-25. Parents v14.872–879. Research note research-notes/Larmor_Harmonic_Gaussian_Truncation_Reproducer.md commit 1d0f0eeb54ecbc9daca2cc95aafa85743ad1680a. Live prewrite HEAD 1d0f0eeb54ecbc9daca2cc95aafa85743ad1680a. Additive only; protected Suzuki/far-tail not edited.

[D] Rotating Gaussian-source translation Fourier phase has Bessel harmonic amplitudes |b_n|²=J_n(k_perp R)². Define Gaussian-weighted W_n(β)=π^(-3/2)∫d³p exp(-p²)J_n(βp_perp)², β=R/a, and omitted harmonic weight T_N=1−W0−2Σ_{1≤n≤N}W_n. Σ_{all n}W_n=1. Evaluated with 70 generalized Gauss–Laguerre radial and 180 Gauss–Legendre angular nodes (reproducer in research note).

Numerical T_N for β=0.5: T2=7.30251571e-5, T4=1.418355583e-8, T8≈0; β=1: T2=0.003419007762, T4=1.040550889e-5, T8=1.315997311e-11; β=2: T2=0.07447503234, T4=0.003161856287, T8=9.136604132e-7, T12=5.023070848e-11.

[D/O] This confirms rapid cutoff convergence for Gaussian-weighted SOURCE harmonic phases at sampled β, not a numerical evaluation of the finite-rotation retarded Maxwell effective kernel. The full J_n velocity sidebands and shifted photon propagator denominators still need integration, and pole errors may be amplified near spectral thresholds. Thus the v14.874 frozen-orbit damped pole has NOT been continued to any nonzero Ω. Do not claim finite-Ω resonance or stability from source-weight convergence. Helical symmetry (v14.878) still makes scalar response frequency-diagonal in isotropic free space.

Flags: harmonic_Bessel_source_weight=DERIVED; Gaussian_harmonic_weight_convergence=NUMERIC_CHECKED; retarded_kernel_convergence=NOT_CHECKED; finite_rotation_pole=OPEN; Higgs_and_Newton_G=NOT_DERIVED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: sandbox
type: finite-larmor-retarded-Maxwell-pole
parent: v14.880
status: open
action: Implement full conserved J and rho harmonic source from v14.879, Gaussian regularized retarded transverse and electrostatic kernels; compute finite Ω poles for declared α=Ωa/c and β=R/a using harmonic-cutoff, radial/angular convergence, retarded-sheet checks, and independent residuals. Compare to v14.874 at α=0. No claims without convergence or external source-support dynamics. Preserve Suzuki and far-tail.
deliverable: reproducible pole sweep and error diagnostics.

HANDOFF
target: external-audit
type: harmonic-Gaussian-weight-check
parent: v14.880
status: open
action: Verify W_n normalization, Gauss quadrature numerics, source harmonic convergence and explicit nonclaim about finite-Ω retarded pole.
deliverable: scoped verdict.
