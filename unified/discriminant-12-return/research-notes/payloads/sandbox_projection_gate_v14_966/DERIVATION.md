# Canonical operator-origin projection gate (v14.942) — sandbox return

**Gate:** ledger v14.942 (Lane A), HANDOFF — Sandbox: canonical
operator-origin projection gate; restated unchanged in v14.961
("the sole active Lane A dependency").
**Answer: branch (N) — a scoped no-go.** In the certification
class 𝒞_proj stated in §1, no auxiliary channel realizes the
v14.909 counter-term profile with exact DM annihilation holding
for a structural (operator-identity) reason. The three possible
provenance routes — output-side projection, input-side class
restriction, intertwining — are each closed in §§3–5. §2 records
the exact operator identities the frozen channels DO satisfy
(Sylvester intertwining up to moment functionals), which are the
operator-level explanation of the closure. §7 states the scope
precisely, mirroring v14.942's own scoping discipline: this is
not a universal no-go.
**Claim types:** [D] derived, [N] numerical evidence, [I]
interpretation, [O] open. RH/GRH: not applicable. No production
run was performed or is authorized; no F1/F2 composition is
claimed; no threshold or charge is touched.

## 0. Operative formalism [D — restated from audited sources]

Per sector σ ∈ {even, odd} (σ = +1 even / −1 odd), input lattice
m ≥ b (b = 512001/512002, m ≡ start mod 2), first far row
F0 = 4161533/4161534; DM output rows are N < F0. The frozen
channel action of an input family y, with no diagonal term, is
(ctgate/DERIVATION.md §0, audited in v14.938):

  A_y(N) = (c/2)·(z_N·V_y(N) − U_y(N)) + 2σ·p_N·P_y,
  V_y(N) = Σ_{m≠N} 2m/(N²−m²)·y_m,
  U_y(N) = Σ_{m≠N} 2N/(N²−m²)·(zy)_m,
  P_y = Σ_m p_m·y_m,   p_m = ⌊L·m/(m²+t)·2^256⌋/2^256.

Constants c = 2/π, L, t are the deposited evaluator's exact
Fraction midpoints; z is the frozen z sequence with the audited
properties |z_m| ≤ Zbar = 7.4232946911477145 and lattice
(nonprime) mean π/2 (the mechanism of the audited drift
β = W_0/2, v14.901 §TASK2B, verified R356). The row functional
ℓ_N(y) := A_y(N) has coefficient of y_m equal to

  k_N(m) = c·(m·z_N − N·z_m)/(N²−m²) + 2σ·p_N·p_m   (m ≠ N),
  k_N(N) = 2σ·p_N²   (pole part only; V/U exclude m = N),

and p_m > 0 for every lattice m (p_m ≥ 2^−256, since
L·m/(m²+t)·2^256 ≥ 1 throughout the framework's range; witness
W3, exact). Two limits used below, from p_m = L·m/(m²+t) −
ε_m with 0 ≤ ε_m < 2^−256 and |z| ≤ Zbar:

  N·k_N(m) → κ_m := −c·z_m + 2σL·p_m   (N → ∞, m fixed),
  m·k_N(m) → κ_N                        (m → ∞, N fixed).

At the spike mode m₁ = b of v14.936, κ_{m₁} ≠ 0 is certified in
exact Fractions (κ = −0.640872 even / −0.962386 odd; witness W2,
recomputed from the deposited constants).

Three-band lemma (ctgate §1, [D]): for an affine input family
ŷ(m) = W*/m + O(1/m²), y = ŷ/l_m, the Λ := ln ln(N/4)
coefficient of N·A_y(N) in block means is exactly −W*/2, and no
other band or channel produces one. The template
CT⁰(N) = [A + β·Λ(N) + D/ln N]/N has β = W_0/2 ≠ 0, so any
input realizing the profile inside the frozen channel species
has W* = −W_0 ≠ 0 — in particular its ŷ is nonzero at every
sufficiently large lattice point (full tail support).

## 1. The certification class 𝒞_proj

The gate demands DM annihilation "for a structural reason"
(v14.942 item 3), with the channel "defined before numerical
evaluation" and its "output locality from an operator identity"
(item 1), "without raw row-wise cutoff or fitted zeros". We
formalize "structural" in the only way that distinguishes it
from the excluded alternatives: the annihilation is a property
of the channel and an operator-defined class — an identity
holding for every input of the class — not a property of one
tuned input (a fit) and not a declaration about evaluation
(the v14.936 clause). The class:

(K) Kernel species: the row action is A_y of §0 (frozen V/U/pole
    channels, coefficients from the frozen spectral data), with
    no diagonal term.
(I) Input classes: 𝒴 = A(𝒟), where 𝒟 is a linear class of input
    data containing every finitely supported sequence on the
    sector lattice, and A is diagonal in the frozen mode basis,
    A = diag(a_m) — i.e. A lies in the Borel spectral calculus
    of the frozen diagonal operator (D_log, equivalently D2:
    operators diagonal in the frozen mode basis are exactly the
    Borel functions of either). DM annihilation is required as
    an identity on 𝒴: ℓ_N(y) = 0 for all DM rows N and all
    y ∈ 𝒴.
(O) Output operators and intertwiners: diagonal operators
    B = diag(β_N) in the same spectral calculus, used either by
    composition (channel B∘A_y) or by intertwining
    (T∘A = B∘T, T the frozen channel map of (K)).
(P) Profile: the constructed input y* ∈ 𝒴 realizes CT⁰'s
    audited coefficients (drift +β and constant A as exact
    identities, 1/ln coefficient to the audited |γ_E| ≤ 2e-4,
    remainder O(1/ln N), per v14.909/v14.939), in particular the
    drift forces W* = −W_0 ≠ 0 (§0).

The frozen data available for provenance are exactly: the mode
basis and its diagonal operators (D_log, D2); the channel
realization (K); the frozen domain (moment class — it contains
all finitely supported sequences, item (I)'s hypothesis on 𝒟).
Not frozen data, hence outside 𝒞_proj: the spectral
decomposition of the full non-diagonal frozen operator, and the
stationary pair / capacity closure (open globally, §7).

## 2. The identities that DO hold: Sylvester, up to moments [D]

Let Λ denote multiplication by the squared index (input side)
and Λ′ the same on rows. For finitely supported y and a
(a = zy in the application), termwise in m ≠ N:

  N²·V_y(N) − V_{Λy}(N) = 2·Σ_{m≠N} m·y_m = 2·(M₁[y] − N·y_N),
  N²·U_a(N) − U_{Λa}(N) = 2N·Σ_{m≠N} a_m = 2N·(M₀[a] − a_N),

since N²·2m − m²·2m = 2m·(N²−m²) and N²·2N − m²·2N = 2N·(N²−m²).
Witness W1 verifies both identities in exact Fractions on
random finite rational inputs (60 trials, including rows on the
support). So the frozen channels intertwine the diagonal
operator D2 up to an explicit defect — and the defect is a
global moment functional of the input (minus its diagonal
sample), never a row-support operator. Every spectral-calculus
manipulation of the channel re-expresses its action through
moments of the input; none manufactures row support. This is
the operator-level content behind §§3–5, and it is the same
moment structure that drives §8(b) of the ctgate return
(all-moment nullity ⇒ y ≡ 0).

## 3. Lemma A — output-side projections collapse to the clause [D]

Let B = diag(β_N) be a projection (B² = B) in the spectral
calculus whose range is exactly the far-row space. Diagonality
forces β_N ∈ {0, 1}; the range condition forces β_N = 1 for
N ≥ F0 and β_N = 0 for N < F0. Hence B = 1[N ≥ F0] — as a
linear map, identical to the hard indicator of v14.936 §2 that
v14.942 excluded. A spectral-calculus redescription ("Borel
function of D_log") does not change the map, and v14.942's
exclusion was of the map — an output-row projector attached to
the construction — not of its description. More generally, any
diagonal B with β_N = 0 on all DM rows annihilates the DM
output coordinates for every input by construction: it is a
row-wise cutoff in operator clothing, which gate item (1)
excludes by requiring locality from an operator identity of
the channel. The only remaining operator-identity route is
intertwining, closed in §5. ∎

## 4. Theorem — input-side class annihilation is impossible [D]

Suppose, in 𝒞_proj, that A has infinite support and that DM
annihilation holds as an identity on 𝒴 = A(𝒟) (item (I)).
Since 𝒟 contains every finitely supported sequence, for each
lattice mode m₀ the data w = e_{m₀} gives y = a_{m₀}·e_{m₀} ∈ 𝒴,
so annihilation at every DM row N gives

  a_{m₀}·k_N(m₀) = 0   for all DM rows N (with k_N(N) as in §0).

The profile (item (P)) forces supp(a) ⊇ tail: y* ∈ 𝒴 has
ŷ*(m) = W*/m + O(1/m²) with W* = −W_0 ≠ 0 at every large
lattice m (§0), and supp(y*) ⊆ supp(a). Hence a_m ≠ 0 for all
large m, and therefore

  k_N(m) = 0   for every DM row N and all large lattice m.

Fix any one DM row N. For all large m (m ≠ N), k_N(m) = 0 reads

  c·(m·z_N − N·z_m) + 2σ·p_N·p_m·(N²−m²) = 0,
  z_m = (z_N/N)·m + (2σ·p_N/(cN))·p_m·(N²−m²).

Insert p_m = L·m/(m²+t) − ε_m, 0 ≤ ε_m < 2^−256, and
Lm(N²−m²)/(m²+t) = −L·m + L(N²+t)m/(m²+t):

  z_m = S·m + ρ_m,   S := z_N/N − 2σ·p_N·L/(cN),
  ρ_m = (2σp_N/(cN))·[ L(N²+t)m/(m²+t) − ε_m(N²−m²) ],

with L(N²+t)m/(m²+t) = O(1/m) → 0 and |ε_m(N²−m²)| ≤ m²·2^−256,
which is < 2^−40 for all m ≤ 2^108. The z family is a half-line
family (the gate's own template and ℓ² conditions are half-line
statements; the evaluator's z is defined at every lattice
point), so the displayed identity at all large m must coexist
with the two audited facts |z_m| ≤ Zbar and lattice mean π/2.
It cannot, in either case:
(i) |S| ≥ 2^−60: at m ≈ 16/|S| ≤ 2^64 the ε-error in ρ_m is
    ≤ C_N·m²·2^−256 < 2^−120 (C_N = |2σp_N/(cN)| ≤ 4.5) and the
    O(1/m) part is negligible, so |z_m| ≥ 16 − 1 > Zbar —
    contradicting the bound.
(ii) |S| < 2^−60 (including S = 0): the Cesàro mean of z over
    [b, X] with X = 2^60 equals S·(mean of m) + o(1), of
    absolute value < 0.5 + o(1) (the ε-part of the mean is
    ≤ C_N·X²·2^−256 < 2^−130), contradicting the audited mean
    π/2 — the very fact that produces the nonzero drift in the
    audited seed expansion.
Therefore no DM row functional vanishes identically on 𝒴:
input-side structural annihilation does not exist in 𝒞_proj.

The remaining case is finite supp(a): then every y ∈ 𝒴 is
finitely supported, and the profile is unattainable — finite
support has W* = 0, hence zero Λ coefficient by the three-band
lemma, against β ≠ 0 (equivalently ctgate §8(a): the V/U sums
of a finitely supported family are rational in N² of bounded
degree and cannot vanish on the DM rows unless y ≡ 0). ∎

## 5. Lemma B — no diagonal intertwiner localizes output [D]

Let A = diag(a_m), B = diag(β_N) with T∘A = B∘T as operators
(T the frozen channel map, §0), tested on finitely supported
inputs. Comparing the coefficient of y_m in row N:

  (β_N − a_m)·k_N(m) = 0   (m ≠ N),   (β_N − a_N)·2σ·p_N² = 0.

Since p_N > 0 (W3), the diagonal pair gives β_N = a_N for every
row N. Pair row N with the certified mode m₁ = b (κ_{m₁} ≠ 0,
W2): (a_N − a_{m₁})·k_N(m₁) = 0 for all N ≠ m₁, and
N·k_N(m₁) → κ_{m₁} ≠ 0 (§0) gives k_N(m₁) ≠ 0 for all large N;
hence a_N = a_{m₁} for all large N, i.e. B = a·I on the whole
far tail with a = a_{m₁}. If a = 0 the intertwined channel
vanishes on the far tail and cannot carry the CT⁰ profile; if
a ≠ 0, B is a nonzero scalar on far rows — it annihilates
nothing. (Rows in the bounded DM band are irrelevant to the
verdict: localization requires B to vanish on DM rows while
acting as the identity, up to the profile's own normalization,
on far rows; the tail conclusion already forbids the far side
of that alternative for every intertwiner.) Hence no
intertwiner in the frozen spectral calculus derives far-output
locality for a channel in 𝒞_proj. ∎

## 6. Exhibits [N — from projgate_witness.py / witness.json]

**W4 — the clause was load-bearing already for the spike.**
The v14.936 spike's closed-form action CT_sp(N) (ctgate §2) is
affine in z_N with the exact nonzero coefficient
(c/2)·y₁·2m₁/(N²−m₁²); CT_sp(N) = 0 would force z_N to one
exact rational ζ(N). At eight sample DM rows ζ(N) misses the
CERTIFIED z_N enclosure (suzuki_bulk_action_z.evaluate) by
0.139 … 13.45 — against enclosure radii at the 1e-39 scale —
so CT_sp(N) ≠ 0 is certified at every sample (values at the
enclosure midpoints: 8.9e-10 … 2.5e-8). Even the phantom's
one-mode component does not annihilate a single sampled DM row
without the clause.

**W5 — the full phantom without the clause.** Evaluating the
v14.936 phantom input (−ŷ_seed + spike) through the frozen
channel sums at DM rows, with no support clause (evaluator's
z model and channel formulas, direct chunked float64 sums over
the input lattice to m ≤ 2·10^8, plus the rigorous affine tail
enclosure of PLAN.md §4 with C_ŷ ≈ 1.262 from the
b^−2j-scaled channel constants):

| sector | DM row N | N·A_ph(N) | tail enclosure on N·A_ph |
|---|---|---|---|
| even | 2080767 | +0.034965 | 0.0018 |
| even | 4161531 | +0.030287 | 0.0036 |
| odd  | 2080768 | +0.117293 | 0.0018 |
| odd  | 4161532 | +0.164442 | 0.0036 |

The un-claused phantom action on DM rows is O(0.03–0.16) in
scaled units — the same order as the far-row profile values
themselves — and exceeds its rigorous enclosure at every row.
The §5 support clause of v14.936 carried the entire DM
silence, confirming v14.942's provenance diagnosis from the
witness side. (Ratios of value to enclosure: 8.5×–66×.)

**W6 — the two limits of §0.** (a) N·k_N(m₁) → κ_{m₁}:
even −0.0360 / −0.5730 / −0.6663 / −0.6407 at
N = 1e5 / 1e6 / 1e7 / 1e8 against κ = −0.640872; odd
−0.0233 / −1.0087 / −0.9887 / −0.9622 against κ = −0.962386 —
oscillatory convergence to the certified values, as Lemma B
requires. (b) The identity the Theorem's hypothesis would
force on z (from the single DM row N₀ = F0−2) predicts z_m
growing linearly: at m = 4·10^8 the forced value is +436.93
(even) / −111.75 (odd) against the model z_m = +3.49 / +1.53 —
the bounded, mean-π/2 sequence of the frozen framework does
nothing of the kind; the contradiction of §4 made visible.

## 7. Scope — what this no-go does and does not close

Proved: within 𝒞_proj (§1) — frozen V/U/pole kernel species,
no diagonal term, input classes / output operators /
intertwiners confined to the frozen mode-basis spectral
calculus, annihilation as an operator identity on the whole
input class — no channel realizes the v14.909 profile with
structural DM annihilation. The v14.936 construction remains
what v14.942 ruled it: numerically frozen, provenance-
inadmissible; and §8 of the ctgate return (finite-support and
all-moment obstructions) is now complemented on the
operator-identity side: the obstruction is not an artifact of
the support clause's phrasing, because every operator-derived
replacement for the clause inside the frozen calculus either
is the clause (Lemma A), is a row cutoff by construction
(§3), cannot annihilate (§4), or cannot localize (§5).

Not claimed, exactly as v14.942 scoped its own obstruction:
(a) a single tuned input whose DM zeros are fitted is not
excluded by §§3–5 — it is excluded by the gate's separate
no-fitted-zeros rule, a prohibition this return does not
re-derive; (b) objects built from data outside the frozen
spectral calculus — above all a spectral decomposition of the
full non-diagonal frozen operator, or the stationary-pair /
capacity structures — are untouched: if such a decomposition
is ever frozen, the gate can be re-asked in the enlarged
calculus, and Lemmas A/B (which use only diagonality) do not
prejudge it; (c) infinite families with prescribed discrete
zeros constructed by non-frozen means (ctgate §8(c)) remain
outside, as do any future re-freezes with new structure.
No universal no-go is asserted.

## 8. Gate checklist against v14.942's negative branch

- Precise operator/channel class: §1 (K), (I), (O), (P). ✓
- Proof of nonexistence in that scope only: §§3–5, scope §7. ✓
- No universal extrapolation: §7 (a)–(c). ✓
- Positive-branch items (1)–(7) are not claimed; items (4)–(6)
  are moot for a nonexistence return, and the profile side of
  (5) enters only as the hypothesis (P) that drives §4's
  support conclusion (the drift forces the tail).
- Witnesses: projgate_witness.py + witness.json (W1 exact
  Sylvester; W2 exact κ_{m₁}; W3 exact p_N > 0; W4 certified
  spike DM action; W5 phantom DM action exhibit with rigorous
  tail enclosure; W6 limit confirmations), CERTIFICATE.md,
  PACKAGE_MANIFEST.md with SHA-256 of every witness file.
- Not claimed: no F1/F2 composition or certificate; no residual
  replay; C_S_32000, the 3e-5 and 0.002 thresholds, and the
  exactly-once v14.354 / v14.403 charges are untouched;
  v14.583 and v14.936's frozen witness values stand exactly as
  audited.
