# Weak force on the cone — first pass (2026-11-03, sandbox, not ledgered)

Starting point (Jeremy's correction): forget importing the weak force's
groups — the cone already carries **SU(2)** (Schwinger two-mode structure)
and **U(1)** (the common phase / Hopf fiber). Electroweak theory is
SU(2)_L × U(1)_Y. So the honest question is narrower and sharper: does the
cone's native **U(2) = SU(2) × U(1)** reproduce any of the weak force's
*representation structure*, or only its group names?
Code: `weak_force_cone.py` (all tests machine-checked).

## What is present

**1. The U(2) container is native and exact.** On each Schwinger shell of
total number N, the SU(2) algebra closes ([Jx,Jy] = iJz etc., Casimir
j(j+1), j = N/2, errors ≤ 2e-15) and the number operator — the U(1)
phase generator — commutes with all of it. The cone's shells *are* U(2)
representations. This is the electroweak group container, carried natively.

**2. Two SM multiplets are literally shells of the locked tower.**
The cone's U(1) charge is not a free label: on shell j it is locked,
Y = ±N = ±2j (sign = phase orientation). With Q = T3 + Y/2:

- Y = −N, j = ½: charges {0, −1} — **the lepton doublet** (ν, e).
- Y = +N, j = ½: charges {+1, 0} — **the Higgs doublet** (conjugate orientation).
- j = 0: {0} — a neutral singlet.

Every shell's spectrum is a staircase: Y = −N gives Q = 0, −1, …, −2j
(the top state is always neutral); Y = +N gives 0, +1, …, +2j.

**3. The chiral slot exists exactly.** On two spinor copies (L + R),
diag(J, 0) acts as a doublet on L and as zero (singlet) on R — the weak
representation pattern — and diag(J,0) = (V + A)/2 exactly, with V
parity-even, A parity-odd, and parity conjugating the L-form to the
R-form. The V−A structure is representable in cone language.

**4. The charged-current shape is the fundamental shell's.** J+ on the
j = ½ doublet has amplitude exactly 1 — the single unit transition of a
weak doublet. (Central amplitudes on higher half-integer shells are
j + ½, the transition-centered signature from v15.282's discussion.)

**5. The breaking slot exists.** For the Higgs-pattern shell, Q = T3 + Y/2
annihilates the neutral component while T1, T2 move it: a residual
U(1)_Q sits inside the cone's U(2) as the diagonal subgroup — the
algebraic shape of electroweak symmetry breaking.

## What is missing — and it is decisive

**Hypercharge freedom.** The SM's Y is an *independent* label per
multiplet. The cone's lock Y = ±2j therefore fails most of the table:

- quark doublet needs Y = +1/3 at j = ½ — the tower gives ±1. **No quarks.**
- right-handed singlets need Y = −2, +4/3, −2/3 at j = 0 — the tower
  gives 0. Only a sterile/neutral singlet fits.
- the W triplet needs Y = 0 at j = 1 — the tower gives ±2 (charges
  {0,±1} shifted to {0,1,2} or {0,−1,−2}). **No W multiplet.**
- anomaly cancellation (which in the SM works generation by generation
  precisely because quark and lepton hypercharges balance) cannot even
  be stated without the quark assignments.

**Chirality selection.** The projector onto one copy is put in by hand;
parity swaps the copies and the cone selects neither. Also the classic
trap, stated plainly: the bicone's two SU(2) factors are Spin(4)
rotation factors (Lorentz chirality slots); weak SU(2)_L is a *third*,
internal SU(2) acting on left-chiral spinors. Having both kinds of
slots is not identifying them.

**Generations and mixing.** Higher shells are symmetric multi-quantum
excitations of one U(2) tower, not three generations; there is no second
flavor index, no mass basis, no CKM/PMNS matrix.

**Dynamics.** No gauge bosons as fields, no coupling g, no Weinberg
angle (it is the g′/g rotation in the neutral T3–Y plane — the plane
exists, the angle is an occupant), no vev or masses. And a double-
occupancy seam: the cone's U(1) already carries an EM-side reading
(Hopf phase, pair charge quantization); reading it as hypercharge is a
second occupant for the same slot and would need the two readings
reconciled, not just asserted.

## Verdict

Same shape as the gravity thread: **the container is exact, the
occupants are not selected.** The cone natively carries U(2); two of its
locked shells coincide exactly with the lepton and Higgs doublets; the
chiral V−A pattern and the residual-U(1)_Q breaking pattern are
representable slots. But the weak force's actual content — independent
(especially fractional) hypercharges, the chiral choice, three
generations, the mixing angle — is exactly the part the cone does not
supply. Slots ≠ occupants, again.

## Sharpest next test

Give hypercharge a second, independent cone integer: the bicone has two
U(1) phases (one per cone). On *unglued* sectors the two shell numbers
(N1, N2) vary independently, so a combination Y = αN1 + βN2 could in
principle decouple Y from j. Test: does any single (α, β) place the full
SM (j, Y) table — leptons, quarks with their thirds, singlets, Higgs —
on bicone lattice points? If the thirds force α or β fractional with no
cone source, the hypercharge seam is closed negatively, cleanly.

## Bicone test — groundwork (2026-11-03) and run (2026-11-04)

The test splits into three readings. Setup throughout: the weak SU(2)
shell comes from cone A (N_A = 2j), Y = α·N_A + β·m with m the second
U(1)'s label, Q = T3 + Y/2, SM table as in `weak_force_cone.py`.
Code: `bicone_hypercharge.py` (exact Fractions throughout).

**Reading A — j = (N1+N2)/2: CLOSED by counting.** j = 0 forces
(N1, N2) = (0,0), hence Y = 0 — but the right-handed singlets need
Y = −2, +4/3, −2/3. And j = ½ gives Y ∈ {α, β}, only two values for the
three doublets needing {−1, +1/3, +1}.

**Reading B1 — j = N_A/2, second cone a nonnegative shell count
m ≥ 0: CLOSED for all α, β, by the singlets alone.** At N_A = 0,
Y = βm has one sign or is zero, but the singlet hypercharges
{−2, +4/3, −2/3, 0} contain both signs nonzero. (Run spot-check: a
rational grid scan over α, β found 0 pairs placing all four singlets.)

**Reading B2 — m a signed winding, m ∈ ℤ, α, β rational: fits EXIST
but cannot select.** Verified in the run:

- The singlet hypercharge differences {2/3, 4/3, 2, 10/3} have gcd
  exactly 2/3: the difference lattice is (2/3)ℤ. So β must rationally
  divide 2/3 — β = ±2/(3t) for a nonzero integer t — and **no nonzero
  integer β works** (β = 0 impossible).
- For β = −2/(3t), t = ±1, ±2, ±3, with α fixed by the lepton offset
  choice m_L ∈ {−1, 0, +1} via α = −1 − β·m_L, **all 18 family members
  reproduce the full SM table exactly** — every winding integral, every
  Q spectrum, W triplet included. (t = 1, m_L = 0 is the groundwork's
  α = −1, β = −2/3 point: windings L 0, Q −2, H −3, e_R +3, u_R −2,
  d_R +1, singlet 0, W −3.)
- But the family is infinite and unstructured: every t works, α shifts
  freely with m_L, and the singlet windings are mixed-sign in every
  member. Nothing picks t, the sign of β, or α. By the first-pass
  criterion stated above — thirds forcing a fractional coefficient with
  no cone source closes the seam negatively — **this closes the linear
  bicone test negatively**: slots-vs-occupants one level down, not the
  cone supplying hypercharge.

**Natural-1/3-source check: NEGATIVE within the record.** Inventory of
the cone's derived U(1)-type quanta: Hopf fiber Chern number −1
(integer); the pair's phase double cover z ↦ z² (half quanta; φ = 2θ);
dyon/Taub–NUT Misner structure (quarter quanta, pair product (k/4)²,
k ∈ ℤ); the quarter-lattice chain (EM half steps, gravity quarter
steps). Every derived quantum has denominator 1, 2, or 4. A targeted
search of the workspace and memory for any triality / Z3-charge / third
quantum found no relevant hit — the only matches were false positives
(the coefficient symbol Z_3 in the v14.936 counterterm entry, Z_357
identifiers in a replay script, and name fragments inside binary run
files), none of them a charge or triality structure. The only Z3 in sight is arithmetic — the
subgroup 4ℤ/12ℤ of the 12-step phase circle — and no derived charge
uses a 4-step move as its quantum. Signed windings do exist in the
record (Chern numbers and ε orientations are signed), so B2's sign
freedom is not itself the problem; the thirds are.

**One more nail for B2's physical reading:** if |m| were reinterpreted
as a second Schwinger shell number, each multiplet would carry a
second-cone SU(2) spin |m|/2 — e_R would sit at |m| = 3, spin 3/2,
where its actual Lorentz label is (0, ½) — and the label changes with t
anyway (e_R: |m| = 3, 6, 9 for t = 1, 2, 3). A quantity that is not
invariant across the fit family is bookkeeping, not an occupant. And if
the second cone is the bicone's other Spin(4) factor, its shell is
Lorentz data, already occupied — the double-occupancy seam from the
first pass.

**Scope.** These are counting/lattice arguments about the test exactly
as posed — Y linear in the two cone integers, Q = T3 + Y/2, the SM
table above. A nonlinear second-U(1) coupling is outside what was
checked and is NOT closed by this.

**Status of the weak-force thread after the run:** the linear routes
to hypercharge — single-cone lock, bicone symmetric (A), bicone
shell-count (B1), bicone signed winding (B2) — are all closed. What
remains open is only what was never in the test: a nonlinear coupling,
or a thirds source from structure the cone record does not currently
contain (in the SM, the thirds trace to color/GUT structure — and the
cone has no SU(3)). Sandbox origin; ledgered at v15.388.

## The nonlinear door and the SU(3)/thirds door are the same door (2026-11-04)

Jeremy's conjecture, tested in `nonlinear_z3_door.py`: opening the
nonlinear door and attacking the SU(3)/thirds absence directly are the
same move. **Confirmed**, in three exact steps:

**1. Nonlinear dynamics cannot change a charge lattice.** The allowed
charges of a compact U(1) are its characters e^{iqθ}, single-valued on
the circle iff q ∈ ℤ. That is representation theory; no Lagrangian,
linear or nonlinear, enters it. Nonlinear field equations change the
forces *between* charges, never the set of charges. A 1/3-charge
character is single-valued only on the **triple cover** of the circle
(period 6π). So "nonlinear coupling produces thirds" can only ever
mean "replace the circle by its triple cover / quotient by Z3" — a
change of global group structure wearing a dynamics costume.

**2. The SM makes exactly that move, openly.** Its gauge group is
(SU(3)×SU(2)×U(1)_Y)/Z6, and the quotient is the congruence

    y + τ/3 + n2/2 ∈ ℤ,   y = Y/2, τ = color triality, n2 = 2j mod 2,

verified exactly on all eight multiplets. Inverted, the fractional
part of y is *forced* by (τ, n2): the classes are 0, 1/2 (τ=0) and
2/3, 1/6, 1/3, 5/6 (τ≠0). **Thirds appear in hypercharge if and only if
triality is nonzero.** Fractional hypercharge is color triality read
through the quotient — there is no version of the thirds that floats
free of the Z3 grading.

**3. B2 was already smuggling the Z3.** In the bicone fit's canonical
member (s=1, m_L=0), the winding residues m mod 3 equal the required
triality of every multiplet exactly (quarks 1, everything else 0). But
the location of the grading is gauge-dependent bookkeeping: shifting
the α-offset (m_L) breaks the residue equality outright, and rescaling
s moves the extraction rule itself (τ = s⁻¹m mod 3). The fit never
avoided the Z3 — it hid it in a residue, in a non-canonical gauge.

**Where this leaves the cone.** The pattern is now one line: the
cone's covers are 2-power (the spinor double cover z ↦ z² and its
square) — hence its charge denominators are 1, 2, 4. Thirds need the
triple cover, i.e. a Z3-graded sector whose grading correlates with
hypercharge's fractional part. No cone state carries such a grading;
the 3 in discriminant 12 is a ramified prime in the arithmetic, not a
grading on states, and triality is not a function of the cone's
existing multiplet labels (Q shares (j, N_A) = (½, 1) with L and H,
which need τ = 0 while Q needs τ = 1 — any τ on cone states is a *new*
label, i.e. the import itself).

**Verdict:** same door, now precisely located. It is not "nonlinear
U(1) dynamics" and it is not "SU(3) in full" — it is the minimal global
move both names point at: **a Z3 (triality) grading on cone states,
correlated with the U(1) fractional parts.** Find that grading in cone
structure, or the thirds — weak and strong alike — stay outside.
Sandbox origin; ledgered at v15.388.

## Type-conversion check: the parabola's 2/3 cannot become a phase 2/3 (2026-11-04)

Jeremy's correction first: the claim "no natural 2/3 source" was too
strong about the number. The cone has a native exact 2/3, from its own
parabolas, ledgered at v14.592: the segment is exactly 2/3 of its
circumscribing parallelogram; segment area ∝ h^{3/2} (so the Airy comb
runs E_N ∝ (N−1/4)^{2/3}); the evolute of the f=½ parabola is the
semicubical parabola 27X² = 8(Y−1)³, i.e. Y−1 = (3/2)|X|^{2/3}. All
re-verified in `type_conversion_check.py` (segment ratio symbolic;
evolute identity exact). The question was whether that 2/3 can
*convert type* — from area ratio / spectral exponent to charge
quantum — via the dictionary "cone coordinate = action = segment
area, phase = action/ħ." It cannot, and the obstruction is one axiom:

**Additivity.** A U(1) generator eigenvalue must add under composition:
Q(M+N) = Q(M) + Q(N). On the integers that forces Q = cN — linear. Both
2/3 candidates fail outright at 50-digit precision: for the Airy comb,
Q(1)+Q(2) = 2.2777 ≠ Q(3) = 1.9629, and Q(2)/Q(1) = 1.759 ≠ 2; the pure
power N^{2/3} fails the same way (t^{2/3} is strictly subadditive). A
nonlinear function of the index is not a homomorphism, hence not a
charge — no matter how native or exact the number is.

**Phase from area, both directions, confirms where the 2/3 lives.**
Equal height steps: phase increments A(h+1)−A(h) grow like (3/2)√h —
no constant winding-per-shell exists. Equal action steps
(Bohr–Sommerfeld, θ_N = 2πN): the charges are N ∈ ℤ by construction,
and the 2/3 lands on the heights, h_N ∝ N^{2/3}. In every reading the
2/3 attaches to energies, heights, areas — spectral and geometric
quantities — and the phase lattice stays integral.

**Nearest miss.** The evolute cusp is the discriminant locus of a
cubic (4a³ + 27b² = 0 on a = −3t², b = 2t³, exact): loops around it
permute the cubic's three roots — a genuine order-3 monodromy. But it
permutes critical points of an auxiliary cubic; no cone state is a
root of that cubic and nothing transports cone states around the cusp.
A discrete 3 that grades no states is not triality. (Separately, the
concrete Suzuki-side segment-area dictionary already dissolved on its
own terms on 2026-10-18 — the 2/3 warp has no foothold in the
archimedean channel; its home is the bouncer/rotor side.)

**Verdict:** the two 2/3s are different species, now by proof rather
than assertion. The parabola's is a nonlinear spectral/geometric
quantity; hypercharge's β must be a coefficient of additive labels.
The triality door stands exactly where the same-door section put it.
Sandbox origin; ledgered at v15.388.

## The 2D+1 AM-GM extension: the door has a native frame (2026-11-04)

Jeremy's candidate: the k=3 member of his own generalized AM-GM family
(ledger v14.818: k-list product P_k, log-coordinate metric of signature
(1, k−1) — the "1" is the list-sum direction; our cone is k=2, signature
(1,1)). The k=3 member is the "2D+1" object, signature (1,2), symmetry
side U(3). Tested in `amgm_k3_triality.py`. This candidate is different
in kind from everything before it, because it passes the two gates that
killed the others:

**Gate 1 — additivity.** The 3-mode Schwinger shells of the k=3 object
(shell N = symmetric SU(3) irrep (N,0), dim (N+1)(N+2)/2) carry
triality τ = N mod 3 intrinsically: the SU(3) center acts on shell N as
ω^N. And τ is a homomorphism to Z3 — τ adds mod 3 under composition,
exactly, where the parabola's (N−1/4)^{2/3} failed additivity outright.
A grading on states, additive: the species the door requires.
[Correction, 2026-11-04: the grading the embedding in the next
sections actually uses is the *split* grading c mod 3 of the 2+1 mode
split, not this shell-irrep triality — the two differ on half the
multiplets. See the final section.]

**Gate 2 — selection.** The radial coordinate of the k=3 object is the
list AM, S/3. Its fractional part is forced by τ (AM mod 1 = τ/3), and
the coefficient 1/3 is 1/k — fixed by the list length of this family
member. There is no free family: contrast B2's β = −2/(3s), s arbitrary.
The mechanism is the family's own: U(k) = (SU(k)×U(1))/Z_k, so the k=2
cone's Z2 quotient is why its charges lock in halves, and the k=3
member's Z3 quotient manufactures thirds the same way. **The SM's Z6
quotient factorizes over the AM-GM family: Z2 from k=2 (the cone's
existing doublet parity), Z3 from k=3 (triality).**

**Correlation.** With τ = 1 for quarks, 0 for non-quarks, the combined
congruence reproduces every SM multiplet's y-fractional part from
(k=2 parity n2, k=3 triality τ) — all eight match. The τ=2 classes,
unused by SM matter, are exactly the anti-multiplets' fractions
(anti-Q_L: 5/6, anti-u_R: 1/3 — both verified): the grading's third
sector is antimatter's, not an empty slot.

**Scope, plainly.** (i) The 3-mode Schwinger structure gives symmetric
(N,0) shells; full SU(3) (p,q) needs conjugate modes — τ = (p−q) mod 3
stays additive there, but full color is not built, and the SU(3) here
is global/kinematic, the same caveat as the cone's SU(2): no gluons, no
gauge dynamics. (ii) The κCη² criterion (2026-10-28: AM-GM bites only
where the theory forms the list invariantly) is formally met — for the
v14.818 family the list *is* the object — but the physical occupant of
the 3 factors in a matter construction is unidentified (the family's
known occupant side is arithmetic, d_k(N) ↔ ζ(s)^k). (iii) **The
embedding is not built:** each multiplet still needs a k=3 shell
number N_3, with quarks at N_3 ≡ 1 (mod 3) and non-quarks at N_3 ≡ 0.
That residue is the entire remaining input.

**Verdict:** the gap has changed species. Before: invent a grading
(B2's windings — unselected parameters wearing a grading's clothes).
Now: one discrete residue per multiplet, on an object in Jeremy's own
family, whose grading, additivity, and 1/3 normalization are all
intrinsic. A selector-shaped gap still — but the selector now has
something concrete to select *on*. Sandbox origin; ledgered at v15.388.

## Closing the gap (2026-11-04)

Three steps, all in `close_the_gap.py`, exact throughout.

**1. The boundary, proven.** τ is not a function of the k=2 labels —
not of (j, N_A, chirality, dimension) or any combination: L_L and Q_L
share (½, 1, L, 2) with τ = 0 vs 1, and e_R, u_R, d_R (plus the neutral
singlet) share (0, 0, R, 1) with τ = {0, 1}. No derivation of triality
from weak-side data exists, and now that's a theorem of this table,
not an impression. The gap's content was exactly the second sector's
existence — and the sector is the k=3 AM-GM member.

**2. The minimal embedding works.** Read a k=3 shell state by its mode
split (pair modes a,b | third mode c): pair occupation N_A = a+b,
shell N = N_A + c, pair spin j = N_A/2, z = N_A − 2c, triality
c mod 3. Embed each multiplet at c = τ (smallest shell with its
residue). **Every multiplet's slot actually occurs**: L_L and H in
shell 1 at c=0; Q_L in shell 2 at c=1; e_R and the singlet at shell 0;
u_R, d_R in shell 1 at c=1; W in shell 2 at c=0 — pair-state counts
exactly 2j+1 in each case. The multiplets are not assigned abstract
residues; they occupy states of the object.

**3. What closes, and what the residue actually is.** In the combined
(k=2 × k=3) frame, (parity n2, triality τ) forces **Y mod 2
completely, with zero free parameters** — all eight multiplets check.
The thirds gap — the subject of this whole thread, from the singlet
gcd onward — is closed. The residual freedom is exactly integer shifts
Y → Y + 2ℤ per field, and it provably does not close inside the frame:
L_L and H share (j, N_A, c, N, z) = (½, 1, 0, 1, 1) with Y = −1 vs +1;
u_R and d_R share (0, 0, 1, 1, −2) with Y = 4/3 vs −2/3. In the SM,
that integer part is fixed by anomaly cancellation. The cone's
symmetries are global — there is no anomaly machinery here to do that
job, and importing it would be a new construction, not a check.

**Final state of the weak-force thread.** Native U(2) container with
two exact SM shells (pass 1); all linear hypercharge routes closed
(bicone test); nonlinear = SU(3) door identified as the Z3 grading
(same-door); the parabola's native 2/3 proven the wrong species
(type-conversion); the grading found in the k=3 AM-GM member with
additivity and 1/k normalization intrinsic (2D+1); the embedding built
and Y mod 2 forced (this section). Remaining open, cleanly separated:
the integer part of Y per field (anomaly-shaped; no cone analog), the
chiral selection, generations/mixing, and all gauge dynamics. Sandbox
origin; ledgered at v15.388.

## Correction, and the integer door (2026-11-04, later)

`anomaly_integer_parts.py`, exact throughout.

**Correction — which Z3 grading the embedding uses.** The k=3 object
carries two additive Z3 gradings: (i) the (N,0) shell's irrep triality
N mod 3 (equivalently z mod 3; every branching component of a shell
shares it), and (ii) the **split grading** c mod 3 — the third mode's
own Z3 phase diag(1,1,ω) in the 2+1 mode split, with c = (N−z)/3
exactly. The SM's τ slot is filled by (ii): tabulated on the embedded
multiplets, (i) disagrees with τ on L_L (1 vs 0), Q_L (2 vs 1), H, and
W, while (ii) matches everywhere. The k=3 section's "triality"
language should be read as (ii) wherever the embedding is concerned.
No computed result changes — the congruence checks always used τ as
assigned and the embedding was built from c — but the name was wrong,
and the distinction matters: (ii) is a grading of the *split* system
(pair | third mode), intrinsic once the weak pair singles out two of
the three modes.

**The integer door opens — conditionally.** Write the frame's output
as Y_i = r_i + 2n_i (r_i forced, n_i ∈ ℤ unknown) and impose the SM's
per-generation anomaly conditions on the five fermion multiplets.
The system solves exactly: the linear conditions force all ratios,
and the cubic reduces to w² = (6a+1)², giving the complete
anomaly-free family

    Y = t · (Q: 1, L: −3, u: 4, d: −2, e: −6),   t = 2a + 1/3, a ∈ ℤ,

plus the u↔d mirror — verified to satisfy all four anomaly equations
for a = −2…2, both mirrors. Anomalies are homogeneous, so the scale t
is *not* fixed by them. **The anchor is the cone's own**: pass 1's
native lepton shell has Y_L = −1 exactly (its spectrum {0,−1} contains
a neutral member); imposing Y_L = −1 selects a = 0 uniquely from the
tower. The mirror is resolved internally: Q_L's T3 = +½ component has
charge 2/3, and the singlet carrying charge 2/3 is u_R. The Yukawa
ties then fix Y_H = 1 — consistently from all three terms (L–e, Q–d,
Q–u) — and Y_singlet = 0; W's Y = 0 is the gauge-multiplet definition.
**The full SM hypercharge table is recovered, uniquely.**

Imports, named exactly: (1) anomaly cancellation itself — a
consistency condition for a chiral *gauging* that does not exist in
the cone yet; using it is conditional on that gauging being the
intended completion. (2) The color multiplicity 3 in the anomaly
weights — imported from the SM; its candidate native source is the
same k=3 list length, an identification, not a derivation. (3) The
anchor Y_L = −1 — record-internal (pass 1's native shell), not
imported. With those three, the integer part of Y — filed as
unclosable inside the frame — closes from outside it, by consistency.

**Generations: a direction, not an answer.** Under c → c+3 every
frame output (n2, τ, Y mod 2) is invariant, for all multiplets —
the frame has an exact generation-blind direction, matching the SM's
generation-universal hypercharges. Why three generations, and their
masses and mixing, are untouched.

**Doors remaining:** chiral selection; generation count and mixing;
gauge dynamics itself (the anomaly import above is a promissory note
against it). Sandbox origin; ledgered at v15.388.

## More doors (2026-11-04, later still)

`open_more_doors.py`, exact throughout. Four probes:

**A. Antimatter completion — OPENED.** Conjugate multiplets embed in
the b-mode (conjugate) sector with signed third-mode occupation
c → −c: the split grading flips sign, τ → (−τ) mod 3, and the full
anti-table's gradings and y-fractions reproduce exactly (anti-Q at
5/6, anti-u/anti-d at 1/3, all eight). This is where a signed winding
is legitimate — an occupation difference of real modes — in contrast
to B2's bookkeeping. The frame now covers matter and antimatter.

**B. Chirality — located, not opened.** Every equation in the thread
is invariant under flipping all fermion chirality tags L↔R; the tags
are never read by any computation. In-frame, the fermion pattern is
"tag = L iff N_A = 1" — the doublet/singlet split, which the frame
does encode. What it cannot encode is the identification of the
N_A = 1 sector with Lorentz-left: that is a correlation between this
internal frame and the bicone's (½,0) Spin(4) factor, a separate
structure. The chiral door's content is exactly that correlation —
selector-shaped, and now stated in one sentence.

**C. Dynamics probe — a clean negative.** Ŷ is not an operator
identity in the frame: the exact linear system Y = αN_A + βc + γz +
δN over the minimal embedding has no solution (EmptySet), and the
obstruction is one row — e_R sits at the frame origin (0,0,0,0) with
Y = −2, where every generator combination vanishes. The frame +
anomalies + anchor fix Y's *value* per field; Y as an *operator* on
shell states does not exist here. That is the same per-field-label
freedom the SM itself has, in another costume — the dynamics door is
where it genuinely lives.

**D. Scope checks.** (i) The anomaly weight κ=3 is not a frame
multiplicity: shell 2's split branching {(2,0):3, (1,1):2, (0,2):1}
contains exactly one doublet component. κ=3 stays imported, with the
list length k as its only candidate native source. (ii) Generation
slots c = τ + 3g exist for every g ≥ 0 and all multiplets — the frame
gives no generation count; the direction is unbounded.

**Standing doors after this pass:** the chiral correlation (internal
frame × Lorentz bicone); the strong side proper — full (p,q) color
structure via conjugate modes, to the same container-and-labels
standard the weak side now meets; generation count and mixing;
gauge dynamics (couplings, Weinberg angle, Ŷ as operator, masses).
Sandbox origin; ledgered at v15.388.

## The (p,q) color completion (2026-11-04)

`pq_color_completion.py`, exact throughout. The k=3 side is extended
with conjugate modes (a-modes in the 3, b-modes in the 3̄ — the
two-oscillator Schwinger construction): irreps (p,q), dimension
(p+1)(q+1)(p+q+2)/2, Young diagram (p+q, q) with p+2q boxes, irrep
triality (p−q) mod 3 = boxes mod 3, conjugation (p,q)↔(q,p) flipping
triality's sign. The full SM internal table is then assembled in one
frame — field = color (p,q) × weak slot (j, shell, N_A, c, z) × Y —
15 fields: one generation of matter, the antimatter conjugates, H,
W, and the gluon ((1,1), weak-singlet slot, Y=0 — separated from ν_R,
which shares its weak slot, by the color factor alone).

**Headline identity: c = p − q, exactly, on every field.** The weak
slot's signed third-mode occupation equals the color factor's (p−q)
— quarks +1, antiquarks −1, everything else 0, gluons (1,1) → 0
included. Consequently the split grading c mod 3 *is* the color irrep
triality (p−q) mod 3 on the whole table: the two Z3 gradings of the
correction note are one grading seen from the two factors. This also
dissolves the presentational tension from that correction — Q_L's
frame shell (2,0) was always a weak-side slot label; its color (1,0)
is a separate factor, and the two were never in competition. Stated
with its scope: c = p−q is a consistency of the completed assignments
(both sides were built from τ_SM), verified field by field with no
exceptions — not a derivation of one factor from the other. All
Y-fractions re-verify from (n2, c mod 3) inside the completed frame,
and the charge spectra come out right (Q_L: {2/3, −1/3}; W: {1,0,−1}).

**Composites.** Triality is uniform across a tensor product's
components (box count mod 3 is additive; a height-3 column removal
changes boxes by 3), so a product can contain the singlet only if its
total triality vanishes. The standard decompositions check by
dimension and triality: q⊗q̄ = 1⊕8 (mesons), q⊗q = 6⊕3̄ (no singlet),
q⊗q⊗q = 10⊕8⊕8⊕1 (baryons), 8⊗8 = 1⊕8⊕8⊕10⊕10̄⊕27 (glueball
channel open at rep level). Exclusions by box counting alone: single
q, qq, and qqq̄ can never contain a singlet. This is the
representation-theoretic content of the confinement pattern — which
composites *may* be colorless — with no dynamics claimed: no gauge
fields, no confinement mechanism, no running coupling (the Oct 21
session's Λ_QCD territory is untouched).

**State of the whole thread.** The SM's internal label system — color
(p,q) and triality, weak slot and parity, hypercharge fractions and
integers, matter and antimatter, composite singlet rules — is now
reproduced inside one frame built from the cone's k=2 structure and
its AM-GM family's k=3 member, with the imports named at each step
(anomaly consistency, κ=3, the lepton-shell anchor). Standing doors,
unchanged in kind: the chiral correlation (internal frame × Lorentz
bicone), generation count and mixing, and gauge dynamics proper —
couplings, the Weinberg angle, Ŷ as an operator, masses, confinement
as a mechanism. Sandbox origin; ledgered at v15.388.

## "2 SU(3) glued together?" (2026-11-04, evening)

Jeremy's joke, run seriously (`doubled_k3.py`): the bicone was two
SU(2)s glued, so glue two k=3 Schwinger systems — L and R, gradings
(τ_L, τ_R) ∈ Z3×Z3, gluing = restriction to the diagonal SU(3), the
synchronous combination (the L = J+K analog; the difference side is
axial). The construction has a textbook occupant, and its rep content
verifies in doubled-Schwinger language: q_L ∼ (3,1), q_R ∼ (1,3);
the meson sector q̄_L × q_R = (3̄, 3) restricts to 8⊕1 under the
diagonal, and the singlet component is the condensate channel —
⟨q̄q⟩ transforms as (3̄,3), and a VEV in its diagonal-singlet
direction is the glue made physical, a pairing of L-antiquanta with
R-quanta; the baryon sector q_L³ restricts to 10⊕8⊕8⊕1 (rep level;
spin symmetrization decides ground-state occupants); diquarks carry
diagonal triality 2 and hold no singlet; Goldstone count
dim(SU(3)×SU(3)) − dim(SU(3)) = 16 − 8 = 8, the pseudoscalar octet.
So the doubled k=3 *is* chiral flavor symmetry SU(3)_L × SU(3)_R,
spontaneously broken to the diagonal SU(3)_V — the eightfold way.

Species separation, which is the point of filing it: this SU(3)×SU(3)
is **flavor**, acting on (u, d, s) — global and approximate (broken
explicitly by quark masses). It is not the frame's color (p,q), not
the weak SU(2)_L chirality of the standing chiral door (different
L/R), and not the three generations (u, d, s is one generation plus
strangeness). One structural difference from the bicone: there the
doubling is unbroken kinematics (Spin(4), glue = the j₁=j₂ shell
constraint); here the physical realization is broken to the diagonal
and the glue is dynamical (the condensate). Verdict: the doubling
pattern has a k=3 occupant, in flavor space, adjacent to the frame —
it opens none of the standing doors, and the map of what's left is
unchanged: the weak chiral correlation, generation count and mixing,
and gauge dynamics proper. Sandbox origin; ledgered at v15.391.

## What the acceleration-parabola coupling experiments buy here (2026-11-04)

Jeremy asked after the coupling experiments of the dynamics chain
(F=ma atlas; drive × reaction, v15.275; rotor coupling anatomy,
v14.626). Their common anatomy, stated once: a coupling on the cone
is a *number* multiplying a *geometric matrix element*, and in every
experiment the number was imported (e² inside τ₀ of Dirac's reaction
term; g inside the rotor's β) while the geometry returned the matrix
elements, the channel structure (symmetric = kinematics,
antisymmetric = reaction), and parameter-free identities (the
pushback collecting the Larmor power exactly; the duck test's rotor
identity; w_j → ½). Transferred to the completed frame, a gauge
vertex has exactly that shape: g × (generator matrix element), and
the frame fixes every matrix element — J± amplitude 1 on the doublet
(pass 1), the (p,q) Clebsch structure on the color side. So the
dynamics door compresses: everything about the SM's couplings is
frame/representation theory except one number per gauge factor
(g₁, g₂, g₃ — the Weinberg angle is a ratio of two of them) plus the
Higgs/Yukawa sector.

The parameter-free part checks out (`coupling_ratios.py`): the
coupling-structure constants are pure (p,q) arithmetic —
C_F = C₂(1,0) = 4/3, C_A = C₂(1,1) = 3, T_F = ½, and the ratio
C_A/C_F = 9/4, which is what four-jet angular measurements at LEP
actually extracted (gluons radiate 9/4 as strongly as quarks, no free
parameter). Same species as the duck test: identities the structure
gives for free. The residue is equally plain: no experiment in the
record, parabolas included, has ever manufactured a coupling
constant's *value* — α and G stand as the same selector-shaped hole
in their third costume. Sandbox origin; ledgered at v15.391.

## Loop dynamics on the cone — extent assessed (2026-11-04, evening)

Prompted by LHCb's B⁰_d → μ⁺μ⁻ evidence (3.2σ combined, announced
2026-11-03; BF ≈ 1.14×10⁻¹⁰ vs SM ≈ 1.03×10⁻¹⁰) and Jeremy's remark
that loop dynamics should sit on the cone "to some extent pretty
easily." The extent, itemized. **Native species:** (i) loop lines are
propagators, and the cone's native pair is retarded/advanced — the
two parabola families of drive × reaction (v15.275), with the phase
(action winding on the ħ circle) as the accumulated quantity around
a closed circuit; (ii) loop sums are resolvent matrix elements —
spectral sums over shells — and the project's certified tail
discipline (resolvent convergence v15.130/v15.141, the far-shell
work) is the same discipline renormalization imposes. Post-survey
correction (2026-11-04, later evening): for determinants the bridge
is exact, not a rhyme — Γ₁ is a ζ-determinant, and Krein ratios
handle determinant quotients — but everything must be rebuilt in
the exponentiated variable: with λₙ ~ log(n/4) the counting
function is exponential, no Seeley–DeWitt or spectral-action
expansion exists in λ, and the heat trace of e^H is 4^β ζ(β)-type
(primon gas / Bost–Connes). Amplitudes additionally need traces
with insertions Tr[(RV)^k]; no spectral GIM/Inami–Lim exists in
the literature, so that step is new machinery, not a citation. (iii) vertex factors inside loops are the frame's matrix
elements (previous section). **New structural point:** external
states carry a generation *label*, but loop lines *sum* over the
generation direction — the first place in the thread where the
c → c+3 direction is summed rather than labeled. The B_d loop check
(`loop_gim_check.py`): A ∝ Σᵢ λᵢY(xᵢ) over i ∈ {u,c,t}; CKM
unitarity Σλᵢ = 0 (a completeness identity over that direction)
forces A into mass-difference form λ_c(Y_c−Y_u) + λ_t(Y_t−Y_u)
exactly, and degenerate internal masses give A = 0 (GIM). **Not
native:** the weights — with real masses the top term is ~100% of
the amplitude (Y(x_t) = 1.0326 vs charm's 1.1×10⁻⁶ contribution),
and that dominance, the λᵢ (CKM), the coupling prefactors, and the
helicity suppression are all imported-number territory. Verdict:
the loop's *architecture* sits on the cone easily; its *weights* are
the standing doors wearing loop clothes. Sandbox only; not
ledgered.

## Door anatomy I — the chiral door is exactly one bit (2026-11-05)

`chirality_door_anatomy.py`. The chiral door was located in
`open_more_doors.py` §B: every frame equation is invariant under
the global flip of chirality tags, and the un-encoded step is
the correlation between the tags and the bicone's Spin(4)
factors. This build measures the door's exact size. Lorentz
side: Spin(4) = SU(2)_A × SU(2)_B, conjugation swaps the
factors ((½,0)* = (0,½)). A correlation φ assigns tagged-L
fermions to one factor's doublet; there are exactly two
candidates (identity, swap), since the bosons are all
swap-fixed reps — H (0,0), W/gluons (½,½), graviton (1,1).
Both candidates were tested against every internal constraint
on record: Yukawa/Dirac scalar existence for all doublet ×
singlet pairs; the charged current (W inside D × D̄); antimatter
consistency (φ must commute with the frame's conjugation);
the spinor doublet's bicone home being the unordered pair
{(½,0), (0,½)} (v15.140/v15.282); graviton/vector reps being
swap-fixed. **Both φ pass everything.** The two correlations
differ by the global factor swap — Lorentz parity itself.

Verdict: the chiral door's information content is exactly
**one bit**, and no quantity internal to either structure
determines it — the frame's computations never see the tags,
and the bicone's factors enter the record only symmetrically
(gluing j₁ = j₂, pair quantities, swap-fixed boson reps). In
nature the bit is set by weak-interaction parity violation: an
empirical input, not a structural output. With the bit
supplied, every Lorentz representation of the 15 fields + H +
W + G is determined — this correlation is the single remaining
frame↔Lorentz contact point. Caveat, named: a future
factor-asymmetric bicone result would reopen the count; on the
current record the factors are symmetric everywhere they
appear. Sandbox only; ledgered at v15.429.

## Door anatomy II — the generation door is an integer, not a bit (2026-11-05)

`generations_door_anatomy.py`. Same method as door anatomy I:
split everything the frame says about the replica tower
c → c + 3g into outputs (what physical computations read) and
addresses (where a replica sits), for g = 0..4, all fields.
**Outputs are all g-invariant, verified exactly:** slot size
2j+1 constant; τ = c mod 3 constant; Y mod 2 recomputed from
the Z₆ congruence in exact fractions and matched against the
closed table for every replica (note u_R and d_R both give
Y mod 2 = 4/3 — they differ by exactly the frame's residual
2ℤ, as filed at v15.388); and the four per-generation anomaly
sums ([SU(2)]²U(1), [SU(3)]²U(1), [grav]²U(1), U(1)³) vanish
identically — being functions of the closed Y table only, they
are the same for every g and carry zero information about the
count. **Addresses are all that varies:** c, shell N, z, and
the ambient (N,0) shell dimension grow with g; no physical
output reads them.

Verdict: the tower has a canonical base (g = 0 is the minimal
embedding) and an order (g is shell height), but **no length**
— slots exist for all g ≥ 0 with no obstruction at any g, and
no frame output is a function of g. The generation door's
content is therefore a different species from the chiral
door's: not one bit but **one unbounded positive integer**
(the count; 3 in nature) plus the mass/mixing sector, which
the frame cannot even phrase (it has no masses; CKM-weighted
generation sums enter only as imports). There is not even a
symmetry whose breaking would fix the count — the replica
direction is a half-line of identical-output slots, and
nature's 3 is an external datum of integer species. Sandbox
only; ledgered at v15.429.

## Door anatomy III — couplings: the frame knows how they move, not where they are (2026-11-05)

`couplings_door_anatomy.py`. Same method as door anatomies I–II:
compute exactly what the frame determines about the couplings,
and name the residue's species. **Frame-determined (all exact,
from the closed label table):** (a) the trace indices over one
LH generation — S_SU(3) = S_SU(2) = 2, S_(Y/2) = 10/3, ratio
exactly 5/3; the equal-index generator ŷ = √(3/5)·(Y/2) is a
property of the table, not an import. (b) The conditional
rational point sin²θ_W = 3/8 at equal couplings — conditional
on the external assumption of unification. (c) The full
one-loop β vector, in exact fractions: (b₁, b₂, b₃) =
(41/10, −19/6, −7) — the standard SM values as label
arithmetic, and explicitly functions of door II's integer
(b₃(N_g) = −11 + (4/3)N_g): the doors are not independent, the
running knows the count. **Not frame-determined:** the values.
Running the frame's own β coefficients up from the measured
(imported) mZ inputs, the pairwise crossings land at three
different scales (1.0×10¹³, 2.4×10¹⁴, 9.6×10¹⁶ GeV) — the
table itself, given measured values, falsifies exact one-loop
unification; 3/8 is a conditional rational point, not a frame
theorem. And every dimensionless number the frame produces is
rational, while the couplings are not frame-nameable.

Verdict: the coupling door's residue is a third species —
**three real numbers** (g₁, g₂, g₃ at a scale), continuous
empirical data, beside door I's bit and door II's integer —
plus the Higgs/Yukawa reals at the shared border with door
II. Full tally (massless neutrinos): the SM carries 18
continuous inputs (3 gauge + 2 Higgs + 9 masses + 4 CKM) plus
θ_QCD; the frame determines none of the values and all of the
discrete structure they hang on. The frame knows how the
couplings move; where they are is nature's data. Sandbox only;
ledgered at v15.429.

## The k=9 generation fold — door II has a candidate mechanism (2026-11-06)

`k9_generation_fold.py`, run on Jeremy's question whether the
doors could be answered by AM-GM at higher k, more gluing, or
bicone-dipole groupings. The refinement is real family
arithmetic (exact throughout): a k-list's split phase has order
k and grades a distinguished mode's occupation c by c mod k, so
at k=9 the reduction Z9 → Z3 has fibers of size k/3 = 3. The
frame's replica tower (c = τ + 3g) read at k=9 folds to exactly
three classes per τ — distinct for g = 0,1,2, period-3 in g, so
a fourth replica duplicates a class instead of extending the
tower. Selectivity verified: fiber sizes for k = 3,6,9,12,15,18
are 1,2,3,4,5,6 — exactly 3 only at k=9; k not divisible by 3
refines nothing. The fine digit (g mod 3, the second base-3
digit of c mod 9) is gauge-invisible by the frame's own
formulas: the Z6 congruence and the closed Y table read only
the mod-3 shadow, verified for all fields at g = 0,1,2.
Antimatter: conjugation is an exact involution on the 9
classes — τ → −τ mod 3 (as filed at v15.388) and digit
g → −g − [τ>0] mod 3; classes are paired, not digit-fixed (a
first draft of this section overstated digit stability; the
exact law is what is filed). The family's existence at k=9 is
ledgered (v14.818: signature (1,8), seat −9 log 2, d₉ ↔ ζ⁹);
no spacetime reading is claimed for it.

What is NOT established, named as the two hypotheses: (1) the
identification of the frame's third mode with a k=9 list's
distinguished mode — the fold is conditional on it; (2) a
sector that reads the fine digit — the mass sector is the
phenomenological candidate, since generations in nature differ
only there, but no such coupling exists on record. If both
hold, door II's integer is answered by a fiber cardinality —
3 = 9/3, the first generation count in this thread produced
rather than assumed — with the falsifiable shape retained: a
fourth generation would duplicate an existing class in every
digit-reading sector. Sandbox origin; ledgered at v15.461.

## AM-GM 3 squared — the square-root-hyperbola construction at level 3 (2026-11-06)

`amgm3_square_hyperbola.py`, on Jeremy's identification: "its
like the square root hyperbola on the cone." The record's
square-root hyperbola (v15.234 §B; boost grid 2026-10-31):
pairs (u,v), uv = N, label/cone-height GM = √N, lattice points
exactly the factor pairs counted by d₂(N), seat u = v on the
lattice iff N is a perfect square, position = the ratio
coordinate ψ. Run at level k and squared, the construction
gives (all exact): (1) The level-3 product locus xyz = N has
factor triples as its lattice points, counted by d₃(N) — direct
enumeration and Dirichlet convolution agree for N ≤ 60. Its
seat x = y = z is on the lattice iff N is a perfect cube, and
the seat is exactly the AM = GM point of the triple AM-GM;
shell N = 36 carries a k=2 seat (6,6) but no k=3 seat (min AM
10/3 > ∛36) — the two hyperbolas see different balanced points
on one shell. (2) Squaring is self-pairing on the Dirichlet
face: d₂ ⋆ d₂ = d₄ and d₃ ⋆ d₃ = d₆ exactly (N ≤ 60) — the
bicone is the k=2 self-pairing and its (1,3) signature is the
k=4 member's Hessian signature on the analytic face (the
spacetime intertwiner stays open, v14.818); the square of
AM-GM 3 is the k=6 member, whose split grading Z6 is the SM's
own quotient group. (3) The frame's composites are the locus's
factor structures: mesons are factor pairs (3 × 3̄, on the
singlet sublocus), baryons factor triples (singlet iff Στ ≡ 0;
qq and qq q̄ never reach it — v15.388's box counting restated
as locus positions). In fold digits the meson's position along
the locus is σ9 = 3(g − g′) mod 9, τ-independent: π sits at the
seat (0), K⁰ at 6, K̄⁰ and B⁰ at 3, B_s at 6 — the seat is
exactly the flavor-diagonal pairs (the balanced pair, the
condensate channel); the baryon fold class cycles 3, 6, 0, 3
with total generation number mod 3 (p, Λ, Ξ, Ω). Sections 1–2
are unconditional family arithmetic; §3's digit statements
inherit the fold's hypotheses H1/H2 (v15.461), its τ-level
statements are v15.388-solid. Sandbox origin; ledgered at v15.466.

## Could k=9 be a self-tripleting of k=3? — split verdict (2026-11-06)

`k9_self_tripleting.py`, Jeremy's question. On the Dirichlet
face, yes trivially: d₃ ⋆ d₃ ⋆ d₃ = d₉ exactly (N ≤ 40) —
(ζ³)³ = ζ⁹, the same sense in which the bicone's square of k=2
is k=4 (v15.466). On the grading face — the face the fold
(v15.461) spends — no, and the discriminator is element order.
The fold needs the cyclic Z9: the tower step c → c+3 cycles
through three distinct classes because Z9 has order-9 elements
(the class 4 = (τ 1, g 1) has order 9). A tripled k=3 — three
3-lists, or any system read through mod-3 channels — has
grading group Z3×Z3 (relatives) × Z3 (total), exponent 3: the
step c → c+3 is 0 in every mod-3 channel, and generations are
exactly as invisible as at k=3 alone. The fold's 9 is the FLAT
9-list (one list, AM in ninths, U(9) center Z9); its base-3
digits are a reading of that flat class, not a tripling of
systems. What tripling would buy instead: a relative-grading
plane Z3² among three sectors — a different instrument. The
fold generalizes along flat 3^m lists (k=27 adds a third
base-3 digit: fiber 9 over Z3, a fold over the fold).
Sandbox origin; ledgered at v15.467.

## The frame's label set is one class mod 18 (2026-11-06)

`frame_address_mod18.py`. The frame's labels come from three
family members — n₂ (k=2 shadow), τ (k=3 shadow), and under
the fold the generation digit g (k=9 shadow). By CRT
(Z18 ≅ Z2 × Z9) the triple (n₂, τ, g) is the shadow system of
a single class mod 18 = 2·3² — the bicone prime times the
squared triple prime. Verified exactly: the CRT map is a
bijection on the 18 triples; the frame's 24 slots (8 entries ×
3 generations) occupy 12 classes with exactly the v15.388
degeneracies (L_L/H share (1,τ=0) at classes 9, 3, 15 across g;
u_R/d_R share (0,1) at 10, 4, 16; e_R/ν_R/W share (0,0) at 0,
12, 6) — the address is as informative as the frame's label
set, degeneracies included, lifted as always by Y's integer
part. Charges read only the mod-6 shadow (c18 mod 6 recovers
(n₂, τ); the Z6 congruence holds from it alone). Antimatter is
negation: class(antiparticle) = −c18 mod 18 for all 24 slots,
composing the fold's digit law with CRT; the self-conjugate
addresses are exactly {0, 9} — the (τ=0, g=0) slots — split
particle/antiparticle by the sign data, as since v15.388. H1
sharpens: the identification the fold needs is now one
statement — the fields carry addresses in Z18 whose mod-9
component is a real class. Filed discussion: the class is an
address, not an operand — nature's mixing does not add digits
(cyclically, generations 0 and 2 are as adjacent as 0 and 1,
but measured |V_ub|/|V_us| ≈ 1/59, and the two |Δg|=1 elements
themselves differ 5×: mixing follows the tower's linear order
and the mass data). The fold needs distinct classes in an
order, which is what an address is. CRT repackaging
unconditional; physical reading conditional on H1/H2.
Sandbox origin; ledgered at v15.467.

## Hitting H2; factor asymmetry from the pair machinery (2026-11-06)

`h2_factor_asymmetry.py`, Jeremy: "lets hit H2, also, it seems
like we could get factor asymmetry out of this." **H2** (the
fold needs a sector reading the generation digit) is now
characterized exactly: such a sector is a class function on
the Z18 addresses — equal values on same-class slots (a 4th
replica duplicates g=0's value), not factoring through the
mod-6 shadow. Sector tests: (i) the loop sums of v15.394 §4c
are reader-shaped — under the fold their completeness is over
exactly 3 classes, a 4th replica duplicating a term rather
than adding one — with CKM/mass weights still imported;
(ii) nature's one exact three-class relation, the Koide
combination, gives Q = 0.666661 for charged leptons vs the
cone's own 2/3 (v14.592), diff 6.2e-06, inside the τ-mass
uncertainty — the right TYPE of fingerprint this time (a
mass-sector relation, not a charge), filed at coincidence
grade; the quark sectors fail it (0.849 up, 0.731 down,
indicative running masses), so if it is signal it is
lepton-shaped, not universal; (iii) negative: the canonical
operator side cannot currently be asked — no dictionary maps
frame addresses (Schwinger labels) to canonical lattice
modes; the fold is frame-side only. H2 not discharged; its
search space is now a definition with one located candidate
fingerprint. **Factor asymmetry:** on the doubled k=3, signed
pair classes (a, b) carry the swap-with-conjugation involution
S(a,b) = (−b, −a), under which σ9 = a+b is odd and δ9 = a−b is
even. The mesons form swap doublets at fixed δ9, exchanged by
σ9 → −σ9: K⁰ (6,5) ↔ K̄⁰ (3,5); B⁰ (3,8) ↔ B̄⁰ (6,8);
B_s (6,2) ↔ B̄_s (3,2); the pion sits at the seat (0,2),
σ9 = 0, the flavor-diagonal balanced pair (condensate
channel), the only swap-blind class. So the pair machinery
holds factor asymmetry as labeled structure: off-seat pairs
split into two distinct classes the swap exchanges. [I]
Reading for door I: the Spin(4) fermion pair {(½,0),(0,½)} is
the maximally off-seat object of its pair space (one factor
carries the doublet, the other nothing) while every boson is
a seat rep (j,j) — the chiral bit is the SIGN of that
displacement, a coordinate this machinery elsewhere realizes
as a physical label (K⁰ vs K̄⁰). The sign itself remains
nature's datum: the asymmetry has a home here, not a source.
Sandbox origin; ledgered at v15.468.

## The acceleration dynamics IS the 2/3 parabola relation (2026-11-06)

`parabola_dynamics_two_thirds.py`, Jeremy's question: are the
acceleration dynamics associated with the parabolas also the
2/3 relation? Yes — mediated by an identity, not an analogy.
(1) Archimedes holds on the cone's own mesh parabola
T(Y) = Y²/(2u) + u/2: segment/parallelogram = 2/3 exactly for
all heights h and mesh parameters u (symbolic). (2) For
constant force the phase-space orbit is a parabola and the
action is its segment area: the bouncer action is
J(E) = 4√2 E^{3/2}/(3a√m), with the 2/3 entering as
∫₀^h √(h−z) dz = (2/3) h^{3/2} — the segment integral of the
square-root profile (the rectangle splits 2/3 + 1/3 under the
parabola read through its inverse). Quantization
J = 2πħ(n − ¼) turns the exponent into the Airy comb
Eₙ ∝ (n − ¼)^{2/3}, checked against the true Airy zeros
(asymptotic errors −0.76% at n=1 falling to −0.01%).
(3) The acceleration locus — the evolute of the f=½ parabola
y = x²/2, the curve the normal acceleration aims at — is
exactly 27X² = 8(Y−1)³ (symbolic identity 0), the semicubical
parabola of v14.592. So the three faces of the record's 2/3
(quadrature, spectral comb, evolute) are one structure, and
it is the dynamics structure: the mesh is the
constant-acceleration atlas (v15.270s), constant force makes
the orbit a parabola, and the action is the segment area. The
2/3's home type is the dynamics/action sector — where masses
live — which is why it failed as a charge (2026-11-04) and
why a mass-sector relation is its right type of fingerprint
(Koide filing, v15.468, whose type remark this grounds). The
constant is one; the sectors differ. Sandbox origin; ledgered
at v15.469.

## The G-charge fingerprint test — the fingerprint advances (2026-11-06)

`g_charge_fingerprint.py`, Jeremy: "we have acceleration and
EM charge, seems like we could get acceleration of mass
giving us G charge." The EM fingerprint was already in the
record: Larmor P = (2/3)e²a²/c³ and Dirac τ₀ = (2/3)e²/(mc³)
(v15.391, v15.275). Tested where the 2/3 lives and whether
mass matches it. (1) Larmor's 2/3 is an angular moment:
⟨sin²θ⟩ = 2/3 over the sphere, the complement of
⟨cos²θ⟩ = ∫₋₁¹ t² dt/2 = 1/3 — literally the parabola
segment's complementary moment of v15.469 (the sphere's axial
coordinate is uniform, so the sphere moment IS the interval
moment; the radiation pattern 1 − cos²θ is the complement of
the quadratic profile; the two transverse directions of three
radiate). (2) The moments form the family 1/(2k+1): the
segment under y = x^{2k} splits the unit rectangle
1/(2k+1) + 2k/(2k+1) — k=1 the pair profile (1/3 + 2/3),
k=2 the SQUARED profile x⁴ (1/5 + 4/5), k=3 gives 1/7 + 6/7.
(3) Mass has no dipole channel: d/dt² of the mass dipole is
the total momentum's derivative, identically 0 for an isolated
system — the G dipole door is closed by momentum
conservation, not by a small coupling; and "G charge" is mass
itself (pair-dependent α_G in the record; no universal
dimensionless charge). (4) The first open channel is the
quadrupole, carrying the family's next entry: the dumbbell
contraction (the two-body arc's own object) gives Σ(Q⃛ᵢⱼ)² =
8m²ω⁶r⁴ exactly, so P = (8/5)(G/c⁵)m²r⁴ω⁶, which under Kepler
is exactly the Peters value (64/5)G⁴m⁵/(c⁵r⁵) — the /5
entering through the trace-free algebra, the ℓ=2 moment.
Verdict: the fingerprint does not repeat; it advances —
2/3 (pair profile) → 1/5 (squared profile) — which is the
weld's own statement in radiation constants: gravity is the
pair, squared (v14.904), and its radiation fingerprint is the
square of the EM one's profile. Not the same constant, and
not unrelated: consecutive moments 1/(2k+1) of one family.
Sandbox origin; ledgered at v15.470.

## Koide geometry + neutrino test — seat angle exact, lepton law dead (2026-11-06)

`koide_geometry_neutrino.py`, door II as directed by Jeremy.
(1) GEOMETRY (exact): for s = (√m₁, √m₂, √m₃), cos² of the
angle to the democratic axis (1,1,1) is 1/(3Q) — so Koide's
Q = 2/3 says exactly that the root-mass vector sits at 45° to
the axis: the seat angle. Q = 1/3 is the axis (degenerate),
Q = 1 a single axis; the Koide family A(1 + √2 cos(2πk/3 + δ))
has Q = 2/3 ∀δ (verified). (2) CHARGED LEPTONS: measured
angle 44.9997° ± 0.0003° (τ uncertainty) — on the seat-angle
cone; residual phase δ = arg[(1/3)Σ s_k e^{−2πik/3}] (k
ascending e, μ, τ) = 0.22223 rad (12.7328°), band
[0.222221, 0.222238] over m_τ ± 0.12, matching the published
Koide phase; the value 2/9 = 0.22222 lies inside the band
(π/14 = 0.22440 does not) — recorded as a curiosity at
coincidence grade, no endorsement: δ is data (3 masses, 2
parameters, 1 constraint). Amplitude |W|/A = 0.70710 vs the
surface's 1/√2, consistent. (3) NEUTRINO TEST (decisive):
with oscillation data (Δm²₂₁ = 7.4e-5, |Δm²₃ℓ| = 2.51e-3 /
2.49e-3 eV²), Q_ν over all lightest masses caps at 0.5857
(NO, at m₁ = 0) and 0.5000 (IO, at m₃ = 0) — 2/3 is
UNREACHABLE in either ordering (deficits 0.081 / 0.167, far
beyond oscillation uncertainties; the NO maximum is
cosmologically allowed, so the exclusion is Koide's own).
Verdict: as a lepton law the fingerprint is dead; what
survives is a CHARGED-lepton datum (quarks already fail,
v15.468) — exactly the sector of the constant's filed home,
charge × acceleration (v15.470). For H2: the reader's locus
narrows to the charged-lepton mass sector; H2 narrowed, not
discharged — no mass is derived, and δ is one more real
datum (door-III species inside door II's sector).
Sandbox origin; ledgered at v15.472.

## Factor-asymmetry hunt — the bet cashes in form, not effect (2026-11-06)

`factor_asymmetry_hunt.py`, door I at Jeremy's "lets
continue" (his v15.429 bet). Target (v15.468 language): a
swap-ODD output of the cone's own structures — not a label,
not an imported datum. Census, each item checked: (A) GRID —
the node map ((n−k)/2, √(nk), (n+k)/2) under n↔k sends
X → −X and fixes Y, T; families exchange, seat fixed, node
set invariant: exact mirror pair, no asymmetry. (B)
OPERATOR — the frozen formula (dm490/far585/kfull/
DERIVATION.md §0–1) is real throughout (kernel c(mz_N −
Nz_m)/(N²−m²) + 2σp_Np_m, d_N = ln(N/4) + real cos
oscillations; the file's own words: K_full is "a formally
symmetric (real) operator") — a real operator carries no
handedness in its elements; the screw overlay (v13.258) is
not locally inspectable in formula form, and its sense
cannot reach K's elements through a real kernel. (C) SECTOR
CONTENT — certified first gaps differ by parity sector
(v15.227: odd 0.00415063, even 0.01295802), a real content
asymmetry, but the swap acts within the doublet whose home
is the odd sector (v15.282): distinguishing sectors is not
a swap-odd observable. (D) SIDE-PICKS — every dynamical
asymmetry in the record is an occupancy or an arrow:
retardation (past cone only; imported Sommerfeld), NUT
l = 0 (the dyon's magnetic side unoccupied), the cosmic
seat (Sciama B at +½ vs the cone's seat at −½; occupancy),
the chiral bit itself. Verdict: factor-asymmetric results
exist throughout the record, and every one is the bit's own
species — nature picking a side of a mirror pair the cone
supplies. None reopens the count. The sharpened picture:
the bit is one of at least four same-shaped side-picks —
the machinery's recurring transaction is "it supplies the
pair, she picks the side." A genuinely reopening result
needs a swap-odd DYNAMICAL output; the only hiding places
left are the screw overlay's sense (screened from K by
reality) and the absent factor↔mode dictionary (v15.468 §4).
Door I stands at one bit, census attached.
Sandbox origin; ledgered at v15.473.

## The selector — antimatter closure forces k=9; the k=27 rung closed (2026-11-06)

`k27_fold_selector.py`, the open frontier as directed. The
frame is antimatter-complete by its own construction
(v15.388): every slot's conjugate is a slot — at the address
level, the observed tower's class set S_m = {(τ + 3g) mod
3^m} must be closed under negation. Ladder test (capacity
per τ / occupied classes / closed / refines): m=1 (level 3):
1 / 3 / yes / no — collapse, no generation structure; m=2
(level 9): 3 / 9 / YES / yes — closed by EXHAUSTION (the 9
slots are the 9 classes); m=3 (level 27): 9 / 9 of 27 / NO /
yes; m=4 (level 81): 27 / 9 of 81 / NO / yes. m=2 is the
UNIQUE refining level where the tower closes. At k=27 in
detail: only the g=0 τ-flip pair and the origin have
conjugates among the occupied classes — every g > 0 slot's
conjugate lands on one of the 18 empty addresses (at that
reading, antimatter would exist only for the first
generation). The negation digit rule at 27 is v15.461's
borrow rule one digit deeper (verified on all 27 classes).
Consequences: the k=27 rung is CLOSED as a reading level
(capacity grows, occupancy doesn't, closure fails); the
standing address remains Z18. And H1 is upgraded: within
flat readings the level is no longer stipulated — closure
plus refinement force 9, given the observed tower (3
generations, antimatter-complete; both empirical). H1's
remaining content is flatness itself (v15.467: a genuine
flat 9-list, not a tripling). The count is still not
derived from nothing — the tower's observed 3 is an input
to the closure test — but the explanation sharpens: an
antimatter-complete tower that exactly exhausts its
reading level has #slots = level, and the observed 9 slots
(3τ × 3g) admit exactly one refining level, 9 — the only
level where the frame and its antimatter completion
describe the same world.
Sandbox origin; ledgered at v15.474.

## Flatness — the borrow is the signature; H1 collapses into H2 (2026-11-06)

`flatness_borrow_law.py`, door II digging. H1 bundled two
questions: flatness (the digit as second base-3 digit of
the ONE occupation integer — flat Z9 — vs an independent
second Z3, nested Z3×Z3) and reality (H2). The conjugation
law discriminates: on canonical digits, flat conjugation
(−c mod 9) pairs {1↔8, 2↔7, 3↔6, 4↔5} with digit law
d → −d − [τ₀>0] — the BORROW — while nested (componentwise)
conjugation pairs {1↔2, 3↔6, 4↔8, 5↔7} with the borrow-free
law d → −d; the pairings differ on 6 of 8 non-fixed classes.
The frame's conjugation is c → −c on the split-grading
integer (b-sector completion, v15.388), and v15.461
machine-verified the borrow law against it: the frame
follows the flat pairing. A borrow-free digit would need a
second independent grading — a second distinguished mode —
and the frame has exactly one; the digit's step is the
integer's +1 step (one 9-cycle; order-9 classes exist),
which is also the tower's ray structure (base + order,
v15.429). Flatness is therefore the frame's own arithmetic,
not an added hypothesis. (Notation check included: in
signed (τ, γ) coordinates the pairings coincide — the
invariant discriminator is the step/carry structure, which
the canonical-digit borrow exhibits.) Consequence: H1
collapses — flatness (here) + level (forced by closure +
refinement, v15.474) + the digit's reality; the first two
are settled, and the third is H2 verbatim. Door II's two
hypotheses merge into one empirical question: does
anything read the second digit? (Locus: charged-lepton
mass sector, v15.472.) Scope: flatness is settled as a
property of this frame's construction; the frame↔nature
identification remains v15.388's, untouched — if nothing
reads the digit, the operative modulus is 3 and the fold
is bookkeeping, which is H2's question, not H1's.
Sandbox origin; ledgered at v15.478.

## H2 head-on — the joint fingerprint is a prediction (2026-11-06)

`h2_joint_fingerprint.py`, door II's last empirical
question at Jeremy's "lets do it." The candidate reader
carries two target values in one sector — Q = 2/3 (v15.468)
and δ = 2/9 (v15.472) — with one imprecise input,
m_τ = 1776.86 ± 0.12 MeV: an over-determined system.
Solved separately (50-digit): m^(Q) = 1776.96903 MeV, where
δ = 0.222222047 vs 2/9 = 0.222222222 (agreement 1.8e-7);
m^(δ) = 1776.96651 MeV, where Q = 0.666666525 vs 2/3
(agreement 1.4e-7). The roots differ by 0.0025 MeV — ~48×
inside the measurement error — both +0.9σ above the current
central value. Falsification horizon: dQ/dm_τ = 5.6e-5/MeV;
if m_τ's central value stayed at 1776.86 while its error
shrank to 0.02 MeV, Q would miss 2/3 by 5.5σ — the joint
fingerprint is decidable at σ(m_τ) ≈ 0.02–0.03 MeV, with
kill condition: m_τ settling outside ≈1776.97 ± 0.03 at
that resolution kills both targets together. Sector census
completed to (θ, δ) with pre-registered candidates (record's
indicative quark masses): up (51.20°, 0.0744 rad), down
(47.54°, 0.1102 rad) hit nothing; leptons alone sit on the
seat angle with a candidate-hitting phase — the fingerprint
is charged-lepton only in both coordinates. Verdict: H2 is
neither discharged nor killed; it is now a PREDICTION.
Coincidence grade retained — selection effects stated
(2/9 was noticed from the data) — but the joint consistency
is a fact of the numbers: two independently noticed target
values are simultaneously satisfiable at one m_τ, with
cross-agreements at the 1e-7 level, far beyond what either
near-miss alone asserts. Door II's last question now waits
on a measurement (an m_τ refinement), not on more
machinery.
Sandbox origin; ledgered at v15.479.

## Screw handedness — the last hiding place is closed (2026-11-06)

`screw_handedness.py`, door I at Jeremy's pick (the screw
overlay, v15.473's named gap). The screw has two faces in
the record and they were kept separate. FACE 1 (Laplace,
v13.258): Φ₁₂ from the entry's own formula — genuinely
one-sided: the prime ramps are absent for −t (R₁₂(−t) = 0
exactly), Φ₁₂(+t) real (0.416, 0.259, 0.498 at t = 1, 3, 6),
and the archimedean term is a half-line formula whose naive
continuation off the half-line is non-real (Lerch branch) —
the mirror isn't an alternative real function awaiting a
choice. What the mirror prescription gives is fixed by the
functional equation: L(1/2 + iz) = −L(1/2 − iz) identically
(verified on the actual ξ₁₂ to machine precision), so the
mirrored transform is −g_F — the same object negated, its
positivity criterion destroyed, not an opposite handedness.
The recorded sign is the Euler-product side's; the
asymmetry species is the transform's arrow (retardation,
censused v15.473) on the log-scale axis — not a spatial
winding. FACE 2 (helix, v13.753): the screw function there
is real and EVEN, and its increment kernel — the Weil
kernel — is invariant under the rapidity reflection
(u, v) → (−u, −v) by two lines of algebra from evenness
(verified); the Fourier-convention sign cancels on even
spectral weight (v13.753 itself: "no residual sign"). The
helix's two winding directions carry the same kernel.
Verdict: no handedness survives in either face; door I's
screw hiding place is CLOSED. With v15.473, the bet stands
fully resolved — side-picks everywhere, a swap-odd output
nowhere: not in the grid, the operator, the sectors, or
the screw. The only remaining hiding place in the whole
census is the absent frame↔canonical dictionary
(v15.468 §4).
Sandbox origin; ledgered at v15.481.

## The dictionary hole, scoped — no residue anchor (2026-11-06)

`dictionary_scoping.py`, at Jeremy's direction (Lane A
works FULL_K; the sandbox approaches from the hole). The
two sides' arithmetic is different in species: the frame's
labels are RESIDUES (addresses mod 18 = 2·3²; τ a mod-3
residue, the digit mod-9), while the operator's frozen
data (SEED_FORMULA v14.819 / DERIVATION §0) is built from
FREQUENCIES: z_m = Σ_{q∈{2,3,4,5,7}} 2w_q sin(θ_q m) + π/2
+ O(1/m) and d_n = log(n/4) + cusp − Σ w_q(2−log q)[cos +
...], with w_q = log q/√q and θ_q = (π/2) log q. Probe:
residue-class means of the seed's oscillatory part decay
to a common limit (mod-3 spread 0.0105 → 0.0030 → 0.0001 →
0.0000 for ranges 1e3–1e6; mod-9 likewise), while a true
period-3 control sits stable at (0, ±0.866) — the probe
can see a residue signal, and there is none. Frequency
census: projections recover exactly the five weights w_q
at the log-frequencies and sit at the leakage floor
(≤ 4e-5) at f = 1/3, 1/9, 2/9, 1/2. The operator's "3" is
the frequency log 3; the frame's "3" is the residue mod 3.
The one exact residue signal in the operator's data is
period 2 (the cusp's (−1)^n term; the sector split
itself) — the frame's Z2 side, where the record's one
exact label contact already lives (sector parity ↔
spinor/boson home, v15.135–143). Existing bridges are
logarithmic or pair-level: the station lattice (u_n =
log n = 2ψ_n, v14.416) and the weld's node = state pair
identification (v14.904). A slot dictionary would need a
frequency→residue conversion with no anchor in the data,
or a construction — barred from provenance by the
admissibility fence (v14.942) and the v15.125 absence. If
frame labels live on the operator side at all, it is at
the BILINEAR level: the kernel K_{N,M} as a function of
the pair (N, M) — i.e. of (T, X) = ((N+M)/2, (N−M)/2), the
Schwinger pair coordinates — where the weld already
lives, and where Lane A's FULL_K work is pointed from
the other side.
Sandbox origin; ledgered at v15.482.

## The bilinear level, checked — geometry yes, labels no (2026-11-06)

`bilinear_check.py`, Jeremy: "lets check it out." The
frozen kernel on same-parity pairs, in the grid node's
own coordinates (T = (N+M)/2 shell/AM, X = (N−M)/2 offset,
Y = √(NM) GM, cosh ψ = T/Y), decomposes EXACTLY (verified
to 2e-16): K = −1/(2T) + 2σ p_N p_M + c(M·osc_N −
N·osc_M)/(4XT). Anatomy: the pole term is a GM law
(p_N p_M/(L²/Y²) → 1, amplitudes 2σL² = +4.12 even /
−0.88 odd — sector sign AND size); the drift −1/(2T) is a
pure shell function; both smooth terms are subdominant at
range to the third term — a 1/X Hilbert-band term
carrying the five log-frequencies (RMS ≈ 0.41 at X = 1,
T-independent at fixed X, decaying ~1/X). The dictionary
question at this level: pair-residue probe on that band
term (the only place labels could hide) — class-mean
spreads at the random-binning null scale (~1e-4) in every
binning (X mod 3, T mod 3, X mod 9, (N,M) mod 3), both
sectors. Verdict: the bilinear level is inhabited, by
pair GEOMETRY — (T, X, Y, ψ) are the kernel's own
coordinates, the level the weld occupies — while the
discrete label layer (τ, digit residues) is absent here
too. With v15.482 (mode level), the frame's label layer
has no anchor anywhere in the operator's construction
data; the only unprobed territory left is the operator's
SPECTRUM (Lane A's certified objects), where a residue
pattern would be a discovery, not a dictionary entry.
Sandbox only; not ledgered.
