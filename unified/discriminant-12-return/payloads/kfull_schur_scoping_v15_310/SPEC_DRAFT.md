# SPEC DRAFT — full-K transfer alternative via the Schur route

Sandbox [N] design/resource spec for the v15.232 `lane-a-kfull-transfer-alternative`
handoff, against Lane A gates v15.303 (exact infinite-tail Schur inertia),
v15.304 (finite stopping rule), v15.305 (non-decay floor). Status: DRAFT,
workspace only, nothing ledgered.

## 0. Scope boundary (read first)

- Lane A's own named gate is the **analytic** bound on ‖Q_N B Q_N‖ from the
  five-frequency kernel, plus Lane A's two-level Feshbach truncation
  criterion. This spec is the **numerical/resource route**: it scopes what a
  certified computation would cost and where it can break. It is **not**
  that proof, must not be represented as it, and produces at best a
  numerical certificate assembled from interval-certified stages.
- The probe numbers below measure the frozen kernel of DERIVATION.md §0
  with the float model `z_float` and float `p_n ≈ L·n/(n²+t)`. Any
  certification stage must swap in the certified evaluators
  (`suzuki_certified_remote_z`, `suzuki_certified_remote_diagonal`, exact
  floored `p_n`) — the probe establishes scales, not certified values.

## 1. Measured inputs (tail_norm_probe.py + floor_check.py, this run dir)

| quantity | odd lattice (b=512001, σ=+1) | even lattice (b=512002, σ=−1) |
|---|---|---|
| v15.305 floor (\|c\|/4)√A, A = 6.7041170580615635… | 0.4120889090 | 0.4120889090 |
| Cesàro mean of \|z_{n+2}−z_n\|² from `z_float` (2·10⁶ samples) | 6.704125 (+1.2e-06) | 6.704115 (−3.7e-07) |
| ‖Q_N B Q_N‖ window estimates, N = 10³…5·10⁵, W = 2000/4000 | 1.8885 – 1.9202 | 1.9151 – 1.9669 |
| ‖V‖, remote J=100 block vs full complement | 0.8677 (‖V‖² = 0.7529) | 0.8835 (‖V‖² = 0.7805) |
| stopping N at measured M_N (b_int = 10.45 / 10.30) | 5.2e6 – 5.3e6 | 4.6e6 – 4.9e6 |
| stopping N at crude certified M = 15 | 2.59e12 | 2.23e12 |

Framing per v15.305: M_N is a **persistent constant**, proven to lie in
[0.4121, 15]; the window estimates place it at ≈ 1.9–2.0, flat in N
(4.6–4.8× the floor at every cutoff). Do not model M_N as decaying.
The window spread is fluctuation, and the estimates are lower bounds —
planning should carry headroom (hypothesis: budget M_N ≤ 2.5; a slow
log-creep of window norms with window size, as in the DERIVATION §3
truncation probe 1.70→1.86 over S = 100→800, cannot be excluded by
2000–4000-mode windows).

Two negative facts the design must respect:

1. **Coarse A_N-only test is dead at the target scale.** The v15.304
   fully-finite acceptance test promotes interval inertia of A_N − x
   only if eigenvalue intervals clear 0 by more than ‖V‖²/g_N. With the
   measured ‖V‖² ≈ 0.75–0.78, the residual is 7.5 (g=0.1) … 0.38 (g=2),
   versus the v15.227 certified gap scales 0.004151 (odd) / 0.012958
   (even) — 30× to 1800× too coarse. (Caveat: the measured ‖V‖ is the
   remote-block coupling, used as a scale indicator; the prefix
   ‖V_N‖ = ‖Q_N B P_N‖ is a different quantity — but v15.305 Gate 2
   gives limsup ‖V_N‖ ≥ 0.4121 for sharp prefixes, so no plausible
   ‖V_N‖ rescues the coarse test at these gap scales.)
2. **The literal prefix route is finite but not executable densely.**
   At measured M_N the stopping index is N ≈ 5·10⁶ physical, i.e.
   ≈ 2.5·10⁶ lattice modes per sector in P_N. A dense P_N K P_N is
   ~10¹³ entries — no interval LDLᵀ/inertia computation touches it on
   this hardware class (2 cores, ~8 GB). The stopping rule certifies
   the *tail* cheaply; the *finite side* is the bottleneck. This is
   exactly the gap Lane A's two-level Feshbach gate and the
   resonant-P branch below are meant to close.

## 2. Route A — sharp prefix + F̂_N (v15.304 direct), as scoped

Pipeline (per sector), target interval [a, b] = the v15.227 windows
(odd ≈ [10.4402, 10.4455]-scale around x = 10.4423; even around
x = 10.2921, b_int tops 10.45 / 10.30):

- **A1. Certified diagonal census.** Evaluate certified enclosures of
  d_n for all lattice n up to N₁ = 4·exp(b + C + M̂ + g) − 2 at chosen
  margin g (M̂ = the working M_N bound). Certifies: the mode set with
  d_n ≤ b + margin is finite, enumerated, and complete.
  Cost driver: interval diagonal evaluation is O(1)/mode; at g = 2,
  N₁ ≈ 3.9·10⁷ (odd) → ~2·10⁷ modes/sector. Feasible-scale
  (hypothesis: hours on this box, extrapolating the v15.227 evaluator
  linearly from its 2·10⁴-mode scans).
- **A2. Tail positivity.** From A1 + M̂: g_N = m_N − b − M̂ > 0 gives
  [a, b] ⊂ ρ(T_N), n₋(T_N − x) = 0, ‖(T_N − x)⁻¹‖ ≤ 1/g_N. Pure
  arithmetic on A1 outputs — *provided M̂ is a certified bound*, which
  is Lane A's analytic gate, not this spec (see §5, Risk R1).
- **A3. F̂_N assembly.** F̂_N(x) = A_N − x − V* R_D,N(x) V with
  R_D,N = (D_Q − x)⁻¹. The V* R_D V term is an **infinite
  diagonal-weighted tail sum**: every entry must be computed with an
  outward-certified remainder (v15.304 NOTE), not truncated silently.
  Interval arithmetic mandatory here.
- **A4. Endpoint inertia.** Interval LDLᵀ/Sylvester inertia of
  F̂_N(a), F̂_N(b) (symmetric greedy pivoting per the v15.227 build),
  eigenvalue enclosures widened by
  ε_F ≤ ‖V‖²·M̂·τ²/(1 − α), τ = 1/(m_N − b), α = M̂τ.
  ε_F at measured constants (remote-block ‖V‖ as indicator):
  g = 1 → 0.49/0.52; g = 2 → 0.18/0.19; g = 4 → 0.061/0.064
  (odd/even). Certifies a full-K gap on [a, b] iff both endpoints are
  ε_F-clear of 0 and inertias agree (v15.303 monotonicity S′ ≤ −I).
- **Blocker inside Route A:** A3–A4 act on the full prefix block
  (~10⁶–10⁷ modes at the margins where ε_F ≲ 0.2). Not executable as
  stated. Route A is the correctness reference; Route B is the
  executable shape.

## 3. Route B — resonant-mode P (v15.303 candidate, preferred)

v15.303's resource-saving candidate, made necessary by §1 fact 2 and
by v15.305 Gate 2 (the limsup obstruction is specific to *sharp
prefixes*): choose P = a **certified set of resonant modes** — modes
whose diagonal enclosure meets [a − ρ, b + ρ] for a declared guard
ρ — wherever they sit in the lattice, plus the v15.227 J=100 remote
block. Q = everything else.

- **B1. Resonant census.** From A1's certified diagonal enclosures,
  extract every mode with d_n ∈ [a − ρ, b + ρ]. The v15.227 tail scan
  found 5 (odd) / 12 (even) fully-in-strip enclosures among the first
  2·10⁴ tail modes; the total resonant count out to the log-clearing
  index is a **hypothesis to be measured by B1** (planning guess:
  10²–10³ per sector at ρ ~ M̂ scale; the census decides). P's size —
  hence the explicit Schur matrix size — is |P| = 100 + resonant
  count, target ≤ ~10³–10⁴.
- **B2. Tail split.** Q splits into (i) a high part n > N₁ (diagonal
  above b + margin): positive by the A2 argument, zero negative
  inertia, resolvent ≤ 1/g; (ii) a bulk part (all remaining modes):
  diagonal bounded away from [a, b] by ≥ ρ − (enclosure width), but
  containing all sub-interval modes, whose negative inertia is **not**
  automatically 0 and must be counted, not assumed. Counting route
  (design choice, to be frozen before any run): band the bulk by
  diagonal value and certify each band's inertia by interval
  diagonal-dominance (Gershgorin) where |d_n − x| exceeds the band's
  coupling scale, with sub-bands that fail dominance promoted into P.
  This promotion loop is the main engineering risk (R3).
- **B3. Schur assembly on P.** S_P(x) = A_P − x − V*(T − x)⁻¹V
  evaluated at x = a, b via the B2 resolvent enclosures; the tail sum
  again needs outward-certified remainders. Interval arithmetic
  mandatory. |P| ≤ 10⁴ keeps dense interval linear algebra in the
  v15.227-proven regime (J = 100 precedent; cubic scaling makes
  10⁴ the practical ceiling on this box — labeled extrapolation).
- **B4. Count assembly.** n₋(K − x) = n₋(T − x) + n₋(S_P(x)) with
  n₋(T − x) = (B2 high part: 0) + (B2 bulk count). Endpoint inertia
  agreement + ε-clearance ⇒ full-K gap/count on [a, b], same
  acceptance shape as v15.158/v15.162 but with the tail handled by
  B2 instead of the diagonal-preserving cutoff.

## 4. Where interval / outward rounding is required (checklist)

1. Certified diagonal enclosures d_n (A1/B1) — producer of record only
   (`suzuki_certified_remote_diagonal.evaluate`), outward rounding.
2. Resonant-set completeness (B1): a mode is resonant if its
   *enclosure* meets the guarded interval — never decide on midpoints.
3. F̂ / S_P tail sums (A3/B3): infinite sums; remainder bounds
   outward-rounded, truncation without a remainder is disqualifying.
4. Eigenvalue/inertia enclosures (A4/B3/B4): widened by ε_F (Route A)
   or the B3 analogue; pivoting order fixed in advance from float
   midpoints (v15.227 lesson: natural order fails by width
   amplification through small pivots).
5. p_n: exact floored values, not the float model, in any certified
   stage (probe used the float model for scale only).
6. z_n: certified evaluator, not `z_float`, in any certified stage.

## 5. Risks

- **R1 (gating, external).** Every stage above consumes a *certified*
  M̂ ≥ ‖Q_N B Q_N‖. The probe's 1.9–2.0 are lower-bound estimates.
  Lane A's analytic bound is the named gate; until it lands, all
  stopping scales in this spec are conditional. Fallback if the
  analytic bound stalls: certify M̂ on a *finite* tail window plus an
  analytic Hilbert-tail majorant — itself a small proof obligation,
  not a probe output.
- **R2.** Prefix ‖V_N‖ is unmeasured; Gate 2 bounds its limsup below
  by 0.4121. If a Route-A variant is ever costed seriously, measure
  ‖V_N‖ matrix-free (power iteration on Gram blocks) at production N
  first — cheap relative to everything else.
- **R3.** Route B's bulk-inertia counting (B2) may fail dominance on
  wide bands, promoting so many modes into P that |P| blows past
  10⁴. Mitigation: none known a priori; B1+B2 on one sector is the
  cheap go/no-go experiment.
- **R4.** Endpoint clearance: ε_F ≈ 0.18–0.19 at g = 2 must fit
  inside the actual eigenvalue clearance of S_P at the chosen
  endpoints. Finite-section evidence is encouraging (v15.227 even
  window margins ≥ 0.0718; odd secondary point ≥ 0.00935 — the odd
  sector's clearances are the tight ones) but full-K clearances are
  unmeasured. Endpoint choice is a search problem, budgeted in B3.
- **R5.** Model risk: `z_float` vs the certified z. The Cesàro check
  (rel. err ~1e-06 against A) says the float model's adjacent
  differences are statistically right; individual certified entries
  can still move window norms at the percent level. No probe number
  should be quoted tighter than ~±0.05.

## 6. Bottom line

- The Schur route is **finite with realistic constants**: at the
  measured M_N ≈ 1.9–2.0 (inside the proven [0.4121, 15] band), the
  v15.304 stopping rule needs N ≈ 5·10⁶, not 10¹² — a ~5·10⁵-fold
  reduction driven entirely by replacing the crude M = 15 with the
  measured tail norm.
- It is **not executable in its literal prefix form** (dense block of
  ~2.5·10⁶ modes/sector), and the coarse A_N-only test is **not
  viable** at the v15.227 gap scale (residual 30–1800× too big).
- The executable shape is **Route B** (resonant-mode P, |P| ≲ 10³–10⁴,
  bulk inertia by banded dominance, high tail by the stopping rule),
  conditional on two cheap, decidable experiments — the B1 resonant
  census and the B2 dominance pass rate — and on Lane A's analytic
  M̂ (R1) for the proof-grade version.
- Feasibility judgment: **worth one scoped build** (B1 + B2 prototype
  on the odd sector, the tighter one), with a hard stop if |P| or the
  dominance failure rate exceeds the §3 targets. Nothing in this spec
  is a certificate, and FULL_K_TRANSFER remains INCONCLUSIVE until a
  run under §4's rounding checklist actually lands.
