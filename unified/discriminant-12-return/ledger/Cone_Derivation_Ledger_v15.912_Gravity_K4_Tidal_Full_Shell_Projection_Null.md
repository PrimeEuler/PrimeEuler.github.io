# Cone Derivation Ledger v15.912 — Actual Fermi tidal coupling projected onto the complete Schwinger ladder

**Date:** 2026-11-13 US Eastern. **Track:** Gravity. **Parents:** Gravity v14.928 K4 pure tensor action, v15.703/705 TT tidal GR comparator, v15.875–876 Fermi tidal oscillator, v15.906–911 fixed-sum / varying-product ladder and full populations. **Live master HEAD immediately before ledger write:** 482165885b182b8bab00d063128bc6af40ef76f7. Target checked absent. Strict additive-only; no changes to certified, Audit, Sandbox or Suzuki files.

**Question:** Does a real, field-derived gravitational interaction change the nested sqrt(nk) action-circle ladder and produce a new dimensionless, coupling-independent dark-node observable?

**Status:** [D] exact leading local Fermi-normal tidal form, fixed-D quantum projection and ΔN selection rule, matched pure-TT K4-versus-GR operator shape; [N] numerical population and dark-node detuning check; [N] no Cone-specific interaction coefficient or additional curvature weighting derived; [O] full K4 scalar/vector+matter action with properly sourced detector response and physical velocity-label intertwiner.

## Gate 616 — gravitational interaction with actual field origin

For the conventional leading nonrelativistic Fermi-frame tidal interaction of a point oscillator in a physical laboratory coordinate plane (q1,q2), take **H_tidal=(M/2) E_ij(t) q_i q_j** with **E_ij** the properly time-unit-converted electric tidal curvature in s^-2. A local TT wave oriented along the third axis has the transverse tracefree matrix

**E=[[A,B],[B,−A]]**, with A,B in s^-2 (sign changes under Riemann conventions). Then

**H_tidal=(M/2)[A(q1²−q2²)+2B q1q2]**.

The physical q_i are spatial detector coordinates in meters and MUST NOT be equated with the Cone's X (m/s velocity coordinate) without a dynamical map. Their oscillator length is l=sqrt[hbar/(2M omega*)]. Expanding q_i=l(a_i+a_i†) yields (i) number-conserving a†a pieces and (ii) pair-creation/annihilation terms carrying ΔN=±2. The latter are real parts of the full quadratic Hamiltonian, not errors; omission by RWA requires physical detuning/weak-coupling conditions.

## Gate 617 — exact fixed-shell projection is standard SU(2)

Let P_N project to Fock sector N=N1+N2=D−1. The exact quadratic projection, independent of invoking RWA, is

**P_N H_tidal P_N = (hbar/omega*)[A J_z + B J_x]**,

where J_z=(N1−N2)/2, J_x=(a1†a2+a2†a1)/2. For every link (n,k)->(n+1,k−1) at fixed D=n+k, B J_x has right-neighbor amplitude **hbar B sqrt(nk)/(2omega*)** and no extra local curvature factor. A J_z is diagonal, changing relative phases. The Hermitian quadratic action's off-shell pieces connect only **N→N±2**. In particular, no physical term built from the basic isotropic point-mass Fermi tidal Hamiltonian produces the arbitrary curvature-link perturbation in v15.911.

For a prescribed local TT tensor, v14.928/v15.705 K4's tensor dispersion alters field time evolution but not its local polarization matrix E_ij or this detector operator. A distinct K4 scalar/vector physical response could change the actual tidal matrix, but was NOT calculated by this gate. The frozen K4 tensor action does not by itself determine a matter source amplitude, proper local metric, boundary condition, or velocity-to-position conversion. Thus a parameter-free difference from the matched GR+matter comparator is NOT established.

## Gate 618 — ordinary tidal polarization destroys the dark node

At D=5, initial Cone pair (4,1) -> |3,1>, define g=B/omega* and scaled time tau=g t with B nonzero. Under the number-conserving Hamiltonian **H_eff/hbar=g(J_x+(A/B)J_z)**, at tau=pi/2 the central (3,2) node's probability is:

- A/B=0: P_center≈0 (numerical <1e-25), full population (1/4,1/4,0,1/4,1/4).
- A/B=0.2: **P_center=0.00010977201163581694**.
- A/B=0.5: P_center≈0.004126498548491597.
- A/B=1: P_center≈0.0560361235824451.

All probabilities normalized to 1. These are *ordinary SU(2) detuning/polarization* effects with standard GR's tidal operator, not evidence of new Cone curvature. A/B is orientation- and polarization-dependent, and a single pure-TT E tensor can be diagonalized by detector-axis rotation; the dark-null condition is not a gauge-invariant standalone novelty claim. Pulse duration and local reference clock must be independently fixed before comparing experiments. The magnetic J_y comparator shares ordinary SU(2) amplitudes up to phase conventions but a multi-drive phase reference can distinguish orientations.

## Gate 619 — exact code, novelty verdict, next physical selector

**Reproducer:** research-notes/k4_fermi_tidal_full_shell_projection_v15_912.py, commit **482165885b182b8bab00d063128bc6af40ef76f7**. Locally executed Python/NumPy/SciPy PASS: finite two-oscillator Fock truncation through N=8, direct full q1²−q2² and q1q2 matrices, exact fixed-D projections D=2..7 to A J_z+B J_x, zero odd/off-shell |ΔN|≠0,2 matrix elements, and explicit D=5 detuned population at tau=pi/2. Independent Audit pending.

**Positive:** the nested sqrt(nk) action-circle radii have a genuine conventional field-interaction counterpart: real tidal gravity gives exactly their Schwinger transition coefficients. Its structure follows from well-defined physical local curvature and oscillator coordinates rather than an inserted random transverse ladder drive.

**Negative:** within this explicitly scoped standard point-detector TT model, every transition remains ordinary SU(2), and even the central-node dark null is lifted by ordinary diagonal tidal polarization. No independent Cone-specific nonlinear link coefficient, new gravitational force, universal n+1 frequency, physical acceleration normalization, or dimensionless experimentally distinct K4 response arises. The X m/s axis remains a postulated measured velocity operator; its physical identification with this detector's quantum velocity is not derived here.

**NEXT:** seek the *actual physical velocity operator* v_i=p_i/M for the same Fermi oscillator and compare its spectral matrix elements to the Cone Xhat=u(J_z+1/2): one is an oscillator quadrature changing occupation by ±1, the other is a number-difference diagonal operator. Test whether any physical intertwiner preserves observed transition probabilities and canonical commutators; a no-go closes the velocity-axis direct-observable shortcut. Separately, derive sourced K4 scalar/vector + Maxwell/matter response rather than posit a non-SU(2) curvature perturbation.

**HANDOFF Audit/Muse:** confirm factor-of-two in projection of E12 cross term, ΔN=±2, ordinary A/B detuning lifting dark node, and scope of pure-TT K4 comparison. Prior Audit Round571 missing standalone scripts v15.888/890/895/897 remain open.
