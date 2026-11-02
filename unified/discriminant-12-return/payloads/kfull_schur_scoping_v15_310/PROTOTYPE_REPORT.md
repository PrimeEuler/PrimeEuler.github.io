# Route B prototype (B1 + B2) — odd sector — PROTOTYPE REPORT [N]

Prototype-grade scoping for SPEC_DRAFT.md §3 (Route B), against the
v15.232 full-K transfer-alternative handoff and Lane A gates
v15.303/v15.304/v15.305. **Not a certified run. Not a certificate.
FULL_K_TRANSFER remains INCONCLUSIVE.** Workspace only; nothing
ledgered.

**Header context (v15.306 / v15.307):** neither entry is present in
the local ledger cache `~/workspace/d12/cache/ledger/` (the cache
tops out at v13.813 and holds no v15 entries), so no certified or
analytic M̂ value could be recorded from them. The prototype
proceeds on the frozen design inputs: guard ρ = 2.5 (working
M̂ = 2.0 + 0.5 margin, design choice), per the task freeze.

## Setting (frozen, from v15.227)

Odd parity lattice, base b = 512001 (σ = +1,
L = 1.4357379705709206, c = 2/π, t = 1/π²). Target point
x = 10.442302397081809, δ = 0.0010376564980985107, target interval
[a, b] = [x − δ, x + δ]. Guard window [a − ρ, b + ρ]
= [7.94126, 12.94334] at ρ = 2.5. Log-clearing index
n_max = 9,582,891 (smallest lattice n with log(n/4) − C > b + ρ,
C = 1.745855454249828); total lattice modes scanned: 4,535,446.

## B1 — resonant census: HARD STOP, |R| ≈ 7.9 × 10⁵

- Float pre-filter (SEED_FORMULA displayed diagonal model, slack
  0.1): **896,843 candidates**; float d_n inside the exact guard
  window: **787,812 modes**.
- Certified classification (producer of record
  `suzuki_certified_remote_diagonal.evaluate`, enclosure-meets-window
  with exact Fraction comparisons, ascending n): the certified
  resonant count crossed the hard-stop threshold of 20,000 after
  only **20,364 certified evaluations**, at n = 553,043 — i.e.
  within the first ~41,000 lattice modes, under 1% of the census
  range. **Certified statement: |R| > 20,000** (20,001 evaluated
  resonant enclosures are listed in census_output.json). Certified
  evaluation halted there per the hard stop.
- Float reliability check: a stratified spot check of 200 candidates
  across the full range agrees with the certified enclosure
  classification **200/200**, with max |certified midpoint − float
  d_n| = 1.23e-06 (the v15.227 F1 O(1/n) scale). The float total
  |R| ≈ **787,812** is therefore a sound prototype-grade scale
  measure.
- Distribution (float, per n-band): the resonant set is **not
  thinning to a sparse tail set**. In-window counts / fractions:

  | n band | modes | resonant (float) | fraction |
  |---|---|---|---|
  | 512k – 750k | 118,999 | 111,187 | 93.4% |
  | 750k – 1.0M | 124,999 | 101,698 | 81.4% |
  | 1.0M – 1.5M | 249,999 | 163,140 | 65.3% |
  | 1.5M – 2.0M | 249,999 | 115,563 | 46.2% |
  | 2M – 3M | 499,999 | 136,265 | 27.3% |
  | 3M – 4M | 499,999 | 74,664 | 14.9% |
  | 4M – 6M | 999,999 | 67,047 | 6.7% |
  | 6M – 9.58M | 1,791,446 | 18,243 | 1.0% |

  The fraction falls only because log(n/4) climbs out of the guard
  window; every band up to 6M still contributes ≥ 6.7 × 10⁴ resonant
  modes. Overall the resonant set is **17.4% of all lattice modes**
  up to the log-clearing index. Mechanism: the guard window has
  width 2ρ ≈ 5.0 while the diagonal oscillation satisfies
  |d_n − log(n/4)| ≲ 1.75 — any mode whose log-center lies within
  ρ + 1.75 of the window has an O(1) chance of qualifying. The
  spec's planning guess (10²–10³) extrapolated the density of the
  δ-strip (width 0.002) to a window ~2400× wider; that extrapolation
  is what failed, not the arithmetic.

- Guard sensitivity (float in-window counts, rho_sensitivity.json):
  ρ = 2.5 → 787,812; 2.0 → 385,908; 1.5 → 162,913; 1.0 → 54,693;
  0.75 → 28,683; **0.5 → 13,292**; 0.25 → 4,814; 0.1 → 1,734;
  0.05 → 879. The |P| ≤ 1e4 target is already exceeded at
  ρ = 0.5 (13,292 resonant, before the J = 100 block and any B2
  promotions), and log-interpolation puts ρ = 0.4121 — the v15.305
  *floor* on the tail-coupling scale — at ≈ 1e4, i.e. at best
  marginal. But the guard must dominate the tail coupling at the
  working scale M̂ ≈ 2, not at the floor: at any ρ in the
  defensible range [1, 2.5], |R| is 5 × 10⁴ – 8 × 10⁵.

## B2 — bulk dominance: NOT RUN (gate), one diagnostic finding

Per the task gate, B2 runs only if B1 passes. B1 hard-stopped, so
the banded dominance pass was **not run** (dominance.py implements
it with the exact prototype criterion — band passes at energy x iff
min |d_n − x| over band modes exceeds the Frobenius norm of the
band's B-rows over the prototype window — and dominance_output.json
records status NOT_RUN; that code path is unexecuted).

Diagnostic finding (as invited by the task): ℓ¹ Gershgorin row sums
do diverge for this kernel. Partial row sums
S(M) = Σ_{m ≤ M, m ≠ N} |B_{N,m}| reach **7.23** (row N = 512001)
and **9.58** (row N = 1000003) at M = n_max, with far-tail
increments tracking log M (slope ≈ 0.22–0.26 per ln unit from
M = 2e6 to 9.58e6, consistent with the |B_{N,m}| ~ c|z_N|/m tail).
ℓ¹ row-sum dominance is disqualified, confirming the task's premise.

## Go / no-go judgment

**NO-GO for Route B as specified in SPEC_DRAFT §3, at its own
targets.** Implied |P| = 100 + |R| + promoted ≥ 100 + 787,812
≈ **7.9 × 10⁵**, about **79× the |P| ≤ ~1e4 target** — and the
excess is entirely in B1, before any B2 dominance failures or
promotions (the §5 risk R3 blow-up mode is not even reached).
The failure is structural, not computational: at a guard ρ tied to
the measured tail-coupling scale (M̂ ≈ 2), the resonant set is a
positive-density subset of the lattice (~17% of all modes), because
the diagonal oscillation amplitude (~1.75) is comparable to ρ
itself. Shrinking ρ to reach |P| ~ 1e4 requires ρ ≲ 0.4 — at or
below the v15.305 floor 0.4121 for the coupling the guard is meant
to dominate — at which point the modes at distance 0.4–2.5 from the
interval fall to the bulk-counting side (B2), exactly where
dominance is hardest and (per the diagnostic) unavailable in ℓ¹
form. A resonant-P Schur certificate with these ingredients does
not close at the §3 targets in the odd sector.

Nothing here touches Route A's status as the correctness reference,
Lane A's analytic M̂ gate, or the FULL_K_TRANSFER = INCONCLUSIVE
freeze. All counts above are prototype-grade [N] except the single
certified statement |R| > 20,000 (20,001 enclosures evaluated).

## Files

- census.py / census_output.json — B1 (float census complete;
  certified pass halted at the hard stop; 200/200 spot check).
- rho_sensitivity.json — float |R|(ρ) table.
- dominance.py / dominance_output.json — B2 (NOT_RUN; gate recorded;
  Gershgorin diagnostic executed).
- Wall times: census 41.6 s; dominance 3.1 s.
