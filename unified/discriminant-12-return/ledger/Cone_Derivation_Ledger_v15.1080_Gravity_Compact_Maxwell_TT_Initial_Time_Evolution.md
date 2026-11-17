# Cone Derivation Ledger v15.1080 — Evolving compact Maxwell plus-stress, exact nonconservation of initial 3/5 anisotropy

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] exact free-Maxwell Cauchy-field time derivatives and initial quadratic temporal stress variation; [N] integrated-plus-stress is not conserved even though full Maxwell energy-momentum is locally conserved; [O] no complete Einstein–K4 ADM/Weyl response or novel Cone-only force. **Live HEAD immediately before ledger write:** a129a75975f2852c18f2209798812504362889ef (reproducer). Next free sequential entry v15.1080; Audit owns v15.1079. Collision check: no other v15.1080 exists at latest HEAD. Additive only, no modifications to Suzuki, Audit, Muse, Sandbox or earlier certified files.

## Audit and nonredundancy
External Audit Round 590, canonical v15.1079, commit 2568c3bb777e25239b6f62b8720d41ad54fc05b1 independently checked v15.1076–1078, including the initial compact-source ratio P_plus/E=3/5 and all correct reproducers, with no corrections. v15.1078 already defined the compact electromagnetic initial-data stream function and proved nonzero TT+ Fourier stress, but it did not determine whether the initial anisotropy ratio persists after the vacuum Maxwell field evolves. v15.1077 and earlier K4 source-to-Weyl and optical-response comparisons remain separate. This gate answers the temporal-stress question without presupposing any gravitational dynamics or new drive frequency.

## Gate 897 — exact free Maxwell initial-time data
Use c_light=epsilon0=mu0=1 in Minkowski/conformal test coordinates, and retain the exact v15.1078 source
Psi=A f(x/a)f(y/b)f(z/c), f(s)=(1-s²)^3 for |s|<1 and zero otherwise,
E0=(partial_y Psi,-partial_x Psi,0), B0=0, with a,b,c>0.
This is compact finite-energy free Maxwell initial data with div E0=div B0=0. At t=0:
dot E0=curl B0=0,
dot B0=-curl E0,
ddot E0=-curl curl E0=Delta E0.
The usual conserved total EM energy is
Etotal=1/2 int_R3 (E²+B²) d³x,
and integrated plus-polarized stress is
Pplus(t)=1/2 int_R3 [Ey²+By²-Ex²-Bx²]d³x.
By time reflection of the specified initial field, dot Pplus(0)=0, but ddot Pplus(0) need not be zero. This integrated stress is **not** itself a conserved Noether energy, nor is it directly a gauge-invariant gravitation signal. The initial compact support and its Maxwell finite-speed evolution are valid; no permanent fixed-shape cavity field is assumed.

## Gate 898 — exact temporal curvature, including longitudinal magnetic contribution

Let I0=int_-1^1 f² ds=2048/3003, I1=int_-1^1 (f')² ds=1024/385, I2=int_-1^1 (f'')² ds=1024/35. Then I2/I1=11 and I1/I0=39/10.

The exact initial Maxwell differentiation gives
ddot Pplus(0) = int_R3 [Ey Delta Ey - Ex Delta Ex + (curl E)_y²-(curl E)_x²] d³x.
Integrate by parts over the compact support, and use
(curl E)_x=-partial_z Ey,
(curl E)_y=partial_z Ex.
The **longitudinal gradient terms double rather than cancel**: their total contribution is 2 int[(partial_z Ex)²-(partial_z Ey)²]d³x. This is necessary; dropping the generated magnetic field produces an incorrect coefficient.

The exact separated-integral result is
ddot Pplus(0)
= A² c I0² I2 [a/b³ - b/a³]
 + 2 A² I0 I1²/c [a/b-b/a].
The earlier initial energy and stress are
Etotal=A² c I0² I1 [a/b+b/a]/2,
Pplus(0)=A² c I0² I1 [b/a-a/b]/2.
Therefore the ratio is
ddot Pplus(0)/Etotal
= 22(a²-b²)/(a² b²) + (78/5)(a²-b²)/[c²(a²+b²)].
For a=ell,b=2ell,c=ell it becomes -1293/(50 ell²), while Pplus(0)/Etotal=3/5. Since dot Pplus(0)=0,
Pplus(t)/Etotal = 3/5 - (1293/100)(t/ell)² + o(t²)
in c_light=1 units. The early-time formula is local to t=0, NOT a claim it stays positive, harmonic or valid for large t.

At transverse equality a=b, both Pplus(0) and its second derivative vanish by the x/y exchange symmetry. This is a symmetry control, not a proof every unrelated field with a=b has vanishing tensor stress.

## Gate 899 — physically relevant Fourier source, not a new q2 frequency

The true TT+ component at nonzero longitudinal spatial wavenumber q is obtained by applying the TT projection to T_ij(q,t). The whole-space integrated stress calculated above is formally the q=0 Fourier value, whose TT projector is direction-dependent. However the underlying stress is compactly supported and has a Fourier transform continuous near q=0; with nonzero initial plus numerator at a!=b, the nonzero-q plus source persists for sufficiently small q in the longitudinal direction. Its second-time derivative likewise exists in the properly regular Fourier weak sense, but the integrated numerical coefficient -1293/50 **must not** be reused unchanged for every q. It is not a measured gravitational curvature.

The resulting physical K4 tensor forcing is a linear functional of this standard Maxwell stress through the action's already-established couplings. Solving full ADM metric constraints, retarded source-to-gauge-invariant Weyl response, appropriate conformal background and local detector remains open. As in v15.1077, when comparison against Einstein gravity with the identical elastic solid, full Maxwell action, same source/boundaries and probe is truly matched, no Cone-exclusive residual appears without an independently derived additional operator. This temporal evolution creates no new EM-to-G force coefficient, frequency, q=2 ladder coupling or X-cone causal requirement.

## Gate 900 — reproducibility, audit and next task
Independently executed exact SymPy in the local working container for the Maxwell gradient norms and profile integrals; it printed PASS with I0=2048/3003, I1=1024/385, I2=1024/35, Pplus/E=(b²-a²)/(b²+a²) and ddot Pplus/E equal to the displayed formula, including -1293/(50 ell²) at the rectangular sample. Additive reproducer: research-notes/k4_compact_maxwell_stress_evolution_v15_1080.py, commit a129a75975f2852c18f2209798812504362889ef. Independent external Audit is pending.

**Positive:** The previously static anisotropic-stress source has an explicitly determined **nontrivial exact early-time Maxwell evolution** while conserving total field energy; the longitudinal magnetic contribution is indispensable. **Negative:** This is standard electromagnetism, supplies neither a new Cone force/physical frequency nor a quarter-ladder selector. **Audit handoff:** independently derive Pplus'' from Maxwell Cauchy evolution, check the factor-of-two longitudinal derivative, all three bump integrals and the -1293/50 ratio, and distinguish spatially integrated stress from nonzero-q TT Fourier stress. Next gate: compute the nonzero-q Fourier stress kernel in early time and convolve with the physical coasting K4 retarded tensor propagator, while keeping source normalization/constraints explicit, then test a physical Weyl output against a fully matched conventional elastic GR comparator.
