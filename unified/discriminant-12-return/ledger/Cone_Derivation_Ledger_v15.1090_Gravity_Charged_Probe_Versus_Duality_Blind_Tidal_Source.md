# Cone Derivation Ledger v15.1090 — Duality-blind tidal source versus duality-sensitive electric charge probe

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] exact pointwise electric test-charge Lorentz-force discrimination for vacuum Maxwell duality-related compact packets and identical full Maxwell gravitational source; [N] the T/X invariant-sign dictionary selects neither a new Einstein–K4 gravitational source nor a physical G or parameter-free gravity observable; [O] finite charged detector apparatus, full Einstein–K4 ADM constraints and complete scalar/vector/tensor tidal reconstruction. **Immediately prewrite live HEAD:** 12790877c3f866975e4840566ec959c229966b2d (new reproducer). New path absent; additive only; no Suzuki, Audit, Sandbox or previously-certified files modified.

## Protocol and prior relevant results

External Audit Round 591/v15.1087 independently confirmed Gravity v15.1080, v15.1083, v15.1085 and Sandbox v15.1082/v15.1084/v15.1086, and found the failing q⁴-vs-q² assertion in v15.1081. Gravity v15.1089 explicitly repaired that reproducibility defect by a separate additive reproducer and established the exact invariant Maxwell stress-energy no-go against using duality sign/T-X field labels as an independently measurable Einstein–K4 source. Sandbox v15.1088 cross-referenced the EM seat's two tags (m,q) with the gravitational one-tag mass dictionary and disclosed its own scope as imported standard field theory; there is no source-derived extra coupling. This gate tests an observable that *does* distinguish the duality labels, making clear why it is ordinary electromagnetism and does not contradict the stress-energy no-go.

## Gate 917 — compact Maxwell field at one specified interior point

Take the vacuum, compact Cauchy data of v15.1078:
Psi=A f(x/a)f(y/b)f(z/c), f(s)=(1-s²)³ for |s|<1 (0 outside), E=(partial_y Psi,-partial_x Psi,0), B=0 at initial t=0. At (x,y,z)=(0,b/2,0), direct exact differentiation gives
E0=(-27A/(16b),0,0) in c_light=epsilon0=mu0=1 units. For any duality rotation theta, the initial vacuum field is
E_theta=cos(theta) E0, B_theta=-sin(theta) E0.
Both satisfy the source-free Maxwell initial constraints, and their full vacuum Maxwell evolution preserves duality. This is a test of external initial fields; a charged test object is added only with negligible backreaction and its own localized self-fields excluded.

## Gate 918 — electric test charge sees the duality angle

A test body of electric charge q_e and rest mass m at the specified point, instantaneously at rest relative to the local inertial frame, experiences the **electromagnetic** Lorentz 3-force F_e=q_e E_theta=q_e cos(theta) E0. Its initial acceleration in this ideal local test limit is a_EM=(q_e/m)cos(theta)E0 (apart from the same common gravitational/geodesic terms). Thus at theta=0 the force is q_e E0; at pi/4 it is q_e E0/sqrt(2); at pi/2 the initial magnetic-dual configuration has E=0, so a stationary electric charge has zero initial Lorentz force. No gravitational comparison can make those ordinary electric accelerations a novel gravitational force law.

For initial probe velocity v=(0,0,v), F_e=q_e[E_theta+v cross B_theta]=q_e[cos(theta)E0-sin(theta)(v cross E0)]. The magnetic response at theta=pi/2 is then nonzero for v≠0 and orthogonal to both v and the local field. This proves the probe selection is about *charge/current type and motion*, rather than a new T- versus X-spacetime.

## Gate 919 — gravitational stress and full ADM source do not see the phase

At every spacetime point in a vacuum source-free Maxwell solution, electric/magnetic duality preserves rho=(E²+B²)/2, S=E cross B, and Tij=rho delta_ij-EiEj-BiBj, hence all components of Tmunu. The canonical reproducer checked this by exact SymPy at the chosen compact point for rotations 0, pi/2, pi/4 and one rational (3/5,4/5) rotation. The global stress equality for arbitrary theta was already established in v15.1089. The same Maxwell gravitational source implies the same Einstein–K4 scalar/vector ADM constraints and tensor forcing, subject to the same gravitational initial/boundary data. Consequently any *purely gravitational, negligible-backreaction* tidal/geodesic detector has equal response under the two duality-related configurations. This is a full-source statement, not merely a TT projector statement.

An electrically charged detector itself is not duality-neutral: its Lorentz force distinguishes the fields. If its charge/backreaction or measuring apparatus contributes non-negligible additional stress, the combined sourced gravitational systems need no longer be identical; then the equal-source claim is restricted to the vacuum-field subsystem and ideal probe limit. Likewise external electric currents, electrodes or monopole boundary constraints break full vacuum duality and require a separate complete physical apparatus calculation.

## Gate 920 — falsifiable status of T/X labels and null hinge

At the same initial point, I1=E²-B² and I2=E dot B rotate as I1_theta=cos(2theta)|E0|², I2_theta=-sin(2theta)|E0|²/2. Thus theta=0 lies in electric-dominated T label, theta=pi/2 in magnetic-dominated X label; the point's Maxwell Tmunu is identical. At theta=pi/4, I1=0 but I2=-|E0|²/2≠0, so the zero-sign boundary is **not** a radiative Maxwell-null hinge despite the label; the two-invariant condition is necessary. No field action mapping arithmetic Cone T/X to electromagnetic duality angle or selecting physical charge is derived. These examples also clarify Sandbox's dictionary does not imply the actual compact packet is radiation at its initial support.

**Reproducer:** research-notes/k4_duality_charged_vs_tidal_probe_v15_1090.py, additive commit 12790877c3f866975e4840566ec959c229966b2d. Executed equivalent script in local Python/SymPy: PASS exact compact point field -27A/(16b), source stress/momentum identity at four duality angles, Lorentz-force formulas for stationary and moving electric test charges, and nonradiative I1=0,I2!=0 check. Audit of this gate pending.

**Verdict:** charged electromagnetic probes can distinguish phase/magnetic-versus-electric duality that gravity sourced only by Maxwell Tmunu cannot. This is standard Lorentz-force physics, not a new gravitational force or independent Cone selector. **NEXT:** to seek a Cone-specific observable, propose and derive a concrete action-level term (or genuine boundary/dynamical selector) consistent with Maxwell gauge symmetry and diffeomorphism Ward identities, then calculate a nonzero *matched conventional GR+elasticity* residual. An ad hoc q² mesh coefficient or tuned G would not qualify.

**AUDIT HANDOFF:** verify pointwise source field derivative and signs; distinction between sourced metric equality and test-charge Lorentz force; stationary magnetic-dual initial force null versus moving probe; vacuum duality assumption and nonzero I2 at theta=pi/4; repeated version-collision hygiene.
