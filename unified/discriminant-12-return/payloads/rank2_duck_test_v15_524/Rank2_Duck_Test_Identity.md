# Duck test, rank-2: the device↔model rhyme in the tidal (G) channel

*Sandbox note (little Euler), 2026-11-07. Jeremy's go-ahead
the same day ("Run the rank-2 duck test"). The v14.628 duck
test found the device↔model rhyme to be identity in the
rotor (rank-1) sector. The rank-2 tidal channel of v14.630
was anatomized there but never duck-tested — and it is the
only channel in the rotor anatomy that carries G itself
(β₂ = 2GM_sI²/(ħ²R³); rank-1's β carries the local g).
Test criterion, the v14.628 criterion, stated in advance:
the rhyme is identity at rank 2 iff the transverse tidal
couplings are the axial channel's weights times exact
closed-form factors in j — no free parameter in the map —
with the climb products closing in closed form on the two
parity chains. Producer: `rank2_duck_test.py`.*

## The three channels are one skeleton [D]

Components of the one rank-2 tensor as operators on the
rotor (bare angular functions, v14.628's normalization
precedent — the source-direction factors of the addition
theorem ride with the field amplitudes, as E_z / E₋ did at
rank 1):

- **Axial** (the v14.630 channel): A₀ = P₂(cos θ). Climb
  v_j = ⟨j+2,0|A₀|j,0⟩ = (3/2)·w_j·w_{j+1} → 3/8; diagonal
  d_j = ⟨j,0|A₀|j,0⟩ → 1/4.
- **Transverse drive, Δm = +1:** A₁ = sin θ cos θ e^{iφ}.
- **Transverse drive, Δm = +2:** A₂ = sin²θ e^{2iφ}.

Ratio laws — each identified from exact Wigner-3j values,
then verified exactly (squares at every j ≤ 32, signed
forms at small j; the transverse weights are nonzero
throughout, guards in the producer):

- climb: **v1_j = −(2/3)·√((j+3)/(j+2)) · v_j**,
  **v2_j = +(2/3)·√((j+3)(j+4)/((j+1)(j+2))) · v_j**;
- diagonal: **d1_j = −d_j/√(j(j+1))**,
  **d2_j = −2·√((j−1)(j+2)/(j(j+1))) · d_j**.

Absolute forms: v1_j = −(j+1)√((j+2)(j+3)) /
((2j+3)√((2j+1)(2j+5))); v2_j =
+√((j+1)(j+2)(j+3)(j+4)) / ((2j+3)√((2j+1)(2j+5))).
Per-step limits: v1 → −1/4, v2 → +1/4 against v → 3/8 —
the transverse climbs run at exactly 2/3 of the axial
per-step strength asymptotically; d1 → 0 (like −1/(4j));
d2 → −1/2, exactly −2× the axial diagonal's limit.

## Climbs [D]

Rank-2 steps (Δj = 2) split the ladder into even and odd
chains (v14.630). The ratio laws' products close:

- Π R2 telescopes exactly:
  Π_{k<N} R2(s+2k) = (2/3)^N · √((s+2N+1)(s+2N+2)/((s+1)(s+2)));
- Π R1 is a Gamma ratio: (−2/3)^N ·
  [Γ((s+3)/2+N)·Γ((s+2)/2) / (Γ((s+3)/2)·Γ((s+2)/2+N))]^{1/2};

both verified against direct products at N = 30 to
≤ 6×10⁻¹⁵. Combined with the axial climbs of v14.630
(√(π/2)·(3/8)^N even, √(3π/8)·(3/8)^N odd — re-verified
here, within 1.6×10⁻⁵ of the constants at N = 4000 and
converging):

- Π v1 ~ C_s · N^{1/4} · (−1/4)^N, C_even = π^{1/4},
  C_odd = π^{1/4}√(3π)/4;
- Π v2 ~ D_s · N · (1/4)^N, D_even = √π, D_odd = √π/2;

measured at N = 4000 within 3×10⁻⁴ of these constants,
converging. The rank-1 climb's Wallis constant √(π/2)
reappears on the even chain, as it did at rank 2 for the
axial channel itself.

## Cross-checks [D]

Three independent paths agree. (i) Wigner-3j values.
(ii) Composition from rank-1 matrix elements only —
A₁ = S·C in both orderings, A₂ = S·S, A₀ via (3C²−1)/2,
with S = sin θ e^{iφ}, C = cos θ — maximum disagreement
with (i) is 2.8×10⁻¹⁶ over j ≤ 12, and the two orderings
for A₁ agree to 1.1×10⁻¹⁶. (iii) The record's axial
formulas, reproduced exactly at j ≤ 30.

Two development catches, filed openly. First, the 3j
m-sum convention: the second symbol's third entry is −m′;
with +m′ every transverse weight vanishes identically and
the ratio checks would have passed vacuously on zeros —
nonzero guards now stand in the producer ahead of every
fit. Second, the Δj = −1 elements of sin θ e^{iφ} carry
the opposite sign to its Δj = +1 elements:
⟨j−1,m+1|S|j,m⟩ = +√((j−m−1)(j−m)/((2j−1)(2j+1)))
(the composition check caught this on d2's sign before
any result was filed; the 3j values fix it). The v14.628
record used only the Δj = +1 elements, so nothing there
is affected.

## Verdict

In the rank-2 tidal channel, the rhyme is **identity of
governing structure**, in the same sense and with the
same force as v14.628: one rank-2 coupling theory
(Wigner–Eckart) governs the axial channel and both
transverse drives, and every map between their weight
systems is an exact closed form with no adjustable
parameter. The rank-2-specific anatomy — the parity-split
chains, and the diagonal channel rank 1 lacked — is part
of the skeleton, not an exception to it: the transverse
drives respect the same parity split, and their diagonal
weights are exact multiples of the axial diagonal.
Jeremy's duck passes in the G-carrying channel.

## Boundaries (what the test does not cover)

- **Scope:** the tidal (P₂) channel's coupling anatomy —
  the far-field channel of v14.630 §§1–2. The exact
  finite-distance device coupling (v14.630 Part 3) carries
  n = 4 content (fourth harmonic 1.5–3.8% at bench
  distances) and sits outside the rank-2 skeleton, as
  designed-in coil turns sat outside rank 1's test.
- Identity of coupling anatomy ≠ a derivation of G:
  β₂'s overall scale still carries the imported G (the
  anatomy is the j-dependence), and the ψ selector is
  untouched. `G_derived = false`, unchanged.
- The first execution of this test was lost to a runtime
  restart ~29 minutes in (an uncached exact-3j climb
  table to j = 4000); the producer was restructured —
  exact work at j ≤ 32, climb products from the verified
  closed forms — and completes in ~2 s. No output from
  the lost run is used anywhere above.
