# Cone Derivation Ledger v13.900 — Auditor-Thread Finding: Record Prime Gaps and Divisor Extremity — a Confound Caught Mid-Analysis, and What Survives It

Date: 2026-10-01

Author: External audit thread (Claude, independent instance) — **contributed finding, not an audit round.** Continuation of v13.898 (HC numbers and local gap bias), prompted by a direct follow-up question from the project owner: do the two tail-only effects found this week (HC numbers sitting in longer-than-local-average gaps; the `A_a` positivity knife-edge) combine — specifically, do the *longest* prime gaps (gap records) disproportionately contain the *most divisible* numbers?

Status: **[N]** numerical throughout; **[I]/[O]** interpretation. No RH/GRH claim. Unrelated to the positivity program (v13.894/896) — same firewall v13.898 already stated.

## Why this entry is worth reading as a confound story, not just a result

The first version of this test gave a clean, confident-looking answer that was **backwards**, due to a statistical confound I didn't catch until redoing the comparison properly. Recording the wrong version alongside the fix, rather than silently presenting only the corrected result, because the failure mode is a useful, reusable lesson for this kind of analysis.

## 1. First pass (confounded) — record gaps looked *less* divisible than typical [N, superseded by §2]

For the 22 maximal prime-gap records up to `N=2,000,000` (the classical "first occurrence of a new maximum gap" sequence: `(2,3)` gap 1, `(3,5)` gap 2, `(7,11)` gap 4, ..., `(4652353,4652507)` gap 154), I compared each record's max-`d(n)`-among-its-composites against the **pooled median** max-`d(n)` across *all* gaps of that same length anywhere in the range.

Result: record gaps averaged `50.82`, versus `74.27` for the pooled same-length comparison — ratio `0.684`, and **0 of 22** records exceeded their length's typical value. This looked like a clean, surprising negative result (records are *less* divisible than ordinary gaps of equal length).

**The flaw:** pooling by raw length across the whole range mixes wildly different `n`-scales. A gap record is, by definition, the *first* occurrence of that length — necessarily early. But *ordinary* (non-record) gaps of that same length keep recurring at much larger `n` for the rest of the range, where `d(n)` runs higher simply because `d(n)` grows (slowly) with `n`. The "pooled median" was therefore dominated by large-`n` occurrences, making any early, small-`n` record look artificially unimpressive by comparison. Gap length was held fixed; `n` was not — that's the confound.

## 2. Second pass (`log n`-controlled) — flips to a strong positive signal [N, itself subject to §3]

Redone with `n` properly controlled: for every gap in the dataset (not just records), I regressed both the enclosing gap's max-`d(n)` and its length against `\log n` (OLS) and used the residuals.

Result: **22 of 22** record gaps now sit above their `n`-adjusted expectation (mean residual `+28.13`, vs. `-0.002` for ordinary gaps, against an overall residual std of `33.39` — roughly 0.84σ on average, unanimous in direction). Across the full dataset of `348{,}512` gaps, the `\log n`-detrended correlation between gap length and max-divisibility-in-gap came out at **`+0.4724`** — by far the strongest correlation found in any test this week (compare: first-composite-after-prime vs. gap length was `-0.0135`; divisor accumulation rate vs. gap length was `\le 0.07` in every variant tested).

## 3. Third pass — isolating a second, more dangerous confound: order statistics [N]

Before accepting `+0.47` as a real number-theoretic connection, I checked the more basic explanation: **a longer gap simply contains more composites, and the maximum of more random draws is mechanically larger** — a generic fact about order statistics, true for any roughly-independent sequence and unrelated to primes specifically. Gap length and "how many composites you're sampling `d(n)` from" are the same quantity, so this is a real risk, not a pedantic one.

**Control:** for a random sample of `20{,}000` actual prime gaps, I compared each gap's max-`d(n)` against the max-`d(n)` in an **arbitrary window of exactly the same length**, placed near the same `n` (not required to sit between two primes — just the same number of consecutive integers, same neighborhood).

Result: actual prime gaps still win, but by much less than §2 suggested — mean `56.25` (real) vs. `52.45` (length-matched random window), a difference of **`+3.80`**, about **7%** relative excess. Still highly statistically significant (`paired t = 13.04`, `p = 1.08\times10^{-38}` on `n=20{,}000` paired samples) — not noise — but an order of magnitude smaller in relative terms than the dramatic `0.84σ`/`22-for-22` framing in §2 implied.

## 4. What the three passes together actually establish [N/I]

- **Most of the §2 effect was the order-statistics artifact flagged in §3.** Longer gaps have more composites; more composites mechanically raises the expected maximum `d(n)` you'll find among them. This explains the bulk of why "longer gap ⟺ more divisible interior" looked so strong once the `n`-scale confound was fixed — length and sample-count are the same variable here.
- **A smaller, genuine residual survives the stricter control.** Actual prime gaps beat length-matched arbitrary windows by `+3.80` (`~7\%`), decisively (`p=1.08\times10^{-38}`). Being a *maximal run bounded by two actual primes* carries a little more divisibility-concentration than an arbitrary same-length stretch of integers would — consistent with, and plausibly the bulk-data echo of, the §4 mechanism proposed in v13.898 (numbers with many small prime factors locally suppress nearby primality, so the composite stretch they sit inside tends to run a bit longer than one containing only unremarkable numbers).
- **The headline-grabbing version of this finding (§2 alone) would have overstated the result by roughly an order of magnitude** had the §3 control not been run. Recording this explicitly because it's a reusable caution for interpreting any "longer run → more extreme interior value" correlation in this kind of data: always check whether "more draws, bigger max" alone already explains it before reading in anything deeper.

## What this is not

- Not predictive in the sense of forecasting future gaps; it's a structural/statistical fact about the already-realized classical gap sequence.
- Not connected to the positivity program or the explicit-formula arc — same firewall as v13.898.
- No RH/GRH claim.

## Reproducibility

All three passes: sieve-based, `N=5{,}000{,}000` throughout (§1-3; the larger bound than v13.898's `N=2{,}000{,}000` was used here to get a fuller set of gap records — 22 records found up to 5M), standard `d[i::i]+=1` divisor sieve. §2's residuals via OLS of `(max_d_in_gap, gap_length)` against `\log(\text{starting prime of gap})`. §3's random-window control: `20{,}000` gaps sampled (seeded RNG, seed 0), window placed at a uniform random offset in `\pm 2000` of the gap's starting prime, same length as the real gap, paired t-test via `scipy.stats.ttest_rel`. Scripts ad hoc, not saved to the repo, consistent with how this session's other contributed findings (v13.898) were reported; methodology above is complete enough to reproduce independently.

## Synchronization

Live ledger head checked immediately before this write: v13.899 (sandbox's independent verification of v13.898, plus Suzuki v3 archival — read in full before writing this entry). No collision on v13.900.
