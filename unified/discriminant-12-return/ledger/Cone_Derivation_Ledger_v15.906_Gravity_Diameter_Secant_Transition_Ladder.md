# Cone Derivation Ledger v15.906 — Original diameter–secant ratio is the fixed-circle transition ladder

**Date:** 2026-11-13 US Eastern. **Track:** Gravity. **Parents:** Sandbox diameter–secant note deposited at v14.550, Paper C Quantum Realizations v1.1, Gravity v15.895–905, External Audit Round 571. **Live master HEAD immediately before ledger write:** fb8a8e497e1ab6ec66c6773e3c02225334009196. Target checked absent. Additive only; do not alter certified, Audit, Sandbox, or Suzuki objects.

**Owner correction:** The transitions meant by the latest n+1-cycles / sqrt(n) discussion are the *already discovered* pair-ladder **(n+k)/(n−k)**, not simply neighboring-shell energy gaps, assumed N=n+1 equidistant outer-circle nodes, or successive temporal global-phase windings. Recover the existing exact factor-pair machine first.

**Status:** [D] exact pair-ladder operator coefficient, projective secant/rapidity ratio and finite geometric angle steps; [N] ratio not itself a frequency and no frequency/force is selected without a Hamiltonian; [O] actual phase/transition dynamics derived from coupled fields.

## Gate 594 — same circle, exact moving secant and quantum amplitude

For factor pair (n,k), with n>=k>0 integers and sector scale u>0, the Cone coordinates are X=u(n−k)/2, Y=u sqrt(nk), T=u(n+k)/2. The outer diameter is u(n+k), and X²+Y²=T² exactly. Its geometric half-chord Y is **u sqrt(nk)**. In the standard Paper C Fock dictionary x=n_1+1, y=n_2, the pair (n,k) is Fock |n−1,k>, total occupation N=n+k−1, spin j=N/2, and fixed-T SU(2) representation dimension 2j+1=n+k.

The canonical Schwinger raising operator **J_+=a_1^dagger a_2** sends

**J_+ |n−1,k> = sqrt(nk) |n,k−1>**, k>=1,

which is the EXACT normalized geometric half-chord in u=1 units. The destination pair is (n+1,k−1), with the same total n+k, so it lies on the same outer action/transition circle; the endpoint (n+k,0) is annihilated by further J_+. In particular, (n,1) -> (n+1,0) with amplitude sqrt(n), the earlier first-transition chord, but the entire (n,k) ladder is the more general structure. The operator coefficient itself is dimensionless until multiplied by a Hamiltonian coupling strength; it must not be called a frequency.

## Gate 595 — secant transition map and bounded angle

Define the rapidity/angle dictionary (for n>k):

**psi=1/2 ln(n/k)**,
**cos(phi)=(n−k)/(n+k)**,
**sin(phi)=2sqrt(nk)/(n+k)**,
**phi=2 atan sqrt(k/n)**,
**(n+k)/(n−k)=coth(psi)=sec(phi)**.

At the next J_+ transition, numerator D=n+k stays fixed, while the difference increases by two:

**R=(n+k)/(n−k) -> R_next=(n+k)/(n−k+2)**.

Geometric angular increment is **Delta phi=2 atan sqrt((k−1)/(n+1))−2 atan sqrt(k/n)** (negative for a raising move); it is generally nonuniform across the ladder. The normalized point z=[(n−k)+2i sqrt(nk)]/(n+k) moves along the **same** unit semicircle. At n=k, the secant/coth ratio diverges because X=0, but phi=pi/2 and Y=u n are finite. This is a coordinate pole, not divergent physical energy or transition rate. For k=0, the endpoint ratio is 1 and phi=0; psi=+infinity is a limit rather than a finite real rapidity.

Example fixed diameter D=5: (3,2) has sqrt(nk)=sqrt6, ratio 5, phi≈1.369438406; (4,1) has sqrt4=2, ratio 5/3, phi≈0.927295218; (5,0) has zero chord, ratio 1 and phi=0. The ladder does not traverse these geometrical angular intervals equally.

## Gate 596 — frequency is a Hamiltonian property, not secant alone

The equal-frequency two-oscillator Hamiltonian H0=hbar omega_*(N+1) assigns the SAME energy hbar omega_*(n+k) to all states on the fixed-D ladder. Hence the J_+ transition **has zero Bohr energy gap under H0**, even though its matrix element and geometric secant change. At k=1, D=n+1, the entire shell globally accumulates n+1 quantum phase cycles in one base period; that common Schrödinger phase is not J_+-induced motion around the circle and is not observable by itself.

An explicit physically normalized drive H_int=hbar g (J_++J_-)/2, g in s^(-1), can cause within-shell population exchange; its matrix elements scale as g sqrt(nk)/2. But g (and pulse protocol or drive field) must be supplied independently. The step's *geometric* Delta phi is not the state-vector evolution angle unless a specific dynamical identification is derived. The conserved shell SU(2) action does not automatically produce the radial inward/outward force, a contraction of physical radii, or the outer circle's independent acceleration/rate parabola.

Thus the project owner's transition ratio has an exact, operator-level interpretation and improves the previous vague n+1-node hypothesis; it does NOT select a unique physical oscillation frequency, n+1 actual inner revolutions, kinetic-energy gain, fundamental acceleration or G.

## Gate 597 — reproducibility and further work

**Reproducer:** research-notes/k4_diameter_secant_ladder_v15_906.py, commit fb8a8e497e1ab6ec66c6773e3c02225334009196. Executed locally in equivalent Python/SymPy against n,k symbolic identities and explicit fixed-D finite matrices for D=2..8: PASS. Checks preserved diameter, secant update, sqrt(nk) J_+ amplitudes, phase formulae, finite n=k phase, and H0 fixed-shell degeneracy. Independent Audit pending.

**NEXT:** (1) derive an explicit time-evolution generator for the J_+ ladder from the already proposed outer acceleration parabola / inner sqrt(n) turning mechanism, not simply insert a drive; (2) test whether physical transition amplitudes g sqrt(nk), phase advances Delta phi, and their action integrals obey any nontrivial invariant between two circles; (3) compare gapped (e.g. anisotropic) versus exactly degenerate SU(2) dynamics, and never identify a zero-gap operator step with a radiated frequency. Keep a separate analysis of possible temporal n+1 phase windings and the pi sqrt(n) arc if they are claimed to be physically related.

**HANDOFF Audit/Muse:** verify normalized chord/Y equals the J_+ coefficient, exact secant update and phi, distinguish n=k pole from actual singularity, and audit the difference between matrix-element amplitude and transition frequency. Audit Round 571's outstanding v15.888/890/895/897 missing reproducibility entries remain open.
