# Cone Derivation Ledger v14.700 — Gravity lane: rank-1/rank-2 rotor response gate; planar/spherical model separation; first G-free null observable is standard gradiometry

**Timestamp:** 2026-10-22 (EDT)
**Lane:** Gravity research (dedicated; separate from Suzuki far-tail certification)
**Parents:** v14.550 (gravity-road open items), v14.620–632 (unit-circle/energy/rotor/rank-2 chain and audits), v14.680–681 (phase-integral closure + audit), v14.696–699 (gravity-selector compression, eccentricity erratum, audits). Live ledger max before this lane's writes was v14.699. Two additive research-note commits were then made on top of that live head: producer commit \`1c61eed2\`, note commit \`433685d9\`.
**Collision check:** immediately before allocation, live \`master\` was \`433685d9fd75e0aaccf48d3d7abd9306fbb9efda\`, whose parent chain contains v14.699 and only this gravity lane's two new additive research-note commits after it. Repository search returned no v14.700. v14.700 was therefore next-free at write time.
**Status:** substantive gravity-lane gate. This entry corrects a model-combination issue in v14.626, derives exact rank-1/rank-2 response identities in one consistent 3-D rotor model, and identifies a genuine dimensionless G-free physical null observable. The novelty test is **negative**: that observable is standard gradiometry/logarithmic field slope, not a new Cone law. No value of G is derived. No Lane A/Suzuki object, far-tail producer, paper, staged draft, or certified object is modified.

## Deposits

- \`research-notes/Gravity_Rotor_Response_Operators.md\` — git blob \`59832d47d859525023813ae9c9fb7317ef8ab547\`.
- \`research-notes/gravity_rotor_response.py\` — git blob \`8488cf94df3e57b2c7f10559201ea03fd985d897\`.

The producer was run before deposit from the same source text. It verifies the exact rational response identities, reproduces the old planar/Mathieu spectrum, separately diagonalizes the spherical \(m=0\) rotor, and evaluates the G-free field-shape ratio.

## 1. Model-separation correction to v14.626 [D/N]

The rank-1 weights used in v14.626,
\[
w_j=\langle j+1,0|\cos\theta|j,0\rangle
=\frac{j+1}{\sqrt{(2j+1)(2j+3)}},
\]
are the standard **3-D spherical rigid-rotor** matrix elements. The corresponding free spectrum is \(j(j+1)\).

But v14.626 §4 diagonalized
\[
-\partial_\theta^2-\beta\cos\theta
\]
on a circle, i.e. the **planar rotor / Mathieu** model, whose free spectrum is \(n^2\) with doublets
\(0,1,1,4,4,9,\ldots\).

The two models are both legitimate, but they are not one Hamiltonian. The Wigner/Legendre weights of v14.626 §2 and v14.630 therefore must not be combined with the v14.626 §4 Mathieu spectrum as if they described one rotor.

Reproducible numerical separation:
- planar, \(\beta=1\): \(-0.378489221,\ 0.918058177,\ 1.293166283,\ldots\), reproducing v14.626 exactly;
- spherical fixed \(m=0\), \(\beta=1\): \(-0.157663483,\ 2.090760648,\ 6.024031655,\ldots\);
- deep-well first spacing tends to \(\sqrt{2\beta}\) in the planar model but \(2\sqrt{2\beta}\) in fixed \(m=0\) spherical response.

**Correction scope:** the audited Wigner/rank-2 algebra of v14.626/v14.630 remains valid. The correction is the model identification of the §4 spectrum.

## 2. Standard angular-momentum reduction [D]

In one consistent spherical rotor, with \(C=\cos\theta\) and \(P_2=(3C^2-1)/2\),

\[
C|j,m\rangle=a^+_{jm}|j+1,m\rangle+a^-_{jm}|j-1,m\rangle,
\]

\[
(a^+_{jm})^2=
\frac{(j+1)^2-m^2}{(2j+1)(2j+3)},\qquad
(a^-_{jm})^2=
\frac{j^2-m^2}{(2j-1)(2j+1)}.
\]

For \(m=0\), v14.630's direct tidal weight is

\[
v_j=\langle j+2,0|P_2|j,0\rangle
=\frac32\,w_jw_{j+1}.
\]

This is exactly the standard operator identity \(P_2=(3C^2-1)/2\), equivalently ordinary Gaunt/3j/Wigner-Eckart algebra. The rank-1/rank-2 selection structure is therefore established angular-momentum theory, not a new Cone dynamical law.

The diagonal rank-2 element is

\[
d_{jm}
=
\langle j,m|P_2|j,m\rangle
=
\frac{j(j+1)-3m^2}{(2j-1)(2j+3)}
\qquad(j>0),
\]
with \(d_{00}=0\).

## 3. Exact response-operator identity [D]

For
\[
h=J^2/\hbar^2-\beta_1C-\beta_2P_2(C),
\]
the rank-1 second-order static response is

\[
S_{jm}
=
\langle jm|C\,Q(\epsilon_j-h_0)^{-1}Q\,C|jm\rangle
=
\frac{j(j+1)-3m^2}
{2j(j+1)(2j-1)(2j+3)}
\qquad(j>0).
\]

Hence

\[
\boxed{d_{jm}=2j(j+1)S_{jm}}.
\]

Equivalently,

\[
\boxed{
-\left.\frac{\partial\epsilon_{jm}}{\partial\beta_2}\right|_0
=
j(j+1)
\left.\frac{\partial^2\epsilon_{jm}}{\partial\beta_1^2}\right|_0
}
\qquad(j>0).
\]

Producer checks are exact rationals for the tested states, including nonzero \(m\). The \(j=0\) exception is explicit: \(d_{00}=0\), \(S_{00}=-1/6\).

**Novelty status:** useful as an internal calibration/null relation, but entirely standard rigid-rotor response.

## 4. First G-free physical observable from the two channels [D/P]

Let a physical rotor at radius \(R\) sit in a general radial potential \(\Phi(R)\). Let:
- \(I_{\rm kin}\) = kinetic moment of inertia,
- \(Ml\) = pivot-to-COM dipole moment,
- \(q\) = axial quadrupole second-moment coefficient.

To quadrupole order,

\[
U_1=Ml\,\Phi'(R)\cos\theta,
\]

\[
U_2=
\frac{q}{3}
\left(\Phi''(R)-\frac{\Phi'(R)}{R}\right)P_2(\cos\theta).
\]

Thus the dimensionless rotor couplings obey

\[
\beta_1=
\frac{2I_{\rm kin}}{\hbar^2}Ml\,\Phi'(R),
\]

\[
\beta_2=
\frac{2I_{\rm kin}}{\hbar^2}\frac{q}{3}
\left(\frac{\Phi'(R)}{R}-\Phi''(R)\right),
\]

and therefore

\[
\boxed{
\Xi(R)
=
\frac{MlR}{q}\frac{\beta_2}{\beta_1}
=
\frac{1-R\Phi''(R)/\Phi'(R)}{3}
=
\frac{1-d\ln g/d\ln R}{3}
}.
\]

For a Newtonian point source \(\Phi=-A/R\),

\[
\boxed{\Xi=1}
\]

exactly. The amplitude \(A\) cancels; if \(A=GM_s\), both \(G\) and the source mass cancel. More generally, \(\Phi=-A/R^p\) gives \(\Xi=(p+2)/3\).

This satisfies the research objective's dimensional requirement: \(\Xi\) is dimensionless, G-free, and experimentally distinguishable.

**But the novelty result is negative.** \(\Xi\) is just the local gravity-gradient/acceleration logarithmic-slope ratio expressed through the rotor's rank-1/rank-2 spectroscopy. The Cone provides a natural single-device representation, not a new gravitational law.

## 5. Geometry-normalization correction/qualification to v14.630 [D]

v14.630's
\[
U_{\rm tidal}=-(GM_sI/R^3)P_2,\qquad
\beta_2=2GM_sI^2/(\hbar^2R^3)
\]
is exact for an ideal slender axial dumbbell where the relevant quadrupole second moment equals the kinetic perpendicular moment.

For a finite axisymmetric body, if
\[
A=\int z'^2\,dm,\qquad
B=\int x'^2\,dm=\int y'^2\,dm,
\]
then
\[
I_{\rm kin,\perp}=A+B,\qquad q=A-B.
\]

Hence \(q=I_{\rm kin}\) only in the slender limit \(B=0\). A physical double-paraboloid implementation must calibrate \(q\) and \(I_{\rm kin}\) separately.

## 6. Separation of claim types

**Mathematical identities [D]:**
standard SO(3) rank algebra; exact response identity; exact G-free field-shape ratio at dipole+quadrupole order.

**Numerical observations [N]:**
the v14.626 planar spectrum is reproduced; the consistent spherical spectrum differs exactly as expected.

**Interpretive correspondences [I]:**
the Cone paraboloid/fibre picture is a useful organizer of rotor channels; it does not by itself alter the angular-momentum algebra.

**Physical prediction [P]:**
a single calibrated rotor carrying both dipole and quadrupole moments can measure \(\Xi\). Newtonian \(1/R\) predicts \(\Xi=1\); a different radial law predicts a different value.

**Novelty verdict:** negative at this gate. No Cone-specific dimensionless gravitational number or tidal law has survived comparison with established angular-momentum/multipole theory yet.

## 7. v14.696 hypotheses preserved separately

The **separatrix logarithm** remains a valid elliptic-integral asymptotic. Its identification with a gravitational/cosmological hierarchy remains a separate physical hypothesis. Nothing in this gate uses or strengthens that identification.

The **apex/initial-seat construction** remains an interpretive initial-condition hypothesis. Nothing in the rotor-response calculation derives the seat, fixes its value, or converts it into \(G\).

## Scope flags

\`answers_lane_a_handoff = false\`;
\`far_tail_touched = false\`;
\`papers_modified = false\`;
\`certified_objects_modified = false\`;
\`G_derived = false\`;
\`new_dimensionless_observable_found = true\`;
\`observable = Xi_field_slope\`;
\`observable_G_free = true\`;
\`observable_experimentally_distinguishable = true\`;
\`observable_Cone_novel = false\`;
\`rank1_rank2_standard_SO3 = true\`;
\`v14_626_planar_spherical_model_mix = CORRECTED_BY_SEPARATION\`;
\`v14_630_I_squared_normalization = SLENDER_DUMBBELL_ONLY\`;
\`separatrix_log_physical_identification = STILL_HYPOTHESIS\`;
\`apex_seat_physical_identification = STILL_HYPOTHESIS\`.

## Next gate

The next mathematical gate is to build the response from the **actual v14.680 cone phase-integral dynamics**, rather than inserting an ordinary rigid-rotor Hamiltonian, and test whether any correction to \(\Xi\) or to the cross-rank response survives reduction to standard Wigner-Eckart/multipole theory.

A positive result must be a correction not removable by basis choice, conventional multipole expansion, source-geometry calibration, or standard response theory.

---

HANDOFF
target: external-audit
type: independent-verification
parent: v14.700
status: open
action: independently re-derive the planar-vs-spherical model separation; verify the exact \(d_{jm}=2j(j+1)S_{jm}\) identity without using the deposited producer; verify the radial-potential expansion and \(\Xi=[1-R\Phi''/\Phi']/3\), including the finite-body \(q\neq I_{\rm kin}\) qualification. Classify whether any statement exceeds standard angular-momentum/multipole theory.
deliverable: audit verdict with any correction promoted explicitly.
constraints: do not touch Suzuki far-tail objects; do not treat \(\Xi\) as Cone-novel unless a standard-theory obstruction is demonstrated.

HANDOFF
target: sandbox
type: experimental-feasibility
parent: v14.700
status: open
action: estimate whether one realistic rotor can resolve both \(\beta_1\) and \(\beta_2\) well enough to measure \(\Xi\), carrying calibration errors in \(l,q,I_{\rm kin},R\), source geometry, Earth-gradient background, and readout noise. Keep this as an apparatus/null-test study, not a derivation of G.
deliverable: reproducible feasibility producer + negative/positive sensitivity conclusion.
constraints: no Suzuki/far-tail edits; no insertion of measured G into a claimed fundamental prediction; if G is used for engineering signal-size estimates, label it explicitly as calibration-only.
