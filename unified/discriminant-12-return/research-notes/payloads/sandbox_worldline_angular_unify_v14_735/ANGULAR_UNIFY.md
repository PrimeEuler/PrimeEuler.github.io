# Angular-sector unification test — result

Sandbox record, 2026-10-22. Test as posed by the gravity lane and relayed by
Jeremy: *can a single duality-covariant worldline action reproduce both the
electromagnetic Dirac-monopole and the gravitational Taub–NUT angular sectors
while respecting their distinct gauge and diffeomorphism symmetries?*

Producer: `angular_unify_test.py` (runs clean, ~3 s). **Verdict: PASS at the
angular-sector level, with the symmetry difference located exactly — it lives
in what the coefficient s is made of, not in the angular structure.**

## The single object

With canonical (θ, φ, p_θ, p_φ) and twisted covariant momentum
Π_φ = p_φ + s cos θ, one vector formula, parameterised by the single real
number s:

    J = p_θ φ̂ − (Π_φ / sin θ) θ̂ − s n̂
      (mechanical angular momentum − s along n̂)

Verified:
1. **J·n̂ = −s**, exactly (symbolic).
2. **J² = p_θ² + (p_φ + s cos θ)²/sin²θ + s² =: A_s**, exactly (symbolic);
   J_z = p_φ identically.
3. **{J_i, J_j} = +ε_ijk J_k** at 300 random phase-space points (symbolic
   derivatives, numeric evaluation; 900/900 bracket checks, worst deviation
   5.8e-15), and {J_i, A_s} = 0 (float scale). One SU(2), one sign convention,
   for all s.
4. **Taub–NUT:** J(s = 2εl) equals the Killing-triad charges Q_x, Q_y, Q_z of
   `charges.py` at 300 random points with arbitrary numeric f(r): worst
   deviation 7.1e-15.
5. **EM:** A_s at s = eg is the MIC/monopole angular HJ function (gauge
   A_φ = −g cos θ), and the parabolic seats ((k∓s)/2)² specialise to the MIC
   seats at s = eg and to (k/2 ∓ εl)² at s = 2εl (algebra, printed).

So both angular sectors are the Noether theory of one first-order worldline
action — sphere kinetic term plus a Wess–Zumino/minimal-coupling term of
coefficient s — and A_s is its angular Hamiltonian in both backgrounds
(for TN this uses the exact TN−MIC sector identity of `tn_sector.py`).

## Where the distinct symmetries live

The action is shared; the *composition and quantisation of s* is not:

| | EM (Dirac) | Gravity (Taub–NUT) |
|---|---|---|
| s | eg — product of two **couplings** | 2εl — background coupling l × **state variable** ε |
| fiber | internal U(1) circle | spacetime time |
| ε's role | none (e is frozen as a coupling) | ε = −p_t, momentum conjugate to the fiber coordinate |
| symmetry respected | internal gauge invariance | diffeomorphism invariance (action is a spacetime scalar; no dual gauge field appears) |
| quantisation route | string/patch independence ⇒ eg/ħ ∈ (1/2)ℤ — quantises s **directly** | Misner regularity ⇒ t periodic (8πl) ⇒ ε quantised in steps ħ/(4l) — quantises the **fiber momentum**, s only through it |
| fibration weight | 1 (A ⊃ g cos θ dφ) | 2 (χ = dt + 2l cos θ dφ) — the source of the quarter vs the half |

Two consistency notes. (i) s being state-dependent on the gravity side does
not spoil the algebra: in the full phase space ε is the ∂_t charge, the
triad is t-independent, so {ε, J_i} = 0 and the closure above is the full
statement, not a fixed-ε artifact. (ii) The pair-product quarter (k/4)² of
v14.731 is the *conversion* between the two rows: α_G is built from the
fiber momentum at rest (μ) and from M̃ = c²l/G separately, and dividing the
half-lattice statement by that conversion produces the extra factor of 2.
The angular momentum itself stays on the half lattice in both theories, as
SU(2) requires.

## What "duality-covariant" can and cannot mean here

Survives: the angular action depends on the pair only through
**s = (fiber momentum) × (monopole charge) × (fibration weight)**, and in
both theories the period lattice is the single-valuedness condition of
whichever fiber carries the momentum. EM duality (rotate e ↔ g) acts on s
by leaving it invariant — that is the covariance the angular sector sees.

Does not exist: a single duality *group* acting on both sectors alike. EM
duality rotates couplings within one theory; on the gravity side the
would-be dual map moves between backgrounds/solutions, not within a gauge
orbit. The single action respects the distinct symmetries precisely by
keeping the two fibers distinct — internal circle vs spacetime time. (In
the Kaluza–Klein reading of EFT_PATH.md Rung 4b both fibers are spacetime
one dimension up, which is why one formula covers both; in 4D the
distinction is real and the action honours it.)

## Scope

Angular sector only — the test as posed. The radial and boost sectors, the
1PM amplitude, and the field layer remain as scoped in EFT_PATH.md (Rung 1
continues from exactly this action: sphere + WZ term is its angular core).
No new ledger claim is made by this memo; it extends the v14.731 package in
the sandbox.
