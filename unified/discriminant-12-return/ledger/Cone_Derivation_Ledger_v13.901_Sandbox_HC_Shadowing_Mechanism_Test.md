# Cone Derivation Ledger v13.901 — Sandbox Mechanism Test: Small-Prime Shadowing Around HC Numbers

Date: 2026-10-01

Author: LIttle Euler (sandbox track). Authorization: project owner, 2026-10-01 ("there should be a ledger entry we can talk about on the HC side of the house"; "might as well test it first then ledger" — mechanism test run before writing, per that instruction).

Predecessors: v13.898 (auditor-thread HC gap-bias finding), v13.899 (independent verification of its headline numbers), v13.900 (auditor-thread record-gaps analysis, read in full before this write — see §4.5).

Status: **[N]** numerical throughout (independent implementation, sieve `N = 2,000,000`); **[I]/[O]** for interpretation. Nothing here touches RH/GRH or the positivity program. v13.898's firewall is respected: this entry tests its proposed mechanism, it does not connect the finding to the operator arc.

**Version note:** this entry was drafted as v13.900; the auditor thread's v13.900 (record gaps vs divisibility, read in full) landed while the mechanism test was running, so this takes v13.901 with no content change beyond the renumber and the new §4.5 engaging it.

## 1. The mechanism under test [D, restating v13.898 §4]

v13.898 proposed [I]/[O]: an HC number like `720720 = 2⁴·3²·5·7·11·13` carries an unusually large set of distinct small prime factors; numbers in its immediate neighborhood are correspondingly more likely to share one of those small factors, locally suppressing primality — the classical `n!+2,…,n!+n` mechanism occurring naturally and softly. This entry tests that mechanism quantitatively, in two versions.

Scripts: `hc_mech2.py`, `hc_mech3.py`, `hc_mech4.py` (sandbox run dir, `runs/20260930-divisor-tension/hc_mechanism/`; ad hoc but complete and re-runnable).

## 2. Test 1 — generic small-prime roughness in ±100 windows: null-ish [N]

For each HC number `m ≥ 5040` (22 numbers; smaller HC lack clean log-matched controls), measured the fraction of integers in `[m−100, m+100]` coprime to `2·3·5·7·11·13`, versus the mean over a 40,000-point log-uniform control pool (centers `≥ 2000`, `> 300` from any HC), matched within `±0.12` in `log m`.

- Mean rough density, HC windows: **0.1904**; matched controls: **0.1919**.
- Mean deficit (control − HC): **0.0015 ± 0.0069**, t = 1.05, n = 22 — not significant.
- corr(deficit, gap z-score) = **0.10** — no within-HC relationship.
- Bulk check (1990 typical numbers): corr(rough density, gap residual) = **−0.059** — no graded trend in the bulk, consistent with v13.898 §1/§3.

**Reading [I]:** the naive version of the mechanism — "HC neighborhoods contain fewer small-prime-rough integers in general" — does not show up. Generic roughness is dominated by the prime 2 (universal), which washes out the HC-specific signal.

## 3. Test 2 — own-factor shadowing: the mechanism's first step confirmed, its gradient absent [N]

The stated mechanism is sharper than Test 1: neighbors share one of the HC number's *own* small factors. For each HC `m ≥ 5040`, with `S(m)` = odd prime factors of `m`, measured the fraction of `[m−100, m+100] \ {m}` divisible by some `p ∈ S(m)` ("shadow fraction"), and the same own-factor quantity for 300 typical numbers.

- **HC neighborhoods: mean shadow fraction 0.58** (0.55 / 0.59 / 0.62 for 3 / 4 / 5 odd prime factors — nearly constant within factor-count groups).
- **Typical numbers: mean 0.20.**
- The shadowing is real and **~3× background** — the mechanism's first step (HC neighborhoods are far more small-factor-shadowed than typical neighborhoods) is quantitatively confirmed.
- **But corr(shadow fraction, gap z-score) = 0.13** across the 22 HC numbers, whose z-scores range from −1.15 to 3.17 while shadow fraction barely moves. There is no within-tail gradient: shadowing does not predict *which* HC number sits in the longest gap.

## 4. Interpretation [I]/[O]

The two tests jointly sharpen v13.898's "specific, not general" framing into a mechanism-level statement:

- **Shadowing is a level effect, not a graded predictor.** HC neighborhoods are deeply and uniformly shadowed (~3× typical); that uniform background is consistent with *why the tail differs from the bulk* (v13.898's +0.677 z-tilt), while its near-constancy across HC numbers is consistent with *why nothing in the bulk or the 99th percentile predicts gaps*. The mechanism explains the level shift, not the within-tail variance.
- **Statistical weight of the underlying finding [I]:** mean z-score +0.675 over 38 HC numbers ≈ 4.2σ under iid assumptions (SE ≈ 1/√38). Caveat: local ±200-prime windows of nearby HC numbers can overlap, so samples are not strictly independent; HC numbers are sparse enough that overlap is minor, but 4.2σ should be read as indicative rather than exact.
- **The rhyme, marked [O] analogy only:** this is the third sandbox result this week with the moral "the bulk is noise; the extremes carry the structure" — the Λ knife-edge (v13.896: indicator captures 96% of the lift yet lands negative), the prime-power ablation (squares and towers do the work), and now the HC tail (flat bulk, 19× jump at the 99.9th percentile, uniform shadowing background). Recorded as an observation about where number-theoretic structure concentrates, not as a claim of connection. No positivity-program implications are drawn.

## 5. What this is not

- **Not predictive.** Identifying a number as HC-type requires its factorization; the shadowing test likewise needs the factor set. Structural fact, not a forecasting tool.
- **Not connected to the positivity program or the explicit-formula arc.** Ordinary sieve statistics about the classical gap sequence. The firewall stands.
- **No RH/GRH claim, implicit or explicit.**
- The within-tail variance of HC gap z-scores (−1.15 to 3.17 at near-constant shadowing) remains unexplained — an open descriptive question, not pursued here.

### 4.5 Relation to the auditor's v13.900 (read in full before this write)

v13.900's §3 control — that "longer gap ⟺ bigger max d(n)" is mostly an order-statistics artifact (more composites, bigger max), with a genuine +3.80 (~7%) residual surviving — does not directly touch this entry's statistics, which are **fractions, not maxima**: shadow fractions (§2–3) are structurally immune to the more-draws-bigger-max artifact. The one place the caution bites is §4's ~4.2σ weight on the mean z-score: that is a mean over HC *gap lengths*, not a max over interiors, so the §3 mechanism does not apply — but the overlapping-window dependence caveat stands regardless.

Directionally the two entries agree: v13.900 §4's surviving residual ("being a maximal run bounded by two actual primes carries a little more divisibility-concentration than an arbitrary same-length stretch") is the bulk-data echo of the level effect measured in §3 above (HC neighborhoods ~3× more shadowed than typical). Two different cuts, same moral: the shadowing is a real background condition of highly divisible neighborhoods, and its explanatory power is confined to the level shift, not the variance.

## Synchronization

Live ledger head checked immediately before this write: v13.900 (auditor thread, record gaps vs divisibility — read in full). No collision on v13.901.
