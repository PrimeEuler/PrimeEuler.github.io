# Cone Derivation Ledger v14.879 — Finite-Larmor retarded harmonic reduction

Date 2026-10-25. Parents v14.872–878. Research note research-notes/Finite_Larmor_Harmonic_Retarded_Seat_Source.md, commit 49feaa8d05c8d736fd0a58f8ab87b054445a6343. Live prewrite HEAD 49feaa8d05c8d736fd0a58f8ab87b054445a6343. Additive gravity lane only; Suzuki/far-tail untouched.

[D] Source at first order δ: rho1=-ig kx f_a(k)e^-ikc(t)δ, J1=g f_a e^-ikc(t)[δdot e_x−ikx v(t)δ]. It exactly obeys Fourier continuity. Define h=e^-ikc(t) and Fourier coefficients b_n=(Ω/2π)∫_0^(2π/Ω)h(t)e^(+inΩt)dt, d_n likewise for h(t)v(t). With this convention h(t)=Σ b_n e^(-inΩt). Therefore for δ=δω e^(-iωt), the nth sideband frequency is ω+nΩ and coefficients are rho_n=-ig kx f_a δω b_n, J_n=gf_a δω[-iω b_n ex−ikx d_n]; frequency-indexed continuity is -i(ω+nΩ)rho_n+i k·J_n=0. NOTE: The companion research note mistakenly labels these coefficients b_{-n},d_{-n}; correct indexing is b_n,d_n for the explicitly defined Fourier convention. This is a sign/index correction only and does not affect the spectrum or helical symmetry statement.

[D] Vacuum Maxwell propagators are rotationally invariant, so exact rigid helical symmetry makes the scalar seat quadratic kernel stationary despite source sidebands. The EM retarded kernel is a single-frequency scalar function of ω with internal channels ω+nΩ rather than necessarily an off-diagonal Floquet matrix. Its dimensionless parameters include α=Ωa/c and β=R/a (plus any source-support parameters). At α=0 the original frozen Gaussian kernel of v14.874 is recovered for arbitrary β, because common fixed translations leave free-space EM field energy unchanged.

[O] No finite-Ω complex pole numerically certified here; requires full conserved source, Gaussian transverse/longitudinal propagators, Bessel harmonic convergence, and support-mechanics assumptions. Static field-energy correction v14.877 cannot be substituted into causal pole equation. No Newton G/Higgs relation.

Flags: conserved_harmonic_source=EXACT; harmonic_index_correction=b_n_not_b_minus_n; helical_seat_kernel_stationary=TRUE; finite_omega_complex_pole=NOT_NUMERICALLY_CERTIFIED; gravity_shared_seat=OPEN; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: finite-larmor-retarded-harmonic-source
parent: v14.879
status: open
action: Verify harmonic Fourier sign convention, channel-by-channel continuity, helical invariance and α→0 limit; develop numerical finite-Ω pole continuation and report convergence rather than assuming field-energy correction produces a force.
deliverable: scoped audit verdict.
