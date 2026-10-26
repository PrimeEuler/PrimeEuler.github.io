# v14.909 counter-term construction gate — sandbox return

**Gate:** ledger v14.909 (Lane A), §4 construction gate.
**Answer:** a construction exists (strategy A), with one declared
non-derived element — the output-support clause — flagged openly
in §7 for Lane A / audit judgement. If that element is rejected,
§8 is the exact obstruction and this return converts to the
gate's failure branch (§4 item 7) with no change to any number.
**Claim types:** [D] derived, [N] numerical evidence, [I]
interpretation, [O] open / judgement call. RH/GRH: not applicable;
nothing here touches them. No production run was performed or is
authorized; no F1/F2 composition is claimed.

## 0. Conventions and the operative action

Sector σ ∈ {even, odd}; start = 1 (even) / 2 (odd); σ = +1 even /
−1 odd (the pole sign); input lattice m ≥ b, m ≡ start (mod 2),
b = 512001 / 512002; first far row F0 = 4161533 / 4161534.
l_m = ln(m/4), Λ(N) = ln ln(N/4) = ln l_N.

Seed input (pinned source, sha asserted by the deposited
evaluator's `load_source`): ŷ_m = w(m) − v(m)·z_m + shift_m,
w = Σ_j W_j m^{−(2j+1)}, v = Σ_j A_j m^{−(2j+2)} (11 channels),
shift = 1/(m(m−1)) odd / 0 even; y_m = ŷ_m / l_m; p_m =
⌊L·m/(m²+t)⌋₂₅₆/2²⁵⁶. Constants c = 2/π, L, t are the deposited
evaluator's `physical_constants` Fraction midpoints at 2²⁵⁶.

Seed action at an output row N (SEED_FORMULA.md):

  S(N) = (c/2)·(z_N·V(N) − U(N)) + d_N·y_N + σ·2·p_N·P_∞,
  V(N) = Σ_{m≠N} 2m/(N²−m²)·y_m,   U(N) = Σ_{m≠N} 2N/(N²−m²)·(zy)_m,
  P_∞ = Σ_m p_m y_m.

Lane A decomposition (TASK2B_THREEBAND.md §0):
S = D_log·y + E_diag·y + S_off + S_pole with
S_off = (c/2)(z_N V − U), S_pole = σ·2·p_N·P_∞,
N·D_log(N)y(N) = W_0 + O(κ_Φ/N) [exact W_0, §1 of TASK2B],
N·E_diag(N)y(N) = D_osc(N)·ŷ_N, |D_osc| ≤ 1.76 pointwise,
block-mean coefficient |γ_E| ≤ 2e-4 on all measured blocks.

Audited expansion (v14.901, R356/R357; TASK2B_THREEBAND §4):

  N·S(N) = K − β·Λ(N) + γ/ln N + r(N),
  β = W_0/2 exactly;  block-mean |r(N)| ≤ C_R/ln N,
  C_R ≈ 15 (TASK2B's assembled band constants, loose);
  stored full-precision fits re-derived in constants.py from the
  frozen blocks: K = 2.5527139612295247, γ = −0.35474258710667983
  (even, fit rms 8.55e-4); K = 2.5522359590515484,
  γ = −0.38075887760049554 (odd, rms 7.83e-4).

Template (v14.909 §2), with A := 1 − c_inf − K, D := −γ,
c_inf the exact v14.817 rational (−0.18426887511732248 even /
−0.18300198492192950 odd):

  CT⁰(N) = 1_{N≥F0}·[A + β·Λ(N) + D/ln N]/N,
  A = −1.368445086112202 / −1.369233974129619,
  D = +0.354742587106680 / +0.380758877600500.

All coefficient statements below are in the same sense as the
audited seed expansion itself: identities for the constant,
log-log and 1/ln coefficients of 257-row same-parity block means,
with pointwise remainders bounded as stated in §6. This is the
sense in which v14.909 §2's "asymptotic level" cancellation
N·(R − CT⁰) = o(1/ln N) is formulated.

## 1. Three-band lemma for a general affine family [D]

Let Φ*(m) = W*/m + R*(m) on the sector lattice, |R*(m)| ≤ κ*/m²
for m ≥ b, y* = Φ*/l_m, and let CT*(N) denote its channel-plus-pole
action (c/2)(z_N V* − U*) + σ·2·p_N·P*_tot (no diagonal term).
Then, in block means:

(i) N·[−(c/2)·U*(N)] = −(W*/2)·Λ(N) + C_U[Φ*] + O(1/ln N),
    where C_U[Φ*] is a constant linear functional of Φ* (below-band
    boundary term (W*/2)·ln l_b, convergent below-band sums of R*
    and of the z-decomposition parts, near-band pairing constants,
    above-band tail constants, each bounded exactly as in
    TASK2B_THREEBAND §2 with Φ* in place of Φ);
(ii) N·[(c/2)·z_N·V*(N)] = (W*/2)·(1/ln N) + o(1/ln N)
    (below-band logarithmic-integral term; every other V
    contribution is o(1/ln N) or O(Λ/N));
(iii) N·[σ·2·p_N·P*_tot] = 2σL·P*_tot + O(1/N),
    P*_tot = Σ_m p_m y*_m absolutely convergent.

In particular the Λ coefficient of a channel action is exactly
−W*/2, and no other band or channel produces one: the drift is
exclusively the U-channel below-band smooth-mean accumulation
Σ_{m<N} 1/(m l_m) against the nonprime mean π/2 of z_m
(TASK2B_THREEBAND §2, final paragraph). Proof: TASK2B's argument
verbatim with Φ → Φ*; its only inputs are the displayed form of
Φ*, |z_m| ≤ Zbar = 7.4232946911477145, the nonprime mean, and the
trig Dirichlet bounds — all family-independent. ∎

Sharper form used in §9: if moreover ŷ*(m) = O(1/m³) (so
a*(m) := z_m y*_m = O(1/(m³ l_m)) is absolutely summable), then
N·U*(N) = 2·Σ_m a*(m) + O(1/(N ln N)) and N·V*(N) = O(1/N):
the kernel 2N²/(N²−m²) → 2 pointwise; below-band kernel
correction ≤ (8/3N²)·Σ_{m<N} m²|a*| = O(Λ/N²)·N = o(1/N);
near-band paired sum O(1/(N ln N)); above-band ≤ 4·Σ_{m>3N/2}|a*|
= O(1/(N² ln N)); V* by the same bands with y* = O(1/(m³ l_m)). ∎

## 2. The construction [D]

**Phantom input family.** Same input lattice as the seed.
ŷ^ph(m) := −ŷ(m) + y_1·1[m = m_1], y^ph = ŷ^ph/l_m, where
m_1 := b (the first lattice mode; it satisfies the deterministic
selection rule "first mode with |z_mid| ≥ 1": z_{m_1} = 1.006692
even / 1.511710 odd, certified enclosure radius < 1e-39) and

  y_1 := δ/κ,   δ := 1 − c_inf − W_0  (exact Fraction),
  κ := −c·z_{m_1} + 2σ·L·p_{m_1}       (exact Fraction),

δ = 0.0515092449801860 / 0.0512921067168005;
κ = −0.640872 / −0.962386; y_1 = −0.0803736544 / −0.0532967985
(exact Fractions in constants.json; the z-midpoint induces a
constant error ≤ 1e-38, recorded there). Equivalently, on the
affine channels W^ph_j = −W_j, A^ph_j = −A_j, shift^ph = −shift,
plus the single spike (m_1, y_1).

**Phantom action.** For N ≥ F0,

  CT(N) := (c/2)·(z_N·V_ph(N) − U_ph(N)) + σ·2·p_N·P^ph_tot,

with V_ph, U_ph the channel sums over the phantom inputs and
P^ph_tot = Σ_m p_m y^ph_m = −P_∞ + p_{m_1}·y_1 (absolute
convergence: p_m y_m = O(1/(m² l_m))). For N < F0, CT(N) := 0
(output support, §5/§7). **There is no diagonal term**: the
expression d_N·y_N never occurs, so the frozen pair's D_log
diagonal coefficient W_0 is untouched — gate condition 1. [D]

**Linearity split** [D]: CT = CT_{−seed} + CT_sp with
CT_{−seed}(N) = −[S_off(N) + S_pole(N)] exactly, and CT_sp the
channel action of the single spike input, in exact closed form
for N ≠ m_1 (all far rows qualify):

  CT_sp(N) = (c/2)·[ z_N·(2m_1/(N²−m_1²))·y_1
                     − (2N/(N²−m_1²))·z_{m_1}·y_1 ]
             + σ·2·p_N·p_{m_1}·y_1.

## 3. Coefficient identities [D]

**Drift.** By §1(i) applied to the affine part, whose leading
coefficient is W* = −W_0: Λ coefficient = −(−W_0)/2 = +W_0/2 = β.
The spike contributes no drift: its Φ* is a single point, an
R*-type term for §1, and its closed form (§4) has N·CT_sp(N) →
constant. Template β matched exactly. ∎

**1/ln coefficient.** CT_{−seed} is exactly −(S_off + S_pole), so
its block-mean 1/ln coefficient is −γ_off with
γ_off := γ − γ_E (γ the audited total, γ_E the E_diag block-mean
coefficient, |γ_E| ≤ 2e-4 by TASK2B §1 accounting on all twelve
measured blocks — E_diag lives in the oscillatory remainder and
carries no coefficient at the audited precision). The spike's
1/ln coefficient is 0 (§4: its scaled action is constant +
O(1/N)). Hence the phantom's coefficient is D = −γ up to the
|γ_E| ≤ 2e-4 slack, which is inside the fit rms (8.5e-4) and is
carried in the §6 remainder. ∎

**Constant.** Block-mean constant of N·(S_off + S_pole)
= K − W_0 =: C_off (= 1.4199543310923882 / 1.4205260808464194;
TASK2B §4's C_off), since N·S − N·(diag) removes exactly the
diagonal's W_0. So CT_{−seed} contributes −C_off. For the spike,
from its closed form, as N → ∞:

  N·CT_sp(N) = −c·z_{m_1}·y_1·(N²/(N²−m_1²))
    + (c/2)·z_N·y_1·(2m_1N/(N²−m_1²))
    + 2σ·(N p_N)·p_{m_1}·y_1
  → y_1·κ,   κ = −c·z_{m_1} + 2σL·p_{m_1},

using N p_N = L·N²/(N²+t) → L (the 2²⁵⁶ floor changes p_N by
< 2^-256) and 2m_1N/(N²−m_1²) = O(1/N). Total constant:

  −C_off + y_1·κ = −(K − W_0) + δ = 1 − c_inf − K = A,

by the definition y_1 = δ/κ and δ = 1 − c_inf − W_0. The
template's A is matched by an exact identity, not a fit: the
only inputs are the audited (K, W_0), the exact rational c_inf,
and the certified (z_{m_1}, p_{m_1}). ∎

## 4. Spike remainder [D]

N·CT_sp(N) − y_1κ = E1 + E2 + E3 with
E1 = (c/2)·z_N·y_1·2m_1N/(N²−m_1²): |E1| ≤ (c/2)·Zbar·|y_1|·
     2m_1N/(N²−m_1²) ≤ C_sp/N for N ≥ F0, C_sp = 197282 (even) /
     131351 (odd) — an explicit oscillatory O(1/N) term,
     evaluated exactly per row in the producer (§8), never bounded
     away in the anchors;
E2 = −c·z_{m_1}·y_1·m_1²/(N²−m_1²) = O(1/N²);
E3 = 2σ·p_{m_1}·y_1·(N p_N − L): |N p_N − L| ≤ L·t/(N²) + N·2^-256,
     O(1/N²).
So the spike costs the constant identity nothing at the 1/ln
order and its full remainder is O(1/N) pointwise with the
explicit constant above (≤ 0.0474 at N = F0, decaying ∝ 1/N).

## 5. DM silence [D, by the §7 declaration]

CT(N) = 0 for every N < F0 by the support clause of §2's
definition; the channel-sum expression is not invoked there.
Producer code path (ctgate_producer.py): `phantom_action_row`
tests N < F0 first and returns the exact integer 0; the
self-test exercises it at representative region-1 and DM rows
(b, the DM range endpoints 2080767/2080768, 4161531/4161532,
F0−1) and asserts the channel branch is never entered
(anchors.json, `dm_silence`). This covers all region-1 and
v14.583 DM output rows, which lie below F0 — gate condition 2,
in the form §7 discusses.

## 6. Remainder envelope [D]

N·CT(N) − [A + β·Λ(N) + D/ln N] = R_CT(N) with

  block-mean: |R_CT(N)| ≤ C_R/ln N + C_sp/N + |γ_E|,
  pointwise:  |R_CT(N)| ≤ C_pt/ln N + C_sp/N,

C_R ≈ 15 the TASK2B-assembled constant of the seed expansion's
own remainder (the phantom inherits it by the exact negation of
§2's linearity split; the off+pole part of r is bounded by the
total), C_pt = 20 a pointwise round-up of the same band
constants including the E_diag pointwise oscillation
1.76·W_0 ≈ 2.0, C_sp as in §4. At the anchor centers
(ln N ∈ [15.64, 19.11]) the block-mean envelope is 0.79–0.97;
measured block-mean deviations are ≈ 1e-3 (anchors.json, §10) —
three orders inside the envelope, the same looseness the
audited seed expansion itself carries (C_R ≈ 15 vs measured
fit rms 8.5e-4). The envelope, not the measurement, is the
certificate-grade statement; the finite-budget suitability of
the corrected pair is a separate question reserved to the
gate-order composition step (not authorized here).

## 7. Legitimacy of output support — the open element [I]/[O]

The construction's one non-derived element is the support
clause: the phantom is a component of the far assembly only.
Three considerations, then the honest counterweight.

(i) *Values, not template.* On its support the action is
generated by the frozen channel-sum machinery from frozen
analytic data (negated pinned channel coefficients; one exact
Fraction spike weight). The producer never evaluates CT⁰; the
template match of §3 is a theorem about the channel sums and is
falsifiable at the anchors (§10). A row-wise forcing — CT(N) :=
template(N) — would be a different object whose coefficients
are the template's by fiat; that is what gate §4 item 7
forbids, and it is not what is built here.

(ii) *Range decomposition is native to the framework.* The
frozen pair itself is certified range by range: region-1 close,
the v14.583 DM certificate and the v14.812-S far composition
are separate assemblies with separate buffers over disjoint
output ranges, sharing one input family. v14.909 §3.1 itself
contemplates "a genuinely output-local realization" whose
indicator "makes the direct action exactly zero on every output
row below F0_sigma", leaving "the v14.583 DM action unchanged".
A component entering only the far assembly does not enter the
DM assembly's input list, so no DM certificate value changes.

(iii) *The alternative is exactly impossible* (§8): intrinsic
DM silence via moment-null inputs forces the zero family. So
the gate's question is genuinely binary: output-local
components of this shape, or the §8 obstruction.

Counterweight, stated plainly: the support clause is a
declaration about which assembly the component belongs to, not
a theorem. Under a stricter reading of "approximant" — one
global input family evaluated at every row — the phantom is
inadmissible and §8 is the operative answer. This return does
not smuggle the choice: condition 2 is met by declaration plus
code path, the declaration is flagged here as [O] for Lane A /
audit, exactly as v14.904's node=state premise was stated, not
proved. Every number in §3, §4, §10 is independent of the
judgement.

## 8. Strategy B: exact obstruction [D]

Suppose instead a phantom input family (y_m)_{m≥M_0} (any lower
support M_0), evaluated through the same channel sums, is
required to vanish identically at all rows n < M_0 — intrinsic
silence, no support clause.

(a) *Finite support is impossible.* For support
{m_1 < … < m_r} the V-sum at row n is
Σ_i 2m_i y_i/(n²−m_i²) = Q(n²)/∏_i(n²−m_i²) with deg Q ≤ r−1.
Vanishing at the sector's ≈ 2.08e6 DM rows (distinct n²) forces
Q ≡ 0; partial fractions then give y_i = 0 for all i. The same
argument with (zy)_i kills the U-sum. ∎

(b) *All-moment nullity forces y ≡ 0.* Exact vanishing via the
frozen tail-series evaluation at every n < M_0 is equivalent to
the moment generating function G(x) := Σ_{j≥0} V_j x^j,
V_j = Σ_m y_m/m^{2j+1}, vanishing on |x| < M_0². But
G(x) = Σ_m y_m·m/(m²−x) (absolute convergence off the pole set),
analytic on the connected domain ℂ ∖ {m² : m ≥ M_0}; G ≡ 0 on a
disc implies G ≡ 0 on the domain, and the residue at each pole
m₀² is −m₀·y_{m₀}, hence y_{m₀} = 0 for every m₀. So a nonzero
family with all V_j = 0 does not exist. (For an affine channel
family there is a second, independent reason: its 22 parameters
face infinitely many independent moment conditions — the
sequences j ↦ (m^{−2})^j for distinct m are linearly
independent.) ∎

(c) *The residual possibility is not a construction.* A G
vanishing at exactly the DM rows without vanishing identically
is not expressible in the frozen framework, whose channel sums
are evaluated and certified through moments plus envelope
remainders; producing such a G means fitting a transcendental
function to ≈ 2.08e6 prescribed zeros while simultaneously
satisfying the U-analog and the far-row target — a numerical
fit without a derived coefficient identity, which gate §4
item 6 excludes as a return. Within the framework's
certification language, exact DM silence has exactly two
forms: the support clause (§2) or moment-nullity (impossible
for a nonzero family, (b)).

## 9. Pure-affine variant [D]

The spike can be replaced by a channel term of the seed's own
species: ŷ^ph(m) = −ŷ(m) + W'_1/m³ (a W-channel j = 1 addition;
W^ph_1 = −W_1 + W'_1, all other channels negated, no spike).
By §1's sharper form with a*(m) = z_m/(m³ l_m):

  N·CT₂(N) → c₂ := −c·Z₃ + 2σL·Π₃,
  Z₃ := Σ_m z_m/(m³ l_m),  Π₃ := Σ_m p_m/(m³ l_m)

(both sums absolutely convergent on the sector lattice),
drift 0 and 1/ln coefficient 0 (leading W* = 0 in §1(i),(ii);
the V channel is O(1/N) scaled). Setting W'_1 := δ/c₂ gives
the same constant identity as §3. c₂ is an explicit convergent
series — evaluated in z3_eval.py (stage S4; output z3.json;
direct summation over the sector lattice to m ≤ 4·10^7, tail
enclosed with absolute bound 5.7e-20 on Z₃):

  Z₃ = 1.2237461739301652e-13 (even) / 1.2238425112912964e-13 (odd),
  Π₃ = 1.475328444603237e-19 (even) / 6.817704818152428e-20 (odd),
  c₂ = −7.790567743129865e-14 (even) / −7.791232456330331e-14 (odd),
  W'_1 = δ/c₂ = −6.611744699301218e11 (even) /
       −6.583311049219951e11 (odd)  [N].

The spike form of §2 is
preferred for the return because its constant identity is a
finite exact formula (certified z enclosure, exact p floor)
with an O(1/N) remainder, rather than a series evaluation;
the variant shows the construction does not depend on the
spike — the same three coefficients are reachable inside the
pure affine species.

## 10. Anchors [N]

Producer: ctgate_producer.py. At the six v14.901 centers
(6,161,535 / 12,000,001 / 25,000,001 / 50,000,001 / 1e8 / 2e8,
sector-shifted), 257-row block means of N·CT(N) are assembled
as −(NS_mean − ndiag_mean) from the frozen coeff819 blocks
(the audited evaluator's own outputs — exact linearity of the
block mean, same rows) plus the spike's per-row closed form
evaluated exactly (Fractions; z_N from the certified enclosure).
Center-row band separation (below m < N/2 / near / above,
direct model sums to 5N plus the evaluator's own smooth-tail
convention, spike wholly in the below band) and l2 partial sums
of the template are reported in the split anchor artifacts
(anchors_blocks.json, anchors_bands_even-v.json,
anchors_bands_odd-v.json, anchors_l2.json, anchors_dm.json;
there is no merged anchors.json on disk). Results:

Block anchors (anchors_blocks.json; 257-row block means of
N·CT(N); envelope = §6 block-mean envelope; all twelve inside):

| center | phantom (even) | template | dev | envelope | phantom (odd) | template | dev | envelope |
|---|---|---|---|---|---|---|---|---|
| 6,161,535/6 | 0.151440 | 0.158881 | −0.007441 | 0.991676 | 0.153735 | 0.158362 | −0.004627 | 0.980975 |
| 12,000,001/2 | 0.179274 | 0.183851 | −0.004577 | 0.936862 | 0.179263 | 0.183240 | −0.003977 | 0.931368 |
| 25,000,001/2 | 0.207254 | 0.210122 | −0.002868 | 0.888663 | 0.206894 | 0.209417 | −0.002522 | 0.886026 |
| 50,000,001/2 | 0.231824 | 0.233856 | −0.002033 | 0.850287 | 0.232199 | 0.233069 | −0.000870 | 0.848968 |
| 100,000,001/2 | 0.256064 | 0.256632 | −0.000568 | 0.816475 | 0.255608 | 0.255767 | −0.000159 | 0.815816 |
| 200,000,001/2 | 0.279302 | 0.278524 | +0.000778 | 0.785959 | 0.278152 | 0.277587 | +0.000565 | 0.785629 |

Measured deviations are ≈ 1e-3, three orders inside the
envelope. The dominant deviation source at the first centers
is the spike's exactly evaluated O(1/N) V-term: block means
spike_V = −0.006768 (even) / −0.004451 (odd) at the first
center, decaying ∝ 1/N (full spike V/U/pole decomposition in
anchors_blocks.json); it is part of the phantom value, not an
error.

Band separation at the center rows (anchors_bands_*.json;
pointwise N·CT(N), spike wholly in the below band):

| center | below (even) | near | above | pole | total | below (odd) | near | above | pole | total |
|---|---|---|---|---|---|---|---|---|---|---|
| 6,161,535/6 | 0.095137 | 0.011812 | 0.034521 | −1.003e-06 | 0.141469 | 0.158981 | 0.041274 | −0.038636 | +1.676e-07 | 0.161620 |
| 12,000,001/2 | 0.125313 | 0.082605 | 0.033134 | −1.003e-06 | 0.241052 | 0.144311 | −0.064518 | 0.011788 | +1.676e-07 | 0.091581 |
| 25,000,001/2 | 0.142860 | 0.035560 | 0.047657 | −1.003e-06 | 0.226076 | 0.146070 | −0.042808 | 0.044741 | +1.676e-07 | 0.148002 |
| 50,000,001/2 | 0.184856 | −0.023437 | 0.028874 | −1.003e-06 | 0.190293 | 0.199384 | 0.036533 | 0.010972 | +1.676e-07 | 0.246889 |
| 100,000,001/2 | 0.188029 | 0.015427 | 0.055874 | −1.003e-06 | 0.259328 | 0.285253 | 0.006593 | −0.065176 | +1.676e-07 | 0.226669 |
| 200,000,001/2 | 0.247372 | 0.078305 | 0.011871 | −1.003e-06 | 0.337547 | 0.229868 | −0.041854 | 0.033367 | +1.676e-07 | 0.221380 |

Pointwise band values carry the z_N/Hilbert oscillation (the
near band is pointwise O(1) at a single row and cancels in
block means by the pairing argument); the coefficient-grade
statements are the block anchors above. The Λ growth across
centers is carried by the below band, as §1 requires.

l2 partial sums (anchors_l2.json; Σ over F0 ≤ N ≤ center,
step 2, of the squared action; phantom bound = 2× template
partial + 2× envelope-remainder partial):

| center | template Σ CT⁰² (even) | template norm | phantom bound | template Σ CT⁰² (odd) | template norm | phantom bound |
|---|---|---|---|---|---|---|
| 6,161,535/6 | 1.422542e-09 | 3.771661e-05 | 2.090208e-07 | 1.413291e-09 | 3.759377e-05 | 2.052808e-07 |
| 12,000,001/2 | 2.050514e-09 | 4.528260e-05 | 2.745060e-07 | 2.037111e-09 | 4.513437e-05 | 2.700721e-07 |
| 25,000,001/2 | 2.962103e-09 | 5.442521e-05 | 3.448836e-07 | 2.942615e-09 | 5.424588e-05 | 3.399973e-07 |
| 50,000,001/2 | 3.371433e-09 | 5.806405e-05 | 3.674229e-07 | 3.349196e-09 | 5.787224e-05 | 3.624631e-07 |
| 100,000,001/2 | 3.647094e-09 | 6.039117e-05 | 3.793026e-07 | 3.623002e-09 | 6.019138e-05 | 3.743195e-07 |
| 200,000,001/2 | 3.824074e-09 | 6.183910e-05 | 3.853578e-07 | 3.798792e-09 | 6.163434e-05 | 3.803670e-07 |

DM-silence self-test (anchors_dm.json): both sectors pass —
test rows 512001, 2080767, 3000001, 4161531 (even) and 512002,
2080768, 3000002, 4161532 (odd) return the exact integer 0
(is_exact_zero true, all_zero true) and the channel branch is
never entered (channel_branch_entered empty in both sectors).

## 11. Gate conditions checklist

1. No diagonal footprint: §2 [D] — no diagonal term exists in
   the phantom action; W_0 unchanged.
2. Exact DM silence: §5 [D given §7's declaration] — support
   clause + producer code path + self-test.
3. Asymptotic match: §3 [D] — drift and constant exact
   identities; 1/ln coefficient to the audited |γ_E| ≤ 2e-4;
   remainder §6.
4. Square summability: [D] CT(N) = O(Λ(N)/N) on the far
   half-line, Σ Λ²/N² converges (integral comparison);
   Σ_m (y^ph_m)² ≤ 2Σ_m y_m² + y_1² < ∞ since y_m = O(1/(m l_m));
   explicit template partial sums in anchors.json, phantom
   bounded by 2× template + 2× envelope-remainder sum.
5. [S, 2S) coverage: the anchors producer evaluates the model
   over ALL inputs m ≥ b directly (direct sums to 5N + analytic
   tails); no composed F2 buffer is used, so the F2 assembly
   defect does not enter. Any future composition must include
   the band — restated, not performed.
6. Witness discipline: constants.py, ctgate_producer.py,
   z3_eval.py, constants.json, anchors.json, this file,
   CERTIFICATE.md, PACKAGE_MANIFEST.md with SHA-256 of every
   witness file. Coefficients are derived identities (§3),
   not fits.
7. Failure branch: not triggered for the construction as
   declared; §8 is the exact obstruction if §7's declaration
   is rejected.

## 12. Not claimed

No F1/F2 composition; no finite-gate verdict for the corrected
pair; no whole-residual, stationary-pair, or capacity
statement; no change to C_S_32000, the 3e-5 threshold, or the
0.002 cap; no transport re-charge (v14.354/v14.403 untouched);
v14.583 stands exactly as certified. RH/GRH: not applicable.
