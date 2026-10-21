# Hydrogen radial dynamics on the cone — exploration report

**Question (Jeremy, 2026-10-06):** given the magnetic driver, can we map electron
orbitals — and specifically, can the cone get hydrogen's *radial* dynamics
(the n-ladder, the 1/n² energies)?

**Status:** sandbox exploration, 2026-10-06. Machine-verified where stated.
Nothing here is ledgered or published.

---

## 1. The dictionary (verified)

**Hydrogen side (literature, standard).** At fixed orbital angular momentum l,
the radial states |n_r⟩ (n_r = 0,1,2,… radial nodes) carry the positive
discrete series D⁺_k of SU(1,1) with Bargmann index

    k = l + 1,      Casimir C = k(k−1) = l(l+1),

and compact generator K₀|n_r⟩ = (n_r + k)|n_r⟩ = n|n_r⟩, where
n = n_r + l + 1 is the principal quantum number. K± raise/lower n_r at
fixed l — they are the radial ladder operators. (Ref: e.g. the su(1,1)
treatment of the hydrogen radial problem; Casimir = l(l+1) fixes k = l+1.)

**Cone side (verified by machine, truncated Fock space).** Paper C's two-mode
realization K₊ = a₁†a₂†, K₋ = a₁a₂, K₀ = (n₁+n₂+1)/2 satisfies

    [K₀,K±] = ±K±,   [K₊,K₋] = −2K₀,   Casimir = k(k−1),  k = (|d|+1)/2

on fixed-d sectors (d = n₁−n₂), and **K₀ = T as operators** — the cone's
T-coordinate *is* the su(1,1) compact generator. K± preserve d, so they
move along fixed-X branches (X = (d+1)/2), changing T by ±1.

**Match.** Setting |d| = 2l+1 (i.e. k = l+1):

| hydrogen radial (fixed l) | cone |
|---|---|
| Bargmann index k = l+1 | fixed-X branch, X = l+1 |
| principal quantum number n ≥ l+1 | T-coordinate, T ≥ X = l+1 |
| radial ladder n → n±1 (fixed l) | K± along the branch, T → T±1 |
| ground rung n_r = 0 (n = l+1) | branch vertex T = X, Y = 0 |
| ladder element √((n_r+1)(n_r+2k)) | Y = √(n_r(n_r+2l+2)), i.e. Y² = (T−X)(T+X) |

The lowest rung sits exactly at the branch vertex (T = X, Y = 0) — the
"circular" state with no radial nodes — and climbing the branch is
climbing the n-ladder at fixed l. The n ≥ l+1 bound falls out of the
cone inequality T ≥ X automatically.

**Y as transition strength.** Y² = n_r(n_r+2k) is the squared ladder
matrix element at rung n_r — the local radial transition strength.
This unifies with the Rabi finding (Ω_{R,q} = |γ|B₁Y_q, Y_q = local Rabi
frequency): across both threads, the cone's Y-coordinate consistently
means *transition strength / coherence*.

## 2. Dynamics verdict: kinematics yes, energetics no (yet)

- **Kinematics: exact.** The cone carries hydrogen's radial state space and
  ladder operators with no approximation — D⁺_{l+1} on the X = l+1 branch,
  T = n, K± the radial ladders. This is not an analogy; it is the same
  representation.
- **Energetics: not derived.** E_n = −R_H/n² becomes E = −R_H/T² on the
  cone — but the 1/T² is Coulomb input, not cone output. The cone supplies
  K₀ = T, the operator the Hamiltonian is a function of; it does not supply
  the function. Claiming the cone "predicts" 1/n² would be overstatement.
- **The established route to dynamics** is Kustaanheimo–Stiefel: hydrogen ↔
  4D oscillator via the Hopf map, with the Coulomb energies emerging from
  the oscillator energy–frequency relation. The cone's two complex modes are
  structurally the KS kind of oscillator pair, but the KS constraint and the
  energy–frequency map have not been worked out on the cone. That is the
  concrete next step if dynamics is the target.

## 3. Driver angle

- **Zeeman (magnetic field):** immediate — the su(2) rings give the m-splitting,
  with Y as the drive axis per the driver theory (axis lock: X = quantization,
  Y = driver). Already covered by the orbital map.
- **Radial driving:** a drive that changes n at fixed l (e.g. microwave-driven
  Rydberg states) would be an su(1,1) drive on a fixed-X branch — the natural
  next dynamical application, not yet worked out.
- **Stark effect** (electric field, parabolic states, SO(4,2)) is beyond the
  cone's su(2)⊕su(1,1); flagged as future, not claimed.

## 4. Calibration

- The D⁺_{l+1} radial structure and K₀ = n are textbook (not new).
- New to the program: K₀ = T as an *operator identity* on the cone (so the
  cone's T-axis is hydrogen's n-axis), the branch-vertex = circular-state
  correspondence, and Y = radial transition strength (unifying the Rabi thread).
- The Casimir coincidence C = l(l+1) on both the su(2) orbital and su(1,1)
  radial sides is noted as an observation, not a result.
- Paper C's operator revival identity vs. Rydberg wavepacket revivals
  (T_rev ∝ n³): possible connection, unexplored — do not claim.

## 6. Sphere-shell reading (Jeremy, 2026-10-06)

"1/T² is the sphere shell of the T circle. It's right there."

Precise form. The fixed-T circle (radius T) is the equator of the 2-sphere
shell of radius T in the embedding space. That shell has area 4πT² and
Gaussian curvature 1/T². Two independent readings converge on 1/T²:

(a) **Gauss.** A conserved flux through the shell has density ∝ 1/T².
Coulomb's law is what a conserved charge looks like spread over the
sphere shell — so the 1/T² *form* is shell geometry, not an imported
potential shape.

(b) **Fock.** In Fock's SO(4) treatment, momentum space stereographically
projects to S³ of radius p₀ = 1/(na₀), and E = −p₀²/2m. With T = n,
1/T² = p₀² (up to constants) — the same 1/T², from the momentum sphere.

This upgrades §2's verdict: the unexplained input shrinks from "1/n²" to
"flux conservation" (reading (a)) or "the Fock S³" (reading (b)) — the
1/T² itself is then forced by geometry. Honest remainder: form ≠ spectrum.
The shell gives the *shape* of the law; E_n as *eigenvalues* still needs the
operator. The search is now narrower: find the cone's conserved current
(for (a)) or the explicit Fock S³ ↔ cone map (for (b)).

## 7. The unified shell (Jeremy, 2026-10-06 — continued)

"The Larmor orbits live on the sphere shell too."

The sphere shell **is** the Bloch sphere. In (X,Y,W) coordinates
(W = Tr(ρσ_y), the imaginary coherence), pure subnormalized states satisfy
X²+Y²+W² = T² — the shell S²_T. The cone's T-circle (X²+Y²=T²) is the
meridian W = 0. Verified by machine:

- **Larmor (lab frame, about quantization axis X):** ṙ = ω_L(x̂×r)
  preserves |r|² = T² and X — the orbits are latitude circles X = const
  on the shell. (Correction 2026-10-06: an earlier draft said "about Y";
  H₀ = Ω₀J_z in v13.595 and X_cone = ⟨σ_z⟩ put lab-frame Larmor about X.
  The driver theory's "revolution about Y" is the rotating-frame
  drive-axis motion — see Rabi bullet — not lab-frame Larmor.)
- **Rabi/drive (about drive axis Y):** uniform circular motion on the
  meridian (the T-circle) at Ω_R = |γ|B₁Y_q (Rabi agent, verified).
- **Coulomb:** Gaussian curvature of the shell, 1/T² (§6).

One shell, three readings: the meridian carries the real (cone) states and
the Rabi drive; the latitude circles carry Larmor precession about the
driver axis; the curvature carries the Coulomb energetics. The cone's
T-circle is where the magnetic dynamics meet the real states. Axis lock
respected throughout: driver ⊥ quantization (Y ⊥ X) by design.

Note on scope: this S²_T (Bloch state space, T = Trρ) and the §6 embedding
shell (T = n) are the same *geometry* in two roles — the cone program's
signature move is that T is radius in both. The full |n,l,m⟩ (su(2)⊕su(1,1),
Paper C) is the larger story; the shell unifies the driver/qubit magnetic
dynamics with the Coulomb curvature reading.

## 8. Bicone doubling — SO(4) (Jeremy's proposal, 2026-10-06)

"What if for SO(4) needs su(2)⊕su(2) you do 2 cones, T circle base to
T circle base inside the sphere."

Two truncated cones glued base-to-base at a common T₀-circle (a bicone),
inside the sphere X²+Y²+(T−T₀)² = T₀² — touching at the poles (apices)
and the equator (the T₀-circle); containment verified. Each cone carries
its own oscillator pair and Schwinger su(2); the gluing is the constraint.

**Verified by machine.** With J from pair (a₁,a₂), K from pair (b₁,b₂),
L = J+K, A = J−K:

    [L_i,L_j]=iε_ijkL_k,  [L_i,A_j]=iε_ijkA_k,  [A_i,A_j]=iε_ijkL_k,

i.e. so(4). On the glued sector j₁=j₂=j: L·A = 0 and L²+A² = 4j(j+1);
dim V_j⊗V_j = (2j+1)² = n² with n = 2j+1.

**The gluing is the KS constraint.** Each cone's T₀-ring carries spin
j = T₀−1/2; gluing at a *common* T₀ forces j₁ = j₂ — exactly the
N_a = N_b / j₁ = j₂ constraint the KS agent found irreducible to one pair.
Gluing rings at different T would give j₁≠j₂ (the unphysical sector);
the geometry selects the physical one.

**Dictionary.** Bicone at T₀ ↔ hydrogen n-shell with n = 2T₀
(n=1,2,3,… ↔ T₀=1/2,1,3/2,…). L = J+K gives l = 0,…,n−1 (n² states ✓);
A = J−K is the Runge–Lenz vector. Geometric reading: L rotates the two
cones synchronously (physical rotations), A rotates them differentially —
and A is now well-defined, dissolving the Fock agent's fiber-mixing
obstruction, because the doubled space gives both SU(2)s a geometric home.
The bicone's sphere has radius T₀ = n/2, curvature 4/n² ∝ 1/n².

**Division of labor (clean).** Single cone, fixed-X branches, su(1,1):
radial ladder, n-changing at fixed l (between shells). Bicone at fixed
T₀, so(4): l,m-changing at fixed n (within a shell). Together: the full
hydrogen kinematics — the cone program's two halves meet.

**Open.** The bicone is a proposal with verified algebra, not a derived
structure: how the two cones' coordinates jointly embed, and whether the
second pair has independent physical meaning in the program (vs. being a
formal doubling), remain open. This is the "second spinor pair" build both
the Fock and KS agents flagged — now with a concrete geometric form.

## 9. Suggested next drill

## 10. Closing the open questions (2026-10-06)

**CLOSED — Fock SO(4) obstructions.** The bicone realizes so(4) directly
(J on cone 1, K on cone 2), so the Hopf-descent obstructions are sidestepped
for the algebra: no fibration needs preserving because both SU(2)s act
geometrically. The Fock S³→bicone map remains unworked but is no longer
load-bearing for the symmetry.

**CLOSED — KS constraint.** It is the gluing: two T₀-rings at a common T₀
force j₁ = j₂ = T₀−1/2. The "irreducibly two-pair" constraint is a
geometric identification, not an extra equation.

**CLOSED (as far as it goes) — the second pair's meaning.** Four complex
modes = the KS 4D oscillator's full ℝ⁸ phase space; cone 1's pair is the KS
spinor/position half (KS agent), cone 2's the remaining mode pair. The split
is (1,2)|(3,4), not position|momentum — the second cone is the rest of the
oscillator, not a formal doubling.

**OPEN (honest).** The ω²=|E|/2m link (Coulomb input — the 1/n²'s remaining
source); the U(1) charge on (X,Y,W) (Gauss source); the radial su(1,1) as
bicone scaling T₀→T₀±1/2 between shells (natural next build); Stark effect
and Rydberg revivals (future).

**Figure.** `fig_bicone_sphere.png` / `.pdf` — the bicone with canonical
mesh, gold T₀-circle (gluing), inside the sphere. Generator:
`~/workspace/d12/figures/bicone_so4.py`.

Work the KS map explicitly for the cone's two modes: identify the KS
constraint in (T,X,Y) language and derive the energy–frequency relation.
If that lands, the cone gets hydrogen dynamics, not just kinematics.
