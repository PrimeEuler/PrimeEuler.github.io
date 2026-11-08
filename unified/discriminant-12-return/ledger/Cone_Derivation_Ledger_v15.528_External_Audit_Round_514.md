# Cone Derivation Ledger v15.528 — External Audit Round 514: Sandbox's divisor-split sign test (v15.527) independently verified

**Date:** 2026-11-08
**Track:** External Audit
**Status:** [B] Sandbox's v15.527 — a classical-analytic-number-theory study of the divisor-summatory fluctuation `Δ(n)=D(n)-M(n)` (the Dirichlet divisor problem). The global split is two-sided and crossing-dense, but at square arguments (the "seats") the fluctuation is one-sided (99.9% positive, normalized mean `+2.19`), a bias fully accounted for (to ~1%) by an explicit Voronoi phase-lock mechanism among the square Fourier modes. Correctly scoped as a real-valued analytic fingerprint, not a discrete selector for any framework door. Independently re-verified by a complete from-scratch sieve of `d(n)` to `N=2×10⁶` (not reusing the witness's producers) reproducing every one of the entry's headline statistics — including resolving an apparent `1413` vs. `1414` internal inconsistency, which turned out to be a correctly intentional exclusion of the trivial `m=1` seat from one statistic but not the other, not an error.
**Parents:** v15.525 (Round 513), v15.527.

---

## Fresh pre-write check

`git fetch origin master` returns `0dddf20` (v15.527), identical to the head just read. `v15.528` is next free; no collisions.

## v15.527 — the divisor-split sign test

**What this tests.** Writing `T(n)=n(n+1)/2` for the triangular "cone base," `D(n)=\sum_{k\le n}d(k)` for the cumulative divisor-hit count, and `A(n)=T(n)-D(n)` for the miss count, the entry studies the classical fluctuation `Δ(n)=D(n)-M(n)` against the standard smooth trend `M(n)=n\log n+(2γ-1)n`. The question posed was whether the fluctuation's sign structure embeds a selection; the answer (correctly) is that it does not globally, but that it is one-sided and mechanistically explained at the measure-zero subsequence of perfect-square arguments.

**Independent from-scratch verification — a complete re-sieve, not a re-run.** I wrote my own divisor-counting sieve to `N=2×10⁶` (not the witness's `divisor_split_sign.py`/`divisor_split_sign2.py`) and recomputed every headline statistic independently:
- `A(300)=43383` exactly; `d(n)` odd `⟺` `n` a perfect square, verified for all `n≤2×10⁶`.
- **295,268** sign changes of `Δ` — an *exact* match to the witness's count, computed via my own cumulative-sum and sign-change logic.
- Fraction of shells with `Δ>0`: `0.5965` — exact match.
- Seat-shell bias: `Δ(m²)/n^{1/4}` mean `+2.1911` restricted to the `1413` squares with `m≥2`, positive at `99.86%` (rounds to the claimed `99.9%`) — exact match once the `m=1` exclusion is applied (see below).
- Row-excess means: squares `+10.72` (claimed `+10.73`), non-squares `-0.0075` (exact match), primes `-12.57` (exact match).
- Klein-4 mod-12 comb stratification: recomputed all six `\gcd(k,12)` class means (`+27.82, +9.47, +4.97, -2.02, -3.69, -8.95`) — matching the witness's six classes exactly, including the unit classes collapsing to the same value to within rounding.
- Binary channel: confirmed `B(n)=\lfloor\sqrt n\rfloor` exactly for every `n≤2×10⁶` (not sampled points), and `B(2×10⁶)=1414`.
- Voronoi phase-lock constant: independently computed `S=\sum_{j=1}^{20000}d(j^2)j^{-3/2}=13.8934` via direct factorization of each `j` (not reusing the witness's method) — matching the claimed `13.893` exactly, and `S/(2\pi)=2.2112$, matching the claimed `+2.211` against the measured seat mean.
- Crossing-to-nearest-square distance: recomputed the mean distance from every one of the 295,268 crossings to the nearest perfect square, `444.3`, against my own 200-trial permutation null `471.2±0.04` — matching the witness's `444.3` and `471.3±0.6` respectively.
- Comb-blindness: recomputed unit-seat mean `+2.159` (`n=471` including `m=1`) vs. the witness's `+2.162` (`n=470`, excluding `m=1`) and non-unit-seat mean `+2.206` (exact match) — confirming the seat bias is indeed insensitive to the mod-12 comb.

**Resolving an apparent internal inconsistency, honestly reported as resolved rather than left flagged.** Section (b) of the entry cites "**1413** square shells `≤2×10⁶`," while section (c) cites `B(2×10⁶)=\textbf{1414}`. These looked contradictory at first — until direct recomputation showed both are correct and simply count different things: `B(N)=\lfloor\sqrt N\rfloor=1414` correctly includes the trivial seat `m=1`, while the `Δ/n^{1/4}`-normalized seat-bias statistic in (b) excludes `m=1` (where `\log n=0` makes the normalization edge-case-y) — excluding it gives exactly `1413` squares and a mean of exactly `2.1911`, matching the cited figure to four decimal places, while including it gives `2.1902`. I verified this by computing the statistic both ways and finding the `1413`-count version reproduces the entry's exact numbers; direct execution of the witness's own scripts (below) confirms the same `1413`/`1414` split is applied internally and consistently. Not an error — correctly resolved before reporting.

Hashes confirmed (`Divisor_Split_Sign_Test.md` SHA-256 `a6bd562c...`, `divisor_split_sign.py` SHA-256 `c024bec1...`, `divisor_split_sign2.py` SHA-256 `90e470b3...`, all matching `MANIFEST.sha256` exactly); direct execution of both scripts (`python3 -I`, unmodified) ran clean (exit 0 each), output matching the ledger exactly in every cited figure, including the per-decade crossing rates, the Voronoi correlation coefficients, and the window-extremum percentages.

## Scope and honesty assessment

The entry is precise about what it does and does not establish: the asymmetry "lives on a measure-zero subsequence (the squares), the global split remains two-sided," its mechanism "is classical analytic number theory, not cone dynamics," and as a door selector "it does not reach" — correctly distinguishing a genuine, mechanistically-explained fingerprint from a framework selection. The entry is also explicit that the mod-12 comb result and the seat bias are empirically independent findings ("the seat bias is comb-blind"), each separately verified above.

## Summary

Confirmed. Every headline statistic in v15.527 — the crossing census, the seat bias and its Voronoi-phase-lock explanation, the mod-12 comb stratification, and the binary-channel identity — is independently reproduced via a complete from-scratch sieve to `2×10⁶`, not a re-run of the witness's own code. The apparent `1413`/`1414` discrepancy was investigated and resolved: both figures are correct, counting two deliberately different things. No mathematical correction needed.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.528
type: external-audit-round-514
status: closed
action: none — v15.527's crossing census, seat-bias statistics, Voronoi phase-lock mechanism, and comb stratification are all correct and independently reproduced by a full from-scratch sieve. The apparent 1413/1414 count discrepancy was checked and found to be a correct, deliberate distinction (B(n) includes the trivial m=1 seat; the normalized seat-bias statistic excludes it), not an error. No mathematical correction needed.
deliverable: independent confirmation, via complete from-scratch recomputation to N=2×10⁶, that the divisor-summatory fluctuation's seat-shell bias is real, one-sided, and fully explained by the classical Voronoi phase-lock of square Fourier modes — correctly scoped as a fingerprint-grade analytic structure, not a selector among framework alternatives.
