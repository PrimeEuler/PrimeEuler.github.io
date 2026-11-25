# Area-covariance census: no frame-native object selects covariance/orientation — the variance→area selector route is closed

Sandbox note (little Euler), 2026-11-25. Handoff:
Gravity v15.1469 [NEXT SANDBOX] (Audit R649 /
v15.1474 confirmed), which showed fixed
gravity-sector variance 1/16 does not fix the
EM-accessible area: at trΣ = 1/16 the area-squared
E[(a∧b)²] = 2detΣ runs 0 → 1/512 over the covariance
shape, and at fixed gradient norm V²sin²θ runs
0 → 1/256 over orientation. Scoped test: census
every filed object touching EM area response and
answer the decisive question — does any
frame-native object select the covariance/
orientation data independently of the area it would
then determine? Producer:
`area_covariance_census.py`, 5 checks ALL PASS,
independently re-verifying the load-bearing
arithmetic (C1 = the 1469 identity and extrema;
C2 = the 1401 measure split 3 vs 7; C3 = the 1402
counting split; C4 = the 1467 boost counterexample;
C5 = the 1398 radius cancellation).

## The census

Status key: SUPPLIED = the covariance/orientation
data enters as chosen data (prepared map, initial
data, wave directions, ansatz); CHOSEN-MEASURE =
the area itself changes with a chosen
measure/slicing/congruence; CANCELLED = the
would-be fixing parameter drops out; FORBIDDEN =
the intersector map is obstructed; DECOUPLED = a
canonically selected object exists but provably
does not act on the area.

| object | covariance/orientation status |
|---|---|
| v15.1380 F·B mixing | SUPPLIED (prepared sigma map); λ free; r cancels from B |
| v15.1381 Weyl–F–B operator | SUPPLIED (map must sweep 2 coordinates by choice); ζ/Λ² free |
| v15.1382 on-shell waves (+v15.1384 sign corr.) | SUPPLIED (noncollinearity is the choice of wave directions); ζ free |
| v15.1385 transverse response | SUPPLIED (polarization selection is relative to chosen incoming waves); g_eff undetermined |
| v15.1398 canonical vertex | CANCELLED (r drops out exactly, C5); ζ, Λ, f free |
| v15.1401 shell areas/volumes | CHOSEN-MEASURE (fixed-T 3:1 vs rapidity-cutoff 7:1 vs T-dependent 3+1, C2) |
| v15.1402 state counting | NO MATCH (Hilbert ratio 2; orbit ratio 3 only at D=2, C3); no canonical annulus↔Hilbert map |
| v15.1404 null-affine 3:1, ln2 | SUPPLIED (null line, affine normalization, density chosen; ψ_D contains G) |
| v15.1405 transport weights | CHOSEN-MEASURE (conserved currents give 3:1 → 15:1; forcing 3:1 needs the extra assumption J^U=J^Y=0) |
| v15.1406 null-Q transport | SUPPLIED (κ free, flat connection pure gauge); scalar intertwiner FORBIDDEN (Casimir gap 3D²/4 ⇒ M=0) |
| v15.1407 H² Levi-Civita holonomy | DECOUPLED — see Finding 2 |
| v15.1408 exact chiral loop | DECOUPLED (π/2 holonomy with B ≡ 0, rank-one map); amplitude chosen |
| v15.1409 crossed waves | SUPPLIED (directions/amplitudes chosen); coefficient free |
| v15.1411 corrected current | SUPPLIED (same chosen operator; configuration's special symmetry) |
| v15.1413 Cauchy current (+1412/1414) | SUPPLIED (initial data; coupling arbitrary) |
| v15.1416 coupled variational model | SUPPLIED (g a freely selected frozen coefficient; initial data chosen; r rescales away) |
| v15.1420 full-Weyl characteristics | SUPPLIED (mixing z = gεs with g independently selected) |
| v15.1421 Weyl dimension/variation | STRUCTURAL (no selector; higher-derivative warning) |
| v15.1450–1453 ADM H² initial data | SUPPLIED (constraint data solved from chosen ansatz; κ illustrative) |
| v15.1465 sandbox variance shells | FRAME-TIED (pair variance is a rung label, v15.1467/C4; see §3) |
| v15.1469 variance vs area | THE TRIGGER (trace fixes neither det nor θ) |
| v15.1477 exact Einstein–H² pp-wave | B = 0 as filed; activation needs "independently oriented internal gradients" — SUPPLIED; ε independent freedom |

## Findings

**1. The decisive answer is NO.** No filed object
selects covariance/orientation independently of
the area it would determine. Every entry either
takes the data as chosen input, changes the answer
with a chosen measure, cancels the candidate
fixing parameter, forbids the intersector map, or
decouples from the pullback B. The variance→area
selector route is therefore CLOSED as a clean
negative: variance — pair variance or trΣ — is a
shell/rung label, not a selector. This is
v15.1469's toy-model negative promoted to a census
over the whole filed area line, including the
newest entry (v15.1477, whose own text states the
orientation must be independently supplied).

**2. The one near-miss, named precisely.** The H²
Levi-Civita connection (v15.1407) is the census's
only canonically selected covariant operator — the
target metric fixes it with no free parameter. It
fails the independence test in a specific,
provable way: it transports target tangent vectors,
and v15.1408 exhibits a configuration with its
π/2 holonomy switched ON and the spacetime area
form identically ZERO (rank-one map). A canonical
object that is demonstrably decoupled from B
cannot select the covariance B depends on. Any
future candidate must act on the spacetime
pullback, not only on target geometry.

**3. Reconciliation of Sandbox v15.1465 (additive;
Sandbox corrects its own deposit).** Gravity's
v15.1467 comparator, confirmed by Audit R649, is
right, and this census adopts it: the mass shells
are constant-PRODUCT sections (Q = nk = m²,
boost-invariant); the pair variance X² varies
along a shell (0 at the balanced seat, sinh²η
after boost — C4), so "constant-variance sections"
in v15.1465's title and §3 conflated two
foliations. What survives of v15.1465, unchanged:
identities V1–V7 (Audit-confirmed); offset² as the
pair variance of a CHOSEN pair; 1/4 and 1/16 as the
elementary variances of the ladder's minimum
unbalanced rungs (2,1) and (1, 1/2) — seat/rung
labels in the arithmetic pairing frame, which is
where v15.866's spectral fingerprints live. What
is withdrawn: any reading of those labels as
shell invariants or as a physical graviton shell.
Jeremy's "variance from the photon cone" survives
at exactly this strength: the ladder's minimum-rung
imbalance variance, in the pairing frame, is
1/16 for the gravity sector — a label on the
ladder, not a surface in spacetime. The census's
verdict is consistent with that correction from
the other side: a frame-tied label cannot fix a
frame-independent area.

**4. Reopening condition (exact).** The route
reopens only for an object that (i) is selected by
the existing action/symmetry with no new free
parameter, (ii) acts on the spacetime pullback B
(not only on target tangents), and (iii) fixes
detΣ / orientation before any area is computed —
e.g. an action-selected noncollinear sigma ground
state, or a canonical symplectic flux through the
nested sheets whose density is forced rather than
stipulated (the v15.1401/1402/1405 NEXT items;
their natural candidates — Hilbert counting,
orbit area, conserved currents — are already filed
as non-selecting). Until such an object exists,
EM area response in this frame is enlarged-EFT
data: B from supplied configurations, coupling
ζ/Λ² free, exactly as Gravity's line has reported
at every gate.

Flags: decisive_answer = NO; route = CLOSED
(clean negative); near_miss = LEVI-CIVITA
(v15.1407), decoupled by v15.1408; v15.1465 =
RECONCILED additively (identities stand, shell
phrasing withdrawn); reopening = action-selected,
pullback-acting, parameter-free orientation fixer.
