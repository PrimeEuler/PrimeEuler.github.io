# Cone Derivation Ledger v13.898 — Auditor-Thread Finding: Highly Composite Numbers Sit in Longer-Than-Local-Average Prime Gaps (Tail-Only Effect)

Date: 2026-10-01

Author: External audit thread (Claude, independent instance) — this is a **contributed finding, not an audit round**. No sandbox or Lane-A entry is being reviewed here; this is original numerical work the auditor thread did in direct conversation with the project owner, offered to the sandbox as a possibly-useful side observation. Standard [D]/[N]/[I]/[O] discipline applies throughout; nothing here touches RH/GRH or the positivity program.

Status: **[N]** numerical findings throughout (statistical correlations and residual comparisons, not theorems); **[I]/[O]** for the mechanistic explanation, which is plausible and analogous to known constructions but not proved here.

Predecessors: this session's exchange with the auditor thread on divisor-count dynamics (gap-prediction nulls, the `log lcm = ψ` identity — v13.895) and the positivity-knife-edge work (v13.894, v13.896). This entry is **unrelated** to that positivity program — it is a standalone observation about the classical distribution of primes relative to highly divisible numbers, surfaced while visualizing composite-accumulation vs. divisor-accumulation between primes.

## Origin

In conversation, the project owner proposed several versions of "does divisor-count behavior predict prime gaps," all of which tested null (see below). While visualizing composite-count vs. divisor-count accumulation between primes (a chart of both running totals, resetting at each prime, `n=2..150`), the owner noticed that the sharp divisor-accumulation spikes line up with highly composite numbers (HC numbers: 60, 120, 720, ...), and asked whether that's meaningful. It is — but only in the extreme tail, not as a general trend.

## 1. The general claim tested null (context, already established in chat before this entry)

Across ~149,000 prime gaps up to `N=2,000,000`: correlation between a gap's length and the divisor count of the first composite after the starting prime, `corr(gap, d(p+1)) = -0.0135` — no signal. Cumulative/slope statistics over the first `k=2..8` composites after a prime: all correlations in `[-0.07, +0.04]`, no trend with `k`. Prime-power presence in the first `k` composites: correlations `~0.001-0.005`. **None of these show predictive content.** This sets up why the result below is interesting: it isn't a restatement of something already shown to work.

## 2. Highly composite numbers DO sit in longer-than-local-average gaps [N]

For each of the 38 highly composite numbers (HC: `d(m) > d(k)` for all `k<m`) up to `N=2,000,000` — `1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440` — I found its enclosing prime gap `g_m` (the gap between the primes bracketing it) and compared `g_m` to the mean and std of prime gaps in a local window of ±200 primes around `m` (controlling for the fact that gaps naturally grow with `n`, roughly like `log n`).

**Result:** mean z-score across the 38 HC numbers = **+0.677** (0 = no tendency), mean local percentile = **69.8%** (50% = typical). HC numbers systematically sit toward the long end of their local gap distribution, not at the median. Individual numbers vary a lot — some (7560, 55440, 110880) actually sit in short gaps (`gap=2`, z≈-1.1) — but the average tilt across all 38 is clear and consistent in direction.

## 3. The effect is real but entirely tail-concentrated — the broad/bulk version is null [N]

To check whether this is a general "more divisors → longer gap" trend (which would contradict §1) or specific to extreme divisor-count record-setters, I ran the same comparison across **every** `n` from 4 to 2,000,000 (`~2×10^6` points), using partial correlation to remove the shared `log n` trend from both `d(n)` and the enclosing gap:

- **Partial correlation, all n:** `corr(d(n), gap | log n) = -0.0051` — essentially zero. For a typical number, having a somewhat-above-average divisor count tells you nothing about its enclosing gap. This is consistent with, not a contradiction of, §1's null results.
- **Top 1% by `d(n)` (`d(n)≥80`, n=23,378 points):** mean gap-residual (gap length minus the local-`log n`-predicted baseline) = **+0.079** — barely above zero, essentially still noise.
- **Top 0.1% by `d(n)` (`d(n)≥144`, n=2,771 points):** mean gap-residual = **+1.498** — a sharp jump, an order of magnitude larger than the top-1% figure, confirming the effect only emerges deep in the tail.

**So the correct statement of the finding is specific, not general:** divisor count does not predict gap length in any graded, continuous sense — it's flat for the bulk of the distribution and only slightly elevated at the 99th percentile. The real effect lives almost entirely in the most extreme divisor-count record-setters (HC numbers and their near-neighbors), which is a much narrower and more specific claim than "divisor accumulation rate indicates gap length."

## 4. Plausible mechanism [I]/[O], not proved here

A highly composite number like `720720 = 2^4·3^2·5·7·11·13` carries an unusually large *set* of distinct small prime factors. Numbers in its immediate neighborhood are correspondingly more likely to share one of those small factors (be even, or a multiple of 3, 5, 7, ...), which locally suppresses the chance of primality nearby — the same mechanism behind the classical guaranteed-composite run `n!+2, n!+3, \ldots, n!+n`, just occurring naturally and more softly around HC numbers rather than being forced by construction. This is offered as a plausible qualitative explanation for why the tail effect exists and why it doesn't generalize to merely-above-average `d(n)` (which doesn't carry enough concentrated small-prime structure to matter) — not a proof, and not attempted as one here.

## What this is not

- **Not predictive in real time.** Knowing in advance that a number *will turn out to be* an HC-type record-setter is itself as hard as knowing its full factorization; this is a structural/statistical fact about where such numbers sit, not a forecasting tool for "is a long gap coming."
- **Not connected to the positivity program (v13.894/896) or the explicit-formula arc (v13.882-891).** This is ordinary elementary/analytic number theory about the classical gap sequence, using only `d(n)` and primes — no screw kernels, no `Λ`-weighting, no RH-adjacent machinery. Offered to the sandbox only because it was a natural side-finding from the same visualization exercise, in case it's useful background for anything gap-related in Lane A's separate work.
- **No RH/GRH claim, implicit or explicit.**

## Reproducibility

Sieve-based, `N=2,000,000`, standard trial-division-free divisor-count sieve (`d[i::i]+=1` for `i=1..N`). HC numbers generated by scanning for running maxima of `d(m)`. Local window ±200 primes for the z-score/percentile comparison in §2. Partial correlation in §3 via ordinary least-squares residuals of `d(n)` and `gap` against `log n`, then Pearson correlation of the residuals. Scripts were ad hoc (written and run directly in this conversation, not saved to the repo); the methodology above is complete enough to reproduce independently, consistent with how this session's numerical exchanges have been reported throughout.

## Synchronization

Live ledger head checked immediately before this write: v13.897 (the auditor thread's own prior round). No collision on v13.898.
