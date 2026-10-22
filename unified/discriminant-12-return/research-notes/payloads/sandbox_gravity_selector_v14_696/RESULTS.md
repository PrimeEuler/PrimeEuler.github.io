# Gravity as e's monopole partner — sandbox test (2026-10-21)

**Jeremy's sketch:** gravity causes the quantization of e; gravity is
the monopole pair with e; the non-degeneracy of the Larmor precession
is the balancing point of G and e. **Status:** sandbox, NOT ledgered.
Producer: `pair_test.py` (scipy.constants).

## A) Pairing arithmetic — anchors verified, no small-n lock

- Dirac number D = e²/(4πε₀ G m_e m_p) = 2.268661e+39;
  ψ = ½ ln D = **45.310004305** — reproduces v14.621 to all digits.
- α_G,e = (m_e/M_Pl)² = 1.751809e-45; depth ½|ln α_G,e| = 51.52784 —
  reproduces the gravity-arc values.
- The true monopole pair locks a product: eg = ħ/2 (n = 1) gives
  α_m = 1/(4α) = 34.2590, i.e. **α · α_m = 1/4 exactly** — the pair
  product is a small rational.
- The (e, G) pair as measured locks nothing small:
  α/α_G,e = 4.166e+42. If gravity is e's partner, the pair's "n" is
  the hierarchy itself (fork branch 2), not a countable integer.

## B) Shell loop budget — an exact two-sector partition [D, definitional]

On the shell S²_T at ring T = j+½, latitude X = m+½, a Larmor loop's
phase budget splits into exactly two fractions:

- pointing (e-side): cos α = (m+½)/(j+½);
- holonomy (curvature / G-side): enclosed solid angle / 2π
  = (j−m)/(j+½) = 1 − cos α.

Sum = 1 on every loop, all (j, m), j ≤ 3 tabulated. Honest weight:
this is the definition of a latitude cap's solid angle — it falls
out trivially once the fractions are named. Its content is
structural, not numerical: the shell's loop budget has exactly two
sectors, winding/pointing and curvature/holonomy, with no third
term — so a G↔e balance stated on the shell has exactly the two
slots Jeremy named (the precession and the curvature) and nowhere
else to live. No constants enter; B alone couples nothing to G.

## C) Hydrogen's two precessions — negative as a selector

Per orbit (n = 1, circular): GR perihelion advance
6πGm_p/(c²a₀) = 4.42e-43 rad; spin-orbit precession at scale
πα² ≈ 1.67e-04 rad (order-of-magnitude — the per-orbit SO angle
carries order-unity factors not resolved here). Ratio ≈ 2.6e-39,
½|ln ratio| = 44.41 vs ψ = 45.31: near the Dirac neighborhood but
not a lock, and the proximity is arithmetic ancestry (both
precessions are built from the same α, α_G, m_p/m_e) — not a
balance condition. Clean negative: the selector is not in the
precession ratio either (consistent with v14.627's negative scans
of the step-arithmetic hunting ground).

## What fell out

1. The monopole dictionary is structurally sound: Dirac's mechanism
   (single-valuedness of the phase around the partner) is the same
   mechanism as the program's ħ-circle anchor (v14.620), and the
   shell provably carries the two sectors such a pairing would
   need (B).
2. No product law falls out: as measured, the (e, G) pair carries
   the full hierarchy in every pairing tried (A, C). If the pairing
   is real, its quantum is e^{2ψ}-scaled — the selector question
   reappears as "why that count," unchanged and still open.

## Addendum (same evening) — the proton pushing back (recoil test)

Producer `recoil_test.py`. Jeremy asked whether the counts take in
the proton's back-action, and wanted the difference quantified:
(a) Spectrum: two-body E1 = −13.598287 eV vs fixed-proton −13.605693
— difference 0.007406 eV (rel 5.44e-4), the reduced-mass shift
already inside the v14.680 closure via μ. (b) GR perihelion per
orbit: two-body value identical to one-body at leading order —
ratio 1.000000000000, difference exactly zero, because the source
mass (m_e+m_p) and the orbit scale (a_rel from μ) shift by the same
(1+m_e/m_p) factor and cancel; next corrections ~3e-8 relative.
The proton's own barycentric orbit is a 2.88e-14 m scaled copy with
the same advance angle. (c) Reciprocal spin precession: the
hyperfine beat, 1420.405751768 MHz = 5.874 μeV; the proton precesses
in the electron's field slower than the electron in its field by
μ_p/μ_e = 1/658.2. (d) Pairing arithmetic: m_e → μ shifts the α_G
depth by 2.7e-4 — nothing. Verdict: the one-body counts stand; the
only place the proton's push is already load-bearing is μ in the
spectrum.

## Selector model (same evening) — built to the spec sheet

Producer `selector_model.py`. Spec: (1) single-valuedness form,
(2) seated in the loop budget's two sectors, (3) hierarchy-size
quantum, (4) dimensionless, G-free, pair-dependent.
Candidate: per-loop phase imbalance (p−h) on the shell loop at
(j+½, m+½); closure count N = 1/|p−h| = (j+½)/|2m−j+½|.
Findings: (i) one shell gives only small rationals — quality (3)
fails at shell scale, in-model proof that no single shell hosts
the selector. (ii) [D, exact] at the most-balanced state of each
shell (|p−h| minimal = 1/(2j+1)) the closure count is exactly
N = 2j+1, the multiplet dimension. (iii) Compounding to ψ:
conductor-chain secant rapidities sum to 0.78 (nowhere); ladder of
m=0 loop sector-ratio rapidities crosses ψ at K=29 shells (sum
45.679, step size there ~2 — a scale datum, NOT a match: chain
rule and stopping point are free choices, so this is chance-level
by the program's own small-rational discipline); (4/3)-steps need
315 (v14.627). Portrait: a qualifying selector = a winding-closure
count compounded over a chain; the compounding length is
rule-dependent (~29 shells / 315 steps / 1e39 raw objects), so the
selector's identity IS its enumerator — and the enumerator is the
still-empty slot. In Sciama's frame the enumerator is the contents
of the universe; the cone has no forced enumerator of that length.

## List model (same evening) — modeling the enumerator

Producer `list_model.py`; rules fixed before totals were read.
(i) Balanced-ladder rapidities telescope exactly: total(J) =
½ ln(J+1) — at J=42 only 1.88; a fitting list of this family needs
J+1 = e^{2ψ} = D links: the list that fits IS the Dirac number read
as a count (Dirac's large-numbers inventory in cone dress).
(ii) Closure-count accumulation Π(2j+1): crosses 2ψ mid-step at
j=29 (89.10 → 93.18; links ~4 wide there) — no terminus fits;
J=12 gives 29.70, J=42 gives 148.88. (iii) The cone's native finite
lists all land at 17–20: helix 12-node list ln(11!) = 17.50;
conductor list Σ ln(1/s) = 18.42, Σ|C₁| = 19.68. Verdict: the
cone's own inventories top out near e^20 in count; the selector
needs e^90.6. The enumerator gap is itself hierarchy-scale
(~e^70). Crossings at depth ~29–30 are generic (K ln K ≈ 90 there
for any ladder growth) and fit nothing to precision.

## Completing the last step (same evening) — the completion problem, posed

Producer `completion.py`. Criterion established first: a completion
must be a SMALL-INTEGER or TOPOLOGICAL closure on the inventory,
because the generic alternative dies quantitatively — phase closure
on the one worldline's total phase (Phi ~ 3e118 rad) has solutions
spaced dN/N ~ 2e-118: at cosmic phase scales the integers are
dense and a winding condition selects nothing. (Dirac's eg = n hbar/2
works because n is small.)
Drift finding: with modern constants sqrt(N_pairs)/D = 4.17, NOT 1 —
Dirac's census coincidence was calibrated on his era's H0; the
ratio is epoch-dependent and has moved. Completions must predict
the ratio, not assume sqrt(N) = D; polishing the census is dead.
Surviving closure: the tangency B = G M_u/(R_u c^2) = Omega/2,
closed at exactly 1/2 iff Omega = 1 — the Hubble volume at its own
Schwarzschild tangency (discriminant-zero; the same species as
every exact closure in the program). It makes the Sciama balance
exact and fixes all ratios, but the count's magnitude remains
exactly ONE free integer (ontologically exact: net baryon number;
knowable only by census). Final shape of the last step: an
exponentiating map from the cone's discrete data to that one
integer, with a FORCED terminus. Ladder products reach ln D at
29 shells and ln N_pairs at 50 shells — both generic K ln K
crossings (scale data only); shell-state census (J+1)^2 needs
J ~ 1e40 (no small J). No forced terminus found tonight.

## Gemini relay assessed (same evening) — the Pell-unit riff

TRUE: eps_12 = 2+sqrt(3) is the discriminant-12 fundamental unit
(norm 1 in Q(sqrt(3)), the program's own genus field); the displayed
form's discriminant is 12; 29 is the Pell number P_5. FALSE: "29 is
the denominator generator of sqrt(3)" — 41^2 - 2*29^2 = -1 puts 29
in sqrt(2)'s convergents; 29 appears in no sqrt(3) convergent
(unit solutions (2,1),(7,4),(26,15),(97,56)); our 29 came from the
prod(2j+1) ladder, a third object. EMPTY: the trace formula
(M_tangency, k(shells) undefined), "50-shell coupling defines the
exact exponent base" (no base named). TESTED: D =? eps^k gives
k=68.81 (nearest power off by x1.28); census k=139.79 (off x1.32);
mutually inconsistent by eps^2=13.9x (the drift again); eps-powers
spaced 1.317 in log make gaps of 0.25 the chance floor. KEPT: the
unit group of the discriminant's own order is the most native home
yet proposed for the exponentiating map; the open slot refines to:
a FORCED exponent. Cone-owned exponents 29/42/50 land at logs
38.2/55.3/65.9 — nothing. Not recorded in the ledger.

## Gemini follow-up assessed (same morning)
Concession on the sqrt(3) link, the empty trace formula, and the
spacing trap: accurate. New claim — that 29/42/50 x ln eps
"matching" 38.2/55.3/65.9 is a structural alignment — is a
tautology: those logs were COMPUTED as k ln eps; agreement with
our own arithmetic is not agreement with a target (psi, depths,
2psi, ln N — none equals 38.19/55.31/65.85). A selector also needs
ONE forced k; three harvested crossings are a menu. Bridge test
(offered by the relay, run): tiers are 10^16.6, 10^24.0, 10^28.6 —
largest ~51 orders below N_B; index sum 121 gives log 159.4 vs
ln N = 184.1. Nothing bridges. eps-exponentiator stays on the
board as most native candidate; verdict unchanged.

## The forced-k hunt (2026-10-22 morning, Jeremy's line "lets hunt it")
Pre-registered candidates (native integers with constructions:
phi(12), helix radius/antinodes/nodes, channel counts and
conductor sums, sum U(12), Y^2 max, K, moments, sum q, n^2) x
targets (psi, depths, 2psi, ln(1/aG) both masses, ln N_pairs):
NO candidate within 2.10 in log of any target (best: k=36 -> 47.41
vs psi, gap 2.10; k=42 gap 3.78; k=144 gap 5.55). The one genuinely
forced construction, ord of eps in (Z[sqrt(3)]/m) for m=12, 24,
equals 12 — canonical, elegant, scale-free: matches nothing.
Exact trace predictions logged for falsifiability: Tr(eps^139) =
3.167445e79, Tr(eps^140) = 1.182107e80; the eta-census 8.94e79
falls BETWEEN consecutive traces (ratios 0.35 / 1.32) — no integer
k matches the census. Verdict: the native-integer family is
CLOSED as a source of forced k; the eps-map survives only as two
exact, testable predictions that currently miss.

## Gemini dichotomy assessed (same morning) — both horns are one horn
Horn 1 (trace-weighted average): required weight on tr(g^140) is
0.667 — a free real in (0,1) that exists for ANY bracketed census;
fitted, it destroys the falsifiability that made the prediction
interesting. Not dressed as 2/3. Horn 2 (missing 30%): the census
is density x CHOSEN volume, not an observable. Particle-horizon
volume: census between tr 139/140. Hubble volume (the tangency's
own radius, B = Omega/2 at R = c/H): census 2.72e78, nearest trace
tr(g^137) = 2.274e78, ratio 1.20. The bracketing k swings 137-140
on convention alone; the count moves x33 across standard volumes,
swamping the x1.32 miss. Dirac ratio sqrt(N)/D by convention:
4.17 (particle horizon) vs 0.73 (Hubble) — the log-gap flips sign.
Residue: the trace thread's fate is a VOLUME-FIXING principle;
the tangency is the only candidate and points at the Hubble
volume, where the miss is 20% — closer, not a lock, and that
volume was chosen knowing the neighborhood (shopping discount
applies). Permitted, not selected.

## Correction (Jeremy, same morning): the Planck yardstick is circular
l_P = sqrt(hbar G / c^3) contains G — quoting R_H/l_P ~ 1e61 as
"the scale to be fixed" embeds the unknown in the yardstick.
Restated G-free (hbar, c, e, masses only): R_H/a0 = 2.60e36
(ln 83.85, required k = 63.67); t_U/t_atomic = 4.63e40 (ln 93.64,
k = 71.11); N_pairs ln 184.09 (k = 139.79). Verdict unchanged —
no integral k — but the spec sharpens: psi and D are themselves
G-laden; an admissible selector may not output psi. It must output
a G-free count or ratio (N, R_H/a0, t_U/t_pair); G then follows
through the Sciama balance. The ledger's alpha_G-as-input framing
knew this from one side; the correction states it from the other.

## Temporal bridge (2026-10-22, Jeremy's idea): counting J states in time
Built three ways. (V1) Pair clocks ticked over the age (G-free
counts): hyperfine 6.19e26 (ln 61.69), orbital 2.87e33 (ln 77.04),
Compton phase 3.38e38 (ln 88.72) — none is a G-free target.
(V2) Temporal trace sums collapse to the last tick (factor
eps/(eps-1) = 1.58, a third of an index step): summing over time
creates no new integer. (V3) The bridge converts the missing
exponent into a missing TICK COUNT: landing on the census needs
K = 140 ticks of ~9.9e7 yr; on D, 69 ticks of ~2.0e8 yr. The
pair's clocks run 1e-16..1e-9 s — nothing in the pair ticks at
1e8 yr; the needed tick is a cosmic period. Yield: the temporal
selector IS a census-age law (the LNH form) — the bridge shows
the river is the age-census relation itself.

## Eccentricity (2026-10-22, Jeremy's reframing)
The cone's only PROVEN dynamics is the phase-angle integration
(v14.680 Test D); every selector candidate hunted this week was a
count, not a property of that dynamics. The phase orbit carries a
continuous parameter: eccentricity — in the bicone it is the L/A
split on the shell (L^2 + A^2 fixed, |A| ~ e, Runge-Lenz), and
slicing the cone generates all e. Test (lobes-coulomb/
eccentric_test.py): squashing the orbit by the Kepler factor
rho = sqrt((1-e)/(1+e)) deforms the integral NON-trivially — at
e = 0.6 the ratio to any reparametrized Legendre function is
theta-dependent, while e = 0 reproduces the exact constants.
So the quantum lobes are the e = 0 member of a one-parameter
family the phase integral generates (Hansen/Bessel sideband
structure classically). Eccentricity passes the selector spec —
dimensionless, G-free, pair-dependent — and is the first
candidate from the DYNAMICS rather than the inventory. Open:
what fixes e — the conic family's own discriminant-zero sits at
the parabolic slice e = 1, but for which orbit, giving what
number, is not yet a computation.

## Separatrix log machine assessed (2026-10-22, Gemini relay)
The K(e) ~ (1/2) ln(16/(1-e^2)) asymptotic is correct, and the
mechanism is theorem-grade: period divergence at a separatrix is
how dynamics manufactures large logs (home in-program: the rotor /
quantum-pendulum separatrix, v14.626). Calibration: the machine
RELOCATES the hierarchy — psi requires 1-e^2 = 7.05e-39, a
proximity exactly as unexplained as D. Fed the pair's own
gravitational smallness (Test C): K = 45.80 (ratio input) / 50.15
(perihelion input) vs psi 45.31 / depth_e 51.53 — the chance swamp
(gaps 0.5-1.4), noted not sold. The relocation becomes a
selection only via DWELL: period divergence makes the orbit spend
a log-divergent share of its time near the separatrix, so a
TIME-WEIGHTED J-state census (Jeremy's temporal bridge) is
dominated by near-tangency states. Open slot, final form: compute
1-e^2 for the frame's fundamental phase orbit from the frame, or
prove the dwell weighting sets the census's effective log.

## The open slot, filled structurally (2026-10-22, Jeremy: "lets fill the open slot")
[D] Identification: e^2 = A^2/(L^2+A^2) on the bicone shell, so
1-e^2 = the shell's angular share; the separatrix e=1 IS the
radial orbit L=0. Frame quantization (Langer fraction
(1.5/n)^2 for the closest orbit) + dwell weighting over shells
to J=42 gives K ~ 4.2-4.7 — the mechanism runs inside the frame
but outputs ln J, single digits: pure-frame fill NEGATIVE.
[D] Cosmic orbit: the expansion's eccentricity IS the flatness
parameter; Omega=1 is the parabolic slice, and today's tangency
B = Omega/2 = 1/2 seats the expansion at the separatrix.
Inflation manufactures the proximity, 1-e^2 -> (1-e^2)_i e^{-2N},
hence the closed form K(e) = N + (1/2) ln(16/(1-e^2)_i): the
hierarchy log = the e-fold count + the initial seat's half-log.
Required N: psi -> 43.9, depth_e -> 50.1, age-ratio -> 69.7,
ln(R_H/a0) -> 82.5; standard flatness N ~ 60 (K = 61.4) — same
band, no exact seat (value-level swamp persists). SLOT STATE:
filled structurally; exactly one unfilled cell remains — the
initial proximity (1-e^2)_i, the inflaton's seat, the same single
initial condition isolated 2026-10-21. Chain: selector = the
count; the count's log = the stretch; the stretch's input = one
scalar's seat.

## Gemini seat routes assessed (2026-10-22)
Route 1 (D8 character / g12 fixed point): the fixed points are
exact, (1 +/- sqrt3)/2, but no frame map sends them to an
angular share; decisively, every algebraic/group quantity at
conductor 12 lies in [0.01, 1], so the seat term
(1/2) ln(16/(1-e^2)_i) is +1.9..+3.6 — O(1) garnish. The seat
cannot carry ~45 from ANY discrete spectrum; the formula puts
the burden on the count N.
Route 2 (LQG area minimum): disqualified by the G-free spec —
the area prefactor 8 pi gamma lP^2 carries lP, hence G — and
stripped of it, sqrt(j(j+1)) is the ordinary AM eigenvalue whose
minimal-share content is this morning's dwell computation
(K ~ 4.2-4.7); the Immirzi gamma would import a free constant.
CONCLUSION: the seat is an initial condition, not a spectrum
eigenvalue; with seat O(1), the hierarchy log lives entirely in
the stretch count N, and "why N ~ 44-50" is a question about the
inflationary epoch's duration.

## The one initial condition (2026-10-22, Jeremy: "the one initial condition being the big bang?")
Yes, at the frame's resolution: the seat (1-e^2)_i is the state at
the START of the stretch (the singularity's immediate output) and
the census is minted at its END (reheating/baryogenesis, eta
included) — both are the beginning as far as later dynamics is
concerned, and the frame's seat-impotence argument shows no
internal spectrum can substitute for it. Edge case: an exactly
tangent beginning ((1-e^2)_i = 0) makes the seat term diverge —
a finite census requires the beginning to sit OFF the tangency
by exactly the proximity the hierarchy prices. Final chain:
the cone selects, the stretch counts, the bang seats. Closes
Jeremy's 2026-10-21 line: stiffness as the singularity's fossil
tension is now the derived shape, not only the metaphor.
G_derived remains false; what is derived is the problem's
compression to a single initial condition.

## The two halves (2026-10-22, Jeremy, with his sign correction)
The cone's parabolic seat — the vertex, spin-0's place — is at
-1/2 (Jeremy's correction of the loose "vertex 1/2" phrasing).
The cosmic balance B = GM_u/(R_u c^2) = Omega/2 closes at +1/2
precisely when Omega = 1. The frame's one distinguished constant,
the 1/2 offset ((j+1/2)^2 = AM^2, the secant offset (n-k)/2,
offset^2 = 1/4), appears SIGNED at both ends of the cosmic
chain: the seat at -1/2 (the beginning, the scalar's place, the
parabola's vertex = the e=1 conic's own tangency point) and the
balance at +1/2 (the outcome, the count's price, the tangency of
the expansion). Seat-to-balance span is exactly 1 — the unit
cell's two rails, [j-1/2, j+1/2] at the fundamental cell:
the beginning seats on the lower rail, the universe balances on
the upper rail, one unit apart.

## The point at 0 (2026-10-22, Jeremy)
"It seems like the point at 0 in our cone is the initial
condition that is outstanding." With the seat at -1/2 and the
balance at +1/2, the remaining unfilled point is the center they
straddle: 0, the cone's apex. Forced by the geometry: a cone is
generated FROM its apex — the apex is the one point the machinery
cannot produce, because everything else (ladder, parabolas, phase
orbits, counts) is a section or winding at a distance from it.
Identifications stacked at 0: the bicone's gluing point (the KS
constraint lives there), the phase angle's origin (every chi is
measured from it; it is never itself integrated), the cone's
only singular point, and in the spacetime reading the past light
cone's apex = the bang. This localizes the outstanding initial
condition — it has coordinates — without supplying its value:
the value is the proximity the bang handed down.

## Dwell test — CLOSED, negative for the census form (2026-10-22, dwell_test.py)
Period-weighted census of the orbit family (shells n, share
s = (l+1/2)^2/n^2, weight K(s) = (1/2) ln(16/s), degeneracy 2l+1):
ln(N_dwell/N_plain) -> 0.6346 (converged by N=2000) while K_max
grows like ln N; mean dwell weight per shell -> ln 4 + 1/2
exactly (continuum limit). In a census, degeneracy beats the
logarithmic dwell weight: separatrix orbits are too few. The log
survives ONLY for a single orbit seated at the separatrix by the
initial condition — the cosmic case. This negative is the arc's
keystone: counting cannot manufacture the hierarchy log, which
is WHY the seat had to be the bang.
