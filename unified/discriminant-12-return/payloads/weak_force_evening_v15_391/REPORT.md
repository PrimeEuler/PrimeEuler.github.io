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
cone has no SU(3)). Sandbox only; not ledgered.

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
Sandbox only; not ledgered.

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
Sandbox only; not ledgered.

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
something concrete to select *on*. Sandbox only; not ledgered.

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
only; not ledgered.

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
against it). Sandbox only; not ledgered.

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
Sandbox only; not ledgered.

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
as a mechanism. Sandbox only; not ledgered.

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
and gauge dynamics proper. Sandbox only; not ledgered.

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
in their third costume. Sandbox only; not ledgered.

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
