# Cone Derivation Ledger v13.899 — Sandbox Independent Verification of v13.898 (HC-Number Gap Bias) + Suzuki v3 Archived

Date: 2026-10-01

Author: LIttle Euler (sandbox track). Authorization: project owner, 2026-10-01 ("lets ledger this and get V3 in the repo").

Predecessors: v13.897 (External Audit Round 129), v13.898 (Auditor-Thread HC-Numbers Local Gap Bias).

Status: **[N]** numerical throughout (independent re-implementation, no shared code with the auditor thread); **[I]/[O]** for interpretation. Nothing here touches RH/GRH or the positivity program. v13.898's own firewall is respected: this entry verifies its numbers, it does not connect them to the operator arc.

## 1. What was verified and how [N]

The auditor thread's scripts were ad hoc (not saved to the repo), so this verification was built **from scratch**: independent Python/numpy implementation, sieve-based, `N = 2,000,000`, no code shared with the auditor thread.

Method:
- Prime sieve to `N`; divisor counts `d(n)` by the `d[i::i] += 1` sieve.
- HC numbers: running maxima of `d(m)` over `1..N`.
- For each HC number `m ≥ 4` (1 and 2 excluded: degenerate enclosing gaps): enclosing prime gap `g_m` between the bracketing primes; local window of ±200 prime gaps around it; z-score `(g_m − μ)/σ` and local percentile.
- Partial correlation `corr(d(n), gap | log n)` over all `n ∈ [4, M]` (`M` = largest prime ≤ `N`, so every `n` has an enclosing gap): OLS residuals of `d(n)` and enclosing-gap length against `log n`, then Pearson correlation of the residuals.
- Tail check: top 1% and top 0.1% of `n` by `d(n)`; mean gap-residual (gap minus local-`log n` baseline) in each tail.

## 2. Results [N] — auditor's numbers reproduced

| quantity | auditor (v13.898) | this verification | match |
|---|---|---|---|
| partial corr, all n | −0.0051 | −0.0051 | exact |
| top-1% threshold / count | `d(n) ≥ 80`, 23,378 | `d(n) ≥ 80`, 23,377 | threshold exact; count off by one point |
| top-1% mean gap-residual | +0.079 | +0.079 | exact |
| top-0.1% threshold / count | `d(n) ≥ 144`, 2,771 | `d(n) ≥ 144`, 2,771 | exact |
| top-0.1% mean gap-residual | +1.498 | +1.498 | exact |
| HC numbers (≥4) mean z-score | +0.677 (38 numbers) | +0.675 (38 numbers) | within 0.003 |

The 40 running-maximum HC numbers found here are exactly the auditor's list (`1, 2, 4, …, 1441440`); restricting to `m ≥ 4` gives the 38 used in the statistics, as in v13.898.

## 3. Assessment [I]/[O]

- **The finding is verified, not merely re-read.** Every headline number in v13.898 §2–§3 reproduces from an independent implementation to the quoted precision. The one-point count difference in the top-1% bin is immaterial (threshold and residual both exact).
- **Statistical weight [I]:** mean z-score +0.675 over 38 samples is ≈ 4.2σ under iid assumptions (SE ≈ 1/√38). Caveat: local windows of nearby HC numbers can overlap, so the samples are not strictly independent; the HC numbers are sparse enough that overlap is minor, but the 4.2σ figure should be read as indicative rather than exact.
- **The shape is the finding [I]:** flat bulk (partial corr −0.0051), barely-elevated 99th percentile (+0.079), then a ~19× jump at the 99.9th percentile (+1.498). This is a tail-concentration signature, not a graded trend — consistent with v13.898's own "specific, not general" framing and its small-prime-shadowing mechanism (the `n!+2,…,n!+n` analogy, occurring naturally around HC numbers).
- **Thematic rhyme, marked as analogy only [O]:** this is the third sandbox result this week whose moral is "the bulk is noise; the extremes carry the structure" — the Λ knife-edge (v13.896: indicator captures 96% of the lift yet lands negative), the prime-power ablation (squares and prime towers do the work), and now the HC tail. No connection to the positivity program is claimed; v13.898's firewall stands. The rhyme is recorded as an observation about where number-theoretic structure concentrates, nothing more.
- **Not predictive [D, restating v13.898]:** identifying a number as HC-type requires its factorization; this remains a structural/statistical fact about the classical gap sequence, not a forecasting tool.

## 4. Housekeeping: Suzuki v3 archived [D]

v13.897 flagged that only Suzuki 2606.09096 **v2** was archived in `research-notes/`, so the auditor could not check citations keyed to v3. This entry's authorization covered the fix: **`unified/discriminant-12-return/research-notes/2606.09096v3.pdf`** (arXiv:2606.09096v3 [math.NT], 23 Sep 2026) has been added alongside `2606.09096v2.pdf`. Future audit rounds can now check both versions. (Sandbox note: the v3-specific items used in our deep read — the ξ/(ξ+ξ′) target change, the circularity admission, the Lerch bracketing, the §8.3–8.5 sign flip — are confirmed present in the archived PDF.)

## Synchronization

Live ledger head checked immediately before this write: v13.898. No collision on v13.899.
